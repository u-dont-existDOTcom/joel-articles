"""Select held-out general cases within the Emulate word cap before detector work."""
import argparse
import hashlib
import json
from pathlib import Path

SOURCE_SHA256 = '56869801ee7f95dfea1681170c745cacf112f93c117a185177c515568c80b089'

def main(args):
    assert hashlib.sha256(args.human_source.read_bytes()).hexdigest() == SOURCE_SHA256
    originals = {r['id']: r for r in (json.loads(l) for l in args.human_source.read_text().splitlines())}
    rows = [json.loads(l) for l in args.pairs.read_text().splitlines()]
    assert rows and all(r['split'] == 'test' and r['accepted'] for r in rows)
    assert len({r['document_id'] for r in rows}) == len(rows)
    for row in rows:
        assert originals[row['id']]['split'] == 'test'
        assert originals[row['id']]['human'] == row['human']
        assert originals[row['id']]['document_id'] == row['document_id']
        assert hashlib.sha256(row['ai'].encode()).hexdigest() == row['ai_sha256']
    # Length is the selection variable, not detector/meaning scores. The resulting
    # general arm is a short-paragraph comparison; report this limitation explicitly.
    ranked = sorted(rows, key=lambda r: (len(r['ai'].split()), r['id']))
    chosen = ranked[:20]
    assert len(chosen) == 20 and min(len(r['ai'].split()) for r in chosen) >= 40
    assert sum(len(r['ai'].split()) for r in chosen) <= args.word_allowance
    cases = [{'id': 'G_' + r['id'], 'set': 'general', 'input': r['ai'],
              'input_sha256': r['ai_sha256'], 'input_words': len(r['ai'].split()),
              'human_reference': r['human'], 'human_source_id': r['id'],
              'document_id': r['document_id'], 'genre': r['genre'],
              'generation_method': r['method'], 'emulate': None} for r in chosen]
    args.output.mkdir(parents=True, exist_ok=True)
    path = args.output / 'general-cases.jsonl'
    assert not path.exists(), 'General selection already frozen; reuse, never replace'
    path.write_text(''.join(json.dumps(r, ensure_ascii=False) + '\n' for r in cases))
    manifest = {'source_sha256': SOURCE_SHA256,
                'pair_file_sha256': hashlib.sha256(args.pairs.read_bytes()).hexdigest(),
                'cases_sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
                'cases': 20, 'emulate_input_words': sum(r['input_words'] for r in cases),
                'word_allowance': args.word_allowance,
                'selection': '20 shortest accepted held-out AI counterparts, ties by source ID; before detector scoring',
                'limitation': 'General results describe short paragraphs, not the full length distribution',
                'E_holdout_accessed': False}
    (args.output / 'general-manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
    print(json.dumps(manifest, indent=2))

if __name__ == '__main__':
    p = argparse.ArgumentParser(); p.add_argument('--pairs', type=Path, required=True)
    p.add_argument('--human-source', type=Path, required=True)
    p.add_argument('--output', type=Path, required=True)
    p.add_argument('--word-allowance', type=int, default=2800)
    main(p.parse_args())
