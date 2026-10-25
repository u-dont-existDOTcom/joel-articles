#!/usr/bin/env python3
"""Turn 109, after reshape_t109.py: the three OWNER-EDITS.json entries whose whole-paragraph strings the reshape split. Each
string becomes the runs of its sentences that stay together, every one still required word for word, with a history note.
The reshape itself waits for his decision on the review page (experiments/t109-review/), so it gets no entry of its own."""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
P = HERE.parents[1] / 'OWNER-EDITS.json'
WHEN = 'Turn 109 (his answers of 2026-10-25 14:20 UTC, experiments/t109-answers/JOEL-20261025-1420.md)'
data = json.loads(P.read_text(encoding='utf-8'))
by = {e['id']: e for e in data['entries']}

SPLITS = {
    'sws-p1-protective-part': [
        "You might go looking for your little one and get mad instead, or realize you've been staring at the rug. I count that as pl/ork too, even if it feels like it's in the way. Before you decide where it's coming from, ask it what it's trying to stop, or what it wants.",
        "Maybe it just has something to say. It could be your little one, mad that you took so long to come back, or a part of you that's trying to protect you. Maybe it's that parent you inherited, or something from earlier today, or a bit of each."],
    'sws-p3-p5-joel': [
        "You can tell that part something like, \"I see you. I'm not going to force my way past you. What's going on?\" Or however you'd actually say that. Then wait and listen patiently.",
        "If nothing comes, that's fine for now. No need to answer for that part just because you'd set this up as a healing session. Even without the answer, you can notice what sets the reaction off, and you can understand what the reaction is propelling you toward, and away from."],
    'joel-102-20261023': [
        "Although personally I wouldn't even bother with that, because whatever they tell you today, the law can change tomorrow.",
        "I'd assume that what you tell won't be completely confidential, especially if it sounds like something dangerous."],
}
NOTES = {
    'sws-p1-protective-part': 'P1 is two runs now: its first three sentences open the section\'s plain path, and the next three open the paragraph about who it might be.',
    'sws-p3-p5-joel': 'his P4 is two runs now: his line to say and "Then wait and listen patiently." close the plain path, and his "If nothing comes" lines are their own paragraph, next to his "Or if you do get an answer".',
    'joel-102-20261023': 'his "I\'d assume" sentence opens Before You Tell the Hardest Stuff now, with his danger lines, and "Although personally I wouldn\'t even bother with that" closes his paragraph about asking what the law requires.',
}
for key, runs in SPLITS.items():
    e = by[key]
    joined = ' '.join(runs)
    hits = [s for s in e['must_contain_exact'] if s == joined]
    assert len(hits) == 1, key
    i = e['must_contain_exact'].index(hits[0])
    e['must_contain_exact'][i:i + 1] = runs
    e.setdefault('history', []).append(WHEN + ': 104 A, reshape_t109.py: ' + NOTES[key] + ' Every sentence is still required word for word.')
P.write_text(json.dumps(data, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('updated', ', '.join(SPLITS))
