"""Record a batch's web-app results (Pangram's dashboard, one paragraph per check) against its predictions, with every
window's confidence (E278), and write its RESULTS.md. DIR holds PREDICTIONS.json (predict_batch.py) and RESULTS-GUI.json
({"detector", "results": {key: {"uuid", "at", "headline", "ai", "words", "windows": [[label, confidence, words, text]]}}},
read from the history by SHA-256, so each result is the text that was predicted).

  python3 articles/neuro-de-armoring/humanize/fix-20261104/checks/record_gui.py DIR --title "..." [--dry-run]
"""
import argparse
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parents[1]
ROOT = H.parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import pangram_ledger as pl  # noqa: E402

LEDGER = H / 'pangram-ledger.jsonl'


def conf(ws):
    return ', '.join('%s (%s, %d words)' % (w[0].replace('AI-Generated', 'AI'), w[1], w[2]) for w in ws)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('dir')
    ap.add_argument('--title', required=True)
    ap.add_argument('--dry-run', action='store_true')
    a = ap.parse_args()
    D = pathlib.Path(a.dir).resolve()
    preds = json.loads((D / 'PREDICTIONS.json').read_text(encoding='utf-8'))
    got = json.loads((D / 'RESULTS-GUI.json').read_text(encoding='utf-8'))
    recs = pl.read(LEDGER)
    rows, out = [], []
    for p in preds:
        r = got['results'][p['key']]
        link = 'https://www.pangram.com/history/' + r['uuid']
        verdict = pl.verdict_of(r['headline'], None, r['ai'])
        open_p = pl.find(recs, sha=p['sha256'], open_only=True)
        assert open_p and open_p['key'] == p['key'], ('no open prediction for', p['key'])
        rec = pl.result_rec(open_p, verdict, link, {'headline': r['headline'], 'ai_fraction': r['ai'], 'words_read': r['words'],
                                                     'detector': got['detector'], 'at': r['at']})
        rec['windows'] = ['%s, %s, %d' % (w[0].replace('AI-Generated', 'AI'), w[1], w[2]) for w in r['windows']]
        out.append(rec)
        pct = '%.1f%% AI' % (r['ai'] * 100)
        rows.append((p, r, link, verdict, pct, rec['right']))
    if not a.dry_run:
        for rec in out:
            pl.append(LEDGER, rec)
    md = ['# %s' % a.title, '',
          'Each text checked by itself in Pangram\'s web app (%s). Predictions were written first (PREDICTIONS.md). Each '
          'window\'s confidence is given; a window that reads Human at less than High is work to do (E278), Low first.'
          % got['detector'], '',
          '| text | words | mine | result | windows | link |', '|---|---|---|---|---|---|']
    for p, r, link, verdict, pct, right in rows:
        md.append('| %s: %s | %d | %s (%.2f)%s | %s, %s | %s | [result](%s) |' % (
            p['key'], p['name'], r['words'], p['call'], p['chance'], '' if right else ' **miss**', r['headline'], pct,
            conf(r['windows']), link))
    for p, r, link, verdict, pct, right in rows:
        md += ['', '## %s: %s' % (p['key'], p['name']), '', '%s, %s: %s' % (r['headline'], pct, link), '']
        for w in r['windows']:
            md.append('- %s (%s, %d words): %s%s' % (w[0].replace('AI-Generated', 'AI'), w[1], w[2], w[3],
                                                     '' if len(w[3]) < 99 else ' ...'))
    (D / 'RESULTS.md').write_text('\n'.join(md) + '\n', encoding='utf-8')
    for p, r, link, verdict, pct, right in rows:
        print(p['key'], verdict, pct, 'right' if right else 'MISS', link)


if __name__ == '__main__':
    main()
