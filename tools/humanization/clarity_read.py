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

  python3 tools/humanization/clarity_read.py make ARTICLE DIR [--kind clarity|edit] [--parts 3] [--about TEXT]
          [--question TEXT] [--examples tools/humanization/clarity_examples.json] [--max-items 12]
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

The reader's edit (part 2 of docs/CLARITY-READ.md; Joel, 2026-10-23 18:13 UTC: "the clarity check for articles should
also include the readability check from GPT that i started doing in the inner child article"): make --kind edit writes
the same reading text and parts with the reader's-edit brief (GPT's questions of 2026-10-23 11:41 UTC and his answers so
far, tools/humanization/readers_edit_examples.json) and marks DIR as an edit read (DIR/KIND); each reader proposes
moves, headings, labels and repeats to cut. collect and page then read and list proposals, not passages: the worker
gives each one "my_pick" ("A" to put it in, "B" to leave it) and a "note" after checking it against the whole article
and his earlier answers, and "status": "drop" for one that cuts a point he kept or a safeguard.
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


EDIT_BRIEF = '''You are a cold first-time reader of part {k} of {n} of {about}. {question}Every sentence may be clear. Your job is the reader's edit: find where the article makes a reader work through more than they need at that moment, and propose the smallest structural change that fixes it.

Ask of each section:
1. How many decisions does one passage ask of the reader? A main path with its alternatives and troubleshooting mixed in makes a simple invitation feel like something to troubleshoot before starting. The main invitation can come first, with the alternative for one difficulty in a short labelled part beside it.
2. Does a second subject start inside the section without a heading of its own? A subheading gives it its own space, and nothing has to be cut.
3. What is each warning's job: does it change what the reader should do here, or does it explain why the instruction has qualifications? A safeguard that changes what the reader does stays next to its step; its reasons can move to a note. A compassionate permission ("you don't have to feel warmth today") belongs to the invitation and stays.
4. Is a paragraph performing, with a joke, a metaphor or a memorable last line that only makes it sound casual, where it could be ordinary? His own humor and stories stay.
5. What would an attentive reader still genuinely need here? A last reassurance or qualification that adds nothing new after the reader has understood can go; a repeat that deepens a scene stays.

What he has decided so far:
{examples}

What you may propose: moving paragraphs (in the order they had, unless the order is the problem), a heading or a label, cutting a repeat (quote both places), moving a warning's reasons (not the safeguard) to a note, cutting a last line that adds nothing (say what the reader already has). What you may not: new jokes, examples, metaphors or teaching; rewording his sentences, beyond a heading, a label or the few words a move needs; cutting a safeguard that changes what the reader does; a style you'd do differently.

Read the file {part} (one Read call; it is part {k} of {n}, headings marked "## "). Then write your report with one Write call to {report}, in this shape, in the article's order, at most {max_items} proposals:

## 1
SECTION: the heading it's under, exactly as in the file
QUOTE: the first sentence of the passage the change is about, copied exactly character for character from the file
MOVE: one of MOVE, HEADING, LABEL, CUT-REPEAT, TO-NOTE, CUT-LAST-LINE
CHANGE: exactly what changes: which paragraphs go where, the heading's or label's words, or the words cut
WHY: in one line, what the reader has to work through now, and which question above it answers
KEEPS: what stays as it is, and anything the change must not lose

If nothing in your part needs it, write only "NOTHING". Then reply with only the number of proposals. Use no tools other than that one Read and that one Write, and don't use the web.
'''

EDIT_FIELDS = ('SECTION', 'QUOTE', 'MOVE', 'CHANGE', 'WHY', 'KEEPS')
CLARITY_FIELDS = ('QUOTE', 'HARD', 'SCORE', 'PLAIN')


def edit_examples_text(ex):
    out = []
    for i, e in enumerate(ex, 1):
        out.append('%d. %s (%s): %s\n   He chose: %s' % (i, e['section'], e['answer'], e['proposal'], e['his_choice']))
    return '\n'.join(out)


def examples_text(ex):
    out = []
    for i, e in enumerate(ex, 1):
        out.append('%d. %s He rewrote this %s:\n   BEFORE: "%s"\n   AFTER: "%s"' % (
            i, e['kind'], e['his_words'], e['before'], e['after']))
    return '\n'.join(out)


def make(article, outdir, parts=3, about=None, question=None, examples=None, max_items=12, read='clarity'):
    """READ is 'clarity' (part 1 of docs/CLARITY-READ.md, passages a reader has to reread) or 'edit' (part 2, the
    reader's edit); an edit read writes DIR/KIND, so that collect and page read proposals."""
    article, outdir = pathlib.Path(article), pathlib.Path(outdir)
    outdir.mkdir(parents=True, exist_ok=True)
    raw = article.read_text(encoding='utf-8')
    kind = 'html' if article.suffix.lower() in ('.html', '.htm') else ('md' if article.suffix.lower() == '.md' else 'txt')
    text = reading_text(raw, kind)
    (outdir / 'ARTICLE.txt').write_text(text, encoding='utf-8')
    edit = read == 'edit'
    default = HERE / ('readers_edit_examples.json' if edit else 'clarity_examples.json')
    ex = json.loads(pathlib.Path(examples or default).read_text(encoding='utf-8'))['examples']
    (outdir / 'KIND').write_text(read + '\n', encoding='utf-8')
    ps = split_parts(text, parts)
    for k, p in enumerate(ps, 1):
        (outdir / ('PART-%d.txt' % k)).write_text(p, encoding='utf-8')
        brief = (EDIT_BRIEF if edit else BRIEF).format(
            k=k, n=len(ps), about=about or "one of Joel's articles, for a general Substack audience",
            question=(question + ' ') if question else '', examples=(edit_examples_text if edit else examples_text)(ex),
            part=(outdir / ('PART-%d.txt' % k)).resolve(), report=(outdir / ('READER-%d.md' % k)).resolve(),
            max_items=max_items)
        (outdir / ('BRIEF-%d.txt' % k)).write_text(brief, encoding='utf-8')
    return text, ps


