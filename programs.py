# -*- coding: utf-8 -*-
"""CHEM 105 notes program for the TI-84 Plus CE (one program: CHEM).

Notes are organized by category. Each category is a list of lines
(or paragraphs, which get word-wrapped to the 26-character screen).
To add notes later, edit the lists below and run: python3 build.py
Blank topics show "(ADD NOTES LATER)".

Screen rules: no apostrophes, no store arrow inside text, use e⁻ for electron.
"""
import textwrap

W = 26
LATER = "  (ADD NOTES LATER)"


def wrap(par, indent=" "):
    """Word-wrap one paragraph; continuation lines get a small indent."""
    return textwrap.wrap(par, W, subsequent_indent=indent, break_on_hyphens=False) or [""]


def lines(*items):
    """Headings (start with '#') print as-is in caps; everything else wraps."""
    out = []
    for it in items:
        if it == "":
            out.append("")
        elif it.startswith("#"):
            out.append(it[1:].strip().upper())
        else:
            out.extend(wrap(it))
    return out


def pages(text_lines, back, per=9):
    """Show lines 9 per screen; ENTER goes to the next screen, then back."""
    chunks = [text_lines[i:i + per] for i in range(0, len(text_lines), per)] or [[]]
    out, n = [], len(chunks)
    for i, ch in enumerate(chunks, 1):
        out.append("ClrHome")
        for j in range(0, len(ch), 3):
            out.append("Disp " + ",".join('"%s"' % s for s in ch[j:j + 3]))
        foot = ("ENTER=NEXT %d/%d" % (i, n)) if i < n else ("ENTER=BACK %d/%d" % (i, n))
        out.append('Output(10,%d,"%s")' % (W - len(foot) + 1, foot))
        out.append("Pause")
    out.append("Goto " + back)
    return "\n".join(out)


# ------------------------------------------------------------------ NOTES

PREFIXES = [
    "SI PREFIXES (10^x)",
    "E  exa     10^18",
    "P  peta    10^15",
    "T  tera    10^12",
    "G  giga    10^9",
    "M  mega    10^6",
    "k  kilo    10^3",
    "h  hecto   10^2",
    "da deca    10^1",
    "b  BASE    10^0",
    "d  deci    10^⁻1",
    "c  centi   10^⁻2",
    "m  milli   10^⁻3",
    "μ  micro   10^⁻6",
    "n  nano    10^⁻9",
    "p  pico    10^⁻12",
    "f  femto   10^⁻15",
    "a  atto    10^⁻18",
    "b = base unit (m, g, L, s)",
    "",
    "CONVERTING:",
    "multiply by 10^(FROM-TO)",
    " ex: 5 km to m:",
    "     5×10^(3-0) = 5000 m",
    " ex: 450 nm to m:",
    "     450×10^⁻9 m",
]

QUANTUM = lines(
    "#n = principal quantum #",
    "n ≥ 1",
    "principal energy level, distance from nucleus, orbital size",
    "",
    "#l = angular momentum QN",
    "l can only be 0 to n-1",
    "sublevel, orbital type, and orbital shape",
    "",
    "#ml = magnetic QN",
    "ml = -l to +l",
    "orientation in space",
    "",
    "#NODES",
    "total nodes = n-1",
    "planar nodes = l",
    " - flat 2D slice through atomic orbital",
    "radial nodes = total - l",
    " - hollow spherical gap in between orbitals",
)

RULES = lines(
    "#I. AUFBAU PRINCIPLE",
    "Electrons are placed in lowest energy orbitals first.",
    "",
    "#II. PAULI EXCLUSION",
    "Only 2 electrons can be placed in each orbital.",
    "",
    "#III. HUNDS RULE",
    "Electrons fill all orbitals of equal energy (degenerate orbitals) singly before "
    "pairing up so all unpaired e⁻ have the same spin. It costs energy to put two "
    "electrons in the same orbital because they repel each other.",
    "",
    "#IV. OCTET RULE",
    LATER,
    "",
    "#V. LE CHATELIERS PRINCIPLE",
    LATER,
)

