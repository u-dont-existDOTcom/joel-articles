#!/usr/bin/env python3
"""Turn 127: PUBLISH-PLAN.json, the publish draft's plan for publish_build.js and publish_dispatch.js in his post's
editor (https://ibogaqueen.substack.com/publish/post/189761959): his guide as round 11 read it
(HUMANIZED-ARTICLE-SO-FAR.md, the text of ../t126-substack/TEXT-A.txt and TEXT-B.txt, now with its links and emphasis)
as the post's whole body, the way the hypnosis lane put its guide in on 2 and 3 November
(articles/inner-signal/humanize/fix-20261103/live/): parsed with the editor's own schema, one transaction, no paste.

Where the article's notes say:
  - the post's own eleven native blocks are carried over as they are (the four pictures, the video, the audio, the
    three YouTube embeds, the two post cards), found in the editor by what they hold; the mantra video's start moves
    from 0:54 to the 0:58 he gave on F2 (turn 117); the demon picture keeps its caption, "Yep. Exactly like that.",
    so that line isn't a paragraph of its own as well;
  - the two new YouTube embeds are added, and his six new pictures, uploaded to Substack in turn 127 from his own files
    (UPLOADS.json: each file's SHA-256 his file's, before and after the upload);
  - the paragraph after the PULL QUOTE note is a pull quote block (his answer on F4, 2026-11-03 23:32 UTC).
The text is built from the same Markdown the round-11 payloads were (make_payloads.py: the notes out, the quote marks
curled with curl() before the split, ptext.plain's reading of links and emphasis), and every block's text is checked
here against round 11's, so the post says word for word what Pangram read. His document has no block quotes or
dividers, so the post has none.

  python3 make_publish.py            writes PUBLISH-PLAN.json and prints its counts"""
import hashlib
import html
import json
import pathlib
import re
import sys
import urllib.parse

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
SRC = ROOT / 'articles/inner-child-therapy/HUMANIZED-ARTICLE-SO-FAR.md'
R11 = HERE.parent / 't126-substack'
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
from paragraphs_alone import plain  # noqa: E402  (ptext.plain, as make_payloads.py)

OPENERS = set('([{—–-/')
ITEM = re.compile(r'^(?:[-*+]|\d+\.)\s+')
LINK = re.compile(r'\[([^\]]+)\]\(((?:[^()\s]|\([^()\s]*\))*)\)')
NOTE = re.compile(r'<!--(.*?)-->', re.S)
# Whitespace, by code point: update.js's list, so the editor's side strips exactly the same characters.
WS = frozenset(map(chr, [0x20, 0x09, 0x0a, 0x0d, 0x0c, 0x0b, 0x85, 0xa0, 0x1680, 0x2028, 0x2029, 0x202f, 0x205f, 0x3000,
                         0xfeff, 0x1c, 0x1d, 0x1e, 0x1f] + list(range(0x2000, 0x200b))))
BASE = {'nodes': 460, 'doc_json_sha256': 'b6c15e9701791c55e7be48a0995226c1a49ef1220a79e4f3577f55923e3d9bac',
        'draft_updated_at': '2026-11-03T22:29:23.548Z'}
CAPTION_OF = {'969adf28-c95f-4c96-bea8-3505a29137cc': 'Yep. Exactly like that.'}
MANTRA_START = {'foHCbX0xjAU': '58'}
POST_YOUTUBE = {'4PxC3zZ2Mus', '4TYvq-d0-XM', 'foHCbX0xjAU'}   # the post's own three YouTube embeds


def curl(s):
    """make_payloads.py's curl(), unchanged: an opening mark at the start, after a space or one of ( [ { — – - /, a
    closing mark or apostrophe elsewhere (a single opening mark only before a letter or digit)."""
    out = []
    for i, c in enumerate(s):
        prev = s[i - 1] if i else ' '
        nxt = s[i + 1] if i + 1 < len(s) else ' '
        if c == '"':
            out.append('“' if prev.isspace() or prev in OPENERS else '”')
        elif c == "'":
            out.append('‘' if (prev.isspace() or prev in OPENERS or prev in '"“') and nxt.isalnum() else '’')
        else:
            out.append(c)
    return ''.join(out)