def read_kind(outdir):
    f = pathlib.Path(outdir) / 'KIND'
    return f.read_text(encoding='utf-8').strip() if f.exists() else 'clarity'


def parse_reader(md, fields=CLARITY_FIELDS):
    if md.strip().upper().startswith('NOTHING'):
        return []
    items, alt = [], '|'.join(fields)
    for block in re.split(r'\n?^## \d+\s*$', md, flags=re.M):
        if 'QUOTE:' not in block:
            continue
        f = {}
        for key in fields:
            m = re.search(r'^%s:\s*(.*?)(?=^\s*(?:%s):|\Z)' % (key, alt), block, re.S | re.M)
            f[key.lower()] = m.group(1).strip() if m else ''
        if 'score' in f:
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
    items, edit = [], read_kind(outdir) == 'edit'
    for f in sorted(outdir.glob('READER-*.md'), key=lambda p: int(re.search(r'(\d+)', p.stem).group(1))):
        part = int(re.search(r'(\d+)', f.stem).group(1))
        for j, it in enumerate(parse_reader(f.read_text(encoding='utf-8'), EDIT_FIELDS if edit else CLARITY_FIELDS), 1):
            where = locate(text, it['quote'])
            if edit:
                rec = {'key': '%d.%d' % (part, j), 'part': part, 'section': it['section'], 'quote': it['quote'],
                       'move': it['move'].upper(), 'change': it['change'], 'why': it['why'], 'keeps': it['keeps'],
                       'found': where is not None, 'line': where[0] if where else None,
                       'heading': where[1] if where else None, 'status': 'keep'}
                prev = old.get(it['quote'])
                if prev:
                    for k in ('status', 'note', 'my_pick', 'change'):
                        if k in prev:
                            rec[k] = prev[k]
                items.append(rec)
                continue
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


MOVES = {'MOVE': 'a move', 'HEADING': 'a heading', 'LABEL': 'a label', 'CUT-REPEAT': 'a repeat cut',
         'TO-NOTE': 'reasons to a note', 'CUT-LAST-LINE': 'a last line cut'}


def edit_page(items, title=None, intro=None):
    """The reader's edit for Joel: the proposals in the article's order, each with its options and my pick."""
    live = sorted((x for x in items if x.get('status', 'keep') == 'keep'), key=lambda x: (x.get('line') or 0))
    dropped = [x for x in items if x.get('status') == 'drop']
    out = ['# ' + (title or "The reader's edit: what a reader has to work through"), '']
    if intro:
        out += [intro, '']
    n = 0
    for x in live:
        n += 1
        pick = (x.get('my_pick') or '').upper()
        out += ['### %d. %s: %s' % (n, x.get('heading') or x.get('section') or '(no heading)',
                                    MOVES.get(x.get('move'), (x.get('move') or 'a change').lower())), '',
                '> ' + x['quote'], '', '**The change:** ' + x['change'], '', '**Why:** ' + x['why'], '']
        if x.get('keeps'):
            out += ['**Stays as it is:** ' + x['keeps'], '']
        if x.get('note'):
            out += ['**My check:** ' + x['note'], '']
        if not x.get('found'):
            out += ['(The reader\'s quote isn\'t in the article word for word: find it by its words before using it.)', '']
        out += ['- **A%s:** put it in.' % (' (my pick)' if pick == 'A' else ''),
                '- **B%s:** leave it as it is.' % (' (my pick)' if pick == 'B' else ''), '']
    if dropped:
        out += ['## Proposed but not offered', '']
        out += ['- **%s:** "%s" (%s)' % (x.get('heading') or '', x['quote'][:140], x.get('note') or '') for x in dropped]
        out.append('')
    return '\n'.join(out), n


def page(outdir, title=None, intro=None):
    items = json.loads((pathlib.Path(outdir) / 'ITEMS.json').read_text(encoding='utf-8'))
    if read_kind(outdir) == 'edit':
        return edit_page(items, title, intro)
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
    m.add_argument('--kind', choices=('clarity', 'edit'), default='clarity',
                   help="clarity (part 1: what a reader has to reread) or edit (part 2: the reader's edit)")
    c = sub.add_parser('collect')
    c.add_argument('dir')
    p = sub.add_parser('page')
    p.add_argument('dir'); p.add_argument('--out', required=True); p.add_argument('--title'); p.add_argument('--intro')
    a = ap.parse_args(argv)
    if a.cmd == 'make':
        text, ps = make(a.article, a.dir, a.parts, a.about, a.question, a.examples, a.max_items, a.kind)
        print('%s: %d characters in %d parts (%s); give each BRIEF-k.txt to a fresh reader' % (
            a.dir, len(text), len(ps), ', '.join(str(len(x)) for x in ps)))
    elif a.cmd == 'collect':
        items = collect(a.dir)
        lost = [x['key'] for x in items if not x['found']]
        print('%d items from the readers%s' % (len(items), ('; not found word for word: ' + ', '.join(lost)) if lost else ''))
    else:
        md, n = page(a.dir, a.title, a.intro)
        pathlib.Path(a.out).write_text(md, encoding='utf-8')
        print('%s: %d numbered %s' % (a.out, n, 'proposals' if read_kind(a.dir) == 'edit' else 'passages'))
    return 0


if __name__ == '__main__':
    sys.exit(main())
