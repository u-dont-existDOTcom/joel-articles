#!/usr/bin/env python3
"""write_predictions.py - the h42a batch's predictions into the lane's ledger, right before the checks run.

Reads UNITS.json and PREDICTIONS-h42a.json (a fresh reader's call, chance and tells for each unit, each tell quoted from
the unit's text) and runs `pangram_ledger.py predict` for each unit, as it stands (--unchanged). A tell that isn't in its
unit's text word for word stops the batch: the ledger asks for tells "in the actual words".

  python3 articles/bad-trips/humanize/h42-20261111/pass/write_predictions.py      (from the repo root)

Run it only when the checks can follow at once: the units are the guide as it stood after round 33, so rebuild them
(build_units.py) and redo the predictions if the guide changed since.
"""
import hashlib, json, pathlib, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
LEDGER = 'articles/bad-trips/humanize/pangram-ledger.jsonl'
U = json.loads((HERE / 'UNITS.json').read_text(encoding='utf-8'))
P = json.loads((HERE / 'PREDICTIONS-h42a.json').read_text(encoding='utf-8'))
for u in U:
    text = (HERE / 'units' / (u['key'] + '.txt')).read_text(encoding='utf-8').rstrip('\n')
    if hashlib.sha256(text.encode('utf-8')).hexdigest() != u['sha256']:
        sys.exit('%s changed since build_units.py: rebuild and predict again' % u['key'])
    p = P[u['key']]
    for t in p['tells'] + p['human_tells']:
        if t not in text:
            sys.exit('%s: the tell %r is not in its text' % (u['key'], t))
    cmd = [sys.executable, 'tools/humanization/pangram_ledger.py', 'predict', LEDGER,
           '--lineage', 'bad-trips %s as it stands (h42)' % u['title'], '--scope', 'section',
           '--text', str((HERE / 'units' / (u['key'] + '.txt')).relative_to(ROOT)),
           '--call', p['call'], '--chance', str(p['chance']),
           '--tells', '; '.join(p['tells']), '--human-tells', '; '.join(p['human_tells']),
           '--unchanged', 'the guide as it stands after round 33 (2026-11-11), the section "%s", %d%% of its words his own '
                          'versions or notes' % (u['title'], round(u['his_share'] * 100)),
           '--detector', 'Pangram web app (his account, Pangram Professional)', '--batch', 'h42a', '--key', u['key'],
           '--diagnosis', 'status check after the sense pass (rounds 27 to 33 changed most sections)',
           '--decides', 'which sections the humanize pass works on first, and which paragraphs could teach the most in '
                        'the teaching round he said he would do once the guide makes sense']
    r = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    if r.returncode:
        sys.exit('%s: %s' % (u['key'], r.stderr.strip()))
    print(r.stdout.strip())
