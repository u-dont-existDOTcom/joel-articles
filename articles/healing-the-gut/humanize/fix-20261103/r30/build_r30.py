#!/usr/bin/env python3
"""r30 = r29 with Phase 4's second organ case in the shape of Phase 6's environment check, the paragraph's last try.

Joined to Phase 4's first paragraph in r24's wording, the paragraph read AI Detected, 23% (#205): the paragraph's own
sentences Human, High, the first case Human, Medium, and the second case AI Low, the one sentence that copies the first
case's mould ("if ..., called ..., you'd test for that with ..., and treat it with ..."). Phase 6 says the same kind of
thing in another shape, and reads High in every check: "Could it be mold/mycotoxins, or Lyme? Get assessed for those, and
if it comes back positive, use specific binders (...)". So the second case asks the reader first, says what happens with
the reader in it, then has them get the test and take the binders. NICE DG44: bile acids that aren't absorbed reach the
colon, and the excess there causes diarrhoea. Writes r30.md and CHANGES.json."""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
md = (HERE.parent / 'r29' / 'r29.md').read_text(encoding='utf-8')
old = ('And if bile is spilling into your colon and giving you diarrhea, called Bile Acid Diarrhea, you\'d test for that '
       'with SeHCAT, and treat it with bile binders.')
new = ('Or is it your bile? If too much of it reaches your colon, you get diarrhea, called Bile Acid Diarrhea. Get a SeHCAT '
       'test for it, and if it comes back positive, take bile binders.')
assert md.count(old) == 1
md = md.replace(old, new)
CHANGES = [{'old': old, 'new': new, 'kind': 'window',
            'why': 'AI Low in the paragraph by itself (#205), copying the first case\'s mould: now in the shape of Phase 6\'s '
                   'environment check (High in every check), with the reader in it',
            'source': 'https://nice.org.uk/guidance/dg44/documents/topic-description'}]
(HERE / 'r30.md').write_text(md, encoding='utf-8')
(HERE / 'CHANGES.json').write_text(json.dumps(CHANGES, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print(len(CHANGES), 'change;', len(md.split()), 'words')
