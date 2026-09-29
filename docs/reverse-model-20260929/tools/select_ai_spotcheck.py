"""Freeze the first 20 open-judge-accepted drafts before detector scores."""
import argparse
import hashlib
import json
from pathlib import Path


def main(args):
    pairs = [json.loads(line) for line in args.generated.joinpath('pairs-audit.jsonl').read_text().splitlines()]
    requests = [json.loads(line) for line in args.generated.joinpath('model-requests.jsonl').read_text().splitlines()]
    by_request = {(r['id'], r['phase']): r for r in requests}
    selected = []
    for pair in sorted(pairs, key=lambda r: r['id']):
        phase = 'paraphrase_or_notes' if pair['method'] == 'paraphrase' else 'fresh_notes_regeneration'
        request = by_request[(pair['id'], phase)]
        assert request['response'] == pair['ai']
        assert hashlib.sha256(pair['ai'].encode()).hexdigest() == pair['ai_sha256']
        if not pair['accepted'] or request['truncated'] or len(pair['ai'].split()) < 50:
            continue
        selected.append({'id': pair['id'], 'text': pair['ai'], 'text_sha256': pair['ai_sha256'],
                         'request': request['request'], 'method': pair['method'],
                         'fidelity_accepted': pair['accepted'], 'model': pair['open_model'],
                         'revision': pair['open_model_revision'], 'scope': 'detector measurement only; never a training filter label'})
        if len(selected) == 20:
            break
    assert len(selected) == 20, 'Need 20 complete drafts before the spot-check'
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(''.join(json.dumps(r, ensure_ascii=False) + '\n' for r in selected))
    print(json.dumps({'selected': 20, 'ids': [r['id'] for r in selected],
                      'selection': 'first complete open-judge-accepted AI drafts by frozen passage ID; before detector scores',
                      'minimum_words': 50, 'selection_sha256': hashlib.sha256(args.output.read_bytes()).hexdigest()}))


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--generated', type=Path, required=True)
    p.add_argument('--output', type=Path, required=True)
    main(p.parse_args())
