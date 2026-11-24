#!/usr/bin/env python3
"""Predictions for the junk pass (r38/junk/), written to the lane's ledger before any check: each of the 16 sections
holding a partly real passage that still stands (ITEMS.json), with only the flagged words changed, his way (lesson
romance-2026-11-23h), checked once by itself with its making-sense receipt (receipts/R-<key>.json)."""
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[5]
LEDGER = ROOT / 'articles/romance/humanize/pangram-ledger.jsonl'
DIFF = json.loads((HERE / 'DIFF.json').read_text(encoding='utf-8'))
done, failed = 0, []
for k, d in DIFF.items():
    n = k[4:6]
    cmd = [sys.executable, str(ROOT / 'tools/humanization/pangram_ledger.py'), 'predict', str(LEDGER),
           '--lineage', 'romance-e307-%s' % n, '--scope', 'section',
           '--text', str(HERE / 'texts' / (k + '.txt')), '--receipt', str(HERE / 'receipts' / ('R-%s.json' % k)),
           '--call', 'Human', '--chance', '0.6',
           '--tells', 'the changed sentences: ' + ' / '.join(s[:80] for s in d['new']),
           '--human-tells', 'the rest of the section, which read Human High in every window in its last check',
           '--key', 'r38j-' + k[4:], '--batch', 'romance-r38j',
           '--detector', "pangram 4.1, the web app (Joel's account, GUI credits)",
           '--first-fix', 'payoff: the flagged sentence said so a reader who has read the section follows it; join: a tacked-on '
                          'line joined to the one it belongs to, with ", but", "so" or "and"; plain: only the flagged words and '
                          'their order changed, with words the passage already has, nothing added (lesson romance-2026-11-23h)',
           '--humanized', 'only the flagged words of %s changed, his way: the vague word given the noun the passage has, a '
                          'tacked-on line joined, a repeat cut; nothing added' % ', '.join(d['items']),
           '--after-fix', 'the section read Human High in every window; this changes only the passage a reader flagged (%s)'
                          % ', '.join(d['items']),
           '--diagnosis', 'A fresh reader flagged %s as not making sense or not following, and a fifth vetted it as partly real '
                          '(r30/junk/VETTED.md). The fix changes only those words, the way his sixth-page versions did.'
                          % ', '.join(d['items']),
           '--decides', 'whether the section still reads Human High in every window with the flagged passage made clear']
    r = subprocess.run(cmd, capture_output=True, text=True, cwd=ROOT)
    if r.returncode:
        failed.append((k, (r.stdout + r.stderr).strip().splitlines()[-2:]))
    else:
        done += 1
print('predictions written:', done, '| refused:', len(failed))
for k, m in failed:
    print(k, ' | '.join(x[:400] for x in m))
