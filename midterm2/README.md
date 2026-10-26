# MIDTERM 2 (TI-84 Plus CE)

Send all four programs to the calculator: `MIDTERM2`, `MT2SN`, `MT2LW`, `MT2G`.
Run `prgmMIDTERM2`. (MT2SN, MT2LW, MT2G are helpers it calls.)

- SN+LP ► SHAPE SOLVER: enter steric number + lone pairs → electron geometry, shape, angle, hybridization, examples, polarity.
- LEWIS SOLVER: type a formula in CAPS (SO4, XEF4, HNO3). The charge can go right in the formula
  (NH4+, SO4-2, NO3-) or at the CHARGE prompt (-2, 2-, +, or 0). Single central atom only.
  Picks the central atom and bonds by formal charge + electronegativity, shows lone pairs, FC,
  equivalent resonance forms, SN/shape/angle/hybridization, sigma/pi counts, octet status, polarity.
  When the best (minimum-FC) structure uses an expanded octet, it also shows the octet-only version.
  H placement (on the center or on O) is chosen by formal charge, so H2CO, CH2O, CH3OH, HOCL all work.
  All-caps two-letter symbols are read by context (SBR2 = S + Br2, SBF5 = SbF5).
  Two-center molecules (C2H6, N2H4) get a clear "probably 2+ centers" message.
- Notes: VSEPR & hybridization, sigma/pi/antibonding/MO, band theory, polyatomic ions, isomers,
  organic drawing, FC & Lewis rules, theory comparison.

Rebuild: `pip install tivars` then `python3 build.py` (in this folder).
`tiinterp.py` + `test_lw.py` / `test_nav.py` run the programs in a small TI-BASIC simulator for testing.
