# -*- coding: utf-8 -*-
"""TI-BASIC source for the CHEM 105 calculator (TI-84 Plus CE).

Each entry in PROGRAMS is program-name -> TI-BASIC source text.
build.py turns these into .8xp files and readable .txt source.
Note: inside strings never use the store arrow (it ends a string on the calc);
use ► instead.
"""

FOOT_W = 26


def pages(lines, back, per=9):
    """Show a list of text lines as screens of `per` lines, ENTER to advance.
    Ends with Goto `back`."""
    chunks = [lines[i:i + per] for i in range(0, len(lines), per)] or [[]]
    out = []
    n = len(chunks)
    for i, ch in enumerate(chunks, 1):
        out.append("ClrHome")
        # Disp in groups of 3 to keep lines readable in the editor
        for j in range(0, len(ch), 3):
            out.append("Disp " + ",".join('"%s"' % s for s in ch[j:j + 3]))
        foot = ("ENTER=NEXT  %d/%d" % (i, n)) if i < n else ("ENTER=BACK  %d/%d" % (i, n))
        out.append('Output(10,%d,"%s")' % (FOOT_W - len(foot) + 1, foot))
        out.append("Pause")
    out.append("ClrHome")
    out.append("Goto " + back)
    return "\n".join(out)


PROGRAMS = {}

# ---------------------------------------------------------------- MAIN
PROGRAMS["CHEM"] = r'''
ClrHome
Lbl 0
Menu("CHEM 105","UNITS ×10^x k μ n",1,"MATTER ρ=m/V n=m/M",2,"LIGHT E=hv c=λv Φ",3,"ATOM λ=h/mv Δx n l",4,"MY NOTES",5,"EQUATION SHEET",6,"MORE/SI TABLE/QUIT",7)
Lbl 1
prgmCHUNIT
Goto 0
Lbl 2
prgmCHMATTR
Goto 0
Lbl 3
prgmCHLIGHT
Goto 0
Lbl 4
prgmCHATOM
Goto 0
Lbl 5
prgmCHNOTES
Goto 0
Lbl 6
prgmCHEQN
Goto 0
Lbl 7
prgmCHREF
Goto 0
'''

# ---------------------------------------------------------------- UNITS
_prefix_labels = [("V1", 1), ("V2", 2), ("V3", 3), ("V4", 4), ("V5", 5), ("V6", 6), ("V7", 7),
                  ("V8", 8), ("V9", 9), ("W1", 10), ("W2", 11), ("W3", 12), ("W4", 13),
                  ("W5", 14), ("W6", 15), ("W7", 16), ("W8", 17)]
_prefix_lbl_code = "\n".join("Lbl %s\n%d→I\nGoto P9" % (l, i) for l, i in _prefix_labels)
_q_lbl_code = "\n".join("Lbl Q%d\n%d→I\nGoto U8" % (i, i) for i in range(1, 8))

PROGRAMS["CHUNIT"] = r'''
{18,15,12,9,6,3,2,1,0,⁻1,⁻2,⁻3,⁻6,⁻9,⁻12,⁻15,⁻18}→ʟPRE
"E P T G M k h dab d c m μ n p f a "→Str9
Lbl 0
1→U
Menu("UNIT CONVERT","PREFIX k►m►μ ×10^x",A,"PREFIX² ³ cm³►m³",B,"AUTO PREFIX 10^x",C,"LENGTH in ft mi m",D,"MASS lb oz g amu",E,"VOL PRES ENERGY TEMP",F,"BACK",Z)
Lbl Z
ClrHome
Return
Lbl B
Menu("SQUARED/CUBED UNIT","² AREA  cm²►m²",B2,"³ VOLUME  cm³►m³",B3,"BACK",0)
Lbl B2
2→U
Goto A
Lbl B3
3→U
Lbl A
ClrHome
Disp "PREFIX CONVERTER","(ANY BASE UNIT)"
Input "VALUE:",X
1→N
"FROM PREFIX:"→Str7
Lbl P0
Menu(Str7,"BIG    E P T G M",PB,"MEDIUM k h da b d c m",PM,"SMALL  μ n p f a",PS,"BACK",0)
Lbl PB
Menu(Str7,"E  exa    10^18",V1,"P  peta   10^15",V2,"T  tera   10^12",V3,"G  giga   10^9",V4,"M  mega   10^6",V5)
Lbl PM
Menu(Str7,"k  kilo   10^3",V6,"h  hecto  10^2",V7,"da deca   10^1",V8,"b  BASE   10^0",V9,"d  deci   10^⁻1",W1,"c  centi  10^⁻2",W2,"m  milli  10^⁻3",W3)
Lbl PS
Menu(Str7,"μ  micro  10^⁻6",W4,"n  nano   10^⁻9",W5,"p  pico   10^⁻12",W6,"f  femto  10^⁻15",W7,"a  atto   10^⁻18",W8)
''' + _prefix_lbl_code + r'''
Lbl P9
If N=2
Goto P8
I→F
2→N
"TO PREFIX:"→Str7
Goto P0
Lbl P8
U(ʟPRE(F)-ʟPRE(I))→E
X*10^(E)→R
ClrHome
Disp "FROM "+sub(Str9,2F-1,2)+"   TO "+sub(Str9,2I-1,2)
If U=2
Disp "(SQUARED UNITS)"
If U=3
Disp "(CUBED UNITS)"
Disp "MULTIPLY BY 10^"
Output(2+(U>1),16,E)
Disp "","START:",X,"ANSWER:",R
Pause
Goto 0
Lbl C
ClrHome
Disp "AUTO PREFIX","ENTER VALUE IN BASE","UNIT (m, g, L, s, J...)"
Input "VALUE:",X
If X=0
Goto C9
int(log(abs(X)))→E
If abs(X)/10^E≥10
E+1→E
If abs(X)/10^E<1
E-1→E
3int(E/3)→G
max(⁻18,min(18,G))→G
9→I
For(J,1,17)
If ʟPRE(J)=G
J→I
End
ClrHome
Disp "START:",X,"","SCIENTIFIC NOTATION:"
Output(5,1,X/10^E)
Output(5,16,"×10^")
Output(5,20,E)
Output(7,1,"WITH PREFIX:")
Output(8,1,X/10^G)
Output(8,16,sub(Str9,2I-1,2))
Output(8,19,"(10^")
Output(8,23,G)
Pause
Goto 0
Lbl C9
Disp "0 HAS NO PREFIX"
Pause
Goto 0
Lbl D
{0.0254,0.3048,0.9144,1609.344,0.01,1,1000}→ʟUF
"in   ft   yd   mi   cm   m    km   "→Str8
"LENGTH"→Str6
1→K
Goto U0
Lbl E
{453.59237,453.59237/16,453.59237/12,2000*453.59237,1.660538ᴇ⁻24,1,1000}→ʟUF
"lb   oz   ozt  ton  amu  g    kg   "→Str8
"MASS"→Str6
2→K
Goto U0
Lbl F
Menu("MORE UNITS","VOLUME gal qt L mL",G,"PRESSURE atm torr Pa",H,"ENERGY J cal eV",I,"TEMP °F °C K",T,"BACK",0)
Lbl G
{3.7854,3.7854/4,0.0295735,0.0164,1,0.001,0.001}→ʟUF
"gal  qt   fl ozin³  L    mL   cm³  "→Str8
"VOLUME"→Str6
3→K
Goto U0
Lbl H
{101325,101325/760,101325/14.6959,101325/406.783,100000,1,1000}→ʟUF
"atm  torr psi  inH₂Obar  Pa   kPa  "→Str8
"PRESSURE"→Str6
4→K
Goto U0
Lbl I
{1,1000,1/0.239,1000/0.239,101.325,1.602ᴇ⁻19}→ʟUF
"J    kJ   cal  kcal L atmeV   "→Str8
"ENERGY"→Str6
5→K
Lbl U0
ClrHome
Disp Str6
Input "VALUE:",X
1→N
Str6+" FROM:"→Str7
Lbl U1
If K=1
Goto M1
If K=2
Goto M2
If K=3
Goto M3
If K=4
Goto M4
Menu(Str7,"J   joule",Q1,"kJ  kilojoule",Q2,"cal calorie",Q3,"kcal",Q4,"L atm",Q5,"eV  electron volt",Q6)
Lbl M1
Menu(Str7,"in  inch",Q1,"ft  foot",Q2,"yd  yard",Q3,"mi  mile",Q4,"cm",Q5,"m   meter",Q6,"km",Q7)
Lbl M2
Menu(Str7,"lb  pound",Q1,"oz  ounce (avdp)",Q2,"ozt troy ounce",Q3,"ton (2000 lb)",Q4,"amu",Q5,"g   gram",Q6,"kg",Q7)
Lbl M3
Menu(Str7,"gal (US)",Q1,"qt  (US)",Q2,"fl oz (US)",Q3,"in³",Q4,"L   liter",Q5,"mL",Q6,"cm³ (=mL)",Q7)
Lbl M4
Menu(Str7,"atm",Q1,"torr = mmHg",Q2,"psi  lb/in²",Q3,"in H₂O",Q4,"bar",Q5,"Pa",Q6,"kPa",Q7)
''' + _q_lbl_code + r'''
Lbl U8
If N=2
Goto U9
I→F
2→N
Str6+" TO:"→Str7
Goto U1
Lbl U9
X*ʟUF(F)/ʟUF(I)→R
ClrHome
Disp Str6,"FROM "+sub(Str8,5F-4,5),X,"TO "+sub(Str8,5I-4,5),R,"","FACTOR (MULTIPLY BY):",ʟUF(F)/ʟUF(I)
Pause
Goto 0
Lbl T
ClrHome
Disp "TEMPERATURE"
Input "VALUE:",X
Menu("TEMP FROM:","°F  FAHRENHEIT",T1,"°C  CELSIUS",T2,"K   KELVIN",T3)
Lbl T1
(X-32)*5/9→C
Goto T4
Lbl T2
X→C
Goto T4
Lbl T3
X-273.15→C
Lbl T4
ClrHome
Disp "TF=(9/5)TC+32","TK=TC+273.15","°F:",9C/5+32,"°C:",C,"K:",C+273.15
Pause
Goto 0
'''

