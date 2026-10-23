#!/usr/bin/env python3
"""clarity_read.py - the whole-article clarity read: passages a smart general reader would have to reread, or wouldn't
get, found by fresh readers, checked against the whole article, and listed for Joel with a plainer version of each.

Joel, 2026-10-23 14:14 UTC, on Nibbāna: "is there any other stuff in the nibbana guide that's hard to understand but still
passing pangram?" Three fresh readers found 29 passages (articles/nibbana/humanize/fix-20261023/clarity/). His answer of
16:55 UTC: "let's make sure this kind of check is standard for articles as we write them and as we finalize before
publishing in future, i thought it already was". It wasn't: the section cold read (reviewer/sense_section.txt) reads the
text a worker drafts, for where the sense breaks, and lets a passage stand that a reader gets on a second look; nothing
read a whole article, Joel's own words included, for what a reader would have to reread. When and how it runs is
docs/CLARITY-READ.md.

  python3 tools/humanization/clarity_read.py make ARTICLE DIR [--parts 3] [--about TEXT] [--question TEXT]
          [--examples tools/humanization/clarity_examples.json] [--max-items 12]
      ARTICLE is the article's HTML (Joel's editor HTML or a payload), Markdown or plain text. Writes DIR/ARTICLE.txt (the
      reading text, one paragraph a line, headings as "## " lines), DIR/PART-k.txt (the article split at headings into
      parts of about equal length) and DIR/BRIEF-k.txt (each part's reader brief, with his examples of what counts).
      Then give each BRIEF-k.txt to a fresh reader (a new agent that has seen nothing else); each writes DIR/READER-k.md.
  python3 tools/humanization/clarity_read.py collect DIR
      Reads every READER-k.md into DIR/ITEMS.json: each item's quote, what's hard, score and plain version, found in
      ARTICLE.txt (its line and heading), or marked not found when the reader didn't copy it exactly. Items already in
      ITEMS.json keep the worker's fields (status, note, check, my_score).
  python3 tools/humanization/clarity_read.py page DIR --out CLARITY.md [--title TEXT] [--intro TEXT]
      The list for Joel, numbered: the hardest (score 3), then what a reader would have to reread (score 2), then the
      small snags and what wasn't counted, each with its heading, the passage, what's hard and the plainer version.

Between collect and page, the worker checks every item against the whole article (each reader saw only its part): an
item explained elsewhere gets "status": "drop" with a note, a small one "minor", and "my_score" overrides a reader's
score; "check" says which step of a plain version is a guess at his reasoning.
"""
import argparse, html, json, pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
SKIP = {'figure', 'picture', 'img', 'source', 'iframe', 'hr', 'script', 'style', 'figcaption', 'button'}
STRAIGHT = str.maketrans({'“': '"', '”': '"', '‘': "'", '’': "'"})


VOID = {'br', 'img', 'hr', 'source', 'input', 'meta', 'link', 'wbr', 'col', 'area', 'base', 'embed', 'param', 'track'}


class Node:
    def __init__(self, name, attrs=None, parent=None):
        self.name, self.attrs, self.parent, self.children = name, dict(attrs or []), parent, []

    def classes(self):
        return (self.attrs.get('class') or '').split()

    def text(self):
        return ''.join(c if isinstance(c, str) else c.text() for c in self.children)


def parse_html(raw):
    """A small tree of RAW's elements (the standard library's parser; CI installs no packages)."""
    from html.parser import HTMLParser

    class P(HTMLParser):
        def __init__(self):
            super().__init__(convert_charrefs=True)
            self.root = self.cur = Node('root')

        def handle_starttag(self, tag, attrs):
            n = Node(tag, attrs, self.cur)
            self.cur.children.append(n)
            if tag not in VOID:
                self.cur = n

        def handle_startendtag(self, tag, attrs):
            self.cur.children.append(Node(tag, attrs, self.cur))

        def handle_endtag(self, tag):
            n = self.cur
            while n is not None and n.name != tag:
                n = n.parent
            if n is not None and n.parent is not None:
                self.cur = n.parent

        def handle_data(self, data):
            self.cur.children.append(data)

    p = P()
    p.feed(raw)
    p.close()
    return p.root


