"""The community article with Joel's answers to question 64 (the caveat cuts) put in. His message of 2026-10-24 19:52 UTC
(joel-20261024-1952-message.txt beside this file): "64.1a 2b 3b it doesn't take back a rule, it explains the limits of
relying on it. 4a 5a 6a 7b 8b ... 31a".

The input is the working copy of his answers of 2026-10-23 22:29 UTC (../joel-20261023/restructure/WORKING.html: the essay,
then the How-To Manual). Each of the 22 cuts he took (A) comes out of its paragraph as the page showed it
(../joel-20261023/caveats/CAVEATS.md), tidied the way the page's "After" should have shown and now does
(tools/humanization/clarity_read.py cut_text: a dash or comma left hanging goes, the next word gets its capital; his 64.14
note). Links and italics stay on their words (tools/humanization/html_text_edit.py). The nine he kept (B) stay, with his
reasons in the record.

Writes, beside this file: WORKING.html (the working copy now), RECORD-64.json, ARTICLE.txt (its reading text) and
READING-COPY.md; and REPEATS.md, question 65's page again on this text, with the "After" of each cut as it will read.

  python3 articles/intentional-communities/candidate/joel-20261024/apply_64.py   (from the repo root)
"""
import collections, html, json, pathlib, re, sys
from html.parser import HTMLParser

HERE = pathlib.Path(__file__).resolve().parent
CAND = HERE.parent
REPO = HERE.parents[3]
sys.path.insert(0, str(REPO / 'tools' / 'humanization'))
import clarity_read as C  # noqa: E402
import html_text_edit as T  # noqa: E402

SRC = CAND / 'joel-20261023' / 'restructure' / 'WORKING.html'
CAV = CAND / 'joel-20261023' / 'caveats'
REP = CAND / 'joel-20261023' / 'repeats'
MSG = HERE / 'joel-20261024-1952-message.txt'
# his reasons, word for word, for the ones he kept where my pick was to cut, and for 29
REASONS = {
    3: "it doesn't take back a rule, it explains the limits of relying on it.",
    8: "it's not just softening, it's actually hardening at the same time showing that their wisdom is always changing as well.",
    20: "it's kind of key to understanding it in context, otherwise they can be too easily demonized and communities in general "
        "can be demonized as potentially abusing children as if children aren't routinely abused anyway.",
    28: "it's important to give a full picture",
    29: "cutting makes sense especially if we don't cut the last part in 28.",
}
NOTES = {14: 'you should make sure in future that instead of telling me "the sentence then starts with.." you actually make '
             'that change in the "after" version.',
         23: 'and i think this is another high freq AI pattern to be aware of: "isn\'t proof of/doesn\'t prove"'}
# the follow-on change my check described instead of showing it (his 64.14 note): the sentence after the cut gets its
# subject back, and the contrast word goes with the clause it answered
FOLLOW = {14: ('It can make a difference', 'Community can make a difference',
               'my check: "The sentence then starts \"Community can make a difference\"."'),
          15: ('But they are an example', 'They are an example',
               'my check: "The next sentence then starts \"They are an example\"."')}
FLAT = str.maketrans({'“': '"', '”': '"', '‘': "'", '’': "'", '\xa0': ' '})   # one character for one: positions hold


def picks():
    line = next(l for l in MSG.read_text(encoding='utf-8').split('\n') if l.startswith('64.'))
    got = [(int(n), ab.upper()) for n, ab in re.findall(r'\b(\d{1,2})\s?([ab])\b', line[3:])]
    assert sorted(n for n, _ in got) == list(range(1, 32)), got
    return dict(got)


def offered():
    """The items in the page's numbering (clarity_read.caveat_page: the ones offered, in the article's order), checked
    against the page he answered."""
    items = json.loads((CAV / 'ITEMS.json').read_text(encoding='utf-8'))
    live = sorted((x for x in items if x.get('status', 'keep') == 'keep'), key=lambda x: (x.get('line') or 0))
    page = (CAV / 'CAVEATS.md').read_text(encoding='utf-8')
    for n, x in enumerate(live, 1):
        sec = re.search(r'^### %d\. .*?(?=^### %d\. |^## |\Z)' % (n, n + 1), page, re.S | re.M).group(0)
        assert ('~~' + x['quote'].strip()).translate(FLAT) in sec.translate(FLAT), (n, x['quote'][:50])
    return live


def find(doc, quote):
    """(paragraph, the quote as it is in the paragraph's text) for the one paragraph that holds QUOTE."""
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


