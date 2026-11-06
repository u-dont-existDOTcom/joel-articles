#!/usr/bin/env python3
"""apply_t16.py - Joel's decision of 2026-11-06 19:43 UTC (JOEL-MESSAGE-20261106-1943.md): "make the cuts regardless of
pangram if it makes the guide read better, that was what we were supposed to do already prior".

The room stretch of Psychological First Aid says again what the guide says in its own place further on, more fully:
  - the hand on the shoulder: Touch, Consent, and Compassion ("Ask first: "Would touch help, or would you rather have
    space?""), the Do list ("Closer or farther away?") and the Don't list ("Don't force eye contact, touch, music ...");
  - speaking slowly and using fewer words: Get One Human Anchor (its script, "speak slowly"), and For the Person Helping
    ("talking through rather than down");
  - the music paragraph: the Grounding Menu's Music ("Silence is a real option", "Keep the stop or change control
    immediate"), the Do list ("Music or quiet?") and the Don't list;
  - water: the Do list ("Water?") and the body section ("The body may need quiet, water, cooling, warmth ...").
So B240 keeps its first sentence (the reason and the two acts that belong to the first five minutes), B241 goes, and the
one thing only the stretch said, that water goes in small sips, moves to the Do list's "Water?" (B282), so it is said
once.

  python3 apply_t16.py      write the guide (../../GUIDE-SO-FAR.md and its blocks) and print what changed
"""
import hashlib
import json
import pathlib
import re

ART = pathlib.Path(__file__).resolve().parent.parent.parent
BJ = ART / 'GUIDE-SO-FAR-blocks.json'
MD = ART / 'GUIDE-SO-FAR.md'
BLOCKS = json.loads(BJ.read_text(encoding='utf-8'))
UNIT = {b['id']: b for b in BLOCKS}
before_md = MD.read_text(encoding='utf-8')
assert '\n\n'.join(b['md'] for b in BLOCKS) + '\n' == before_md, 'the blocks and the guide disagree'

B240 = ("They're feeling overwhelmed, so dim the lights, and clear out the extra people around them. If they're thirsty, "
        "offer water, and suggest they sip it rather than chug. Ask if they'd like a hand on the shoulder. Speak slowly "
        "and use fewer words.")
B241 = ("Ask \"Would you like music or is quiet best?\" If a track starts pulling the experience somewhere unwanted, go "
        "ahead and change it.")
WATER = '"Closer or farther away?" "Water?"\n'
assert UNIT['B240']['md'] == B240, UNIT['B240']['md']
assert UNIT['B241']['md'] == B241, UNIT['B241']['md']
assert UNIT['B282']['md'].count(WATER) == 1

UNIT['B240']['md'] = "They're feeling overwhelmed, so dim the lights, and clear out the extra people around them."
UNIT['B282']['md'] = UNIT['B282']['md'].replace(WATER, '"Closer or farther away?" "Water?" (in small sips)\n')
BLOCKS = [b for b in BLOCKS if b['id'] != 'B241']

text = '\n\n'.join(b['md'] for b in BLOCKS) + '\n'
MD.write_text(text, encoding='utf-8')
BJ.write_text(json.dumps(BLOCKS, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
w0, w1 = len(re.findall(r'\S+', before_md)), len(re.findall(r'\S+', text))
print('B240: its first sentence kept; water, the hand on the shoulder and speaking slowly cut (said in their own places)')
print('B241: the music paragraph out (the Grounding Menu\'s Music, the Do and Don\'t lists)')
print('B282: "Water?" (in small sips), the one thing only the stretch said')
print('%d words -> %d (%+d); GUIDE-SO-FAR.md sha256 %s' % (w0, w1, w1 - w0, hashlib.sha256(text.encode()).hexdigest()))
