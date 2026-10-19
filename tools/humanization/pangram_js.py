#!/usr/bin/env python3
"""Print the two browser calls for a pushed Pangram batch, one per tab (turn 76: fewer rounds of calls per batch).

  python3 tools/humanization/pangram_js.py RUN N [--sha SHA] [--article inner-child-therapy]

RUN is the batch's file stem in the article's tools/pangram-runs/ (for example 2026-10-19-turn76-a) and N is how many
checks it has. Tab-11 runs the batch forward. Tab-6 runs it in reverse, then reads the results every 5 seconds until
all N are in or 35 seconds have passed, and returns what it has as JSON. The browser tool stops a call after 45
seconds (turn 76), so a long batch then needs the third call, "read", which only polls for another 35 seconds; send
it again until all N are in. The files are fetched from raw.githubusercontent.com at SHA (default HEAD, which must be
pushed).
"""
import argparse
import pathlib
import subprocess
import sys

REPO = pathlib.Path(__file__).resolve().parents[2]


def calls(run, n, sha, article='inner-child-therapy'):
    base = 'https://raw.githubusercontent.com/u-dont-existDOTcom/joel-articles/%s/articles/%s/tools/pangram-runs/%s' % (
        sha, article, run)
    fwd = "window.__reverse = false; const src = await fetch('%s.js').then(r => r.text()); (0, eval)(src);" % base
    poll = ("const rd = (await fetch('%s-read.js').then(r => r.text())).replace('JSON.stringify(out)', 'return JSON.stringify(out)'); "
            "const read = new (Object.getPrototypeOf(async function () {}).constructor)(rd); let res = '{}'; "
            "for (let i = 0; i < 7; i++) { await new Promise(r => setTimeout(r, 5000)); res = await read(); "
            "if (Object.keys(JSON.parse(res)).length >= %d) break; } res") % (base, n)
    rev = "window.__reverse = true; const src = await fetch('%s.js').then(r => r.text()); (0, eval)(src); " % base + poll
    return fwd, rev, poll


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('run')
    ap.add_argument('n', type=int)
    ap.add_argument('--sha')
    ap.add_argument('--article', default='inner-child-therapy')
    a = ap.parse_args(argv)
    sha = a.sha or subprocess.run(['git', 'rev-parse', 'HEAD'], cwd=REPO, capture_output=True, text=True, check=True).stdout.strip()
    fwd, rev, poll = calls(a.run, a.n, sha, a.article)
    print('tab-11:', fwd)
    print('tab-6:', rev)
    print('read:', poll)
    return 0


if __name__ == '__main__':
    sys.exit(main())
