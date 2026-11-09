#!/usr/bin/env python3
"""apply_r28.py - round 28's and round 29's answers (Joel, exported 2026-11-09 17:22:21 and 17:22:46 UTC;
ANSWERS-R28-20261109-1722.json, ../r29/ANSWERS-R29-20261109-1722.json) put into the guide.

- Round 29, TYPO-AYA and TYPO-HYPER, approved: "ayahauasca" to "ayahuasca" (B182), "hyper intelligent" to
  "hyperintelligent" (B219).
- AFT-TERMS, approved, with his comment "link somatic experiencing to my guide at somatic.u-dont-exist.com": the three
  glosses as the card had them, and "Somatic Experiencing" linked to http://somatic.u-dont-exist.com/ (read 2026-11-09:
  it opens his "Somatic Therapy Modalities Map" post, which covers Somatic Experiencing), in the http:// form his other
  site links in the guide have.
- LOOP-ONCE, his comment: "i thought i already merged it and cut that section in the last turn". His round-27 version on
  the card whose stretch was this section put the loop into his first five minutes; the section was the copy elsewhere,
  so it goes (lesson bad-trips-2026-11-09d): the heading, its loop paragraph, "Loop breaker:" and the four steps
  (B371, B372, B374, B375). Its picture, which sat right after the loop paragraph in his post, moves with the loop: right
  after his panic-loop paragraph (R27-PFA3). Warning W106 ("Stop debating ...") and the four numbered steps go as his
  decision (../../humanize/h01/FIDELITY-KEYS-R28.json; W107's "This is a wave" is still said in the sitter's script),
  and so does the q5-room-first owner edit's fourth place.

The other four choices (METHOD-WHERE, AFT-HOW-MUCH, HELPER-NOW, RUE-SAFETY) change nothing here: their answers start the
ToC pass he asked for, and round 30 (see ../../CURRENT-STATE.md).

  python3 apply_r28.py      write the guide after rounds 28 and 29 and print what changed
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

A28 = json.loads((HERE / 'ANSWERS-R28-20261109-1722.json').read_text(encoding='utf-8'))
A29 = json.loads((HERE.parent / 'r29' / 'ANSWERS-R29-20261109-1722.json').read_text(encoding='utf-8'))
R28 = json.loads((HERE / 'REVIEW-R28.json').read_text(encoding='utf-8'))
R29 = json.loads((HERE.parent / 'r29' / 'REVIEW-R29.json').read_text(encoding='utf-8'))
assert A28['review_id'] == R28['review_id'] == 'bad-trips-r28' and A29['review_id'] == R29['review_id'] == 'bad-trips-r29'
assert hashlib.sha256((HERE / 'PAGE-R28.md').read_bytes()).hexdigest() == A28['article']['sha256']
assert hashlib.sha256((HERE.parent / 'r29' / 'PAGE-R29.md').read_bytes()).hexdigest() == A29['article']['sha256']
I28 = {x['id']: x for x in A28['items']}
I29 = {x['id']: x for x in A29['items']}
assert I28['AFT-TERMS']['status'] == 'approved' and 'somatic.u-dont-exist.com' in I28['AFT-TERMS']['comment']
assert I28['LOOP-ONCE']['comment'].startswith('i thought i already merged it and cut that section')
assert I29['TYPO-AYA']['status'] == I29['TYPO-HYPER']['status'] == 'approved'
UNIT = {b['id']: b for b in BLOCKS}


def swap(bid, old, new):
    b = UNIT[bid]
    assert b['md'].count(old) == 1, (bid, old)
    b['md'] = b['md'].replace(old, new)


# round 29
swap('B182', "But when I'm on ayahauasca or", "But when I'm on ayahuasca or")
swap('B219', 'that hyper intelligent state', 'that hyperintelligent state')

# AFT-TERMS, as the card had it, with his link
swap('B426', 'CBT-style reality testing is one way', "CBT-style reality testing, checking the frightening thought against "
     "what's actually happening, is one way")
swap('B426', '**Derealization and depersonalization:**', '**Derealization and depersonalization (when the world, or you '
     'yourself, feel unreal):**')
swap('B426', 'and Somatic Experiencing therapy.', 'and [Somatic Experiencing](http://somatic.u-dont-exist.com/), a therapy '
     'that works through body sensations.')

# LOOP-ONCE: the section goes, its picture moves with the loop
CUT = ['B371', 'B372', 'B374', 'B375']
assert UNIT['B371']['md'] == '## The Fear/Panic Loop'
pic = UNIT['B373']
assert pic['kind'] == 'image' and '633de218' in pic['md']
ids = [b['id'] for b in BLOCKS]
assert ids.index('B373') == ids.index('B372') + 1 and ids.index('B376') == ids.index('B375') + 1
BLOCKS = [b for b in BLOCKS if b['id'] not in CUT and b['id'] != 'B373']
k = [b['id'] for b in BLOCKS].index('R27-PFA3')
BLOCKS.insert(k + 1, pic)

MD.write_text('\n\n'.join(b['md'] for b in BLOCKS) + '\n', encoding='utf-8')
BJ.write_text(json.dumps(BLOCKS, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
after = MD.read_text(encoding='utf-8')
print('words: %d -> %d' % (len(before_md.split()), len(after.split())))
print('cut: %s; the picture B373 now after R27-PFA3' % ', '.join(CUT))
