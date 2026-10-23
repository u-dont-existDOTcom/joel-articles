#!/usr/bin/env python3
"""Push the lane in one step (turn 76; Joel, 2026-10-19 00:55 UTC: "it took you 14m to put one line in... def need
to fix that right?").

  python3 tools/humanization/lane_push.py "Commit subject" [--article inner-child-therapy] [--add PATH ...]
                                           [--pr "Pull request title" --pr-body FILE]

1. registers the article's artifacts (scripts/register_article_artifacts.py --write), stages the article folder,
   articles/INDEX.json and any --add paths, and commits with the subject, adding the trailer lines in
   $LANE_COMMIT_TRAILERS (one per line) when it's set;
2. drops INDEX entries for article files that no longer exist (the pre-push hook refuses them), registers again,
   sets the article's CURRENT-STATE.md hash, and commits that as "INDEX hash" when anything changed;
3. runs CI's checks first (.github/workflows/content-integrity.yml) with CI's bare Python (`-S`: no installed packages),
   the unit tests whenever tests/, tools/ or scripts/ changed, and stops before the push when one fails;
4. pushes HEAD to origin (the pre-push hook runs as usual);
5. with --pr, opens a pull request into main when none is open for the branch, or names the open one;
6. says whether the branch's open pull request can merge, and when main has moved past it with a conflict, says so
   (Joel, 2026-10-22 21:41 UTC: "the pr has conflicts"; main had taken another lane's pull request after the merge).

It prints the pushed commit, which the browser's raw.githubusercontent.com fetches use.
"""
import argparse
import hashlib
import json
import os
import pathlib
import re
import subprocess
import sys
import time

REPO = pathlib.Path(__file__).resolve().parents[2]


def run(cmd, check=True, timeout=600):
    r = subprocess.run(cmd, cwd=REPO, capture_output=True, text=True, timeout=timeout)
    if check and r.returncode:
        sys.exit('failed (%d): %s\n%s%s' % (r.returncode, ' '.join(cmd), r.stdout[-3000:], r.stderr[-3000:]))
    return r


def register(article):
    run([sys.executable, 'scripts/register_article_artifacts.py', '--article', article, '--write'], timeout=300)


