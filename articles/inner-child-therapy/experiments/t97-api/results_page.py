#!/usr/bin/env python3
"""Turn 97: API-RESULTS.md, a page Joel can open for the API checks (E214: every stretch I ask him to fix comes with the
check that shows it; API checks have no Pangram page, so this page shows what each one flagged).

Reads API-RESULTS-*.jsonl (the lines pangram_api.py printed with --windows) and NAMES below, and writes each check's
text with its AI windows in bold, labelled with their confidence.
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
NAMES = json.loads((HERE / 'NAMES.json').read_text(encoding='utf-8'))


def marked(windows):
    out = []
    for label, conf, words, start, end, text in windows:
        pieces = text.split('\n')
        for i, piece in enumerate(pieces):
            if i:
                out.append('\n\n')
            if piece.strip() and label != 'Human Written':
                tag = 'AI' if label == 'AI-Generated' else label
                lead = len(piece) - len(piece.lstrip())
                out.append(piece[:lead] + '**[%s, %s] %s**' % (tag, conf, piece.strip()))
            else:
                out.append(piece)
    return ''.join(out)


def main():
    lines = ['# Turn 97\'s API checks (Pangram 4.1)', '',
             'Each check went through Joel\'s API key (`tools/humanization/pangram_api.py`). AI windows are in **bold**, with '
             'their label and confidence; everything else read Human. The predictions are in `../../tools/pangram-ledger.jsonl` '
             '(batch t97-api).', '']
    for f in sorted(HERE.glob('API-RESULTS-*.jsonl')):
        for l in f.read_text(encoding='utf-8').splitlines():
            r = json.loads(l)
            pct = round(100 * (r['fraction_ai'] or 0))
            lines += ['## %s: %s' % (r['name'], NAMES.get(r['name'], '')), '',
                      '%s (%s), %d%% AI, %d words, version %s, %s.' % (r['headline'], r['prediction_short'], pct, r['words'],
                                                                      r['version'], r['utc']), '',
                      marked(r['windows']), '']
    (HERE / 'API-RESULTS.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print('wrote', HERE / 'API-RESULTS.md')


if __name__ == '__main__':
    main()
