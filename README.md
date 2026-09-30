# CHEM 105 Notes — TI-84 Plus CE (TI-BASIC)

One program, `CHEM`, with my CHEM 105 notes organized by category.

## Install
1. Open **TI Connect CE**, plug in the calculator, go to Calculator Explorer.
2. Drag **all 12 files** in `8xp/` onto the calculator (choose **Replace** if asked):
   `CHEM, CHFULL, CHF1 ... CHF10`. FULL NOTES needs all of them.
3. On the calculator: `prgm` → `CHEM` → `ENTER` → `ENTER`.

## Menu
```
CHEM 105 NOTES
0 FULL NOTES ►            10 categories (CHFULL + CHF1..CHF10), each with topic pages
1 PREFIXES 10^x k μ n     E..a table with powers of ten + converting
2 QUANTUM #S & NODES      n, l, ml, total/planar/radial nodes
3 e⁻ RULES/PRINCIPLES     Aufbau, Pauli, Hund, Octet*, Le Chatelier*
4 PERIODIC TRENDS         general trends, atomic radius, ions, ionization energy
5 EXPERIMENTS             cathode ray, oil drop, radioactivity, gold foil, Chadwick
6 MORE ►                  Laws list A-F, Light relationships (+/-), Isoelectronic list tool,
                          Electron config tool (full + noble-gas condensed),
                          Accurate vs precise*
7 QUIT
```
`*` = title only, notes to be added later.

Each page: ENTER goes to the next screen; after the last screen it returns to the menu.

## Adding notes
Edit the lists in `programs.py` (plain text, auto-wrapped to the 26-character
screen), then run `python3 build.py` (needs `pip install tivars`). The build
checks every line fits and that no command gets garbled.

## Tools
- **Isoelectronic list**: type a symbol and charge; lists every neutral atom and
  known monatomic ion (standard ion table, no hypothetical ions) with the same
  number of electrons.
- **Electron config**: type a symbol and charge; shows full and noble-gas
  condensed configurations, written in order of n then l (s, p, d, f), with a
  space between orbitals. Includes all 20 measured ground-state exceptions to
  Aufbau for Z <= 103 (Cr, Cu, Nb, Mo, Ru, Rh, Pd, Ag, La, Ce, Gd, Pt, Au, Ac,
  Th, Pa, U, Np, Cm, Lr), marked `*EXCEPTION TO AUFBAU`. Cations lose electrons
  from the highest n first (then highest l), outside the noble-gas core.
  Z >= 104 is marked `*PREDICTED`; ions not in the known-ion table are marked
  `*NOT A KNOWN ION`.

## Full notes
Source text: `full_notes.txt`. Readable copies by category: `FULL NOTES/`.
