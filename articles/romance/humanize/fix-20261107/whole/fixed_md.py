#!/usr/bin/env python3
"""The fixed version as one Markdown file, FIXED.md: the whole post in order (its copy of 2026-11-22,
live-check/LIVE-POST-BLOCKS-20261122.jsonl), every changed paragraph as REPLACEMENTS.json has it, headings at their
levels, the post's links as Markdown links, and its pictures, videos and Instagram posts as IMAGE and EMBED notes
(tools/humanization/article_images.py) where they sit, plus the embed he asked for (r30/HIS-T4.json).

It is the text every read of the whole article and every marking page starts from (Joel, 2026-11-22 22:24 UTC: "it
would have helped if you just had the whole page so i could see the whole context"). A link in a changed paragraph is
kept where its words are still there once; the live update carries the rest from the editor HTML
(tools/humanization/substack_merge.py)."""
import argparse
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
ap = argparse.ArgumentParser()
ap.add_argument('--repl', default='REPLACEMENTS.json', help='the replacements to apply (REPLACEMENTS-CHECKS.json: the '
                'fixed version as it stood before his answers of 2026-11-22)')
ap.add_argument('--no-layer', action='store_true', help='without his answers\' links and embed')
ap.add_argument('--out', default='FIXED.md')
A = ap.parse_args()
POSTF = HERE.parent / 'live-check' / 'LIVE-POST-BLOCKS-20261122.jsonl'
recs = [json.loads(l) for l in POSTF.read_text(encoding='utf-8').splitlines()]
REPL = {int(k): v for k, v in json.loads((HERE / A.repl).read_text(encoding='utf-8')).items()}
LAYER = json.loads((HERE.parent / 'r30' / 'HIS-T4.json').read_text(encoding='utf-8'))
if A.no_layer:
    LAYER = {'links': [], 'changes': [], 'embeds': []}
extra_links = {}
for l in LAYER['links']:
    extra_links.setdefault(l['card'], []).append((l['words'], l['href']))
card_of = {}
for ch in LAYER['changes']:
    for n in ([ch['live']] if ch['kind'] == 'para' else ch['live'][:1]):
        card_of[n] = ch['card']
embed_after = {}
for e in LAYER['embeds']:
    embed_after.setdefault(int(e['card'][2:]), []).append(e)


def linked(text, links):
    """Each link's words, where they appear once, as a Markdown link. Words given as "before |words" link only the
    words after the bar, found by the whole phrase (r30/HIS-T4.json: "And |breathwork")."""
    out = text
    for words, href in links:
        before, _, w = words.rpartition('|')
        find = before + w
        if not w or out.count(find) != 1 or ('[' + w) in out:
            continue
        out = out.replace(find, '%s[%s](%s)' % (before, w, href), 1)
    return out


recs_by_n = {r['n']: r for r in recs if r.get('n') is not None}
lines = []
prev_n = None
for k, r in enumerate(recs):
    tag = r['tag']
    if tag == 'EMBED':
        e = r['embed']
        kind = e.get('kind')
        if kind == 'youtube-wrap':
            v = e['attrs']['videoId']
            lines.append('<!-- EMBED https://www.youtube.com/watch?v=%s : a YouTube video -->' % v)
        elif kind == 'instagram-embed-wrap':
            a = e['attrs']
            lines.append('<!-- EMBED https://www.instagram.com/p/%s/ : Instagram post, %s -->' % (
                a.get('instagram_id'), (a.get('title') or a.get('author_name') or '').replace('--', '-')))
        elif kind == 'img':
            lines.append('<!-- IMAGE %s : a picture in the post%s -->' % (
                e.get('src', ''), (', ' + e['alt'].replace('--', '-')) if e.get('alt') else ''))
        continue
    n = r.get('n')
    text = r['text']
    if tag == 'H1':
        lines.append('# ' + linked(text, [tuple(l) for l in r.get('links', [])]))
        continue
    if n is None or n >= 457:      # 457: the Subscribe button's line
        continue
    if tag == 'P' and prev_n is not None and recs_by_n[prev_n]['tag'] == 'LI' and recs_by_n[prev_n]['text'] == text:
        prev_n = n
        continue
    prev_n = n
    if tag in ('H2', 'H3', 'H4'):
        lines.append('#' * int(tag[1]) + ' ' + text)
        continue
    if n in REPL:
        new = REPL[n]
        links = [tuple(l) for l in r.get('links', [])] + extra_links.get(card_of.get(n, ''), [])
        for p in new:
            lines.append(('- ' if tag == 'LI' else '') + linked(p, links))
    else:
        lines.append(('- ' if tag == 'LI' else '') + linked(text, [tuple(l) for l in r.get('links', [])]))
    for e in embed_after.get(n, []):
        lines.append('<!-- EMBED %s : Instagram reel he asked for here (2026-11-22) -->' % e['url'])

md = '\n\n'.join(lines) + '\n'
(HERE / A.out).write_text(md, encoding='utf-8')
words = len(re.sub(r'<!--.*?-->', '', md, flags=re.S).split())
print('%s: %d blocks, %d words' % (A.out, len(lines), words))
