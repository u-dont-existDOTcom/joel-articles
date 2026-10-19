#!/usr/bin/env python3
"""Apply a turn's update to a handoff note in one step (turn 76). It runs on Joel's laptop, from the lane clone,
with Python's standard library only, so the note's update is one fixed command:

  cd ~/ai-work/claude-dangerous-lane/joel-articles && git fetch -q origin BRANCH && \
    git show FETCH_HEAD:tools/humanization/handoff_note.py | python3 - --rev FETCH_HEAD \
      --update articles/inner-child-therapy/HANDOFF-UPDATE.json \
      --note ~/claude-acceptance-transfer/handoffs/inner-child-article.md

The update is JSON:
  "replace":       [[regex, replacement, count], ...]   each regex must match exactly COUNT times (default 1)
  "insert_before": [[line_prefix, text], ...]           TEXT goes before the first line that starts with LINE_PREFIX,
                                                        unless the note already has TEXT's first line (a rerun)
  "sections":      {"## Heading": "new body", ...}      the body under that heading, to the next "## " heading
Nothing is written unless every step applies. Without --rev, --update is read as a file.
"""
import argparse
import json
import pathlib
import re
import subprocess
import sys


def apply(note, upd):
    done = []
    for item in upd.get('replace', []):
        pat, new = item[0], item[1]
        want = item[2] if len(item) > 2 else 1
        n = len(re.findall(pat, note, flags=re.M))
        if n != want:
            raise SystemExit('replace: %d matches (wanted %d) for %r' % (n, want, pat[:90]))
        note = re.sub(pat, lambda m: new, note, flags=re.M)
        done.append('replaced %r' % pat[:60])
    for prefix, text in upd.get('insert_before', []):
        first = text.split('\n')[0]
        if first in note:
            done.append('already there: %r' % first[:60])
            continue
        lines = note.split('\n')
        i = next((k for k, l in enumerate(lines) if l.startswith(prefix)), None)
        if i is None:
            raise SystemExit('insert_before: no line starts with %r' % prefix)
        note = '\n'.join(lines[:i] + text.rstrip('\n').split('\n') + lines[i:])
        done.append('inserted before %r' % prefix[:40])
    for heading, body in upd.get('sections', {}).items():
        lines = note.split('\n')
        if lines.count(heading) != 1:
            raise SystemExit('section: %d lines are %r' % (lines.count(heading), heading))
        i = lines.index(heading)
        j = next((k for k in range(i + 1, len(lines)) if lines[k].startswith('## ')), len(lines))
        tail = [''] if j < len(lines) else []
        note = '\n'.join(lines[:i + 1] + body.rstrip('\n').split('\n') + tail + lines[j:])
        done.append('section %r' % heading)
    return note, done


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('--update', required=True)
    ap.add_argument('--note', required=True)
    ap.add_argument('--rev', help='read --update from this git revision of the current repository')
    a = ap.parse_args(argv)
    if a.rev:
        raw = subprocess.run(['git', 'show', '%s:%s' % (a.rev, a.update)], capture_output=True, text=True, check=True).stdout
    else:
        raw = pathlib.Path(a.update).read_text(encoding='utf-8')
    upd = json.loads(raw)
    p = pathlib.Path(a.note).expanduser()
    note, done = apply(p.read_text(encoding='utf-8'), upd)
    p.write_text(note, encoding='utf-8')
    print('handoff note updated (%s): %s' % (upd.get('turn', '?'), '; '.join(done)))
    return 0


if __name__ == '__main__':
    sys.exit(main())
