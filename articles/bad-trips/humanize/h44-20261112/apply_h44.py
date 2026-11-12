#!/usr/bin/env python3
"""apply_h44.py - turn 35's change to the guide from this folder: Risk of Harm's number paragraph said once.

His round-34 comment on TEACH-HARM, "make sure this is only said once": the 911 line repeated the reasons his paragraph now
gives ("violence underway, or a situation you cannot safely contain") and the paragraph's own first sentence ("immediate
danger", "medical emergency"). The fix of mine that reworded the whole paragraph read AI, 100% (45f31361), no better than
before, so only the repeats go: 911 joins the first sentence, with the two reasons only it had (a weapon, a crime in
progress); W003's and W004's keys stay.

  python3 apply_h44.py
"""
import json, pathlib
HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parents[1]
BJ = ART / 'GUIDE-SO-FAR-blocks.json'
MD = ART / 'GUIDE-SO-FAR.md'
B = json.loads(BJ.read_text(encoding='utf-8'))
assert '\n\n'.join(b['md'] for b in B) + '\n' == MD.read_text(encoding='utf-8')
OLD = ("Use local emergency services for immediate danger or a medical emergency. In the United States, 988 can provide "
       "mental-health crisis guidance, de-escalation, and connection to local resources when no immediate physical emergency "
       "exists. Call 911 for immediate danger, a crime in progress, medical emergency, weapon, violence underway, or a "
       "situation you cannot safely contain. Outside the United States")
NEW = ("Use local emergency services (911 in the United States) for immediate danger, a medical emergency, a weapon, or a "
       "crime in progress. In the United States, 988 can provide mental-health crisis guidance, de-escalation, and "
       "connection to local resources when no immediate physical emergency exists. Outside the United States")
hits = [b for b in B if OLD in b['md']]
assert len(hits) == 1 and hits[0]['id'] == 'B278'
hits[0]['md'] = hits[0]['md'].replace(OLD, NEW)
MD.write_text('\n\n'.join(b['md'] for b in B) + '\n', encoding='utf-8')
BJ.write_text(json.dumps(B, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print(hits[0]['id'], hits[0]['md'])
