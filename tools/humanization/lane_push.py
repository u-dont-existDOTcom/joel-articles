#!/usr/bin/env python3
"""Push the lane in one step (turn 76; Joel, 2026-10-19 00:55 UTC: "it took you 14m to put one line in... def need
to fix that right?").

  python3 tools/humanization/lane_push.py "Commit subject" --mailbox "2026-11-01 22:27" [--article inner-child-therapy]
                                           [--add PATH ...] [--pr "Pull request title" --pr-body FILE] [--unread-ok "why"]

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

Before any of that, the mailbox (AGENTS.md, "Suggested fixes from other projects"; Joel, 2026-10-31: "can we make sure
you always check what is addressed to you in each turn? like checking ur mailbox? every lane should have its mailbox
checked right"): --mailbox names the turn by its first clock reading, and tools/humanization/lane_mailbox.py must have a
complete check of that turn on record (every place read, or unreachable with what failed and when it will be retried, and
every new item with an outcome or a next step). Without it nothing is committed or pushed. A place that can't be read
never stops a push once it is recorded that way.

Then the comparison gate (gate E284): for every COMPARE-GATE.json in the article's folder, every paragraph
of the article must be his as published, his own words, or read beside his text by a comparative read at its present
words, and every finding of severity 2 or 3 still in it needs a fate (tools/humanization/compare_read.py gate). On a
failure nothing is committed or pushed, unless --unread-ok "reason" is given; the reason goes into the commit message.
Joel, 2026-10-28 16:05 UTC, after the hypnosis guide had become "too incomprehensible" through rewrites nobody read
beside his text: "let's repair the process durably so that can't happen again also". An article with a lane folder of
rewritten text (a HUMANIZED-*.md) and no COMPARE-GATE.json gets a warning.

Then the lane's integration with main (gate E339; Joel, 2026-11-03 22:02 UTC: "i want to make sure each lane is feeding
into and reading from the same place so i don't duplicate work", and 2026-11-04 00:37 UTC: "make sure no other lane can
make the same mistake you made next time"). The gut lane had branched from main, never merged it again, pushed with
plain `git push`, opened no pull request, and changed a shared test that the bad-trips lane's open pull request had
changed the same day. So, before anything is committed:
  - main must be merged: `origin/main` (fetched now) has to be in HEAD's history, or nothing is pushed;
  - the branch needs a pull request: one open already, or --pr TITLE --pr-body FILE to open it;
  - a shared file this branch changes (tools/, docs/, tests/, scripts/, .github/, AGENTS.md, SKILL.md) that another
    open pull request also changes stops the push until --overlap-ok "how this builds on theirs" says how the two fit
    (read their change first: gh api repos/OWNER/REPO/pulls/N/files);
  - the pre-push hook is installed if it isn't (tools/humanization/git-hooks/pre-push), and the push carries
    LANE_PUSH=1, so a plain `git push` from a lane is refused by the hook.
A place GitHub can't be reached for prints what failed and doesn't stop the push (as the mailbox does).

Lessons go to main the turn they are made (Joel, 2026-11-05 15:15 UTC: "make sure you merge lessons with main branch so
everyone is sharing always"). A lesson that waits in an open pull request is shared with nobody: the bad trips lane's
E360, E361, docs/MAKING-SENSE.md and O68 sat in its pull request #280 for a day while other lanes worked without them. So
a branch that changes a shared file against main (tools/, docs/, tests/, scripts/, .github/, AGENTS.md, SKILL.md) is
pushed with --merge: after the push, once its pull request's checks on the pushed commit have finished green, it is
merged into main (a merge commit, as Joel merges), and every lane takes it at its next turn's merge of main (E339).
--no-merge "why" pushes without merging, for a change that must wait (its tests fail, or it needs Joel's decision); the
reason is printed and goes in the commit message. A branch with no shared change needs neither: article work waits for
Joel's merge as before.

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


def compare_gate(article, unread_ok=None):
    """Run every COMPARE-GATE.json of ARTICLE's folder (compare_read.py gate); stop on a failure unless UNREAD_OK gives a
    reason. Returns the note for the commit message, or ''."""
    folder = REPO / 'articles' / article
    configs = sorted(folder.rglob('COMPARE-GATE.json'))
    if not configs:
        if any(folder.rglob('HUMANIZED-*.md')):
            print('warning: articles/%s has rewritten text (HUMANIZED-*.md) and no COMPARE-GATE.json, so nothing checks '
                  'that every rewritten paragraph was read beside his text (docs/FIXING-AN-ARTICLE.md section 5)' % article)
        return ''
    failed = []
    for c in configs:
        r = run([sys.executable, 'tools/humanization/compare_read.py', 'gate', '--config', str(c.relative_to(REPO))],
                check=False, timeout=300)
        print(r.stdout.strip()[-3000:])
        if r.returncode:
            failed.append(str(c.relative_to(REPO)))
    if failed and not unread_ok:
        sys.exit('not committed or pushed: the comparison gate failed for %s. Read the unread paragraphs beside his text '
                 '(compare_read.py) and give every open finding a fate, or push anyway with --unread-ok "why"'
                 % ', '.join(failed))
    return ('Unread-ok (the comparison gate failed for %s): %s' % (', '.join(failed), unread_ok)) if failed else ''


def commit(subject, paths, note=''):
    run(['git', 'add', '-A'] + paths)
    if run(['git', 'diff', '--cached', '--quiet'], check=False).returncode == 0:
        return False
    msg = subject + ('\n\n' + note if note else '')
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


SHARED_PREFIXES = ('tools/', 'docs/', 'tests/', 'scripts/', '.github/')
SHARED_FILES = ('AGENTS.md', 'SKILL.md')
NOT_SHARED = ('state/MAILBOX.json', 'articles/INDEX.json')   # every lane writes these; their merges are mechanical
HOOK = REPO / 'tools' / 'humanization' / 'git-hooks' / 'pre-push'


def shared(paths):
    """The paths every lane reads from: the shared rules and tools, not an article's own folder."""
    return sorted({p for p in paths if p not in NOT_SHARED and (p.startswith(SHARED_PREFIXES) or p in SHARED_FILES)})


