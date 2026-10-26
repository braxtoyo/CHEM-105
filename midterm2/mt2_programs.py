# -*- coding: utf-8 -*-
"""MIDTERM 2 study set for TI-84 Plus CE (26 x 10 home screen).

Programs:
  MIDTERM2  main menu + all notes
  MT2SN     SN + lone pairs -> geometry / shape / angle / hybridization
  MT2LW     single-center Lewis structure solver
  MT2G      shared geometry lookup (called by MT2SN and MT2LW)
"""

ROWS = 9  # 9 text lines + a footer on row 10, so the screen never scrolls


def _screens(screens, end):
    out, n = [], len(screens)
    for i, sc in enumerate(screens, 1):
        out.append("ClrHome")
        for j in range(0, len(sc), 3):
            out.append("Disp " + ",".join('"%s"' % s for s in sc[j:j + 3]))
        foot = ("ENTER=NEXT %d/%d" % (i, n)) if i < n else ("ENTER=BACK %d/%d" % (i, n))
        if n == 1:
            foot = "ENTER=BACK"
        out.append('Output(10,%d,"%s")' % (27 - len(foot), foot))
        out.append("Pause")
    out.append(end)
    return out


def pages(label, back, lines, rows=ROWS, end=None):
    """Lbl, then screens of up to `rows` lines, each ending in Pause."""
    scr = [lines[i:i + rows] for i in range(0, len(lines), rows)]
    return "\n".join(["Lbl " + label] + _screens(scr, end or "Goto " + back))


def blocks(label, back, entries, header=(), rows=ROWS, end=None):
    """Like pages() but never splits an entry (list of lines) across screens."""
    screens, cur = [], list(header)
    for e in entries:
        if len(cur) + len(e) > rows:
            screens.append(cur)
            cur = []
        cur += e
    screens.append(cur)
    return "\n".join(["Lbl " + label] + _screens(screens, end or "Goto " + back))


def menu(label, title, items):
    s = ",".join('"%s",%s' % (t, l) for t, l in items)
    return "Lbl %s\nClrHome\nMenu(\"%s\",%s)" % (label, title, s)


# ---------------------------------------------------------------- shapes
# (SN, LP): electron geometry, molecular shape, angle, hybridization,
#           example, symmetric (nonpolar if all outer atoms identical)
SHAPES = [
    (2, 0, "LINEAR", "LINEAR", "180°", "sp", "CO₂ BeCl₂ HCN", 1),
    (2, 1, "LINEAR", "LINEAR (DIATOMIC)", "180°", "sp", "N IN N₂, C IN CO", 0),
    (3, 0, "TRIGONAL PLANAR", "TRIGONAL PLANAR", "120°", "sp²", "BF₃ SO₃ CO₃²⁻ NO₃⁻", 1),
    (3, 1, "TRIGONAL PLANAR", "BENT", "<120°", "sp²", "SO₂ O₃ NO₂⁻", 0),
    (3, 2, "TRIGONAL PLANAR", "LINEAR (DIATOMIC)", "180°", "sp²", "O IN C=O, O IN O₂", 0),
    (4, 0, "TETRAHEDRAL", "TETRAHEDRAL", "109.5°", "sp³", "CH₄ NH₄+ SO₄²⁻", 1),
    (4, 1, "TETRAHEDRAL", "TRIGONAL PYRAMIDAL", "<109.5° (NH₃ 107°)", "sp³", "NH₃ PCl₃ ClO₃⁻", 0),
    (4, 2, "TETRAHEDRAL", "BENT", "<109.5° (H₂O 104.5°)", "sp³", "H₂O OF₂ ClO₂⁻", 0),
    (4, 3, "TETRAHEDRAL", "LINEAR (DIATOMIC)", "180°", "sp³", "HF HCl, F IN F₂", 0),
    (5, 0, "TRIGONAL BIPYRAMIDAL", "TRIGONAL BIPYRAMIDAL", "90° 120° 180°", "sp³d", "PCl₅ PF₅", 1),
    (5, 1, "TRIGONAL BIPYRAMIDAL", "SEESAW", "<90° AND <120°", "sp³d", "SF₄ IF₄+", 0),
    (5, 2, "TRIGONAL BIPYRAMIDAL", "T-SHAPED", "<90°", "sp³d", "ClF₃ BrF₃", 0),
    (5, 3, "TRIGONAL BIPYRAMIDAL", "LINEAR", "180°", "sp³d", "XeF₂ I₃⁻", 1),
    (5, 4, "TRIGONAL BIPYRAMIDAL", "LINEAR (DIATOMIC)", "180°", "sp³d", "RARE", 0),
    (6, 0, "OCTAHEDRAL", "OCTAHEDRAL", "90° 180°", "sp³d²", "SF₆ PF₆⁻", 1),
    (6, 1, "OCTAHEDRAL", "SQUARE PYRAMIDAL", "<90°", "sp³d²", "BrF₅ IF₅ XeOF₄", 0),
    (6, 2, "OCTAHEDRAL", "SQUARE PLANAR", "90° 180°", "sp³d²", "XeF₄ ICl₄⁻", 1),
    (6, 3, "OCTAHEDRAL", "T-SHAPED", "<90°", "sp³d²", "RARE", 0),
    (6, 4, "OCTAHEDRAL", "LINEAR", "180°", "sp³d²", "RARE", 1),
    (6, 5, "OCTAHEDRAL", "LINEAR (DIATOMIC)", "180°", "sp³d²", "RARE", 0),
]


def mt2g():
    out = ['"?"→Str4', '"?"→Str5', '"?"→Str6', '"?"→Str7', '"?"→Str0', "0→Y"]
    for sn, lp, eg, sh, ang, hyb, ex, sym in SHAPES:
        out += ["If S=%d and L=%d" % (sn, lp), "Then",
                '"%s"→Str4' % eg, '"%s"→Str5' % sh, '"%s"→Str6' % ang,
                '"%s"→Str7' % hyb, '"%s"→Str0' % ex, "%d→Y" % sym, "End"]
    out.append("Return")
    return "\n".join(out)


def d1(x):
    return 'sub("0123456789",%s+1,1)' % x


def d2(x):
    return ('sub(" 123456789",int(%s/10)+1,1)+sub("0123456789",%s-10int(%s/10)+1,1)'
            % (x, x, x))


NEXT = 'Output(10,17,"ENTER=NEXT")'

MT2SN = r"""
Lbl 1
ClrHome
Disp "SN + LONE PAIRS ► SHAPE","SN = ATOMS BONDED TO THE","CENTER + ITS LONE PAIRS","(A DOUBLE OR TRIPLE BOND","COUNTS AS 1 ATOM)"
Input "STERIC NUMBER:",S
Input "LONE PAIRS:",L
(S<2 or S>6 or L<0 or L≥S or fPart(S) or fPart(L))→E
If E
Disp "USE SN 2 TO 6","AND LONE PAIRS 0 TO SN-1"
If E
Pause
If E
Goto 1
prgmMT2G
ClrHome
Disp "STERIC NUMBER: "+%(S)s
" = "+%(A)s+" ATOM"→Str2
If S-L≠1
Str2+"S"→Str2
Str2+" + "+%(L)s+" LONE PAIR"→Str2
If L≠1
Str2+"S"→Str2
Disp Str2
Disp "ELECTRON GEOMETRY:","  "+Str4,"MOLECULAR GEOMETRY:","  "+Str5,"BOND ANGLE:","  "+Str6
Disp "HYBRIDIZATION: "+Str7
%(NEXT)s
Pause
ClrHome
Disp "EXAMPLES:","  "+Str0
If Y
Disp "NONPOLAR IF ALL OUTER","  ATOMS ARE THE SAME"
If not(Y) and S-L=1
Disp "POLAR IF THE 2 ATOMS","  ARE DIFFERENT"
If not(Y) and S-L>1
Disp "POLAR (LONE PAIRS MAKE","  IT LOPSIDED)"
Disp "SIGMA (σ) BONDS USE THE","  "+Str7+" HYBRID ORBITALS","PI (π) BONDS USE LEFTOVER","  UNHYBRIDIZED p ORBITALS"
Output(10,17,"ENTER=MENU")
Pause
Lbl 3
Menu("SN SOLVER","NEW ENTRY",1,"WHAT DOES IT MEAN?",4,"BACK",2)
Lbl 4
prgmMT2H
Goto 3
Lbl 2
Return
""" % {"S": d1("S"), "A": d1("(S-L)"), "L": d1("L"), "NEXT": NEXT}

