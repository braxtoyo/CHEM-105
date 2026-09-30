# -*- coding: utf-8 -*-
"""Build .8xp files (and readable .txt source) from programs.py.

Usage:  python3 build.py
Needs:  pip install tivars
"""
import os
import re
import sys

from tivars.types import TIProgram
from tivars.models import TI_84PCE

from programs import PROGRAMS

HERE = os.path.dirname(os.path.abspath(__file__))
OUT8 = os.path.join(HERE, "8xp")
OUTT = os.path.join(HERE, "src")
TOK = TI_84PCE.tokens.bytes
TWO_BYTE = {0x5C, 0x5D, 0x5E, 0x60, 0x61, 0x62, 0x63, 0x7E, 0xAA, 0xBB, 0xEF}
STR_RE = re.compile(r'"([^"\n]*)"')


def prep(src):
    """π must be written 'pi' in code and '|π' inside strings for tivars."""
    out = []
    for line in src.strip("\n").split("\n"):
        parts = line.split('"')
        for i in range(len(parts)):
            if i % 2:  # inside a string
                parts[i] = parts[i].replace("π", "|π")
            else:
                parts[i] = parts[i].replace("π", "pi")
        ln = '"'.join(parts)
        if ln.strip() == "Pause":  # token is "Pause " (with space)
            ln = "Pause "
        out.append(ln)
    return "\n".join(out)


def tokens_of(text):
    p = TIProgram(name="X")
    p.load_string(prep('"' + text + '"'))
    data = bytes(p.data)[1:]
    toks, i = [], 0
    while i < len(data):
        n = 2 if data[i] in TWO_BYTE else 1
        toks.append(TOK[data[i:i + n]].langs["en"].display)
        i += n
    if toks and toks[-1] == '"':
        toks.pop()
    return toks


def width(text):
    return sum(1 for _ in tokens_of(text))  # one glyph per token (approx.)


def check(name, src):
    probs = []
    for ln, line in enumerate(src.strip("\n").split("\n"), 1):
        s = line.strip()
        lits = STR_RE.findall(s)
        if "→" in "".join(lits):
            probs.append((ln, "store arrow inside string", s))
        for lit in lits:
            toks = tokens_of(lit)
            multi = [t for t in toks if len(t) > 1 and t not in ("√(", "⁻¹", "₁₀")]
            if multi:
                probs.append((ln, "word token in string %r" % multi, lit))
        if s.startswith("Menu("):
            for k, lit in enumerate(lits):
                w = width(lit)
                lim = 24 if k == 0 else 22
                if w > lim:
                    probs.append((ln, "menu text %d>%d" % (w, lim), lit))
            if len(lits) > 8:
                probs.append((ln, "too many menu items", s))
        elif s.startswith("Disp") or (s.startswith("Output(") and "sub(" not in s):
            for lit in lits:
                if width(lit) > 26:
                    probs.append((ln, "disp text %d>26" % width(lit), lit))
        elif s.startswith("Input"):
            for lit in lits:
                if width(lit) > 20:
                    probs.append((ln, "prompt %d>20" % width(lit), lit))
    # labels and Goto/Menu targets must be 1-2 characters
    for ln, line in enumerate(src.strip("\n").split("\n"), 1):
        s = line.strip()
        for lab in re.findall(r"^(?:Lbl|Goto) (\S+)$", s):
            if len(lab) > 2:
                probs.append((ln, "label longer than 2 characters", s))
        if s.startswith("Menu("):
            for lab in re.sub(r'"[^"]*"', "", s[5:-1]).split(",")[1:]:
                if lab and len(lab) > 2:
                    probs.append((ln, "menu label longer than 2 characters", lab))
    # Output( column + length must fit
    for ln, line in enumerate(src.strip("\n").split("\n"), 1):
        m = re.match(r'Output\((\d+),(\d+),"([^"]*)"\)', line.strip())
        if m and int(m.group(2)) - 1 + width(m.group(3)) > 26:
            probs.append((ln, "Output overflows", line))
    return probs


def letter_runs(p):
    """Flag commands that got spelled out as letters instead of tokens."""
    d = bytes(p.data)
    toks, i = [], 0
    while i < len(d):
        n = 2 if d[i] in TWO_BYTE else 1
        toks.append((d[i:i + n], TOK[d[i:i + n]].langs["en"].display))
        i += n
    probs, inq, run, ln, prev = [], False, "", 1, ""
    for b, t in toks + [(b"\x3f", "\n")]:
        if not run:
            before = prev
        prev = t
        if b == b"\x3f":
            inq = False
        if t == '"':
            inq = not inq
        if not inq and len(t) == 1 and t.isalpha():
            run += t
            continue
        if len(run) >= 3 and before != "prgm" and not run.startswith("ʟ"):
            probs.append((ln, "command spelled as letters", run))
        run = ""
        if b == b"\x3f":
            ln += 1
    return probs


def main():
    os.makedirs(OUT8, exist_ok=True)
    os.makedirs(OUTT, exist_ok=True)
    bad = False
    for name, src in PROGRAMS.items():
        body = src.strip("\n")
        p = TIProgram(name=name)
        p.load_string(prep(body), model=TI_84PCE)
        p.save(os.path.join(OUT8, name + ".8xp"))
        with open(os.path.join(OUTT, name + ".txt"), "w", encoding="utf-8") as f:
            f.write(p.string() + "\n")
        probs = check(name, body) + letter_runs(p)
        print("%-8s %6d bytes  %4d lines  %d issues" % (name, len(p.data), body.count("\n") + 1, len(probs)))
        for pr in probs:
            bad = True
            print("   line %d: %s: %s" % pr)
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