class Nesting(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack, self.errors = [], 0

    def handle_starttag(self, tag, attrs):
        if tag not in C_VOID:
            self.stack.append(tag)

    def handle_endtag(self, tag):
        if self.stack and self.stack[-1] == tag:
            self.stack.pop()
        else:
            self.errors += 1


C_VOID = {'br', 'img', 'hr', 'input', 'meta', 'link', 'source', 'wbr', 'area', 'base', 'col', 'embed', 'param', 'track',
          'path', 'circle', 'rect', 'line', 'polyline', 'polygon'}


def nesting_errors(doc):
    p = Nesting()
    p.feed(doc)
    return p.errors + len(p.stack)


def main():
    pick, live = picks(), offered()
    assert len(live) == 31
    doc = SRC.read_text(encoding='utf-8')
    base_errors = nesting_errors(doc)
    rec, removed_words, added_words = [], collections.Counter(), collections.Counter()
    for n, x in enumerate(live, 1):
        entry = {'n': '64.%d' % n, 'answer': pick[n], 'kind': x['kind'], 'quote': x['quote'], 'heading': x.get('heading'),
                 'my_pick': x.get('my_pick')}
        if n in REASONS:
            entry['his_reason'] = REASONS[n]
        if n in NOTES:
            entry['his_note'] = NOTES[n]
        if pick[n] == 'B':
            entry['done'] = 'kept'
            rec.append(entry)
            continue
        (start, end, ia, ib, plain), q = find(doc, x['quote'])
        new = C.cut_text(plain, q)
        assert flat_words(plain.replace(q, ' ', 1)) == flat_words(new), ('more than the cut changed', n)
        removed_words.update(flat_words(q))
        if n in FOLLOW:
            a, b, why = FOLLOW[n]
            assert new.count(a) == 1, (n, a)
            new = new.replace(a, b)
            removed_words.update(flat_words(a))
            added_words.update(flat_words(b))
            entry['follow_on'] = {'old': a, 'new': b, 'why': why}
        if new == '':
            doc = doc[:start] + doc[end:]
            entry.update(done='cut: the whole paragraph', old=plain)
        else:
            inner, dropped, moved = T.set_text(doc[ia:ib], new)
            if not dropped and not moved:  # every tag is still there, in the same order
                assert re.findall(r'<[^>]+>', inner) == re.findall(r'<[^>]+>', doc[ia:ib]), ('markup changed', n)
            doc = doc[:ia] + inner + doc[ib:]
            entry.update(done='cut', old=plain, new=new, markup_dropped=dropped, markup_moved=moved)
        rec.append(entry)
    before = collections.Counter(flat_words(C.reading_text(SRC.read_text(encoding='utf-8'), 'html')))
    after = collections.Counter(flat_words(C.reading_text(doc, 'html')))
    assert after == before - removed_words + added_words, 'the cuts are not the only change'
    assert nesting_errors(doc) == base_errors, ('tags out of order', nesting_errors(doc), base_errors)
    (HERE / 'WORKING.html').write_text(doc, encoding='utf-8')
    text = C.reading_text(doc, 'html')
    (HERE / 'ARTICLE.txt').write_text(text, encoding='utf-8')
    (HERE / 'RECORD-64.json').write_text(json.dumps(rec, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    try:
        from markdownify import markdownify
        # markdownify drops a space alone inside bold or italics ("ideology<strong> </strong>which" came out
        # "ideologywhich", 2026-10-25), so such a tag becomes its plain space first
        md = re.sub(r'\n{3,}', '\n\n', markdownify(re.sub(r'<(strong|em|b|i|u|s|a)\b[^>]*>(\s+)</\1>', r'\2', doc), heading_style='ATX', bullets='-', strip=['span'])).strip()
        (HERE / 'READING-COPY.md').write_text(
            '> A reading copy of the new version (WORKING.html beside this file, which is what gets pasted into Substack), '
            'made by apply_64.py: your answers of 2026-10-23 22:29 UTC and your 64 (2026-10-24 19:52 UTC) are in '
            '(RECORD-64.json lists the cuts; ../joel-20261023/restructure/RECORD.json the changes before them).\n\n'
            + md + '\n', encoding='utf-8')
    except ImportError:
        print('no markdownify here: READING-COPY.md not rebuilt')
    repeats_page(text)
    cut = [r for r in rec if r['done'] != 'kept']
    print('%d cut (%d whole paragraphs), %d kept; markup dropped: %s; moved: %s' % (
        len(cut), sum(r['done'].endswith('paragraph') for r in cut), len(rec) - len(cut),
        [d for r in cut for d in r.get('markup_dropped', [])], [m for r in cut for m in r.get('markup_moved', [])]))


def repeats_page(text):
    """Question 65's page on the text with the 64 cuts in: the same items, numbers and picks, each "After" as it will read."""
    items = json.loads((REP / 'ITEMS.json').read_text(encoding='utf-8'))
    old = (REP / 'REPEATS.md').read_text(encoding='utf-8')
    intro = old.split('\n\n')[1]
    for x in items:
        if x.get('status', 'keep') == 'keep' and C.locate(text, x['quote']) is None:
            raise SystemExit('a cut of 65 is not in the text any more: ' + x['quote'][:80])
    md, n = C.caveat_page(items, text, 'Community article: what it says more than once', intro)
    assert n == 31, n
    (HERE / 'REPEATS.md').write_text(md + '\n', encoding='utf-8')


if __name__ == '__main__':
    main()