# ---------------------------------------------------------------- Lewis
HAL = "(J=7 or J=12 or J=17 or J=23)"
FCS = 'sub("-4-3-2-1 0+1+2+3+4",2%s+9,2)'

SETUP = r"""
ʟLWA(B)→J
J→ʟLWR(16)
ʟLWV(J)→ʟLWR(12)
ʟLWE(J)→ʟLWR(13)
ʟLWP(J)→ʟLWR(14)
(J=2 or J=3 or J=8 or J=13 or J=19)→ʟLWR(15)
2000(ʟLWN(B)≠1)+round(10ʟLWE(J),0)→ʟLWR(25)
"""

BUILD = r"""
0→M
For(I,1,K)
ʟLWA(I)→J
If J≠1
Then
For(D,1,ʟLWN(I)-(I=B))
M+1→M
J→ʟLWT(M)
0→ʟLWH(M)
3-2%s→ʟLWB(M)
End
End
End
O→D
For(I,1,M)
If D and ʟLWT(I)=6
Then
1→ʟLWH(I)
2→ʟLWB(I)
D-1→D
End
End
ʟLWR(10)-O→θ
""" % HAL

DECODE = r"""
Q→R
For(I,1,M)
R-ʟLWB(I)int(R/ʟLWB(I))+1→ʟLWO(I)
int(R/ʟLWB(I))→R
End
"""

EVAL = r"""
θ→X
0→W
0→Z
0→U
0→G
1→H
For(I,1,M)
X+ʟLWO(I)→X
8-2(ʟLWO(I)+ʟLWH(I))→D
If D<0
0→H
D→ʟLWL(I)
W+D→W
ʟLWV(ʟLWT(I))-D-ʟLWO(I)-ʟLWH(I)→F
F→ʟLWF(I)
Z+abs(F)→Z
max(U,abs(F))→U
G+F*ʟLWE(ʟLWT(I))→G
End
V-2X-2O-W→L
2X+L→Y
If L<0 or (ʟLWR(14)=2 and Y>8) or M+θ+int((L+1)/2)>6
0→H
ʟLWR(12)-L-X→F
Z+abs(F)→Z
max(U,abs(F))→U
G+F*ʟLWR(13)→G
20(20000(40000(10(20(1-ʟLWR(15))(8-min(Y,8))+Z)+U)+ʟLWR(25)+100(6-M-θ)+20000ʟLWR(17)(θ>0)(ʟLWR(16)≠6))+round(100G,0)+10000)+Y→S
"""

UPDATE = r"""
If H
Then
If S<ʟLWR(1)
Then
S→ʟLWR(1)
B→ʟLWR(2)
O→ʟLWR(3)
Q→ʟLWR(4)
1→ʟLWR(5)
Else
If S=ʟLWR(1) and B=ʟLWR(2) and O=ʟLWR(3)
ʟLWR(5)+1→ʟLWR(5)
End
If Y≤8 and S<ʟLWS(B)
Then
S→ʟLWS(B)
O→ʟLWU(B)
Q→ʟLWQ(B)
End
End
"""

NEEDP = """If Z+%d>9
Then
Output(10,17,"ENTER=NEXT")
Pause
ClrHome
0→Z
End"""

