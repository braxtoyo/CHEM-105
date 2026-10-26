# Minimal TI-BASIC interpreter for testing the generated programs (subset).
import re, math

TOKRE = re.compile(r'''
 (?P<str>"[^"\n→]*"?)
|(?P<num>(?:\d+\.?\d*|\.\d+)(?:ᴇ⁻?\d+)?)
|(?P<sci>ᴇ⁻?\d+)
|(?P<func>(?:sub|inString|length|int|fPart|abs|min|max|round|not|dim|iPart|remainder|log|sum)\()
|(?P<strv>Str\d)
|(?P<list>ʟ[A-Zθ0-9]+)
|(?P<op>≠|≤|≥|=|<|>|\+|-|\*|/|\^|⁻|\(|\)|,|\{|\})
|(?P<kw>\ and\ |\ or\ |\ xor\ )
|(?P<var>[A-Zθ])
|(?P<sp>\s+)
''', re.X)


def tokenize(s):
    out, i = [], 0
    while i < len(s):
        m = TOKRE.match(s, i)
        if not m:
            raise SyntaxError("tok at %r" % s[i:])
        i = m.end()
        k = m.lastgroup
        if k == 'sp':
            continue
        v = m.group(k)
        if k == 'kw':
            v = v.strip()
        if k == 'str':
            v = v[1:-1] if v.endswith('"') and len(v) > 1 else v[1:]
        out.append((k, v))
    return out


class Parser:
    def __init__(s, toks, env):
        s.t, s.i, s.env = toks, 0, env

    def peek(s):
        return s.t[s.i] if s.i < len(s.t) else (None, None)

    def take(s):
        s.i += 1
        return s.t[s.i - 1]

    def expect(s, v):
        k, x = s.take()
        if x != v:
            raise SyntaxError("expected %s got %s" % (v, x))

    def parse(s):
        return s.orx()

    def orx(s):
        a = s.andx()
        while s.peek() in (('kw', 'or'), ('kw', 'xor')):
            op = s.take()[1]
            b = s.andx()
            a = float(bool(a) or bool(b)) if op == 'or' else float(bool(a) != bool(b))
        return a

    def andx(s):
        a = s.cmp()
        while s.peek() == ('kw', 'and'):
            s.take()
            b = s.cmp()
            a = float(bool(a) and bool(b))
        return a

    def cmp(s):
        a = s.add()
        while s.peek()[1] in ('=', '≠', '<', '>', '≤', '≥') and s.peek()[0] == 'op':
            op = s.take()[1]
            b = s.add()
            a = float({'=': a == b, '≠': a != b, '<': a < b, '>': a > b, '≤': a <= b, '≥': a >= b}[op])
        return a

    def add(s):
        a = s.mul()
        while s.peek()[1] in ('+', '-') and s.peek()[0] == 'op':
            op = s.take()[1]
            b = s.mul()
            if op == '+':
                a = a + b
            else:
                a = a - b
        return a

    def starts_primary(s):
        k, v = s.peek()
        return k in ('num', 'func', 'strv', 'list', 'var', 'str') or (k == 'op' and v in ('(', '{', '⁻'))

    def mul(s):
        a = s.unary()
        while True:
            k, v = s.peek()
            if k == 'op' and v in ('*', '/'):
                s.take()
                b = s.unary()
                a = a * b if v == '*' else a / b
            elif s.starts_primary() and not (k == 'op' and v == '⁻'):
                a = a * s.unary()
            else:
                return a

    def unary(s):
        if s.peek() == ('op', '⁻'):
            s.take()
            return -s.unary()
        return s.power()

    def power(s):
        a = s.primary()
        while s.peek() == ('op', '^'):
            s.take()
            a = a ** s.unary()
        return a

    def args(s):
        out = [s.parse()]
        while s.peek() == ('op', ','):
            s.take()
            out.append(s.parse())
        if s.peek() == ('op', ')'):
            s.take()
        return out

    def primary(s):
        k, v = s.take()
        e = s.env
        if k == 'num':
            x = float(v.replace('ᴇ⁻', 'e-').replace('ᴇ', 'e'))
            if s.peek()[0] == 'sci':
                x *= 10 ** float(s.take()[1][1:].replace('⁻', '-'))
            return x
        if k == 'str':
            return v
        if k == 'strv':
            return e.strs[v]
        if k == 'var':
            return e.vars.get(v, 0.0)
        if k == 'list':
            lst = e.lists[v]
            if s.peek() == ('op', '('):
                s.take()
                idx = s.parse()
                if s.peek() == ('op', ')'):
                    s.take()
                i = int(idx)
                if i < 1 or i > len(lst) or idx != i:
                    raise IndexError("bad list index %s %s" % (v, idx))
                return lst[i - 1]
            return list(lst)
        if k == 'op' and v == '(':
            x = s.parse()
            if s.peek() == ('op', ')'):
                s.take()
            return x
        if k == 'op' and v == '{':
            items = [s.parse()]
            while s.peek() == ('op', ','):
                s.take()
                items.append(s.parse())
            if s.peek() == ('op', '}'):
                s.take()
            return items
        if k == 'func':
            f = v[:-1]
            a = s.args()
            if f == 'sub':
                st, p, n = a
                p, n = int(p), int(n)
                if p < 1 or n < 1 or p + n - 1 > len(st):
                    raise IndexError("sub( out of range %r %d %d" % (st, p, n))
                return st[p - 1:p - 1 + n]
            if f == 'inString':
                return float(a[0].find(a[1]) + 1)
            if f == 'length':
                return float(len(a[0]))
            if f == 'int':
                return float(math.floor(a[0]))
            if f == 'fPart':
                return a[0] - math.trunc(a[0])
            if f == 'abs':
                return abs(a[0])
            if f == 'min':
                return min(a)
            if f == 'max':
                return max(a)
            if f == 'round':
                return float(round(a[0], int(a[1])))
            if f == 'log':
                return math.log10(a[0])
            if f == 'sum':
                return float(sum(a[0]))
            if f == 'not':
                return float(not a[0])
            if f == 'dim':
                return float(len(a[0]))
        raise SyntaxError("primary %s %s" % (k, v))


