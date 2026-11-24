"""record_r55.py - his round-55 versions in OWNER-EDITS.json and KEEP-AS-IS.json (run after apply_r55.py, from the repo
root):

  python3 articles/bad-trips/review/r55/record_r55.py

New: r55-answers (his B114 and B118 as his checks had them; B115 with why magnesium chloride, from his question; B117
from the post's text with his round-55 ways). Cuts he meant: C15 "meaningful" ("ai slop" he never wrote), C16 the aside
"described to me as essentially zero" (his first fix of TEACH-WIFE).
"""
import json
import pathlib

ART = pathlib.Path(__file__).resolve().parents[2]
ANS = 'articles/bad-trips/review/r55/ANSWERS-R55-20261124-1953.json'
WHEN = '2026-11-24 19:53 UTC'

o = ART / 'OWNER-EDITS.json'
d = json.loads(o.read_text(encoding='utf-8'))
new = {'id': 'r55-answers', 'status': 'applied',
       'what': ('his round-55 versions of the MDMA section\'s first paragraph (B114, TEACH-JAW) and of his second wife\'s '
                'paragraph (B118, TEACH-WIFE), each as his checks had them (6c2c336b; 38fe09f7, one double space made single); '
                'B115 with why magnesium chloride, from his TEACH-JAW question, Human High 109 in one window through the API '
                '(af5fd4f9); B117 from the post\'s text with the ways of his round-55 fixes, Human High 62 in one window '
                '(686d3bd1) (review/r55/apply_r55.py; humanize/h74-20261124/RESULTS.md)'),
       'joel': '%s: his round-55 export (%s), TEACH-JAW and TEACH-WIFE' % (WHEN, ANS),
       'applied_by': 'review/r55/apply_r55.py',
       'must_contain_exact': [
           'With MDMA, I treat jaw tension as the earliest warning that the body needs more magnesium.',
           "I don't have studies to back this up, but everyone I know who has taken enough magnesium chloride",
           'has avoided the MDMA toxicity symptoms they get otherwise',
           'At the hospital, they figured out what caused that:',
           'That experience is what leads me to treat serious MDMA toxicity as a broader electrolyte emergency, although magnesium is still the first and most useful supplement to give once the jaw tenses',
           'since potassium gets depleted after magnesium',
           'I use it mostly because it absorbs far better than magnesium oxide',
           "so you can see how it's helping, usually within a minute",
           "I don't mind a little less euphoria"],
       'must_not_contain': ['meaningful jaw tension', 'described to me as essentially zero', 'most useful early intervention']}
by = {e['id']: e for e in d['entries']}
if new['id'] in by:
    by[new['id']].update(new)
else:
    d['entries'].append(new)
o.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')

k = ART / 'KEEP-AS-IS.json'
kk = json.loads(k.read_text(encoding='utf-8'))
cuts = [
    {'id': 'C15', 'quote': 'meaningful jaw tension',
     'what': ('"meaningful" before jaw tension in the MDMA section\'s first paragraph, out in his version: a word of the post he '
              'never wrote, which my round-55 card wrongly called a held word of his'),
     'joel': 'idk where "meaningful" came from, i didn\' tput that in so it must be ai slop', 'when': WHEN,
     'where': 'round 55, TEACH-JAW (%s)' % ANS, 'basis': 'his answer'},
    {'id': 'C16', 'quote': 'described to me as essentially zero',
     'what': ('the aside in his second wife\'s paragraph, out in his version: his first fix of four, each checked ("first i '
              'took out the part inbetween em dashes, that helped a bit")'),
     'joel': 'first i took out the part inbetween em dashes, that helped a bit', 'when': WHEN,
     'where': 'round 55, TEACH-WIFE (%s)' % ANS, 'basis': 'his answer'},
]
for c in cuts:
    if not any(x['id'] == c['id'] for x in kk['cuts']):
        kk['cuts'].append(c)
k.write_text(json.dumps(kk, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('owner edits:', len(d['entries']), '| meant cuts:', len(kk['cuts']))