MT2LW = r"""
Lbl S
ClrHome
Disp "LEWIS SOLVER (1 CENTER)","TYPE CAPS: SO4 XEF4 HNO3","CHARGE OK: NH4+  SO4-2"
Input "FORMULA:",Str1
"0"→Str2
max(inString(Str1+" ","+"),max(inString(Str1+" ","-"),inString(Str1+" ","⁻")))→P
If P>1
Then
sub(Str1,P,length(Str1)-P+1)→Str2
sub(Str1,1,P-1)→Str1
End
If not(P)
Input "CHARGE (0 IF NONE):",Str2
Str2+" "→Str3
0→M
0→E
1→F
For(I,1,length(Str3))
sub(Str3,I,1)→Str0
inString("0123456789",Str0)→D
If D
10M+D-1→M
If Str0="-" or Str0="⁻"
⁻1→F
If Str0="-" or Str0="⁻" or Str0="+"
1→E
End
If E and not(M)
1→M
FM→C
Disp "WORKING..."
"H BEB C N O F ALSIP S CLGAGEASSEBRKRINSNSBTEI XE"→Str9
"H BeB C N O F AlSiP S ClGaGeAsSeBrKrInSnSbTeI Xe"→Str8
{1,2,3,4,5,6,7,3,4,5,6,7,3,4,5,6,7,8,3,4,5,6,7,8}→ʟLWV
{2.2,1.57,2.04,2.55,3.04,3.44,3.98,1.61,1.9,2.19,2.58,3.16,1.81,2.01,2.18,2.55,2.96,3,1.78,1.96,2.05,2.1,2.66,2.6}→ʟLWE
{1,2,2,2,2,2,2,3,3,3,3,3,4,4,4,4,4,4,5,5,5,5,5,5}→ʟLWP
7→dim(ʟLWT)
7→dim(ʟLWH)
7→dim(ʟLWB)
7→dim(ʟLWO)
7→dim(ʟLWL)
7→dim(ʟLWF)
25→dim(ʟLWR)
Fill(0,ʟLWR)
Str1+"  "→Str3
length(Str1)→N
{0}→ʟLWA
{0}→ʟLWN
0→K
0→E
1→P
While P≤N and not(E)
sub(Str3,P,2)→Str2
0→J
For(I,1,24)
If sub(Str9,2I-1,2)=Str2 or sub(Str8,2I-1,2)=Str2
I→J
End
If J and (sub(Str2,2,1)=" " and P<N or not(inString("0123456789HBCNOFASGKITXP ",sub(Str3,P+2,1))))
0→J
If J
Then
P+2→P
Else
sub(Str3,P,1)+" "→Str2
For(I,1,24)
If sub(Str9,2I-1,2)=Str2 or sub(Str8,2I-1,2)=Str2
I→J
End
P+1→P
End
If not(J) and not(E)
P-1→ʟLWR(20)
If not(J)
1→E
0→M
inString("0123456789",sub(Str3,P,1))→D
While D
10M+D-1→M
P+1→P
inString("0123456789",sub(Str3,P,1))→D
End
If not(M)
1→M
If J
Then
0→F
For(I,1,K)
If ʟLWA(I)=J
I→F
End
If F
Then
ʟLWN(F)+M→ʟLWN(F)
Else
K+1→K
J→ʟLWA(K)
M→ʟLWN(K)
End
End
End
If E
Disp "CAN NOT READ: "+sub(Str3,ʟLWR(20),1),"USE CAPS, NO ( ) OR SPACE","MAIN-GROUP ELEMENTS ONLY"
If not(K) and not(E)
Disp "TYPE A FORMULA, EX: SO4"
If E or not(K)
Pause
If E or not(K)
Goto S
0→V
0→T
For(I,1,K)
V+ʟLWV(ʟLWA(I))ʟLWN(I)→V
If ʟLWA(I)=1
ʟLWN(I)→ʟLWR(10)
If ʟLWA(I)=6
ʟLWN(I)→ʟLWR(11)
If ʟLWA(I)≠1
Then
T+ʟLWN(I)→T
ʟLWR(22)+1→ʟLWR(22)
End
End
V-C→V
(not(T) or T>7 or abs(C)>4 or V<2)→E
If E
Disp "CAN NOT SOLVE THIS ONE","1 CENTER, MAX 6 OUTER","CHARGE -4 TO +4"
If E
Pause
If E
Goto S
⁻1→A
If Str1="H3PO3"
2→A
If Str1="H3PO2"
1→A
(sub(Str1,1,1)="H" and ʟLWR(11)>0)→ʟLWR(17)
9ᴇ99→ʟLWR(1)
1→ʟLWR(2)
K→dim(ʟLWS)
K→dim(ʟLWU)
K→dim(ʟLWQ)
Fill(9ᴇ99,ʟLWS)
For(B,1,K)
ʟLWA(B)→J
If J≠1 and (J≠7 or ʟLWR(22)=1)
Then
%(SETUP)s
min(ʟLWR(10),ʟLWR(11)-(J=6))→ʟLWR(24)
0→ʟLWR(23)
If A≥0
Then
A→ʟLWR(23)
min(A,ʟLWR(24))→ʟLWR(24)
End
For(O,ʟLWR(23),ʟLWR(24))
%(BUILD)s
If M+θ≥1 and M+θ≤6
Then
1→T
For(I,1,M)
T*ʟLWB(I)→T
End
For(Q,0,T-1)
%(DECODE)s
%(EVAL)s
%(UPDATE)s
End
End
End
End
End
If ʟLWR(1)=9ᴇ99
Disp "NO 1-CENTER STRUCTURE","PROBABLY 2+ CENTERS","(EX: C2H6, N2H4)"
If ʟLWR(1)=9ᴇ99
Pause
If ʟLWR(1)=9ᴇ99
Goto S
ʟLWR(2)→B
ʟLWR(3)→O
ʟLWR(4)→Q
Lbl D
%(SETUP)s
%(BUILD)s
%(DECODE)s
%(EVAL)s
min(4,max(⁻4,F))→ʟLWR(20)
ClrHome
0→Z
If ʟLWR(21)
Then
Disp "OCTET-ONLY VERSION","(IF YOUR CLASS DOES NOT","ALLOW EXPANDED OCTETS):"
3→Z
End
min(4,max(⁻4,C))→F
If C
Disp Str1+"  (CHARGE "+%(FCT)s+")"
If not(C)
Disp Str1+"  (NEUTRAL)"
Disp %(V2)s+" VALENCE e⁻ IN TOTAL"
ʟLWR(16)→J
Disp "CENTER ATOM: "+sub(Str8,2J-1,2-(sub(Str8,2J,1)=" "))
ʟLWR(20)→F
"  "+%(LP)s+" LONE PAIR"→Str2
If int(L/2)≠1
Str2+"S"→Str2
Disp Str2+", FC "+%(FCT)s
Z+4→Z
If fPart(L/2)
Then
Disp "  + 1 UNPAIRED e⁻"
Z+1→Z
End
Disp "BONDED TO:"
Z+1→Z
For(I,1,M)
100ʟLWT(I)+10ʟLWH(I)+ʟLWO(I)→D
0→E
0→N
For(P,1,M)
If D=100ʟLWT(P)+10ʟLWH(P)+ʟLWO(P)
Then
N+1→N
If P<I
1→E
End
End
If not(E)
Then
%(NEED2)s
ʟLWT(I)→J
sub(Str8,2J-1,2-(sub(Str8,2J,1)=" "))+" ATOM"→Str6
If ʟLWH(I)
"O-H GROUP"→Str6
If N>1
Str6+"S"→Str6
sub("SINGLEDOUBLETRIPLE",6ʟLWO(I)-5,6)+" BOND"→Str2
If N>1
Str2+"S"→Str2
Disp %(N1)s+" "+Str6+", "+Str2
min(4,max(⁻4,ʟLWF(I)))→F
"  "→Str2
If N>1
"  EACH: "→Str2
Str2+sub("0123",ʟLWL(I)/2+1,1)+" LONE PAIR"→Str2
If ʟLWL(I)≠2
Str2+"S"→Str2
If N>1
Str2+" FC "→Str2
If N=1
Str2+", FC "→Str2
Disp Str2+%(FCT)s
Z+2→Z
End
End
If θ
Then
%(NEED1)s
"H ATOM"→Str6
If θ>1
"H ATOMS"→Str6
"SINGLE BOND"→Str2
If θ>1
"SINGLE BONDS"→Str2
Disp %(TH)s+" "+Str6+", "+Str2
End
Output(10,17,"ENTER=NEXT")
Pause
If ʟLWR(21)
Goto E
ClrHome
Y→ʟLWR(19)
X→ʟLWR(20)
M+θ→D
int((L+1)/2)→E
D+E→S
E→L
prgmMT2G
Disp "STERIC NUMBER (SN): "+%(SS)s
" = "+%(DD)s+" ATOM"→Str2
If D≠1
Str2+"S"→Str2
Str2+" + "+%(LL)s+" LONE PAIR"→Str2
If L≠1
Str2+"S"→Str2
Disp Str2
Disp "ELECTRON GEOMETRY:","  "+Str4,"MOLECULAR GEOMETRY:","  "+Str5,"BOND ANGLE:","  "+Str6
Output(10,17,"ENTER=NEXT")
Pause
ClrHome
Disp "HYBRIDIZATION: "+Str7
Disp "SIGMA (σ) BONDS: "+%(SIG)s
Disp "PI (π) BONDS: "+%(PI)s
ʟLWR(19)→E
If E>8
Disp "EXPANDED OCTET: "+%(E2)s+" e⁻"
If E=8
Disp "OCTET COMPLETE (8 e⁻)"
If E<8 and not(fPart(E/2))
Disp "INCOMPLETE OCTET: "+%(E1)s+" e⁻"
If fPart(E/2)
Disp "RADICAL: 1 UNPAIRED e⁻"
If C
Then
Disp "POLARITY: N/A (ION)"
Else
1→E
For(I,1,M)
If ʟLWT(I)≠ʟLWT(1) or ʟLWH(I)
0→E
End
If θ and M
0→E
If D=1 and M=1
(ʟLWT(1)=ʟLWR(16) and not(ʟLWH(1)))→E
If D=1 and θ=1
0→E
If E and (Y or D=1)
Then
Disp "NONPOLAR MOLECULE"
Else
Disp "POLAR MOLECULE"
End
End
Disp "OTHER RESONANCE FORMS: "+%(RES)s
0→E
For(I,1,M)
If ʟLWT(I)=4
1→E
End
If E and D≥2
Disp "CHECK: MAY HAVE 2+","  CENTER ATOMS"
If ʟLWR(19)>8 and ʟLWS(B)<9ᴇ99
Output(10,8,"ENTER=OCTET VERSION")
If ʟLWR(19)≤8 or ʟLWS(B)=9ᴇ99
Output(10,17,"ENTER=MENU")
Pause
If ʟLWR(19)>8 and ʟLWS(B)<9ᴇ99
Then
1→ʟLWR(21)
ʟLWU(B)→O
ʟLWQ(B)→Q
End
If ʟLWR(21)
Goto D
Lbl E
Menu("LEWIS SOLVER","NEW MOLECULE",S,"WHAT DOES IT MEAN?",H,"BACK",R)
Lbl H
prgmMT2H
Goto E
Lbl R
DelVar ʟLWV
DelVar ʟLWE
DelVar ʟLWP
DelVar ʟLWT
DelVar ʟLWH
DelVar ʟLWB
DelVar ʟLWO
DelVar ʟLWL
DelVar ʟLWF
DelVar ʟLWR
DelVar ʟLWA
DelVar ʟLWN
DelVar ʟLWS
DelVar ʟLWU
DelVar ʟLWQ
Return
""" % {
    "SETUP": SETUP.strip(), "BUILD": BUILD.strip(), "DECODE": DECODE.strip(),
    "EVAL": EVAL.strip(), "UPDATE": UPDATE.strip(),
    "FCC": FCS % "C", "FCF": FCS % "F", "V2": d2("V"),
    "LP": d1("int(L/2)"), "N1": d1("N"), "TH": d1("θ"),
    "SS": d1("S"), "DD": d1("D"), "LL": d1("L"),
    "SIG": d1("min(9,D+O)"), "PI": d1("(ʟLWR(20)-D)"),
    "E2": d2("E"), "E1": d1("E"), "RES": d1("min(9,ʟLWR(5)-1)"),
    "FCT": 'sub("-4-3-2-1 0+1+2+3+4",2F+9+(F=0),2-(F=0))',
    "NEED1": NEEDP % 1, "NEED2": NEEDP % 2,
}

