#!/usr/bin/env python3
"""Record web-app results in the article's Pangram ledger by the text's SHA-256, with each window's confidence.

  python3 record_gui.py RESULTS.json

RESULTS.json: {"<sha256 of the checked text>": [headline, ai likelihood, words, "label, confidence, words; ...", time,
"/<history uuid>", [texts of the windows below Human High]]}, the compact form the page reader returns, keyed by hash
because these predictions were made without a key. `pangram_ledger.py result` writes the result; this adds the windows
as records, which is what `lane_push.py` reads to tell a High result from an open one (2026-11-25).
"""
import json, os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..', '..', '..'))
LEDGER = os.path.join(ROOT, 'articles', 'inner-signal', 'humanize', 'pangram-ledger.jsonl')
TOOL = os.path.join(ROOT, 'tools', 'humanization', 'pangram_ledger.py')
DETECTOR = "Pangram 4.1 (web app, his account, in the desktop app's browser pane)"


def main(path):
    res = json.load(open(path, encoding='utf-8'))
    for sha, r in res.items():
        headline, lk, words, wins, at, tail = r[:6]
        ws = []
        for part in [p.strip() for p in wins.split(';') if p.strip()]:
            label, conf, n = [x.strip() for x in part.split(',')]
            ws.append({'label': label, 'confidence': conf, 'words': int(n)})
        flagged = r[6] if len(r) > 6 else []
        low = [w for w in ws if not (w['label'].startswith('Human') and w['confidence'] == 'High')]
        for w, t in zip(low, flagged):
            w['text'] = t
        n_h = [w for w in ws if w['label'].startswith('Human')]
        verdict = 'Human' if len(n_h) == len(ws) else 'AI' if not n_h else 'Mixed'
        shading = '%d windows: %d AI, %d Human (%d High, %d Medium, %d Low)' % (
            len(ws), len(ws) - len(n_h), len(n_h), *[sum(1 for w in n_h if w['confidence'] == c) for c in ('High', 'Medium', 'Low')])
        out = subprocess.run([sys.executable, TOOL, 'result', LEDGER, '--sha', sha, '--verdict', verdict,
                              '--link', 'https://www.pangram.com/history' + tail, '--headline', headline,
                              '--likelihood', '%.3g' % lk, '--words', str(words), '--shading', shading,
                              '--detector', DETECTOR, '--at', at], capture_output=True, text=True)
        print((out.stdout + out.stderr).strip().splitlines()[-1])
        lines = open(LEDGER, encoding='utf-8').read().split('\n')
        for i in range(len(lines) - 1, -1, -1):
            if lines[i].strip() and '"type": "result"' in lines[i]:
                d = json.loads(lines[i])
                if not d.get('windows'):
                    d['windows'] = ws
                    lines[i] = json.dumps(d, ensure_ascii=False, sort_keys=True)
                break
        open(LEDGER, 'w', encoding='utf-8').write('\n'.join(lines))


if __name__ == '__main__':
    main(sys.argv[1])
