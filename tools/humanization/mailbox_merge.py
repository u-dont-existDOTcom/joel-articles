#!/usr/bin/env python3
"""mailbox_merge.py - git's merge driver for state/MAILBOX.json: every lane's mailbox records, from both sides, kept once.

Every lane records each turn's mailbox check at the end of state/MAILBOX.json (lane_mailbox.py record), so every merge of
main into a lane, and of a lane into main, conflicted there: the gut lane resolved it by hand three times on 2026-11-04
alone. The records are append-only and never edited, so the merge is their union: the base's records in order, then each
side's new ones once, by the time they were recorded. A change to the file's header ("about", "places") is a real
conflict: the driver leaves it to a person (exit 1).

  git config merge.lane-mailbox.driver "python3 tools/humanization/mailbox_merge.py %O %A %B"
  (.gitattributes: state/MAILBOX.json merge=lane-mailbox; lane_push.py and lane_mailbox.py set the config in each clone)
"""
import json, pathlib, sys


def merge(base, ours, theirs):
    """The merged mailbox, or None when the headers differ."""
    head = lambda m: {k: v for k, v in m.items() if k != 'checks'}
    if head(ours) != head(theirs):
        return None
    key = lambda c: json.dumps(c, sort_keys=True, ensure_ascii=False)
    have = {key(c) for c in base.get('checks', [])}
    seen, new = set(have), []
    for c in ours.get('checks', []) + theirs.get('checks', []):
        k = key(c)
        if k not in seen:
            seen.add(k)
            new.append(c)
    out = dict(ours)
    out['checks'] = list(base.get('checks', [])) + sorted(new, key=lambda c: c.get('recorded_utc', ''))
    # a record one side dropped from the base stays dropped
    gone = have - {key(c) for c in ours.get('checks', [])} | (have - {key(c) for c in theirs.get('checks', [])})
    out['checks'] = [c for c in out['checks'] if key(c) not in gone]
    return out


def main(argv=None):
    o, a, b = (argv or sys.argv[1:])[:3]
    read = lambda p: json.loads(pathlib.Path(p).read_text(encoding='utf-8')) if pathlib.Path(p).stat().st_size else {}
    m = merge(read(o), read(a), read(b))
    if m is None:
        print('mailbox_merge: the headers differ; merge state/MAILBOX.json by hand', file=sys.stderr)
        return 1
    pathlib.Path(a).write_text(json.dumps(m, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    return 0


if __name__ == '__main__':
    sys.exit(main())
