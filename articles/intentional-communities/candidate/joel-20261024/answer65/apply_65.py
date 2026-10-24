"""The community article with Joel's answers to question 65 (the repeats) and the image he asked for put in. His message of
2026-10-24 23:40 UTC (../joel-20261024-2340-message.txt): "65 1a 2 b 3 b ... 21 a but after the "preferences and social
change" i want to add this image: /home/joel/Documents/community article/kibbutz harms.png ... 31 a".

The input is ../WORKING.html (his 64 cuts in, ../apply_64.py). Each of the 20 cuts he took (A) comes out as its page
showed it (../REPEATS.md, made on that text with clarity_read.cut_text), with links and bold on their words
(html_text_edit.set_text); the 11 he kept (B) stay. 21's paragraph then ends "... parents’ preferences and social change.",
and his image goes right after it: kibbutz-harms.png (his file, SHA-256 3972208c..., copied from his laptop into this
folder), as Substack's own image block. It was uploaded into the temporary community draft and read back from that
draft's editor (KIBBUTZ-ISLAND.html, the raw HTML Substack made), so the block is Substack's, not mine
(docs/SUBSTACK-HELPER-DELIVERY-GATE.md). Two attributes change, as on the article's other 20 images: the alt text (his 63
a), and the image's link back to its post (internalRedirect), which names the community post (198340475) instead of the
temporary draft. Without KIBBUTZ-ISLAND.html the script writes the text and says the image is pending.

Writes WORKING.html, RECORD-65.json, ARTICLE.txt and READING-COPY.md beside this file.

  python3 articles/intentional-communities/candidate/joel-20261024/answer65/apply_65.py   (from the repo root)
"""
import collections, html, json, pathlib, re, sys, urllib.parse

HERE = pathlib.Path(__file__).resolve().parent
J24 = HERE.parent
CAND = J24.parent
REPO = HERE.parents[4]
sys.path.insert(0, str(REPO / 'tools' / 'humanization'))
import clarity_read as C  # noqa: E402
import html_text_edit as T  # noqa: E402

SRC = J24 / 'WORKING.html'
REP = CAND / 'joel-20261023' / 'repeats'
PAGE = J24 / 'REPEATS.md'
MSG = J24 / 'joel-20261024-2340-message.txt'
ISLAND = HERE / 'KIBBUTZ-ISLAND.html'
IMAGE_AFTER = 'parents’ preferences and social change.'
POST_ID = '198340475'   # his community post: every other image's internalRedirect names it
ALT = ('A summary card, “What happens to adults raised with different caregiving practices?”: in a 1994 study of 48 infants '
       'on Israeli kibbutzim, 48% were securely attached with communal sleeping and 80% with sleeping at home, a 32-point '
       'difference in favor of family sleeping; the families weren’t randomly assigned, and the sample was small.')
FLAT = str.maketrans({'“': '"', '”': '"', '‘': "'", '’': "'", '\xa0': ' '})


def picks():
    body = MSG.read_text(encoding='utf-8').split('\n65\n', 1)[1]
    got = [(int(n), ab.upper()) for n, ab in re.findall(r'(?m)^(?:65 )?(\d{1,2})\s*([ab])\b', body)]
    assert sorted(n for n, _ in got) == list(range(1, 32)), got
    return dict(got)


def offered():
    """The items in the page's numbering (clarity_read.caveat_page), checked against the page he answered."""
    items = json.loads((REP / 'ITEMS.json').read_text(encoding='utf-8'))
    live = sorted((x for x in items if x.get('status', 'keep') == 'keep'), key=lambda x: (x.get('line') or 0))
    page = PAGE.read_text(encoding='utf-8')
    for n, x in enumerate(live, 1):
        sec = re.search(r'^### %d\. .*?(?=^### %d\. |^## |\Z)' % (n, n + 1), page, re.S | re.M).group(0)
        assert ('~~' + x['quote'].strip()).translate(FLAT) in sec.translate(FLAT), (n, x['quote'][:50])
    return live


def find(doc, quote):
    hits = []
    for par in T.paragraphs(doc):
        plain = par[4]
        for q in (quote, quote.strip()):
            k = plain.translate(FLAT).find(q.translate(FLAT))
            if k >= 0:
                hits.append((par, plain[k:k + len(q)]))
                break
    assert len(hits) == 1, (quote[:60], len(hits))
    return hits[0]


def flat_words(s):
    return re.sub(r'[^\w]+', ' ', s.translate(FLAT).lower()).split()


def island_with_alt(island):
    """KIBBUTZ-ISLAND.html with the alt text and the post's own image link, both in the img's data-attrs (what the editor
    reads on paste) and the alt in the img's alt attribute, as make_working.alt_text does for the other images."""
    tags = re.findall(r'<img\b[^>]*>', island)
    assert len(tags) == 1, len(tags)
    tag = tags[0]
    raw = re.search(r'\bdata-attrs="([^"]*)"', tag).group(1)
    attrs = json.loads(html.unescape(raw))
    dump = lambda d: html.escape(json.dumps(d, ensure_ascii=False, separators=(',', ':')), quote=True)
    assert dump(attrs) == raw, 'data-attrs would not round-trip'
    was = {'alt': attrs.get('alt'), 'internalRedirect': attrs.get('internalRedirect')}
    attrs['alt'] = ALT
    attrs['internalRedirect'] = 'https://ibogaqueen.substack.com/i/%s?img=%s' % (POST_ID, urllib.parse.quote(attrs['src'], safe=''))
    new = tag.replace(raw, dump(attrs))
    new = re.sub(r'\balt="[^"]*"', lambda m: 'alt="%s"' % html.escape(ALT, quote=True), new) if re.search(r'\balt="', new) \
        else new.replace('<img ', '<img alt="%s" ' % html.escape(ALT, quote=True), 1)
    return island.replace(tag, new), was, attrs


