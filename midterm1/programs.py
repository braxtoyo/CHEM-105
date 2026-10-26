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
# Display order: Aufbau (filling) order so 4s shows before 3d, 5s before 4d, etc.
ORDER = list(range(1, 20))
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


def _render(prefix, has_text):
    """Print filled subshells with Aufbau index > U, in n-then-l order, wrapped to 26.
    Never joins onto an empty string (that errors on the calculator): W=1 means
    Str2 already holds text; otherwise Str2 is a placeholder that gets replaced."""
    return "\n".join([
        prefix + "→Str2",
        "%d→W" % (1 if has_text else 0),
        "For(J,1,19)",
        "ʟOR(J)→I",
        "If ʟEC(I)>0 and I>U",
        "Then",
        "sub(Str6,2I-1,2)+sub(Str5,2ʟEC(I)-1,2)→Str3",
        'If sub(Str3,4,1)=" "',
        "sub(Str3,1,3)→Str3",
        "If W",
        "Then",
        "If length(Str2)+length(Str3)≥26",
        "Then",
        PAGE,
        "Disp Str2",
        "V+1→V",
        "Str3→Str2",
        "Else",
        'Str2+" "+Str3→Str2',
        "End",
        "Else",
        "Str3→Str2",
        "1→W",
        "End",
        "End",
        "End",
        "If W",
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
    _render('"?"', False),
    PAGE,
    'Disp "CONDENSED:"',
    "V+1→V",
    "If P",
    "Then",
    "ʟCI(P)→U",
    _render('"["+sub(Str4,2P-1,2)+"]"', True),
    "Else",
    PAGE,
    'Disp "(SAME AS FULL)"',
    "End",
    'Output(10,15,"ENTER=BACK")',
    "Pause ",
    "Goto 0",
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
    "Goto 0",
])

# ------------------------------------------------------------------ PROGRAM

