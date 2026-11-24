#!/usr/bin/env python3
"""Predictions for r40's checks, written to the lane's ledger before any check: his new opening of "Primal attraction"
in its two section parts (his words, a new lineage each, since nothing of mine went before them), and "Twin Flames?" with
"Senegal" corrected (its own lineage, one word changed after a Human High read)."""
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
LEDGER = ROOT / 'articles/romance/humanize/pangram-ledger.jsonl'
DET = "pangram 4.1, the web app (Joel's account, GUI credits)"
HIS = 'payoff: his own words, unchanged; join: his own words, unchanged; plain: his own words (obvious corrections only)'
JOBS = [
    ('52', 'romance-r40-primal-p1', HERE / 'primal' / 'R-52.json', '0.8',
     'none: his own new text, as he wrote it',
     'his jokes and asides ("alive and poppin’", "shit-testing", "for safety and legal reasons"), his own memories, the Cooper video',
     'his new opening of the section, paragraphs 1 to 5, read by itself for the fixed version\'s record',
     'his paste of 2026-11-24 16:23 UTC as he wrote it, with "descendants" spelled right and his links made whole'),
    ('53', 'romance-r40-primal-p2', HERE / 'primal' / 'R-53.json', '0.8',
     'none: his own new text, as he wrote it',
     'his asides ("until everyone does", "especially since I don\'t exist!", the women stopping their cars), "soy boy smile"',
     'his new opening of the section, paragraphs 6 to 10, read by itself for the fixed version\'s record',
     'his paste of 2026-11-24 16:23 UTC as he wrote it'),
    ('64', 'romance-e307-64', HERE / 'twin' / 'R-r40-64-twin-flames.json', '0.95',
     'none: one word respelled in his own paragraph',
     'the section read Human High in every window in its last check (#330)',
     'whether "Twin Flames?" still reads Human High in every window with Senegal spelled as he asked',
     'the section as #330 read it, with "Sênêgal" spelled "Senegal" (his message of 2026-11-24 16:23 UTC)'),
]
for k, lineage, receipt, chance, tells, human, decides, unchanged in JOBS:
    text = next((HERE / 'checks').glob('CHECK-r40-%s-*.txt' % k))
    cmd = [sys.executable, str(ROOT / 'tools/humanization/pangram_ledger.py'), 'predict', str(LEDGER),
           '--lineage', lineage, '--scope', 'section', '--text', str(text), '--receipt', str(receipt),
           '--call', 'Human', '--chance', chance, '--tells', tells, '--human-tells', human,
           '--key', text.stem[len('CHECK-'):], '--batch', 'romance-r40', '--detector', DET, '--first-fix', HIS,
           '--humanized', 'his own words, not rewritten', '--after-fix', unchanged,
           '--diagnosis', 'his own text, checked by itself for the fixed version before the live update', '--decides', decides]
    r = subprocess.run(cmd, capture_output=True, text=True, cwd=ROOT)
    print(k, 'refused' if r.returncode else 'ok', (r.stdout + r.stderr).strip().splitlines()[-1][:400] if (r.stdout + r.stderr).strip() else '')
