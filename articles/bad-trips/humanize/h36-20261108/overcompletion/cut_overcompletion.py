#!/usr/bin/env python3
"""cut_overcompletion.py - the overcompletion cuts that lose nothing (gate E328), from five fresh readers' candidates.

Five fresh Sonnet readers, one part of the guide each, blind to whose words they read, given BRIEF.md (his definition:
"overcompletion is when you already have it explained and then you explain it again", and his rulings) found 39
candidates (PART-1.json to PART-5.json); check_candidates.py ran each through the fidelity keys (R25), the keep-as-is
ledger and the owner edits (CHECKED.json). Each was then read by hand (RESULTS.md has every one and what it came to).
These nine say again only what the sentence, the heading or the item before them says, lose no point, key, kept line
or owner edit, and are the model's text, not his; they go in (turn 16, his message of 2026-11-06 19:43 UTC: "make the
cuts regardless of pangram if it makes the guide read better"). Two more, which may be his own lines or hold a change
that read Human, are round 27's cards.

  python3 cut_overcompletion.py
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parents[2]
BJ, MD = ART / 'GUIDE-SO-FAR-blocks.json', ART / 'GUIDE-SO-FAR.md'
CUTS = [  # (block, the words cut: a sentence or a whole block)
    ('B95', ' Calling medics does not require waiting passively, and using a fast field remedy does not require giving up a '
            'time-sensitive medical option.'),
    ('B165', ' The tools in this section are for somebody who still wants the trip to continue.'),
    ('B197', ' The mistake showed me that DMSO and aged ozonated-charcoal water address different kinds of overload.'),
    ('B218', 'Useful substances can still be poor rescue tools when somebody is already destabilized.'),
    ('B224', 'That finishes the rescue-chemistry side of the guide. '),
    ('B295', 'Choose one or two options rather than all of them. '),
    ('B304', ' Music should remain an option, rather than become another authority in the room.'),
    ('B337', 'That is tripsitting, shadow work, and the path becoming practical.'),
    ('B401', ' A demon can fight your hatred, feed on your fear, argue with your pride or seduce your grandiosity, but there\'s '
             'nothing in love for it to grab.'),
]
blocks = json.loads(BJ.read_text(encoding='utf-8'))
assert '\n\n'.join(b['md'] for b in blocks) + '\n' == MD.read_text(encoding='utf-8')
by = {b['id']: b for b in blocks}
for bid, cut in CUTS:
    assert by[bid]['md'].count(cut) == 1, (bid, cut)
    by[bid]['md'] = by[bid]['md'].replace(cut, '')
    print('%-5s %s' % (bid, by[bid]['md'][:110] or '(block gone)'))
blocks = [b for b in blocks if b['md'].strip()]
MD.write_text('\n\n'.join(b['md'] for b in blocks) + '\n', encoding='utf-8')
BJ.write_text(json.dumps(blocks, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
