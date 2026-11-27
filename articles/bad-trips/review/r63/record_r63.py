"""record_r63.py - his round-63 answers in OWNER-EDITS.json (run after humanize/h82-20261127/apply_h82.py and its fix, from
the repo root):

  python3 articles/bad-trips/review/r63/record_r63.py

TEACH-B173: his version, whole, with "(the dried juice)" from his comment where the extract paste is first named, and
"Eating" before "a whole leaf" (mine, after the section's second check). His version carries his round-62 amounts, so
r62-nibble-size is in. SKIN-AMOUNT: "sensitive skin" back in B174's skin sentence, and the amounts as the same as by
mouth, or a few drops of fresh juice. His comment's "ppl can find it in some places growing (railroad vine is one name
used)" is in B171 (my reading: a fact he gave that tells the reader where to get it); his "i don't necessarily want to say
i sell it in this guide since then it looks like a sales pitch" is held as words the guide must not have. No numbers new
to the guide's keys (his amounts are R62's), so the fidelity keys stay R62.
"""
import json
import pathlib

ART = pathlib.Path(__file__).resolve().parents[2]
ANS = 'articles/bad-trips/review/r63/ANSWERS-R63-20261127-2003.json'
WHEN = '2026-11-27 20:03 UTC'
RES = 'humanize/h82-20261127/RESULTS.md'

o = ART / 'OWNER-EDITS.json'
d = json.loads(o.read_text(encoding='utf-8'))
by = {e['id']: e for e in d['entries']}
new = [
    {'id': 'r63-teach-b173', 'status': 'applied',
     'what': ('his round-63 TEACH-B173 version of B173, whole (his check, Human High 84 in one window, 09e42ca2), with '
              '"(the dried juice)" from his comment where the extract paste is first named (Human High 87, bf3ae1f3) and '
              '"Eating" before "a whole leaf" after the section\'s second check (Human High 88, 9bae6cd1; %s)' % RES),
     'joel': '%s: his round-63 export (%s), card TEACH-B173' % (WHEN, ANS),
     'applied_by': 'humanize/h82-20261127/apply_h82.py (and its "fix")',
     'must_contain_exact': ['A tiny nibble can sometimes smooth psychedelic nausea and even smooth the trip without ending it.',
                            "For nausea I'd try 200mg of leaf at a time, or 10mg of the extract paste (the dried juice).",
                            'But it takes only a little more than a nibble to end the trip, so I use it for nausea only when '
                            'the person is okay with their trip possibly ending.'],
     'must_not_contain': ['even improve the trip']},
    {'id': 'r63-skin-amount', 'status': 'applied',
     'what': ('his round-63 SKIN-AMOUNT answer in B174: the juice works through sensitive skin (my sentence had said "the '
              'skin"), and on the skin about the same amounts as by mouth, or maybe a few drops of fresh juice; B174 now '
              'follows B173 so its amounts point back (Human High 143 with B171, 3da1f8d2; %s)' % RES),
     'joel': '%s: his round-63 export (%s), card SKIN-AMOUNT' % (WHEN, ANS),
     'applied_by': 'humanize/h82-20261127/apply_h82.py',
     'must_contain_exact': ['Its juice works through sensitive skin almost as well as eating the leaf does',
                            "I'd use about the same amounts as by mouth, or maybe a few drops of fresh juice"],
     'must_not_contain': ['works through the skin almost']},
    {'id': 'r63-where-to-find', 'status': 'applied',
     'what': ('from his comment on TEACH-B173, in B171: "People still find it growing in some places, under names like '
              'railroad vine." (my reading of his "ppl can find it in some places growing (railroad vine is one name '
              'used)"; Human High 69 by itself, 0e0bd36d); and his wish that the guide not say he sells the extract paste'),
     'joel': ('%s: his round-63 export (%s), card TEACH-B173\'s comment: "i don\'t necessarily want to say i sell it in this '
              'guide since then it looks like a sales pitch, altho nobody is selling it other than me but ppl can find it in '
              'some places growing (railroad vine is one name used)"' % (WHEN, ANS)),
     'applied_by': 'humanize/h82-20261127/apply_h82.py',
     'must_contain_exact': ['railroad vine'],
     'must_not_contain': ['I sell', 'sold by me']},
]
for n in new:
    if n['id'] in by:
        by[n['id']].clear()
        by[n['id']].update(n)
    else:
        d['entries'].append(n)
e = by['r62-nibble-size']
e.update({'status': 'applied', 'applied_by': 'humanize/h82-20261127/apply_h82.py, in his round-63 TEACH-B173 version',
          'must_contain_exact': ["200mg of leaf at a time, or 10mg of the extract paste"]})
e.pop('waits_for', None)
e['what'] = e['what'] + ' In since turn 74: his own version of B173 carries them (r63-teach-b173); his "more" is not in it.'
lj = by['r62-leaf-juice']
lj['must_contain_exact'] = ['can relax me if the juice', 'almost as well as eating the leaf does',
                            'you can put it under the armpits, for example']
if 'turn 74' not in lj['what']:
    lj['what'] += (' Since turn 74 (r63-skin-amount): "sensitive skin", "put it" for "put the juice", since the amounts on '
                   'the skin are leaf or paste as well as juice.')
o.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('owner edits:', len(d['entries']))