# ---------------------------------------------------------------- notes
N = []  # main program pieces

N.append(menu("0", "MIDTERM 2  CHEM 105", [
    ("SN+LP ► SHAPE SOLVER", "S"), ("LEWIS SOLVER", "L"),
    ("VSEPR & HYBRID ►", "V"), ("σ π BONDS & MO ►", "M"),
    ("BANDS & CONDUCTION ►", "B"), ("MORE ►", "X"), ("QUIT", "Q")]))
N.append("Lbl S\nprgmMT2SN\nGoto 0\nLbl L\nprgmMT2LW\nGoto 0\nLbl Q\nClrHome\nStop")
N.append(menu("X", "MORE", [
    ("POLYATOMIC IONS ►", "A"), ("ISOMERS ►", "I"), ("ORGANIC GROUPS ►", "O"),
    ("FC & LEWIS RULES ►", "F"), ("THEORY COMPARE ►", "T"),
    ("BACK", "0"), ("QUIT", "Q")]))

# VSEPR & hybridization
N.append(menu("V", "VSEPR & HYBRIDIZATION", [
    ("ALL SHAPES TABLE", "V1"), ("SN 2, 3, 4 DETAIL", "V2"),
    ("SN 5, 6 DETAIL", "V3"), ("HYBRIDIZATION RULES", "V4"),
    ("VSEPR RULES", "V5"), ("BACK", "0"), ("QUIT", "Q")]))

SHORT = {"TRIGONAL PLANAR": "TRIG PLANAR", "TRIGONAL PYRAMIDAL": "TRIG PYRAM",
         "TRIGONAL BIPYRAMIDAL": "TRIG BIPYR", "SQUARE PYRAMIDAL": "SQ PYRAM",
         "SQUARE PLANAR": "SQ PLANAR", "LINEAR (DIATOMIC)": "LINEAR"}
SHORT_ANG = {"<109.5° (NH₃ 107°)": "<109.5°", "<109.5° (H₂O 104.5°)": "<109.5°",
             "90° 120° 180°": "90/120/180", "<90° AND <120°": "<90 <120",
             "90° 180°": "90° 180°"}
tab = ["S/L SHAPE       ANGLE", "(SN/LONE PAIRS)"]
for sn, lp, eg, sh, ang, hyb, ex, sym in SHAPES:
    if lp == sn - 1:
        continue  # diatomic-only rows are covered in the detail pages
    tab.append("%d/%d %-12s%s" % (sn, lp, SHORT.get(sh, sh), SHORT_ANG.get(ang, ang)))
N.append(pages("V1", "V", tab[:10] + [tab[0]] + tab[10:]))


def detail(sns):
    ents = []
    for s in sns:
        rows = [r for r in SHAPES if r[0] == s]
        ents.append(["SN %d: EG %s" % (s, SHORT.get(rows[0][2], rows[0][2])),
                     "  HYBRID %s" % rows[0][5]])
        for sn, lp, eg, sh, ang, hyb, ex, sym in rows:
            ents.append(["%d LP: %s" % (lp, sh), "  %s" % ang, "  EX: %s" % ex])
    return ents


N.append(blocks("V2", "V", detail([2, 3, 4])))
N.append(blocks("V3", "V", detail([5, 6])))
N.append(pages("V4", "V", [
    "HYBRIDIZATION FROM SN", "SN 2 ► sp      (2 HYBRIDS)", "SN 3 ► sp²     (3)",
    "SN 4 ► sp³     (4)", "SN 5 ► sp³d    (5)", "SN 6 ► sp³d²   (6)",
    "# HYBRID ORBITALS = SN", "ORDER: s FIRST, THEN p,", "  THEN d", "",
    "LEFTOVER p ► π BONDS", "sp: 2 p LEFT (TRIPLE OR", "  2 DOUBLE BONDS)",
    "sp²: 1 p LEFT (1 DOUBLE)", "sp³: 0 p LEFT (ALL SINGLE)",
    "SINGLE = 1σ", "DOUBLE = 1σ + 1π", "TRIPLE = 1σ + 2π",
    "σ: HYBRID OVERLAP END-ON", "π: UNHYBRID p SIDE-BY-SIDE"]))
N.append(pages("V5", "V", [
    "VSEPR BASICS", "e⁻ DOMAINS REPEL ► SPREAD", "  AS FAR APART AS POSSIBLE",
    "DOMAIN = BONDED ATOM OR LP", "DBL/TRIPLE BOND = 1 DOMAIN",
    "SN = ATOMS + LONE PAIRS", "EG: COUNTS ALL DOMAINS", "SHAPE: ATOMS ONLY",
    "REPULSION: LP-LP > LP-BP", "  > BP-BP",
    "LP TAKE MORE ROOM ►", "  BOND ANGLES SHRINK", "SN 5: LP GO EQUATORIAL",
    "SN 6: 2 LP GO OPPOSITE", "  (180° APART)", "POLAR IF SHAPE IS",
    "  ASYMMETRIC OR OUTER", "  ATOMS ARE DIFFERENT"]))

# sigma / pi / MO
N.append(menu("M", "σ π BONDS & MO THEORY", [
    ("SIGMA VS PI", "M1"), ("ANTIBONDING & NODES", "M2"), ("MO FILL ORDER", "M3"),
    ("BOND ORDER & MAGNETISM", "M4"), ("MO EXAMPLES", "M5"),
    ("BACK", "0"), ("QUIT", "Q")]))
N.append(pages("M1", "M", [
    "σ (SIGMA) BOND", "END-ON (HEAD-TO-HEAD)", "  OVERLAP ON THE BOND AXIS",
    "e⁻ DENSITY ON THE AXIS,", "  BETWEEN THE NUCLEI", "FROM s+s, s+p, p+p END-ON,",
    "  OR HYBRID ORBITALS", "FREE ROTATION ALLOWED", "EVERY BOND HAS EXACTLY 1σ",
    "STRONGER THAN A π BOND",
    "σ PICTURE (END-ON):", "s+s: (+A)(+B)", "  ► (+  A  B  +)", "  ONE BLOB AROUND THE AXIS",
    "p+p: (-)A(+)(+)B(-)", "  ► BIG OVERLAP BETWEEN", "  A AND B, ON THE AXIS", "",
    "AXIS = LINE THROUGH", "  BOTH NUCLEI",
    "π (PI) BOND", "SIDE-BY-SIDE OVERLAP OF", "  PARALLEL p ORBITALS",
    "e⁻ DENSITY ABOVE AND BELOW", "  THE AXIS (NOT ON IT)", "NODAL PLANE ON THE AXIS",
    "NO FREE ROTATION", "ONLY IN DOUBLE/TRIPLE", "DBL = 1σ+1π  TRPL = 1σ+2π", "",
    "π PICTURE (SIDE-BY-SIDE):", "  (+)  (+)      (  +  )", "   A    B   ►    A---B",
    "  (-)  (-)      (  -  )", "TOP LOBES MERGE, BOTTOM", "  LOBES MERGE",
    "AXIS ITSELF = NODE (0 e⁻)"]))