def overlaps(mine, others):
    """{pr number: [shared files both change]} for the other open pull requests; others is {number: (branch, files)}."""
    mine = set(shared(mine))
    out = {}
    for num, (_, files) in sorted(others.items()):
        both = sorted(mine & set(shared(files)))
        if both:
            out[num] = both
    return out


MAILBOX_DRIVER = 'python3 tools/humanization/mailbox_merge.py %O %A %B'


def install_merge_driver():
    """The mailbox's merge driver in this clone's config (.gitattributes names it): every lane appends to
    state/MAILBOX.json, and every merge conflicted there until 2026-11-04. Returns what was done, or ''."""
    have = run(['git', 'config', '--get', 'merge.lane-mailbox.driver'], check=False).stdout.strip()
    if have == MAILBOX_DRIVER:
        return ''
    run(['git', 'config', 'merge.lane-mailbox.name', 'the union of the lanes\' mailbox records'], check=False)
    run(['git', 'config', 'merge.lane-mailbox.driver', MAILBOX_DRIVER], check=False)
    return 'set the mailbox merge driver (tools/humanization/mailbox_merge.py)'


def install_hook():
    """The pre-push hook and the mailbox merge driver, set in this clone when they aren't. Returns what was done, or ''."""
    return '; '.join(x for x in (link_hook(), install_merge_driver()) if x)


def link_hook():
    """The pre-push hook, linked into this clone's hooks folder when it isn't there (E158 asked for it once per clone,
    and the gut lane's clone never had it, 2026-11-03). Returns what was done, or ''."""
    gd = run(['git', 'rev-parse', '--git-common-dir'], check=False).stdout.strip()
    if not gd:
        return ''
    hooks = (REPO / gd if not pathlib.Path(gd).is_absolute() else pathlib.Path(gd)) / 'hooks'
    target = hooks / 'pre-push'
    if target.exists() and target.resolve() == HOOK.resolve():
        return ''
    hooks.mkdir(parents=True, exist_ok=True)
    if target.exists() or target.is_symlink():
        target.rename(target.with_name('pre-push.before-lane-push'))
    target.symlink_to(HOOK.resolve())
    return 'installed the pre-push hook in %s' % hooks


