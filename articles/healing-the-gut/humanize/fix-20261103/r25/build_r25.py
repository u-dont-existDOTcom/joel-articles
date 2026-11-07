#!/usr/bin/env python3
"""r25 = r24 with Phase 4's second organ case in its own shape.

Phase 4's organ paragraph by itself read AI Generated, 100%, High (#196), though the same words read High inside Phases
4 and 5 (#194) and the whole protocol section (#195). My r23 rewrite had given the second case the first case's mould word
for word ("if ..., called ..., you'd test for that with ..., and treat it with ..."): two sentences of one template, the
parallel build models write, where his own versions vary the shape (his Phase 1: questions, then "Then according to Hale",
"Rosenberg's fix is", "Hale says"). The first case stays as he approved it (batch 12, F12-2, with r24's join); the second
gets its own shape: the term in parentheses, and Brown acting ("Brown has you tested with SeHCAT and put on bile binders",
neuro-2026-11-06e). "Too much of your bile ... reaching your colon" is NICE DG44's account: bile acids that aren't absorbed
travel to the colon, and the excess there causes diarrhoea. Writes r25.md and CHANGES.json."""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
md = (HERE.parent / 'r24' / 'r24.md').read_text(encoding='utf-8')
CHANGES = []
old = ('And if bile is spilling into your colon and giving you diarrhea, called Bile Acid Diarrhea, you\'d test for that '
       'with SeHCAT, and treat it with bile binders.')
new = ('If too much of your bile is reaching your colon and giving you diarrhea (Bile Acid Diarrhea), Brown has you tested '
       'with SeHCAT and put on bile binders.')
assert md.count(old) == 1
md = md.replace(old, new)
CHANGES.append({'old': old, 'new': new, 'kind': 'window',
                'why': 'the organ paragraph alone read AI High (#196): two cases in one mould; the second now has its own '
                       'shape, with the term in parentheses and Brown acting',
                'source': 'https://nice.org.uk/guidance/dg44/documents/topic-description'})
(HERE / 'r25.md').write_text(md, encoding='utf-8')
(HERE / 'CHANGES.json').write_text(json.dumps(CHANGES, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print(len(CHANGES), 'change;', len(md.split()), 'words')
