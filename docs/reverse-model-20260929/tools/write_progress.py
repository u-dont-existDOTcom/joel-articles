"""Read-only measurement of the current pilot runtime; no paid calls or restarts."""
import argparse
import json
from pathlib import Path
import subprocess
import time


def records(path):
    if not path.exists():
        return []
    # A growing file's incomplete final line is not yet an admitted receipt.
    return [json.loads(line) for line in path.read_bytes().split(b'\n')[:-1] if line]


def main(args):
    root = args.root
    pairs = records(root / 'generated/pairs-audit.jsonl')
    requests = records(root / 'generated/model-requests.jsonl')
    phases = []
    path = root / args.log
    for line in path.read_text(errors='replace').splitlines() if path.exists() else []:
        if line.startswith('{'):
            try:
                phases.append(json.loads(line))
            except ValueError:
                pass
    base = json.loads((root/'runtime-environment/download-manifest-base.json').read_text())
    supervisor = subprocess.run(['supervisorctl', 'status'], capture_output=True, text=True)
    gpu = subprocess.run(['nvidia-smi', '--query-gpu=utilization.gpu,memory.used,memory.total',
                          '--format=csv,noheader,nounits'], capture_output=True, text=True)
    receipts = sorted((root/'generated/run-history').glob('*/run-receipt.json'))
    result = {'as_of_unix': time.time(),
              'supervisor': [line for line in supervisor.stdout.splitlines() if 'reverse-pilot-' in line],
              'gpu': gpu.stdout.strip(), 'processed': len(pairs),
              'accepted': sum(pair['accepted'] for pair in pairs), 'requests': len(requests),
              'phases': phases[-5:], 'base_status': base['status'],
              'base_verified_weights': sum(f['filename'].endswith('.safetensors') and f['verified'] for f in base['files']),
              'base_partial_allocated_bytes': sum(p.stat().st_blocks*512 for p in (root/'download-pieces-base').glob('*.safetensors')),
              'latest_run_receipt': json.loads(receipts[-1].read_text()) if receipts else None}
    (root/'runtime-progress.txt').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2), flush=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--root', type=Path, default=Path('/workspace/reverse-pilot-20260929'))
    parser.add_argument('--log', default='batch32.log')
    main(parser.parse_args())
