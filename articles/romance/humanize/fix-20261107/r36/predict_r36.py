#!/usr/bin/env python3
"""Predictions for the section recheck (sections.py, CHANGED.json), written to the lane's ledger before any check: each
section whose text changed since the section pass (r32) through r33 to r36, checked once as the fixed version has it
now (--unchanged: every change in it was checked by itself first, with its receipt or as his own check). The flaws
section is left out: its text now is the one r33 rechecked (romance-e307-26#251, Human High, Medium, High).
My call is Human for every one; my chance of a 100% Human result is higher where his own versions went in."""
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
LEDGER = ROOT / 'articles/romance/humanize/pangram-ledger.jsonl'
TELLS = json.loads((HERE.parent / 'r32' / 'TELLS.json').read_text(encoding='utf-8'))
R32 = json.loads((HERE.parent / 'r32' / 'checks' / 'RESULTS-r32.json').read_text(encoding='utf-8'))
def read(key):
    r = R32.get(key)
    if not r:
        return 'no result'
    return '%s (%s)' % (r['headline'], ', '.join('%s %s' % (w['label'], w['confidence']) for w in r['windows']))
WHAT = {  # what changed in each section since r32, in the order the layers apply
    '02': 'J-B10, the first of its two paragraphs (his approval, sixth page)',
    '03': 'J-B10, the second of its two paragraphs (his approval, sixth page)',
    '05': 'r34: "honestly" dropped from "willing to find out honestly with you"',
    '15': 'J-B84: the one-line summary after the knee story cut (his approval, sixth page)',
    '40': 'J-B201: four short lines made one sentence (his approval, sixth page)',
    '45': 'J-B220: the list without the friends the paragraphs before cover (his approval, sixth page)',
    '51': 'Q-B257: his own version ("Asking that question out loud is the first step in figuring it out")',
    '72': 'J-B379: "this ironically bureaucratic basis of romance" named (his approval, sixth page)',
    '78': 'J-B412: the warning without the line it repeats later (his approval, sixth page)',
    '85': 'Q-B442: his own version (the point after the list, the Bee story last)',
    '88': 'J-B453: the opening line leads to whether, and counseling (his approval, sixth page)',
    '89': 'r34: "do it honestly" became "do it fairly"',
    '91': 'r35: B473, one point said three times said once',
    '93': 'r36: "blossom in its own time" (r34) became "blossom genuinely"',
}
done, failed = 0, []
for c in json.loads((HERE / 'CHANGED.json').read_text(encoding='utf-8')):
    n = c['key'][4:6]
    if n == '26':
        continue
    old = TELLS.get(c['was']) or {}
    his = n in ('51', '85')
    cmd = [sys.executable, str(ROOT / 'tools/humanization/pangram_ledger.py'), 'predict', str(LEDGER),
           '--lineage', 'romance-e307-%s' % n, '--scope', 'section',
           '--text', str(HERE / 'checks' / ('CHECK-%s.txt' % c['key'])), '--call', 'Human',
           '--chance', '0.65' if his else '0.6',
           '--tells', 'the changed paragraph: ' + WHAT[n] + ('; the section pass\'s: ' + old['tells'] if old.get('tells') else ''),
           '--human-tells', old.get('human_tells') or 'the rest of the section, which read Human High in the section pass',
           '--key', c['key'], '--batch', 'romance-r36',
           '--detector', "pangram 4.1, the web app (Joel's account, GUI credits)",
           '--unchanged', 'the fixed version\'s section "%s" as it stands now (whole/FIXED.md after r36), each change in it '
                          'checked by itself first: %s' % (c['heading'], WHAT[n]),
           '--decides', 'whether this section still reads Human High by itself (E307) with the changes since the section '
                        'pass in it (its one recheck)',
           '--diagnosis', 'Section recheck after the paragraph fixes of r33 to r36: the section read %s in the section pass '
                          '(%s); since then %s.' % (read(c['was']), c['was'], WHAT[n])]
    r = subprocess.run(cmd, capture_output=True, text=True, cwd=ROOT)
    if r.returncode:
        failed.append((c['key'], (r.stdout + r.stderr).strip().splitlines()[-1][:300]))
    else:
        done += 1
print('predictions written:', done, '| refused:', len(failed))
for k, m in failed[:8]:
    print(k, m)
