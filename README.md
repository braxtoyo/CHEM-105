# CHEM 105 Notes — TI-84 Plus CE (TI-BASIC)

One program, `CHEM`, with my CHEM 105 notes organized by category.

## Install
1. Open **TI Connect CE**, plug in the calculator, go to Calculator Explorer.
2. Drag `8xp/CHEM.8xp` onto the calculator (choose **Replace** if asked).
3. On the calculator: `prgm` → `CHEM` → `ENTER` → `ENTER`.

## Menu
```
CHEM 105 NOTES
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
