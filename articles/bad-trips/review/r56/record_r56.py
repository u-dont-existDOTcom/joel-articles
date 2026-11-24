"""record_r56.py - his round-56 answers in OWNER-EDITS.json (run after apply_r56.py, from the repo root):

  python3 articles/bad-trips/review/r56/record_r56.py

New: r56-answers (B115's last sentence as his claim with the source out; B118's last phrase, his choice (a)). The two
lines of r55-answers that these answers replace move out of its must_contain_exact, each with a note, and the removed
source's address goes in must_not_link so no later rewrite links it again.
"""
import json
import pathlib

ART = pathlib.Path(__file__).resolve().parents[2]
ANS = 'articles/bad-trips/review/r56/ANSWERS-R56-20261124-2126.json'
WHEN = '2026-11-24 21:26 UTC'
OUT = {'since potassium gets depleted after magnesium':
           'replaced by his round-56 choice (a), WIFE-LAST: "since potassium gets depleted once magnesium runs low"',
       'I use it mostly because it absorbs far better than magnesium oxide':
           'replaced by his round-56 answer, CHLORIDE-CLAIM: the source out, the claim as what he knows works best'}

o = ART / 'OWNER-EDITS.json'
d = json.loads(o.read_text(encoding='utf-8'))
by = {e['id']: e for e in d['entries']}
r55 = by['r55-answers']
r55['must_contain_exact'] = [s for s in r55['must_contain_exact'] if s not in OUT]
r55['replaced_by_r56'] = [{'was': k, 'why': v, 'when': WHEN} for k, v in OUT.items()]
new = {'id': 'r56-answers', 'status': 'applied',
       'what': ('his round-56 answers: the absorption study\'s link out of the amounts paragraph (B115), with his claim said as '
                'what he knows works best, in the words of his round-55 comment, Human High 118 in one window through the API '
                '(f330e220); and his second wife\'s paragraph (B118) ending "since potassium gets depleted once magnesium runs '
                'low", his choice (a), Human High 77 in one window (e74a7e6b) (review/r56/apply_r56.py; '
                'humanize/h75-20261124/RESULTS.md)'),
       'joel': ('%s: his round-56 export (%s). CHLORIDE-CLAIM: "remove the source then if there\'s no source, but i definitely '
                'can\'t recommend using anything other than what i know works best"; WIFE-LAST: "a"') % (WHEN, ANS),
       'applied_by': 'review/r56/apply_r56.py',
       'must_contain_exact': [
           "I use it mostly because it's what I know works best: it absorbs faster and better than any other form, so you can see how it's helping, usually within a minute.",
           'since potassium gets depleted once magnesium runs low'],
       'must_not_contain': ['far better than magnesium oxide', 'gets depleted after magnesium'],
       'must_not_link': ['https://pubmed.ncbi.nlm.nih.gov/11794633']}
if new['id'] in by:
    by[new['id']].update(new)
else:
    d['entries'].append(new)
o.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('owner edits:', len(d['entries']))
