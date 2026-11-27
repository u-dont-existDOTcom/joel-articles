"""apply_r61.py - his round-61 answers into the guide, from the repo root (after
`python3 articles/bad-trips/humanize/h79-20261126/apply_h79.py charcoal`, his CHARCOAL-WORDS "a"):

  python3 articles/bad-trips/review/r61/apply_r61.py b155     his TEACH-B155 version of B155, whole, from his answers file
  python3 articles/bad-trips/review/r61/apply_r61.py b158     B158 with his FROM-POST answer on the rubbing, from the
                                                              checked text (humanize/h80-20261127/TEST-a3-b158.txt), once
                                                              it reads Human High by itself (apply_gate.py)

TEACH-B155 ("revise"): his version, which he checked himself, Human High in one window by itself (00eb45f1) and with
B158 before it (54b91410); read from the pages his links open (review/r61/HIS-CHECKS-R61.json). The one change is the
space after his last full stop, which his box kept and the guide's blocks never carry.
"""
import json
import pathlib
import sys

REPO = pathlib.Path(__file__).resolve().parents[4]
ART = REPO / 'articles' / 'bad-trips'
ANS = ART / 'review' / 'r61' / 'ANSWERS-R61-20261127-1534.json'


def save(blocks):
    (ART / 'GUIDE-SO-FAR.md').write_text('\n\n'.join(x['md'] for x in blocks) + '\n', encoding='utf-8')
    (ART / 'GUIDE-SO-FAR-blocks.json').write_text(json.dumps(blocks, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')


def his(card):
    return {x['id']: x for x in json.loads(ANS.read_text(encoding='utf-8'))['items']}[card]['your_version']


def b155():
    blocks = json.loads((ART / 'GUIDE-SO-FAR-blocks.json').read_text(encoding='utf-8'))
    by = {x['id']: x for x in blocks}
    by['B155']['md'] = his('TEACH-B155').strip()
    save(blocks)
    print('applied: B155 (his TEACH-B155 version, whole)')


def b158():
    sys.path.insert(0, str(REPO / 'tools' / 'humanization'))
    import apply_gate  # noqa: E402
    text = (ART / 'humanize' / 'h80-20261127' / "TEST-a3-b158.txt").read_text(encoding='utf-8').strip()
    apply_gate.require(ART / 'humanize' / 'pangram-ledger.jsonl', [text])
    blocks = json.loads((ART / 'GUIDE-SO-FAR-blocks.json').read_text(encoding='utf-8'))
    {x['id']: x for x in blocks}['B158']['md'] = text
    save(blocks)
    print('applied: B158 (the rubbing is with zeolite mixed in water)')


if __name__ == '__main__':
    {'b155': b155, 'b158': b158}[sys.argv[1]]()
