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
SYMS = """H He Li Be B C N O F Ne Na Mg Al Si P S Cl Ar K Ca Sc Ti V Cr Mn Fe Co Ni Cu Zn
Ga Ge As Se Br Kr Rb Sr Y Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I Xe Cs Ba La Ce Pr Nd
Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu Hf Ta W Re Os Ir Pt Au Hg Tl Pb Bi Po At Rn Fr Ra Ac Th
Pa U Np Pu Am Cm Bk Cf Es Fm Md No Lr Rf Db Sg Bh Hs Mt Ds Rg Cn Nh Fl Mc Lv Ts Og""".split()
assert len(SYMS) == 118
SYM_PROPER = "".join(s.ljust(2) for s in SYMS)
SYM_CAPS = SYM_PROPER.upper()

# Known monatomic ions (standard general-chemistry ion tables). Hypothetical
# ions (e.g. B5-, C4-, Ne2+) are NOT listed, so the isoelectronic list only
# shows neutral atoms plus these ions.
KNOWN_IONS = {
    "H": [1, -1], "Li": [1], "Na": [1], "K": [1], "Rb": [1], "Cs": [1], "Fr": [1],
    "Be": [2], "Mg": [2], "Ca": [2], "Sr": [2], "Ba": [2], "Ra": [2],
    "Al": [3], "Ga": [3], "In": [1, 3], "Tl": [1, 3],
    "Sn": [2, 4], "Pb": [2, 4], "Sb": [3], "Bi": [3],
    "N": [-3], "P": [-3], "As": [-3],
    "O": [-2], "S": [-2], "Se": [-2], "Te": [-2],
    "F": [-1], "Cl": [-1], "Br": [-1], "I": [-1],
    "Sc": [3], "Ti": [2, 3, 4], "V": [2, 3], "Cr": [2, 3], "Mn": [2, 3], "Fe": [2, 3],
    "Co": [2, 3], "Ni": [2], "Cu": [1, 2], "Zn": [2],
    "Y": [3], "Zr": [4], "Ru": [2, 3], "Rh": [3], "Pd": [2], "Ag": [1], "Cd": [2],
    "Hf": [4], "Ir": [3], "Pt": [2, 4], "Au": [1, 3], "Hg": [2],
    "La": [3], "Ce": [3, 4], "Pr": [3], "Nd": [3], "Pm": [3], "Sm": [2, 3], "Eu": [2, 3],
    "Gd": [3], "Tb": [3], "Dy": [3], "Ho": [3], "Er": [3], "Tm": [3], "Yb": [2, 3], "Lu": [3],
    "Ac": [3], "Th": [4], "U": [3, 4], "Np": [3, 4], "Pu": [3, 4], "Am": [3], "Cm": [3],
}
SPECIES = sorted([(z, 0) for z in range(1, 119)] +
                 [(SYMS.index(s) + 1, q) for s, qs in KNOWN_IONS.items() for q in qs])
CHG = ["3-", "2-", "-", "", "+", "2+", "3+", "4+"]          # charges -3..+4
CHARGE_TXT = "".join(c.ljust(2) for c in CHG)
assert all(-3 <= q <= 4 for _, q in SPECIES)

ACCURACY = lines(
    "#ACCURATE VS PRECISE",
    LATER,
)


