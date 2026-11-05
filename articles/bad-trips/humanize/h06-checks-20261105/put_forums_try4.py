#!/usr/bin/env python3
"""The Active Seizure section's forums paragraph (N-FORUMS), try 4, into the guide (2026-11-05). His version (round 6,
CBD-TRIAL, its third paragraph) read AI Detected, 62% AI, and three tries of mine after the making-sense read and the
tell panel read 43%, 98% and 41% AI (RESULTS.md beside this script). Try 4 is the clearest: what's smoked and when, the
EEG woman as a study (his version put her among the forum posts), and an ending that says what the reports and the rats
share ("So it may come down to how much THC is in it"; his "the THC may be what makes it go either way" was followed by
rats in which THC only made things worse). Its last two sentences still read AI (Low), so it goes to him on round 7's
page (FORUMS-EDIT), and stays in the guide meanwhile (gate E291: the clear version stays).

  python3 articles/bad-trips/humanize/h06-checks-20261105/put_forums_try4.py
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parent.parent
BLOCKS = ART / 'GUIDE-SO-FAR-blocks.json'
b = json.loads(BLOCKS.read_text(encoding='utf-8'))
(u,) = [x for x in b if x['id'] == 'N-FORUMS']
assert u['md'].startswith('I also read on forums some swear it stops'), u['md']
u['md'] = (HERE / 'bt-r06-forums-4.txt').read_text(encoding='utf-8').strip()
BLOCKS.write_text(json.dumps(b, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
(ART / 'GUIDE-SO-FAR.md').write_text('\n\n'.join(x['md'] for x in b) + '\n', encoding='utf-8')
print('N-FORUMS: try 4 in;', len(re.findall(r'\S+', (ART / 'GUIDE-SO-FAR.md').read_text())), 'words')
