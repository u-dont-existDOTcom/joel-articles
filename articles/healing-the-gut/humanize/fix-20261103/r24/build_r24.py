#!/usr/bin/env python3
"""r24 = r23 with Phase 4's first organ case joined to the check it starts.

r23's rewrite took the cut of Phases 4 and 5 to Human Written, no Low (#191), and the cut of Phases 3 to 6 to Mostly
Human Written, 4.2% AI (#192), where its only AI window was Phase 4's first organ case ("If your pancreas doesn't make
enough digestive enzymes, called Exocrine Pancreatic Insufficiency, you'd test for that with Stool Elastase, and treat it
with high-dose enzymes.", AI Low) and the 5-word sentence before it, "So check your organs (Brown).", read Low. In that cut
the check stands alone and the case starts on "If your pancreas" with nothing in its words tying it to the check
(neuro-2026-11-06b); his usual fix joins a short sentence to the one it introduces (E368). So: "So check your organs
(Brown), starting with your pancreas: if it doesn't make enough digestive enzymes, ...". The words of the case stay as he
approved them (batch 12, F12-2). Writes r24.md and CHANGES.json."""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
md = (HERE.parent / 'r23' / 'r23.md').read_text(encoding='utf-8')
CHANGES = []


def ch(old, new, kind, why):
    global md
    assert md.count(old) == 1, (old[:60], md.count(old))
    md = md.replace(old, new)
    CHANGES.append({'old': old, 'new': new, 'kind': kind, 'why': why})


ch('So check your organs (Brown). If your pancreas doesn\'t make enough digestive enzymes,',
   'So check your organs (Brown), starting with your pancreas: if it doesn\'t make enough digestive enzymes,', 'window',
   'In the cut of Phases 3 to 6 (#192) "So check your organs (Brown)." read Low alone and the first organ case AI Low: the '
   'short sentence joined to the case it introduces (E368), with the tie in the words, "starting with your pancreas" '
   '(neuro-2026-11-06b)')
(HERE / 'r24.md').write_text(md, encoding='utf-8')
(HERE / 'CHANGES.json').write_text(json.dumps(CHANGES, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print(len(CHANGES), 'change;', len(md.split()), 'words')