N.append(pages("M2", "M", [
    "ANTIBONDING (*) ORBITALS", "OUT-OF-PHASE OVERLAP", "  (+ MEETS -)",
    "NODE BETWEEN THE NUCLEI", "  (0 e⁻ DENSITY THERE)", "HIGHER ENERGY THAN THE",
    "  ATOMIC ORBITALS", "e⁻ IN * ORBITALS WEAKEN", "  THE BOND", "",
    "σ* (END-ON, OUT OF PHASE):", "  (+A)(-B) ► (+A) ! (-B)", "  ! = NODE PLANE CUTTING",
    "  THE AXIS BETWEEN NUCLEI", "π* (SIDE, OUT OF PHASE):", "  (+)  (-)      (+) ! (-)",
    "   A    B   ►    A  !  B", "  (-)  (+)      (-) ! (+)", "  NODES: AXIS PLANE AND",
    "  PLANE BETWEEN NUCLEI",
    "NODAL PLANES:", "σ   0", "σ*  1 (BETWEEN NUCLEI)", "π   1 (ALONG THE AXIS)",
    "π*  2 (AXIS + BETWEEN)", "MORE NODES ► HIGHER ENERGY"]))
N.append(pages("M3", "M", [
    "MO FILL ORDER (LOW ► HIGH)", "B₂ C₂ N₂ (Z ≤ 7):", "  s-p MIXING",
    " σ2s σ*2s π2p π2p", " σ2p π*2p π*2p σ*2p", "  π2p FILLS BEFORE σ2p",
    "  (SMALL 2s-2p GAP)", "", "O₂ F₂ Ne₂ (Z ≥ 8, O+):", "  NO s-p MIXING",
    " σ2s σ*2s σ2p π2p π2p", " π*2p π*2p σ*2p", "  σ2p FILLS BEFORE π2p", "",
    "FILL LIKE ATOMS: AUFBAU,", "  PAULI, HUND (1 e⁻ IN", "  EACH π BEFORE PAIRING)",
    "IONS: USE THE ELEMENT", "  ORDER (O₂⁻ ► O ORDER)", "USE VALENCE e⁻ ONLY"]))
N.append(pages("M4", "M", [
    "BOND ORDER", "BO = (BONDING e⁻ -", "  ANTIBONDING e⁻) / 2",
    "BO 0 ► NO STABLE BOND", "HIGHER BO ► STRONGER,", "  SHORTER BOND", "",
    "PARAMAGNETIC: UNPAIRED e⁻", "  (PULLED INTO FIELD)", "DIAMAGNETIC: ALL PAIRED",
    "  (SLIGHTLY REPELLED)", "O₂ IS PARAMAGNETIC", "  (ONLY MO EXPLAINS IT)"]))
N.append(pages("M5", "M", [
    "     VAL e⁻  BO   MAGNET", "H₂     2     1    DIA", "He₂    4     0    NONE",
    "Li₂    2     1    DIA", "Be₂    4     0    NONE", "B₂     6     1    PARA",
    "C₂     8     2    DIA", "N₂    10     3    DIA", "O₂    12     2    PARA",
    "F₂    14     1    DIA",
    "     VAL e⁻  BO   MAGNET", "Ne₂   16     0    NONE", "N₂+    9    2.5   PARA",
    "O₂+   11    2.5   PARA", "O₂⁻   13    1.5   PARA", "O₂²⁻  14     1    DIA",
    "NO    11    2.5   PARA", "CO    10     3    DIA", "CN⁻   10     3    DIA",
    "NO+   10     3    DIA"]))

# bands
N.append(menu("B", "BAND THEORY", [
    ("BAND BASICS", "B1"), ("GAP & CONDUCTIVITY", "B2"), ("TEMPERATURE & LIGHT", "B3"),
    ("N-TYPE DOPING", "B4"), ("P-TYPE DOPING", "B5"), ("BACK", "0"), ("QUIT", "Q")]))
N.append(pages("B1", "B", [
    "BAND THEORY = MO THEORY", "  FOR A WHOLE SOLID", "N ATOMIC ORBITALS ► N MOs",
    "HUGE N ► MOs MERGE INTO", "  CONTINUOUS BANDS", "VALENCE BAND: FILLED",
    "  (FROM BONDING MOs)", "CONDUCTION BAND: EMPTY", "  (FROM ANTIBONDING MOs)",
    "BAND GAP Eg = ENERGY GAP", "  BETWEEN THE TWO BANDS", "e⁻ MUST REACH THE",
    "  CONDUCTION BAND TO MOVE"]))
N.append(pages("B2", "B", [
    "SMALL GAP ► HIGH CONDUCT.", "LARGE GAP ► LOW CONDUCT.", "",
    "METAL (CONDUCTOR): NO GAP", "  (BANDS OVERLAP OR PART", "  FILLED) ► CONDUCTS BEST",
    "SEMICONDUCTOR: SMALL GAP", "  Si 1.1 eV  Ge 0.67 eV", "INSULATOR: LARGE GAP",
    "  DIAMOND C 5.5 eV",
    "GAP: INSULATOR >", "  SEMICONDUCTOR > METAL", "CONDUCTIVITY: METAL >",
    " SEMICONDUCTOR > INSULATOR", "DOWN A GROUP GAP SHRINKS:", "  C > Si > Ge > Sn",
    "  (CONDUCTIVITY GOES UP)"]))
N.append(pages("B3", "B", [
    "HEAT A METAL ► CONDUCTS", "  LESS (ATOMS VIBRATE,", "  SCATTER e⁻)",
    "HEAT A SEMICONDUCTOR ►", "  CONDUCTS MORE (MORE e⁻", "  JUMP THE GAP)",
    "LIGHT: PHOTON E ≥ Eg CAN", "  PROMOTE AN e⁻", "EMITTED LIGHT (LED): E=Eg",
    "SMALLER GAP ► LONGER λ", "  (REDDER)", "BIGGER GAP ► SHORTER λ", "  (BLUER)",
    "E = hc/λ", "λ(nm) = 1240 / E(eV)"]))
N.append(pages("B4", "B", [
    "N-TYPE (NEGATIVE)", "DOPE WITH ATOM THAT HAS", "  MORE VALENCE e⁻",
    "  Si (GRP 14) + P, As (15)", "EXTRA e⁻ IN DONOR LEVEL", "  JUST BELOW CONDUCTION",
    "  BAND", "MAJORITY CARRIER: e⁻", "CONDUCTIVITY GOES UP"]))
N.append(pages("B5", "B", [
    "P-TYPE (POSITIVE)", "DOPE WITH ATOM THAT HAS", "  FEWER VALENCE e⁻",
    "  Si (GRP 14) + B, Ga (13)", "MAKES HOLES (MISSING e⁻)", "ACCEPTOR LEVEL JUST",
    "  ABOVE VALENCE BAND", "MAJORITY CARRIER: HOLES", "CONDUCTIVITY GOES UP",
    "P-N JUNCTION = DIODE/LED"]))

# isomers
N.append(menu("I", "ISOMERS", [
    ("ISOMER TYPES (TREE)", "I1"), ("CONSTITUTIONAL", "I2"), ("STEREOISOMERS", "I3"),
    ("CONFORMERS", "I4"), ("HOW TO TELL", "I5"), ("BACK", "X"), ("QUIT", "Q")]))
N.append(pages("I1", "I", [
    "ISOMERS: SAME FORMULA,", "  DIFFERENT ARRANGEMENT", "1 CONSTITUTIONAL",
    "  (STRUCTURAL): DIFFERENT", "  CONNECTIVITY", "  - CHAIN", "  - POSITIONAL",
    "  - FUNCTIONAL GROUP", "2 STEREOISOMERS: SAME", "  CONNECTIVITY, DIFF. 3D",
    "  - CIS/TRANS (GEOMETRIC)", "  - ENANTIOMERS", "  - DIASTEREOMERS",
    "CONFORMERS: SAME MOLECULE", "  TWISTED ABOUT A σ BOND", "  (NOT TRUE ISOMERS)"]))