def payload_blocks(md):
    """make_payloads.py's blocks(), unchanged: what round 11 pasted, as (kind, level, text or items)."""
    md = curl(re.sub(r'<!--.*?-->', '', md, flags=re.S))
    out = []
    for b in re.split(r'\n\s*\n', md):
        b = b.strip('\n')
        if not b.strip():
            continue
        if b.startswith('#'):
            out.append(('h', len(b.split(' ')[0]), plain(b)))
            continue
        lines = b.split('\n')
        if ITEM.match(lines[0]):
            items = []
            for l in lines:
                if ITEM.match(l):
                    items.append(ITEM.sub('', l).rstrip())
                else:
                    items[-1] += '\n' + l.strip()
            out.append(('ol' if re.match(r'^\d+\.', lines[0]) else 'ul', 0, [plain(x).replace(' \n', '\n') for x in items]))
            continue
        out.append(('p', 0, plain(b).replace(' \n', '\n')))
    return out


def chars(md):
    """One block's inline Markdown as [char, bold, italic, href]: a link as its text with its address, '**' and '*' as
    bold and italic switches that are not text (ptext.plain drops every '*')."""
    out, st = [], {'b': False, 'i': False}

    def emit(s, href):
        i = 0
        while i < len(s):
            if s.startswith('**', i):
                st['b'] = not st['b']
                i += 2
            elif s[i] == '*':
                st['i'] = not st['i']
                i += 1
            else:
                out.append([s[i], st['b'], st['i'], href])
                i += 1
    pos = 0
    for m in LINK.finditer(md):
        emit(md[pos:m.start()], None)
        emit(m.group(1), m.group(2))
        pos = m.end()
    emit(md[pos:], None)
    assert not st['b'] and not st['i'], 'emphasis left open: %r' % md[:80]
    return out


def normalized(md):
    """chars() read the way ptext.plain and make_payloads read text: runs of spaces and tabs one space, the ends
    stripped, no space before a line break."""
    cs = []
    for c in chars(md):
        if c[0] in ' \t' and cs and cs[-1][0] in ' \t':
            continue
        cs.append([' ' if c[0] == '\t' else c[0]] + c[1:])
    while cs and cs[0][0].isspace():
        cs.pop(0)
    while cs and cs[-1][0].isspace():
        cs.pop()
    return [c for i, c in enumerate(cs) if not (c[0] == ' ' and i + 1 < len(cs) and cs[i + 1][0] == '\n')]


def inline_html(cs):
    out, i = [], 0
    while i < len(cs):
        j = i
        while j < len(cs) and cs[j][1:] == cs[i][1:]:
            j += 1
        t = html.escape(''.join(c[0] for c in cs[i:j]), quote=False).replace('\n', '<br>')
        _, b, it, href = cs[i]
        if it:
            t = '<em>%s</em>' % t
        if b:
            t = '<strong>%s</strong>' % t
        if href:
            t = '<a href="%s">%s</a>' % (html.escape(href, quote=True), t)
        out.append(t)
        i = j
    return ''.join(out)


def text_of(cs):
    return ''.join(c[0] for c in cs)


def sig(text):
    return hashlib.sha256(''.join(c for c in text if c not in WS).encode('utf-8')).hexdigest()[:6]


def youtube(url):
    u = urllib.parse.urlparse(url)
    q = urllib.parse.parse_qs(u.query)
    vid = q['v'][0] if 'v' in q else u.path.rstrip('/').split('/')[-1]
    start = q.get('t', [None])[0]
    return vid, (start.rstrip('s') if start else None)


