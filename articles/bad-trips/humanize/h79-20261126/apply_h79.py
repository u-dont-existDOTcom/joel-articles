"""apply_h79.py - turn 71's checked texts into the guide, from the repo root:

  python3 articles/bad-trips/humanize/h79-20261126/apply_h79.py

Each text read Human High by itself through the API, in every window that holds its words:

- B154 (ZeoCharge & Ferment): the ferments paragraph with his round-60 answer 2.1 (ZEO-FACTS), Human High 93 in one
  window (cc52709b), then with its short smelling line joined to the next sentence, Human High 94 in one window (cd5a0e49);
- B158: how he takes zeolite, by itself, Human High 68 in one window (fe031537);
- B156: how he ozonates it, Human High 74 by itself in one window (e36188fb), and Human High 115 with B157 (c6363909). Its
  try 2 (TEST-a2-b156.txt: the safety line joined, "going past ten minutes") read High by itself (99253002) but Medium on
  its last sentence with B157 (568966ab), so try 1 stays;
- B157: zeolite binds metals, in his post's plain words, Human High 115 with B156 (c6363909);
Not here: B155 (which zeolite). It is under 50 words, so it is read with a neighbour, and no check of it has every window
High (apply_gate.py): with B158 its sentences read High and Medium (38bb7235); with B156 after it, High 58 for its words
but Medium on B156's safety line (bf5f7b19), and with B156's try 2, Medium 9 on its first sentence and Medium on all of
B156 (9363878c). It stays as the post has it and goes to him as round 61's TEACH-B155.

Not here: Activated Charcoal (B160, B161, B162). My version read Human High 94 in one window (ae42aae9, TEST-a3-charcoal.txt),
but the warning check (fidelity_keys.py) holds two of the post's lines word for word because each has a cue word, "toxicity"
(W049) and "stop" (W051), though neither is a caution; it goes in on his answer to round 61's CHARCOAL-WORDS, with
apply_charcoal() below and his card in FIDELITY-KEYS' owner_changes.
"""
import json
import pathlib

REPO = pathlib.Path(__file__).resolve().parents[4]
ART = REPO / 'articles' / 'bad-trips'
HERE = ART / 'humanize' / 'h79-20261126'


def text(key):
    return (HERE / ('TEST-%s.txt' % key)).read_text(encoding='utf-8').strip()


def main():
    blocks = json.loads((ART / 'GUIDE-SO-FAR-blocks.json').read_text(encoding='utf-8'))
    by = {x['id']: x for x in blocks}
    ozone = text('a5-b156-b157').split('\n\n')
    assert len(ozone) == 2
    new = {'B154': text('a3-b154'), 'B158': text('a2-b158'), 'B156': ozone[0], 'B157': ozone[1]}
    for bid, md in new.items():
        by[bid]['md'] = md
    (ART / 'GUIDE-SO-FAR.md').write_text('\n\n'.join(x['md'] for x in blocks) + '\n', encoding='utf-8')
    (ART / 'GUIDE-SO-FAR-blocks.json').write_text(json.dumps(blocks, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print('applied: ' + ', '.join(new))


def apply_charcoal():
    """Activated Charcoal as it read Human High (ae42aae9), once he says the two lines may be reworded (round 61)."""
    blocks = json.loads((ART / 'GUIDE-SO-FAR-blocks.json').read_text(encoding='utf-8'))
    by = {x['id']: x for x in blocks}
    charcoal = text('a3-charcoal').split('\n\n')
    for bid, md in zip(('B160', 'B161', 'B162'), charcoal):
        by[bid]['md'] = md
    (ART / 'GUIDE-SO-FAR.md').write_text('\n\n'.join(x['md'] for x in blocks) + '\n', encoding='utf-8')
    (ART / 'GUIDE-SO-FAR-blocks.json').write_text(json.dumps(blocks, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print('applied: B160, B161, B162')


if __name__ == '__main__':
    import sys
    apply_charcoal() if sys.argv[1:] == ['charcoal'] else main()