N.append(pages("I2", "I", [
    "CONSTITUTIONAL ISOMERS", "DIFFERENT BOND CONNECTIONS", "DIFFERENT NAMES AND",
    "  PROPERTIES (bp, mp)", "CHAIN: DIFFERENT CARBON", "  SKELETON (BRANCHING)",
    "  BUTANE vs ISOBUTANE", "POSITIONAL: SAME GROUP,", "  DIFFERENT POSITION",
    "  1-PROPANOL vs 2-PROPANOL",
    "FUNCTIONAL: DIFFERENT", "  FUNCTIONAL GROUP", "  ETHANOL (ALCOHOL) vs",
    "  DIMETHYL ETHER (C₂H₆O)"]))
N.append(pages("I3", "I", [
    "STEREOISOMERS", "SAME CONNECTIVITY,", "  DIFFERENT 3D ARRANGEMENT",
    "CIS/TRANS (GEOMETRIC):", "  C=C OR RING CAN NOT", "  ROTATE",
    "  CIS = SAME SIDE", "  TRANS = OPPOSITE SIDES", "  NEED 2 DIFFERENT GROUPS",
    "  ON EACH C OF THE C=C",
    "ENANTIOMERS: NON-", "  SUPERIMPOSABLE MIRROR", "  IMAGES (CHIRAL)",
    "CHIRAL CENTER: C WITH 4", "  DIFFERENT GROUPS", "ALL CENTERS FLIPPED",
    "SAME bp/mp; ROTATE PLANE-", "  POLARIZED LIGHT IN", "  OPPOSITE DIRECTIONS", "",
    "DIASTEREOMERS: STEREO-", "  ISOMERS NOT MIRROR", "  IMAGES; SOME (NOT ALL)",
    "  CENTERS FLIPPED", "  INCLUDES CIS/TRANS", "  DIFFERENT PROPERTIES",
    "MESO: CHIRAL CENTERS BUT", "  A MIRROR PLANE ► ACHIRAL",
    "MAX STEREOISOMERS = 2^n", "  n = # CHIRAL CENTERS"]))
N.append(pages("I4", "I", [
    "CONFORMERS", "SAME MOLECULE, DIFFERENT", "  SHAPE FROM ROTATING",
    "  ABOUT A SINGLE (σ) BOND", "INTERCONVERT FAST ► NOT", "  SEPARATE COMPOUNDS",
    "STAGGERED: LOWER ENERGY", "ECLIPSED: HIGHER ENERGY", "CYCLOHEXANE: CHAIR",
    "  (MORE STABLE) vs BOAT"]))
N.append(pages("I5", "I", [
    "SAME FORMULA? NO ►", "  NOT ISOMERS", "SAME CONNECTIVITY? NO ►",
    "  CONSTITUTIONAL", "YES ► ONLY σ ROTATION?", "  YES ► CONFORMERS",
    "  NO ► STEREOISOMERS:", "  MIRROR IMAGES ► ENANTIO", "  NOT MIRROR ► DIASTEREO",
    "  SUPERIMPOSABLE ► SAME"]))

# organic drawing
N.append(menu("O", "ORGANIC", [
    ("DRAWING RULES", "O1"), ("CARBOXYLIC ACID", "O2"), ("CARBOXYLATE", "O3"),
    ("AMINES", "O4"), ("OTHER GROUPS", "O5"), ("BACK", "X"), ("QUIT", "Q")]))
N.append(pages("O1", "O", [
    "ORGANIC LINE DRAWINGS", "EACH CORNER/END = C", "C ALWAYS HAS 4 BONDS",
    "H ON C NOT DRAWN (IMPLIED)", "  # H = 4 - LINES ON C", "OTHER ATOMS ARE DRAWN",
    "  (N, O...) AND THEIR H", "LONE PAIRS OFTEN NOT", "  DRAWN BUT ARE THERE", "",
    "NEUTRAL ATOM: BONDS + LP", "C        4 BONDS  0 LP", "N        3 BONDS  1 LP",
    "O        2 BONDS  2 LP", "F Cl Br I 1 BOND  3 LP", "H        1 BOND   0 LP",
    "CHARGED: N 4 BONDS = +1", "  O 3 BONDS 1 LP = +1", "  O 1 BOND 3 LP = -1",
    "  C 3 BONDS 1 LP = -1",
    "C SHAPE BY BONDS:", "4 SINGLE ► sp³ 109.5°", "1 DOUBLE ► sp² 120°",
    "TRIPLE OR 2 DBL ► sp 180°", "N, O: COUNT LP AS DOMAINS"]))

N.append(pages("O2", "O", [
    "CARBOXYLIC ACID: R-COOH", "  R-C(=O)-O-H", "  (R = REST OF MOLECULE)",
    "C: DOUBLE BOND TO ONE O,", "  SINGLE BOND TO THE OH", "C IS sp², TRIG PLANAR 120°",
    "WEAK ACID: GIVES UP THE H+", "  FROM THE O-H", "  R-COOH ► R-COO⁻ + H+",
    "NAME ENDS IN -OIC ACID", "  CH₃COOH = ETHANOIC ACID", "    (ACETIC ACID, VINEGAR)",
    "  HCOOH = METHANOIC ACID", "    (FORMIC ACID)", "POLAR + H-BONDS ►",
    "  HIGH BOILING POINT", "  SMALL ONES MIX WITH H₂O"]))
N.append(pages("O3", "O", [
    "CARBOXYLATE ION: R-COO⁻", "= CARBOXYLIC ACID THAT", "  LOST ITS H+",
    "  (ITS CONJUGATE BASE)", "CHARGE -1 SHARED BY BOTH", "  O ATOMS (RESONANCE)",
    "2 RESONANCE FORMS: THE", "  DOUBLE BOND SWITCHES", "  BETWEEN THE 2 O",
    "BOTH C-O BONDS ARE EQUAL", "  (BOND ORDER 1.5)", "C IS sp², TRIG PLANAR 120°",
    "NAME ENDS IN -OATE", "  CH₃COO⁻ = ETHANOATE", "    (ACETATE)",
    "SALT: CH₃COONa =", "  SODIUM ACETATE",
    "IN THE BODY (pH 7.4):", "  ACIDS ARE MOSTLY IN THE", "  CARBOXYLATE FORM"]))
N.append(pages("O4", "O", [
    "AMINE: N BONDED TO C", "  (NH₃ WITH H REPLACED", "  BY CARBON GROUPS)",
    "PRIMARY 1°:   R-NH₂", "SECONDARY 2°: R₂NH", "TERTIARY 3°:  R₃N",
    "  (COUNT C GROUPS ON N)", "N: 3 BONDS + 1 LONE PAIR", "  sp³, TRIG PYRAMIDAL",
    "  ABOUT 107° (LIKE NH₃)", "WEAK BASE: LONE PAIR", "  GRABS AN H+",
    "  R-NH₂ + H+ ► R-NH₃+", "  (AMMONIUM ION, N FC +1)", "NAME ENDS IN -AMINE",
    "  CH₃NH₂ = METHYLAMINE", "1° AND 2° HAVE N-H ►", "  CAN H-BOND",
    "AMINO ACIDS HAVE BOTH", "  -NH₂ AND -COOH", "IN THE BODY: -NH₃+ AND",
    "  -COO⁻ (ZWITTERION)", "AMIDE IS NOT AN AMINE:", "  N ON A C=O, R-C(=O)-N",
    "  NOT BASIC; PEPTIDE BOND"]))