def find_body(n):
    if isinstance(n, Node):
        if n.name == 'div' and 'body' in n.classes():
            return n
        for c in n.children:
            b = find_body(c)
            if b is not None:
                return b
    return None


def _html_lines(el, out):
    if not isinstance(el, Node) or el.name in SKIP:
        return
    classes = el.classes()
    if el.name == 'div' and ('captioned-image-container' in classes or 'image-gallery-embed' in classes):
        return
    if re.fullmatch(r'h[1-6]', el.name or ''):
        t = re.sub(r'\s+', ' ', el.text()).strip()
        if t:
            out.append('## ' + t)
        return
    if el.name == 'p':
        t = el.text().strip()
        if t and not re.fullmatch(r'https?://\S+', t):
            out.append(t)
        return
    if el.name == 'li':  # a list item reads as "- " and its text, so a reader sees the list
        if any(isinstance(c, Node) and c.name in ('p', 'ul', 'ol') for c in el.children):
            at = len(out)
            for c in el.children:
                _html_lines(c, out)
            if len(out) > at and not out[at].startswith(('- ', '## ')):
                out[at] = '- ' + out[at]
        elif el.text().strip():
            out.append('- ' + el.text().strip())
        return
    for c in el.children:
        _html_lines(c, out)


def reading_text(raw, kind):
    """The article as a reader reads it: one paragraph a line, headings as "## " lines."""
    if kind == 'html':
        root = parse_html(raw)
        body = find_body(root) or root
        out = []
        for c in body.children:
            _html_lines(c, out)
        lines = out
    elif kind == 'md':
        lines = []
        for l in raw.split('\n'):
            l = re.sub(r'!\[[^\]]*\]\([^)]*\)', '', l)
            l = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', l).strip()
            if not l:
                continue
            m = re.match(r'#+\s*(.*)', l)
            lines.append('## ' + m.group(1).strip() if m else l)
    else:
        lines = [l.strip() for l in raw.split('\n') if l.strip()]
    return '\n'.join(lines)


def split_parts(text, n):
    """N parts of about equal length, each starting at a heading (the first may start before one)."""
    lines = text.split('\n')
    starts = [0] + [i for i, l in enumerate(lines) if l.startswith('## ') and i > 0]
    sizes = [len(l) + 1 for l in lines]
    total = sum(sizes)
    cuts, pos, s = [], {}, 0
    for i, z in enumerate(sizes):
        pos[i] = s
        s += z
    for k in range(1, n):
        target = total * k / n
        best = min((st for st in starts if st not in cuts and st > (cuts[-1] if cuts else 0)),
                   key=lambda st: abs(pos[st] - target), default=None)
        if best is not None:
            cuts.append(best)
    cuts = sorted(set(cuts))
    bounds = [0] + cuts + [len(lines)]
    return ['\n'.join(lines[a:b]) for a, b in zip(bounds, bounds[1:]) if b > a]


BRIEF = '''You are a cold first-time reader of part {k} of {n} of {about}. {question}Find the passages a smart general reader would have to stop and reread, or would come away not understanding.

What counts, from his own fixes:
{examples}
Other things that count: several claims packed into one sentence; a chain of abstract nouns ("the functional coordination through which ..."); a foreign or technical term the reader needs but that isn't explained there or earlier in your part; a "this", "that" or "it" whose referent isn't clear; a step missing from the reasoning, so the conclusion doesn't follow for the reader; a term used before it's explained; a sentence whose point you can't state after reading it twice.
What doesn't count: his jokes, emoji, slang, exclamations and casual grammar (that's his voice); a style you'd do differently; a term explained nearby; a long passage that is clear; a claim you disagree with (don't fact-check).

Read the file {part} (one Read call; it is part {k} of {n}, headings marked "## "). Then write your report with one Write call to {report}, in this shape, the hardest first, at most {max_items} items:

## 1
QUOTE: the passage, copied exactly character for character from the file (a sentence or two; enough to find it)
HARD: in one line, what a reader stumbles on (which words, and why)
SCORE: 3 (most readers would not get it), 2 (most would have to reread) or 1 (a small snag)
PLAIN: the smallest change to his own words that a reader would get on first read: keep his words, his order, his images and his voice; change only what stops a reader, and add only the missing step or gloss (in parentheses where it fits); no summing-up line ("Put together, ...", "That's why ...", "In other words, ..."); keep every claim, name, number and citation, and add no new claim or fact

If you find nothing that counts, write only "NOTHING". Then reply with only the number of items. Use no tools other than that one Read and that one Write, and don't use the web.
'''


