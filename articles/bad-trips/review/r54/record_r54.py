"""record_r54.py - his round-54 answer (ANSWERS-R54-20261124-1817.json, 2026-11-24 18:17 UTC), from the repo root:

  python3 articles/bad-trips/review/r54/record_r54.py

POTASSIUM-DRAIN (a): the second half of his QUIZ-3 note (the vomiting and diarrhea then draining potassium) stays out of
step 6, as turn 64 left it. No text changes: it goes on the keep-as-is list as a cut he meant (C14), so no later pass puts
it back, and OWNER-EDITS r53-answers records his answer.
"""
import json
import pathlib

ART = pathlib.Path(__file__).resolve().parents[2]
ANS = 'articles/bad-trips/review/r54/ANSWERS-R54-20261124-1817.json'
WHEN = '2026-11-24 18:17 UTC'

k = ART / 'KEEP-AS-IS.json'
d = json.loads(k.read_text(encoding='utf-8'))
cut = {'id': 'C14', 'quote': 'which then drain it again',
       'what': ('step 6\'s clause saying the vomiting and diarrhea then drain potassium again, out since turn 64: all three '
                'fresh reads took the draining as a reason to give more chips, not to stop them, and its sentence was the '
                'step\'s Medium window; the step already says potassium can be running high as well as low'),
       'joel': 'a', 'when': WHEN,
       'where': 'round 54, POTASSIUM-DRAIN (%s), option (a): "Leave it out"' % ANS, 'basis': 'his answer'}
if not any(c['id'] == 'C14' for c in d['cuts']):
    d['cuts'].append(cut)
k.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')

o = ART / 'OWNER-EDITS.json'
e = json.loads(o.read_text(encoding='utf-8'))
for x in e['entries']:
    if x['id'] == 'r53-answers':
        note = (' | %s: his POTASSIUM-DRAIN answer on round 54, (a): the draining clause stays out (keep-as-is C14)' % WHEN)
        if note not in x['what']:
            x['what'] += note
o.write_text(json.dumps(e, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('C14 on the keep-as-is list; r53-answers noted')