# ---------------------------------------------------------------- SIG FIG HELPER
# In: Str3 (number typed as text). Out: S = # sig figs, P = power of ten of
# the last significant digit (e.g. 43.7 -> -1, 200 -> 2).
PROGRAMS["CHSFN"] = r'''
0→W
inString(Str3,"ᴇ")→K
If K>1
Then
expr(sub(Str3,K+1,length(Str3)-K))→W
sub(Str3,1,K-1)→Str3
End
If sub(Str3,1,1)="⁻" and length(Str3)>1
sub(Str3,2,length(Str3)-1)→Str3
length(Str3)→L
inString(Str3,".")→D
0→F
0→G
For(J,1,L)
sub(Str3,J,1)→Str5
If inString("123456789",Str5)
Then
If not(F)
J→F
J→G
End
End
0→S
0→P
If F
Then
If D
Then
L-F+1-(D>F)→S
D-L→P
Else
G-F+1→S
L-G→P
End
End
P+W→P
'''

# ---------------------------------------------------------------- MATTER
PROGRAMS["CHMATTR"] = r'''
6.022141ᴇ23→N
Lbl 0
Menu("MATTER & MOLES","SIG FIGS  4.50►3 SF",S,"DENSITY ρ=m/V",D,"MOLES n=m/M #=n×NA",M,"ISOTOPE AVG Σ(m×%)",I,"SAME # e⁻/p+ Mg►Ca",J,"BACK",Z)
Lbl Z
ClrHome
Return
Lbl J
prgmCHION
Goto 0
Lbl S
Menu("SIG FIGS","COUNT SIG FIGS",S1,"ROUND TO N SIG FIGS",S2,"CALC +- PLACE ×/ SF",S3,"RULES",S4,"BACK",0)
Lbl S1
ClrHome
Disp "TYPE IT EXACTLY:","KEEP 0S + DECIMAL PT","USE EE FOR ×10^"
Input "NUMBER:",Str3
prgmCHSFN
Disp "","SIG FIGS:",S,"LAST SIG DIGIT 10^x:",P
If not(S)
Disp "(ALL ZEROS)"
Pause
Goto S
Lbl S2
ClrHome
Input "NUMBER:",X
Input "# SIG FIGS:",A
If X=0
Goto S8
int(log(abs(X)))→E
If abs(X)/10^E≥10
E+1→E
If abs(X)/10^E<1
E-1→E
E-A+1→Q
round(X/10^Q,0)*10^Q→R
int(log(abs(R)))→B
If abs(R)/10^B≥10
B+1→B
ClrHome
Disp "ROUNDED:",R,"MANTISSA:",R/10^B,"×10^",B,"ADD TRAILING 0S IF","NEEDED TO SHOW ALL SF"
Pause
Goto S
Lbl S8
Disp "0 STAYS 0"
Pause
Goto S
Lbl S3
ClrHome
Disp "TYPE THE CALC, E.G.","21+43.7   44.0*3","(-) KEY FOR NEGATIVE","MIX +- AND ×/ ONE STEP","AT A TIME"
Input "CALC:",Str1
expr(Str1)→X
99→M
⁻99→Q
0→A
0→B
""→Str2
Str1+")"→Str1
For(I,1,length(Str1))
sub(Str1,I,1)→Str6
If inString("0123456789.ᴇ⁻",Str6)
Then
Str2+Str6→Str2
Else
If length(Str2)
Then
Str2→Str3
prgmCHSFN
If S
Then
min(M,S)→M
max(Q,P)→Q
End
""→Str2
End
If Str6="+" or Str6="-"
1→A
If Str6="*" or Str6="/"
1→B
End
End
ClrHome
Disp "RAW ANSWER:",X
If M=99
Goto SZ
If A and B
Goto SX
If B and X=0
Goto SZ
If B
Goto SM
If A
Goto SA
Disp "SIG FIGS:",M
Goto SZ
Lbl SA
round(X/10^Q,0)*10^Q→R
Disp "+- RULE: KEEP PLACE 10^",Q,"ANSWER:",R
Goto SZ
Lbl SM
int(log(abs(X)))→E
If abs(X)/10^E≥10
E+1→E
If abs(X)/10^E<1
E-1→E
round(X/10^(E-M+1),0)*10^(E-M+1)→R
Disp "×/ RULE: FEWEST SF",M,"ANSWER:",R
Goto SZ
Lbl SX
Disp "MIXED +- AND ×/:","DO ONE STEP AT A TIME"
Lbl SZ
Pause
Goto S
Lbl S4
''' + pages([
    "SIG FIG RULES (TA):",
    "NONZERO DIGITS: SIG",
    "CAPTIVE 0 (4.502): SIG",
    "TRAILING 0 W/ DECIMAL",
    " (3.900): SIG",
    "620. (DECIMAL PT): SIG",
    "PLACEHOLD 0 (200): NOT",
    "LEADING 0 (0.0014): NOT",
    "EXACT #S: INFINITE SF",
    "+- : USE PLACE VALUE",
    " FARTHEST LEFT",
    " 21+43.7=65 (ONES)",
    "×/ : USE FEWEST SIG FIGS",
    " 44.0×3=100 (1 SF)",
    "LAST DIGIT = ESTIMATED",
], "S") + r'''
Lbl D
Menu("DENSITY ρ=m/V","FIND ρ = m/V",D1,"FIND m = ρV",D2,"FIND V = m/ρ",D3,"BACK",0)
Lbl D1
ClrHome
Input "MASS m (g):",M
Input "VOLUME V (mL):",V
ClrHome
Disp "ρ=m/V","DENSITY (g/mL):",M/V
Pause
Goto D
Lbl D2
ClrHome
Input "DENSITY ρ (g/mL):",P
Input "VOLUME V (mL):",V
ClrHome
Disp "m=ρV","MASS (g):",P*V
Pause
Goto D
Lbl D3
ClrHome
Input "MASS m (g):",M
Input "DENSITY ρ (g/mL):",P
ClrHome
Disp "V=m/ρ","VOLUME (mL):",M/P
Pause
Goto D
Lbl M
ClrHome
Disp "n=m/M  #=n×NA","ENTER 0 IF UNKNOWN","TIP: M CAN BE TYPED","AS 2*1.008+16.00"
Input "MASS m (g):",A
Input "MOLAR MASS M:",B
Input "MOLES n:",C
Input "# PARTICLES:",D
If C=0 and D≠0
D/N→C
If C=0 and A≠0 and B≠0
A/B→C
If C=0
Goto M8
If A=0 and B≠0
C*B→A
If B=0 and A≠0
A/C→B
C*N→D
ClrHome
Disp "n=m/M  #=n×NA","MASS m (g):",A,"MOLAR MASS (g/mol):",B,"MOLES n (mol):",C,"# PARTICLES:",D
Pause
Goto 0
Lbl M8
ClrHome
Disp "NEED ONE OF:","  n","  m AND M","  # PARTICLES"
Pause
Goto M
Lbl I
Menu("ISOTOPES Σ(m×%)","FIND AVG ATOMIC MASS",I1,"FIND 1 ISOTOPE MASS",I2,"FIND % (2 ISOTOPES)",I3,"BACK",0)
Lbl I1
ClrHome
Disp "AVG=Σ(MASS×ABUND)","ENTER % (99.60 NOT .996)"
Input "# OF ISOTOPES:",K
0→A
0→B
For(J,1,K)
Disp "ISOTOPE",J
Input "MASS (amu):",M
Input "ABUNDANCE %:",P
A+M*P/100→A
B+P→B
End
ClrHome
Disp "AVG=Σ(MASS×ABUND)","AVG ATOMIC MASS:",A,"(amu = g/mol)","TOTAL % (CHECK 100):",B
Pause
Goto I
Lbl I2
ClrHome
Disp "SOLVE FOR ONE","UNKNOWN ISOTOPE MASS"
Input "AVG MASS (amu):",A
Input "UNKNOWN %:",U
Input "# OTHER ISOTOPES:",K
0→B
For(J,1,K)
Disp "OTHER ISOTOPE",J
Input "MASS (amu):",M
Input "ABUNDANCE %:",P
B+M*P/100→B
End
ClrHome
Disp "UNKNOWN ISOTOPE","MASS (amu):",(A-B)/(U/100)
Pause
Goto I
Lbl I3
ClrHome
Disp "2 ISOTOPES, FIND %"
Input "AVG MASS (amu):",A
Input "ISOTOPE 1 MASS:",M
Input "ISOTOPE 2 MASS:",R
(A-R)/(M-R)→X
ClrHome
Disp "X=(AVG-m2)/(m1-m2)","ISOTOPE 1 %:",100X,"ISOTOPE 2 %:",100(1-X)
Pause
Goto I
'''

