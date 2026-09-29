"""Measure the repository's unmodified tells linter on raw evaluation outputs."""
import argparse
import ast
import hashlib
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

def main(args):
    rows = [json.loads(l) for l in args.cases.read_text().splitlines()]
    args.output.mkdir(parents=True, exist_ok=True)
    scored = []
    linter_sha = hashlib.sha256(args.linter.read_bytes()).hexdigest()
    with tempfile.TemporaryDirectory() as temp:
        source, draft = Path(temp) / 'source.txt', Path(temp) / 'draft.txt'
        for case in rows:
            source.write_text(case.get('input', case.get('ai')))
            for system, result in case['outputs'].items():
                draft.write_text(result['text'])
                run = subprocess.run([sys.executable, str(args.linter), str(draft), '--source', str(source)],
                                     text=True, capture_output=True)
                assert run.returncode in {0, 1, 2} and 'metrics:' in run.stdout, run.stderr
                metrics = ast.literal_eval(next(l[9:] for l in run.stdout.splitlines() if l.startswith('metrics: ')))
                counts = {rule: int(count) for rule, count in re.findall(r'^-- (.+) \((\d+)\)$', run.stdout, re.M)}
                hits = sum(counts.values())
                record = {'id': case['id'], 'system': system,
                          'output_sha256': hashlib.sha256(result['text'].encode()).hexdigest(),
                          'linter_sha256': linter_sha, 'metrics': metrics, 'flags_by_rule': counts,
                          'hits': hits, 'hits_per_100_words': 100 * hits / metrics['words'],
                          'hard_conditions': [l.strip()[6:] for l in run.stdout.splitlines() if l.strip().startswith('HARD: ')],
                          'verdict': next(l[9:] for l in run.stdout.splitlines() if l.startswith('verdict: ')),
                          'definition': 'All printed per-rule flags; aggregate hard conditions reported separately',
                          'raw_stdout': run.stdout.replace(str(source), '<input>').replace(str(draft), '<output>')}
                scored.append(record)
    (args.output / 'tells-scores.jsonl').write_text(''.join(json.dumps(r, ensure_ascii=False) + '\n' for r in scored))
    print(json.dumps({'outputs_scored': len(scored), 'linter_sha256': linter_sha}))

if __name__ == '__main__':
    p = argparse.ArgumentParser(); p.add_argument('--cases', type=Path, required=True)
    p.add_argument('--linter', type=Path, required=True); p.add_argument('--output', type=Path, required=True)
    main(p.parse_args())