def native_item(kind, target, uploads):
    if kind == 'IMAGE':
        if target.startswith('https://substack-post-media.s3.amazonaws.com/'):
            item = {'k': 'carry', 'type': 'captionedImage', 'src': target}
            key = target.split('/')[-1].split('_')[0]
            if key in CAPTION_OF:
                item['caption'] = CAPTION_OF[key]
            return item
        name = urllib.parse.unquote(target.split('/')[-1])
        up = uploads[name]
        return {'k': 'new_image', 'from': target, 'src': up['url'], 'width': up['width'], 'height': up['height'],
                'bytes': up['bytes'], 'type': up['type']}
    if target.startswith('substack-video:'):
        return {'k': 'carry', 'type': 'video', 'mediaUploadId': target.split(':', 1)[1]}
    if target.startswith('substack-audio:'):
        return {'k': 'carry', 'type': 'audio', 'mediaUploadId': target.split(':', 1)[1]}
    if 'youtube.com' in target or 'youtu.be' in target:
        vid, start = youtube(target)
        if vid in POST_YOUTUBE:
            return {'k': 'carry', 'type': 'youtube2', 'videoId': vid, 'startTime': MANTRA_START.get(vid)}
        return {'k': 'new_youtube', 'videoId': vid, 'startTime': start}
    if target.startswith('https://ibogaqueen.substack.com/p/'):
        return {'k': 'carry', 'type': 'digestPostEmbed', 'canonical_url': target}
    raise ValueError('a note this script does not know: %s %s' % (kind, target))


