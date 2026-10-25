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

The caveat read (part 3 of docs/CLARITY-READ.md; Joel, 2026-10-23 22:29 UTC: "did we already look at whether there's too
much safety language in this article? just cut out a ton of obnoxious safety language and caveats from inner child
article. same question for community and hypnosis articles"): make --kind caveats writes the brief for safety lines,
reassurances, takebacks, hedges and disclaimers a reader doesn't need where they are (the examples are
tools/humanization/caveat_examples.json, from the Inner Child lane's safety-language pass), and collect and page list
cuts: each with the cut struck through in its paragraph, the paragraph after the cut, why, what a reader loses, and the
worker's pick and "note" (with "said_already" quotes for a repeat).
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
            if tag == 'br':  # a line break is a break for the reader (2026-10-23: "it also!<br><br>But first" read as one)
                self.cur.children.append('\n')
            if tag not in VOID:
                self.cur = n

        def handle_startendtag(self, tag, attrs):
            self.cur.children.append(Node(tag, attrs, self.cur))
            if tag == 'br':
                self.cur.children.append('\n')

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


MEDIA = {'captioned-image-container': '[an image]', 'image-gallery-embed': '[images]', 'youtube-wrap': '[a video]',
         'native-video-embed': '[a video]'}


def _html_lines(el, out):
    """One line a paragraph, "## " a heading, "- " a list item, and a marker line where the reader sees an image or a
    video (2026-10-23: with the video out of the reading text, the line under it, "DN 27 wraps the theory into a bedtime
    story.", read as a repeat of the paragraph above it, and a reader proposed cutting it)."""
    if not isinstance(el, Node) or el.name in SKIP:
        if isinstance(el, Node) and el.name in ('iframe', 'video'):
            out.append('[a video]')
        return
    classes = el.classes()
    mark = next((m for c, m in MEDIA.items() if c in classes), None)
    if el.name == 'div' and mark:
        out.append(mark)
        return
    if re.fullmatch(r'h[1-6]', el.name or ''):
        t = re.sub(r'\s+', ' ', el.text()).strip()
        if t:
            out.append('## ' + t)
        return
    if el.name == 'p':  # a paragraph with line breaks in it reads as separate lines, as the post shows them
        for t in el.text().split('\n'):
            t = t.strip()
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
            out.append('- ' + re.sub(r'\s*\n\s*', ' ', el.text().strip()))
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
        # notes in HTML comments are the editor's, never the reader's (2026-10-24: the Inner Child guide's Markdown keeps
        # its turn notes and Pangram records in comments, and the first reader's-edit run would have shown them all)
        raw = re.sub(r'<!--.*?-->', '', raw, flags=re.S)
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

Work quickly: read the part once, noting candidates as you go, then pick the clearest and write them down. Don't rewrite every passage in your head or weigh each one at length: a short report naming the passages that stop a reader most is the job. (2026-10-25: the reader of the first sixth of a 29,000-word guide spent its whole output deliberating and wrote nothing.)

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
2. Does a second subject start inside the section without a heading of its own? A subheading gives it its own space, and nothing has to be cut. A heading you propose names everything under it (on 2026-10-24 he turned down "One Grown-Up, Three Jobs" for a section that also covers a song and forced adulthood).
3. What is each warning's job: does it change what the reader should do here, or does it explain why the instruction has qualifications? A safeguard that changes what the reader does stays next to its step; its reasons can move to a note. A compassionate permission ("you don't have to feel warmth today") belongs to the invitation and stays.
4. Is a paragraph performing, with a joke, a metaphor or a memorable last line that only makes it sound casual, where it could be ordinary? His own humor and stories stay.
5. What would an attentive reader still genuinely need here? A last reassurance or qualification that adds nothing new after the reader has understood can go; a repeat that deepens a scene stays.

What he has decided so far:
{examples}

What you may propose: moving paragraphs (in the order they had, unless the order is the problem), a heading or a label, cutting a repeat (quote both places), moving a warning's reasons (not the safeguard) to a note, cutting a last line that adds nothing (say what the reader already has). What you may not: new jokes, examples, metaphors or teaching; rewording his sentences, beyond a heading, a label or the few words a move needs; cutting a safeguard that changes what the reader does; a style you'd do differently.

Work quickly: read the part once, noting candidates as you go, then pick the strongest and write them down. Don't rewrite the article in your head or weigh every paragraph; a short report that names the few changes that matter most is the job. (2026-10-23: three readers given a third of an article each spent their whole output deliberating and wrote nothing.)

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

CAVEAT_BRIEF = '''You are a cold first-time reader of part {k} of {n} of {about}. {question}Joel finds his articles overloaded with safety language and caveats, much of it added by AI drafts: in his words, "all the extra extra ridiculous safety language which gets repeated everywhere" and "obnoxious safety language and caveats". Your job is to list every line in your part that is a warning, a caution, a reassurance, a disclaimer, or a caveat or hedge that a reader doesn't need where it is, so that it can be cut.

The test for each line: does it change what the reader should do right here, or does it only explain why an instruction has qualifications, reassure, or protect the writer? {books}

What counts (give each one its kind):
- SAID-AGAIN: a warning or caveat the article already made (quote the other place if it's in your part).
- BLANKET: a general add-on tacked onto something it doesn't change.
- NOBODY-SUGGESTED: a warning against a step the text never suggested.
- REASSURANCE: a line that reassures or softens after the point is made.
- TAKEBACK: a line that takes back part of what was just said, or answers an objection nobody raised.
- HEDGE: a caveat that weakens a claim for no reader benefit.
- DISCLAIMER: a not-advice or not-a-claim notice that protects the writer.

Cuts from his inner child guide, of the kind he wants gone:
{examples}

What doesn't count, so keep it: {kept}; a marker that tells the reader whose claim it is when the article reports texts or science ("the suttas say", or "I think" where it separates his view from a source's); a hedge that is the claim itself (he really isn't sure); his jokes, stories and voice.

Work quickly: read the part once, noting candidates as you go, then write them down. A short report with the clearest cuts is the job.

Read the file {part} (one Read call; it is part {k} of {n}, headings marked "## "). Then write your report with one Write call to {report}, in this shape, in the article's order, at most {max_items} items:

## 1
SECTION: the heading it's under, exactly as in the file
QUOTE: the exact words to cut, copied exactly character for character from the file: a whole sentence, a clause or a parenthesis, no more than the cut
KIND: one of SAID-AGAIN, BLANKET, NOBODY-SUGGESTED, REASSURANCE, TAKEBACK, HEDGE, DISCLAIMER
WHY: in one line, why a reader doesn't need it here (for SAID-AGAIN, where it's said; for a TAKEBACK or a HEDGE, what the line tells the reader first, and why that adds nothing)
LOSES: what a reader loses if it's cut ("nothing" when that's so)

If nothing in your part counts, write only "NOTHING". Then reply with only the number of items. Use no tools other than that one Read and that one Write, and don't use the web.
'''

REPEAT_BRIEF = '''You are a cold first-time reader of {about}. {question}Joel says his articles are too long and too redundant ("as much as possible we should be deduplicating because i feel the article is really too redundant"; "everyone says my articles are too long (and hard to read because of the excessive redundancy and details which are from the AI writing)"). Your job is to find what the article says more than once, so the repeats can be cut.

You own part {k} of {n}: the points made in that part. For each point made in your part, look through the whole article for every other place that makes the same point again (an explanation, an argument, a definition, a story, a warning or a list that a reader already has). Then say which place keeps the point (usually the fullest one, or the one where the reader needs it), and which words to cut elsewhere.

What counts: the same explanation or argument given again in other words; a definition repeated; a story or example told twice; a summing-up that restates what the paragraph just said; a preview that the section it previews then says again in full. What doesn't count: a short callback that names an earlier point to build on it ("as I said about the founders, ..."), a pointer to another section, a point applied to a new case where the new case is the content, his jokes and stories told once.

Cut whole sentences or clauses only, so the paragraph still reads after the cut; no rewording. If a cut would leave a paragraph that no longer makes sense, say so in LOSES.

Work quickly: read the whole article once, noting repeats of your part's points as you go, then pick the clearest and write them down. Don't compare every paragraph with every other or weigh each cut at length: a short report naming the biggest repeats is the job. (2026-10-23: three of the four readers of the community article spent their whole output thinking, again and again, and wrote nothing.)

Read the whole article in {article} (one Read call; headings marked "## "), and your part, the same text as part {k} of {n}, in {part} (one Read call). Then write your report with one Write call to {report}, in this shape, in the article's order of the cuts, at most {max_items} items:

## 1
SECTION: the heading the cut is under, exactly as in the file
QUOTE: the exact words to cut, copied exactly character for character from the file: whole sentences or clauses, no more than the cut
KEPT: the words, copied exactly from the file, of the place that keeps the point, and its heading in brackets
WHY: in one line, what the cut says again
LOSES: what a reader loses if it's cut ("nothing" when that's so)

If you find no repeats of your part's points, write only "NOTHING". Then reply with only the number of items. Use no tools other than those two Reads and that one Write, and don't use the web.
'''

EDIT_FIELDS = ('SECTION', 'QUOTE', 'MOVE', 'CHANGE', 'WHY', 'KEEPS')
REPEAT_FIELDS = ('SECTION', 'QUOTE', 'KEPT', 'WHY', 'LOSES')
CAVEAT_FIELDS = ('SECTION', 'QUOTE', 'KIND', 'WHY', 'LOSES')
CLARITY_FIELDS = ('QUOTE', 'HARD', 'SCORE', 'PLAIN')


def edit_examples_text(ex):
    out = []
    for i, e in enumerate(ex, 1):
        out.append('%d. %s (%s): %s\n   He chose: %s' % (i, e['section'], e['answer'], e['proposal'], e['his_choice']))
    return '\n'.join(out)


def caveat_examples_text(ex):
    return '\n'.join('%d. %s: "%s" (%s). Why: %s' % (i, e['kind'], e['cut'], e['context'], e['why'])
                     for i, e in enumerate(ex, 1))


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
    edit, cav, rep = read == 'edit', read == 'caveats', read == 'repeats'
    default = HERE / {'edit': 'readers_edit_examples.json', 'caveats': 'caveat_examples.json'}.get(read, 'clarity_examples.json')
    exfile = {'examples': []} if rep else json.loads(pathlib.Path(examples or default).read_text(encoding='utf-8'))
    ex = exfile['examples']
    (outdir / 'KIND').write_text(read + '\n', encoding='utf-8')
    ps = split_parts(text, parts)
    for k, p in enumerate(ps, 1):
        (outdir / ('PART-%d.txt' % k)).write_text(p, encoding='utf-8')
        brief = (REPEAT_BRIEF if rep else CAVEAT_BRIEF if cav else EDIT_BRIEF if edit else BRIEF).format(
            article=(outdir / 'ARTICLE.txt').resolve(),
            k=k, n=len(ps), about=about or "one of Joel's articles, for a general Substack audience",
            question=(question + ' ') if question else '',
            examples=(caveat_examples_text if cav else edit_examples_text if edit else examples_text)(ex) if ex else '',
            books=exfile.get('books', ''), kept='; '.join(exfile.get('kept', [])),
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
    items, edit, cav, rep = [], read_kind(outdir) == 'edit', read_kind(outdir) == 'caveats', read_kind(outdir) == 'repeats'
    for f in sorted(outdir.glob('READER-*.md'), key=lambda p: int(re.search(r'(\d+)', p.stem).group(1))):
        part = int(re.search(r'(\d+)', f.stem).group(1))
        fields = REPEAT_FIELDS if rep else CAVEAT_FIELDS if cav else EDIT_FIELDS if edit else CLARITY_FIELDS
        for j, it in enumerate(parse_reader(f.read_text(encoding='utf-8'), fields), 1):
            where = locate(text, it['quote'])
            if rep:
                it['kind'] = 'REPEAT'
            if cav or rep:
                rec = {'key': '%d.%d' % (part, j), 'part': part, 'section': it['section'], 'quote': it['quote'],
                       'kind': it['kind'].upper(), 'why': it['why'], 'loses': it['loses'],
                       **({'said_already': it['kept']} if rep else {}),
                       'found': where is not None, 'line': where[0] if where else None,
                       'heading': where[1] if where else None, 'status': 'keep'}
                prev = old.get(it['quote'])
                if prev:
                    for k in ('status', 'note', 'my_pick', 'said_already', 'whose', 'why'):
                        if k in prev:
                            rec[k] = prev[k]
                items.append(rec)
                continue
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
    # what the worker's own check found and added (gives "by": "mine") stays when the readers' reports are collected again
    items += [x for x in old.values() if x.get('by') == 'mine']
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
        out += ['### %d. %s: %s%s' % (n, x.get('heading') or x.get('section') or '(no heading)',
                                      MOVES.get(x.get('move'), (x.get('move') or 'a change').lower()),
                                      ' (from my check, not a reader\'s)' if x.get('by') == 'mine' else ''), '',
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
    out += dup_section(items)
    return '\n'.join(out), n


def dup_section(items):
    """Items with "status": "dup": the same passage flagged by a second reader, or one offered on another list of the
    same check. They are listed once at the end with the note saying where they are offered, so he never answers the same
    cut twice (2026-10-25: 48 of the 295 items from the hypnosis guide's 36 readers were the same words twice, or on two lists)."""
    dups = [x for x in items if x.get('status') == 'dup']
    if not dups:
        return []
    out = ['## Flagged twice, or offered on another list', '']
    out += ['- **%s:** "%s" (%s)' % (x.get('heading') or '', x['quote'][:140], x.get('note') or '') for x in dups]
    return out + ['']


def numbers(items):
    """{key: its number on the page}: the offered items, in the article's order, as every page numbers them."""
    live = sorted((x for x in items if x.get('status', 'keep') == 'keep'), key=lambda x: (x.get('line') or 0))
    return {x['key']: i for i, x in enumerate(live, 1)}


KINDS = {'REPEAT': 'a repeat', 'SAID-AGAIN': 'said already', 'BLANKET': 'a blanket add-on', 'NOBODY-SUGGESTED': 'warns against a step nobody '
         'suggested', 'REASSURANCE': 'a reassurance', 'TAKEBACK': 'a takeback', 'HEDGE': 'a hedge',
         'DISCLAIMER': 'a disclaimer', 'TRIM': 'a trim you asked for'}


HANGING = re.compile(r'\s*(?:[–—]|--|,|;|:)\s*$')   # a dash or comma the cut leaves with nothing after it
SENTENCE_END = re.compile(r'[.!?…][”"’\')\]]*$')


def cut_text(line, quote):
    """LINE with QUOTE cut, as it will read. A dash, comma or colon left hanging before the punctuation after the cut goes
    with it, a comma left at a sentence's start goes, and when the cut took a sentence's first words the next word gets its
    capital. Joel, 2026-10-24 19:52 UTC, on the community caveats (64.14): "you should make sure in future that instead of
    telling me "the sentence then starts with.." you actually make that change in the "after" version". The Nibbāna
    caveats' 5 had shown "almost never discuss the suttas –." for the same reason."""
    i = line.index(quote)
    b, r = line[:i].rstrip(), line[i + len(quote):].lstrip()
    if (not r or r[0] in '.,;:!?)]') and HANGING.search(b):
        b = HANGING.sub('', b)
    starts = not b or SENTENCE_END.search(b)
    if starts and r[:1] in (',', ';', ':'):
        r = r[1:].lstrip()
    if starts:
        m = re.match(r'([“"‘\'(\[]*)([^\W\d_])', r)
        if m and m.group(2).islower():
            r = r[:m.start(2)] + m.group(2).upper() + r[m.end(2):]
    if not b or not r:
        out = b or r
    elif r[0] in '.,;:!?)]”’':
        out = b + r
    else:
        out = b + ' ' + r
    return re.sub(r'\s+([.,;:!?)])', r'\1', re.sub(r'\(\s*\)', '', re.sub(r' {2,}', ' ', out))).strip()


def cut_paragraph(text, quote):
    """(the paragraph with the cut struck through, the paragraph after the cut) from the reading text."""
    line = next((l for l in text.split('\n') if quote in l), None)
    if line is None:
        line = next((l for l in text.split('\n') if quote.translate(STRAIGHT) in l.translate(STRAIGHT)), None)
        if line is None:
            return None, None
        i = line.translate(STRAIGHT).index(quote.translate(STRAIGHT))
        quote = line[i:i + len(quote)]
    struck = line.replace(quote, '~~' + quote + '~~', 1)
    return struck, cut_text(line, quote)


def caveat_page(items, text, title=None, intro=None):
    """The caveat read for Joel: the cuts in the article's order, each struck through in its paragraph, with the paragraph
    after the cut, why, what a reader loses, and my pick."""
    live = sorted((x for x in items if x.get('status', 'keep') == 'keep'), key=lambda x: (x.get('line') or 0))
    dropped = [x for x in items if x.get('status') == 'drop']
    out = ['# ' + (title or 'Safety lines and caveats a reader doesn\'t need'), '']
    if intro:
        out += [intro, '']
    n = 0
    for x in live:
        n += 1
        pick = (x.get('my_pick') or 'A').upper()
        struck, after = cut_paragraph(text, x['quote'])
        out += ['### %d. %s: %s' % (n, x.get('heading') or x.get('section') or '(no heading)',
                                    KINDS.get(x.get('kind'), (x.get('kind') or 'a cut').lower())), '']
        if x.get('whose'):
            out += ['*Whose words:* ' + x['whose'], '']
        out += ['> ' + (struck or x['quote']), '', '**Why:** ' + x['why'], '']
        if x.get('said_already'):
            out += ['**Said already:** ' + x['said_already'], '']
        out += ['**What a reader loses:** ' + (x.get('loses') or 'nothing'), '']
        if x.get('note'):
            out += ['**My check:** ' + x['note'], '']
        if after == '':
            out += ['**After:** the whole paragraph goes.', '']
        elif after is not None:
            out += ['**After:**', '', '> ' + after, '']
        else:
            out += ['(The reader\'s quote isn\'t in the article word for word: find it by its words before using it.)', '']
        out += ['- **A%s:** cut it.' % (' (my pick)' if pick == 'A' else ''),
                '- **B%s:** keep it.' % (' (my pick)' if pick == 'B' else ''), '']
    if dropped:
        out += ['## Looked at and kept', '']
        out += ['- **%s:** "%s" (%s)' % (x.get('heading') or '', x['quote'][:140], x.get('note') or '') for x in dropped]
        out.append('')
    out += dup_section(items)
    return '\n'.join(out), n


def page(outdir, title=None, intro=None):
    items = json.loads((pathlib.Path(outdir) / 'ITEMS.json').read_text(encoding='utf-8'))
    if read_kind(outdir) == 'edit':
        return edit_page(items, title, intro)
    if read_kind(outdir) in ('caveats', 'repeats'):
        return caveat_page(items, (pathlib.Path(outdir) / 'ARTICLE.txt').read_text(encoding='utf-8'),
                           title or ('What the article says more than once' if read_kind(outdir) == 'repeats' else None), intro)
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
    out += dup_section(items)
    return '\n'.join(out), n


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    sub = ap.add_subparsers(dest='cmd', required=True)
    m = sub.add_parser('make')
    m.add_argument('article'); m.add_argument('dir'); m.add_argument('--parts', type=int, default=3)
    m.add_argument('--about'); m.add_argument('--question'); m.add_argument('--examples')
    m.add_argument('--max-items', type=int, default=12)
    m.add_argument('--kind', choices=('clarity', 'edit', 'caveats', 'repeats'), default='clarity',
                   help="clarity (part 1: what a reader has to reread), edit (part 2: the reader's edit) or caveats "
                        "(part 3: safety lines and caveats a reader doesn't need) or repeats (part 4: what the article "
                        "says more than once; each reader reads the whole article and owns one part's points)")
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
        print('%s: %d numbered %s' % (a.out, n, {'edit': 'proposals', 'caveats': 'cuts', 'repeats': 'cuts'}.get(read_kind(a.dir), 'passages')))
    return 0


if __name__ == '__main__':
    sys.exit(main())
