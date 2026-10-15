"""Section 13 draft v13 (2026-10-15): v12 with round r9's findings fixed (review-r9/DISPOSITIONS-r9.md). Each fix is an
exact old -> new pair on one v12 paragraph. Writes v13.md and v13-fixes.json. Run from this folder: python3 make_v13.py"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent


def blocks(md):
    return [b.strip() for b in re.split(r'\n\s*\n', md) if b.strip()]


v9 = blocks((HERE / 'v12.md').read_text(encoding='utf-8'))
IDS = [None, 'H1-P1', 'H1-P2', 'H1-P3', 'H1-P4', None, 'H2-P1', 'H2-P2', 'H2-P3', 'H2-P3b', 'H2-P4', None, 'H3-P1',
       'H3-P2', 'H3-P3', 'H3-P4', 'H3-P5', None, 'H4-P1', 'H4-P2', 'H4-P3', 'H4-P4', 'H4-P5', 'H4-P6', 'H4-P7', 'H4-P8',
       'H4-P9', None, 'H5-P1', 'H5-P2', 'H5-P3', 'H5-P4']
assert len(IDS) == len(v9) and all((i is None) == b.startswith('#') for i, b in zip(IDS, v9))
text = {i: b for i, b in zip(IDS, v9) if i}

FIX = {
 'H3-P3': [('(cash if it uses money, or tools, transportation, temporary housing, stored goods, the right to keep using something).',
            '(cash if it uses money, but also tools, transportation, temporary housing, stored goods or the right to keep using '
            'something).',
            'trace T3 of r9: the published "but also" (in-kind forms on top of cash), with its "or" before the last item, which '
            'round r7\'s trace wanted (alternatives, not a bundle)')],
 'H4-P8': [("(Hanging out doesn't count, I'm afraid!)", "(Sorry, hanging out doesn't count! I know, it's the fun part.)",
            'march: no break in either reading of r9; "I know" remarks have been breaks in every reading')],
 'H5-P2': [('On the other hand, the power to remove people is one of the easiest to abuse.',
            'On the other hand, the power to remove people is also one of the easiest to abuse.',
            'trace T5 of r9: "also", a further fact, as published'),
           ('How can the person reply and request a review or appeal of the decision without endangering others?',
            'How can the person reply, and what review or appeal is possible without endangering others?',
            'trace T5 of r9: the published "what review or appeal is possible"'),
           ('What will be done to provide housing, protect records, preserve access to family, allow access to common resources, '
            'and/or provide access to outside funds (if any)?',
            'What will be done to protect their housing, records, family contact, and access to common resources or outside '
            'funds (if any) during separation?',
            'trace T5 of r9: protect what the person has, all of it, during separation')],
 'H5-P3': [(', an emergency service, or anything else.', ', an emergency service.',
            'traces T5 of r6 and T6 of r9: the published names the forms; two reviewers now'),
           ('and when power crept up in theirs, they pushed it back down.',
            'and when power crept up in their own system, they pushed it back down.',
            'trace T6 of r9: "theirs" could be any autonomous institutions; the clause is section 9\'s account (kept: '
            'review-r9/DISPOSITIONS-r9.md)')],
 'H5-P4': [('or for accepting the finality of separation when', 'or for a final separation when',
            'trace T6 of r9: the separation itself, as published, not someone\'s accepting it')],
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
(HERE / 'v13.md').write_text('\n\n'.join(out) + '\n', encoding='utf-8')
(HERE / 'v13-fixes.json').write_text(json.dumps(log, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('v13.md:', len([b for b in out if not b.startswith('#')]), 'paragraphs;', len(log), 'fixes; changed:', sorted(FIX))