def main():
    md = SRC.read_text(encoding='utf-8')
    uploads = {u['file']: u for u in json.loads((HERE / 'UPLOADS.json').read_text(encoding='utf-8'))['pictures']}
    notes = []

    def keep(m):
        body = m.group(1).strip()
        n = re.match(r'(IMAGE|EMBED)\s+(\S+)\s*:', body)
        if n:
            notes.append(('native', n.group(1), n.group(2)))
        elif body.startswith('PULL QUOTE'):
            notes.append(('pull', None, None))
        else:
            return ''
        return '\n\n@@NOTE%d@@\n\n' % (len(notes) - 1)
    for m in NOTE.finditer(md):   # each note stands on its own line, so the blocks around it are the payload's
        if re.match(r'\s*(IMAGE|EMBED)\s|\s*PULL QUOTE', m.group(1)):
            assert re.search(r'(^|\n)[ \t]*$', md[:m.start()]) and re.match(r'[ \t]*(\n|$)', md[m.end():]), \
                'a note inside a paragraph: %s' % m.group(0)[:80]
    marked = curl(NOTE.sub(keep, md))
    seq = []
    for b in re.split(r'\n\s*\n', marked):
        b = b.strip('\n')
        if not b.strip():
            continue
        m = re.fullmatch(r'\s*@@NOTE(\d+)@@\s*', b)
        if m:
            seq.append(('note', int(m.group(1))))
            continue
        if b.startswith('#'):
            lvl = len(b.split(' ')[0])
            seq.append(('h', lvl, normalized(re.sub(r'^#{1,6}\s+', '', b.strip()))))
            continue
        lines = b.split('\n')
        if ITEM.match(lines[0]):
            items = []
            for l in lines:
                if ITEM.match(l):
                    items.append(ITEM.sub('', l).rstrip())
                else:
                    items[-1] += '\n' + l.strip()
            seq.append(('ol' if re.match(r'^\d+\.', lines[0]) else 'ul', 0, [normalized(x) for x in items]))
            continue
        seq.append(('p', 0, normalized(b.strip())))

    # The text, block by block, is round 11's.
    mine = [(k, l, [text_of(x) for x in t] if k in ('ul', 'ol') else text_of(t)) for k, l, t in (s for s in seq if s[0] != 'note')]
    theirs = payload_blocks(md)
    assert len(mine) == len(theirs), (len(mine), len(theirs))
    for a, b in zip(mine, theirs):
        assert a == b, 'a block differs from round 11:\n%r\n%r' % (a, b)
    r11 = ''.join((R11 / ('TEXT-%s.txt' % x)).read_text(encoding='utf-8') for x in 'AB')
    joined = '\n\n'.join('\n'.join(t) if k in ('ul', 'ol') else t for k, _, t in theirs)
    assert ''.join(c for c in joined if c not in WS) == ''.join(c for c in r11 if c not in WS), 'not round 11 text'

    items, after, links, chunk, pull, consume = [], [], [], [], False, None
    counts = {'bold': 0, 'italic': 0, 'headings': {}}

    def flush():
        if chunk:
            items.append({'k': 'html', 'n': len(chunk), 'html': ''.join(chunk)})
            chunk.clear()
    for s in seq:
        if s[0] == 'note':
            kind, nk, target = notes[s[1]][0], notes[s[1]][1], notes[s[1]][2]
            if kind == 'pull':
                pull = True
                continue
            flush()
            it = native_item(nk, target, uploads)
            items.append(it)
            after.append('t:' + {'carry': it.get('type'), 'new_image': 'captionedImage', 'new_youtube': 'youtube2'}[it['k']])
            consume = it.get('caption')
            continue
        k, lvl, t = s
        if consume is not None:
            assert k == 'p' and text_of(t) == consume, 'the caption %r is not the next paragraph %r' % (consume, t)
            consume = None
            continue
        cs_all = [c for x in t for c in x] if k in ('ul', 'ol') else t
        for c in cs_all:
            if c[0] != '\n':   # a line break is a hardBreak node in the editor, not text
                counts['bold'] += c[1]
                counts['italic'] += c[2]
        prev = None
        for c in cs_all:
            if c[3] and c[3] != prev:
                links.append(c[3])
            prev = c[3]
        if k == 'h':
            counts['headings'][str(lvl)] = counts['headings'].get(str(lvl), 0) + 1
            block, text = '<h%d>%s</h%d>' % (lvl, inline_html(t), lvl), text_of(t)
        elif k in ('ul', 'ol'):
            block = '<%s>%s</%s>' % (k, ''.join('<li><p>%s</p></li>' % inline_html(x) for x in t), k)
            text = ''.join(text_of(x) for x in t)
        else:
            block, text = '<p>%s</p>' % inline_html(t), text_of(t)
        if pull:
            assert k == 'p'
            flush()
            items.append({'k': 'pullquote', 'html': block})
            after.append(sig(text))
            pull = False
            continue
        chunk.append(block)
        after.append(sig(text))
    flush()
    full = ''.join(c for k, _, t in theirs for c in ('\n'.join(t) if k in ('ul', 'ol') else t) if c not in WS)
    plan = {'about': __doc__.split('\n\n')[0].replace('\n', ' '),
            'source': {'file': str(SRC.relative_to(ROOT)), 'sha256': hashlib.sha256(SRC.read_bytes()).hexdigest()},
            'round11_words_sha256': {x['part']: x['words_sha256'] for x in json.loads((R11 / 'PAYLOADS.json').read_text(encoding='utf-8'))['parts']},
            'base': BASE, 'items': items, 'after': after, 'links': links, 'counts': counts,
            'text_sha256_no_whitespace': hashlib.sha256(full.encode('utf-8')).hexdigest(),
            'carried': sum(1 for i in items if i['k'] == 'carry')}
    (HERE / 'PUBLISH-PLAN.json').write_text(json.dumps(plan, ensure_ascii=False, indent=0) + '\n', encoding='utf-8')
    kinds = {}
    for i in items:
        kinds[i['k']] = kinds.get(i['k'], 0) + 1
    print('nodes after', len(after), '| items', kinds, '| links', len(links), '| bold chars', counts['bold'],
          '| italic chars', counts['italic'], '| headings', counts['headings'])
    return 0


if __name__ == '__main__':
    sys.exit(main())