def main_gate():
    """Refuse unless origin/main, fetched now, is merged into HEAD. Returns a warning when main can't be fetched.
    The fetch names its destination: a clone whose fetch refspec covers only its lane branch (the Inner Child lane's
    laptop clone, 2026-11-04) took "git fetch origin main" into FETCH_HEAD alone and kept an origin/main weeks old, so
    this gate passed against that old main and the overlap check counted every shared file main had changed since as
    this branch's own (pull requests #109 and #280, neither touched by the branch)."""
    f = run(['git', 'fetch', '-q', 'origin', '+refs/heads/main:refs/remotes/origin/main'], check=False, timeout=180)
    if f.returncode:
        return 'warning: origin/main could not be fetched (%s); main is checked again on the next push' % f.stderr.strip()[-200:]
    if run(['git', 'merge-base', '--is-ancestor', 'origin/main', 'HEAD'], check=False).returncode == 0:
        return ''
    behind = run(['git', 'log', '--oneline', 'HEAD..origin/main'], check=False).stdout.strip().split('\n')
    files = shared(run(['git', 'diff', '--name-only', 'HEAD...origin/main'], check=False).stdout.split())
    sys.exit('refused: main has %d commit(s) this branch doesn\'t (gate E339). Merge it first, before any other work:\n'
             '  git merge origin/main\nthen read what it changed in the shared rules and tools%s' % (
                 len(behind), (':\n  ' + '\n  '.join(files)) if files else ' (none this time)'))


def pull_files(owner, repo, num):
    """The files an open pull request changes, or None when they can't be read. Pages are fetched by number:
    `gh api --paginate` follows GitHub's next-page links, which name the repository by its numeric id, and the session
    proxy refuses those (2026-11-04: pull requests 199 and 200, over 100 files each, blinded the whole check)."""
    files = []
    for page in range(1, 31):  # GitHub lists at most 3000 files for a pull request
        f = run(['gh', 'api', 'repos/%s/%s/pulls/%s/files?per_page=100&page=%d' % (owner, repo, num, page),
                 '--jq', '.[].filename'], check=False)
        if f.returncode:
            return None
        got = f.stdout.split()
        files += got
        if len(got) < 100:
            break
    return files


def open_pulls():
    """{number: (branch, files)} for every open pull request, or None when the list can't be read. A pull request whose
    files can't be read has files None, and the gate names it rather than going blind to the others."""
    owner, repo = owner_repo()
    r = run(['gh', 'api', 'repos/%s/%s/pulls?state=open&per_page=100' % (owner, repo), '--jq',
             '.[] | (.number|tostring) + " " + .head.ref'], check=False)
    if r.returncode:
        return None
    out = {}
    for line in r.stdout.strip().split('\n'):
        if not line.strip():
            continue
        num, branch = line.split(' ', 1)
        out[int(num)] = (branch, pull_files(owner, repo, num))
    return out


def integration_gate(a, extra_paths=()):
    """Main merged, a pull request for the branch, and no shared file changed beside another lane's open change."""
    notes = []
    w = main_gate()
    if w:
        notes.append(w)
    branch = run(['git', 'rev-parse', '--abbrev-ref', 'HEAD']).stdout.strip()
    pulls = open_pulls()
    if pulls is None:
        notes.append('warning: the open pull requests could not be read; their overlap and this branch\'s own pull request '
                     'are checked again on the next push')
        return notes
    mine_open = [n for n, (b, _) in pulls.items() if b == branch]
    if not mine_open and not a.pr:
        sys.exit('refused: %s has no open pull request (gate E339). A lane\'s pull request is how its shared changes reach '
                 'main and the other lanes: push with --pr "TITLE" --pr-body FILE.' % branch)
    changed = run(['git', 'diff', '--name-only', 'origin/main...HEAD'], check=False).stdout.split()
    changed += run(['git', 'diff', '--name-only', 'HEAD'], check=False).stdout.split() + list(extra_paths)
    others = {n: v for n, v in pulls.items() if v[0] != branch and v[1] is not None}
    unread = sorted(n for n, v in pulls.items() if v[0] != branch and v[1] is None)
    if unread and shared(changed):
        notes.append('warning: the files of open pull request(s) %s could not be read, so their overlap with this push\'s '
                     'shared files is checked again on the next push' % ', '.join('#%d' % n for n in unread))
    both = overlaps(changed, others)
    # the reason names each pull request it answers for: a reason written for #280 said nothing about #285, which
    # opened an hour later on the same file, and the push went through on it (2026-11-04)
    named = set(int(n) for n in re.findall(r'#(\d+)', a.overlap_ok or ''))
    missing = [n for n in both if n not in named]
    if missing:
        sys.exit('refused: other open pull requests change the same shared files (gate E339). Read each one\'s change, build '
                 'on it rather than beside it, then push with --overlap-ok "how this builds on theirs", naming each one '
                 '(#N) it answers for%s:\n  ' % (' (not named yet: %s)' % ', '.join('#%d' % n for n in missing)
                                                  if a.overlap_ok else '') +
                 '\n  '.join('#%d (%s): %s' % (n, others[n][0], ', '.join(f)) for n, f in both.items() if n in missing))
    if both:
        notes.append('shared files also changed by open pull requests %s: %s' % (
            ', '.join('#%d' % n for n in both), a.overlap_ok))
    return notes


