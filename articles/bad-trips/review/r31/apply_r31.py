#!/usr/bin/env python3
"""apply_r31.py - round 31's answers (Joel, exported 2026-11-09 18:59:05 UTC; ANSWERS-R31-20261109-1859.json) put into the
guide.

- AFT-PLACE, "c": paranoia and derealization stay in the aftermath list, with the support list right after it.
- MW-ALONE, revised with his version: after "Send the human-anchor script.", as he wrote it ("the other on your solar
  plexus just under your chest", for my "belly"). His comment: "belly must be an ai error, it's funny it keeps changing
  that". The Grounding Menu's "Put one hand on the heart and one on the belly or solar plexus." is that same error, from
  the post's drafted list, so it says the solar plexus too; KEEP-AS-IS K24 and OWNER-EDITS r31-solar-plexus keep it so.
- MW-BREATH and MW-PREP, approved: in as the cards had them.

  python3 apply_r31.py      write the guide after round 31 and print what changed
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
A = json.loads((HERE / 'ANSWERS-R31-20261109-1859.json').read_text(encoding='utf-8'))
R = json.loads((HERE / 'REVIEW-R31.json').read_text(encoding='utf-8'))
assert A['review_id'] == R['review_id'] == 'bad-trips-r31'
assert hashlib.sha256((HERE / 'PAGE-R31.md').read_bytes()).hexdigest() == A['article']['sha256']
I = {x['id']: x for x in A['items']}
assert I['AFT-PLACE']['comment'].strip().lower() == 'c'
assert I['MW-ALONE']['status'] == 'revise' and 'solar plexus' in I['MW-ALONE']['your_version']
assert I['MW-BREATH']['status'] == I['MW-PREP']['status'] == 'approved'
UNIT = {b['id']: b for b in BLOCKS}


def swap(bid, old, new):
    b = UNIT[bid]
    assert b['md'].count(old) == 1, (bid, old)
    b['md'] = b['md'].replace(old, new)


# MW-ALONE: his version, after "Send the human-anchor script."
k = [b['id'] for b in BLOCKS].index('B273') + 1
BLOCKS.insert(k, {'id': 'R31-ALONE', 'kind': 'p', 'md': I['MW-ALONE']['your_version'].strip(), 'text': None})
# MW-BREATH
swap('B302', '- Whisper: "This is a wave."', '- Whisper: "This is a wave. I can love the part of me that feels it."')
# MW-PREP
swap('B366b', 'spiritual breakthroughs. Sometimes', 'spiritual breakthroughs. And train before you need it, sending love to a '
     'frightening image, to someone you hate (without approving of what they did), and to the inner child. Sometimes')
# his correction, where the guide has the same error
swap('B298', '- Put one hand on the heart and one on the belly or solar plexus.',
     '- Put one hand on the heart and one on the solar plexus.')

MD.write_text('\n\n'.join(b['md'] for b in BLOCKS) + '\n', encoding='utf-8')
BJ.write_text(json.dumps(BLOCKS, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
after = MD.read_text(encoding='utf-8')
print('words: %d -> %d' % (len(before_md.split()), len(after.split())))
