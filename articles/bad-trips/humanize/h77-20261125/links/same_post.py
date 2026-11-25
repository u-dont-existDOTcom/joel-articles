"""same_post.py - the guide's links to its own sections in the form that scrolls, from the repo root:

  python3 articles/bad-trips/humanize/h77-20261125/links/same_post.py

Joel, 2026-11-25 11:18 UTC (the contents lane): "i notice that your anchor links are reloading the whole page, don't you
need to fix them to be just # without the url before it?" and 16:14 UTC: "fixing thea nchor links for the other guides"
(lesson toc-2026-11-25c; the contents lane's promise 2, this lane's promise 2). Inside the post a link to one of its own
sections is "#§<slug>"; the /i/<post id>/<slug> form loads the page again. Every such link in the guide becomes the
same-post form here, no word changes (the checks read the text without its links), and the catalog's links are read
again from the guide as it stands, each one checked against a heading's anchor.
"""
import json
import pathlib
import re
import sys

REPO = pathlib.Path(__file__).resolve().parents[5]
sys.path.insert(0, str(REPO / 'tools' / 'humanization'))
import section_links as SL  # noqa: E402

ART = REPO / 'articles' / 'bad-trips'
BL = ART / 'GUIDE-SO-FAR-blocks.json'
CAT = ART / 'SECTION-LINKS.json'
OLD = re.compile(r'\]\(https://ibogaqueen\.substack\.com/i/170920118/([a-z0-9-]+)\)')
LINK = re.compile(r'\[([^\]]+)\]\((#§[^)]+)\)')


def main():
    blocks = json.loads(BL.read_text(encoding='utf-8'))
    cat = json.loads(CAT.read_text(encoding='utf-8'))
    anchors = {h['anchor'] for h in cat['headings']}
    n, sec, links, bad = 0, None, [], []
    for x in blocks:
        x['md'], k = OLD.subn(lambda m: '](#§%s)' % m.group(1), x['md'])
        n += k
        if x['kind'] in ('h1', 'h2', 'h3'):
            sec = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', x['md'].lstrip('#').strip()).replace('**', '')
        for text, href in LINK.findall(x['md']):
            slug = href[2:]
            if slug not in anchors:
                bad.append((x['id'], text, href))
            links.append({'in': sec, 'block': x['id'], 'text': text.replace('*', ''), 'href': href})
    if bad:
        sys.exit('no heading has this anchor: %r' % bad)
    cat['links'] = links
    cat['source'] = (cat['source'].split('; links read again')[0]
                     + '; links read again from the guide 2026-11-25 (turn 69), every one in the same-post form "#§slug"')
    (ART / 'GUIDE-SO-FAR.md').write_text('\n\n'.join(x['md'] for x in blocks) + '\n', encoding='utf-8')
    BL.write_text(json.dumps(blocks, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    CAT.write_text(json.dumps(cat, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print('%d links changed; %d same-post links in the guide, each on a heading\'s anchor' % (n, len(links)))


if __name__ == '__main__':
    main()
