"""record_r59.py - his round-59 answers in OWNER-EDITS.json and KEEP-AS-IS.json (run after apply_r59.py and
humanize/h78-20261126/apply_h78.py, from the repo root):

  python3 articles/bad-trips/review/r59/record_r59.py

New: r59-answers (POISON-LINE "b"; GUT-SIGNS 2.1 and 2.2 as paragraphs from his words). r58-answers no longer requires
the clause his "b" replaced. A cut he meant: C19, "for liability reasons". The fidelity keys stay R58: nothing keyed was
lost (fidelity_keys.py check passes on the guide as it now stands).
"""
import json
import pathlib

ART = pathlib.Path(__file__).resolve().parents[2]
ANS = 'articles/bad-trips/review/r59/ANSWERS-R59-20261126-1555.json'
WHEN = '2026-11-26 15:55 UTC'
OLD = "They might have important info, especially if the drugs are well-known, even if they often can't give actionable advice for liability reasons."

o = ART / 'OWNER-EDITS.json'
d = json.loads(o.read_text(encoding='utf-8'))
by = {e['id']: e for e in d['entries']}
r58 = by['r58-answers']
if OLD in r58['must_contain_exact']:
    r58['must_contain_exact'] = [x for x in r58['must_contain_exact'] if x != OLD] + [
        'They might have important info, especially if the drugs are well-known.']
    r58['what'] += ('. Round 59 (his "b" on POISON-LINE, %s): the clause "even if they often can\'t give actionable advice '
                    'for liability reasons" is replaced by two sentences on what happened to the person he knows; his other '
                    'sentences stay word for word' % WHEN)
new = {'id': 'r59-answers', 'status': 'applied',
       'what': ('his round-59 answers: POISON-LINE "b" (B128: his three sentences and two on what happened to the person he '
                'knows, with Poison Control\'s page linked; Human High 74, 9afb6a77); GUT-SIGNS 2.1 and 2.2 as paragraphs '
                'made from his words (B141, R59-GUT-DO, B151, R59-GUT-COMMON; Human High 105, 65 and 151 in one window each: '
                '7a9e0fdc, af2c0ec5, a53a2ce3) (review/r59/apply_r59.py; humanize/h78-20261126/apply_h78.py; '
                'review/r59/RESULTS-R59.md). What I left out of his GUT-SIGNS answers is his to rule on: round 60, GUT-SIGNS-IN'),
       'joel': '%s: his round-59 export (%s), POISON-LINE and GUT-SIGNS, sent 2026-11-26 15:56 UTC' % (WHEN, ANS),
       'applied_by': 'review/r59/apply_r59.py; humanize/h78-20261126/apply_h78.py',
       'must_contain_exact': [
           "But I wouldn't ask Poison Control about charcoal.",
           "Someone I know did, and came away very confused after being told they aren't allowed to tell anyone to take it.",
           'not being able to sit up, stand, walk or talk',
           "You don't need to try to tell which is from what.",
           'A gut-driven mental hell is often mistaken as shadow work.',
           "people generally don't feel good mentally during the nausea and gut pain parts of the come-up",
           "usually there's a lot of relief once everything starts coming out in the toilet",
           'dosing lower on the psychedelic helps too'],
       'must_not_contain': ['for liability reasons']}
if new['id'] in by:
    by[new['id']].update(new)
else:
    d['entries'].append(new)
o.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')

k = ART / 'KEEP-AS-IS.json'
kk = json.loads(k.read_text(encoding='utf-8'))
cut = {'id': 'C19', 'quote': 'for liability reasons',
       'what': ('the clause "even if they often can\'t give actionable advice for liability reasons" of his round-58 poison '
                'control paragraph, out by his choice of version (b): what happened to the person he knows is said instead'),
       'joel': 'b', 'when': WHEN, 'where': 'round 59, POISON-LINE (%s)' % ANS, 'basis': 'his answer'}
if not any(x['id'] == cut['id'] for x in kk['cuts']):
    kk['cuts'].append(cut)
k.write_text(json.dumps(kk, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('owner edits:', len(d['entries']), '| meant cuts:', len(kk['cuts']))