# ---------------------------------------------------------------- LIGHT
PROGRAMS["CHLIGHT"] = r'''
6.62607ᴇ⁻34→H
2.99792458ᴇ8→C
9.109383ᴇ⁻31→M
1.0974ᴇ7→R
Lbl 0
Menu("LIGHT & ENERGY","c=λv  E=hv  E=hc/λ",A,"PHOTOELEC Φ=hv-KE",B,"RYDBERG 1/λ=RH(..)",C,"BOHR En=-Z²RHhc/n²",D,"BACK",Z)
Lbl Z
ClrHome
Return
Lbl A
Menu("c=λv  E=hv  E=hc/λ","KNOW λ (nm)",A1,"KNOW λ (m)",A2,"KNOW v (Hz = 1/s)",A3,"KNOW E (J/PHOTON)",A4,"BACK",0)
Lbl A1
ClrHome
Input "λ (nm):",L
L*1ᴇ⁻9→L
Goto A5
Lbl A2
ClrHome
Input "λ (m):",L
Lbl A5
C/L→F
H*F→E
Goto A9
Lbl A3
ClrHome
Input "v (Hz):",F
C/F→L
H*F→E
Goto A9
Lbl A4
ClrHome
Input "E (J):",E
E/H→F
C/F→L
Lbl A9
ClrHome
Disp "c=λv  E=hv=hc/λ","λ (m):",L,"λ (nm):",L*1ᴇ9,"v FREQUENCY (Hz):",F,"E (J/PHOTON):",E
Pause
Goto A
Lbl B
Menu("PHOTOELEC Φ=hv-KE","FIND KE=hv-Φ (+VEL)",B1,"FIND Φ=hv-KE",B2,"FIND LIGHT v,λ",B3,"THRESHOLD v₀=Φ/h",B4,"KE=1/2mv² ◄► VEL",B5,"BACK",0)
Lbl BL
Disp "LIGHT: TYPE λ IN nm","(OR 0 TO TYPE v)"
Input "λ (nm):",L
If L
C/(L*1ᴇ⁻9)→F
If not(L)
Input "v (Hz):",F
If Y=1
Goto BA
Goto BB
Lbl B1
ClrHome
1→Y
Goto BL
Lbl BA
Input "Φ (J):",P
H*F-P→K
ClrHome
Disp "KE=hv-Φ"
If K<0
Goto BN
√(2K/M)→V
Disp "KE OF e⁻ (J):",K,"e⁻ VELOCITY (m/s):",V,"(v=√(2KE/me))"
Pause
Goto B
Lbl BN
Disp "hv < Φ: BELOW","THRESHOLD, NO e⁻","EJECTED. hv-Φ =",K
Pause
Goto B
Lbl B2
ClrHome
2→Y
Goto BL
Lbl BB
Input "KE (J), 0=USE VEL:",K
If not(K)
Input "e⁻ VEL (m/s):",V
If not(K)
.5M*V²→K
ClrHome
Disp "Φ=hv-KE","WORK FUNCTION Φ (J):",H*F-K
Pause
Goto B
Lbl B3
ClrHome
Input "Φ (J):",P
Input "KE (J), 0=USE VEL:",K
If not(K)
Input "e⁻ VEL (m/s):",V
If not(K)
.5M*V²→K
(P+K)/H→F
ClrHome
Disp "v=(Φ+KE)/h","v (Hz):",F,"λ (nm):",C/F*1ᴇ9,"E PHOTON hv (J):",H*F
Pause
Goto B
Lbl B4
ClrHome
Input "Φ (J):",P
P/H→F
ClrHome
Disp "THRESHOLD v₀=Φ/h (Hz):",F,"MAX λ=c/v₀ (nm):",C/F*1ᴇ9
Pause
Goto B
Lbl B5
ClrHome
Input "MASS kg, 0=e⁻:",W
If not(W)
M→W
Menu("KE=1/2mv²","KNOW KE ► FIND VEL",B6,"KNOW VEL ► FIND KE",B7)
Lbl B6
ClrHome
Input "KE (J):",K
Disp "v=√(2KE/m) (m/s):",√(2K/W)
Pause
Goto B
Lbl B7
ClrHome
Input "VELOCITY (m/s):",V
Disp "KE=1/2mv² (J):",.5W*V²
Pause
Goto B
Lbl C
Menu("1/λ=RH(1/n₁²-1/n₂²)","FIND λ (n START, END)",C1,"FIND UNKNOWN n",C2,"BACK",0)
Lbl C1
ClrHome
Input "n INITIAL:",I
Input "n FINAL:",J
min(I,J)→A
max(I,J)→B
R(1/A²-1/B²)→Q
ClrHome
If Q=0
Goto C9
1/Q→L
If I>J
Disp "EMITTED (HIGH►LOW n)"
If I<J
Disp "ABSORBED (LOW►HIGH n)"
Disp "λ (nm):",L*1ᴇ9,"v (Hz):",C/L,"E PHOTON (J):",H*C/L
Pause
Goto C
Lbl C9
Disp "SAME LEVEL: NO LIGHT"
Pause
Goto C
Lbl C2
ClrHome
Input "λ (nm):",L
L*1ᴇ⁻9→L
Input "KNOWN n:",A
Menu("KNOWN n IS THE...","LOWER  n₁",C3,"HIGHER n₂",C4)
Lbl C3
1/A²-1/(R*L)→Q
If Q≤0
Goto C8
1/√(Q)→B
ClrHome
Disp "HIGHER n₂ =",B,"NEAREST WHOLE #:",round(B,0),"(SHOULD BE CLOSE TO","A WHOLE NUMBER)"
Pause
Goto C
Lbl C4
1/(R*L)+1/A²→Q
1/√(Q)→B
ClrHome
Disp "LOWER n₁ =",B,"NEAREST WHOLE #:",round(B,0),"(SHOULD BE CLOSE TO","A WHOLE NUMBER)"
Pause
Goto C
Lbl C8
ClrHome
Disp "NO SOLUTION:","CHECK λ OR WHETHER","KNOWN n IS LOW/HIGH"
Pause
Goto C
Lbl D
Menu("En=-Z²RHhc/n²","FIND En (ONE LEVEL)",D1,"ΔE BETWEEN 2 LEVELS",D2,"BACK",0)
Lbl D1
ClrHome
Input "Z (H=1):",Z
Input "n:",N
⁻Z²*R*H*C/N²→E
ClrHome
Disp "En=-Z²RHhc/n²","En (J):",E,"En (eV):",E/1.602ᴇ⁻19
Pause
Goto D
Lbl D2
ClrHome
Input "Z (H=1):",Z
Input "n INITIAL:",I
Input "n FINAL:",J
Z²*R*H*C→W
W/I²-W/J²→E
ClrHome
Disp "ΔE=Efinal-Einit (J):",E
If E<0
Disp "EMITTED (ΔE<0)"
If E>0
Disp "ABSORBED (ΔE>0)"
If E=0
Goto D9
Disp "λ=hc/|ΔE| (nm):",H*C/abs(E)*1ᴇ9,"v=|ΔE|/h (Hz):",abs(E)/H
Lbl D9
Pause
Goto D
'''

