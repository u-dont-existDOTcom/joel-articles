"""record_r62.py - his round-62 answers in the fidelity keys and OWNER-EDITS.json, from the repo root:

  python3 articles/bad-trips/review/r62/record_r62.py keys    FIDELITY-KEYS-R62.json (before the steps' fidelity check)
  python3 articles/bad-trips/review/r62/record_r62.py edits   OWNER-EDITS.json's entries (after humanize/h81-20261127/apply_h81.py)

LEAF-JUICE: "touching the juice is relaxing, especially on sensitive skin, it absorbs almost as well as eating it. can put
it under armpits for example to absorb well" goes into B174, the handling paragraph. NIBBLE-SIZE: "i'd try 10mg at a time
for nausea of the extract paste, or 200mg leaf at a time (more if they don't mind reducing trip intensity)" goes into B173,
the amounts paragraph; its two amounts are numbers the guide didn't have, so FIDELITY-KEYS-R62.json is R61 with an
owner_changes entry naming them (numbers_new), and the card that gave them.
"""
import json
import pathlib
import sys

ART = pathlib.Path(__file__).resolve().parents[2]
ANS = 'articles/bad-trips/review/r62/ANSWERS-R62-20261127-1716.json'
WHEN = '2026-11-27 17:16 UTC'


def keys():
    k61 = json.loads((ART / 'humanize' / 'h01' / 'FIDELITY-KEYS-R61.json').read_text(encoding='utf-8'))
    k62 = dict(k61)
    k62['about'] = k61['about'] + (' | R62 (2026-11-27 17:16 UTC, turn 73): R61 with his round-62 NIBBLE-SIZE amounts, '
                                   'numbers the guide did not have before (owner_changes, numbers_new).')
    k62['owner_changes'] = list(k61.get('owner_changes', [])) + [{
        'by': ('%s, card NIBBLE-SIZE (%s): his amounts for nausea, "i\'d try 10mg at a time for nausea of the extract '
               'paste, or 200mg leaf at a time (more if they don\'t mind reducing trip intensity)", in B173 as "For nausea '
               'I\'d try 200mg of leaf at a time, or 10mg of the extract paste."' % (ANS, WHEN)),
        'numbers_new': ['10mg', '200mg']}]
    out = ART / 'humanize' / 'h01' / 'FIDELITY-KEYS-R62.json'
    out.write_text(json.dumps(k62, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print('fidelity keys R62 written:', out.relative_to(ART.parents[1]))


def edits():
    o = ART / 'OWNER-EDITS.json'
    d = json.loads(o.read_text(encoding='utf-8'))
    new = [{'id': 'r62-leaf-juice', 'status': 'applied',
            'what': ('his round-62 LEAF-JUICE answer in B174: the juice relaxes him; it works through the skin almost as '
                     'well as eating the leaf; to give it on purpose, the juice can go under the armpits, for example (three '
                     'steps, the last Human High 122 with B171, 6026d11b; humanize/h81-20261127/RESULTS.md)'),
            'joel': '%s: his round-62 export (%s), card LEAF-JUICE' % (WHEN, ANS),
            'applied_by': 'humanize/h81-20261127/apply_h81.py',
            'must_contain_exact': ['can relax me if the juice', 'almost as well as eating the leaf does',
                                   'you can put the juice under the armpits, for example'],
            'must_not_contain': ['even picking one can affect me']},
           {'id': 'r62-nibble-size', 'status': 'pending',
            'what': ('his round-62 NIBBLE-SIZE answer in B173: 200mg of leaf at a time, or 10mg of the extract paste, for '
                     'nausea; more only if the person doesn\'t mind the trip getting less intense. With them in, the nibble '
                     'sentence read Medium 16 in every step and the lineage used its six tries, so his own version of B173 '
                     'goes in (round 63, TEACH-B173)'),
            'joel': '%s: his round-62 export (%s), card NIBBLE-SIZE' % (WHEN, ANS),
            'waits_for': 'his answer to round 63\'s TEACH-B173'}]
    by = {e['id']: e for e in d['entries']}
    for n in new:
        if n['id'] in by:
            by[n['id']].clear()
            by[n['id']].update(n)
        else:
            d['entries'].append(n)
    o.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print('owner edits:', len(d['entries']))


if __name__ == '__main__':
    {'keys': keys, 'edits': edits}[sys.argv[1]]()
