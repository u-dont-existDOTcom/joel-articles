#!/usr/bin/env python3
"""Set an article's CURRENT-STATE.md checkpoint for a turn: its date and turn number, In progress, Next step and
Waiting on Joel (turn 76; replaces the scratch state71.py, which kept writing the date 2026-10-18).

  python3 tools/humanization/lane_state.py TURN DATE "<in progress>" "<next step>" "<waiting on Joel>"
                                            [--article inner-child-therapy] [--file PATH]

DATE is the turn's date, his message's (YYYY-MM-DD). lane_push.py registers the file and fixes its hash.
"""
import argparse
import pathlib
import re
import sys

REPO = pathlib.Path(__file__).resolve().parents[2]
FIELDS = ('In progress', 'Next step (updated on every push, so another account can pick up here)', 'Waiting on Joel')


def set_state(text, turn, date, values):
    assert re.fullmatch(r'\d{4}-\d\d-\d\d', date), date
    text, n1 = re.subn(r'Updated: \d{4}-\d\d-\d\d \(turn \d+\)\.', 'Updated: %s (turn %s).' % (date, turn), text, count=1)
    text, n2 = re.subn(r'## Current checkpoint \(\d{4}-\d\d-\d\d, turn \d+\)', '## Current checkpoint (%s, turn %s)' % (date, turn),
                       text, count=1)
    if not (n1 and n2):
        raise SystemExit('no "Updated:" line or checkpoint heading to set')
    for label, new in zip(FIELDS, values):
        pat = re.compile(r'^- \*\*' + re.escape(label) + r':\*\* .*$', re.M)
        if not pat.search(text):
            raise SystemExit('no field: ' + label)
        text = pat.sub(lambda m: '- **%s:** %s' % (label, new), text, count=1)
    return text


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('turn')
    ap.add_argument('date')
    ap.add_argument('in_progress')
    ap.add_argument('next_step')
    ap.add_argument('waiting')
    ap.add_argument('--article', default='inner-child-therapy')
    ap.add_argument('--file')
    a = ap.parse_args(argv)
    p = pathlib.Path(a.file) if a.file else REPO / 'articles' / a.article / 'CURRENT-STATE.md'
    p.write_text(set_state(p.read_text(encoding='utf-8'), a.turn, a.date, (a.in_progress, a.next_step, a.waiting)),
                 encoding='utf-8')
    print('state set: turn %s, %s' % (a.turn, a.date))
    return 0


if __name__ == '__main__':
    sys.exit(main())
