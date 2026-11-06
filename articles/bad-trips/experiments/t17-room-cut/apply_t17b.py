#!/usr/bin/env python3
"""apply_t17b.py - Psychological First Aid's last paragraph (B246) cut, by the same decision of Joel's as apply_t17.py
(2026-11-06 19:43 UTC: "make the cuts regardless of pangram if it makes the guide read better"; gate E378).

B246 points to the next two sections and says again what later sections say more fully:
  - "one safe thing to try with their body and one calm person to stay with them, which the next two sections are about":
    the next two sections, Stillness or Movement? ("Try one for two minutes") and Get One Human Anchor ("Use one calm
    human anchor as the lead"), whose headings the reader meets next;
  - protecting sleep, especially when euphoric or grandiose, and leaving the meaning until after sleep: No Rash Actions
    ("Write it down. Protect sleep. Revisit it sober with one grounded person."), When the Trip Feels Amazing ("Have I
    slept? Sleep comes before mission."; "If it is true, it survives sleep.") and Give the Session a Beginning and an End
    ("Sleep and food come before turning the experience into a new life plan").
Pangram, his account: B246 after the section's first half (Human alone, 3bd48be6) turns all of it AI, one window
(0502aeef).

  python3 apply_t17b.py      write the guide (../../GUIDE-SO-FAR.md and its blocks) and print what changed
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
B246 = ("Then help them pick one safe thing to try with their body and one calm person to stay with them, which the next "
        "two sections are about. Protect their sleep too, especially if they're euphoric or grandiose, and leave what it "
        "all meant until they've slept.")
assert UNIT['B246']['md'] == B246, UNIT['B246']['md']
BLOCKS = [b for b in BLOCKS if b['id'] != 'B246']
text = '\n\n'.join(b['md'] for b in BLOCKS) + '\n'
MD.write_text(text, encoding='utf-8')
BJ.write_text(json.dumps(BLOCKS, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
w0, w1 = len(re.findall(r'\S+', before_md)), len(re.findall(r'\S+', text))
print('B246 (the pointer to the next sections, with sleep and meaning) cut')
print('%d words -> %d (%+d); GUIDE-SO-FAR.md sha256 %s' % (w0, w1, w1 - w0, hashlib.sha256(text.encode()).hexdigest()))