# ---------------------------------------------------------------- ATOM
PROGRAMS["CHATOM"] = r'''
6.62607ᴇ⁻34→H
9.109383ᴇ⁻31→M
Lbl 0
Menu("ATOM & QUANTUM","DE BROGLIE λ=h/mv",A,"HEISEN ΔxΔ(mv)≥h/4π",B,"QUANTUM #S n l ml ms",C,"NODES n-1  l  (n-1)-l",D,"COULOMB F=keQ₁Q₂/r²",E,"BACK",Z)
Lbl Z
ClrHome
Return
Lbl A
Menu("DE BROGLIE λ=h/mv","FIND λ = h/mv",A1,"FIND v = h/mλ",A2,"FIND m = h/λv",A3,"BACK",0)
Lbl A1
ClrHome
Disp "GRAMS? TYPE g/1000"
Input "MASS kg, 0=e⁻:",W
If not(W)
M→W
Input "VELOCITY (m/s):",V
H/(W*V)→L
ClrHome
Disp "λ=h/mv","λ (m):",L,"λ (nm):",L*1ᴇ9
Pause
Goto A
Lbl A2
ClrHome
Disp "GRAMS? TYPE g/1000"
Input "MASS kg, 0=e⁻:",W
If not(W)
M→W
Input "λ (nm):",L
ClrHome
Disp "v=h/mλ","VELOCITY (m/s):",H/(W*L*1ᴇ⁻9)
Pause
Goto A
Lbl A3
ClrHome
Input "λ (nm):",L
Input "VELOCITY (m/s):",V
H/(L*1ᴇ⁻9*V)→W
ClrHome
Disp "m=h/λv","MASS (kg):",W,"MASS (g):",1000W
Pause
Goto A
Lbl B
Menu("ΔxΔ(mv)≥h/4π","MIN Δx FROM m, Δv",B1,"MIN Δx FROM Δ(mv)",B2,"MIN Δv FROM m, Δx",B3,"MIN Δ(mv) FROM Δx",B4,"BACK",0)
Lbl B1
ClrHome
Input "MASS kg, 0=e⁻:",W
If not(W)
M→W
Input "Δv (m/s):",V
W*V→P
Goto B5
Lbl B2
ClrHome
Input "Δ(mv) (kg m/s):",P
Lbl B5
H/(4πP)→X
ClrHome
Disp "Δx≥h/(4πΔ(mv))","MIN Δx (m):",X,"MIN Δx (nm):",X*1ᴇ9
Pause
Goto B
Lbl B3
ClrHome
Input "MASS kg, 0=e⁻:",W
If not(W)
M→W
Input "Δx (m):",X
ClrHome
Disp "Δv≥h/(4πmΔx)","MIN Δv (m/s):",H/(4πW*X)
Pause
Goto B
Lbl B4
ClrHome
Input "Δx (m):",X
ClrHome
Disp "Δ(mv)≥h/(4πΔx)","MIN Δ(mv) (kg m/s):",H/(4πX)
Pause
Goto B
Lbl C
Menu("QUANTUM #S","n,l ► SUBSHELL INFO",C1,"NAME (4d) ► n,l INFO",C2,"CHECK n l ml ms SET",C3,"BACK",0)
Lbl C1
ClrHome
Input "n:",N
Input "l:",L
Goto C5
Lbl C2
ClrHome
Input "n (THE NUMBER):",N
Menu("LETTER","s  (l=0)",CS,"p  (l=1)",CP,"d  (l=2)",CD,"f  (l=3)",CF)
Lbl CS
0→L
Goto C5
Lbl CP
1→L
Goto C5
Lbl CD
2→L
Goto C5
Lbl CF
3→L
Lbl C5
If N<1 or L<0 or L>N-1 or fPart(N) or fPart(L)
Goto C9
ClrHome
Disp "SUBSHELL:","SHAPE:","ml: -l TO +l =","# ORBITALS 2l+1:","MAX e⁻ (2/ORBITAL):","TOTAL NODES n-1:","PLANAR NODES = l:","RADIAL (n-1)-l:","ms = +1/2 OR -1/2"
Output(1,11,N)
Output(1,12+(N≥10),sub("spdfghik",min(L+1,8),1))
Output(2,8,sub("SPHERE   HOURGLASSCLOVER   WEIRD    ",9min(L,3)+1,9))
Output(3,16,⁻L)
Output(3,20,"TO")
Output(3,23,L)
Output(4,18,2L+1)
Output(5,21,2(2L+1))
Output(6,18,N-1)
Output(7,19,L)
Output(8,17,N-1-L)
Pause
Goto C
Lbl C9
ClrHome
Disp "NOT ALLOWED:","n = 1, 2, 3...","l = 0 TO n-1"
Pause
Goto C
Lbl C3
ClrHome
Input "n:",N
Input "l:",L
Input "ml:",J
Input "ms (.5 OR -.5):",S
ClrHome
0→V
If N<1 or fPart(N)
Then
Disp "BAD n: MUST BE 1,2,3..."
1→V
End
If L<0 or L>N-1 or fPart(L)
Then
Disp "BAD l: MUST BE 0 TO n-1"
1→V
End
If abs(J)>L or fPart(J)
Then
Disp "BAD ml: MUST BE -l TO +l"
1→V
End
If abs(S)≠.5
Then
Disp "BAD ms: +1/2 OR -1/2"
1→V
End
If not(V)
Disp "VALID SET"
Pause
Goto C
Lbl D
Menu("NODES","n,l ► # OF NODES",D1,"NODES ► SUBSHELL",D2,"BACK",0)
Lbl D1
ClrHome
Input "n:",N
Input "l:",L
If N<1 or L<0 or L>N-1
Goto C9
ClrHome
Disp "TOTAL = n-1:",N-1,"PLANAR = l:",L,"RADIAL = (n-1)-l:",N-1-L
Pause
Goto D
Lbl D2
ClrHome
Disp "l = # PLANAR","n = TOTAL + 1"
Input "# PLANAR NODES:",L
Input "# RADIAL NODES:",J
L+J+1→N
Goto C5
Lbl E
Menu("COULOMB","F=keQ₁Q₂/r²  (N)",E1,"V=Q₁Q₂/(4πε₀r) (J)",E2,"BACK",0)
Lbl E1
1→Y
Goto E3
Lbl E2
2→Y
Lbl E3
Menu("CHARGES GIVEN AS","ION CHARGE (+1, -2)",E4,"COULOMBS (C)",E5)
Lbl E4
1.6021765ᴇ⁻19→Q
Goto E6
Lbl E5
1→Q
Lbl E6
ClrHome
Disp "(-) KEY FOR NEGATIVE","1 ANGSTROM = 1ᴇ⁻10 m"
Input "Q₁:",A
Input "Q₂:",B
Input "r (m):",R
If Y=1
8.987551ᴇ9*A*B*Q²/R²→F
If Y=2
A*B*Q²/(4π*8.8541877ᴇ⁻12*R)→F
ClrHome
If Y=1
Disp "F=keQ₁Q₂/r²","FORCE (N):",F
If Y=2
Disp "V=Q₁Q₂/(4πε₀r)","ENERGY (J):",F
If F<0
Disp "NEGATIVE = ATTRACT"
If F>0
Disp "POSITIVE = REPEL"
Pause
Goto E
'''

