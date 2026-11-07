#!/usr/bin/env python3
"""r31 = r30 with oxytocin's gloss corrected, after Joel's comment on card F14-3 (2026-11-07 01:11 UTC): "altho oxytocin
is a bonding hormone not the love hormone exactly" (lesson gut-2026-11-07c). Cleveland Clinic lists oxytocin's roles in
trust, romantic attachment and parent-infant bonding; "love hormone" is the nickname those roles gave it
(https://my.clevelandclinic.org/health/articles/22618-oxytocin). r30 has all five batch-14 cards in, as approved.
Writes r31.md and CHANGES.json."""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
md = (HERE.parent / 'r30' / 'r30.md').read_text(encoding='utf-8')
old = 'boosts oxytocin (the "love hormone")'
new = 'boosts oxytocin (a bonding hormone)'
assert md.count(old) == 1
md = md.replace(old, new)
CHANGES = [{'old': old, 'new': new, 'kind': 'fact',
            'why': 'Joel on F14-3: "altho oxytocin is a bonding hormone not the love hormone exactly"; the gloss says what '
                   'oxytocin is, not its nickname (gut-2026-11-07c)',
            'source': 'https://my.clevelandclinic.org/health/articles/22618-oxytocin'}]
(HERE / 'r31.md').write_text(md, encoding='utf-8')
(HERE / 'CHANGES.json').write_text(json.dumps(CHANGES, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print(len(CHANGES), 'change;', len(md.split()), 'words')
