#!/usr/bin/env python3
"""Turn the live post's body HTML into this run's files (the method of ../../../inner-child-therapy/experiments/t130-toc
and t131-toc-check, docs/FIXING-AN-ARTICLE.md section 3).

  python3 make_files.py LIVE-BODY.html

Writes, beside this script:
  SECTIONS.json          one entry per heading (h1-h6): id (S001 = first heading), level, heading, own words, own text
  TEXT-NO-HEADINGS.md    the whole text, each section marked [S001] ... with its heading taken out (for the agent that
                         writes the situations and the agent that checks their key: neither sees any heading)
  ARTICLE-SECTIONS.md    the whole text with each section's id, level and heading (for the headings writer)
  CONTENTS-NOW.json      [{id, level, heading, words}] of the headings the sidebar lists (h1-h4), for toc_check.py
  TOC-NOW-SIDEBAR.md     the contents as the sidebar shows it, numbered lines; TOC-NOW-FULL.md the same, whole headings
  LINES-NOW.json         [{n, id}]: a reader's line number to its section id
"""
import json, os, re, sys
from bs4 import BeautifulSoup, Tag

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', '..', '..', 'tools', 'humanization'))
import toc_sidebar as ts


def words(t):
    return len(re.findall(r"[\w’'\-]+", t))


def text_of(tag):
    return re.sub(r'\s+', ' ', tag.get_text(' ', strip=True)).strip()


def sections_of(html):
    soup = BeautifulSoup(html, 'html.parser')
    cur = {'idx': 0, 'level': 0, 'heading': '(before the first heading)', 'texts': []}
    out = [cur]
    for b in soup.children:
        if not isinstance(b, Tag):
            continue
        if re.fullmatch(r'h[1-6]', b.name or ''):
            # a heading's inline markup (Awareness<strong>es</strong>) joins without a space, as the sidebar shows it
            cur = {'idx': len(out), 'level': int(b.name[1]), 'heading': re.sub(r'\s+', ' ', b.get_text('')).strip(), 'texts': []}
            out.append(cur)
            continue
        t = text_of(b)
        if t:
            cur['texts'].append(t)
    for s in out:
        s['id'] = 'S%03d' % s['idx']
        s['own_words'] = words(' '.join(s['texts']))
    return out


def contents_of(S):
    """The headings the sidebar lists (h1-h4), each with its own words plus any h5/h6 sections folded under it."""
    out = []
    for s in S:
        if s['level'] == 0:
            continue
        if s['level'] > 4 and out:
            out[-1]['words'] += s['own_words']
            continue
        if not s['heading']:
            continue
        out.append({'id': s['id'], 'level': s['level'], 'heading': s['heading'], 'words': s['own_words']})
    return out


def render(entries, title, sidebar):
    lines, nums = ['# ' + title, '', 'Line, level and heading, then the words under it.', ''], []
    for n, e in enumerate(entries, 1):
        h = ts.shown(e['heading'], e['level'])[1] if sidebar else e['heading']
        lines.append('%02d.  %s%s %s  (%d words)' % (n, '    ' * (e['level'] - 1), '#' * e['level'], h, e['words']))
        nums.append({'n': n, 'id': e['id']})
    return '\n'.join(lines) + '\n', nums


def main(path):
    S = sections_of(open(path, encoding='utf-8').read())
    json.dump([{k: s[k] for k in ('id', 'level', 'heading', 'own_words')} | {'text': '\n\n'.join(s['texts'])} for s in S],
              open(os.path.join(HERE, 'SECTIONS.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    with open(os.path.join(HERE, 'TEXT-NO-HEADINGS.md'), 'w', encoding='utf-8') as f:
        f.write('# The guide\'s text, its headings taken out\n\nEach section starts with its id in brackets.\n\n')
        for s in S:
            f.write('[%s]\n\n%s\n\n' % (s['id'], '\n\n'.join(s['texts']) or '(no text of its own)'))
    with open(os.path.join(HERE, 'ARTICLE-SECTIONS.md'), 'w', encoding='utf-8') as f:
        f.write('# The guide, section by section\n\nEach section: [id] (level) heading, then its own text.\n\n')
        for s in S:
            f.write('[%s] (h%d) %s\n\n%s\n\n' % (s['id'], s['level'], s['heading'], '\n\n'.join(s['texts']) or '(no text of its own)'))
    C = contents_of(S)
    json.dump(C, open(os.path.join(HERE, 'CONTENTS-NOW.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    side, nums = render(C, 'Contents as the sidebar shows it', True)
    full, _ = render(C, 'Contents with whole headings', False)
    open(os.path.join(HERE, 'TOC-NOW-SIDEBAR.md'), 'w', encoding='utf-8').write(side)
    open(os.path.join(HERE, 'TOC-NOW-FULL.md'), 'w', encoding='utf-8').write(full)
    json.dump(nums, open(os.path.join(HERE, 'LINES-NOW.json'), 'w'), indent=0)
    cut = sum(1 for e in C if not ts.shown(e['heading'], e['level'])[0])
    print('%d sections, %d listed in the sidebar, %d cut off, %d words' % (len(S), len(C), cut, sum(s['own_words'] for s in S)))


if __name__ == '__main__':
    main(sys.argv[1])