# ---------------------------------------------------------------- ELECTRON CONFIG
# Subshells in Aufbau (filling) order; capacities; 10n+l score.
SUBSHELLS = "1s 2s 2p 3s 3p 4s 3d 4p 5s 4d 5p 6s 4f 5d 6p 7s 5f 6d 7p".split()
CAPS = [{"s": 2, "p": 6, "d": 10, "f": 14}[s[1]] for s in SUBSHELLS]
SCORE = [10 * int(s[0]) + "spdf".index(s[1]) for s in SUBSHELLS]
# Display order: by n, then l (s, p, d, f)
ORDER = sorted(range(1, 20), key=lambda i: SCORE[i - 1])
# Noble-gas cores: (symbol, electrons, last Aufbau index)
CORES = [("He", 2, 1), ("Ne", 10, 3), ("Ar", 18, 5), ("Kr", 36, 8), ("Xe", 54, 11), ("Rn", 86, 15)]
# ALL measured ground-state exceptions to Aufbau for Z <= 103:
# (Z, from Aufbau index, to Aufbau index, # of e- moved)
EXCEPTIONS = [
    (24, 6, 7, 1),    # Cr  [Ar] 3d5 4s1
    (29, 6, 7, 1),    # Cu  [Ar] 3d10 4s1
    (41, 9, 10, 1),   # Nb  [Kr] 4d4 5s1
    (42, 9, 10, 1),   # Mo  [Kr] 4d5 5s1
    (44, 9, 10, 1),   # Ru  [Kr] 4d7 5s1
    (45, 9, 10, 1),   # Rh  [Kr] 4d8 5s1
    (46, 9, 10, 2),   # Pd  [Kr] 4d10
    (47, 9, 10, 1),   # Ag  [Kr] 4d10 5s1
    (57, 13, 14, 1),  # La  [Xe] 5d1 6s2
    (58, 13, 14, 1),  # Ce  [Xe] 4f1 5d1 6s2
    (64, 13, 14, 1),  # Gd  [Xe] 4f7 5d1 6s2
    (78, 12, 14, 1),  # Pt  [Xe] 4f14 5d9 6s1
    (79, 12, 14, 1),  # Au  [Xe] 4f14 5d10 6s1
    (89, 17, 18, 1),  # Ac  [Rn] 6d1 7s2
    (90, 17, 18, 2),  # Th  [Rn] 6d2 7s2
    (91, 17, 18, 1),  # Pa  [Rn] 5f2 6d1 7s2
    (92, 17, 18, 1),  # U   [Rn] 5f3 6d1 7s2
    (93, 17, 18, 1),  # Np  [Rn] 5f4 6d1 7s2
    (96, 17, 18, 1),  # Cm  [Rn] 5f7 6d1 7s2
    (103, 18, 19, 1), # Lr  [Rn] 5f14 7s2 7p1
]

PAGE = "\n".join([
    "If V≥8",
    "Then",
    'Output(10,15,"ENTER=MORE")',
    "Pause ",
    "ClrHome",
    "0→V",
    "End",
])


