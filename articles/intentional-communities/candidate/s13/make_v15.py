"""Section 13 draft v15 (2026-10-15): v14 with round r10's findings fixed (review-r10/DISPOSITIONS-r10.md). Each fix is
an exact old -> new pair on one v14 paragraph. Writes v15.md and v15-fixes.json. Run from this folder: python3 make_v15.py"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent


def blocks(md):
    return [b.strip() for b in re.split(r'\n\s*\n', md) if b.strip()]


v9 = blocks((HERE / 'v14.md').read_text(encoding='utf-8'))
IDS = [None, 'H1-P1', 'H1-P2', 'H1-P3', 'H1-P4', None, 'H2-P1', 'H2-P2', 'H2-P3', 'H2-P3b', 'H2-P4', None, 'H3-P1',
       'H3-P2', 'H3-P3', 'H3-P4', 'H3-P5', None, 'H4-P1', 'H4-P2', 'H4-P3', 'H4-P4', 'H4-P5', 'H4-P6', 'H4-P7', 'H4-P8',
       'H4-P9', None, 'H5-P1', 'H5-P2', 'H5-P3', 'H5-P4']
assert len(IDS) == len(v9) and all((i is None) == b.startswith('#') for i, b in zip(IDS, v9))
text = {i: b for i, b in zip(IDS, v9) if i}

FIX = {
 'H3-P3': [("need to be recorded somewhere, and can't depend on one person's permission.",
            "need to be recorded somewhere, and can't depend on one person's memory or permission.",
            'trace T1 of r10: "memory" lost; the published words, and the fix loses nothing')],
 'H4-P5': [("(A full member's rights and responsibilities should be addressed in the agreements you draw up when you are first "
            "starting your group.)",
            "(A full member's rights and responsibilities should be addressed in your founding agreements.)",
            'stance check against the article so far, r10: the timing put members\' rights before practice and a processed '
            'conflict (section 16\'s order); the published "follow the founding agreements" sets no time')],
 'H5-P3': [("a regulatory agency, an emergency service. The Zapatistas",
            "a regulatory agency, an emergency service. Just not the community itself! The Zapatistas",
            'march: no break in either reading of r10 once his sentence replaced my aside; the published "not reviewing its '
            'own conduct" said again as a reaction')],
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
(HERE / 'v15.md').write_text('\n\n'.join(out) + '\n', encoding='utf-8')
(HERE / 'v15-fixes.json').write_text(json.dumps(log, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('v15.md:', len([b for b in out if not b.startswith('#')]), 'paragraphs;', len(log), 'fixes; changed:', sorted(FIX))
