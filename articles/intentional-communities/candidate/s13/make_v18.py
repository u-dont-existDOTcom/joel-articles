"""Section 13 draft v18 (2026-10-15): v17 (H3-P1 way A) with round r11's findings fixed (review-r11/DISPOSITIONS-r11.md).
Each fix is an exact old -> new pair on one v17 paragraph. Writes v18.md and v18-fixes.json. Run from this folder:
python3 make_v18.py"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent


def blocks(md):
    return [b.strip() for b in re.split(r'\n\s*\n', md) if b.strip()]


v9 = blocks((HERE / 'v17.md').read_text(encoding='utf-8'))
IDS = [None, 'H1-P1', 'H1-P2', 'H1-P3', 'H1-P4', None, 'H2-P1', 'H2-P2', 'H2-P3', 'H2-P3b', 'H2-P4', None, 'H3-P1',
       'H3-P2', 'H3-P3', 'H3-P4', 'H3-P5', None, 'H4-P1', 'H4-P2', 'H4-P3', 'H4-P4', 'H4-P5', 'H4-P6', 'H4-P7', 'H4-P8',
       'H4-P9', None, 'H5-P1', 'H5-P2', 'H5-P3', 'H5-P4']
assert len(IDS) == len(v9) and all((i is None) == b.startswith('#') for i, b in zip(IDS, v9))
text = {i: b for i, b in zip(IDS, v9) if i}

FIX = {
 'H3-P3': [("Large transfers (land, equipment, stores or outside cash) need to be recorded somewhere, and can't depend on one "
            "person's memory or permission.",
            "Large transfers (land, equipment, stores or outside cash) can't depend on one person's memory or permission.",
            'trace T2 of r11: "recorded somewhere" added a requirement; with trace T1 of r10 on the same words, two tracers; '
            'the published sentence')],
 'H5-P3': [("'Outside' doesn't have to be a nation-state.", "'Outside' doesn't always mean the nation-state.",
            'cold reads of r10 (a) and r11 (four of six): which way "that way" points in Joel\'s next sentence; his published '
            '"does not always mean the nation-state", so it leans toward the state')],
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
(HERE / 'v18.md').write_text('\n\n'.join(out) + '\n', encoding='utf-8')
(HERE / 'v18-fixes.json').write_text(json.dumps(log, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('v18.md:', len([b for b in out if not b.startswith('#')]), 'paragraphs;', len(log), 'fixes; changed:', sorted(FIX))