def main():
    pick, live = picks(), offered()
    assert len(live) == 31
    doc = SRC.read_text(encoding='utf-8')
    rec, removed = [], collections.Counter()
    for n, x in enumerate(live, 1):
        entry = {'n': '65.%d' % n, 'answer': pick[n], 'key': x['key'], 'kind': x['kind'], 'quote': x['quote'],
                 'heading': x.get('heading'), 'my_pick': x.get('my_pick'), 'said_already': x.get('said_already')}
        if pick[n] == 'B':
            entry['done'] = 'kept'
            rec.append(entry)
            continue
        (start, end, ia, ib, plain), q = find(doc, x['quote'])
        new = C.cut_text(plain, q)
        assert flat_words(plain.replace(q, ' ', 1)) == flat_words(new), ('more than the cut changed', n)
        removed.update(flat_words(q))
        if new == '':
            li = re.search(r'<li\b[^>]*>\s*$', doc[:start])
            if li and re.match(r'\s*</li>', doc[end:]):   # the paragraph is a list item's only content: the item goes
                start, end = li.start(), end + re.match(r'\s*</li>', doc[end:]).end()
            doc = doc[:start] + doc[end:]
            entry.update(done='cut: the whole paragraph', old=plain)
        else:
            inner, dropped, moved = T.set_text(doc[ia:ib], new)
            if not dropped and not moved:
                assert re.findall(r'<[^>]+>', inner) == re.findall(r'<[^>]+>', doc[ia:ib]), ('markup changed', n)
            doc = doc[:ia] + inner + doc[ib:]
            entry.update(done='cut', old=plain, new=new, markup_dropped=dropped, markup_moved=moved)
        rec.append(entry)
    before = collections.Counter(flat_words(C.reading_text(SRC.read_text(encoding='utf-8'), 'html')))
    after = collections.Counter(flat_words(C.reading_text(doc, 'html')))
    assert after == before - removed, 'the cuts are not the only change'
    # his image, right after the paragraph 21's cut now ends
    ends = [p for p in T.paragraphs(doc) if p[4].rstrip().endswith(IMAGE_AFTER)]
    assert len(ends) == 1, len(ends)
    image = {'answer': '65.21 (his note)', 'after': ends[0][4][-120:], 'file': 'kibbutz-harms.png',
             'his_file': '/home/joel/Documents/community article/kibbutz harms.png'}
    if ISLAND.exists():
        island, was, attrs = island_with_alt(ISLAND.read_text(encoding='utf-8'))
        assert 'captioned-image-container' in island and attrs['src'].startswith('https://substack-post-media.s3.amazonaws.com/')
        doc = doc[:ends[0][1]] + island + doc[ends[0][1]:]
        image.update(done='in', src=attrs['src'], alt=ALT, was=was, island='KIBBUTZ-ISLAND.html')
    else:
        image['done'] = 'pending: KIBBUTZ-ISLAND.html is not here yet'
        print('the image is pending: no KIBBUTZ-ISLAND.html')
    rec.append(image)
    (HERE / 'WORKING.html').write_text(doc, encoding='utf-8')
    (HERE / 'ARTICLE.txt').write_text(C.reading_text(doc, 'html'), encoding='utf-8')
    (HERE / 'RECORD-65.json').write_text(json.dumps(rec, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    try:
        from markdownify import markdownify
        md = re.sub(r'\n{3,}', '\n\n', markdownify(doc, heading_style='ATX', bullets='-', strip=['span'])).strip()
        (HERE / 'READING-COPY.md').write_text(
            '> A reading copy of the new version (WORKING.html beside this file, which is what gets pasted into Substack), '
            'made by apply_65.py: your answers of 2026-10-23 22:29 UTC, your 64 and your 65 (2026-10-24) are in '
            '(RECORD-65.json lists the 65 cuts and the image; ../RECORD-64.json and '
            '../../joel-20261023/restructure/RECORD.json the changes before them).\n\n' + md + '\n', encoding='utf-8')
    except ImportError:
        print('no markdownify here: READING-COPY.md not rebuilt')
    cut = [r for r in rec if r.get('done', '').startswith('cut')]
    print('%d cut (%d whole paragraphs), %d kept; image: %s; markup dropped: %s; moved: %s; %d characters of text' % (
        len(cut), sum(r['done'].endswith('paragraph') for r in cut), sum(r.get('done') == 'kept' for r in rec),
        image['done'], [d for r in cut for d in r.get('markup_dropped', [])], [m for r in cut for m in r.get('markup_moved', [])],
        len(C.reading_text(doc, 'html'))))


if __name__ == '__main__':
    main()
