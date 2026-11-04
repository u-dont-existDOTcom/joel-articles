#!/usr/bin/env python3
"""make_plan.py: UPDATE-PLAN.json, what post 176569317's editor must hold after the update (2026-11-04).

SOURCE is r11 (r10 with the one slip of ours the pre-publish reads found, fixed).

Joel, 2026-11-04 20:27 UTC: "publish it (don't email anyone)". His post "Healing the Gut Naturally"
(https://ibogaqueen.substack.com/p/healing-the-gut-naturally) gets the article as SOURCE says, in its editor, as one
transaction (the way the hypnosis guide went in on 2 November, gate E332's first update): the HTML parsed with the editor's
own schema, the post's own native blocks (its two pictures, three YouTube videos and the paywall) carried over as the
same nodes, never pasted.

The plan holds:
- source: the article HTML's path and SHA-256 (the tab fetches it from a pushed commit and checks it);
- base: the editor's text blocks now (the master's, which the editor was checked equal to before anything changed);
- after: the text blocks the editor must hold, in order, whitespace removed, with "<captionedImage>", "<youtube2:ID>"
  and "<paywall>" where the native blocks go.

  python3 articles/healing-the-gut/humanize/fix-20261103/live/make_plan.py [SOURCE.html]
"""
import hashlib
import json
import pathlib
import re
import sys

from bs4 import BeautifulSoup

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[4]
SOURCE = pathlib.Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else HERE.parent / 'r11' / 'r11.html'
MASTER = REPO / 'articles' / 'healing-the-gut' / 'master.html'
TEXT = ('p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6')


def blocks(html):
    s = BeautifulSoup(html, 'html.parser')
    root = s.find(class_='ProseMirror') or s
    out = []

    def walk(el):
        for k in el.children:
            name = getattr(k, 'name', None)
            if not name:
                continue
            cls = ' '.join(k.get('class') or [])
            if 'paywall-editor' in cls:
                out.append('<paywall>')
            elif 'captioned-image-container' in cls:
                out.append('<captionedImage>')
            elif 'youtube-wrap' in cls:
                attrs = json.loads(k.get('data-attrs') or '{}')
                out.append('<youtube2:%s>' % attrs.get('videoId', ''))
            elif name == 'hr':
                out.append('<horizontalRule>')
            elif name in TEXT:
                t = re.sub(r'\s+', '', k.get_text())
                if t:
                    out.append(t)
            else:
                walk(k)

    walk(root)
    return out


def main():
    src = SOURCE.read_bytes()
    plan = {
        'post': 176569317,
        'url': 'https://ibogaqueen.substack.com/p/healing-the-gut-naturally',
        'source': {'path': str(SOURCE.relative_to(REPO)), 'sha256': hashlib.sha256(src).hexdigest()},
        'base': blocks(MASTER.read_text(encoding='utf-8')),
        'after': blocks(src.decode('utf-8')),
    }
    for k in ('base', 'after'):
        kinds = [b for b in plan[k] if b.startswith('<') and b != '<horizontalRule>']
        plan[k + '_natives'] = kinds
    assert [b.split(':')[0] for b in plan['base_natives']] == [b.split(':')[0] for b in plan['after_natives']], (
        plan['base_natives'], plan['after_natives'])
    out = HERE / 'UPDATE-PLAN.json'
    out.write_text(json.dumps(plan, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print(out.name, hashlib.sha256(out.read_bytes()).hexdigest(), 'base', len(plan['base']), 'after', len(plan['after']),
          plan['after_natives'])


if __name__ == '__main__':
    main()
