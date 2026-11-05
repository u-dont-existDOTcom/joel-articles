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
      draft, or two answers come in the opposite order to their questions (gate E347). It also exits 1 until the draft
      itself has had a fresh read of its current words (make DRAFT DIR/draft, a fresh reader, collect DIR/draft) and each
      thing that reader can't follow is fixed (a new draft, read again) or dropped with a note (gate E355).

Its questions are the making-sense read's (docs/MAKING-SENSE.md, gate E360): since 2026-11-04 22:14 UTC they also ask what
an instruction is for, which thing exactly, what a word acts on, and whether a fact helps the reader in the section's
situation, from Joel's round-5 versions in the bad trips guide.

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
    # E360 (the bad trips guide's round 5, Joel 2026-11-04 22:14 UTC: "you don't need any lived experience, you just need
    # it to MAKE SENSE"; docs/MAKING-SENSE.md): what an instruction is for, which thing exactly, what a word acts on, and
    # whether a fact helps this reader now
    {'before': 'Begin with whatever could hurt somebody in the next five minutes. Put away the car keys.',
     'gap': 'Hurt whom, them or someone else? And why put the keys away: is it about where they are, or about driving?',
     'his': 'Anything that could let someone hurt themselves in the next five minutes takes priority, so get the car keys out '
            'of reach'},
    {'before': 'Move away from roads, balconies, water, weapons, crowds, and strangers.',
     'gap': 'Water? What is dangerous about water?',
     'his': 'move them away from roads and balconies, or pools of water for that matter'},
    {'before': 'I treat it as a plausible experimental adjunct rather than something to wait on while a seizure continues.',
     'gap': 'An adjunct to what?',
     'his': 'I\'d treat it as a plausible experimental adjunct remedy rather than something to wait on while a seizure '
            'continues.'},
    {'before': 'In a 2025 study of high-dose oral CBD, ... focal seizures fell by about half to three quarters over nearly '
               'three years',
     'gap': 'This section is about a seizure happening now: what does three years of daily CBD do for me here?',
     'his': '(cut: "think about the usefulness of the THREE YEAR STUDY when we are talking to people having seizures RIGHT '
            'NOW")'},
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
    {'before': 'so in theory they\'re a quick energy source for your enterocytes too. But nobody has shown that eating them '
               'gives those cells much extra fuel on top of the glutamine.',
     'gap': 'Why "but"? Quick energy is good, so what is it up against: is glutamine already enough?',
     'his': 'And they do supply quick energy, because they are made and used by that mitochondrial energy cycle ... But '
            'glutamine is still the main thing they need, because it helps build new cells in addition to giving the needed '
            'energy.'},
    {'before': 'Malic and citric acid (which make green apples and tart cherries sour) are made and used partway round that '
               'same cycle',
     'gap': 'Why am I reading about these acids at all?',
     'his': 'Some people will tell you to take malic and citric acid (which make green apples and tart cherries sour) as an '
            'extra quick energy source for your enterocytes.'},
    {'before': 'They do help you absorb iron, though. In one study, people absorbed two to three times as much of the iron in '
               'a rice meal when 1 g of pure malic or citric acid was mixed in',
     'gap': 'A study? I didn\'t know one was coming: what is it about?',
     'his': 'Those acids do help you absorb iron, even two or three times better according to one study where people ate '
            'rice with 1g pure malic acid or citric acid mixed in'},
    {'before': 'Gemini suggested three kits to me, but so far they\'re the best ones I\'ve seen',
     'gap': 'Why "but"? If Gemini just suggested three kits, what is the "but" answering?',
     'his': 'Gemini suggested these kits to me, but so far they\'re the best ones I\'ve seen (the "but" answers that these '
            'particular kits are only Gemini\'s picks; my change to "three" broke it)'},
    {'before': 'since that\'s what your bacteria make when they ferment it (resistant starch does it too)',
     'gap': 'What is "that", and what is "it"?',
     'his': 'since gas is what your bacteria make when they ferment the fiber or resistant starch'},
    {'before': 'has a probiotic and two lining products, one of them glutamine',
     'gap': 'Which lining?',
     'his': 'has a probiotic and two gut lining products, one of them glutamine'},
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
- why it matters to you, the reader;
- what a "but", "so", "though" or "because" turns on, when the claim it answers or follows from isn't said;
- what a "this", "that", "it", "these" or "those" points to, when you can't tell;
- what an instruction is for, when its purpose isn't said and you could guess wrong;
- which thing exactly, when a word names a whole kind of thing and only one case of it is meant (dangerous, useful,
  wrong);
- what a word acts on or means here, when you have to guess ("adjunct" to what?);
- why a fact is here for you, in the situation this part is about, when it doesn't help you there;
- why you're being told something at that point, when it comes before you'd want it (a study before the claim it backs, a
  detail before the point, a fact before the question it answers).

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


def draft_problems(d, draft):
    """E355 (Joel, 2026-11-04 16:00 UTC, on my kits: "your version, r08, makes no sense by the 6th word. Where is the "but"
    coming from? You can't say that. read it. it only follows from "these" kits not "three kits""): the draft itself gets
    a fresh read, of its current words, in DIR/draft (make DRAFT DIR/draft, a fresh reader, collect DIR/draft), and each
    thing that reader can't follow is fixed, which means a new draft and a new read, or dropped with a note saying why the
    words are right as they are. My change of one word, to answer the first read's question, broke the sentence's "but",
    and nothing read the draft after it."""
    dd = pathlib.Path(d) / 'draft'
    want = '\n'.join('S%d %s' % (i, s) for i, s in enumerate(sentences(draft), 1)) + '\n'
    if not (dd / 'TEXT.txt').exists():
        return ['the draft has had no fresh read of its own: make DRAFT %s, give its BRIEF.txt to a new reader, collect %s '
                '(E355: a word changed to answer the first read can break the sentence around it)' % (dd, dd)]
    if (dd / 'TEXT.txt').read_text(encoding='utf-8') != want:
        return ['the draft changed after its fresh read (%s/TEXT.txt is an older draft): read the new one again (E355)' % dd]
    if not (dd / 'LINKS.json').exists():
        return ['the draft read has no LINKS.json: collect %s' % dd]
    out = []
    for g in json.loads((dd / 'LINKS.json').read_text(encoding='utf-8')):
        if not (g.get('status') == 'drop' and g.get('note')):
            out.append('draft read %s: S%d "%s" (%s): fix it in a new draft and read that one, or drop it with a note saying '
                       'why the words are right' % (g['id'], g['sentence'], g['quote'], g['gap']))
    return out


def check(a):
    gaps = json.loads((pathlib.Path(a.dir) / 'LINKS.json').read_text(encoding='utf-8'))
    text = pathlib.Path(a.draft).read_text(encoding='utf-8')
    first = problems(gaps, text)
    probs = first + draft_problems(a.dir, text)
    for p in probs:
        print(p)
    print('%d gaps, %d answered or dropped, %d problems' % (len(gaps), len(gaps) - len(first), len(probs)))
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
