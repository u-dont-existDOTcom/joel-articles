"""record_r58.py - his round-58 answer in OWNER-EDITS.json, KEEP-AS-IS.json and the fidelity keys (run after apply_r58.py,
from the repo root):

  python3 articles/bad-trips/review/r58/record_r58.py

New: r58-answers (his charcoal and poison control paragraphs, whole). A cut he meant: C18, poison control as who to ask
about charcoal ("i do not recommend calling poison control to see about giving charcoal"). The fidelity keys from now on
are humanize/h01/FIDELITY-KEYS-R58.json: his version's key losses are his changes.
"""
import json
import pathlib

ART = pathlib.Path(__file__).resolve().parents[2]
ANS = 'articles/bad-trips/review/r58/ANSWERS-R58-20261125-1742.json'
WHEN = '2026-11-25 17:42 UTC'

o = ART / 'OWNER-EDITS.json'
d = json.loads(o.read_text(encoding='utf-8'))
new = {'id': 'r58-answers', 'status': 'applied',
       'what': ('his round-58 version of the charcoal and poison control paragraphs of Swallowed Too Much? (B127, B128, '
                'CHARCOAL-HOUR), whole, as his comment has it, with the guide\'s link back on "Activated charcoal" and the '
                'review\'s on "The usual advice"; the API reads the two Human High 166 in one window (7b62fe4a) '
                '(review/r58/apply_r58.py; humanize/h77-20261125/RESULTS.md)'),
       'joel': '%s: his round-58 export (%s), CHARCOAL-HOUR, sent 2026-11-25 17:43 UTC' % (WHEN, ANS),
       'applied_by': 'review/r58/apply_r58.py',
       'must_contain_exact': [
           'Activated charcoal is safe and can help with many drug overdoses (and toxins in the gut).',
           "The usual advice says it's only useful within an hour of the drug overdose, but that's not true for many plant medicines which can take hours to digest.",
           "Obviously don't give anything by mouth to someone who can't swallow, as they could aspirate it into their lungs and die.",
           "And don't give any fine powders to anyone directly, mix in water first to prevent choking.",
           "If you're unsure about the interactions between the drugs taken, it could be helpful to check with AI & Poison Control.",
           "They might have important info, especially if the drugs are well-known, even if they often can't give actionable advice for liability reasons.",
           'They can also help you with standard first aid instructions.'],
       'must_not_contain': ['value of charcoal', 'mandatory ritual', 'decision support, not first aid',
                            'within the last hour or so']}
by = {e['id']: e for e in d['entries']}
if new['id'] in by:
    by[new['id']].update(new)
else:
    d['entries'].append(new)
o.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')

k = ART / 'KEEP-AS-IS.json'
kk = json.loads(k.read_text(encoding='utf-8'))
cuts = [
    {'id': 'C18', 'quote': 'value of charcoal',
     'what': ('poison control as who to ask whether to give charcoal (the post: "Poison control may be useful when the '
              'substance, combination, delayed risk, or value of charcoal is unclear"), out in his version: poison control '
              'is for the interactions between the drugs taken and for standard first aid instructions'),
     'joel': ('i do not recommend calling poison control to see about giving charcoal, why? because i know someone who did, '
              'and poison control said they aren\'t allowed to tell them to take charcoal, so it left them very confused'),
     'when': WHEN, 'where': 'round 58, CHARCOAL-HOUR (%s)' % ANS, 'basis': 'his answer'},
]
for c in cuts:
    if not any(x['id'] == c['id'] for x in kk['cuts']):
        kk['cuts'].append(c)
k.write_text(json.dumps(kk, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')

f57 = ART / 'humanize' / 'h01' / 'FIDELITY-KEYS-R57.json'
f58 = ART / 'humanize' / 'h01' / 'FIDELITY-KEYS-R58.json'
fk = json.loads(f57.read_text(encoding='utf-8'))
by_ = ('%s, card CHARCOAL-HOUR (%s): his version of both paragraphs, whole: who must not be given anything by mouth is '
       '"someone who can\'t swallow" ("they could aspirate it into their lungs and die") in place of the four cases; poison '
       'control is for the interactions between the drugs and for first aid instructions, not for whether to give charcoal; '
       'his stance on calling them is said as what they can and can\'t give') % (ANS, WHEN)
if not any(x.get('by') == by_ for x in fk['owner_changes']):
    fk['owner_changes'].append({'by': by_, 'keys_lost': {'W032': [['aspiration'], ['sedated']],
                                                         'W033': [['delayed'], ['value']],
                                                         'W034': [['usefulness'], ['mandatory']]}})
fk['about'] = fk.get('about', '') + ' R58 (2026-11-25): his round-58 charcoal and poison control paragraphs\' key losses added as his changes.'
f58.write_text(json.dumps(fk, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('owner edits:', len(d['entries']), '| meant cuts:', len(kk['cuts']), '| fidelity owner changes:', len(fk['owner_changes']))
