#!/usr/bin/env python3
"""apply_h58.py - turn 50's tries into the guide, each change of mine only once its check by itself read Human High in
every window (tools/humanization/apply_gate.py; RESULTS.md has the links). The edits are build.py's, so the words that go
in are the words that were checked; each edit's old words, so it can be undone, are in build.py's TRIES.

- B214, niacin's side effects (b02-niacin-side, Human High 62, b6d71dcc): the liver risk said where he says it is
  (2026-11-20 00:01 UTC: "the niacin risk is for extended release yeah, haven't seen that with IR niacin unless you take
  it thru the day to make it ER. don't make it seem like niacin in general or "certain formulations" causes liver
  injury"): "Higher or repeated doses" now "Sustained-release niacin, or repeated doses through the day", with the
  randomized trial on "Sustained-release niacin" (McKenney et al. 1994, JAMA: hepatotoxic effects in 12 of 23 on
  sustained-release, none on immediate-release, at the same doses up to 3 g a day).
- B203, DMSO's side effects (c01-dmso-side, Human High 192, a579f6b8): "Sensitivity varies." back in the nausea
  line, as he asked ("don't cut 'sensitivity varies' ... we can explain they should try less at first because of
  that"), said as "Sensitivity to DMSO varies, so start with less than you planned."; the rats line's "higher
  doses" said as "higher doses of DMSO". b01 (fb34d3fb), the line as "so try a small amount at first", read both
  lines Human Medium.

  python3 articles/bad-trips/humanize/h58-20261120/apply_h58.py      (from the repo root)
"""
import json, pathlib, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parents[1]
REPO = ART.parents[1]
BJ = ART / 'GUIDE-SO-FAR-blocks.json'
MD = ART / 'GUIDE-SO-FAR.md'
LEDGER = 'articles/bad-trips/humanize/pangram-ledger.jsonl'
sys.path.insert(0, str(HERE))
import build as BD  # noqa: E402

PASSED = ['b02-niacin-side', 'c01-dmso-side']


def gate(key):
    test = HERE / ('TEST-%s.txt' % key)
    r = subprocess.run([sys.executable, 'tools/humanization/apply_gate.py', LEDGER, '--file', str(test.relative_to(REPO))],
                       cwd=REPO, capture_output=True, text=True)
    if r.returncode:
        sys.exit('refused by apply_gate.py for %s:\n%s' % (key, (r.stdout + r.stderr)[-800:]))


def main():
    B = json.loads(BJ.read_text(encoding='utf-8'))
    assert '\n\n'.join(b['md'] for b in B) + '\n' == MD.read_text(encoding='utf-8')
    ids = [b['id'] for b in B]
    for key in PASSED:
        gate(key)
        for blk, old, new in BD.TRIES[key][1]:
            md = B[ids.index(blk)]['md']
            if new in md and old not in md:
                continue                                   # already in
            assert md.count(old) == 1, (key, blk, old)
            B[ids.index(blk)]['md'] = md.replace(old, new)
    MD.write_text('\n\n'.join(b['md'] for b in B) + '\n', encoding='utf-8')
    BJ.write_text(json.dumps(B, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print('applied', ', '.join(PASSED), '|', len(MD.read_text(encoding='utf-8').split()), 'words')


if __name__ == '__main__':
    main()