TRENDS = lines(
    "#GENERAL",
    "Metallic character and atomic radius increase to the LEFT and DOWN",
    "Nonmetallic character, electron affinity and ionization energy increase RIGHT and UP",
    "",
    "#ATOMIC RADIUS",
    "- Going up and right: the increased nuclear charge from an increasing number of "
    "protons pulls the e⁻ more tightly = smaller radius.",
    "- Going down: each new period adds a new e⁻ shell, which increases the overall "
    "size of the atom.",
    "- Cations (take e⁻) are smaller than their neutral atom: increased Zeff.",
    "- Anions (give e⁻) are larger than their neutral atom: same # of protons but more "
    "e⁻ to repel one another. The increased repulsion makes the e⁻ cloud expand = "
    "bigger ion.",
    "",
    "#IONIZATION ENERGY",
    "- In general IE increases across a period because Zeff increases left to right. "
    "More protons = valence e⁻ feel greater nuclear attraction, despite adding e⁻ "
    "to the same energy level.",
    "- EXCEPTIONS: N and O. N 1st IE is unusually high because it requires breaking "
    "a stable half-filled p subshell. O 2nd IE increases less than expected because "
    "it results in a stable half-filled p subshell. e⁻ configuration can sometimes "
    "override the trend.",
    "- As each e⁻ is removed, the Zeff felt by the remaining e⁻ increases.",
)

EXPERIMENTS = lines(
    "#CATHODE RAY",
    "e⁻ exist and have a charge",
    "#OIL DROP",
    "what the charge of e⁻ is",
    "#RADIOACTIVE EMISSIONS",
    "atoms have +/- subparticles",
    "#GOLD FOIL",
    "there is something in the middle (nucleus)",
    "#CHADWICK",
    "discovered neutron, atomic mass did not match count",
)

LAWS = lines(
    "#LAWS & PRINCIPLES LIST",
    "A. Law of Conservation of Mass",
    "B. Newtons Second Law of Motion",
    "C. Law of Conservation of Energy",
    "D. Law of Definite Proportions",
    "E. Archimedes Principle",
    "F. Bernoullis Principle",
)

LIGHT = [
    "LIGHT RELATIONSHIPS",
    "+ both go up together",
    "- one up, other goes down",
    "0 no effect",
    "(freq = frequency v,",
    " vel = velocity)",
    "",
    "c=λv  E=hv=hc/λ",
    " freq & E          +",
    " λ & freq          -",
    " λ & E             -",
    "λ=h/mv (DE BROGLIE)",
    " λ & m             -",
    " λ & vel           -",
    "KE=1/2mv²",
    " KE & m            +",
    " KE & vel          +",
    "KE=hv-Φ (PHOTOELECTRIC)",
    " KE & freq         +",
    " KE & E of photon  +",
    " KE & Φ            -",
    " Φ & threshold freq +",
    "INTENSITY (BRIGHTNESS)",
    " intensity & # photons +",
    " intensity & # e⁻ out  +",
    " intensity & KE of e⁻  0",
    " intensity & E/photon  0",
    " # photons & total E   +",
    "BELOW THRESHOLD FREQ:",
    " no e⁻ out, even if",
    " brighter",
]

# Element symbols Z = 1..118 (proper case for display, CAPS for matching input)
SYMS = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe', 'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Nh', 'Fl', 'Mc', 'Lv', 'Ts', 'Og']
SYM_PROPER = "".join(s.ljust(2) for s in SYMS)
SYM_CAPS = SYM_PROPER.upper()
CHARGE_TXT = "".join(c.ljust(2) for c in ["5-", "4-", "3-", "2-", "-", "", "+", "2+", "3+", "4+", "5+"])

ACCURACY = lines(
    "#ACCURATE VS PRECISE",
    LATER,
)


