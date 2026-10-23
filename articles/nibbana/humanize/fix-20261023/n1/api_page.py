"""Nibbāna batch n1's API checks as a page Joel can open (the hypnosis guide's E214: an API check has no Pangram page, so
its link is its heading here): API-CHECKS.md from API-RESULTS-*.jsonl, the AI windows in bold with label and confidence.

  python3 articles/nibbana/humanize/fix-20261023/n1/api_page.py   (from the repo root)
"""
import json, pathlib

N = pathlib.Path(__file__).resolve().parent
PAGE = ('https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/community-joel-1018/articles/nibbana/humanize/'
        'fix-20261023/n1/API-CHECKS.md')


def main():
    rows = []
    for f in sorted(N.glob('API-RESULTS-*.jsonl')):
        rows += [json.loads(l) for l in f.read_text(encoding='utf-8').splitlines() if l.strip()]
    out = ['# Nibbāna batch n1\'s API checks (Pangram 4.1)', '',
           'Each check went through Joel\'s API key (`tools/humanization/pangram_api.py`, run on his laptop). AI windows '
           '(AI-Generated or AI-Assisted) are in **bold**, with their label and confidence; everything else read Human. The '
           'predictions are in `../../pangram-ledger.jsonl`; the fixes and why are in `make_n1.py`. Each check is a heading '
           'below, so its link is this page with #name at the end.', '']
    for r in rows:
        out += ['## %s' % r['name'], '', '**%s** (%s), %.0f%% AI, %d words, Pangram %s, %s.' % (
            r['headline'], r['prediction_short'], 100 * r['fraction_ai'], r['words'], r['version'], r['utc']), '']
        parts = []
        for label, conf, words, a, b, text in r['windows']:
            if label.startswith('AI'):
                kind = 'AI-assisted' if 'Assist' in label else 'AI'
                tag = '[%s, %s] ' % (kind, conf)
                # a window that runs over a paragraph break is labelled on every line: unlabelled, its later lines were
                # misread as Human (2026-10-23, Nibbāna n1's driving caution; E230)
                more = '[%s, %s, same window] ' % (kind, conf)
                pieces, first = [], True
                for line in text.split('\n'):
                    lead = line[:len(line) - len(line.lstrip())]
                    if line.strip():
                        pieces.append(lead + '**%s%s**' % (tag if first else more, line.strip()))
                        first = False
                    else:
                        pieces.append('')
                parts.append('\n'.join(pieces))
            else:
                parts.append(text)
        out += [x.strip() for x in ''.join(parts).split('\n')] + ['']
    (N / 'API-CHECKS.md').write_text('\n\n'.join(x for x in out if x) + '\n', encoding='utf-8')
    for r in rows:
        print(r['name'], r['headline'], PAGE + '#' + r['name'])


if __name__ == '__main__':
    main()
