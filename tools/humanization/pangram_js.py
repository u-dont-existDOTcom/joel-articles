#!/usr/bin/env python3
"""Print the two browser calls for a pushed Pangram batch, one per tab (turn 76: fewer rounds of calls per batch).

  python3 tools/humanization/pangram_js.py RUN N [--sha SHA] [--article inner-child-therapy]

RUN is the batch's file stem in the article's tools/pangram-runs/ (for example 2026-10-19-turn76-a) and N is how many
checks it has. Send the tab-11 call (forward) and the tab-6 call (reverse) together. Then send the third call, "read",
once the batch has had time to run (about 10 seconds a check per tab): it reads the results once, keeps them in
window.__res, and returns how many of the N are in with each one's headline. The browser tool stops a call after 45
seconds and one read can take 10 seconds or more (it pages through Pangram's history), so the read doesn't poll; send it
again until all N are in, then save window.__res. The files are fetched from raw.githubusercontent.com at SHA (default
HEAD, which must be pushed).
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
            "window.__res = await new (Object.getPrototypeOf(async function () {}).constructor)(rd)(); const o = JSON.parse(window.__res); "
            "Object.keys(o).length + ' of %d: ' + Object.entries(o).map(([k, v]) => k + ' ' + v.headline + ' ' + v.avg_ai_likelihood.toFixed(3)"
            " + ' [' + v.windows.join('; ') + ']').join(' | ')") % (base, n)
    rev = "window.__reverse = true; const src = await fetch('%s.js').then(r => r.text()); (0, eval)(src);" % base
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