# ---------------------------------------------------------------- MY NOTES
NOTE_PREFIX = [
    "MY PREFIX NOTES:",
    "T  tera   10^12",
    "G  giga   10^9",
    "M  mega   10^6",
    "k  kilo   10^3",
    "h  hecto  10^2",
    "d  deca   10^1  (da)",
    "b  BASE   10^0",
    "d  deci   10^⁻1",
    "c  centi  10^⁻2",
    "m  milli  10^⁻3",
    "μ  micro  10^⁻6",
    "n  nano   10^⁻9",
    "p  pico   10^⁻12",
    "f  femto  10^⁻15",
    "a  atto   10^⁻18",
    "(TA ADDS: E exa 10^18,",
    " P peta 10^15)",
]
NOTE_CONST = [
    "SPEED OF LIGHT:",
    " c=2.99792458ᴇ8 m/s",
    "PLANCKS:",
    " h=6.62607ᴇ⁻34 J s",
    "MASS OF ELECTRON:",
    " me=9.109383ᴇ⁻31 kg",
    "MASS OF NEUTRON:",
    " mn=1.6749273ᴇ⁻27 kg",
    "MASS OF PROTON:",
    " mp=1.6726217ᴇ⁻27 kg",
    "RYDBERGS:",
    " RH=1.0974ᴇ7 m⁻1",
]
NOTE_LIGHT = [
    "c=λv  ]",
    "E=hv  ] E=hc/λ",
    " v = FREQUENCY",
    " λ = WAVELENGTH",
    " E = ENERGY",
    "",
    "SIDEWAYS ARROWS:",
    " ► m  (MASS)",
    " ► v  (FREQUENCY)",
    " ► E  (ENERGY)",
    " ◄ λ  (WAVELENGTH)",
    "m, v, E GO TOGETHER;",
    "λ GOES THE OPPOSITE WAY",
]
NOTE_DB = [
    "DE BROGLIE:",
    " λ=h/mv",
    " m = MASS",
    " [ PAIRED WITH:",
    " Ekinetic=1/2mv²",
    "",
    "WORK FUNCTION:",
    " Φ=hv-KEelectron",
    " KE = KE OF e⁻ THAT",
    "      COMES OFF",
]
NOTE_EN = [
    "ENERGY OF ELECTRON",
    "WHILE IN ORBIT:",
    " En=-Z²RHhc/n²",
    " Z = ATOMIC NUMBER",
    "SIMPLIFIED:",
    " En=-Rh/n²",
    " (ONLY USE IF H)",
    " [Rh=RHhc=2.18ᴇ⁻18 J]",
    "",
    "RYDBERG/BALMER EQUATION:",
    " 1/λ=RH(1/n₁²-1/n₂²)",
    " n₁ = LOWER",
    " n₂ = HIGHER",
]
NOTE_QN = [
    "n l ml ms",
    "n = PRINCIPAL QUANTUM #",
    " n ≥ 1",
    " -PRINCIPAL ENERGY LEVEL",
    " -DISTANCE FROM NUCLEUS",
    " -ORBITAL SIZE",
    "l = ANGULAR MOMENTUM QN",
    " l = 0 TO n-1",
    " -SUBLEVEL",
    " -ORBITAL TYPE",
    " -ORBITAL SHAPE",
    " l= 0-s 1-p 2-d 3-f",
    "ml = MAGNETIC QUANTUM #",
    " ml = -l TO +l",
    " -ORIENTATION IN SPACE",
    "",
    "TOTAL NODES = n-1",
    "PLANAR NODE (= l)",
    " -FLAT 2D SLICE THROUGH",
    "  ATOMIC ORBITAL",
    "RADIAL NODE (= TOTAL-l)",
    " -HOLLOW SPHERICAL GAP",
    "  IN AN ORBITAL",
]

