#!/usr/bin/env python3
"""post_embeds.py - every picture, video, audio and post card in a published Substack post, from its HTML, with the words
just before each; and which of them an article's Markdown has no note for.

Lesson E341. On the turn-116 marking page I asked Joel to keep "these seven" pictures and videos of the live Inner Child
post; the post has eleven. I had listed them from the last guide's notes and memory, not from the post, and missed the
mantra video, the Cosmic Jackpot picture, the Treasuring post card and Key's audio meditation. Joel, 2026-11-03 23:32 UTC:
"you didn't see that one in the original guide? ... i hope you're not losing other embeds from the original". So the
list comes from the post itself: save its page (the browser's, signed in or not), and run this on it.

  python3 tools/humanization/post_embeds.py POST.html [--article ARTICLE.md]

Each line: the kind (picture, video, audio, post card), its id or address, and the end of the paragraph before it. With
--article, each one the article's IMAGE and EMBED notes (article_images.py) don't name, by its id or address, is
listed as MISSING, and the exit is 1."""
import argparse
import html as htmlmod
import pathlib
import re
import sys

# The editor HTML he pastes (rather than the published page) marks a YouTube video only by its class, "youtube-wrap", with
# no data-component-name; and "<p" must be a whole tag name, or a picture's own <picture> tag reads as a paragraph that runs
# to the next </p>, past the video after it: bad trips turn 4 (2026-11-04), where his pasted post's four videos were
# missing from the list.
BLOCK = re.compile(r'<(p|h[1-6])(?=[\s>])[^>]*>(.*?)</\1>|data-component-name="([A-Za-z0-9]+)"|class="(youtube-wrap)"', re.S)
KINDS = {'Image2ToDOM': 'picture', 'VideoEmbedPlayer': 'video', 'AudioEmbedPlayer': 'audio', 'Youtube2ToDOM': 'video',
         'DigestPostEmbed': 'post card', 'EmbeddedPostToDOM': 'post card', 'youtube-wrap': 'video'}


def body_of(page):
    """The post's body: from its "body markup" div to the end of the article, or the whole page."""
    i = page.find('class="body markup"')
    if i < 0:
        return page
    j = page.find('</article>', i)
    return page[i:j if j > 0 else len(page)]


def ref_of(kind, ctx):
    """The id or address that names an embed, from the HTML around its marker."""
    pats = {'picture': r'images%2F([0-9a-f]{8}-[0-9a-f-]{27,}[^%"&]*?)(?:"|%|&| )',
            'video': r'videoId(?:&quot;|"):(?:&quot;|")([A-Za-z0-9_-]{11})|media-upload-id="([0-9a-f-]{36})"',
            'audio': r'/audio/upload/([0-9a-f-]{36})|mediaUploadId(?:&quot;|"):(?:&quot;|")([0-9a-f-]{36})',
            'post card': r'href="(https?://[^"/]+/p/[a-z0-9-]+)|canonical_url(?:&quot;|"):(?:&quot;|")(https?://[^&"]+/p/[a-z0-9-]+)'}
    m = re.search(pats[kind], ctx)
    return next((g for g in m.groups() if g), '') if m else ''


def cards_in_data(page):
    """The posts the page's own data embeds (their canonical addresses), the post itself left out."""
    own = re.search(r'rel="canonical" href="([^"]+)"', page)
    urls = re.findall(r'canonical_url(?:&quot;|"):(?:&quot;|")(https?://[^&"]+/p/[a-z0-9-]+)', page)
    seen, out = set(), []
    for u in urls:
        if (own and u == own.group(1)) or u in seen:
            continue
        seen.add(u)
        out.append(u)
    return out


def embeds(page):
    """[(kind, ref, the end of the paragraph before)] for every embed in the post's body, once each, in order."""
    body = body_of(page)
    last, out, seen = '', [], set()
    for m in BLOCK.finditer(body):
        if m.group(1):
            t = htmlmod.unescape(re.sub(r'<[^>]+>', '', m.group(2))).strip()
            if t:
                last = t
            continue
        kind = KINDS.get(m.group(3) or m.group(4))
        if not kind:
            continue
        tag = body.rfind('<', 0, m.start())   # the element's own opening tag (a YouTube embed's id is in it)
        if kind == 'picture':
            ctx = body[max(0, m.start() - 400):m.start() + 1500]
        elif kind == 'post card':                # up to the next paragraph, so a link after the card isn't taken for it
            nxt = body.find('<p', m.start())
            ctx = body[tag:nxt if nxt > 0 else m.start() + 6000]
        else:
            ctx = body[tag:m.start() + 6000]
        ref = ref_of(kind, ctx)
        if not ref and kind == 'post card':   # a video post's card has no link in the page, only in its data
            ref = next((u for u in cards_in_data(page) if u not in {r for _, r, _ in out}), '')
        key = (kind, ref or last)
        if key in seen:
            continue
        seen.add(key)
        out.append((kind, ref, last[-100:]))
    return out


def missing(found, md):
    """The embeds whose id or address no IMAGE or EMBED note of the article names."""
    notes = ' '.join(re.findall(r'<!--\s*(?:IMAGE|EMBED)\s+(\S+)', md))
    return [e for e in found if not e[1] or e[1].split('_')[0] not in notes]


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('post')
    ap.add_argument('--article')
    a = ap.parse_args(argv)
    found = embeds(pathlib.Path(a.post).read_text(encoding='utf-8'))
    for kind, ref, before in found:
        print('%-9s %-48s after: ...%s' % (kind, ref or '(no id found)', before[-70:]))
    print('%d in the post' % len(found))
    if not a.article:
        return 0
    gone = missing(found, pathlib.Path(a.article).read_text(encoding='utf-8'))
    for kind, ref, before in gone:
        print('MISSING %s %s (after: ...%s)' % (kind, ref or '(no id)', before[-60:]))
    print('%d of them have no note in the article' % len(gone))
    return 1 if gone else 0


if __name__ == '__main__':
    sys.exit(main())
