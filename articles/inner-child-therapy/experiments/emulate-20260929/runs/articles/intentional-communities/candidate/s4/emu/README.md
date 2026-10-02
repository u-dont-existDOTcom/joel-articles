# Emulate versions of section 4 (2026-10-02, API, two calls per unit)

Exact copies of the outputs on Joel's laptop (`/home/joel/ai-work/claude-dangerous-lane/emulate-runs/community-s4/`); the hash of the 24 texts matched there and here (sha256 of the sorted JSON: ad04f852…). Inputs are in `../emu-in/` (units in `units.json`): e1 = P1+P2, e2 = P3+P4, e3 = P5+P6+P7, e4 = P11+P12, e5 = P15+P16, e6 = P17+P18+P19, e7 = P20+P21, e8 = P22+P23+P24, e9 = P25, e10 = P26, e11 = P27+P28, e12 = P29+P30+P31. Only the paragraphs Pangram flagged in the published section were sent (P8 to P10, P13 and P14 read Human). 24 calls, 1,858 words charged; balance after: 252,835.

Two outputs came back cut off (e3-emuA, e6-emuA, e11-emuA end mid-sentence). Both versions of e4 dropped P11's last sentence and turned P12 into a list item; both versions of e12 said the first three parts create the container, the opposite of P30.
