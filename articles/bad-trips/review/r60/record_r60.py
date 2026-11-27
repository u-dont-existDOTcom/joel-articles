"""record_r60.py - his round-60 answers in OWNER-EDITS.json and KEEP-AS-IS.json (run after
humanize/h79-20261126/apply_h79.py, from the repo root):

  python3 articles/bad-trips/review/r60/record_r60.py

GUT-SIGNS-IN "a": the four paragraphs of round 59 stay as they are, and what I left out of his GUT-SIGNS answers stays out;
"if the gut is fine" becomes a cut he meant (C20). ZEO-FACTS 2.1: B154 with his answer (humanize/h79-20261126, Human High
94, cd5a0e49). 2.2 to 2.6 went unanswered; what his ZeoCharge post says on them is round 61's FROM-POST.
"""
import json
import pathlib

ART = pathlib.Path(__file__).resolve().parents[2]
ANS = 'articles/bad-trips/review/r60/ANSWERS-R60-20261126-2229.json'
WHEN = '2026-11-26 22:29 UTC'

o = ART / 'OWNER-EDITS.json'
d = json.loads(o.read_text(encoding='utf-8'))
new = {'id': 'r60-answers', 'status': 'applied',
       'what': ('his round-60 answers: GUT-SIGNS-IN "a" (the round-59 paragraphs stay as they are; GPT\'s symptom list and "if '
                'the gut is fine obviously it\'s not related to the gut" stay out; the call-medics pointer stays); ZEO-FACTS '
                '2.1 in B154, his words for which ferments work (Human High 94 in one window, cd5a0e49; '
                'humanize/h79-20261126/apply_h79.py; review/r60/RESULTS-R60.md)'),
       'joel': '%s: his round-60 export (%s), sent 2026-11-26 23:31 UTC' % (WHEN, ANS),
       'applied_by': 'humanize/h79-20261126/apply_h79.py',
       'must_contain_exact': [
           'The ZHoly3O ferment contains more than just fermented beet juice, but you can ferment your own beet juice or even use other ferments.',
           'I found fermented beet made with apple vinegar and salt was best so far, though kimchi and kombucha also helped.',
           "Most yogurts weren't fermented enough to work, and apple vinegar by itself only helped a little.",
           'Losing control of the body like that is on the list to call medics for'],
       'must_not_contain': ['if the gut is fine', 'Many ferments help to different degrees']}
by = {e['id']: e for e in d['entries']}
if new['id'] in by:
    by[new['id']].update(new)
else:
    d['entries'].append(new)
o.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')

k = ART / 'KEEP-AS-IS.json'
kk = json.loads(k.read_text(encoding='utf-8'))
cut = {'id': 'C20', 'quote': 'if the gut is fine',
       'what': ('his round-59 line "if the gut is fine obviously it\'s not related to the gut", left out of the gut-driven paragraphs '
                '(two fresh readers: it tells the reader nothing, and a fine gut does not rule out the brain); his "a" on round 60 '
                'kept it out'),
       'joel': 'a', 'when': WHEN, 'where': 'round 60, GUT-SIGNS-IN (%s)' % ANS, 'basis': 'his answer'}
if not any(x['id'] == cut['id'] for x in kk['cuts']):
    kk['cuts'].append(cut)
k.write_text(json.dumps(kk, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('owner edits:', len(d['entries']), '| meant cuts:', len(kk['cuts']))