PROGRAMS["CHNOTES"] = r'''
Lbl 0
Menu("MY NOTES","SI PREFIXES k μ n",A,"CONSTANTS c h me RH",B,"E=hc/λ + ARROWS",C,"λ=h/mv  KE  Φ",D,"En  +  RYDBERG n₁ n₂",E,"QUANTUM #S & NODES",F,"BACK",Z)
Lbl Z
ClrHome
Return
Lbl A
''' + pages(NOTE_PREFIX, "0") + "\nLbl B\n" + pages(NOTE_CONST, "0") + \
    "\nLbl C\n" + pages(NOTE_LIGHT, "0") + "\nLbl D\n" + pages(NOTE_DB, "0") + \
    "\nLbl E\n" + pages(NOTE_EN, "0") + "\nLbl F\n" + pages(NOTE_QN, "0") + "\n"

# ---------------------------------------------------------------- EQUATION SHEET
EQ_CONST = [
    "CONSTANTS",
    "a₀=0.5291772059 ANGSTROM",
    "c=2.99792458ᴇ8 m/s",
    "e=1.6021765ᴇ⁻19 C",
    "ε₀=8.8541877ᴇ⁻12 F/m",
    "h=6.62607ᴇ⁻34 J s",
    "kB=1.38065ᴇ⁻23 J/K",
    "ke=8.987551ᴇ9 N m²/C²",
    "me=9.109383ᴇ⁻31 kg",
    "mn=1.6749273ᴇ⁻27 kg",
    "mp=1.6726217ᴇ⁻27 kg",
    "NA=6.022141ᴇ23 mol⁻1",
    "R=8.31447 J/(mol K)",
    " =0.0820575 L atm/(mol K)",
    " =1.987207 cal/(mol K)",
    "RH=1.0974ᴇ7 m⁻1",
]
EQ_CONV = [
    "CONVERSIONS (*=EXACT)",
    "LENGTH",
    "1 in=2.54 cm*",
    "1 ft=12 in*",
    "1 yd=3 ft*",
    "1 m=39.37 in*",
    "1 mile=5280 ft*",
    "1 mile=1.609 km",
    "MASS",
    "1 lb=453.59237 g",
    "    =16 oz avdp*",
    "1 US lb=12 troy oz*",
    "1 ton=2000 lb*",
    "1 amu=1.660538ᴇ⁻24 g",
    "VOLUME",
    "1 US gal=3.7854 L=4 qt*",
    "1 US qt=32 US fl oz*",
    "1 US fl oz=29.5735 mL",
    "1 cm³=0.001 L*",
    "1 in³=16.4 cm³",
    "PRESSURE",
    "1 bar=100,000 Pa*",
    "1 atm=760 torr*",
    "     =101325 Pa*",
    "     =406.783 in H₂O",
    "     =14.6959 psi",
    "1 torr=1 mmHg (0°C)*",
    "1 Pa=1 kg m⁻1 s⁻²*",
    "FORCE, POWER, ENERGY",
    "1 N=1 kg m s⁻²",
    "1 Watt=1 J/s",
    "1 J=1 kg m²/s²=0.2390 cal",
    "1 J=1 V C=0.009869 L atm",
    "1 eV=1.602ᴇ⁻19 J",
    "1 L atm=101.3 J",
]
EQ_ATOM = [
    "ρ=m/V",
    "TF=(9°F/5°C)TC+32°F",
    "TK=(1K/1°C)TC+273.15K",
    "c=λv",
    "E=hv",
    "λ=h/mv",
    "Ekinetic=1/2mv²",
    "E=mc²",
    "Φ=hv-KEelectron",
    "En=-Z²RHhc/n²",
    "ΔxΔ(mv)≥h/4π",
    "1/λ=RH(1/n₁²-1/n₂²)",
    "V(r)=Q₁Q₂/(4πε₀r)",
    "F(r)=keQ₁Q₂/r²",
    "(SHEET: GREEK v=FREQ,",
    " v=VELOCITY)",
]
EQ_THERMO = [
    "μ=Qr",
    "ΔE=q+w",
    "ΔEuniv=0",
    "ΔSuniv≥0",
    "S=kB ln W",
    "q=mCΔT",
    "w=-PextΔV",
    "ΔH=ΔE+PΔV",
    "ΔS=qrev/T",
    "ΔG=ΔH-TΔS",
    "ΔG=ΔG°+RT ln Q",
    "ΔH°rxn=ΣnH°f,prod",
    "       -ΣmH°f,react",
    "ΔH°rxn (APPROX.) =",
    " ΣnDbroken-ΣmDformed",
]
EQ_GAS = [
    "PV=nRT",
    "Ptot=P1+P2+P3+...",
    "M=mRT/(PV)  (MOLAR MASS)",
    "d=PM/(RT)",
    "[P+a(n/V)²](V-nb)=nRT",
    "RateA/RateB=TimeB/TimeA",
    "   =√(MB/MA)",
    "KEave=(3/2)RT",
    "urms=√(v²)=√(3RT/M)",
    "pX=-log X",
    "Kw=[H₃O+][OH-]",
]