class Env:
    def __init__(s):
        s.vars, s.strs, s.lists = {}, {}, {}


def ev(expr, env):
    p = Parser(tokenize(expr), env)
    v = p.parse()
    if p.i != len(p.t):
        raise SyntaxError("trailing in %r at %r" % (expr, p.t[p.i:]))
    return v


class Halt(Exception):
    pass


def run(progs, name, env, inputs, menus, screen, maxsteps=3_000_000):
    lines = progs[name].split("\n")
    labels = {l[4:]: i for i, l in enumerate(lines) if l.startswith("Lbl ")}
    pc, stack, steps = 0, [], 0

    def skip_block(pc, allow_else):
        depth = 0
        while True:
            pc += 1
            l = lines[pc]
            if l == "Then" or l.startswith("For(") or l.startswith("While "):
                depth += 1
            elif l == "End":
                if depth == 0:
                    return pc
                depth -= 1
            elif l == "Else" and depth == 0 and allow_else:
                return pc

    while pc < len(lines):
        steps += 1
        if steps > maxsteps:
            raise RuntimeError("too many steps")
        l = lines[pc].strip()
        if l.startswith("If "):
            c = ev(l[3:], env)
            if pc + 1 < len(lines) and lines[pc + 1] == "Then":
                if c:
                    stack.append(("if", pc))
                    pc += 2
                else:
                    j = skip_block(pc + 1, True)
                    if lines[j] == "Else":
                        stack.append(("if", j))
                    pc = j + 1
            else:
                pc += 1 if c else 2
            continue
        if l == "Else":  # reached end of true branch
            stack.pop()
            pc = skip_block(pc, False) + 1
            continue
        if l == "End":
            kind, info = stack[-1]
            if kind == "if":
                stack.pop()
                pc += 1
            elif kind == "for":
                var, end, start = info
                env.vars[var] += 1
                if env.vars[var] <= end:
                    pc = start + 1
                else:
                    stack.pop()
                    pc += 1
            elif kind == "while":
                start = info
                if ev(lines[start][6:], env):
                    pc = start + 1
                else:
                    stack.pop()
                    pc += 1
            continue
        if l.startswith("For("):
            inner = l[4:].rstrip(")")
            parts = split_args(inner)
            var = parts[0]
            a, b = ev(parts[1], env), ev(parts[2], env)
            env.vars[var] = a
            if a <= b:
                stack.append(("for", (var, b, pc)))
                pc += 1
            else:
                pc = skip_block(pc, False) + 1
            continue
        if l.startswith("While "):
            if ev(l[6:], env):
                stack.append(("while", pc))
                pc += 1
            else:
                pc = skip_block(pc, False) + 1
            continue
        if l.startswith("Lbl ") or l in ("ClrHome",):
            if l == "ClrHome":
                screen.append("----")
            pc += 1
            continue
        if l.startswith("Goto "):
            pc = labels[l[5:]]
            continue
        if l.startswith("Disp "):
            for a in split_args(l[5:]):
                v = ev(a, env)
                if isinstance(v, str) and len(v) > 26:
                    screen.append("!!TOO WIDE!! " + v)
                screen.append(v if isinstance(v, str) else fmt(v))
            pc += 1
            continue
        if l.startswith("Output("):
            a = split_args(l[7:-1])
            screen.append("[out r%d c%d] %s" % (int(ev(a[0], env)), int(ev(a[1], env)), ev(a[2], env)))
            pc += 1
            continue
        if l.startswith("Pause"):
            screen.append("[pause]")
            pc += 1
            continue
        if l.startswith("Input "):
            prompt, var = split_args(l[6:])
            val = inputs.pop(0)
            if var.startswith("Str"):
                env.strs[var] = val
            else:
                env.vars[var] = ev(val, env)
            pc += 1
            continue
        if l.startswith("Menu("):
            a = split_args(l[5:-1])
            if not menus:
                raise Halt()
            choice = menus.pop(0)
            pc = labels[a[2 * choice]]
            continue
        if l.startswith("prgm"):
            run(progs, l[4:], env, inputs, menus, screen)
            pc += 1
            continue
        if l == "Return":
            return
        if l == "Stop":
            raise Halt()
        if l.startswith("DelVar "):
            pc += 1
            continue
        if l.startswith("Fill("):
            v, lst = split_args(l[5:].rstrip(")"))
            env.lists[lst] = [ev(v, env)] * len(env.lists[lst])
            pc += 1
            continue
        if "→" in l:
            expr, tgt = l.rsplit("→", 1)
            if tgt.startswith("dim("):
                lst = tgt[4:].rstrip(")")
                n = int(ev(expr, env))
                cur = env.lists.get(lst, [])
                env.lists[lst] = (cur + [0.0] * n)[:n]
            else:
                v = ev(expr, env)
                m = re.match(r"(ʟ[A-Zθ0-9]+)\((.*)\)$", tgt)
                if m:
                    lst = env.lists[m.group(1)]
                    i = int(ev(m.group(2), env))
                    if i == len(lst) + 1:
                        lst.append(v)
                    elif 1 <= i <= len(lst):
                        lst[i - 1] = v
                    else:
                        raise IndexError("store idx")
                elif tgt.startswith("ʟ"):
                    env.lists[tgt] = list(v)
                elif tgt.startswith("Str"):
                    env.strs[tgt] = v
                else:
                    env.vars[tgt] = v
            pc += 1
            continue
        raise SyntaxError("unknown line %r" % l)


def fmt(v):
    return str(int(v)) if v == int(v) else str(v)


def split_args(s):
    out, depth, cur, inq = [], 0, "", False
    for ch in s:
        if ch == '"':
            inq = not inq
        if not inq and ch in "({":
            depth += 1
        if not inq and ch in ")}":
            depth -= 1
        if ch == "," and depth == 0 and not inq:
            out.append(cur)
            cur = ""
        else:
            cur += ch
    out.append(cur)
    return out
