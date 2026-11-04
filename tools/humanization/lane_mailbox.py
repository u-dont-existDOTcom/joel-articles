#!/usr/bin/env python3
"""lane_mailbox.py - the record of each turn's mailbox check, and the check lane_push.py runs before it pushes.

Joel asked on 2026-10-31 that every lane look at what is addressed to it in every turn, "like checking ur mailbox"
(universal-dev-architecture, docs/requirements/2026-10-31-lane-mailbox-every-turn.owner-requirement.json; its item for this
repository, suggested-fixes/joel-articles/2026-10-31-mailbox-every-turn.md, adopted here on 2026-11-01). The places, as
AGENTS.md ("Suggested fixes from other projects") names them:
  uda-lane   this repository's lane in universal-dev-architecture, suggested-fixes/joel-articles/ on its default branch
             (no folder means no items), against docs/suggested-fixes-ledger.md;
  repo       new issues and pull requests in this repository, and new comments and reviews on any of them, including
             replies on the lane's own;
  notes      edits others made to the lane's handoff notes and owner questions pages since its last turn;
  runtime    the messages the session's runtime queued for it (notifications).
Each place is either read, with what was there, or unreachable, with what failed and when it will be tried again (a
place that can't be read never stops a turn). Each new item gets an outcome or a next step.

  python3 tools/humanization/lane_mailbox.py record --turn "2026-11-01 22:27" --lines "hypnosis guide" "community article" \\
      --read uda-lane "1 new item: 2026-10-31-mailbox-every-turn.md" --read repo "no new issues, comments or reviews" \\
      --read notes "..." --read runtime "no queued notifications" \\
      --item "2026-10-31-mailbox-every-turn.md" "adopted: AGENTS.md section replaced, this tool, lane_push.py checks it"
  python3 tools/humanization/lane_mailbox.py record --turn T ... --unreachable repo "GitHub API 502" "first thing next turn"
  python3 tools/humanization/lane_mailbox.py check --turn "2026-11-01 22:27"     # exit 0, or 2 with what is missing

The record is the lane's own file, state/mailbox/<branch>.json (newest check last; the branch's name with "/" as "-").
Until 2026-11-04 every lane wrote one shared state/MAILBOX.json, so every lane's open pull request conflicted with main
whenever another lane's merged first (Joel, 2026-11-04 13:53 UTC: "290 has conflicts", the third time that day); that file
stays as the history, and a check recorded there still counts. lane_push.py refuses to push without --mailbox TURN naming
a complete check of this turn: the turn's first clock reading, the same one the final answer's stamp starts from.
"""
import argparse
import datetime
import json
import os
import pathlib
import re
import subprocess
import sys

REPO = pathlib.Path(__file__).resolve().parents[2]
LEGACY = REPO / 'state' / 'MAILBOX.json'     # every lane's checks until 2026-11-04; read, never written
LANES = REPO / 'state' / 'mailbox'


def lane_record(where=REPO):
    """This lane's own record, state/mailbox/<branch>.json; the shared file when no branch is checked out. Git runs without
    the caller's GIT_* variables (inside a hook GIT_DIR would name the repository being pushed)."""
    env = {k: v for k, v in os.environ.items() if not k.startswith('GIT_')}
    try:
        b = subprocess.run(['git', '-C', str(where), 'branch', '--show-current'], capture_output=True, text=True,
                           timeout=20, env=env).stdout.strip()
    except (OSError, subprocess.SubprocessError):
        b = ''
    slug = re.sub(r'[^A-Za-z0-9._-]+', '-', b).strip('-')
    return LANES / (slug + '.json') if slug else LEGACY


RECORD = LEGACY
PLACES = {
    'uda-lane': 'this repository\'s lane in universal-dev-architecture (suggested-fixes/joel-articles/), against '
                'docs/suggested-fixes-ledger.md',
    'repo': 'new issues and pull requests here, and new comments and reviews on any of them, replies on our own '
            'included',
    'notes': 'edits others made to the lane\'s handoff notes and owner questions pages since its last turn',
    'runtime': 'the messages the session\'s runtime queued for it',
}


def turn_key(s):
    """A turn's first clock reading, as a minute in UTC ('2026-11-01T22:27Z'); accepts '2026-11-01 22:27',
    '2026-11-01T22:27:00Z' and the like."""
    m = re.match(r'^\s*(\d{4}-\d{2}-\d{2})[ T](\d{2}):(\d{2})', s or '')
    if not m:
        raise ValueError('a turn is its first clock reading, like "2026-11-01 22:27" (UTC): %r' % s)
    return '%sT%s:%sZ' % m.groups()


def load(path=None):
    path = path or lane_record()
    if path.exists():
        return json.loads(path.read_text(encoding='utf-8'))
    return {'about': 'Each turn\'s mailbox check (tools/humanization/lane_mailbox.py; AGENTS.md, "Suggested fixes from other '
                     'projects"). Newest last.', 'places': PLACES, 'checks': []}


