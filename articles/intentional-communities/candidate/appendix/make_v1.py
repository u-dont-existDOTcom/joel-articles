"""The appendix, draft v1 (2026-10-17): the published appendix with three changes.
- Diana Leafe Christian's entry: "start here for sequencing, membership, money, land, and agreements" becomes "start here for
  membership, money, land, and agreements" (Joel 2026-10-16 23:38 UTC: "no we should not lean on Christian's book order if it
  contradicts my own order that wouldn't make sense so fix that"; his order is section 16's).
- The dedup (Joel 2026-10-17 02:07 UTC: "you can only cut if it isn't losing important meaning or there's no good way to
  merge"; ../s16/review-r1/DISPOSITIONS-r1.md, items 1 and 2): "and now online" goes from his father's film (section 1 says
  it, and the entry links it); "My father lived there for 17 years." goes from Inside the Bruderhof (sections 1 and 4 say it).
Writes v1.md and v1-fixes.json. Run from this folder: python3 make_v1.py"""
import json, pathlib

HERE = pathlib.Path(__file__).resolve().parent
t = (HERE / 'v0.md').read_text(encoding='utf-8')
FIX = [
 ("start here for sequencing, membership, money, land, and agreements.", "start here for membership, money, land, and agreements.",
  'Joel 2026-10-16 23:38 UTC: the book is not recommended for its order; his order is section 16\'s'),
 ("my father’s documentary, made with Jerry Mintz and now online.", "my father’s documentary, made with Jerry Mintz.",
  'dedup (repeats r1 item 1): section 1 says it\'s online, and the entry links it'),
 (" My father lived there for 17 years. The Bruderhof also has", " The Bruderhof also has",
  'dedup (repeats r1 item 2): sections 1 and 4 say it'),
]
log = []
for old, new, why in FIX:
    assert t.count(old) == 1, old
    t = t.replace(old, new)
    log.append({'old': old, 'new': new, 'why': why})
(HERE / 'v1.md').write_text(t, encoding='utf-8')
(HERE / 'v1-fixes.json').write_text(json.dumps(log, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('wrote v1.md')
