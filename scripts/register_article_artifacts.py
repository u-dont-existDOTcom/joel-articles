#!/usr/bin/env python3
"""Bring an article's additional-artifact inventory in articles/INDEX.json up to date.

The content validator (scripts/validate_content_repository.py) fails when a file inside a
registered article's folder isn't in that article's authority, review, export or
additional-artifact inventory, or when a registered file's SHA-256 doesn't match. Working
branches add records (drafts, reviewer targets, Pangram texts) without registering them, so
the validator passes on main and fails on the branch. Run this before merging a branch into
main (2026-10-01, when the Inner Child lane was first merged):

  python3 scripts/register_article_artifacts.py --article inner-child-therapy          # report
  python3 scripts/register_article_artifacts.py --article inner-child-therapy --write  # update

What it changes, and only this:
- adds every unregistered file in articles/<id>/ to additional_artifacts, with its SHA-256
  and a role taken from its path (ROLE_RULES below; anything else is a working record);
- updates the SHA-256 of an additional artifact whose file changed, but only for roles that
  are meant to change (active_*, and the working roles below). A changed file with any other
  role (a superseded snapshot, a receipt) is reported and left alone for a person to decide.
It never touches the authority or review entries (the master, owner locks, source evidence,
current state, citations, detector and editorial status): those hashes are the authority.
"""
import argparse
import fnmatch
import hashlib
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
INDEX = ROOT / 'articles' / 'INDEX.json'

# (glob relative to the article folder, role); the first match wins
ROLE_RULES = [
    ('experiments/emulate-*/**', 'emulate_experiment'),
    ('experiments/reviewer-loop-*/**', 'reviewer_loop_experiment'),
    ('experiments/WRITER-LEASE-*.json', 'writer_lease'),
    ('experiments/*PRESERVATION*', 'preservation_proof'),
    ('experiments/*RESULT*', 'detector_experiment_result'),
    ('experiments/*RECEIPT*', 'editorial_receipt'),
    ('experiments/SOURCE-SNAPSHOT-*', 'source_snapshot'),
    ('experiments/SOURCE-INSERT-*', 'owner_source_insert'),
    ('experiments/SOURCE-WORKING-*', 'source_working_copy'),
    ('experiments/SOURCE-UPDATE-*', 'source_delta_humanization_impact'),
    ('tools/targets/*', 'reviewer_target'),
    ('tools/in-context/*', 'in_context_map'),
    ('tools/pangram-runs/*', 'detector_check_texts'),
    ('tools/PREDICTIONS.md', 'detector_prediction_log'),
    ('tools/HUMANIZATION-GATE.md', 'pointer_to_shared_gate'),
    ('OWNER-EDITS.json', 'owner_edits_ledger'),
    ('OPEN-OWNER-FLAGS.md', 'open_owner_flags'),
    ('OWNER-QUESTIONS.md', 'owner_questions_page'),
    ('PARKED-READER-QUESTIONS.md', 'parked_reader_questions'),
]
DEFAULT_ROLE = 'humanization_working_record'
MUTABLE_ROLES = ({role for _, role in ROLE_RULES} | {DEFAULT_ROLE}) - {'editorial_receipt', 'detector_experiment_result', 'source_snapshot'}


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def role_for(rel):
    for pattern, role in ROLE_RULES:
        if fnmatch.fnmatch(rel, pattern) or (pattern.endswith('/**') and rel.startswith(pattern[:-2])):
            return role
    return DEFAULT_ROLE


def registered_paths(article):
    paths = set()
    def walk(x):
        if isinstance(x, dict):
            if isinstance(x.get('path'), str):
                paths.add(x['path'])
            for v in x.values():
                walk(v)
        elif isinstance(x, list):
            for v in x:
                walk(v)
    for key in ('authority', 'review', 'publication_exports', 'additional_artifacts'):
        walk(article.get(key))
    return paths


def main():
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('--article', required=True, help="the article's id in articles/INDEX.json")
    ap.add_argument('--write', action='store_true', help='update articles/INDEX.json (default: report only)')
    a = ap.parse_args()
    index = json.loads(INDEX.read_text(encoding='utf-8'))
    article = next((x for x in index['articles'] if x.get('id') == a.article), None)
    if article is None:
        sys.exit(f'no article {a.article!r} in {INDEX}')
    folder = ROOT / 'articles' / a.article
    known = registered_paths(article)
    added, updated, refused = [], [], []
    for f in sorted(folder.rglob('*')):
        if not f.is_file() or '__pycache__' in f.parts or f.name.startswith('.'):
            continue
        path = f.relative_to(ROOT).as_posix()
        if path in known:
            continue
        rel = f.relative_to(folder).as_posix()
        entry = {'path': path, 'sha256': sha256(f), 'role': role_for(rel)}
        article.setdefault('additional_artifacts', []).append(entry)
        added.append(entry)
    for entry in article.get('additional_artifacts', []):
        f = ROOT / entry['path']
        if not f.is_file() or entry in added:
            continue
        now = sha256(f)
        if now != entry.get('sha256'):
            if entry.get('role', '').startswith('active_') or entry.get('role') in MUTABLE_ROLES:
                entry['sha256'] = now
                updated.append(entry['path'])
            else:
                refused.append((entry['path'], entry.get('role')))
    for e in added:
        print(f"add     {e['role']:<34} {e['path']}")
    for p in updated:
        print(f'rehash  {p}')
    for p, r in refused:
        print(f'CHANGED {p} (role {r!r}): left alone; decide by hand')
    print(f'{len(added)} to add, {len(updated)} to rehash, {len(refused)} left alone')
    if a.write and (added or updated):
        INDEX.write_text(json.dumps(index, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
        print(f'wrote {INDEX.relative_to(ROOT)}')
    return 1 if refused else 0


if __name__ == '__main__':
    sys.exit(main())