def problems(entry):
    """What a check of a turn lacks: a place neither read nor recorded as unreachable with a retry, or an item without
    an outcome or next step."""
    out = []
    got = {p['place']: p for p in entry.get('places', [])}
    for k in PLACES:
        p = got.get(k)
        if not p:
            out.append('%s: not checked (%s)' % (k, PLACES[k]))
        elif p.get('status') == 'read' and not (p.get('found') or '').strip():
            out.append('%s: read, but what was there is not recorded' % k)
        elif p.get('status') == 'unreachable' and not ((p.get('failed') or '').strip() and (p.get('retry') or '').strip()):
            out.append('%s: unreachable needs what failed and when it will be tried again' % k)
        elif p.get('status') not in ('read', 'unreachable'):
            out.append('%s: status must be read or unreachable' % k)
    for it in entry.get('items', []):
        if not (it.get('outcome') or '').strip():
            out.append('item %s: no outcome or next step' % it.get('item'))
    return out


def find(record, turn):
    k = turn_key(turn)
    hits = [c for c in record.get('checks', []) if c.get('turn') == k]
    return hits[-1] if hits else None


def check(turn, path=None):
    """[] when this turn's mailbox check is recorded and complete; else what is missing. Without PATH: the lane's own
    record, then the shared one of before 2026-11-04."""
    entry = find(load(path), turn)
    if not entry and path is None and lane_record() != LEGACY:
        entry = find(load(LEGACY), turn)
    if not entry:
        return ['no mailbox check is recorded for the turn that started %s: check the places in AGENTS.md ("Suggested '
                'fixes from other projects") and record them with tools/humanization/lane_mailbox.py record'
                % turn_key(turn)]
    return problems(entry)


def record(turn, lines, read, unreachable, items, path=None):
    path = path or lane_record()
    rec = load(path)
    k = turn_key(turn)
    places = [{'place': p, 'status': 'read', 'found': f} for p, f in read]
    places += [{'place': p, 'status': 'unreachable', 'failed': f, 'retry': r} for p, f, r in unreachable]
    bad = [p['place'] for p in places if p['place'] not in PLACES]
    if bad:
        raise ValueError('unknown places %s; the places are %s' % (bad, ', '.join(PLACES)))
    entry = {'turn': k, 'lines_of_work': lines, 'places': places,
             'items': [{'item': i, 'outcome': o} for i, o in items],
             'recorded_utc': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%MZ')}
    rec['checks'] = [c for c in rec.get('checks', []) if c.get('turn') != k] + [entry]
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(rec, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    return problems(entry)


def start_of_turn():
    """What a lane does next, right after its mailbox (gate E339): the pre-push hook installed if this clone lacks it, and
    whether origin/main is merged. Nothing here stops the record; lane_push.py refuses the push if main isn't merged."""
    out = []
    try:
        sys.path.insert(0, str(REPO / 'tools' / 'humanization'))
        import lane_push as lp
        done = lp.install_hook()
        if done:
            out.append(done)
        f = lp.run(['git', 'fetch', '-q', 'origin', 'main'], check=False, timeout=180)
        if f.returncode:
            out.append('main: not fetched (%s); merge it before other work once it can be' % f.stderr.strip()[-200:])
        elif lp.run(['git', 'merge-base', '--is-ancestor', 'origin/main', 'HEAD'], check=False).returncode:
            n = len([x for x in lp.run(['git', 'log', '--oneline', 'HEAD..origin/main'], check=False).stdout.split('\n') if x])
            files = lp.shared(lp.run(['git', 'diff', '--name-only', 'HEAD...origin/main'], check=False).stdout.split())
            out.append('main: %d commit(s) not merged here. Merge origin/main now, before other work (gate E339), and read '
                       'what it changed in the shared files: %s' % (n, ', '.join(files) or 'none'))
        else:
            out.append('main: merged')
    except Exception as e:   # a lane's record never fails on this
        out.append('main: not checked (%s)' % e)
    return out


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    sub = ap.add_subparsers(dest='cmd', required=True)
    r = sub.add_parser('record')
    r.add_argument('--turn', required=True)
    r.add_argument('--lines', nargs='*', default=[], help='the lines of work this turn covers')
    r.add_argument('--read', nargs=2, action='append', default=[], metavar=('PLACE', 'WHAT_WAS_THERE'))
    r.add_argument('--unreachable', nargs=3, action='append', default=[], metavar=('PLACE', 'WHAT_FAILED', 'RETRY'))
    r.add_argument('--item', nargs=2, action='append', default=[], metavar=('ITEM', 'OUTCOME_OR_NEXT_STEP'))
    c = sub.add_parser('check')
    c.add_argument('--turn', required=True)
    a = ap.parse_args(argv)
    probs = (record(a.turn, a.lines, a.read, a.unreachable, a.item) if a.cmd == 'record' else check(a.turn))
    if a.cmd == 'record':
        for line in start_of_turn():
            print(line)
    for p in probs:
        print('missing:', p)
    if probs:
        return 2
    print('mailbox check of %s: complete' % turn_key(a.turn))
    return 0


if __name__ == '__main__':
    sys.exit(main())
