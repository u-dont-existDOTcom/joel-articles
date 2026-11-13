#!/usr/bin/env python3
"""said_twice.py - before a text goes into an article, the studies and pages it cites that the article already cites
elsewhere: the same link in two places is most often the same thing said twice (lesson bad-trips-2026-11-13a).

Joel, 2026-11-13 14:59 UTC, after his DMSO text went into the bad trips guide's DMSO section whole, describing Lu & Mattson
2001, which his own evidence paragraph in My Brain Feels Damaged already described: "also i wasn't clear on why Lu &
Mattson need to be described in 2 places, maybe we can merge that?" The turn that put it in had seen both and kept both
because both were his words. Gate E376 already says a point said in two places is merged into one; nothing made the
second place show up when the new text went in. A link is an exact question (the same URL), so code finds it; whether the
two places say the same thing is a reader's judgment, made on what this lists.

  python3 tools/humanization/said_twice.py ARTICLE.md NEW.md [--exclude-new]

NEW.md is the text about to go in (Markdown, with its links). Lists each URL of NEW.md that ARTICLE.md has outside it,
with each other place's line. Exit 1 when there is any, so an apply script can stop on it until each is merged or kept
with why. As a module: places(article_md, new_md) -> {url: [lines elsewhere]}.
"""
import re
import sys

LINK = re.compile(r'\]\((https?://[^)\s]+)\)')


def norm(url):
    return url.rstrip('/').replace('http://', 'https://').split('?')[0].split('#')[0]


def places(article_md, new_md):
    """{url: [each line of the article outside NEW that links the same url]}."""
    rest = article_md.replace(new_md, '') if new_md and new_md in article_md else article_md
    out = {}
    for url in dict.fromkeys(norm(u) for u in LINK.findall(new_md)):
        hits = [ln.strip() for ln in rest.split('\n') if any(norm(u) == url for u in LINK.findall(ln))]
        if hits:
            out[url] = hits
    return out


def main(argv):
    if len(argv) < 3:
        print(__doc__)
        return 2
    art = open(argv[1], encoding='utf-8').read()
    new = open(argv[2], encoding='utf-8').read().strip()
    found = places(art, new)
    for url, hits in found.items():
        print('ALSO CITED ELSEWHERE: %s' % url)
        for h in hits:
            print('   - %s' % (h[:240] + ('...' if len(h) > 240 else '')))
    if not found:
        print('none: no link of the new text is cited elsewhere in the article')
    return 1 if found else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
