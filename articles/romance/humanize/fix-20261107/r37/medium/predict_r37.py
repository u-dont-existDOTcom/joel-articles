#!/usr/bin/env python3
"""Predictions for the Medium pass (lesson romance-2026-11-23i), written to the lane's ledger before any check: each of
the 21 sections whose last check had a Medium window, with only the Medium sentences (and the ones beside them that read
the same way) changed, checked once by itself, with its making-sense receipt (receipts/R-<key>.json)."""
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[5]
LEDGER = ROOT / 'articles/romance/humanize/pangram-ledger.jsonl'
DIFF = json.loads((HERE / 'DIFF.json').read_text(encoding='utf-8'))
MED = json.loads(pathlib.Path('/home/claude/work/r37/med.json').read_text(encoding='utf-8'))
done, failed = 0, []
for k, d in DIFF.items():
    n = k[4:6]
    wins = '; '.join('"%s"' % w[2].replace('\n', ' ')[:120] for w in MED[n])
    his = bool(d['his_touched'])
    cmd = [sys.executable, str(ROOT / 'tools/humanization/pangram_ledger.py'), 'predict', str(LEDGER),
           '--lineage', 'romance-e307-%s' % n, '--scope', 'section',
           '--text', str(HERE / 'texts' / (k + '.txt')), '--receipt', str(HERE / 'receipts' / ('R-%s.json' % k)),
           '--call', 'Human', '--chance', '0.5' if his or len(MED[n]) > 2 else '0.55',
           '--tells', 'the changed sentences: ' + ' / '.join(s[:80] for s in d['new']),
           '--human-tells', 'the rest of the section, which read High in its windows of the last check',
           '--key', 'r37-' + k[4:], '--batch', 'romance-r37',
           '--detector', "pangram 4.1, the web app (Joel's account, GUI credits)",
           '--first-fix', 'payoff: the point of each Medium sentence said with it, not after it; join: a Medium sentence '
                          'that stood alone joined to the one it belongs to, with "so", "because" or a comma, the way his '
                          'fix of the "Talk about making love" section did; plain: no word changed to get past the detector, '
                          'a mirrored pair broken, a closing line carried on into its point',
           '--humanized', 'only the sentences in the Medium windows, and the ones beside them that read the same way, '
                          'changed his ways (lesson romance-2026-11-23i); nothing added',
           '--diagnosis', 'The section read Human with Medium windows on %s (his message of 2026-11-23 23:49 UTC: "i often '
                          'find the medium windows indicate other issues also"). His fix of three in another section, and '
                          'the blind round 6 that read Human High from it, changed each sentence\'s form; this try does the '
                          'same here.' % wins,
           '--decides', 'whether fixing the Medium sentences his ways takes this section to Human High in every window']
    r = subprocess.run(cmd, capture_output=True, text=True, cwd=ROOT)
    if r.returncode:
        failed.append((k, (r.stdout + r.stderr).strip().splitlines()[-3:]))
    else:
        done += 1
print('predictions written:', done, '| refused:', len(failed))
for k, m in failed:
    print(k, ' | '.join(x[:300] for x in m))