PROGRAMS["CHEQN"] = r'''
Lbl 0
Menu("EQUATION SHEET","CONSTANTS",A,"CONVERSIONS",B,"ρ LIGHT & ATOM",C,"THERMO ΔE ΔH ΔS ΔG",D,"GASES PV=nRT & pH",E,"BACK",Z)
Lbl Z
ClrHome
Return
Lbl A
''' + pages(EQ_CONST, "0") + "\nLbl B\n" + pages(EQ_CONV, "0") + \
    "\nLbl C\n" + pages(EQ_ATOM, "0") + "\nLbl D\n" + pages(EQ_THERMO, "0") + \
    "\nLbl E\n" + pages(EQ_GAS, "0") + "\n"

# ---------------------------------------------------------------- MORE / REFERENCE
REF_SI = [
    "E  exa    10^18",
    "P  peta   10^15",
    "T  tera   10^12",
    "G  giga   10^9",
    "M  mega   10^6",
    "k  kilo   10^3",
    "h  hecto  10^2",
    "da deca   10^1",
    "b  BASE   10^0",
    "d  deci   10^⁻1",
    "c  centi  10^⁻2",
    "m  milli  10^⁻3",
    "μ  micro  10^⁻6",
    "n  nano   10^⁻9",
    "p  pico   10^⁻12",
    "f  femto  10^⁻15",
    "a  atto   10^⁻18",
    "1 km=1000 m",
    "BIG: EVEN PIGS TASTE",
    " GOOD MEALS",
    "MEDIUM: KING HENRY DIED",
    " BY DRINKING CHOCOLATE",
    " MILK",
    "SMALL: MANY NICE PIANOS",
    " FALL APART",
    "1 μm = 10^⁻6 m",
]
REF_TA = [
    "NOT ON SHEET-MEMORIZE:",
    "ATOMIC MASS =",
    " Σ(ISOTOPE MASS×ABUND)",
    " ABUND AS DECIMAL",
    " (99.60% = 0.9960)",
    "1 MOLE = 6.022ᴇ23",
    "MOLAR MASS (g/mol) =",
    " AVG ATOMIC MASS VALUE",
    "",
    "SIG FIGS:",
    " +- : FARTHEST-LEFT PLACE",
    " ×/ : FEWEST SIG FIGS",
    "λ AND v ARE INVERSELY",
    " PROPORTIONAL",
    "LOW n►HIGH n = ABSORB",
    "HIGH n►LOW n = EMIT",
    "2 e⁻ IN EACH ORBITAL",
    "# ml VALUES = # ORBITALS",
    "s SPHERICAL",
    "p HOURGLASS",
    "d CLOVER (MOSTLY)",
    "f WEIRD",
    "PSI² = ORBITAL (90%",
    " CHANCE TO FIND e⁻)",
    "e⁻ ARE IN A CLOUD,",
    " NOT BOHR RINGS",
]
REF_EM = [
    "LOW ENERGY, LONG λ",
    " RADIO",
    " MICROWAVE",
    " INFRARED",
    " VISIBLE (RED...VIOLET)",
    " ULTRAVIOLET",
    " X-RAY",
    " GAMMA",
    "HIGH ENERGY, SHORT λ",
    "RAMPANT MARTIANS INVADE",
    " VENUS USING X-RAY GUNS",
    "RED = LOW E",
    "VIOLET = HIGH E",
    "HOTTER BLACKBODY = HIGHER",
    " E, SHORTER λ",
    "LIGHT = WAVE + PARTICLE",
    "PHOTON = QUANTIZED PACKET",
]
REF_H = [
    "HYDROGEN LINES:",
    " 656 nm RED     3►2",
    " 486 nm GREEN   4►2",
    " 434 nm VIOLET  5►2",
    "COLOR WE SEE = EMITTED;",
    " OTHERS ABSORBED",
    "",
    "PHOTOELECTRIC EFFECT:",
    "LOW ENERGY LIGHT: NO e⁻",
    " EVEN IF BRIGHTER",
    "↑ FREQ/ENERGY: e⁻ OUT",
    "↑ INTENSITY: MORE e⁻",
    "↑ FREQ ABOVE THRESHOLD:",
    " FASTER e⁻",
    "Φ = MIN ENERGY FOR e⁻",
    " TO JUMP OFF",
]
REF_HIST = [
    "GREEKS: FIRE, EARTH,",
    " AIR, WATER",
    "BOYLE: THEORIES BASED ON",
    " OBSERVATION+DEMONSTRATION",
    "LAVOISIER: BURNED METAL",
    " IN SEALED CONTAINERS ►",
    " CONSERVATION OF MASS",
    "PROUST: RATIOS IN A",
    " COMPOUND ALWAYS SAME ►",
    " DEFINITE PROPORTIONS",
    "DALTON: CO VS CO2 = 1:2 ►",
    " MULTIPLE PROPORTIONS",
    " (SMALL WHOLE #S = ATOMS)",
    "THOMSON: CATHODE RAY TUBE",
    " e⁻ CHARGE/MASS RATIO,",
    " e⁻ SMALLER THAN ATOMS,",
    " PLUM PUDDING MODEL",
    "MILLIKAN: OIL DROP ►",
    " EXACT CHARGE+MASS OF e⁻",
    "CURIE: RADIOACTIVITY ►",
    " ATOMS HAVE + AND - PARTS",
    " (ALPHA+ BETA- GAMMA)",
    "RUTHERFORD: GOLD FOIL,",
    " ALPHA BOUNCED ► NUCLEUS",
    " +CHARGE UNIQUE ►ATOMIC #",
    "CHADWICK: ALPHA AT Be ►",
    " NEUTRONS + ISOTOPES",
    "FRAUNHOFER: GAPS IN",
    " SUNLIGHT (NOT CONTINUOUS)",
    "BUNSEN/KIRCHHOFF: ELEMENTS",
    " ABSORB/EMIT DIFFERENT λ",
    "BALMER/RYDBERG: H λ FROM",
    " WHOLE NUMBERS",
    "BOHR: e⁻ ENERGY QUANTIZED",
    "DE BROGLIE: MATTER=WAVE",
]

PROGRAMS["CHREF"] = r'''
Lbl 0
Menu("MORE","SI PREFIX TABLE",A,"TA: MEMORIZE THESE",B,"EM SPECTRUM ORDER",C,"H LINES & PHOTOELEC",D,"HISTORY/EXPERIMENTS",E,"BACK",Z,"QUIT",Q)
Lbl Z
ClrHome
Return
Lbl Q
ClrHome
Stop
Lbl A
''' + pages(REF_SI, "0") + "\nLbl B\n" + pages(REF_TA, "0") + \
    "\nLbl C\n" + pages(REF_EM, "0") + "\nLbl D\n" + pages(REF_H, "0") + \
    "\nLbl E\n" + pages(REF_HIST, "0") + "\n"