def parser():
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('subject')
    ap.add_argument('--article', default='inner-child-therapy')
    # 2026-10-23: with nargs='*' alone, a second --add replaced the first, so "--add TOOL --add TEST" committed the test
    # without the tool it tests; each --add now adds to the list
    ap.add_argument('--add', nargs='*', action='extend', default=[], help='more paths to stage (tools, tests, docs)')
    ap.add_argument('--pr', help='open a pull request with this title when none is open for the branch')
    ap.add_argument('--pr-body', help='the pull request body (a file)')
    ap.add_argument('--unread-ok', help='push although the comparison gate fails, and say why in the commit message')
    ap.add_argument('--overlap-ok', help='another open pull request changes a shared file this one does: say how this '
                                          'builds on theirs (gate E339)')
    ap.add_argument('--merge', action='store_true',
                    help='merge the pull request into main once its checks pass: required when the branch changes shared '
                         'rules or tools, so every lane has them at its next turn (Joel, 2026-11-05)')
    ap.add_argument('--no-merge', help='push a branch with shared changes without merging it: why it must wait')
    ap.add_argument('--mailbox', metavar='TURN',
                    help='the turn\'s first clock reading ("2026-11-01 22:27", UTC): its mailbox check must be on record '
                         '(tools/humanization/lane_mailbox.py record); required')
    return ap


def mailbox_gate(turn):
    """Stop unless this turn's mailbox check is recorded and complete (tools/humanization/lane_mailbox.py)."""
    sys.path.insert(0, str(REPO / 'tools' / 'humanization'))
    import lane_mailbox as mb
    if not turn:
        sys.exit('refused: --mailbox "<the turn\'s first clock reading, UTC>" is required. Check the mailbox first '
                 '(AGENTS.md, "Suggested fixes from other projects": the lane in universal-dev-architecture, issues, pull '
                 'requests, comments and reviews here, edits others made to the handoff notes and questions pages, and the '
                 'runtime\'s queued messages), record it with tools/humanization/lane_mailbox.py record, then push again.')
    try:
        probs = mb.check(turn)
    except ValueError as e:
        sys.exit('refused: %s' % e)
    if probs:
        sys.exit('refused: the mailbox check of this turn is not complete:\n  ' + '\n  '.join(probs))


def shared_changes():
    """The shared files this branch changes against origin/main (fetched by main_gate)."""
    return shared(run(['git', 'diff', '--name-only', 'origin/main...HEAD'], check=False).stdout.split())


def merge_gate(a, pending):
    """Refuse a push of shared changes that says neither --merge nor --no-merge (Joel, 2026-11-05: "make sure you merge
    lessons with main branch so everyone is sharing always")."""
    if pending and not (a.merge or a.no_merge):
        sys.exit('refused: this branch changes shared rules or tools (%s), and lessons go to main the turn they are made '
                 '(Joel, 2026-11-05 15:15 UTC: "make sure you merge lessons with main branch so everyone is sharing '
                 'always"). Push again with --merge, or with --no-merge "why it must wait".' % ', '.join(pending[:6]))
    if a.merge and a.no_merge:
        sys.exit('refused: --merge and --no-merge together')


