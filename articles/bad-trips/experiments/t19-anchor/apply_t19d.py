#!/usr/bin/env python3
"""apply_t19d.py - two repeats cut from Who to Contact, and When (B262) and Alone at 3 a.m. (B273), by Joel's decision of
2026-11-06 19:43 UTC (../t16-answers/JOEL-MESSAGE-20261106-1943.md: "make the cuts regardless of pangram if it makes the
guide read better"; gate E378), and his first ask, the call-for-help lines in one place ("too much safety language spread
everywhere rather than in one spot", ../t01-answers/JOEL-MESSAGE-20261103-1545.md).

- B262's "Psychedelic peer support does not replace emergency, medical, psychiatric, or suicide-crisis care." is what the
  guide's call-for-help part says, under its heading "When Peer Support Isn't Enough" (B276, B278).
- B273's "When nobody is available, use Fireside during its coverage hours, TripSit for drug-related peer support, or Find
  A Helpline and a local crisis service for fear, despair, self-harm, or inability to stay safe." names again the services
  of Who to Contact, and When, the section just above, and the call-for-help part's cases. Alone at 3 a.m. keeps its own
  steps: the phone only for a calm person or a support service, and the human-anchor script.

No fidelity key is in either (fidelity_keys.py check).

  python3 apply_t19d.py      write the guide (../../GUIDE-SO-FAR.md and its blocks) and print what changed
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
CUT1 = " Psychedelic peer support does not replace emergency, medical, psychiatric, or suicide-crisis care."
assert UNIT['B262']['md'].endswith(CUT1), UNIT['B262']['md']
UNIT['B262']['md'] = UNIT['B262']['md'][:-len(CUT1)]
CUT2 = (" When nobody is available, use Fireside during its coverage hours, TripSit for drug-related peer support, or Find A "
        "Helpline and a local crisis service for fear, despair, self-harm, or inability to stay safe.")
assert UNIT['B273']['md'] == 'Send the human-anchor script.' + CUT2, UNIT['B273']['md']
UNIT['B273']['md'] = 'Send the human-anchor script.'
text = '\n\n'.join(b['md'] for b in BLOCKS) + '\n'
MD.write_text(text, encoding='utf-8')
BJ.write_text(json.dumps(BLOCKS, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
w0, w1 = len(re.findall(r'\S+', before_md)), len(re.findall(r'\S+', text))
print('B262: the peer-support line cut; B273: the services named again cut')
print('%d words -> %d (%+d); GUIDE-SO-FAR.md sha256 %s' % (w0, w1, w1 - w0, hashlib.sha256(text.encode()).hexdigest()))
