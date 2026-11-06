#!/usr/bin/env python3
"""apply_t17.py - the room paragraph of Psychological First Aid (B238) cut, by Joel's decision of 2026-11-06 19:43 UTC
(../t16-answers/JOEL-MESSAGE-20261106-1943.md: "make the cuts regardless of pangram if it makes the guide read better,
that was what we were supposed to do already prior"; gate E378).

B238 says again what the guide says in its own places:
  - that the room is often the problem: Why Bad Trips Tend to Happen ("an unsafe setting", "admit that the room is bad");
  - the light and the music: the fixes line after it (B240, "dim the lights"), the Do list ("Would less light help?"
    "Music or quiet?"), the Don't list ("Don't force ... music") and the Grounding Menu's Music;
  - five people talking at once: B240 ("clear out the extra people around them") and Get One Human Anchor ("too many
    people crowd in", "A committee of frantic people");
  - touch they hate: the Don't list ("Don't force eye contact, touch ...") and Touch, Consent, and Compassion;
  - too hot or too cold: the Do list ("warm") and the body paragraph ("cooling, warmth").
Two things only it said move to the Do list (B282), so each is said once: the bathroom (a question beside "Water?") and
someone they're wary of (with keeping the room safe).

Pangram, his account (../../humanize/h11-20261106/RESULTS.md): the first half of the section without B238 reads Human
Written (3bd48be6); with B238, in eleven versions, and with any of its sentences after his dangers paragraph, it reads AI,
his paragraph included.

  python3 apply_t17.py      write the guide (../../GUIDE-SO-FAR.md and its blocks) and print what changed
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

B238 = ("A lot of what looks like a deep psychedelic crisis is a scared person in a room that's getting on their nerves, so "
        "look around the room next. Maybe the light's too bright or the music's horrible. Are five concerned people talking "
        "at once? Somebody might be touching them and they hate it, or they're stuck beside someone they're wary of. And "
        "check whether they're too hot or too cold, or desperate for the bathroom.")
assert UNIT['B238']['md'] == B238, UNIT['B238']['md']
ASK = '"Closer or farther away?" "Water?" (in small sips)\n'
ROOM = '- Keep the room quiet, private, warm, and physically safe.\n'
md = UNIT['B282']['md']
assert md.count(ASK) == 1 and md.count(ROOM) == 1
UNIT['B282']['md'] = (md.replace(ASK, '"Closer or farther away?" "Water?" (in small sips) "Need the bathroom?"\n')
                        .replace(ROOM, "- Keep the room quiet, private, warm, and physically safe, and move anyone they're "
                                       "wary of somewhere else.\n"))
BLOCKS = [b for b in BLOCKS if b['id'] != 'B238']

text = '\n\n'.join(b['md'] for b in BLOCKS) + '\n'
MD.write_text(text, encoding='utf-8')
BJ.write_text(json.dumps(BLOCKS, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
w0, w1 = len(re.findall(r'\S+', before_md)), len(re.findall(r'\S+', text))
print('B238 (the room paragraph) cut; B282 (the Do list) asks "Need the bathroom?" and moves anyone they\'re wary of')
print('%d words -> %d (%+d); GUIDE-SO-FAR.md sha256 %s' % (w0, w1, w1 - w0, hashlib.sha256(text.encode()).hexdigest()))