def merge_now(wait=600):
    """Merge the branch's open pull request into main once the check runs on the pushed commit have all finished
    green. Returns what happened."""
    branch = run(['git', 'rev-parse', '--abbrev-ref', 'HEAD']).stdout.strip()
    head = run(['git', 'rev-parse', 'HEAD']).stdout.strip()
    owner, repo = owner_repo()
    num = run(['gh', 'api', 'repos/%s/%s/pulls?state=open&head=%s:%s' % (owner, repo, owner, branch),
               '--jq', '.[0].number // empty'], check=False).stdout.strip()
    if not num:
        return 'NOT MERGED: no open pull request for %s (open one with --pr)' % branch
    end = time.time() + wait
    runs = []
    while time.time() < end:
        r = run(['gh', 'api', 'repos/%s/%s/commits/%s/check-runs' % (owner, repo, head), '--jq',
                 '.check_runs[] | .name + "\t" + .status + "\t" + (.conclusion // "")'], check=False)
        runs = [x.split('\t') for x in r.stdout.strip().split('\n') if x.strip()]
        if runs and all(x[1] == 'completed' for x in runs):
            break
        time.sleep(15)
    bad = [x for x in runs if x[1] != 'completed' or x[2] not in ('success', 'neutral', 'skipped')]
    if not runs:
        return 'NOT MERGED: no checks ran on %s within %ds; merge it once they have: pull request %s' % (head[:8], wait, num)
    if bad:
        return 'NOT MERGED: checks not green on %s (%s): pull request %s waits' % (
            head[:8], '; '.join('%s %s %s' % tuple(x[:3]) for x in bad), num)
    r = run(['gh', 'api', '-X', 'PUT', 'repos/%s/%s/pulls/%s/merge' % (owner, repo, num), '-f', 'merge_method=merge',
             '-f', 'sha=' + head, '--jq', '.sha'], check=False)
    if r.returncode:
        return 'NOT MERGED: GitHub refused the merge of pull request %s: %s' % (num, (r.stderr or r.stdout).strip()[-300:])
    return 'merged pull request %s into main (%s): every lane takes it at its next merge of main' % (num, r.stdout.strip()[:12])


def main(argv=None):
    ap = parser()
    a = ap.parse_args(argv)
    if a.pr and not a.pr_body:
        ap.error('--pr needs --pr-body')
    sys.path.insert(0, str(REPO / 'tools' / 'humanization'))
    import lane_mailbox as mb
    own = mb.lane_record()          # the lane's own mailbox file (state/mailbox/<branch>.json), so lanes don't conflict
    moved = mb.settle()             # and the shared history file exactly as main has it (Joel, 2026-11-04 14:28 UTC)
    if moved:
        print('mailbox: %s moved from state/MAILBOX.json to %s' % (', '.join(moved), own.relative_to(REPO)))
    paths = ['articles/%s' % a.article, 'articles/INDEX.json', 'state/MAILBOX.json'] + \
        ([str(own.relative_to(REPO))] if own != mb.LEGACY and own.exists() else []) + a.add
    mailbox_gate(a.mailbox)
    for line in [install_hook()] + integration_gate(a, a.add):
        if line:
            print(line)
    pending = sorted(set(shared_changes()) | set(shared(a.add)))
    merge_gate(a, pending)
    note = compare_gate(a.article, a.unread_ok)
    if pending and a.no_merge:
        note = ((note + '\n\n') if note else '') + 'Shared changes not merged into main this turn: ' + a.no_merge
    register(a.article)
    made = commit(a.subject, paths, note)
    gone = prune(a.article)
    fixed = commit('INDEX hash', paths)
    preflight()
    os.environ['LANE_PUSH'] = '1'   # the pre-push hook refuses a lane's push that doesn't come through here (E339)
    r = run(['git', 'push', '-q', 'origin', 'HEAD'], timeout=600)
    head = run(['git', 'rev-parse', 'HEAD']).stdout.strip()
    print('pushed %s (%s%s%s)' % (head, 'committed' if made else 'nothing new to commit',
                                   ', %d gone from the index' % gone if gone else '', ', index hash commit' if fixed else ''))
    if r.stderr.strip():
        print(r.stderr.strip()[-1500:])
    if a.pr:
        print('pull request', pull_request(a.pr, a.pr_body))
    print(mergeable())
    if a.merge:
        print(merge_now())
    elif pending:
        print('shared changes NOT merged into main: %s' % a.no_merge)
    return 0


if __name__ == '__main__':
    sys.exit(main())
