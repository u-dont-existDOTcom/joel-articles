"""Section 13 draft v11 (2026-10-15): v10 with round r8's findings fixed (review-r8/DISPOSITIONS-r8.md). Each fix is an
exact old -> new pair on one v10 paragraph. Writes v11.md and v11-fixes.json. Run from this folder: python3 make_v11.py"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent


def blocks(md):
    return [b.strip() for b in re.split(r'\n\s*\n', md) if b.strip()]


v9 = blocks((HERE / 'v10.md').read_text(encoding='utf-8'))
IDS = [None, 'H1-P1', 'H1-P2', 'H1-P3', 'H1-P4', None, 'H2-P1', 'H2-P2', 'H2-P3', 'H2-P3b', 'H2-P4', None, 'H3-P1',
       'H3-P2', 'H3-P3', 'H3-P4', 'H3-P5', None, 'H4-P1', 'H4-P2', 'H4-P3', 'H4-P4', 'H4-P5', 'H4-P6', 'H4-P7', 'H4-P8',
       'H4-P9', None, 'H5-P1', 'H5-P2', 'H5-P3', 'H5-P4']
assert len(IDS) == len(v9) and all((i is None) == b.startswith('#') for i, b in zip(IDS, v9))
text = {i: b for i, b in zip(IDS, v9) if i}

FIX = {
 'H1-P2': [('allowing each of you to take the time you need,', 'giving each of you time,',
            'stance check against the article so far, r8: section 4\'s relational pl/ork gives everyone equal time; the '
            'published "Give each person time"')],
 'H4-P8': [("(Sorry, hanging out doesn't count!)", "(Hanging out doesn't count, I'm afraid!)",
            'march: still no break in reading a of r8; the writer\'s voice ("I\'m afraid") the way "I know" and "I realize" '
            'have read as breaks in every reading')],
 'H5-P1': [('Even a safe community can\u2019t promise to keep everyone.', 'A safe community can\u2019t promise to keep everyone. Yes, really.',
            'trace T3 of r8: "Even" made safety a concession; "Yes, really." is the break (march: none in reading b of r8), '
            'the published claim said again as a reaction'),
           ('won\u2019t respect essential boundaries and won\u2019t stop,', 'keeps violating essential boundaries,',
            'trace T3 of r8: the published "repeatedly violates"')],
 'H5-P3': [('a professional, a court,', 'a professional, an autonomous regional institution, a court,',
            'the published list, with the institution back in it'),
           ('The Zapatistas have been important in opening my eyes to the possibilities of autonomous regional institutions, '
            'which can review local power without becoming the state.',
            'The Zapatistas are an important correction here: autonomous institutions can review local power without becoming '
            'the state, and when power crept up in theirs, they pushed it back down.',
            'traces T4 of r6 and r8 ("opening my eyes" a personal claim), the published-essay stance check of r8 ("regional" '
            'narrowed the lesson) and both cold reads of r8 (section 9 tells how their higher levels were dissolved): the '
            'published sentence, and section 9\'s account as its last clause')],
}
log = []
for pid, fixes in FIX.items():
    t = text[pid]
    for old, new, why in fixes:
        assert t.count(old) == 1, (pid, old)
        t = t.replace(old, new)
        log.append({'id': pid, 'old': old, 'new': new, 'why': why})
    text[pid] = t
out = [b if i is None else text[i] for i, b in zip(IDS, v9)]
(HERE / 'v11.md').write_text('\n\n'.join(out) + '\n', encoding='utf-8')
(HERE / 'v11-fixes.json').write_text(json.dumps(log, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('v11.md:', len([b for b in out if not b.startswith('#')]), 'paragraphs;', len(log), 'fixes; changed:', sorted(FIX))
