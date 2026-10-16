"""Section 13 draft v20 (2026-10-15): v19 with round r12's findings fixed (review-r12/DISPOSITIONS-r12.md): the published-
essay stance check on H5-P4, and the repeats my rewrite made (the same concession four times, five breaks opening "Yes", the
land-last line said twice in a row, and the "good person" detector lost). Each fix is an exact old -> new pair on one v19
paragraph. Writes v20.md and v20-fixes.json. Run from this folder: python3 make_v20.py"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent


def blocks(md):
    return [b.strip() for b in re.split(r'\n\s*\n', md) if b.strip()]


v9 = blocks((HERE / 'v19.md').read_text(encoding='utf-8'))
IDS = [None, 'H1-P1', 'H1-P2', 'H1-P3', 'H1-P4', None, 'H2-P1', 'H2-P2', 'H2-P3', 'H2-P3b', 'H2-P4', None, 'H3-P1',
       'H3-P2', 'H3-P3', 'H3-P4', 'H3-P5', None, 'H4-P1', 'H4-P2', 'H4-P3', 'H4-P4', 'H4-P5', 'H4-P6', 'H4-P7', 'H4-P8',
       'H4-P9', None, 'H5-P1', 'H5-P2', 'H5-P3', 'H5-P4']
assert len(IDS) == len(v9) and all((i is None) == b.startswith('#') for i, b in zip(IDS, v9))
text = {i: b for i, b in zip(IDS, v9) if i}

FIX = {
 'H2-P3': [("Throw sexuality and gender onto that list. Yes, it keeps getting longer.",
            "Throw sexuality and gender onto that list. Where do you stand?",
            'repeats r12 (5): one of four concessions and five "Yes" breaks; a question to the reader, the published "write '
            'down what you actually believe" asked of this item')],
 'H3-P5': [("and lastly you get the land. So yes, the land comes last!",
            "and lastly you get the land. (It's in the reading list at the end, too.)",
            'repeats r12 (17, 23): the land-last line said twice in a row, and a "Yes" break; a pointer to his appendix, '
            'which lists the book')],
 'H4-P5': [("(Hint: it shouldn't be the person who recruited them.)", "(Hint: not the person who recruited them!)",
            'the published "The recruiter should not control the decision" as the break, now that the concession goes'),
           (" Yes, it's a lot of homework!", "",
            'repeats r12 (5): one of four concessions and five "Yes" breaks; traces T4 of r7 and T3 of r11: an opinion the '
            'published doesn\'t give')],
 'H4-P6': [("but it won\u2019t tell you if someone is a good person.", "but there\u2019s still no \u201cgood person\u201d detector.",
            'repeats r12 (24): his phrase back ("it does not validate a \u201cgood person\u201d detector"); without it, the '
            'sentence was H4-P4\'s "more evidence, not certainty" in other words')],
 'H5-P4': [("consent to continue in a relationship or a shared life is no longer present",
            "consent to continue in a shared life is no longer present",
            'published-essay stance check of r12: "a relationship" lets a reader take a breakup as grounds for separation, '
            'against his jealousy section; the published consent is to the shared life')],
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
(HERE / 'v20.md').write_text('\n\n'.join(out) + '\n', encoding='utf-8')
(HERE / 'v20-fixes.json').write_text(json.dumps(log, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('v20.md:', len([b for b in out if not b.startswith('#')]), 'paragraphs;', len(log), 'fixes; changed:', sorted(FIX))
