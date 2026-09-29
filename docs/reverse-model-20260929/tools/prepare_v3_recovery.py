"""Preserve interrupted v3 requests and reissue only censored calls per Claude."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import tempfile

from request_cache import complete_lines, key


FILES = ('model-requests.jsonl', 'request-reservations.jsonl',
         'trial-results.jsonl', 'trial.log', 'trial-manifest.json')
EXPECTED_CENSORED = 'H0021 H0023 H0026 H0027 H0029 H0030 H0032 H0033'.split()


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_jsonl(path, rows):
    with path.open('w') as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False) + '\n')
        handle.flush()
        os.fsync(handle.fileno())


def prepare(old, target):
    assert old.is_dir() and not target.exists()
    assert all((old/name).is_file() for name in FILES)
    requests = complete_lines(old/'model-requests.jsonl')
    reservations = complete_lines(old/'request-reservations.jsonl')
    results = complete_lines(old/'trial-results.jsonl')
    assert len(requests) == 40 and len(reservations) == 48 and len(results) == 8
    assert {row['id'] for row in results} == set('H0002 H0003 H0008 H0009 H0012 H0014 H0015 H0020'.split())
    completed = {key(row['id'], row['phase'], row['messages'][0]['content']) for row in requests}
    reserved = {tuple(row['key']) for row in reservations}
    assert len(completed) == len(requests) and len(reserved) == len(reservations)
    assert completed <= reserved
    pending = [row for row in reservations if tuple(row['key']) not in completed]
    assert len(pending) == 8
    assert {row['key'][0] for row in pending} == set(EXPECTED_CENSORED)
    assert all(row['key'][1] == 'v3_notes_1' for row in pending)
    log = (old/'trial.log').read_text()
    # The generator prints phase summaries only after all responses were saved.
    summaries = []
    for line in log.splitlines():
        if line.startswith('{'):
            try:
                summaries.append(json.loads(line))
            except ValueError:
                pass
    assert not any(set(item.get('ids', [])) & set(EXPECTED_CENSORED)
                   for item in summaries if item.get('phase') == 'v3_notes_1'), \
        'Process log shows output for a supposedly censored call'
    assert not any(row['id'] in EXPECTED_CENSORED and row['phase'] == 'v3_notes_1'
                   for row in requests), 'Request journal shows a completed output'
    target.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='.v3-recovery-', dir=target.parent) as temp:
        staging = Path(temp)
        snapshot = staging/'run-history'/'small-batch-interrupted'
        snapshot.mkdir(parents=True)
        hashes = {}
        for name in FILES:
            shutil.copy2(old/name, snapshot/name)
            hashes[name] = sha256(snapshot/name)
            assert hashes[name] == sha256(old/name)
            (snapshot/name).chmod(0o444)
        write_jsonl(staging/'model-requests.jsonl', [dict(row, batch_size=8) for row in requests])
        write_jsonl(staging/'request-reservations.jsonl',
                    [row for row in reservations if tuple(row['key']) in completed])
        shutil.copy2(old/'trial-results.jsonl', staging/'trial-results.jsonl')
        censored = [dict(reservation_key=row['key'], status='CENSORED_NO_OUTPUT',
                         reason='Operator stopped batch-8 process after first 8 final outcomes to follow Claude batch-size ruling',
                         directive_commit='2f00b08f350be837995b1f6143e124b667b69e46')
                    for row in pending]
        write_jsonl(staging/'censored-calls.jsonl', censored)
        receipt = {'source_dir': str(old), 'snapshot_sha256': hashes,
                   'completed_requests_preserved': len(requests),
                   'completed_passages_preserved': len(results),
                   'censored_reservations': len(pending),
                   'censored_ids': [row['key'][0] for row in pending],
                   'censored_reservation_ids': [row['key'] for row in pending],
                   'log_has_censored_output': False,
                   'new_batch_size': 32,
                   'reissue_policy': 'Only censored, unseen calls may be reissued; first 8 final outcomes cannot be rerun'}
        (staging/'recovery-receipt.json').write_text(json.dumps(receipt, indent=2)+'\n')
        staging.rename(target)
    return receipt


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--old', type=Path, required=True)
    p.add_argument('--target', type=Path, required=True)
    args = p.parse_args()
    print(json.dumps(prepare(args.old, args.target), indent=2))
