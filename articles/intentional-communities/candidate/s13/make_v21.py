"""Section 13 draft v21 (2026-10-15): v20 with round r13's findings fixed (review-r13/DISPOSITIONS-r13.md). Each fix is an
exact old -> new pair on one v20 paragraph. Writes v21.md and v21-fixes.json. Run from this folder: python3 make_v21.py"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent


def blocks(md):
    return [b.strip() for b in re.split(r'\n\s*\n', md) if b.strip()]


v9 = blocks((HERE / 'v20.md').read_text(encoding='utf-8'))
IDS = [None, 'H1-P1', 'H1-P2', 'H1-P3', 'H1-P4', None, 'H2-P1', 'H2-P2', 'H2-P3', 'H2-P3b', 'H2-P4', None, 'H3-P1',
       'H3-P2', 'H3-P3', 'H3-P4', 'H3-P5', None, 'H4-P1', 'H4-P2', 'H4-P3', 'H4-P4', 'H4-P5', 'H4-P6', 'H4-P7', 'H4-P8',
       'H4-P9', None, 'H5-P1', 'H5-P2', 'H5-P3', 'H5-P4']
assert len(IDS) == len(v9) and all((i is None) == b.startswith('#') for i, b in zip(IDS, v9))
text = {i: b for i, b in zip(IDS, v9) if i}

FIX = {
 'H2-P3': [("Throw sexuality and gender onto that list. Where do you stand? Could", "Throw sexuality and gender onto that list. Could",
            'march of r13: no break in either reading'),
           ("its values on freedom and child-rearing are incomplete.", "its values on freedom and child-rearing are incomplete. Both of them!",
            'the break: the published "hasn\'t finished discussing either freedom or child-rearing values" said again as a reaction')],
 'H3-P5': [("For the order to do all this in, see Diana Leafe Christian\u2019s", "For the full sequence, see Diana Leafe Christian\u2019s",
            'trace T1 of r13: "full" lost, and "all this" names nothing'),
           ("First you get the vision, then you get the members, then you pool the major resources, and lastly you get the land.",
            "the vision comes before the members, the members before you pool the major resources, and the land comes last.",
            'stance checks against the article so far of r11 and r13 and the repeats check of r12 (C4): "First" put the vision '
            'ahead of practice and a processed conflict; the published puts pairs in order')],
 'H4-P5': [("Have you thought about these questions:", "Write down your answers to these questions:",
            'both stance checks of r13: the published "Define", and his "would require written terms" (2026-10-11)'),
           ("(Hint: not the person who recruited them!)", "(Hint: not the person who recruited them! \U0001F61C)",
            'march of r13: the hint a break in reading a only; his articles use emoji in practical steps (his preference); '
            '\U0001F61C is on his allowlist (tools/humanization/EMOJI-LIST.md), \U0001F609 is his ban (the linter caught it)')],
 'H5-P3': [("Just not the community itself!", "Just not whoever\'s being reviewed!",
            'stance check against the article so far of r13: the published test is whether the layer reviews its own conduct, '
            'not who it is')],
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
(HERE / 'v21.md').write_text('\n\n'.join(out) + '\n', encoding='utf-8')
(HERE / 'v21-fixes.json').write_text(json.dumps(log, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('v21.md:', len([b for b in out if not b.startswith('#')]), 'paragraphs;', len(log), 'fixes; changed:', sorted(FIX))
