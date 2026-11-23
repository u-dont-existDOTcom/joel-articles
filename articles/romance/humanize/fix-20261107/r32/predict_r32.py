#!/usr/bin/env python3
"""Predictions for the section pass (sections.py), written to the lane's ledger before any check. Each section is the
fixed version as it stands (--unchanged). My call is Human for every one; my chance of a 100% Human result is lower for
the sections where the vetted junk read found real or partly real junk (r30/junk/VETTED.md)."""
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
LEDGER = ROOT / 'articles/romance/humanize/pangram-ledger.jsonl'
WEAK = ('tough love', 'ending consciously', 'psychedelic timing', 'different levels', 'whole world', 'slow & steady',
        'what i gained from loss', 'what will honesty produce', 'attraction and exclusivity', 'what we mean by')
TELLS = json.loads((HERE / 'TELLS.json').read_text(encoding='utf-8'))   # a fresh reader's quotes, one pair a section
done, failed = 0, []
for c in json.loads((HERE / 'SECTIONS.json').read_text(encoding='utf-8')):
    weak = any(w in c['heading'].lower() for w in WEAK)
    cmd = [sys.executable, str(ROOT / 'tools/humanization/pangram_ledger.py'), 'predict', str(LEDGER),
           '--lineage', 'romance-e307-%s' % c['key'][4:6], '--scope', 'section',
           '--text', str(HERE / 'checks' / ('CHECK-%s.txt' % c['key'])), '--call', 'Human',
           '--chance', '0.5' if weak else '0.6',
           '--tells', TELLS[c['key']]['tells'], '--human-tells', TELLS[c['key']]['human_tells'], '--key', c['key'], '--batch', 'romance-r32',
           '--detector', "pangram 4.1, the web app (Joel's account, GUI credits)",
           '--unchanged', "the fixed version's section \"%s\" as it stands (whole/FIXED.md, 2026-11-22), by itself under "
                          "gate E307" % c['heading'],
           '--decides', 'whether this section reads Human High by itself (E307), before the vetted junk is fixed',
           '--diagnosis', 'E307 section pass: this article had sections checked by themselves only where a check flagged them'
                          + ('; the vetted junk read found real or partly real junk here' if weak else '')]
    r = subprocess.run(cmd, capture_output=True, text=True, cwd=ROOT)
    if r.returncode:
        failed.append((c['key'], (r.stdout + r.stderr).strip().splitlines()[-1][:300]))
    else:
        done += 1
print('predictions written:', done, '| refused:', len(failed))
for k, m in failed[:8]:
    print(k, m)
