"""Bound and audit a resumed generation run in a separate runtime directory."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import signal
import subprocess
import time


def main(args):
    repo = args.root / 'repo'
    tool = repo / 'docs/reverse-model-20260929/tools/generate_pairs.py'
    source = repo / 'docs/reverse-model-20260929/data/human-passages.jsonl'
    output = args.root / 'generated'
    assert args.batch_size > 0 and args.new_passages >= 0 and args.seconds > 0
    assert source.is_file() and output.joinpath('pairs-audit.jsonl').is_file()
    started = time.time()
    run_id = f'{int(started)}-b{args.batch_size}-n{args.new_passages}'
    history = output / 'run-history' / run_id
    history.mkdir(parents=True, exist_ok=False)
    for name in ['generation-manifest.json', 'generation-status.json']:
        if output.joinpath(name).is_file():
            shutil.copy2(output / name, history / name)
    before = [json.loads(line) for line in output.joinpath('pairs-audit.jsonl').read_text().splitlines()]
    receipt = {'started_unix': started, 'run_id': run_id,
               'repo_commit': subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=repo, text=True).strip(),
               'generator_sha256': hashlib.sha256(tool.read_bytes()).hexdigest(),
               'source_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
               'processed_before': len(before), 'batch_size': args.batch_size,
               'new_passage_limit': args.new_passages, 'deadline_seconds': args.seconds,
               'termination_grace_seconds': 120, 'status': 'RUNNING'}
    path = history / 'run-receipt.json'
    path.write_text(json.dumps(receipt, indent=2)+'\n')
    command = ['/venv/main/bin/python', '-u', str(tool), '--input', str(source),
               '--output', str(output), '--batch-size', str(args.batch_size),
               '--limit', str(args.new_passages), '--deadline-unix', str(started+args.seconds)]
    child = subprocess.Popen(command, start_new_session=True)
    try:
        returncode = child.wait(timeout=args.seconds)
        status = 'COMPLETE' if returncode == 0 else 'FAILED'
    except subprocess.TimeoutExpired:
        os.killpg(child.pid, signal.SIGTERM)
        try:
            returncode = child.wait(timeout=120)
        except subprocess.TimeoutExpired:
            os.killpg(child.pid, signal.SIGKILL)
            returncode = child.wait()
        status = 'DEADLINE_SAVED_PARTIAL_EVIDENCE'
    receipt.update(ended_unix=time.time(), returncode=returncode, status=status)
    path.write_text(json.dumps(receipt, indent=2)+'\n')
    print(json.dumps(receipt), flush=True)
    raise SystemExit(0 if status in {'COMPLETE', 'DEADLINE_SAVED_PARTIAL_EVIDENCE'} else returncode)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--root', type=Path, default=Path('/workspace/reverse-pilot-20260929'))
    parser.add_argument('--batch-size', type=int, default=32)
    parser.add_argument('--new-passages', type=int, default=32)
    parser.add_argument('--seconds', type=int, default=3600)
    main(parser.parse_args())
