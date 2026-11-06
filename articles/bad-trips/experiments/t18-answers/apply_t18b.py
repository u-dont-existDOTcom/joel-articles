#!/usr/bin/env python3
"""apply_t18b.py - Psychological First Aid's intro line (B234) cut, by Joel's decision of 2026-11-06 19:43 UTC
(../t16-answers/JOEL-MESSAGE-20261106-1943.md: "make the cuts regardless of pangram if it makes the guide read better";
gate E378).

B234 said "The triage app gives you the order to do things in, and this section is about doing them in a way that takes
pressure off the person." Both of its points are said where a reader needs them: the triage app is the guide's first line
("Quick Triage Web-App Version HERE") and is named again in Alone at 3 a.m., Give the Session a Beginning and an End and
the resources, and the picture under the heading is its screen; taking pressure off the person is the subject of For the
Person Helping: Calm Anchor, Not Guru. The section now opens on its first act, under its heading and picture.

Pangram, his account (../../humanize/h12-20261106/RESULTS.md): in every check with more of the section after it, the
window holding the heading, this line and the dangers paragraph's start read AI; without the line, the section to the
reminder reads Human Written (a49943b6).

  python3 apply_t18b.py      write the guide (../../GUIDE-SO-FAR.md and its blocks) and print what changed
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
B234 = ("The [triage app](https://ibogaqueen.com/1625-2/) gives you the order to do things in, and this section is about "
        "doing them in a way that takes pressure off the person.")
assert UNIT['B234']['md'] == B234, UNIT['B234']['md']
assert before_md.startswith('[**Quick Triage Web-App Version HERE**](https://ibogaqueen.com/1625-2/)')
BLOCKS = [b for b in BLOCKS if b['id'] != 'B234']
text = '\n\n'.join(b['md'] for b in BLOCKS) + '\n'
MD.write_text(text, encoding='utf-8')
BJ.write_text(json.dumps(BLOCKS, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
w0, w1 = len(re.findall(r'\S+', before_md)), len(re.findall(r'\S+', text))
print('B234 (the intro line) cut')
print('%d words -> %d (%+d); GUIDE-SO-FAR.md sha256 %s' % (w0, w1, w1 - w0, hashlib.sha256(text.encode()).hexdigest()))