# ---------------------------------------------------------------- ELECTRON CONFIG
# Subshells in Aufbau (filling) order, their capacities, and 10n+l for
# "remove from highest n first (then highest l)" when making cations.
SUBSHELLS = "1s 2s 2p 3s 3p 4s 3d 4p 5s 4d 5p 6s 4f 5d 6p 7s 5f 6d 7p".split()
CAPS = [{"s": 2, "p": 6, "d": 10, "f": 14}[s[1]] for s in SUBSHELLS]
SCORE = [10 * int(s[0]) + "spdf".index(s[1]) for s in SUBSHELLS]
# Noble-gas cores: (symbol, electrons, last subshell index 1-based)
CORES = [("He", 2, 1), ("Ne", 10, 3), ("Ar", 18, 5), ("Kr", 36, 8), ("Xe", 54, 11), ("Rn", 86, 15)]
# Standard exceptions taught with Cr/Cu: one e- moves from ns to (n-1)d.
# (Z, from-index, to-index), indexes 1-based into SUBSHELLS
EXCEPTIONS = [(24, 6, 7), (29, 6, 7), (42, 9, 10), (47, 9, 10), (79, 12, 14)]


PAGE = "\n".join([
    "If V≥8",
    "Then",
    'Output(10,15,"ENTER=MORE")',
    "Pause ",
    "ClrHome",
    "0→V",
    "End",
])


def _render(start, prefix):
    """TI code: print subshells start..19 wrapped to 26 chars, paging every 9 lines."""
    return "\n".join([
        prefix + "→Str2",
        "For(I,%s,19)" % start,
        "If ʟEC(I)>0",
        "Then",
        "sub(Str6,2I-1,2)+sub(Str5,2ʟEC(I)-1,2)→Str3",
        'If sub(Str3,4,1)=" "',
        "sub(Str3,1,3)→Str3",
        "If length(Str2)+length(Str3)≥26",
        "Then",
        PAGE,
        "Disp Str2",
        "V+1→V",
        "Str3→Str2",
        "Else",
        "If length(Str2)",
        'Str2+" "→Str2',
        "Str2+Str3→Str2",
        "End",
        "End",
        "End",
        "If length(Str2)",
        "Then",
        PAGE,
        "Disp Str2",
        "V+1→V",
        "End",
    ])


CONFIG_CODE = "\n".join([
    "{" + ",".join(map(str, CAPS)) + "}→ʟCAP",
    "{" + ",".join(map(str, SCORE)) + "}→ʟSC",
    '"' + "".join(s.ljust(2) for s in SUBSHELLS) + '"→Str6',
    '"' + "".join(str(i).ljust(2) for i in range(1, 15)) + '"→Str5',
    '"' + "".join(c[0] for c in CORES) + '"→Str4',
    "{" + ",".join(str(c[1]) for c in CORES) + "}→ʟCE",
    "{" + ",".join(str(c[2]) for c in CORES) + "}→ʟCI",
    # fill: cations start from the neutral atom
    "N→R",
    "If C>0",
    "Z→R",
    "19→dim(ʟEC)",
    "Fill(0,ʟEC)",
    "For(I,1,19)",
    "min(R,ʟCAP(I))→ʟEC(I)",
    "R-ʟEC(I)→R",
    "End",
    "0→X",
] + sum([[
    "If C≥0 and Z=%d" % z,
    "Then",
    "ʟEC(%d)-1→ʟEC(%d)" % (a, a),
    "ʟEC(%d)+1→ʟEC(%d)" % (b, b),
    "1→X",
    "End",
] for z, a, b in EXCEPTIONS], []) + [
    # cations: remove from highest n (then highest l)
    "If C>0",
    "Then",
    "For(J,1,C)",
    "0→B",
    "0→D",
    "For(I,1,19)",
    "If ʟEC(I)>0 and ʟSC(I)>B",
    "Then",
    "ʟSC(I)→B",
    "I→D",
    "End",
    "End",
    "ʟEC(D)-1→ʟEC(D)",
    "End",
    "End",
    # noble-gas core
    "0→P",
    "For(K,1,6)",
    "1→F",
    "For(I,1,ʟCI(K))",
    "If ʟEC(I)≠ʟCAP(I)",
    "0→F",
    "End",
    "If F and (ʟCE(K)<N or (C≠0 and ʟCE(K)≤N))",
    "K→P",
    "End",
    # header
    "ClrHome",
    "sub(Str8,2Z-1,2)→Str2",
    'Disp Str2+" CHARGE:"',
    "Output(1,12,C)",
    'Disp "e⁻ COUNT:"',
    "Output(2,11,N)",
    "2→V",
    "If X and C=0",
    "Then",
    'Disp "(EXCEPTION: ns TO d)"',
    "V+1→V",
    "End",
    'Disp "FULL:"',
    "V+1→V",
    _render("1", '""'),
    PAGE,
    'Disp "CONDENSED:"',
    "V+1→V",
    "If P",
    "Then",
    _render("ʟCI(P)+1", '"["+sub(Str4,2P-1,2)+"]"'),
    "Else",
    PAGE,
    'Disp "(SAME AS FULL)"',
    "End",
    'Output(10,15,"ENTER=BACK")',
    "Pause ",
    "Goto M",
])

