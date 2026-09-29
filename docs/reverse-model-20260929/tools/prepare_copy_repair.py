"""Preserve the original audit and queue only accepted copied regenerations."""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import os
from copy_check import regeneration_guard, POLICY


def atomic_text(path, body):
    pending = path.with_name(path.name + '.pending')
    with pending.open('w') as handle:
        handle.write(body)
        handle.flush()
        os.fsync(handle.fileno())
    pending.replace(path)


def write_splits(output, rows):
    for split in ['train', 'dev', 'test']:
        atomic_text(output / f'{split}-pairs.jsonl', ''.join(
            json.dumps(row, ensure_ascii=False)+'\n' for row in rows
            if row['accepted'] and row['split'] == split))


def prepare(output):
    history = output / 'run-history/pre-copy-repair-v2'
    receipt = history / 'repair-admission.json'
    if receipt.exists():
        return json.loads(receipt.read_text())
    rows = [json.loads(line) for line in (output/'pairs-audit.jsonl').read_text().splitlines()]
    assert len({row['id'] for row in rows}) == len(rows)
    history.mkdir(parents=True, exist_ok=True)
    baseline_manifest = history / 'baseline-manifest.json'
    if baseline_manifest.exists():
        hashes = json.loads(baseline_manifest.read_text())
        assert all(hashlib.sha256((history/name).read_bytes()).hexdigest() == value
                   for name, value in hashes.items()), 'Immutable baseline changed'
    else:
        hashes = {}
        for name in ['pairs-audit.jsonl', 'train-pairs.jsonl', 'dev-pairs.jsonl',
                     'test-pairs.jsonl', 'generation-manifest.json', 'generation-status.json']:
            path = output / name
            if path.exists():
                saved = history / name
                if not saved.exists():
                    shutil.copy2(path, saved)
                hashes[name] = hashlib.sha256(saved.read_bytes()).hexdigest()
        atomic_text(baseline_manifest, json.dumps(hashes, indent=2)+'\n')
    # The immutable baseline also repairs an interruption between atomic writes.
    rows = [json.loads(line) for line in (history/'pairs-audit.jsonl').read_text().splitlines()]
    pending = []
    for row in rows:
        if row['accepted'] and row['method'] == 'notes_regeneration':
            row['copy_guard'] = regeneration_guard(row['human'], row['notes'], row['ai'])
            if not row['copy_guard']['passed']:
                row['copy_repair_pending'] = True
                row['accepted'] = False
                row['rejection_reasons'] = ['copy_guard_repair_pending']
                pending.append(row['id'])
    result = {'policy': POLICY, 'baseline_files_sha256': hashes, 'processed_before': len(rows),
              'accepted_before': sum(json.loads(line)['accepted'] for line in (history/'pairs-audit.jsonl').read_text().splitlines()),
              'queued_once_for_fresh_notes_and_draft': pending,
              'accepted_retained_before_repair': sum(row['accepted'] for row in rows),
              'paraphrases_unchanged': True, 'detector_used_as_filter': False}
    atomic_text(output/'pairs-audit.jsonl', ''.join(json.dumps(row, ensure_ascii=False)+'\n' for row in rows))
    write_splits(output, rows)
    atomic_text(receipt, json.dumps(result, indent=2)+'\n')
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, required=True)
    print(json.dumps(prepare(parser.parse_args().output), indent=2))