def prune(article):
    """Drop registered files of ARTICLE that are gone, register again, and set its CURRENT-STATE.md hash."""
    ip = REPO / 'articles/INDEX.json'
    pre = 'articles/%s/' % article
    index = json.loads(ip.read_text(encoding='utf-8'))
    gone = 0
    for a in index['articles']:
        arts = a.get('additional_artifacts')
        if isinstance(arts, list):
            keep = []
            for x in arts:
                path = x.get('path') if isinstance(x, dict) else x
                if path and path.startswith(pre) and not (REPO / path).exists():
                    gone += 1
                    continue
                keep.append(x)
            a['additional_artifacts'] = keep
    ip.write_text(json.dumps(index, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    register(article)
    index = json.loads(ip.read_text(encoding='utf-8'))
    for a in index['articles']:
        cs = (a.get('authority') or {}).get('current_state') or {}
        if cs.get('path') == pre + 'CURRENT-STATE.md':
            cs['sha256'] = hashlib.sha256((REPO / cs['path']).read_bytes()).hexdigest()
    ip.write_text(json.dumps(index, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    return gone


def commit(subject, paths):
    run(['git', 'add', '-A'] + paths)
    if run(['git', 'diff', '--cached', '--quiet'], check=False).returncode == 0:
        return False
    msg = subject
    trailers = os.environ.get('LANE_COMMIT_TRAILERS', '').strip()
    if trailers:
        msg += '\n\n' + trailers
    run(['git', 'commit', '-q', '-m', msg])
    return True


def preflight():
    """CI's checks with CI's bare Python, so a push that would fail there stops here. On 2026-10-22 a new test needed
    BeautifulSoup, which the workflow doesn't install; it passed here and failed only in CI.

    The checks run on the working tree, so a change to tools/, tests/ or scripts/ left out of the commit would pass here
    and fail in CI (2026-10-23: a test went in without the tool change it tests). Such a change stops the push."""
    left = run(['git', 'status', '--porcelain', '--', 'tools', 'tests', 'scripts']).stdout.strip()
    if left:
        sys.exit('not pushed: tools/, tests/ or scripts/ have changes the commit leaves out, which the checks would run '
                 'against:\n%s\nadd them with --add, or set them aside' % left)
    branch = run(['git', 'rev-parse', '--abbrev-ref', 'HEAD']).stdout.strip()
    base = next((b for b in ('origin/' + branch, 'origin/main')
                 if run(['git', 'rev-parse', '--verify', '-q', b], check=False).returncode == 0), None)
    changed = run(['git', 'diff', '--name-only', base, 'HEAD']).stdout.split() if base else ['tests/']
    py = [sys.executable, '-S']
    if any(p.startswith(('tests/', 'tools/', 'scripts/')) for p in changed):
        run(py + ['-m', 'unittest', 'discover', '-s', 'tests'], timeout=900)
    for cmd in (['scripts/validate_content_repository.py', '--root', '.'],
                ['scripts/validate_article_architecture_maps.py', '--root', '.'],
                ['scripts/audit_codex_github.py', '--root', '.', '--fail-on', 'error']):
        run(py + cmd, timeout=300)


def mergeable(tries=6):
    """The open pull request's state for this branch: GitHub works out mergeability after a push, so ask a few times."""
    branch = run(['git', 'rev-parse', '--abbrev-ref', 'HEAD']).stdout.strip()
    owner, repo = owner_repo()
    r = run(['gh', 'api', 'repos/%s/%s/pulls?state=open&head=%s:%s' % (owner, repo, owner, branch),
             '--jq', '.[0].number // empty'], check=False)
    num = r.stdout.strip()
    if not num:
        return 'no open pull request for ' + branch
    state = ''
    for i in range(tries):
        state = run(['gh', 'api', 'repos/%s/%s/pulls/%s' % (owner, repo, num), '--jq',
                     '(.mergeable|tostring) + " " + .mergeable_state + " " + .html_url'], check=False).stdout.strip()
        if state and not state.startswith('null'):
            break
        time.sleep(5)
    if state.startswith('false'):
        return 'pull request %s CANNOT MERGE (%s): merge origin/main into the branch and push again' % (num, state)
    return 'pull request %s: mergeable %s' % (num, state)


def owner_repo():
    url = run(['git', 'remote', 'get-url', 'origin']).stdout.strip()
    m = re.search(r'github\.com[:/]+([^/]+)/([^/]+?)(?:\.git)?/?$', url) or re.search(r'/([^/]+)/([^/]+?)(?:\.git)?/?$', url)
    return m.group(1), m.group(2)


def pull_request(title, body_file):
    branch = run(['git', 'rev-parse', '--abbrev-ref', 'HEAD']).stdout.strip()
    owner, repo = owner_repo()
    r = run(['gh', 'api', 'repos/%s/%s/pulls?state=open&head=%s:%s' % (owner, repo, owner, branch),
             '--jq', '.[] | (.number|tostring) + " " + .html_url'])
    if r.stdout.strip():
        return 'open already: ' + r.stdout.strip().split('\n')[0]
    r = run(['gh', 'api', 'repos/%s/%s/pulls' % (owner, repo), '-f', 'title=' + title, '-f', 'head=' + branch,
             '-f', 'base=main', '-F', 'body=@' + str(pathlib.Path(body_file).resolve()),
             '--jq', '(.number|tostring) + " " + .html_url'])
    return 'opened: ' + r.stdout.strip()


def parser():
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('subject')
    ap.add_argument('--article', default='inner-child-therapy')
    # 2026-10-23: with nargs='*' alone, a second --add replaced the first, so "--add TOOL --add TEST" committed the test
    # without the tool it tests; each --add now adds to the list
    ap.add_argument('--add', nargs='*', action='extend', default=[], help='more paths to stage (tools, tests, docs)')
    ap.add_argument('--pr', help='open a pull request with this title when none is open for the branch')
    ap.add_argument('--pr-body', help='the pull request body (a file)')
    return ap


def main(argv=None):
    ap = parser()
    a = ap.parse_args(argv)
    if a.pr and not a.pr_body:
        ap.error('--pr needs --pr-body')
    paths = ['articles/%s' % a.article, 'articles/INDEX.json'] + a.add
    register(a.article)
    made = commit(a.subject, paths)
    gone = prune(a.article)
    fixed = commit('INDEX hash', paths)
    preflight()
    r = run(['git', 'push', '-q', 'origin', 'HEAD'], timeout=600)
    head = run(['git', 'rev-parse', 'HEAD']).stdout.strip()
    print('pushed %s (%s%s%s)' % (head, 'committed' if made else 'nothing new to commit',
                                   ', %d gone from the index' % gone if gone else '', ', index hash commit' if fixed else ''))
    if r.stderr.strip():
        print(r.stderr.strip()[-1500:])
    if a.pr:
        print('pull request', pull_request(a.pr, a.pr_body))
    print(mergeable())
    return 0


if __name__ == '__main__':
    sys.exit(main())