def examples_text(ex):
    out = []
    for i, e in enumerate(ex, 1):
        out.append('%d. %s He rewrote this %s:\n   BEFORE: "%s"\n   AFTER: "%s"' % (
            i, e['kind'], e['his_words'], e['before'], e['after']))
    return '\n'.join(out)


def make(article, outdir, parts=3, about=None, question=None, examples=None, max_items=12):
    article, outdir = pathlib.Path(article), pathlib.Path(outdir)
    outdir.mkdir(parents=True, exist_ok=True)
    raw = article.read_text(encoding='utf-8')
    kind = 'html' if article.suffix.lower() in ('.html', '.htm') else ('md' if article.suffix.lower() == '.md' else 'txt')
    text = reading_text(raw, kind)
    (outdir / 'ARTICLE.txt').write_text(text, encoding='utf-8')
    ex = json.loads(pathlib.Path(examples or HERE / 'clarity_examples.json').read_text(encoding='utf-8'))['examples']
    ps = split_parts(text, parts)
    for k, p in enumerate(ps, 1):
        (outdir / ('PART-%d.txt' % k)).write_text(p, encoding='utf-8')
        brief = BRIEF.format(k=k, n=len(ps), about=about or "one of Joel's articles, for a general Substack audience",
                             question=(question + ' ') if question else '', examples=examples_text(ex),
                             part=(outdir / ('PART-%d.txt' % k)).resolve(), report=(outdir / ('READER-%d.md' % k)).resolve(),
                             max_items=max_items)
        (outdir / ('BRIEF-%d.txt' % k)).write_text(brief, encoding='utf-8')
    return text, ps


def parse_reader(md):
    if md.strip().upper().startswith('NOTHING'):
        return []
    items = []
    for block in re.split(r'\n?^## \d+\s*$', md, flags=re.M):
        if 'QUOTE:' not in block:
            continue
        f = {}
        for key in ('QUOTE', 'HARD', 'SCORE', 'PLAIN'):
            m = re.search(r'^%s:\s*(.*?)(?=^\s*(?:QUOTE|HARD|SCORE|PLAIN):|\Z)' % key, block, re.S | re.M)
            f[key.lower()] = m.group(1).strip() if m else ''
        try:
            f['score'] = int(re.match(r'\d', f['score']).group(0))
        except (AttributeError, TypeError):
            f['score'] = None
        items.append(f)
    return items


def locate(text, quote):
    """(line number, heading) of QUOTE in TEXT, also when only the quote marks differ; None when it isn't there once."""
    lines = text.split('\n')
    for t, q in ((text, quote), (text.translate(STRAIGHT), quote.translate(STRAIGHT))):
        if t.count(q) == 1:
            i = t.index(q)
            n = t[:i].count('\n')
            head = next((l[3:] for l in reversed(lines[:n + 1]) if l.startswith('## ')), '')
            return n + 1, head
    return None


