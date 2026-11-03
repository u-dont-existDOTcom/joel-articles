#!/usr/bin/env python3
"""window_confidence.py - every window of a Pangram result that isn't High-confidence Human, with where it is and whose words.

Joel, 2026-10-26 12:43 UTC, on the hypnosis guide's recheck (part A 100% Human, part B one AI segment): "i also want you
to fix any segments that are not high confidence human if you can, and always we should be marking down the confidence if
we have it, because less than high confidence means it's likely next pangram version will mark it ai (that happened in
pangram 4.1 update)". So every reading of a result records each window's confidence, and every window that reads Human at
Medium or Low confidence is listed with the AI ones, as work to do (gate E278).

  python3 tools/humanization/window_confidence.py RESULT.json [RESULT2.json ...] --out CONFIDENCE.md
          [--json CONFIDENCE.json] [--article ARTICLE.md] [--his FILE ...] [--other NAME=FILE ...]

RESULT.json is a lane's rebuilt result (substack_check_text.py result) or pangram_feed_read.js's full output: it needs
"text" and "windows" (label, confidence, word_count, start_index, end_index, calibrated_confidence when the result has it).
--article, the Markdown the checked text was built from, puts each window's place on it (its heading and P-number, the
numbers on Joel's pages). --his names files of the author's own words (Markdown or HTML): a sentence found in them word
for word (quotes, dashes, case and spaces aside) is marked "his". --other NAME=FILE marks sentences found in FILE as NAME
(an inner child guide, a list of approved sentences). Anything else is "approved wording": words in the working copy that
are neither his nor named, which in a lane means wording he approved on a page (Emulate's or a model's).

The page lists, for each result: the counts by label and confidence, then a table of the windows that aren't High-
confidence Human (window number, label and confidence, calibrated confidence, words, place, text, whose words), so a
report can say "Human (Low)" for a window instead of "Human".
"""
import argparse
import html
import json
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

FLAT = str.maketrans({'“': '"', '”': '"', '‘': "'", '’': "'", '–': '-', '—': '-', ' ': ' '})
ORDER = [('Human', 'High'), ('Human', 'Medium'), ('Human', 'Low'), ('AI', 'Low'), ('AI', 'Medium'), ('AI', 'High')]


def norm(s):
    s = s.translate(FLAT).lower()
    s = re.sub(r'[*_`#>]', '', s)
    return re.sub(r'\s+', ' ', s).strip(' "\'()[]')


def text_of(p):
    p = pathlib.Path(p)
    t = p.read_text(encoding='utf-8')
    if p.suffix.lower() in ('.html', '.htm'):
        t = html.unescape(re.sub(r'<[^>]+>', ' ', t))
    return norm(t)


def sentences(t):
    parts = re.split(r'(?<=[.!?…])["”’)]?\s+(?=["“‘(]?[A-Z0-9])|\n+', t)
    return [p.strip() for p in parts if p.strip()]


def label(w):
    return 'AI' if str(w.get('label', '')).startswith('AI') else 'Human'


def counts(windows):
    c = {}
    for w in windows:
        k = (label(w), w.get('confidence'))
        c[k] = c.get(k, 0) + 1
    return ['%s %s %d' % (k[0], k[1], c[k]) for k in ORDER if c.get(k)] + \
           ['%s %s %d' % (k[0], k[1], v) for k, v in c.items() if k not in ORDER]


def rows(result, his='', others=(), article=None):
    t = result['text']
    places = []
    if article:
        import suggestion_review as sr
        md = pathlib.Path(article).read_text(encoding='utf-8')
        bl = sr.blocks(md)
        places = [(sr.where(bl, b['i']), norm(b['text'])) for b in bl if not b['level']]
    out = []
    for n, w in enumerate(result['windows']):
        if label(w) == 'Human' and w.get('confidence') == 'High':
            continue
        seg = t[w['start_index']:w['end_index']]
        sents = []
        for s in sentences(seg):
            ns = norm(s)
            if len(ns) < 2:
                continue
            whose = 'his' if his and ns in his else next((name for name, txt in others if ns in txt), 'approved wording')
            sents.append({'text': s, 'whose': whose})
        place = None
        longest = max(sents, key=lambda x: len(x['text']))['text'] if sents else ''
        if longest:
            nl = norm(longest)
            place = next((where for where, pt in places if nl and nl in pt), None)
        cal = w.get('calibrated_confidence')
        out.append({'window': n, 'label': label(w), 'confidence': w.get('confidence'),
                    'calibrated': round(cal, 4) if isinstance(cal, (int, float)) else None, 'words': w.get('word_count'),
                    'uncertainty_highlighted': bool(w.get('uncertainty_highlighting')), 'where': place,
                    'text': seg.strip(), 'sentences': sents})
    return out


def page(results):
    lines = ['# Every window that isn\'t High-confidence Human', '',
             'Made by `tools/humanization/window_confidence.py`. A window that reads Human at Medium or Low confidence is listed '
             'with the AI ones: less than High is what a later Pangram version is likeliest to read AI (Joel, 2026-10-26; gate '
             'E278). "Calibrated" is Pangram\'s calibrated confidence for the window, where the result gives it.', '']
    for name, res, rs in results:
        lines += ['## %s' % name, '']
        if res.get('link') or res.get('headline'):
            lines += ['%s%s.' % (res.get('headline') or '', (' (%s)' % res['link']) if res.get('link') else ''), '']
        lines += ['Windows: %s.' % ', '.join(counts(res['windows'])), '']
        if not rs:
            lines += ['Every window reads High-confidence Human.', '']
            continue
        lines += ['| # | read | calibrated | words | where | text | whose |', '| --- | --- | --- | --- | --- | --- | --- |']
        for x in rs:
            whose = ', '.join(sorted({s['whose'] for s in x['sentences']})) or '-'
            cal = '%.3f' % x['calibrated'] if x['calibrated'] is not None else '-'
            lines.append('| %d | %s %s | %s | %s | %s | %s | %s |' % (
                x['window'], x['label'], x['confidence'], cal, x['words'], x['where'] or '-',
                x['text'].replace('\n', ' / ').replace('|', '\\|')[:160], whose))
        lines.append('')
    return '\n'.join(lines) + '\n'


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('results', nargs='+')
    ap.add_argument('--out', required=True)
    ap.add_argument('--json')
    ap.add_argument('--article')
    ap.add_argument('--his', action='append', default=[])
    ap.add_argument('--other', action='append', default=[], help='NAME=FILE')
    a = ap.parse_args(argv)
    his = ' '.join(text_of(p) for p in a.his)
    others = [(o.split('=', 1)[0], text_of(o.split('=', 1)[1])) for o in a.other]
    results, data = [], {}
    for p in a.results:
        res = json.loads(pathlib.Path(p).read_text(encoding='utf-8'))
        rs = rows(res, his, others, a.article)
        name = pathlib.Path(p).name
        results.append((name, res, rs))
        data[name] = {'link': res.get('link'), 'headline': res.get('headline'), 'counts': counts(res['windows']), 'rows': rs}
        print('%s: %s; not High-confidence Human: %d' % (name, ', '.join(counts(res['windows'])), len(rs)))
    pathlib.Path(a.out).write_text(page(results), encoding='utf-8')
    if a.json:
        pathlib.Path(a.json).write_text(json.dumps(data, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')


if __name__ == '__main__':
    main()
