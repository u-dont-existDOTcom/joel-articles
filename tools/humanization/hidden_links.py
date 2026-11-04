#!/usr/bin/env python3
"""hidden_links.py - the newcomer read: before a compressed paragraph is rewritten, a fresh reader who doesn't know the
subject lists every link the paragraph leaves out (gate E345), and the draft has to state each one.

Joel, 2026-11-04 10:18 UTC, on the gut article's fuels, after three tries of mine at each of three paragraphs read AI:
"now you try with what i taught you -- but i taught you the SAME thing as before, so idk why i keep having to teach the
same thing? just explain stuff to someone who doesn't already know the hidden links in your prose's thinking". His two
rewrites read Human: glutamine gained "So that's why consuming pure glutamine gives energy to those cells faster than
eating food" (why skipping digestion matters), and butyrate "preventing the dangerous escape of substances from gut to
blood, which then turns down inflammatory signals that would be needed otherwise to contain the damage" (how a tighter
barrier and less inflammation connect). Gates E338 (gut) and E342 had recorded his method as moves (a definition first,
one step a sentence, glosses in the flow); I applied the moves and left the links out, and the meaning check failed the
one link I did write. This step asks the question his rewrites answer, before drafting, and checks the draft answers it.

  python3 tools/humanization/hidden_links.py make TEXT DIR [--context FILE] [--about TEXT]
      DIR/TEXT.txt (the paragraph, a sentence a line, S1, S2 ...) and DIR/BRIEF.txt for a fresh reader (a new agent that
      has seen nothing else, the lead session's model). --context is what the reader has already read just before it (it
      explains nothing twice); --about says what the article is. The reader writes DIR/READER.md.
  python3 tools/humanization/hidden_links.py collect DIR
      DIR/LINKS.json from READER.md: each gap's sentence, quote and what a newcomer can't see. A gap already in LINKS.json
      keeps the worker's fields.
  python3 tools/humanization/hidden_links.py check DIR DRAFT
      Every gap in LINKS.json needs "answer" (the words in the draft that state the link, copied exactly) and "raised"
      (the draft's words where the reader first asks it), or "status": "drop" with a "note" (explained earlier in the
      article, or not a link the original's reasoning holds). Exits 1 while one is unanswered, its answer isn't in the
      draft, or two answers come in the opposite order to their questions (gate E347). Then read the draft again the same
      way (make DRAFT DIR2, a fresh reader, collect DIR2): what that reader still can't follow, the draft's own new terms
      included, is fixed in the next draft, or dropped with a note.

A stated link must be true and the original's own reasoning (or plain common knowledge), never a new claim; the blind
meaning check reads it as LINK, not as an added fact (the fuels' brief, 2026-11-04).

State each link as a cause or a consequence for the reader, in the flow ("they're already part of it, so your mitochondria
can use them for energy directly"), not as a definition line: a TCA draft that answered all eleven gaps as glosses ("is
just another name for", "are the compounds the cycle goes through") read AI High in one window (2026-11-04). And when the
paragraph already has a version, state the link where the AI window is and keep the other sentences: Joel's two Human
rewrites changed only that stretch; all six of my TCA tries rewrote the whole paragraph and read AI.
"""
import argparse, json, pathlib, re, sys

EXAMPLES = [
    {'before': 'It skips the complicated digestive steps other nutrients have to go through.',
     'gap': 'So what? Why does skipping digestion matter to the cells, or to me?',
     'his': 'It doesn\'t have to go through the complicated digestive steps other nutrients do. ... So that\'s why consuming '
            'pure glutamine gives energy to those cells faster than eating food.'},
    {'before': 'Besides feeding the colonocytes, they lock down the barrier in your lower gut and keep turning down '
               'inflammatory signals.',
     'gap': 'How does a tighter barrier have anything to do with inflammation?',
     'his': 'Besides feeding the colonocytes, SCFAs lock down the barrier in your lower gut, preventing the dangerous escape '
            'of substances from gut to blood, which then turns down inflammatory signals that would be needed otherwise to '
            'contain the damage.'},
    {'before': 'If your enterocytes (small intestine) or colonocytes (large intestine) lack their preferred mitochondrial '
               'fuels, the barrier structurally collapses',
     'gap': 'What are enterocytes? And how does a cell running out of fuel make a barrier collapse?',
     'his': 'Your gut barrier needs a lot of energy, to keep its tight junctions intact. If the cells lining your small '
            'intestine (called enterocytes) or the colonocytes lining your large intestine don\'t do that, the barrier '
            'loosens up.'},
]

BRIEF = '''You know nothing about this subject: you're a smart reader who has never studied biology or health, reading an
article written for people like you.{about}{context}

Here is the next part, one sentence a line:

---
{text}
---

List every place where you can't see one of these, because the writer knows it and didn't say it:
- what a word means;
- why a sentence follows from the one before it (the step in between);
- how something does what the sentence says it does;
- why it matters to you, the reader.

Don't list what the part above already explained. Don't judge whether the claims are true, and don't rewrite anything.
Here is what counts, from the writer's own fixes of other paragraphs:

{examples}

Write one line per gap, this way, and nothing else:
S<number> | "<the exact words, copied>" | <what you can't see, as your question>
If there's none, write: none
'''


