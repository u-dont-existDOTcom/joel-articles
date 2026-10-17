"""Section 14 draft v6 (2026-10-17): v5 deduplicated, as Joel asked (2026-10-16 23:38 UTC: "let's merge/dedup section 14 without
losing important things pls"). Round r3's repeats check (review-r3/REPEATS.md) found two repeats inside the section that v5 still
had, both in the published text too:

- item 2: P2 asks twice who keeps people housed, fed and cared for ("who is responsible for ensuring that everyone has a place to
  live and food to eat?" and "Who takes responsibility for bridging people's food, housing and care, and any outside cash or
  benefits, if relevant?"); the second adds only the outside cash or benefits, so it keeps just that.
- item 3: P5 opens "Institutions and relationships don't die at the same time." and the last paragraph says it again for what
  people learned to give one another. The check found P5 the better carrier (it has the case, the Farm sisters); the last
  paragraph's own part, "some of what people learned to give one another may go on", moves into P5's first sentence, and the
  last paragraph goes, with my break "I hope so, anyway.". The section now ends on the father paragraph.

The other repeats round r3 counted are with other sections and stay as they are, each for its reason (STATUS.md, 2026-10-17
entry). Writes v6.md and v6-fixes.json. Run from this folder: python3 make_v6.py"""
import json, pathlib

HERE = pathlib.Path(__file__).resolve().parent
FIX = [
    ('P2', 'Who takes responsibility for bridging people’s food, housing and care, and any outside cash or benefits, if relevant?',
     'Who takes responsibility for bridging any outside cash or benefits people depend on, if relevant?',
     'repeats r3 item 2: food, housing and care are already asked about in the first two questions; the new part is the outside '
     'cash or benefits'),
    ('P5', 'Institutions and relationships don’t die at the same time. What a relief!',
     'Institutions and relationships don’t die at the same time, and some of what people learned to give one another may go on '
     'too. What a relief!',
     'repeats r3 item 3: the last paragraph told P5\'s point again; its own part, what people learned to give one another, is here '
     'now'),
    ('P7', '\n\nEven after the community ends as a legal entity, some of what people learned to give one another may go on. I hope '
           'so, anyway.', '',
     'repeats r3 item 3: merged into P5 (the legal entity is P5\'s "institutions")'),
]
t = (HERE / 'v5.md').read_text(encoding='utf-8')
log = []
for pid, old, new, why in FIX:
    assert t.count(old) == 1, old
    t = t.replace(old, new)
    log.append({'id': pid, 'old': old.strip(), 'new': new, 'why': why})
(HERE / 'v6.md').write_text(t, encoding='utf-8')
(HERE / 'v6-fixes.json').write_text(json.dumps(log, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print(t[-900:])