PROGRAMS = {}
PROGRAMS["CHEM"] = r"""
Lbl 0
Menu("CHEM 105 NOTES","FULL NOTES ►",N,"EXAM SETUP ►",P,"UNIT CONVERT ►",C,"PREFIXES 10^x k μ n",A,"ISOELECTRONIC LIST",H,"ELECTRON CONFIG",J,"QUIT",Q)
Lbl N
prgmCHFULL
Goto 0
Lbl P
prgmCHPS
Goto 0
Lbl C
prgmCHCV
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
        ("A", PREFIXES, "0"),
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
    'Menu("FULL NOTES",' + ",".join('"%s",%s' % (CAT_NAMES[n], "C%d" % (n % 10)) for n in range(1, 6))
    + ',"MORE CATEGORIES ►",P,"◄ BACK TO CHEM",Z)',
    "Lbl P",
    'Menu("FULL NOTES 2",' + ",".join('"%s",%s' % (CAT_NAMES[n], "C%d" % (n % 10)) for n in range(6, 11))
    + ',"◄ BACK",0)',
    "Lbl Z",
    "ClrHome",
    "Return",
] + sum([["Lbl C%d" % (n % 10), "prgmCHF%d" % n, "Goto %s" % ("0" if n <= 5 else "P")] for n in range(1, 11)], []))

# ======================================================== EXAM PROBLEM SETUP
# Accessible from the CHEM main menu as "EXAM SETUP ►" (label P -> prgmCHPS).
# Each section: triggers, equations, unit traps, step-by-step workflow.

_LIGHT_PHOTONS = [
    "LIGHT & PHOTONS",
    "TRIGGERS:",
    "wavelength, frequency",
    "photon energy, nm",
    "radio broadcast",
    "EQUATIONS:",
    "c = lambda*nu",
    "E = h*nu",
    "REARRANGEMENTS:",
    "nu = c/lambda",
    "E = hc/lambda",
    "h*nu = photon energy",
    "UNIT TRAPS:",
    "lambda MUST be in m",
    "1 nm = 1E-9 m",
    "nu must be in Hz",
    "c = 2.998E8 m/s",
    "h = 6.626E-34 J*s",
    "WORKFLOW:",
    "1. Note what is given",
    "  and what to find",
    "2. Convert to SI first",
    "  lam: nm to m (*1E-9)",
    "  nu: MHz to Hz (*1E6)",
    "3. c=lam*nu to get nu",
    "4. E=h*nu to get E",
    "5. Rearrange as needed",
]

_PHOTOELECTRIC = [
    "PHOTOELECTRIC EFFECT",
    "TRIGGERS:",
    "work function phi",
    "strikes metal",
    "ejected electron, KE",
    "electron speed v",
    "EQUATIONS:",
    "phi = h*nu - KE",
    "KE = (1/2)*m*v^2",
    "REARRANGEMENTS:",
    "KE = h*nu - phi",
    "v = sqrt(2*KE/me)",
    "UNIT TRAPS:",
    "me = 9.109E-31 kg",
    "use electron mass only",
    "not atomic mass unit",
    "1 eV = 1.602E-19 J",
    "convert eV to J first",
    "WORKFLOW:",
    "1. Find photon E: hc/lam",
    "  or h*nu",
    "2. Is h*nu > phi?",
    "  No: no e- ejected.",
    "  Yes: continue.",
    "3. KE = h*nu - phi",
    "4. v=sqrt(2*KE/me)",
    "5. eV to J: *1.602E-19",
]

_DEBROGLIE = [
    "DE BROGLIE WAVES",
    "TRIGGERS:",
    "wavelength of a moving",
    "  particle or electron",
    "matter wave",
    "EQUATION:",
    "lambda = h / (m*v)",
    "UNIT REQUIREMENTS:",
    "m MUST be in kg",
    "v MUST be in m/s",
    "WHY IT WORKS:",
    "1 J = 1 kg*m^2/s^2",
    "units cancel with h",
    "h = 6.626E-34 J*s",
    "WORKFLOW:",
    "1. Convert mass to kg",
    "  1 amu = 1.66E-27 kg",
    "  1 g = 1E-3 kg",
    "2. v must be in m/s",
    "3. lam = h/(m*v)",
    "  h = 6.626E-34 J*s",
]

_BOHR = [
    "BOHR / HYDROGEN MODEL",
    "TRIGGERS:",
    "H atom spectral line",
    "electron transition",
    "emits/absorbs photon",
    "EQUATIONS:",
    "En=-Z^2*RH*hc/n^2",
    "1/lam=RH*(1/n1^2",
    "  - 1/n2^2)",
    "KEY CONCEPT:",
    "dE = Ef - Ei = h*nu",
    "ABSORPTION:",
    "e- moves low to high n",
    "dE > 0",
    "EMISSION:",
    "e- drops high to low n",
    "dE < 0 (photon E > 0)",
    "WORKFLOW:",
    "1. ID ni and nf",
    "  emission: ni>nf",
    "  absorption: ni<nf",
    "2. dE = Ef - Ei",
    "3. Photon E = magn of dE",
    "4. For lam: Rydberg eq",
    "  n1=smaller, n2=larger",
    "5. dE < 0 for emission",
]

_MOLES_ISOTOPES = [
    "MOLES & ISOTOPES",
    "TRIGGERS:",
    "grams, molar mass",
    "atoms or molecules",
    "avg atomic mass",
    "percent abundance",
    "MOLE EQUATIONS:",
    "mol = g / MM",
    "g = mol * MM",
    "particles=mol*6.022E23",
    "ISOTOPE EQUATIONS:",
    "Avg=M1*x+M2*(1-x)",
    "x=(Avg-M2)/(M1-M2)",
    "x*100 = pct abundance",
    "WORKFLOW:",
    "1. g to mol: g/MM",
    "2. mol to g: mol*MM",
    "3. parts: mol*6.022E23",
    "4. MM: sum(mass*subscript)",
    "5. Isotopes: solve for x",
    "6. Sanity: avg nearest",
    "  most abundant isotope",
]

_QUANTUM_NOS = [
    "QUANTUM NUMBERS",
    "TRIGGERS:",
    "four quantum numbers",
    "last electron",
    "allowed values of ml",
    "RULES:",
    "n: 1, 2, 3... (level)",
    "l: 0 to n-1",
    "  s=0, p=1, d=2, f=3",
    "ml: -l to +l",
    "ms: +1/2 or -1/2",
    "WORKFLOW:",
    "1. Write e- config",
    "2. Find last subshell",
    "3. n = number before",
    "  the subshell letter",
    "4. l from s/p/d/f",
    "5. Hund: fill boxes low",
    "  to high ml singly",
    "6. 1st e- in box: +1/2",
    "  2nd e- in box: -1/2",
]

PROGRAMS["CHPS"] = "\n".join([
    "Lbl 0",
    'Menu("EXAM PROBLEM SETUP","1:LIGHT/PHOTONS",A,"2:PHOTOELECTRIC",B,"3:DE BROGLIE",C,"4:BOHR MODEL",D,"5:MOLES/ISOTOPES",E,"6:QUANTUM NUMBERS",F,"BACK",Z)',
    "Lbl A",
    pages(_LIGHT_PHOTONS, "0"),
    "Lbl B",
    pages(_PHOTOELECTRIC, "0"),
    "Lbl C",
    pages(_DEBROGLIE, "0"),
    "Lbl D",
    pages(_BOHR, "0"),
    "Lbl E",
    pages(_MOLES_ISOTOPES, "0"),
    "Lbl F",
    pages(_QUANTUM_NOS, "0"),
    "Lbl Z",
    "Return",
])


# ======================================================== UNIT CONVERTER

_PX_NAMES   = ["none", "kilo", "milli", "micro", "nano", "mega", "centi"]
_PX_FACTORS = ["1", "1000", ".001", "1E-6", "1E-9", "1000000", ".01"]

def _ucv_block(units, f_lbls, f_done, t_lbls, t_done, px_lbls, px_done):
    """Generate TI-BASIC ratio-conversion code for one unit category.
    Flow: enter value → pick SI prefix → pick FROM unit → pick TO unit → display result.
    units    : list of (display_name, factor_string); factor = base units per 1 of this unit
    f_lbls   : 2-char label strings for FROM menu items
    f_done   : label after FROM selection
    t_lbls   : 2-char label strings for TO menu items
    t_done   : label after TO selection
    px_lbls  : 7 label strings for prefix menu items
    px_done  : label after prefix selection
    """
    names   = [u[0] for u in units]
    factors = [u[1] for u in units]
    rows = []
    rows.append('Input "VALUE? ",X')
    # SI PREFIX menu (none / kilo / milli / micro / nano / mega / centi)
    items = ",".join(f'"{n}",{l}' for n, l in zip(_PX_NAMES, px_lbls))
    rows.append(f'Menu("SI PREFIX:",{items})')
    for fac, lbl in zip(_PX_FACTORS, px_lbls):
        rows += [f"Lbl {lbl}", f"{fac}→K", f"Goto {px_done}"]
    rows += [f"Lbl {px_done}", "X*K→X"]
    # FROM menu
    items = ",".join(f'"{n}",{l}' for n, l in zip(names, f_lbls))
    rows.append(f'Menu("FROM UNIT:",{items})')
    for fac, lbl in zip(factors, f_lbls):
        rows += [f"Lbl {lbl}", f"{fac}→F", f"Goto {f_done}"]
    rows.append(f"Lbl {f_done}")
    # TO menu
    items = ",".join(f'"{n}",{l}' for n, l in zip(names, t_lbls))
    rows.append(f'Menu("TO UNIT:",{items})')
    for fac, lbl in zip(factors, t_lbls):
        rows += [f"Lbl {lbl}", f"{fac}→T", f"Goto {t_done}"]
    rows.append(f"Lbl {t_done}")
    # Calculate and display
    rows += ["ClrHome", "X*F/T→R", 'Disp "RESULT:"', "Disp R",
             'Output(10,1,"ENTER=BACK")', "Pause ", "Goto 0"]
    return "\n".join(rows)


# Unit data: (display name, factor as string)
# Factor = number of BASE UNITS per 1 of this unit.
_CVOL = [  # base: mL
    ("mL",    "1"),
    ("L",     "1000"),
    ("cm3",   "1"),
    ("fl oz", "29.5735"),
    ("qt",    "946.353"),
    ("gal",   "3785.41"),
    ("in3",   "16.3871"),
]
_CMAS = [  # base: g
    ("g",   "1"),
    ("kg",  "1000"),
    ("mg",  ".001"),
    ("μg",  "1E-6"),
    ("lb",  "453.592"),
    ("oz",  "28.3495"),
    ("ng",  "1E-9"),
]
_CLEN = [  # base: m
    ("m",  "1"),
    ("cm", ".01"),
    ("mm", ".001"),
    ("nm", "1E-9"),
    ("km", "1000"),
    ("in", ".0254"),
    ("ft", ".3048"),
]
_CENR = [  # base: J
    ("J",    "1"),
    ("kJ",   "1000"),
    ("eV",   "1.60218E-19"),
    ("cal",  "4.184"),
    ("kcal", "4184"),
]

# Temperature: K <-> C (non-ratio, no prefix needed in gen chem)
_TEMP = "\n".join([
    'Input "VALUE? ",X',
    'Menu("FROM UNIT:","K (Kelvin)",T0,"C (Celsius)",T1)',
    "Lbl T0", "0→G", "Goto TF",
    "Lbl T1", "1→G", "Goto TF",
    "Lbl TF",
    'Menu("TO UNIT:","K (Kelvin)",U0,"C (Celsius)",U1)',
    "Lbl U0", "0→H", "Goto TT",
    "Lbl U1", "1→H", "Goto TT",
    "Lbl TT",
    "ClrHome",
    "X→R",
    "If G=0",   # K to C
    "If H=1",
    "X-273.15→R",
    "If G=1",   # C to K
    "If H=0",
    "X+273.15→R",
    'Disp "RESULT:"',
    "Disp R",
    'Output(10,1,"ENTER=BACK")',
    "Pause ",
    "Goto 0",
])

PROGRAMS["CHCV"] = "\n".join([
    "Lbl 0",
    'Menu("UNIT CONVERTER","1:VOLUME",A,"2:MASS",B,"3:LENGTH",C,"4:ENERGY",D,"5:TEMP",E,"QUIT",Z)',
    # VOLUME  prefix:X0-X6/XF  FROM:V0-V6/VF  TO:W0-W6/VT
    "Lbl A",
    _ucv_block(_CVOL,
               ["V0","V1","V2","V3","V4","V5","V6"], "VF",
               ["W0","W1","W2","W3","W4","W5","W6"], "VT",
               ["X0","X1","X2","X3","X4","X5","X6"], "XF"),
    # MASS    prefix:Y0-Y6/YF  FROM:M0-M6/MF  TO:N0-N6/MT
    "Lbl B",
    _ucv_block(_CMAS,
               ["M0","M1","M2","M3","M4","M5","M6"], "MF",
               ["N0","N1","N2","N3","N4","N5","N6"], "MT",
               ["Y0","Y1","Y2","Y3","Y4","Y5","Y6"], "YF"),
    # LENGTH  prefix:J0-J6/JF  FROM:P0-P6/PF  TO:Q0-Q6/PT
    "Lbl C",
    _ucv_block(_CLEN,
               ["P0","P1","P2","P3","P4","P5","P6"], "PF",
               ["Q0","Q1","Q2","Q3","Q4","Q5","Q6"], "PT",
               ["J0","J1","J2","J3","J4","J5","J6"], "JF"),
    # ENERGY  prefix:K0-K6/KF  FROM:R0-R4/RF  TO:S0-S4/ET
    "Lbl D",
    _ucv_block(_CENR,
               ["R0","R1","R2","R3","R4"], "RF",
               ["S0","S1","S2","S3","S4"], "ET",
               ["K0","K1","K2","K3","K4","K5","K6"], "KF"),
    # TEMPERATURE (no prefix step)
    "Lbl E",
    _TEMP,
    # QUIT -> return to CHEM
    "Lbl Z",
    "Return",
])
