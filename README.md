# CHEM 105 Calculator — TI-84 Plus CE (TI-BASIC)

Menu-driven CHEM 105 (Exam 1) calculator built from the official BYU CHEM 105
equation sheet, my annotated sheet, and the TA study guide.

## Install
1. Install **TI Connect CE** on your computer and plug in the calculator.
2. Drag **all 9 files** from `8xp/` onto the calculator (Calculator Explorer):
   `CHEM, CHUNIT, CHSFN, CHMATTR, CHLIGHT, CHATOM, CHNOTES, CHEQN, CHREF`.
   They all have to be there, because `CHEM` calls the others.
3. On the calculator: `prgm` → `CHEM` → `ENTER` → `ENTER`.

## Menu map
```
CHEM 105
1 UNITS ×10^x k μ n     prefix converter (E..a), cm²/cm³, auto-prefix,
                        length, mass, volume, pressure, energy, temperature
2 MATTER ρ=m/V n=m/M    sig figs (count / round / calc with rules),
                        density, moles solver (m, M, n, #), isotope average
3 LIGHT E=hv c=λv Φ     c=λv & E=hv, photoelectric (KE, Φ, threshold, e⁻ velocity),
                        Rydberg (λ from n's, unknown n), Bohr En and ΔE
4 ATOM λ=h/mv Δx n l    de Broglie, Heisenberg, quantum numbers (info + checker),
                        nodes (both directions), Coulomb F and V
5 MY NOTES              handwritten notes from my sheets
6 EQUATION SHEET        whole official sheet (constants, conversions, atom, thermo, gases/pH)
7 MORE/SI TABLE/QUIT    SI table + mnemonics, TA "memorize" list, EM spectrum,
                        H lines & photoelectric, history of experiments, QUIT
```

## Tips
- Every prompt accepts math, e.g. type `2*1.008+16.00` for a molar mass,
  `2.3*1.602E-19` to put eV into joules, or `625/1000` to turn grams into kg.
- Sig figs → *Count* and *Calc*: type the number exactly as written (keep zeros
  and the decimal point; use `2nd EE` for ×10^). The calculator itself drops
  trailing zeros, so it can't see them otherwise.
- `v` on screen = frequency (ν); velocity prompts say VELOCITY / VEL.
- The programs use the letter variables A–Z, Str1–Str9, and the lists
  ʟPRE and ʟUF, so anything you stored in those will be overwritten.

## Rebuilding
`programs.py` holds the source; `python3 build.py` (needs `pip install tivars`)
regenerates `8xp/*.8xp` and readable `src/*.txt`, and checks that every line fits
the 26-character screen.
