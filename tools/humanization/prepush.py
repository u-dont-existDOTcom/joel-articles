#!/usr/bin/env python3
"""prepush.py - before a push of a humanization branch: register each article's new files, bring the hand-kept authority
and review hashes in articles/INDEX.json up to date for those articles, then run the content validator (2026-10-18; it
was a scratch script of the community lane until then, so a second account couldn't run it).

  python3 tools/humanization/prepush.py --article intentional-communities --article inner-signal   # from the repo root

A working record that was deleted (superseded, never Joel's) is dropped from the inventory; Git keeps its history. The
authority and review hashes are refreshed only for the articles named, whose working copies this lane changes on purpose.
The pre-push hook (tools/humanization/git-hooks/pre-push) still runs CI's steps on every pushed commit.
"""
import argparse, hashlib, json, pathlib, subprocess, sys

ROOT = pathlib.Path(__file__).resolve().parents[2]


def run(*a):
    r = subprocess.run(a, cwd=ROOT, capture_output=True, text=True)
    out = (r.stdout + r.stderr).strip().splitlines()
    print(' '.join(str(x) for x in a[1:4]), 'rc=%d' % r.returncode, *(out[-3:] if out else []), sep='\n  ')
    return r.returncode


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--article', action='append', required=True)
    a = ap.parse_args()
    for art in a.article:
        run(sys.executable, 'scripts/register_article_artifacts.py', '--article', art, '--write')
    p = ROOT / 'articles' / 'INDEX.json'
    d = json.loads(p.read_text(encoding='utf-8'))
    changed = []
    for art in d['articles']:
        if art['id'] not in a.article:
            continue
        pre = 'articles/%s/' % art['id']
        gone = [e for e in art.get('additional_artifacts', []) if not (ROOT / e['path']).is_file()
                and e['path'].startswith(pre) and e.get('role') == 'humanization_working_record']
        for e in gone:
            art['additional_artifacts'].remove(e)
            changed.append('dropped ' + e['path'])
        for e in art.get('additional_artifacts', []):
            f = ROOT / e['path']
            if f.is_file() and e.get('role') == 'humanization_working_record':
                h = hashlib.sha256(f.read_bytes()).hexdigest()
                if e.get('sha256') != h:
                    e['sha256'] = h
                    changed.append(e['path'])
        for grp in ('authority', 'review'):
            for k, v in (art.get(grp) or {}).items():
                f = ROOT / v['path']
                if f.is_file():
                    h = hashlib.sha256(f.read_bytes()).hexdigest()
                    if v['sha256'] != h:
                        v['sha256'] = h
                        changed.append('%s %s' % (art['id'], k))
    if changed:
        p.write_text(json.dumps(d, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    print('hashes updated:', changed or 'none')
    return run(sys.executable, 'scripts/validate_content_repository.py')


if __name__ == '__main__':
    sys.exit(main())
