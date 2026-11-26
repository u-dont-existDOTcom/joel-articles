#!/usr/bin/env python3
"""live_markdown.py - the somatic guide as it is live (LIVE-BODY-20261126.html, fetched 2026-11-26) as the Markdown the
marking page reads: every block in order, links, bold and italics kept, each picture an IMAGE note and each video, post
card or Instagram post an EMBED note (tools/humanization/article_images.py), the horizontal rules left out.

  python3 articles/somatic-therapies/experiments/additions-20261126/live_markdown.py

Writes WHOLE-LIVE-20261126.md next to this file.
"""
import html
import json
import pathlib
import re
import sys

from bs4 import BeautifulSoup, NavigableString, Tag

HERE = pathlib.Path(__file__).resolve().parent
SRC = HERE / 'LIVE-BODY-20261126.html'
OUT = HERE / 'WHOLE-LIVE-20261126.md'


def inline(node):
    """A block's inline content as Markdown."""
    out = []
    for c in node.children:
        if isinstance(c, NavigableString):
            out.append(str(c))
            continue
        if not isinstance(c, Tag):
            continue
        inner = inline(c)
        if c.name == 'a' and c.get('href'):
            out.append('[%s](%s)' % (inner, c['href']) if inner.strip() else '')
        elif c.name in ('strong', 'b'):
            out.append('**%s**' % inner if inner.strip() else inner)
        elif c.name in ('em', 'i'):
            out.append('*%s*' % inner if inner.strip() else inner)
        elif c.name == 'br':
            out.append(' ')
        else:
            out.append(inner)
    s = ''.join(out)
    s = re.sub(r'\*\*(\s+)\*\*', r'\1', s)
    return re.sub(r'[ \t\r\n]+', ' ', s).strip()


def attrs(b):
    try:
        return json.loads(b.get('data-attrs') or '{}')
    except ValueError:
        return {}


def note(kind, url, desc):
    desc = ' '.join((desc or '').replace('-->', '').split())
    return '<!-- %s %s : %s -->' % (kind, url, desc)


def convert(body_html):
    blocks = []
    for b in BeautifulSoup(body_html, 'html.parser').children:
        if not isinstance(b, Tag):
            continue
        cls = ' '.join(b.get('class') or [])
        if b.name in ('h1', 'h2', 'h3', 'h4', 'h5', 'h6'):
            t = inline(b)
            if t:
                blocks.append('#' * int(b.name[1]) + ' ' + t)
        elif b.name == 'p' and 'button-wrapper' in cls:
            a = attrs(b)
            blocks.append(note('EMBED', a.get('url', ''), 'Button: "%s"' % a.get('text', '')))
        elif b.name == 'p':
            t = inline(b)
            if t:
                blocks.append(t)
        elif b.name in ('ul', 'ol'):
            for k, li in enumerate(b.find_all('li', recursive=False), 1):
                t = inline(li.find('p') or li) if li.find('p') else inline(li)
                if li.find_all('p'):
                    t = ' '.join(inline(p) for p in li.find_all('p'))
                blocks.append(('- ' if b.name == 'ul' else '%d. ' % k) + t)
        elif 'captioned-image-container' in cls:
            img = b.find('img')
            src = img.get('src', '') if img else ''
            m = re.search(r'(https://substack-post-media\.s3\.amazonaws\.com/public/images/[^\s,"]+)', html.unescape(str(b)))
            if m:
                src = m.group(1)
            cap = b.find('figcaption')
            desc = (cap.get_text(' ', strip=True) if cap else '') or (img.get('alt') if img else '') or 'a picture in the post'
            blocks.append(note('IMAGE', src, desc))
        elif 'youtube-wrap' in cls:
            a = attrs(b)
            blocks.append(note('EMBED', 'https://www.youtube.com/watch?v=%s' % a.get('videoId', ''), 'YouTube video'))
        elif 'digest-post-embed' in cls:
            a = attrs(b)
            url = a.get('url') or (b.find('a') or {}).get('href', '') if b.find('a') else a.get('url', '')
            blocks.append(note('EMBED', url or 'substack-post', 'Post card: "%s"' % html.unescape(a.get('title', ''))))
        elif 'native-video-embed' in cls:
            a = attrs(b)
            blocks.append(note('EMBED', 'substack-video:%s' % a.get('mediaUploadId', ''), 'a video uploaded to the post'))
        elif 'instagram-embed-wrap' in cls:
            a = attrs(b)
            blocks.append(note('EMBED', 'https://www.instagram.com/p/%s/' % a.get('instagram_id', ''),
                               'Instagram post: %s' % html.unescape(a.get('title', ''))))
        elif 'callout-block' in cls:
            for p in b.find_all(['p', 'h1', 'h2', 'h3', 'h4']):
                t = inline(p)
                if t:
                    blocks.append(('#' * int(p.name[1]) + ' ' if p.name.startswith('h') else '') + t)
        elif b.name == 'div' and b.find('hr') and not b.get_text(strip=True):
            continue
        else:
            t = inline(b)
            if t:
                blocks.append(t)
            else:
                sys.stderr.write('left out: %s\n' % str(b)[:120])
    return '\n\n'.join(blocks) + '\n'


if __name__ == '__main__':
    OUT.write_text(convert(SRC.read_text(encoding='utf-8')), encoding='utf-8')
    print(OUT)
