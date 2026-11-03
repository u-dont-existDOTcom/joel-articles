"""Predictions for the section checks of 1 November (batch s1101), written before the run (the budget rule,
docs/PANGRAM-PRODUCTION-BUDGET-20261020.md; tools/humanization/pangram_ledger.py).

The evidence for each section is how its words read in the last whole-guide check (30 October 21:40 UTC, part A
https://www.pangram.com/feed/a123b9a4-de86-462a-aa45-4f46b122ab4e and part B
https://www.pangram.com/feed/a485abe9-057b-4209-a9be-11ad81a90b90; ../../fix-20261030/tries/read/RESULT-A.json and
RESULT-B.json): every window of that check with at least two runs of eight of its words still in the section (or all of a
short one), with its label and confidence, and how much of the section those runs cover (the rest changed since: his answers of 1 November and the second full
read). My chance of a 100% Human result starts from those windows: every one Human (High), 0.8; any Human (Medium),
0.65; any Human (Low), 0.45; any AI, 0.3; less than half the section covered, 0.55 at most (new words, unread by Pangram).
A section read alone loses the Human context around it (E307), so each chance is that, less 0.05.

  python3 articles/inner-signal/humanize/fix-20261101/sections/predict_sections.py [--ledger]
Writes PREDICTIONS.md; with --ledger, adds each prediction to ../../pangram-ledger.jsonl (lineage HG1101-NN, scope
section, batch s1101) through pangram_ledger.py predict, which refuses what the budget rule forbids.
"""
import argparse
import json
import pathlib
import re
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parents[1]
ROOT = H.parents[2]
READ = H / 'fix-20261030' / 'tries' / 'read'
LEDGER = H / 'pangram-ledger.jsonl'
TEXTS = pathlib.Path('/tmp/claude-0/-home-claude/c925a45d-77a0-5b11-a8c3-3ce570004d0e/scratchpad/s1101-texts')
FLAT = str.maketrans({'“': '"', '”': '"', '‘': "'", '’': "'", '\xa0': ' ', '—': '-', '–': '-'})


def norm(s):
    return re.sub(r'\s+', ' ', s.translate(FLAT)).strip()


def windows():
    out = []
    for p in 'AB':
        r = json.loads((READ / ('RESULT-%s.json' % p)).read_text(encoding='utf-8'))
        for k, w in enumerate(r['windows'], 1):
            t = norm(r['text'][w['start_index']:w['end_index']])
            out.append({'part': p, 'n': k, 'label': w['label'], 'conf': w['confidence'], 'words': w['word_count'],
                        'text': t})
    return out


def pieces(t, n=8):
    """The window's words in runs of N: a run still in the section means those words are still there."""
    w = t.split()
    return [' '.join(w[i:i + n]) for i in range(0, max(1, len(w) - n + 1), n)]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--ledger', action='store_true')
    a = ap.parse_args()
    secs = json.loads((HERE / 'SECTIONS.json').read_text(encoding='utf-8'))['sections']
    ws = windows()
    rows = []
    for s in secs:
        st = norm(s['text'])
        hit, covered = [], 0
        for w in ws:
            ps = pieces(w['text'])
            k = sum(1 for p in ps if p in st)
            # a window runs across section boundaries: it counts here when two of its runs of eight words are here
            # (or all of a short one)
            if k >= 2 or (ps and k == len(ps)):
                hit.append(w)
                covered += k * 8
        cover = min(1.0, covered / max(1, s['words']))
        labels = [(w['label'], w['conf']) for w in hit]
        if any(l != 'Human' for l, c in labels):
            chance = 0.3
        elif ('Human', 'Low') in labels:
            chance = 0.45
        elif ('Human', 'Medium') in labels:
            chance = 0.65
        elif labels:
            chance = 0.8
        else:
            chance = 0.55
        if cover < 0.5:
            chance = min(chance, 0.55)
        chance = round(chance - 0.05, 2)
        tells, human = [], []
        for l, c in sorted(set(labels)):
            n = labels.count((l, c))
            (human if l == 'Human' and c == 'High' else tells).append(
                '%d window%s %s (%s) on 30 October' % (n, '' if n == 1 else 's', 'AI' if l != 'Human' else 'Human', c))
        if cover < 0.9:
            tells.append('%d%% of it new or changed since 30 October' % round(100 * (1 - cover)))
        if not human:
            human.append('read beside his published version (second full read, 1 November)')
        call = 'Human' if chance >= 0.5 else 'AI'
        rows.append({'key': s['key'], 'lineage': 'HG1101-%s' % s['key'].split('-')[1], 'name': s['name'],
                     'words': s['words'], 'call': call, 'chance': chance, 'tells': tells, 'human_tells': human,
                     'cover': round(cover, 2), 'windows_30oct': ['%s%d %s %s' % (w['part'], w['n'], w['label'], w['conf'])
                                                                  for w in hit]})
    out = ['# Batch s1101: each section of the guide by itself (predictions, written before the run)', '',
           'Gate E307. Chance = my chance of a 100% Human result; the evidence is the section\'s windows in the check of 30 '
           'October 21:40 UTC (predict_sections.py says how the chance is set). The Pangram column is filled after the run.',
           '', '| text | mine | chance | why | Pangram |', '|---|---|---|---|---|']
    for r in rows:
        out.append('| %s: %s (%d words) | %s | %.2f | %s | |' % (r['key'], r['name'].replace('|', '/'), r['words'], r['call'],
                                                              r['chance'], '; '.join(r['tells'] + r['human_tells'])))
    (HERE / 'PREDICTIONS.md').write_text('\n'.join(out) + '\n', encoding='utf-8')
    (HERE / 'PREDICTIONS.json').write_text(json.dumps(rows, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    from collections import Counter
    print(len(rows), 'predictions;', dict(Counter(r['call'] for r in rows)), 'mean chance %.2f' %
          (sum(r['chance'] for r in rows) / len(rows)))
    if not a.ledger:
        return
    TEXTS.mkdir(parents=True, exist_ok=True)
    for s, r in zip(secs, rows):
        f = TEXTS / (s['key'] + '.txt')
        f.write_text(s['text'], encoding='utf-8')
        cmd = [sys.executable, str(ROOT / 'tools' / 'humanization' / 'pangram_ledger.py'), 'predict', str(LEDGER),
               '--lineage', r['lineage'], '--scope', 'section', '--text', str(f), '--call', r['call'],
               '--chance', str(r['chance']), '--key', s['key'], '--batch', 's1101',
               '--decides', 'whether this section reads Human by itself (E307), and which of its windows need a fix (E306)']
        for t in r['tells']:
            cmd += ['--tells', t]
        for t in r['human_tells']:
            cmd += ['--human-tells', t]
        p = subprocess.run(cmd, capture_output=True, text=True)
        if p.returncode:
            sys.exit('%s: %s%s' % (s['key'], p.stdout, p.stderr))
    print('ledger: %d predictions added' % len(rows))


if __name__ == '__main__':
    main()