N.append(pages("O5", "O", [
    "GROUP     FORMULA  NAME", "ALCOHOL   R-OH     -OL", "ETHER     R-O-R    ETHER",
    "ALDEHYDE  R-CHO    -AL", "KETONE    R-CO-R   -ONE", "CARB ACID R-COOH -OIC ACID",
    "CARBOXYLATE R-COO⁻ -OATE", "ESTER     R-COO-R  -OATE", "AMINE     R-NH₂    -AMINE",
    "AMIDE     R-CONH₂  -AMIDE"]))

# FC & Lewis rules
N.append(menu("F", "FORMAL CHARGE & LEWIS", [
    ("FC FORMULA", "F1"), ("BEST STRUCTURE", "F2"), ("LEWIS STEPS", "F3"),
    ("OCTET EXCEPTIONS", "F4"), ("RESONANCE", "F5"), ("BACK", "X"), ("QUIT", "Q")]))
N.append(pages("F1", "F", [
    "FORMAL CHARGE", "FC = V - L - B", " V = VALENCE e⁻ (GROUP)", " L = LONE-PAIR e⁻ (DOTS)",
    " B = # BONDS (LINES)", "SUM OF FC = ION CHARGE", "SHORTCUT (IF OCTET):",
    "  FC = BONDS - USUAL BONDS", "  N: 4 BONDS = +1", "  O: 1 BOND = -1"]))
N.append(pages("F2", "F", [
    "BEST LEWIS STRUCTURE", "1 OCTETS FIRST (C N O F", "  NEVER OVER 8 e⁻)",
    "2 FC AS CLOSE TO 0 AS", "  POSSIBLE", "3 NEGATIVE FC ON THE MOST",
    "  ELECTRONEGATIVE ATOM", "4 AVOID LIKE CHARGES ON", "  NEIGHBOR ATOMS",
    "PERIOD 3+ CAN EXPAND", "  OCTET TO LOWER FC", "  (ASK WHICH YOUR CLASS", "  WANTS)"]))
N.append(pages("F3", "F", [
    "LEWIS STRUCTURE STEPS", "1 COUNT VALENCE e⁻", "  (- ION: ADD e⁻,",
    "   + ION: SUBTRACT e⁻)", "2 CENTER = LEAST EN ATOM", "  (NEVER H; F IS OUTER)",
    "3 SINGLE BONDS TO CENTER", "4 FILL OUTER OCTETS", "5 LEFTOVER e⁻ ► CENTER",
    "6 CENTER SHORT? MOVE LP",
    "  IN ► DOUBLE/TRIPLE BOND", "7 CHECK FC, PICK BEST", "OXYACIDS: H GOES ON O",
    "  HNO₃ = HO-NO₂"]))
N.append(pages("F4", "F", [
    "OCTET EXCEPTIONS", "H: 2 e⁻ (1 BOND)", "Be: 4 e⁻   B, Al: 6 e⁻",
    "  (INCOMPLETE OCTET)", "ODD e⁻ (RADICALS):", "  NO  NO₂  ClO₂",
    "EXPANDED (PERIOD 3+ ONLY):", "  PCl₅ SF₆ XeF₄ I₃⁻", "PERIOD 2 (C N O F) NEVER",
    "  MORE THAN 8 e⁻"]))
N.append(pages("F5", "F", [
    "RESONANCE", "SAME ATOM POSITIONS,", "  DIFFERENT e⁻ PLACEMENT",
    "REAL ION = AVERAGE", "  (HYBRID), NOT FLIPPING", "BOND ORDER = TOTAL BONDS",
    "  / # OF THOSE LINKS", "  NO₃⁻ CO₃²⁻: 4/3 = 1.33", "  O₃ NO₂⁻: 3/2 = 1.5",
    "ALL THOSE BONDS EQUAL"]))

# theories
N.append(menu("T", "BONDING THEORIES", [
    ("LEWIS & VSEPR", "T1"), ("VALENCE BOND", "T2"), ("MO THEORY", "T3"),
    ("BAND THEORY", "T4"), ("WHICH ONE FOR WHAT", "T5"), ("BACK", "X"), ("QUIT", "Q")]))
N.append(pages("T1", "T", [
    "LEWIS STRUCTURES", "DOTS = LONE PAIRS", "LINES = SHARED PAIRS",
    "SHOWS: CONNECTIVITY, LP,", "  FC, RESONANCE, OCTETS", "CAN NOT: 3D SHAPE,",
    "  ENERGY, MAGNETISM", "  (O₂ DRAWN ALL PAIRED", "  BUT IS PARAMAGNETIC)", "",
    "VSEPR", "e⁻ DOMAINS REPEL", "SHOWS: 3D SHAPE, BOND", "  ANGLES, POLARITY",
    "NEEDS LEWIS FIRST", "CAN NOT: WHY BONDS FORM,", "  ORBITALS, BOND ENERGY"]))
N.append(pages("T2", "T", [
    "VALENCE BOND (VB) THEORY", "BOND = OVERLAP OF 2 HALF-", "  FILLED ORBITALS",
    "e⁻ PAIR LOCALIZED BETWEEN", "  2 ATOMS", "USES HYBRID ORBITALS",
    "  sp sp² sp³ sp³d sp³d²", "EXPLAINS σ AND π BONDS", "CAN NOT: O₂ MAGNETISM,",
    "  DELOCALIZED e⁻ (NEEDS", "  RESONANCE)"]))
N.append(pages("T3", "T", [
    "MOLECULAR ORBITAL THEORY", "ATOMIC ORBITALS COMBINE", "  ► MOs OVER THE WHOLE",
    "  MOLECULE (DELOCALIZED)", "# MOs = # ATOMIC ORBITALS", "BONDING (LOW E) AND",
    "  ANTIBONDING * (HIGH E)", "SHOWS: BOND ORDER,", "  MAGNETISM (O₂ PARA),",
    "  WHY He₂ DOES NOT EXIST", "CAN NOT (EASILY): SHAPE,", "  BIG MOLECULES"]))
N.append(pages("T4", "T", [
    "BAND THEORY", "MO THEORY FOR A SOLID", "  (HUGE # OF ATOMS)",
    "MOs BLUR INTO BANDS:", "  VALENCE + CONDUCTION", "SHOWS: CONDUCTOR vs",
    "  SEMICONDUCTOR vs", "  INSULATOR (BAND GAP),", "  DOPING, LEDs",
    "ONLY FOR SOLIDS"]))
N.append(pages("T5", "T", [
    "WHICH THEORY FOR WHAT", "CONNECTIONS, FC ► LEWIS", "SHAPE, ANGLES ► VSEPR",
    "HYBRIDS, σ/π ► VB", "BOND ORDER, MAGNET ► MO", "CONDUCTIVITY ► BAND",
    "LOCALIZED e⁻: LEWIS, VB", "DELOCALIZED e⁻: MO, BAND", "O₂ PARAMAGNETIC: ONLY",
    "  MO EXPLAINS IT"]))

