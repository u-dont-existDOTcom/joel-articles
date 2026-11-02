"""An API batch's results (pangram_api.py on Joel's laptop, with public links), read into the ledger and written out:
batch r1102 (this folder), and the batches after it (--dir, --ledger-file, --log).

API-ROUND1.log is pangram_api.py's output for TEXTS.json (one line per text, with --windows and --public), copied back
from the laptop (inbox/pangram-r1102/round1.log). This script checks each line's SHA-256 against the text sent, writes
RESULTS.json (the ledger's form: headline, AI fraction, words, every window as "label, confidence, words", time, link)
and RESULTS.md (each text's result with its public link and every window that isn't Human (High), with its words), and
with --ledger adds the results to ../../pangram-ledger.jsonl.

  python3 articles/inner-signal/humanize/fix-20261102/recheck/record_r1102.py [--ledger] [--dir DIR] [--log NAME]
      [--ledger-file LEDGER] [--title TITLE]
"""
import argparse
import hashlib
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parents[1]
ROOT = H.parents[2]
LEDGER = H / 'pangram-ledger.jsonl'


def label(w):
    return 'AI' if w[0].lower().startswith('ai') else 'Human'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--ledger', action='store_true')
    ap.add_argument('--dir', default=str(HERE))
    ap.add_argument('--log', default='API-ROUND1.log')
    ap.add_argument('--ledger-file', default=str(LEDGER))
    ap.add_argument('--title', default='Batch r1102')
    a = ap.parse_args()
    D = pathlib.Path(a.dir)
    texts = json.loads((D / 'TEXTS.json').read_text(encoding='utf-8'))
    preds = {p['key']: p for p in json.loads((D / 'PREDICTIONS.json').read_text(encoding='utf-8'))}
    res, md = {}, ['# %s: results (Pangram 4.1 through the API, public links)' % a.title, '',
                   'Each text was checked by itself (TEXTS.json; predictions in PREDICTIONS.md, written before the run). '
                   'Windows that read Human (High) aren\'t listed.', '',
                   '| text | words | mine | result | link |', '|---|---|---|---|---|']
    detail = []
    for line in (D / a.log).read_text(encoding='utf-8').splitlines():
        d = json.loads(line)
        k = d['name']
        assert d['sha256'] == hashlib.sha256(texts[k].encode('utf-8')).hexdigest(), k
        assert str(d['version']) == '4.1', k
        wins = ['%s, %s, %d' % (label(w), w[1], w[2]) for w in d['windows']]
        res[k] = {'headline': d['headline'], 'fraction_ai': d['fraction_ai'], 'words': d['words'], 'windows': wins,
                  'utc': d['utc'], 'link': d['dashboard_link']}
        p = preds[k]
        name = p.get('name') or p.get('why', '')
        md.append('| %s: %s | %d | %s (%.2f) | %s, %.1f%% AI | [result](%s) |' % (
            k, name.replace('|', '/'), d['words'], p['call'], p['chance'], d['headline'], 100 * d['fraction_ai'],
            d['dashboard_link']))
        flagged = [w for w in d['windows'] if not (label(w) == 'Human' and w[1] == 'High')]
        if flagged:
            detail += ['', '## %s: %s' % (k, name), '', '%s, %.1f%% AI: %s' % (
                d['headline'], 100 * d['fraction_ai'], d['dashboard_link']), '']
            detail += ['- %s (%s, %d words): %s' % (label(w), w[1], w[2], ' '.join((w[5] or '').split())) for w in flagged]
    assert set(res) == set(preds), set(preds) - set(res)
    (D / 'RESULTS.json').write_text(json.dumps(res, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    (D / 'RESULTS.md').write_text('\n'.join(md + detail) + '\n', encoding='utf-8')
    print(len(res), 'results')
    if a.ledger:
        p = subprocess.run([sys.executable, str(ROOT / 'tools' / 'humanization' / 'pangram_ledger.py'), 'results',
                            a.ledger_file, str(D / 'RESULTS.json')], capture_output=True, text=True)
        print(p.stdout[-3000:], p.stderr[-2000:])
        if p.returncode:
            sys.exit(p.returncode)


if __name__ == '__main__':
    main()