def _render(prefix):
    """Print filled subshells with Aufbau index > U, in n-then-l order, wrapped to 26."""
    return "\n".join([
        prefix + "→Str2",
        "For(J,1,19)",
        "ʟOR(J)→I",
        "If ʟEC(I)>0 and I>U",
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


def _tl(xs):
    return "{" + ",".join(str(x).replace("-", "⁻") for x in xs) + "}"


CONFIG_CODE = "\n".join([
    _tl(CAPS) + "→ʟCAP",
    _tl(SCORE) + "→ʟSC",
    _tl(ORDER) + "→ʟOR",
    '"' + "".join(s.ljust(2) for s in SUBSHELLS) + '"→Str6',
    '"' + "".join(str(i).ljust(2) for i in range(1, 15)) + '"→Str5',
    '"' + "".join(c[0] for c in CORES) + '"→Str4',
    _tl([c[1] for c in CORES]) + "→ʟCE",
    _tl([c[2] for c in CORES]) + "→ʟCI",
    _tl([e[0] for e in EXCEPTIONS]) + "→ʟXZ",
    _tl([e[1] for e in EXCEPTIONS]) + "→ʟXA",
    _tl([e[2] for e in EXCEPTIONS]) + "→ʟXB",
    _tl([e[3] for e in EXCEPTIONS]) + "→ʟXN",
    # fill by Aufbau (cations start from the neutral atom)
    "N→R",
    "If C>0",
    "Z→R",
    "19→dim(ʟEC)",
    "Fill(0,ʟEC)",
    "For(I,1,19)",
    "min(R,ʟCAP(I))→ʟEC(I)",
    "R-ʟEC(I)→R",
    "End",
    # known exceptions (neutral atom, and the atom a cation comes from)
    "0→X",
    "If C≥0",
    "Then",
    "For(I,1,dim(ʟXZ))",
    "If ʟXZ(I)=Z",
    "Then",
    "ʟEC(ʟXA(I))-ʟXN(I)→ʟEC(ʟXA(I))",
    "ʟEC(ʟXB(I))+ʟXN(I)→ʟEC(ʟXB(I))",
    "1→X",
    "End",
    "End",
    "End",
    # cations: remove valence e- (outside the noble-gas core), highest n first, then highest l
    "If C>0",
    "Then",
    "0→T",
    "For(K,1,6)",
    "If ʟCE(K)<Z",
    "ʟCI(K)→T",
    "End",
    "For(K,1,C)",
    "0→B",
    "0→D",
    "For(I,T+1,19)",
    "If ʟEC(I)>0 and ʟSC(I)>B",
    "Then",
    "ʟSC(I)→B",
    "I→D",
    "End",
    "End",
    "If not(D)",
    "Then",
    "For(I,1,19)",
    "If ʟEC(I)>0 and ʟSC(I)>B",
    "Then",
    "ʟSC(I)→B",
    "I→D",
    "End",
    "End",
    "End",
    "ʟEC(D)-1→ʟEC(D)",
    "End",
    "End",
    # noble-gas core for the condensed form
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
    # header + warnings
    "ClrHome",
    'Disp sub(Str8,2Z-1,2)+" CHARGE:"',
    "Output(1,12,C)",
    'Disp "e⁻ COUNT:"',
    "Output(2,11,N)",
    "2→V",
    "If X and C=0",
    "Then",
    'Disp "*EXCEPTION TO AUFBAU"',
    "V+1→V",
    "End",
    "If Z≥104",
    "Then",
    'Disp "*PREDICTED (SUPERHEAVY)"',
    "V+1→V",
    "End",
    "If C≠0 and not(G)",
    "Then",
    'Disp "*NOT A KNOWN ION"',
    "V+1→V",
    "End",
    'Disp "FULL:"',
    "V+1→V",
    "0→U",
    _render('""'),
    PAGE,
    'Disp "CONDENSED:"',
    "V+1→V",
    "If P",
    "Then",
    "ʟCI(P)→U",
    _render('"["+sub(Str4,2P-1,2)+"]"'),
    "Else",
    PAGE,
    'Disp "(SAME AS FULL)"',
    "End",
    'Output(10,15,"ENTER=BACK")',
    "Pause ",
    "Goto M",
])

ISO_CODE = "\n".join([
    "ClrHome",
    'Disp "SAME # OF e⁻:"',
    "Output(1,15,N)",
    "If G",
    'Disp "(KNOWN ATOMS/IONS)"',
    "If not(G)",
    'Disp "*GIVEN ION NOT KNOWN"',
    "0→R",
    "For(I,1,dim(ʟSZ))",
    "If ʟSZ(I)-ʟSQ(I)=N",
    "Then",
    "sub(Str8,2ʟSZ(I)-1,2)→Str2",
    'If sub(Str2,2,1)=" "',
    "sub(Str2,1,1)→Str2",
    "Str2+sub(Str7,2ʟSQ(I)+7,2)→Str2",
    "If ʟSZ(I)=Z and ʟSQ(I)=C",
    'Str2+" ◄"→Str2',
    "R+1→R",
    "If R≤7",
    "Output(2+R,2,Str2)",
    "If R>7 and R≤14",
    "Output(R-5,14,Str2)",
    "End",
    "End",
    'Output(10,17,"ENTER=BACK")',
    "Pause ",
    "Goto M",
])

# ------------------------------------------------------------------ PROGRAM

PROGRAMS = {}
PROGRAMS["CHEM"] = r"""
Lbl 0
Menu("CHEM 105 NOTES","FULL NOTES ►",N,"PREFIXES 10^x k μ n",A,"QUANTUM #S & NODES",B,"e⁻ RULES/PRINCIPLES",C,"PERIODIC TRENDS",D,"EXPERIMENTS",E,"MORE ►",M)
Lbl M
Menu("MORE NOTES","LAWS LIST A-F",F,"LIGHT RELATIONSHIPS",G,"ISOELECTRONIC LIST",H,"ELECTRON CONFIG",J,"ACCURATE VS PRECISE",I,"QUIT",Q,"◄ BACK",0)
Lbl N
prgmCHFULL
Goto 0
Lbl Q
ClrHome
Stop
Lbl H
1→Y
Goto S0
Lbl J
2→Y
Lbl S0
""" + '"' + SYM_CAPS + '"→Str9\n"' + SYM_PROPER + '"→Str8\n"' + CHARGE_TXT + '"→Str7\n' + \
    _tl([s[0] for s in SPECIES]) + "→ʟSZ\n" + _tl([s[1] for s in SPECIES]) + "→ʟSQ\n" + r"""ClrHome
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
If fPart(C)
Goto H7
Z-C→N
If N<1
Goto H9
0→G
If C=0
1→G
For(I,1,dim(ʟSZ))
If ʟSZ(I)=Z and ʟSQ(I)=C
1→G
End
If Y=2
Goto J0
""" + ISO_CODE + r"""
Lbl H7
Disp "CHARGE MUST BE A","WHOLE NUMBER"
Pause
Goto S0
Lbl H8
Disp "SYMBOL NOT FOUND"
Pause
Goto S0
Lbl H9
Disp "THAT LEAVES 0 e⁻"
Pause
Goto S0
Lbl J0
""" + CONFIG_CODE + "\n" + "\n".join(
    "Lbl %s\n%s" % (lbl, pages(txt, back))
    for lbl, txt, back in [
        ("A", PREFIXES, "0"), ("B", QUANTUM, "0"), ("C", RULES, "0"),
        ("D", TRENDS, "0"), ("E", EXPERIMENTS, "0"),
        ("F", LAWS, "M"), ("G", LIGHT, "M"), ("I", ACCURACY, "M"),
    ]
) + "\n"


# ================================================================ FULL NOTES
# Source text lives in full_notes.txt (CATEGORY / TOPIC headings).
# One menu program CHFULL + one program per category CHF1..CHF10.
import os as _os
import re as _re

_SIGNNOTE = ("Note: the study guide wavelength equation has an incorrect sign for "
             "emission. Wavelength is always positive and depends on the magnitude "
             "of the energy gap.")

# Short menu names (menu option text max 22 characters)
CAT_NAMES = {
    1: "e⁻ CONFIG & MAGNETISM", 2: "QUANTUM #S & NODES", 3: "PERIODIC TRENDS",
    4: "LIGHT & PHOTOELECTRIC", 5: "BOHR MODEL & SPECTRA", 6: "MATTER WAVES/UNCERTAIN",
    7: "SCIENTISTS/EXPERIMENTS", 8: "MOLES, MASS, ISOTOPES", 9: "ATOMS, IONS, CHARGES",
    10: "MEASUREMENT & MATTER",
}
TOPIC_SHORT = {
    "LAST-ELECTRON QUANTUM NUMBERS": "LAST e⁻ QUANTUM #S",
    "CONFIGURATION EXCEPTIONS": "CONFIG EXCEPTIONS",
    "TRANSITION-METAL IONS": "TRANSITION METAL IONS",
    "FIRST POSSIBLE SUBSHELL": "FIRST POSSIBLE SUBSHEL",
    "EFFECTIVE NUCLEAR CHARGE": "EFFECTIVE NUC CHARGE",
    "ELECTRON-AFFINITY EXCEPTIONS": "e⁻ AFFINITY EXCEPTIONS",
    "PHOTOELECTRIC THRESHOLD": "PHOTOELECTRIC THRESH.",
    "FREQUENCY VERSUS INTENSITY": "FREQUENCY VS INTENSITY",
    "BOUND ENERGY AND IONIZATION": "BOUND E & IONIZATION",
    "INITIAL AND FINAL LEVELS": "INITIAL & FINAL LEVELS",
    "MILLIKAN AND FLETCHER": "MILLIKAN & FLETCHER",
    "BUNSEN AND KIRCHHOFF": "BUNSEN & KIRCHHOFF",
    "BALMER AND RYDBERG": "BALMER & RYDBERG",
    "COUNTING ATOMS IN COMPOUNDS": "COUNT ATOMS/COMPOUNDS",
    "ELECTROSTATIC INTERACTIONS": "ELECTROSTATIC FORCES",
    "COMMON CONVERSION TRAPS": "CONVERSION TRAPS",
    "ELECTROMAGNETIC ORDER": "ELECTROMAGNETIC ORDER",
}
# Exceptions / hard concepts first within these categories
TOPIC_FIRST = {
    1: ["CONFIGURATION EXCEPTIONS", "TRANSITION-METAL IONS"],
    3: ["IONIZATION EXCEPTIONS", "ELECTRON-AFFINITY EXCEPTIONS"],
    10: ["COMMON CONVERSION TRAPS"],
}


def _clean(s):
    for a, b in [("’", ""), ("'", ""), ("“", ""), ("”", ""), ("–", "-"), ("−", "-"),
                 ("—", "-"), ("|ψ| squared", "psi² (psi squared)"), ("ψ", "psi"),
                 ("ν", "nu"), ("dz2", "dz²"), ("→", " to ")]:
        s = s.replace(a, b)
    return s


def _sentences(par):
    parts = _re.split(r"(?<=[.:;])\s+(?=(?:[A-Z0-9|]|[a-z]{1,4}[,:]|ml|ms|n |l |s |p |d |f |exa))", par)
    return [p for p in parts if p]


def _load_full_notes():
    path = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "full_notes.txt")
    cats, cur, top = [], None, None
    for raw in open(path, encoding="utf-8").read().splitlines():
        line = raw.strip()
        if not line:
            continue
        m = _re.match(r"CATEGORY (\d+): (.*)", line)
        if m:
            cur = {"n": int(m.group(1)), "title": m.group(2), "topics": []}
            cats.append(cur)
            continue
        m = _re.match(r"TOPIC: (.*)", line)
        if m:
            top = {"title": m.group(1), "text": []}
            cur["topics"].append(top)
            continue
        top["text"].append(_SIGNNOTE if line == "@SIGNNOTE" else line)
    for c in cats:
        first = TOPIC_FIRST.get(c["n"], [])
        c["topics"].sort(key=lambda t: first.index(t["title"]) if t["title"] in first else len(first))
    return cats


def _topic_lines(t):
    out = wrap(_clean(t["title"]), indent=" ")
    for par in t["text"]:
        par = _clean(par)
        # the metric prefix list reads best one prefix per line
        pieces = _sentences(par) if len(par) > W else [par]
        for s in pieces:
            out.extend(wrap(s, indent="  "))
    return out


def _labels():
    for a in "ABCDEFGHIJKMNOPQRSTUVWX":
        for b in "0123456789":
            yield a + b


FULL_CATS = _load_full_notes()
assert len(FULL_CATS) == 10


def _category_program(c):
    gen = _labels()
    topics = c["topics"]
    per = 5
    chunks = [topics[i:i + per] for i in range(0, len(topics), per)]
    if len(topics) <= 6:
        chunks = [topics]
    page_lbl = ["0"] + [next(gen) for _ in chunks[1:]]
    top_lbl = [next(gen) for _ in topics]
    title = "CAT %d: %s" % (c["n"], CAT_NAMES[c["n"]])
    if len(title) > 24:
        title = CAT_NAMES[c["n"]]
    code, k = [], 0
    for pi, ch in enumerate(chunks):
        opts = []
        for t in ch:
            name = _clean(TOPIC_SHORT.get(t["title"], t["title"]))[:22]
            opts.append('"%s",%s' % (name, top_lbl[k]))
            k += 1
        if pi + 1 < len(chunks):
            opts.append('"MORE TOPICS ►",%s' % page_lbl[pi + 1])
        opts.append('"◄ BACK",%s' % ("Z" if pi == 0 else page_lbl[pi - 1]))
        code.append("Lbl %s" % page_lbl[pi])
        code.append('Menu("%s",%s)' % (title, ",".join(opts)))
    code += ["Lbl Z", "Return"]
    k = 0
    for pi, ch in enumerate(chunks):
        for t in ch:
            code.append("Lbl %s" % top_lbl[k])
            code.append(pages(_topic_lines(t), page_lbl[pi]))
            k += 1
    return "\n".join(code)


for _c in FULL_CATS:
    PROGRAMS["CHF%d" % _c["n"]] = _category_program(_c)

PROGRAMS["CHFULL"] = "\n".join([
    "Lbl 0",
    'Menu("FULL NOTES",' + ",".join('"%s",%s' % (CAT_NAMES[n], "A%d" % n) for n in range(1, 6))
    + ',"MORE CATEGORIES ►",P,"◄ BACK TO CHEM",Z)',
    "Lbl P",
    'Menu("FULL NOTES 2",' + ",".join('"%s",%s' % (CAT_NAMES[n], "A%d" % n) for n in range(6, 11))
    + ',"◄ BACK",0)',
    "Lbl Z",
    "ClrHome",
    "Return",
] + sum([["Lbl A%d" % n, "prgmCHF%d" % n, "Goto %s" % ("0" if n <= 5 else "P")] for n in range(1, 11)], []))
