#!/usr/bin/env python3
"""The whole-article check of 2026-11-06 (Joel's extension, feed f481f824), mapped onto the article's paragraphs.

Rebuilds the text Pangram read from the pasted payload (tools/humanization/substack_check_text.py's checked_text), with
the one difference the rendered check found (his line break in the dynorphin paragraph, which Substack shows as a
space), checks its SHA-256 against the feed's, then gives every paragraph the windows that cover it and every section a
count. Writes RESULT.json and RESULT.md beside it.
"""
import hashlib
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import substack_check_text as sct  # noqa: E402

PAYLOAD = HERE.parent / 'substack' / 'PAYLOAD-A.html'
FEED = 'https://www.pangram.com/feed/f481f824-5b0b-462f-96e4-237f0b2c057d'
WANT = '51a3f49274a4fdc9584b25ec1f1ee608c3bb0b2fffa126714ef8aa676a08afa0'


def main():
    payload = PAYLOAD.read_text(encoding='utf-8')
    text = sct.checked_text(payload).replace('attention to).\nEven', 'attention to). Even', 1)
    got = hashlib.sha256(text.encode('utf-8')).hexdigest()
    assert got == WANT, got
    lines = text.split('\n')
    # each line's heading: the payload's top-level blocks in order, as checked_text walks them
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(payload, 'html.parser')
    head, heads = '', []
    for el in soup.children:
        if getattr(el, 'name', None) in ('h1', 'h2', 'h3', 'h4', 'h5', 'h6'):
            head = el.get_text().strip()
            continue
        got_lines = []
        sct._lines(el, got_lines)
        heads.extend([head] * len(got_lines))
    assert len(heads) == len(lines), (len(heads), len(lines))
    wins = []
    for w in (HERE / 'WINDOWS.txt').read_text().strip().split(';'):
        lab, conf, s, e, words = w.split(',')[:5]
        wins.append(('AI' if lab == 'A' else 'Human', {'H': 'High', 'M': 'Medium', 'L': 'Low'}[conf], int(s), int(e),
                     int(words)))
    starts, pos = [], 0
    for ln in lines:
        starts.append(pos)
        pos += len(ln) + 1
    paras = []
    for n, (ln, st) in enumerate(zip(lines, starts)):
        en = st + len(ln)
        cover = [w for w in wins if w[2] < en and w[3] > st]
        reads = [{'label': w[0], 'confidence': w[1], 'words': w[4],
                  'text': text[max(w[2], st):min(w[3], en)][:90]} for w in cover]
        worst = 'Human, High'
        if any(r['label'] == 'AI' for r in reads):
            worst = 'AI'
        elif any(r['confidence'] == 'Low' for r in reads):
            worst = 'Human, Low'
        elif any(r['confidence'] == 'Medium' for r in reads):
            worst = 'Human, Medium'
        paras.append({'n': n + 1, 'section': heads[n], 'start': ln[:80], 'words': len(ln.split()), 'worst': worst,
                      'windows': reads})
    sections = []
    for p in paras:
        if not sections or sections[-1]['section'] != p['section']:
            sections.append({'section': p['section'], 'paragraphs': 0, 'AI': 0, 'Human, Low': 0, 'Human, Medium': 0,
                             'Human, High': 0})
        sections[-1]['paragraphs'] += 1
        sections[-1][p['worst']] += 1
    out = {'feed': FEED, 'text_sha256': got, 'paragraphs': paras, 'sections': sections}
    (HERE / 'RESULT.json').write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    md = ['# The whole article, 6 November: what Pangram read, paragraph by paragraph', '',
          'Joel\'s extension check of the article as it stood (HUMANIZED-SO-FAR.md d18316ea), [the result](%s): AI Detected, '
          '56%% AI (77 AI windows, 56 Human), the text read checked by SHA-256 against the pasted payload. A paragraph\'s '
          'reading is its worst window: AI; Human at Low; Human at Medium; or Human, High throughout.' % FEED, '',
          '| section | paragraphs | AI | Human, Low | Human, Medium | Human, High |', '|---|---|---|---|---|---|']
    for s in sections:
        md.append('| %s | %d | %d | %d | %d | %d |' % (s['section'] or '(before the first heading)', s['paragraphs'], s['AI'],
                                                     s['Human, Low'], s['Human, Medium'], s['Human, High']))
    md += ['', '## Every paragraph that isn\'t Human, High throughout', '']
    cur = None
    for p in paras:
        if p['worst'] == 'Human, High':
            continue
        if p['section'] != cur:
            cur = p['section']
            md += ['', '**%s**' % (cur or '(before the first heading)'), '']
        md.append('- %d. %s: "%s..."' % (p['n'], p['worst'], p['start'][:70]))
    (HERE / 'RESULT.md').write_text('\n'.join(md) + '\n', encoding='utf-8')
    tot = {k: sum(s[k] for s in sections) for k in ('paragraphs', 'AI', 'Human, Low', 'Human, Medium', 'Human, High')}
    print(json.dumps(tot))


if __name__ == '__main__':
    main()
