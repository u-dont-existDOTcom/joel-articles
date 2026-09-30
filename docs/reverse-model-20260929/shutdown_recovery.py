#!/usr/bin/env python3
"""Inventory and package the stopped reverse-pilot instance for verified recovery."""

import hashlib
import os
import re
import sys
import tarfile
from pathlib import Path

ROOT = Path('/workspace/reverse-pilot-20260929')
OUT = ROOT / 'shutdown-export'
V4 = ROOT / 'trial-v4' / 'roundtrip'
SLOTS = ROOT / 'trial-v3' / 'slots'
SECRET_RE = re.compile(
    rb'(?:hf_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|'
    rb'gh[opusr]_[A-Za-z0-9_]{20,}|(?<![A-Za-z])sk-[A-Za-z0-9_-]{20,}|'
    rb'(?:Authorization|Bearer|VENICE_API_KEY|VAST_API_KEY|HF_TOKEN|'
    rb'GITHUB_TOKEN)\s*[:= ]\s*[A-Za-z0-9_./+-]{16,})', re.I
)
NAME_SECRETS = {'.env', '.netrc', '.git-credentials', '.bash_history',
                '.zsh_history', '.python_history', '.vast_api_key'}


def digest(path):
    h = hashlib.sha256()
    with path.open('rb') as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()


def files_under(path):
    if path.is_file() or path.is_symlink():
        yield path
    elif path.exists():
        for base, dirs, names in os.walk(path, followlinks=False):
            dirs[:] = sorted(d for d in dirs if not (Path(base) / d).is_symlink())
            for name in sorted(names):
                yield Path(base) / name


def candidates():
    yield from files_under(ROOT)
    for extra in ['/tmp/pilot-agent-guide.txt', '/tmp/reverse-pilot-range-probe',
                  '/tmp/torchinductor_root',
                  '/tmp/.ipynb_checkpoints/pilot-agent-guide-checkpoint.txt',
                  '/root/.vast_api_key', '/root/.ssh/authorized_keys']:
        yield from files_under(Path(extra))
    for path in files_under(Path('/root')):
        name = str(path).lower()
        if any(tag in name for tag in ('reverse-pilot', 'pilot-', 'trial-v3', 'trial-v4')):
            yield path


def is_weight(path):
    s = str(path).lower()
    return (path.suffix in {'.safetensors', '.aria2'} or
            '/download-pieces-' in s or '/.cache/huggingface/' in s or
            '/models--' in s)


def is_secret_name(path):
    return any(part in NAME_SECRETS or part.startswith('.env.')
               for part in path.parts) or '/.ssh/' in str(path)


def contains_secret(path):
    if path.is_symlink():
        return False
    with path.open('rb') as fh:
        tail = b''
        for chunk in iter(lambda: fh.read(1024 * 1024), b''):
            if SECRET_RE.search(tail + chunk):
                return True
            tail = chunk[-256:]
    return False


def bucket(path):
    if path == SLOTS or SLOTS in path.parents:
        return 'slots'
    if path == V4 or V4 in path.parents:
        return 'v4'
    return 'remainder'


def collect():
    unique = sorted(set(p for p in candidates() if OUT not in p.parents),
                    key=str)
    rows = []
    included = {'v4': [], 'slots': [], 'remainder': []}
    excluded = []
    for path in unique:
        try:
            size = path.lstat().st_size
            if is_weight(path):
                rows.append((str(path), str(size), '-', 'WEIGHT_OR_PARTIAL'))
            elif is_secret_name(path) or contains_secret(path):
                rows.append((str(path), str(size), '-', 'CREDENTIAL_EXCLUDED'))
                excluded.append(str(path))
            elif path.is_symlink():
                rows.append((str(path), str(size), '-', 'SYMLINK'))
                included[bucket(path)].append(path)
            else:
                rows.append((str(path), str(size), digest(path), bucket(path)))
                included[bucket(path)].append(path)
        except (OSError, PermissionError) as exc:
            rows.append((str(path), '-', '-', 'READ_ERROR:' + type(exc).__name__))
    return rows, included, excluded


def write_inventory(rows, excluded):
    OUT.mkdir(parents=True, exist_ok=True)
    with (OUT / 'INSTANCE-INVENTORY.tsv').open('w') as fh:
        fh.write('path\tbytes\tsha256\tclassification\n')
        for row in rows:
            fh.write('\t'.join(row) + '\n')
    (OUT / 'EXCLUDED-CREDENTIAL-PATHS.txt').write_text(
        ''.join(path + '\n' for path in excluded))


def make_archive(name, paths):
    target = OUT / name
    with tarfile.open(target, 'w:gz', compresslevel=6) as tf:
        for path in paths:
            tf.add(path, arcname=str(path).lstrip('/'), recursive=False)
    return target


def split_archive(path):
    limit = 45 * 1024 * 1024
    if path.stat().st_size < 50 * 1024 * 1024:
        return []
    parts = []
    with path.open('rb') as source:
        n = 0
        while True:
            chunk = source.read(limit)
            if not chunk:
                break
            n += 1
            part = path.with_name(path.name + '.part' + str(n).zfill(3))
            part.write_bytes(chunk)
            parts.append(part)
    return parts


def main():
    rows, included, excluded = collect()
    write_inventory(rows, excluded)
    errors = [r for r in rows if r[3].startswith('READ_ERROR')]
    print('INVENTORY', len(rows), 'included',
          {key: len(paths) for key, paths in included.items()},
          'credentials_excluded', len(excluded), 'read_errors', len(errors),
          flush=True)
    if errors:
        sys.exit('Read errors; archives not made')
    archives = [make_archive('v4-roundtrip-complete.tar.gz', included['v4']),
                make_archive('slots-complete.tar.gz', included['slots']),
                make_archive('instance-remainder.tar.gz', included['remainder'])]
    for archive in archives:
        split_archive(archive)
    published = [OUT / 'INSTANCE-INVENTORY.tsv',
                 OUT / 'EXCLUDED-CREDENTIAL-PATHS.txt']
    for archive in archives:
        parts = sorted(OUT.glob(archive.name + '.part*'))
        published.extend(parts or [archive])
    with (OUT / 'SHA256SUMS').open('w') as fh:
        for path in archives + published:
            fh.write(digest(path) + '  ' + path.name + '\n')
            print('SHA256', digest(path), path.stat().st_size, path.name,
                  flush=True)
    print('DONE', str(OUT), flush=True)


if __name__ == '__main__':
    main()
