"""Section 16 draft v28 (2026-10-17 13:11 UTC): v26 kni (the best faithful version, Mostly Human 0.32 with one 61-word window
from the showers sentence into the land line, 399g, https://www.pangram.com/history/112d2d5b-83c3-439a-a38a-74a631b7fe13)
with Joel's answers of 13:11 (joel-20261017/joel-20261017-1311-message.txt):
- question 42: "I replaced the AI lines with: "And whether communal showers feel liberating, or make you start looking at studio
  apartments! No manifesto is going to tell you any of that! Look before you leap. It will really save you some time & money."
  and now the whole section is 100% human. I felt like "do those three things" also sounded ai bc instruction manual + ai
  always doing three things." His first two sentences are H3-P6's last two as they stood; his last two replace H3-P7 ("Do those
  three things before you spend serious time or money looking for land. I know, I know!"), which stays its own paragraph;
- "practice comes before property p3: remove "quietly" that's an ai tell at the end": H1-P3's last sentence without it.
Writes v28.md. Run from this folder: python3 make_v28.py"""
import pathlib, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
subprocess.run([sys.executable, str(HERE / 'make_v26.py'), 'kni'], check=True, capture_output=True)
t = (HERE / 'v26.md').read_text(encoding='utf-8')
CH = [
    ("Do those three things before you spend serious time or money looking for land. I know, I know!",
     "Look before you leap. It will really save you some time & money."),
    ("(That sounds kind of weird when somebody else is quietly paying the tax bill.)",
     "(That sounds kind of weird when somebody else is paying the tax bill.)"),
]
for old, new in CH:
    assert t.count(old) == 1, old
    t = t.replace(old, new)
JOEL_P6_END = ("And whether communal showers feel liberating, or make you start looking at studio apartments! No manifesto is going to "
               "tell you any of that!")
assert t.count(JOEL_P6_END) == 1
(HERE / 'v28.md').write_text(t, encoding='utf-8')
print('wrote v28.md')