def collect(outdir):
    outdir = pathlib.Path(outdir)
    text = (outdir / 'ARTICLE.txt').read_text(encoding='utf-8')
    old = {}
    if (outdir / 'ITEMS.json').exists():
        old = {x['quote']: x for x in json.loads((outdir / 'ITEMS.json').read_text(encoding='utf-8'))}
    items = []
    for f in sorted(outdir.glob('READER-*.md'), key=lambda p: int(re.search(r'(\d+)', p.stem).group(1))):
        part = int(re.search(r'(\d+)', f.stem).group(1))
        for j, it in enumerate(parse_reader(f.read_text(encoding='utf-8')), 1):
            where = locate(text, it['quote'])
            rec = {'key': '%d.%d' % (part, j), 'part': part, 'quote': it['quote'], 'hard': it['hard'], 'score': it['score'],
                   'plain': it['plain'], 'plain_by': "the reader's", 'found': where is not None,
                   'line': where[0] if where else None, 'heading': where[1] if where else None, 'status': 'keep'}
            prev = old.get(it['quote'])
            if prev:
                for k in ('status', 'note', 'check', 'my_score', 'plain', 'plain_by'):
                    if k in prev:
                        rec[k] = prev[k]
            items.append(rec)
    (outdir / 'ITEMS.json').write_text(json.dumps(items, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    return items


def score_of(x):
    return x.get('my_score') or x.get('score') or 1


def page(outdir, title=None, intro=None):
    items = json.loads((pathlib.Path(outdir) / 'ITEMS.json').read_text(encoding='utf-8'))
    live = [x for x in items if x.get('status', 'keep') == 'keep']
    hard = sorted((x for x in live if score_of(x) >= 3), key=lambda x: (x.get('line') or 0))
    reread = sorted((x for x in live if score_of(x) == 2), key=lambda x: (x.get('line') or 0))
    snags = [x for x in items if x.get('status') == 'minor' or (x.get('status', 'keep') == 'keep' and score_of(x) <= 1)]
    dropped = [x for x in items if x.get('status') == 'drop']
    out = ['# ' + (title or 'What passes Pangram but is hard to understand'), '']
    if intro:
        out += [intro, '']
    n = 0
    for head, group in (('The hardest: most readers wouldn\'t get these', hard), ('A reader would have to reread these', reread)):
        if not group:
            continue
        out += ['## ' + head, '']
        for x in group:
            n += 1
            out += ['### %d. %s' % (n, x.get('heading') or '(no heading)'), '', '> ' + x['quote'], '',
                    '**What\'s hard:** ' + x['hard'], '', '**Plainer (%s):** %s' % (x.get('plain_by', "the reader's"), x['plain']), '']
            if x.get('check'):
                out += ['**Check:** ' + x['check'], '']
            if not x.get('found'):
                out += ['(The reader\'s quote isn\'t in the article word for word: find it by its words before using it.)', '']
    if snags:
        out += ['## Small snags', '']
        out += ['- **%s:** "%s" (%s)' % (x.get('heading') or '', x['quote'][:100] + ('...' if len(x['quote']) > 100 else ''),
                                       x.get('note') or x['hard']) for x in snags]
        out.append('')
    if dropped:
        out += ['## Flagged but not counted', '']
        out += ['- **%s:** "%s" (%s)' % (x.get('heading') or '', x['quote'][:140], x.get('note') or '') for x in dropped]
        out.append('')
    return '\n'.join(out), n


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    sub = ap.add_subparsers(dest='cmd', required=True)
    m = sub.add_parser('make')
    m.add_argument('article'); m.add_argument('dir'); m.add_argument('--parts', type=int, default=3)
    m.add_argument('--about'); m.add_argument('--question'); m.add_argument('--examples')
    m.add_argument('--max-items', type=int, default=12)
    c = sub.add_parser('collect')
    c.add_argument('dir')
    p = sub.add_parser('page')
    p.add_argument('dir'); p.add_argument('--out', required=True); p.add_argument('--title'); p.add_argument('--intro')
    a = ap.parse_args(argv)
    if a.cmd == 'make':
        text, ps = make(a.article, a.dir, a.parts, a.about, a.question, a.examples, a.max_items)
        print('%s: %d characters in %d parts (%s); give each BRIEF-k.txt to a fresh reader' % (
            a.dir, len(text), len(ps), ', '.join(str(len(x)) for x in ps)))
    elif a.cmd == 'collect':
        items = collect(a.dir)
        lost = [x['key'] for x in items if not x['found']]
        print('%d items from the readers%s' % (len(items), ('; not found word for word: ' + ', '.join(lost)) if lost else ''))
    else:
        md, n = page(a.dir, a.title, a.intro)
        pathlib.Path(a.out).write_text(md, encoding='utf-8')
        print('%s: %d numbered passages' % (a.out, n))
    return 0


if __name__ == '__main__':
    sys.exit(main())
