#!/usr/bin/env python3
"""Turn 124: his live post as it is before anything replaces it (gate E332: check the editor against what was last put in,
replace only what changed), against what this lane last had of it and against his guide.

LIVE-POST-20261104-1520.json is Substack's public API answer for the post (https://ibogaqueen.substack.com/p/inner-child-self-
love-tips-and-guided, post 189761959), fetched on his laptop on 2026-11-04 at 15:20 UTC; Substack last saved it on
2026-11-03 at 22:29 UTC. master.html is the lane's copy of its editor body of 2026-09-20. Every paragraph, heading and list
item of each is compared by its words (quote marks, dashes, spaces and case aside): the live post's blocks master.html
doesn't have are the post's changes since September; of those, the ones whose opening words are in neither his reorganized
guide (experiments/t116-joel/JOEL-GUIDE-20261103.md) nor the article are the ones a replacement of the post would drop
unseen. Writes LIVE-COMPARE.json and LIVE-COMPARE.md.
  python3 articles/inner-child-therapy/experiments/t124-live/compare_live.py"""
import difflib
import json
import pathlib
import re

from bs4 import BeautifulSoup

HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parents[1]
SAME = str.maketrans({'‘': "'", '’': "'", '“': '"', '”': '"', '\xa0': ' ', '–': '-', '—': '-'})


def norm(s):
    return re.sub(r'\s+', ' ', s.translate(SAME)).strip().lower()


def blocks(html):
    soup = BeautifulSoup(html, 'html.parser')
    out = []
    for el in soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'li']):
        if el.name == 'p' and el.find_parent('li'):
            continue
        t = el.get_text(' ')
        if norm(t):
            out.append({'tag': el.name, 'text': re.sub(r'\s+', ' ', t).strip()})
    return out


live = json.loads((HERE / 'LIVE-POST-20261104-1520.json').read_text(encoding='utf-8'))
post = live.get('post', live)
L = blocks(post['body_html'])
M = blocks((ART / 'master.html').read_text(encoding='utf-8'))
mset = {norm(b['text']) for b in M}
lset = {norm(b['text']) for b in L}
plain = lambda p: norm(re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', p.read_text(encoding='utf-8')).replace('**', '').replace('*', ''))
guide = plain(ART / 'experiments/t116-joel/JOEL-GUIDE-20261103.md')
article = plain(ART / 'HUMANIZED-ARTICLE-SO-FAR.md')
new = [dict(b, n=i) for i, b in enumerate(L) if norm(b['text']) not in mset]
oct3 = norm((ART / 'source/inner-child-guide-substack-20261003.txt').read_text(encoding='utf-8'))
paras = [norm(re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', x).replace('**', '').replace('*', ''))
         for x in re.split(r'\n\s*\n', (ART / 'HUMANIZED-ARTICLE-SO-FAR.md').read_text(encoding='utf-8')) if x.strip()]
for b in new:
    head = norm(b['text'])[:60]
    b['in_guide'] = head in guide
    b['in_article'] = head in article
    b['in_oct3_post'] = head in oct3   # the post as he updated it on 2026-10-03 (the lane's copy)
    if not (b['in_guide'] or b['in_article']):
        best = max(paras, key=lambda x: difflib.SequenceMatcher(None, norm(b['text'])[:300], x[:300]).ratio())
        b['nearest_in_article'] = best[:160]
        b['nearest_ratio'] = round(difflib.SequenceMatcher(None, norm(b['text']), best).ratio(), 2)
gone = [b for b in M if norm(b['text']) not in lset]
res = {'post': {'id': post['id'], 'title': post['title'], 'url': post['canonical_url'], 'updated_at': post['updated_at'],
                'wordcount': post.get('wordcount'), 'body_html_chars': len(post['body_html'])},
       'live_blocks': len(L), 'master_blocks': len(M), 'live_not_in_master': len(new), 'master_not_in_live': len(gone),
       'live_only_not_in_guide_or_article': sum(1 for b in new if not (b['in_guide'] or b['in_article'])),
       'new': new, 'gone': gone}
(HERE / 'LIVE-COMPARE.json').write_text(json.dumps(res, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
md = ['# His live post against our September copy and his guide', '',
      'The post: [%s](%s), last saved by Substack on %s; %d blocks (master.html, 2026-09-20: %d).' % (
          post['title'], post['canonical_url'], post['updated_at'], len(L), len(M)), '',
      '%d of the live post\'s blocks aren\'t in master.html; %d of those open with words in neither his guide nor the article. '
      '%d of master.html\'s blocks are gone from the live post. Made by compare_live.py.' % (
          len(new), res['live_only_not_in_guide_or_article'], len(gone)), '',
      '## The live post\'s blocks since September, not in his guide or the article', '']
md += ['%d. (%s, block %d; %s; the nearest paragraph of the article, %d%% alike: "%s ...") %s' % (
    k + 1, b['tag'], b['n'], 'in his post of 2026-10-03' if b['in_oct3_post'] else 'not in his post of 2026-10-03',
    100 * b['nearest_ratio'], b['nearest_in_article'][:90], b['text'])
    for k, b in enumerate([b for b in new if not (b['in_guide'] or b['in_article'])])]
md += ['', '## The live post\'s other blocks since September (in his guide or the article)', '']
md += ['- (%s, block %d) %s' % (b['tag'], b['n'], b['text'][:200]) for b in new if b['in_guide'] or b['in_article']]
(HERE / 'LIVE-COMPARE.md').write_text('\n'.join(l.rstrip() for l in md) + '\n', encoding='utf-8')
print(json.dumps({k: v for k, v in res.items() if k not in ('new', 'gone')}, ensure_ascii=False))
