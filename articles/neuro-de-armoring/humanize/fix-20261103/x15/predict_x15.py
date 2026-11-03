"""His version of agmatine's interactions (X-15 on Neuro De-Armoring Cards, 3 November), checked by itself.

He tested his other two versions himself ("passes", X-26 and X-84), so they aren't sent again; he left X-15 with no
comment. This writes TEXTS.json (the paragraph as the post reads it, from HUMANIZED-SO-FAR.md after apply_answers_x1103.py)
and PREDICTIONS.json (the list record_r1102.py reads), and puts the prediction in the lane's ledger first (gate E307).

  python3 articles/neuro-de-armoring/humanize/fix-20261103/x15/predict_x15.py
Then on the laptop, in inbox/neuro-x1103 with TEXTS.json and SHA256SUMS:
  python3 ../pangram-r1102/pangram_api.py check TEXTS.json out --expect 4.1 --windows --public > x15.log 2> x15.err
"""
import hashlib
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parents[1]
ROOT = H.parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import suggestion_review as sr  # noqa: E402

LEDGER = H / 'pangram-ledger.jsonl'
ARTICLE_SHA = '6db92b7aff987195049b8af1f99883ec4a3f2e05e62af6a978679871c7957944'
DETECTOR = 'pangram 4.1, the API (Joel\'s key, run on his laptop; E218, E325: at most six paragraphs and 1,200 words)'
BATCH = 'x1103'
P = {'key': 'x15', 'name': 'his version of agmatine\'s interactions (X-15), by itself', 'lineage': 'ND1103-X15',
     'scope': 'paragraph', 'chance': 0.4,
     'why': 'his package-insert register and his own qualifiers ("and/or", "(will reduce tolerance)", "lower end blood '
            'pressure", "a physician competent to consider the likelihoods") against a dense list of drugs and conditions, '
            'the shape that read 100% AI in round 1; he left it without "passes"',
     'diagnosis': 'his own rewrite of the warnings paragraph, one of the three examples he asked for to train round 2',
     'decides': 'whether his way with warnings reads Human by itself, so round 2 writes the other warnings his way, or '
                'whether a list of warnings needs something more'}


def main():
    md = (H / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
    assert hashlib.sha256(md.encode('utf-8')).hexdigest() == ARTICLE_SHA, 'the article changed'
    hits = [b for b in sr.blocks(md) if b['text'].startswith('Precautions/Side Effects: Do not use concurrently')]
    assert len(hits) == 1
    t = hits[0]['text']
    sha = hashlib.sha256(t.encode('utf-8')).hexdigest()
    (HERE / 'TEXTS.json').write_text(json.dumps({P['key']: t}, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    (HERE / 'x15.txt').write_text(t, encoding='utf-8')
    call = 'Human' if P['chance'] >= 0.5 else 'AI'
    row = {'key': P['key'], 'name': P['name'], 'lineage': P['lineage'], 'scope': P['scope'], 'words': len(t.split()),
           'call': call, 'chance': P['chance'], 'why': P['why'], 'sha256': sha}
    (HERE / 'PREDICTIONS.json').write_text(json.dumps([row], ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    done = any(json.loads(l).get('batch') == BATCH and json.loads(l).get('key') == P['key']
               for l in LEDGER.read_text(encoding='utf-8').splitlines())
    if done:
        print('already predicted in', BATCH)
        return
    subprocess.run([sys.executable, str(ROOT / 'tools' / 'humanization' / 'pangram_ledger.py'), 'predict', str(LEDGER),
                    '--lineage', P['lineage'], '--scope', P['scope'], '--text', str(HERE / 'x15.txt'), '--call', call,
                    '--chance', str(P['chance']), '--key', P['key'], '--batch', BATCH, '--detector', DETECTOR,
                    '--tells', P['why'], '--diagnosis', P['diagnosis'], '--decides', P['decides']], check=True)


if __name__ == '__main__':
    main()