def sentences(text):
    text = re.sub(r'\s+', ' ', text.strip())
    out, buf = [], ''
    for part in re.split(r'(?:(?<=[.!?])|(?<=[.!?][)"”]))\s+(?=[A-Z(“"])', text):
        buf = (buf + ' ' + part).strip() if buf else part
        if not re.search(r'\b(e\.g|i\.e|vs|Dr|etc)\.$', buf):
            out.append(buf)
            buf = ''
    if buf:
        out.append(buf)
    return out


def make(a):
    d = pathlib.Path(a.dir)
    d.mkdir(parents=True, exist_ok=True)
    ss = sentences(pathlib.Path(a.text).read_text(encoding='utf-8'))
    (d / 'TEXT.txt').write_text('\n'.join('S%d %s' % (i, s) for i, s in enumerate(ss, 1)) + '\n', encoding='utf-8')
    about = ('\n\nThe article: ' + a.about) if a.about else ''
    context = ('\n\nYou have just read this part of it:\n\n---\n%s\n---' % pathlib.Path(a.context).read_text(encoding='utf-8').strip()
               ) if a.context else ''
    ex = '\n\n'.join('Before: "%s"\nA newcomer\'s question: %s\nHis fix: "%s"' % (e['before'], e['gap'], e['his']) for e in EXAMPLES)
    (d / 'BRIEF.txt').write_text(BRIEF.format(about=about, context=context, text=(d / 'TEXT.txt').read_text(encoding='utf-8').strip(),
                                              examples=ex), encoding='utf-8')
    print('%s: %d sentences; give %s to a fresh reader, who writes %s' % (d, len(ss), d / 'BRIEF.txt', d / 'READER.md'))


LINE = re.compile(r'^\s*[-*]?\s*S(\d+)\s*\|\s*["“](.+?)["”]\s*\|\s*(.+?)\s*$')


def parse(reply):
    gaps = []
    for line in reply.splitlines():
        m = LINE.match(line)
        if m:
            gaps.append({'sentence': int(m.group(1)), 'quote': m.group(2), 'gap': m.group(3)})
    return gaps


def collect(a):
    d = pathlib.Path(a.dir)
    old = {}
    if (d / 'LINKS.json').exists():
        old = {(g['sentence'], g['quote']): g for g in json.loads((d / 'LINKS.json').read_text(encoding='utf-8'))}
    gaps = []
    for n, g in enumerate(parse((d / 'READER.md').read_text(encoding='utf-8')), 1):
        g = dict(old.get((g['sentence'], g['quote']), {}), **g)
        g['id'] = 'L%d' % n
        gaps.append(g)
    (d / 'LINKS.json').write_text(json.dumps(gaps, ensure_ascii=False, indent=1), encoding='utf-8')
    print('%s: %d gaps' % (d / 'LINKS.json', len(gaps)))


def norm(t):
    return re.sub(r'\s+', ' ', t.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')).strip()


def problems(gaps, draft):
    """Every gap answered in the draft, and the answers in the order a reader asks the questions ("raised": the draft's
    words where the reader first asks it). Joel, 2026-11-04 11:32 UTC: "it's not just about whether the points get
    addressed eventually, but do they get addressed in the order a reader would be thinking, so that reading is easy?"
    (gate E347). His glutamine answers "so what?" three sentences after the question, once the how is told: the order is
    what counts, not the distance."""
    draft = norm(draft)
    out, placed = [], []
    for g in gaps:
        if g.get('status') == 'drop':
            if not g.get('note'):
                out.append('%s: dropped with no note' % g['id'])
            continue
        if not g.get('answer'):
            out.append('%s: no answer for S%d "%s" (%s)' % (g['id'], g['sentence'], g['quote'], g['gap']))
            continue
        a = draft.find(norm(g['answer']))
        if a < 0:
            out.append('%s: its answer isn\'t in the draft: "%s"' % (g['id'], g['answer']))
            continue
        if not g.get('raised'):
            out.append('%s: no "raised" (the draft\'s words where the reader first asks it)' % g['id'])
            continue
        r = draft.find(norm(g['raised']))
        if r < 0:
            out.append('%s: its "raised" words aren\'t in the draft: "%s"' % (g['id'], g['raised']))
            continue
        placed.append((r, a, g['id']))
    placed.sort()
    for (r1, a1, i1), (r2, a2, i2) in zip(placed, placed[1:]):
        if a2 < a1 and r2 > r1:
            out.append('%s: answered before %s, though the reader asks it later (the order a reader thinks)' % (i2, i1))
    return out


def check(a):
    gaps = json.loads((pathlib.Path(a.dir) / 'LINKS.json').read_text(encoding='utf-8'))
    probs = problems(gaps, pathlib.Path(a.draft).read_text(encoding='utf-8'))
    for p in probs:
        print(p)
    print('%d gaps, %d answered or dropped, %d problems' % (len(gaps), len(gaps) - len(probs), len(probs)))
    return 1 if probs else 0


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    sub = ap.add_subparsers(dest='cmd', required=True)
    m = sub.add_parser('make')
    m.add_argument('text')
    m.add_argument('dir')
    m.add_argument('--context')
    m.add_argument('--about')
    c = sub.add_parser('collect')
    c.add_argument('dir')
    k = sub.add_parser('check')
    k.add_argument('dir')
    k.add_argument('draft')
    a = ap.parse_args(argv)
    return {'make': make, 'collect': collect, 'check': check}[a.cmd](a) or 0


if __name__ == '__main__':
    sys.exit(main())