# ---------------------------------------------------------------- IONS / SAME # OF ELECTRONS
# Symbols, molar masses (g/mol) and common ion charges for Z = 1..86.
# Charge 99 = no single common ion, so the program asks.
_EL = """H 1.008 1|HE 4.003 0|LI 6.94 1|BE 9.012 2|B 10.81 3|C 12.01 99|N 14.01 -3|O 16.00 -2|F 19.00 -1|NE 20.18 0|
NA 22.99 1|MG 24.31 2|AL 26.98 3|SI 28.09 99|P 30.97 -3|S 32.07 -2|CL 35.45 -1|AR 39.95 0|K 39.10 1|CA 40.08 2|
SC 44.96 3|TI 47.87 99|V 50.94 99|CR 52.00 99|MN 54.94 99|FE 55.85 99|CO 58.93 99|NI 58.69 99|CU 63.55 99|ZN 65.38 2|
GA 69.72 3|GE 72.63 99|AS 74.92 -3|SE 78.97 -2|BR 79.90 -1|KR 83.80 0|RB 85.47 1|SR 87.62 2|Y 88.91 3|ZR 91.22 99|
NB 92.91 99|MO 95.95 99|TC 98 99|RU 101.07 99|RH 102.91 99|PD 106.42 99|AG 107.87 1|CD 112.41 2|IN 114.82 3|SN 118.71 99|
SB 121.76 99|TE 127.60 -2|I 126.90 -1|XE 131.29 0|CS 132.91 1|BA 137.33 2|LA 138.91 3|CE 140.12 99|PR 140.91 99|ND 144.24 99|
PM 145 99|SM 150.36 99|EU 151.96 99|GD 157.25 99|TB 158.93 99|DY 162.50 99|HO 164.93 99|ER 167.26 99|TM 168.93 99|YB 173.05 99|
LU 174.97 99|HF 178.49 99|TA 180.95 99|W 183.84 99|RE 186.21 99|OS 190.23 99|IR 192.22 99|PT 195.08 99|AU 196.97 99|HG 200.59 99|
TL 204.38 99|PB 207.2 99|BI 208.98 99|PO 209 99|AT 210 -1|RN 222 0"""
ELEMENTS = [e.split() for e in _EL.replace("\n", "").split("|")]
assert len(ELEMENTS) == 86
_SYM = "".join(s.ljust(2) for s, _, _ in ELEMENTS)
_MM = "{" + ",".join(m for _, m, _ in ELEMENTS) + "}"
_CHG = "{" + ",".join(c.replace("-", "⁻") for _, _, c in ELEMENTS) + "}"

# rounding helper: rounds θ to N sig figs (uses E)
PROGRAMS["CHRND"] = r"""
If θ≠0
Then
int(log(abs(θ)))→E
If abs(θ)/10^E≥10
E+1→E
If abs(θ)/10^E<1
E-1→E
round(θ/10^(E-N+1),0)*10^(E-N+1)→θ
End
"""

PROGRAMS["CHION"] = _MM + "→ʟMM\n" + _CHG + "→ʟCHG\n" + '"' + _SYM + '"→Str9\n' + r"""
Menu("SAME NUMBER OF...","ELECTRONS e⁻",A1,"PROTONS p+",A2,"IONS / ATOMS",A3,"BACK",Z)
Lbl Z
ClrHome
Return
Lbl A1
1→T
Menu("ELECTRONS IN...","IONS (Mg²+, Cl⁻...)",B1,"NEUTRAL ATOMS",B2)
Lbl A2
2→T
Goto B2
Lbl A3
3→T
Lbl B2
0→A
Goto C0
Lbl B1
1→A
Lbl C0
ClrHome
Disp "ELEMENT: TYPE SYMBOL","IN CAPS (MG, CA, CL)","OR ATOMIC NUMBER"
Input "GIVEN ELEMENT:",Str1
1→Y
Lbl E0
0→Z
If inString("0123456789",sub(Str1,1,1))
expr(Str1)→Z
If length(Str1)=1
Str1+" "→Str1
If not(Z)
Then
For(J,1,86)
If sub(Str9,2J-1,2)=Str1
J→Z
End
End
If Z<1 or Z>86 or fPart(Z)
Goto E8
ʟCHG(Z)→C
If not(A)
0→C
If C=99
Then
Disp sub(Str9,2Z-1,2)+" ION CHARGE?"
Input "(E.G. 2 OR -3):",C
End
If Y=2
Goto G0
Z→B
C→U
Menu("GIVEN AMOUNT IS IN","MOLES",F1,"GRAMS",F2,"# OF IONS / ATOMS",F3)
Lbl F1
1→I
Goto F4
Lbl F2
2→I
Goto F4
Lbl F3
3→I
Lbl F4
ClrHome
Disp "TYPE IT EXACTLY AS","WRITTEN (KEEP ZEROS,","E.G. 0.750)"
Input "AMOUNT:",Str3
expr(Str3)→X
prgmCHSFN
S→N
If I=2
X/ʟMM(B)→X
If I=3
X/6.022141ᴇ23→X
ClrHome
Disp "NEW ELEMENT: SYMBOL","IN CAPS OR ATOMIC #"
Input "NEW ELEMENT:",Str1
2→Y
Goto E0
Lbl E8
Disp "UNKNOWN ELEMENT.","USE CAPS: MG NOT Mg"
Pause
Goto C0
Lbl G0
Z→H
C→V
1→O
1→Q
If T=1
B-U→O
If T=1
H-V→Q
If T=2
B→O
If T=2
H→Q
If Q≤0
Goto G8
X*O/Q→M
ClrHome
Output(1,1,sub(Str9,2B-1,2)+" EACH:")
Output(1,11,O)
Output(2,1,sub(Str9,2H-1,2)+" EACH:")
Output(2,11,Q)
If T=1
Output(3,1,"(e⁻ = Z - CHARGE)")
If T=2
Output(3,1,"(p+ = Z)")
Output(4,1,"ANSWER, SIG FIGS:")
Output(4,19,N)
M*ʟMM(H)→θ
prgmCHRND
Output(5,1,"GRAMS:")
Output(5,11,θ)
M→θ
prgmCHRND
Output(6,1,"MOLES:")
Output(6,11,θ)
M*6.022141ᴇ23→θ
prgmCHRND
Output(7,1,"PARTICLES:")
Output(7,11,θ)
Output(9,1,"MOLAR MASS USED:")
Output(9,18,ʟMM(H))
Pause
ClrHome
Return
Lbl G8
ClrHome
Disp "NEW ION HAS 0 e⁻","(CHECK THE CHARGE)"
Pause
ClrHome
Return
"""