# ------------------------------------------------------------------ PROGRAM

PROGRAMS = {}
PROGRAMS["CHEM"] = r'''
Lbl 0
Menu("CHEM 105 NOTES","PREFIXES 10^x k μ n",A,"QUANTUM #S & NODES",B,"e⁻ RULES/PRINCIPLES",C,"PERIODIC TRENDS",D,"EXPERIMENTS",E,"MORE ►",M,"QUIT",Q)
Lbl M
Menu("MORE NOTES","LAWS LIST A-F",F,"LIGHT RELATIONSHIPS",G,"ISOELECTRONIC LIST",H,"ELECTRON CONFIG",J,"ACCURATE VS PRECISE",I,"◄ BACK",0)
Lbl Q
ClrHome
Stop
Lbl H
1→Y
Goto S0
Lbl J
2→Y
Lbl S0
"''' + SYM_CAPS + '''"→Str9
"''' + SYM_PROPER + '''"→Str8
"''' + CHARGE_TXT + '''"→Str7
ClrHome
If Y=1
Disp "ISOELECTRONIC LIST"
If Y=2
Disp "ELECTRON CONFIG"
Disp "TYPE SYMBOL (NA OR Na)"
Input "SYMBOL:",Str1
If length(Str1)=1
Str1+" "→Str1
0→Z
For(J,1,118)
If sub(Str9,2J-1,2)=Str1 or sub(Str8,2J-1,2)=Str1
J→Z
End
If not(Z)
Goto H8
Disp "CHARGE: 0 IF NEUTRAL","USE (-) KEY FOR NEG"
Input "CHARGE:",C
Z-C→N
If N<1
Goto H9
If Y=2
Goto J0
ClrHome
Disp "SAME # OF e⁻:","(CHARGES -5 TO +5)"
Output(1,15,N)
0→R
For(K,N-5,N+5)
If K≥1 and K≤118
Then
sub(Str8,2K-1,2)→Str2
If sub(Str2,2,1)=" "
sub(Str2,1,1)→Str2
Str2+sub(Str7,2(K-N)+11,2)→Str2
If K=Z
Str2+" ◄"→Str2
R+1→R
If R≤6
Output(2+R,2,Str2)
If R>6
Output(R-4,14,Str2)
End
End
Output(10,17,"ENTER=BACK")
Pause
Goto M
Lbl H8
Disp "SYMBOL NOT FOUND"
Pause
Goto S0
Lbl H9
Disp "THAT LEAVES 0 e⁻"
Pause
Goto S0
Lbl J0
''' + CONFIG_CODE + r'''
''' + "\n".join(
    "Lbl %s\n%s" % (lbl, pages(txt, back))
    for lbl, txt, back in [
        ("A", PREFIXES, "0"), ("B", QUANTUM, "0"), ("C", RULES, "0"),
        ("D", TRENDS, "0"), ("E", EXPERIMENTS, "0"),
        ("F", LAWS, "M"), ("G", LIGHT, "M"), ("I", ACCURACY, "M"),
    ]
) + "\n"
