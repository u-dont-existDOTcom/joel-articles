#!/usr/bin/env python3
"""apply_r33.py - round 33's answers (Joel, exported 2026-11-11 19:54:04 UTC; ANSWERS-R33-20261111-1954.json) put into the
guide: the boilerplate he asked me to find (his round-32 note on GROUND-ROOM), cut where he approved it.

- LABELS-CUT, approved (after a reject), with his question "or should we label the evidence like this instad of removing
  the labeling idea? we do label evidence like this already i think but not with these exact labels.": the section goes;
  the guide already labels its evidence where each claim is ("just anecdotes", "preclinical but relevant", "a recent
  systematic review found the evidence for major outcomes inconclusive"), so the answer to his question goes in the
  turn's report, with tags on the remedy headings offered if he wants them.
- STILL-CUT, approved: Stillness or Movement? goes, heading and all four paragraphs.
- MENU-CUTS, approved, with his comment "ok I would like to add next to Buteyko reduced breathing that Systema continuous
  partial breathing in coordination with relaxed movement and muscular detensioning is excellent for entering a flow
  state. It helps to watch a video on how to do it prior though, as it's a bit tricky to understand compared to simple
  reduced breathing.": the card's lines go, except the reduced-breathing line, which his line sits next to and compares
  itself with ("simple reduced breathing"). That line now names the technique as he does ("Buteyko reduced breathing"),
  and his line follows it as he wrote it. The Buteyko evidence note goes, as approved.
- SMELL, "yes" (A): a Smell part right after Body, one line pointing to the remedies.
- ANCHOR-CUTS, HELPER-CUTS, REDEFINE-CUTS, approved: as the cards had them.
- SMALL-CUTS, "agree with ur advice": e, f and g go (the revelation after breakfast, "A vitamin is not automatically
  harmless.", "Twelve simultaneous techniques can become another form of panic."); a to d stay.

  python3 apply_r33.py      write the guide after round 33 and print what changed
"""
import hashlib
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parent.parent
BJ = ART / 'GUIDE-SO-FAR-blocks.json'
MD = ART / 'GUIDE-SO-FAR.md'
BLOCKS = json.loads(BJ.read_text(encoding='utf-8'))
before_md = MD.read_text(encoding='utf-8')
assert '\n\n'.join(b['md'] for b in BLOCKS) + '\n' == before_md, 'the blocks and the guide disagree'
A = json.loads((HERE / 'ANSWERS-R33-20261111-1954.json').read_text(encoding='utf-8'))
R = json.loads((HERE / 'REVIEW-R33.json').read_text(encoding='utf-8'))
assert A['review_id'] == R['review_id'] == 'bad-trips-r33'
assert hashlib.sha256((HERE / 'PAGE-R33.md').read_bytes()).hexdigest() == A['article']['sha256']
I = {x['id']: x for x in A['items']}
for cid in ('MENU-CUTS', 'STILL-CUT', 'ANCHOR-CUTS', 'HELPER-CUTS', 'REDEFINE-CUTS', 'LABELS-CUT'):
    assert I[cid]['status'] == 'approved', cid
assert I['SMELL']['comment'].strip().lower() == 'yes'
assert I['SMALL-CUTS']['comment'].strip().lower() == 'agree with ur advice'
SYSTEMA = I['MENU-CUTS']['comment'].strip()
assert SYSTEMA.startswith('ok I would like to add next to Buteyko reduced breathing that ')
SYSTEMA = SYSTEMA[len('ok I would like to add next to Buteyko reduced breathing that '):]
SYSTEMA = SYSTEMA[0].upper() + SYSTEMA[1:]
assert SYSTEMA == ('Systema continuous partial breathing in coordination with relaxed movement and muscular detensioning is '
                   'excellent for entering a flow state. It helps to watch a video on how to do it prior though, as it\'s a '
                   'bit tricky to understand compared to simple reduced breathing.')


def ids():
    return [b['id'] for b in BLOCKS]


def unit(bid):
    return BLOCKS[ids().index(bid)]


def cut(bid, expect_start):
    b = unit(bid)
    assert b['md'].startswith(expect_start), (bid, b['md'][:80])
    BLOCKS.remove(b)


def cut_items(bid, starts):
    b = unit(bid)
    lines = b['md'].split('\n')
    keep = [l for l in lines if not any(l.startswith('- ' + s) for s in starts)]
    assert len(lines) - len(keep) == len(starts), (bid, starts)
    b['md'] = '\n'.join(keep)


def swap(bid, old, new):
    b = unit(bid)
    assert b['md'].count(old) == 1, (bid, old)
    b['md'] = b['md'].replace(old, new)


# LABELS-CUT
cut('B147', '## How I label the evidence')
cut('B148', '- **Established acute treatment:**')
# STILL-CUT
cut('B248', '### Stillness or Movement?')
cut('B249', 'Test stillness and movement')
cut('B250', 'When lying down feels like imprisonment')
cut('B251', '**Parallel processing**')
cut('B313', '**Movement evidence note:**')
# MENU-CUTS, with the reduced-breathing line kept for his Systema line
cut_items('B298', ['Feel both feet against the floor.', 'Hold something with weight or texture.',
                   'Slowly unclench the jaw, hands, belly, and shoulders.'])
cut_items('B302', ['Try inhaling for four and exhaling for six, without strain.'])
swap('B302', '- Or breathe softly and slowly through the nose, taking in slightly less air than desired until there is '
             'faint air hunger.',
     '- Or try Buteyko reduced breathing: breathe softly and slowly through the nose, taking in slightly less air than '
     'desired until there is faint air hunger.\n- ' + SYSTEMA)
cut('B314', '**Buteyko evidence note:**')
cut_items('B304', ['Silence is a real option.', 'Keep the stop or change control immediate.'])
cut_items('B308', ['Ask one calm person to stay as the lead anchor.', 'Let them remind you where you are.'])
# SMELL, A: right after Body
SMELL = ('- Scratch & sniff a lime peel, or smell an authentic calming essential oil, the Metta NMT sniffer or humic acid '
         'powder (see Mental Stabilizers That Don\'t Abort the Trip).')
k = ids().index('B298') + 1
assert ids()[k] == 'B301'
BLOCKS[k:k] = [{'id': 'R33-SMELL', 'kind': 'p', 'md': '**Smell**', 'text': None},
               {'id': 'R33-SMELL-L', 'kind': 'ul', 'md': SMELL, 'text': None}]
# ANCHOR-CUTS
cut('B259', '**Script for the sitter or friend:**')
cut('B260', '> I\'m here. You\'re not alone.')
cut('B274', 'When the body still needs movement, keep it contained and boring')
# HELPER-CUTS
cut_items('B282', ['Reflect without arguing:', 'Keep the room quiet, private, warm', 'Translate metaphysics into shared'])
cut('B290', 'Redirect within the person\'s value-world')
# REDEFINE-CUTS
cut('B360', 'A bad trip or destabilizing state may also come from')
cut('B362', 'Cognitive distortions from Cognitive Behavioral Therapy')
cut('B363', '- **Catastrophizing:**')
# SMALL-CUTS e, f, g
cut('B328', 'The revelation will still exist after breakfast.')
swap('B212', ' A vitamin is not automatically harmless.', '')
swap('B295', ' Twelve simultaneous techniques can become another form of panic.', '')

MD.write_text('\n\n'.join(b['md'] for b in BLOCKS) + '\n', encoding='utf-8')
BJ.write_text(json.dumps(BLOCKS, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
after = MD.read_text(encoding='utf-8')
print('words: %d -> %d' % (len(before_md.split()), len(after.split())))
print(unit('B302')['md'])
