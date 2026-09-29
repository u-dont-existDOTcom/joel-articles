"""Join frozen cases to first cached outputs, never generate or replace a result."""
import argparse
import hashlib
import json
from pathlib import Path

def main(args):
    cases = [json.loads(l) for p in args.cases for l in p.read_text().splitlines()]
    assert len({r['id'] for r in cases}) == len(cases)
    joined = []
    for case in cases:
        text = case.get('input', case.get('ai'))
        digest = hashlib.sha256(text.encode()).hexdigest()
        assert digest == case['input_sha256']
        outputs = {}
        for system, directory in [('base', args.base), ('instruct', args.instruct)]:
            result = json.loads((directory / (case['id'] + '.json')).read_text())
            assert result['condition'] == system and result['input_sha256'] == digest
            assert result['temperature'] == 0.8
            outputs[system] = result
        if case.get('emulate'):
            outputs['emulate'] = case['emulate']
        elif args.emulate and (args.emulate / (case['id'] + '.json')).exists():
            result = json.loads((args.emulate / (case['id'] + '.json')).read_text())
            assert result['input_sha256'] == digest and result['status'] == 'completed'
            outputs['emulate'] = result
        for result in outputs.values():
            result['output_sha256'] = hashlib.sha256(result['text'].encode()).hexdigest()
        joined.append({**case, 'outputs': outputs})
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(''.join(json.dumps(r, ensure_ascii=False) + '\n' for r in joined))
    print(json.dumps({'cases': len(joined), 'all_three_systems': sum(len(r['outputs']) == 3 for r in joined),
                      'joined_sha256': hashlib.sha256(args.output.read_bytes()).hexdigest()}))

if __name__ == '__main__':
    p = argparse.ArgumentParser(); p.add_argument('--cases', type=Path, nargs='+', required=True)
    p.add_argument('--base', type=Path, required=True); p.add_argument('--instruct', type=Path, required=True)
    p.add_argument('--emulate', type=Path); p.add_argument('--output', type=Path, required=True)
    main(p.parse_args())
