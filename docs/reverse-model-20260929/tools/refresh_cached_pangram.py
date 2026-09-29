"""Bind newer paid results to the already frozen first Emulate outputs."""
import argparse
import hashlib
import json
import subprocess
from pathlib import Path

ROOT = 'articles/inner-child-therapy/experiments/emulate-20260929/'

def main(args):
    commit = subprocess.check_output(['git', 'rev-parse', args.ref], text=True).strip()
    grades = [json.loads(l) for l in subprocess.check_output(
        ['git', 'show', commit + ':' + ROOT + 'runs/pangram.jsonl'], text=True).splitlines()]
    cases = [json.loads(l) for l in args.cases.read_text().splitlines()]
    receipts = []
    for case in cases:
        first = case.get('emulate')
        if not first:
            continue
        path = first['source_file']
        assert path.startswith(ROOT + 'runs/'), path
        matching = [g for g in grades if ROOT + g.get('text_file', '') == path
                    and g.get('status', 'completed') == 'completed']
        if not matching:
            continue
        actual = subprocess.check_output(['git', 'show', commit + ':' + path], text=True)
        digest = hashlib.sha256(actual.encode()).hexdigest()
        assert digest == first['sha256'], 'First output changed at newer ref: ' + case['id']
        for grade in matching:
            assert not grade.get('text_sha256') or grade['text_sha256'] == digest
            receipts.append({'id': case['id'], 'system': 'emulate', 'boundary': 'alone',
                             'output_sha256': digest, 'source_commit': commit,
                             'source_file': path, 'reused_paid_result': True, 'score': grade})
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(''.join(json.dumps(r, ensure_ascii=False) + '\n' for r in receipts))
    print(json.dumps({'cached_first_outputs': len({r['id'] for r in receipts}),
                      'receipts': len(receipts), 'source_commit': commit,
                      'new_paid_scans': 0, 'E_holdout_accessed': False}))

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--ref', required=True)
    p.add_argument('--cases', type=Path, required=True)
    p.add_argument('--output', type=Path, required=True)
    main(p.parse_args())