# polyatomic ions (the user's class list), alphabetical by name
IONS = [
    ("C₂H₃O₂⁻", "ACETATE", ["CH₃ C TETRAHEDRAL 109.5°", "COO C TRIG PLANAR 120°"]),
    ("NH₄+", "AMMONIUM", ["N TETRAHEDRAL 109.5° sp³"]),
    ("N₃⁻", "AZIDE", ["LINEAR 180° (MIDDLE N sp)"]),
    ("HCO₃⁻", "BICARBONATE", ["C TRIG PLANAR 120° sp²", "(HYDROGEN CARBONATE)"]),
    ("HSO₃⁻", "BISULFITE", ["S TRIG PYRAM <109.5° sp³", "(HYDROGEN SULFITE)"]),
    ("CO₃²⁻", "CARBONATE", ["C TRIG PLANAR 120° sp²"]),
    ("ClO₃⁻", "CHLORATE", ["Cl TRIG PYRAM <109.5° sp³"]),
    ("Cl⁻", "CHLORIDE", ["1 ATOM: NOT POLYATOMIC,", "NO SHAPE"]),
    ("CrO₄²⁻", "CHROMATE", ["Cr TETRAHEDRAL 109.5°"]),
    ("CN⁻", "CYANIDE", ["LINEAR (2 ATOMS)  C sp"]),
    ("Cr₂O₇²⁻", "DICHROMATE", ["EACH Cr TETRAHEDRAL", "Cr-O-Cr LINK IS BENT"]),
    ("H₂PO₄⁻", "DIHYDROGEN PHOSPHATE", ["P TETRAHEDRAL 109.5° sp³"]),
    ("S₂²⁻", "DISULFIDE", ["LINEAR (2 ATOMS)  S sp³"]),
    ("HPO₄²⁻", "HYDROGEN PHOSPHATE", ["P TETRAHEDRAL 109.5° sp³"]),
    ("OH⁻", "HYDROXIDE", ["LINEAR (2 ATOMS)"]),
    ("ClO⁻", "HYPOCHLORITE", ["LINEAR (2 ATOMS)"]),
    ("NO₃⁻", "NITRATE", ["N TRIG PLANAR 120° sp²"]),
    ("NO₂⁻", "NITRITE", ["N BENT <120° sp²"]),
    ("ClO₄⁻", "PERCHLORATE", ["Cl TETRAHEDRAL 109.5° sp³"]),
    ("MnO₄⁻", "PERMANGANATE", ["Mn TETRAHEDRAL 109.5°"]),
    ("PO₄³⁻", "PHOSPHATE", ["P TETRAHEDRAL 109.5° sp³"]),
    ("SO₄²⁻", "SULFATE", ["S TETRAHEDRAL 109.5° sp³"]),
    ("SO₃²⁻", "SULFITE", ["S TRIG PYRAM <109.5° sp³"]),
    ("SCN⁻", "THIOCYANATE", ["C LINEAR 180° sp"]),
]
N.append(menu("A", "POLYATOMIC IONS & ACIDS", [
    ("ION LIST + SHAPES", "A1"), ("OXYANION PATTERN", "A2"), ("ACID NAMING", "A3"),
    ("COMMON ACIDS", "A4"), ("STRONG ACIDS", "A5"), ("BACK", "X"), ("QUIT", "Q")]))
ents = []
for f, nm, geo in IONS:
    first = f + "  " + nm
    if len(first) > 26:
        ents.append([f, "  " + nm] + [" " + g for g in geo])
    else:
        ents.append([first] + [" " + g for g in geo])
N.append(blocks("A1", "A", ents, header=["ANGLES = VSEPR PREDICTION", ""]))
N.append(pages("A2", "A", [
    "OXYANION PATTERN", "PER___ATE: 1 MORE O", "___ATE: BASE ION",
    "___ITE: 1 LESS O", "HYPO___ITE: 2 LESS O", "  ClO₄⁻ PERCHLORATE",
    "  ClO₃⁻ CHLORATE", "  ClO₂⁻ CHLORITE", "  ClO⁻  HYPOCHLORITE",
    "CHARGE STAYS THE SAME", "ADD H+ ► CHARGE GOES UP 1",
    "  CO₃²⁻ ► HCO₃⁻", "  PO₄³⁻ ► HPO₄²⁻ ► H₂PO₄⁻", "BI- = HYDROGEN",
    "  BISULFITE = HSO₃⁻"]))
N.append(pages("A3", "A", [
    "ACID NAMING", "-IDE ION ► HYDRO___IC", "  Cl⁻ ► HCl HYDROCHLORIC",
    "-ATE ION ► ___IC ACID", "  NO₃⁻ ► HNO₃ NITRIC", "-ITE ION ► ___OUS ACID",
    "  NO₂⁻ ► HNO₂ NITROUS", "S AND P GET -UR/-OR:", "  SULFURIC, SULFUROUS,",
    "  PHOSPHORIC"]))
N.append(pages("A4", "A", [
    "HCl   HYDROCHLORIC", "HBr   HYDROBROMIC", "HI    HYDROIODIC", "HF    HYDROFLUORIC",
    "HCN   HYDROCYANIC", "H₂S   HYDROSULFURIC", "HNO₃  NITRIC", "HNO₂  NITROUS",
    "H₂SO₄ SULFURIC", "H₂SO₃ SULFUROUS",
    "H₃PO₄ PHOSPHORIC", "H₂CO₃ CARBONIC", "HC₂H₃O₂ ACETIC", "HClO₄ PERCHLORIC",
    "HClO₃ CHLORIC", "HClO₂ CHLOROUS", "HClO  HYPOCHLOROUS", "H₂CrO₄ CHROMIC"]))
N.append(pages("A5", "A", [
    "STRONG ACIDS (100% IONIZE)", "  HCl  HBr  HI", "  HNO₃  H₂SO₄  HClO₄",
    "  (HClO₃ OFTEN COUNTED)", "ALL OTHERS ARE WEAK", "HF IS WEAK!"]))


HELP = [
    ["WHAT THE RESULTS MEAN", ""],
    ["VALENCE e⁻: OUTER e⁻ THAT", "  FORM BONDS (ADD e⁻ FOR A", "  - ION, SUBTRACT FOR +)"],
    ["LONE PAIR: 2 e⁻ ON ONE", "  ATOM, NOT SHARED (DOTS)"],
    ["SINGLE BOND = 1 LINE", "DOUBLE BOND = 2 LINES", "TRIPLE BOND = 3 LINES"],
    ["FC = FORMAL CHARGE: THE", "  CHARGE AN ATOM SEEMS TO", "  HAVE IN THE DRAWING",
     "  FC = VALENCE - DOTS -", "    LINES", "  BEST DRAWING: ALL FC AS", "  CLOSE TO 0 AS POSSIBLE"],
    ["CENTER ATOM: THE ONE THE", "  OTHERS BOND TO"],
    ["STERIC NUMBER (SN) =", "  ATOMS ON THE CENTER +", "  LONE PAIRS ON THE CENTER"],
    ["ELECTRON GEOMETRY: SHAPE", "  OF ATOMS + LONE PAIRS"],
    ["MOLECULAR GEOMETRY: SHAPE", "  OF THE ATOMS ONLY (WHAT", "  THE MOLECULE LOOKS LIKE)",
     "  SAME AS ELECTRON GEOM.", "  IF CENTER HAS NO LONE", "  PAIRS",
     "(NEITHER ONE IS MO THEORY)"],
    ["BOND ANGLE: ANGLE BETWEEN", "  2 BONDS ON THE CENTER"],
    ["HYBRIDIZATION: MIXED", "  ORBITALS ON THE CENTER", "  SN 2 sp, 3 sp², 4 sp³,", "  5 sp³d, 6 sp³d²"],
    ["SIGMA σ: EVERY BOND HAS 1", "PI π: THE EXTRA LINES IN", "  DOUBLE/TRIPLE BONDS"],
    ["OCTET: 8 e⁻ AROUND AN ATOM", "  EXPANDED: OVER 8", "  (ONLY PERIOD 3 AND UP)",
     "  INCOMPLETE: UNDER 8", "  (H, Be, B, Al)"],
    ["POLAR: CHARGE IS LOPSIDED", "  (UNEVEN SHAPE OR MIXED", "  OUTER ATOMS)"],
    ["OTHER RESONANCE FORMS: #", "  OF OTHER EQUALLY GOOD", "  DRAWINGS (SAME ATOMS,",
     "  DOUBLE BOND MOVED)", "  0 = ONLY ONE DRAWING", "  REAL MOLECULE = AVERAGE"],
]
MT2H = blocks("1", "", HELP, end="Return")

MIDTERM2 = "\n".join(N)

PROGRAMS = {
    "MIDTERM2": MIDTERM2,
    "MT2SN": MT2SN,
    "MT2LW": MT2LW,
    "MT2G": mt2g(),
    "MT2H": MT2H,
}
