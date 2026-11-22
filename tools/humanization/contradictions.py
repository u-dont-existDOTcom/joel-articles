#!/usr/bin/env python3
"""contradictions.py - the contradictions check, a standard step for every article (gate neuro-2026-11-20a).

Joel, 2026-11-20 17:05 UTC, after answering the neuro de-armoring protocol's first contradictions: "let's make the
contradictions check a standard step in joel-articles (especially for clearly contradictory statements that aren't
explained)".

A fresh reader who has seen nothing else reads the whole article and lists every pair of statements that can't both be
followed or both be true: two amounts, timings or lengths for the same thing; one thing given two different uses; an
instruction and another that forbids it; the article's own numbers not adding up to what it says they come to; a claim
and a later claim against it. It quotes both with their line numbers and says whether the article itself explains the
difference (a later stage that changes the plan and says so, a stated exception, two different cases). It judges nothing
true or false and suggests no fix. Each pair the article doesn't explain goes to Joel as a question: which holds is his
decision, in his words, never the worker's alone. Every item then gets a fate in the article's fates file, and the
article isn't done while an item has none, or while one waits on him.

  python3 tools/humanization/contradictions.py brief ARTICLE.md OUT_DIR [--about "what the article is, for whom"]
      writes OUT_DIR/BRIEF.txt: the reader's brief with the article, one numbered line per line. Give it to a fresh
      reader (an agent that has seen nothing of the article or the work; Sonnet or stronger, since the whole article
      has to be held at once), who writes OUT_DIR/EXTRACT.md.
  python3 tools/humanization/contradictions.py check EXTRACT.md FATES.json [--article ARTICLE.md] [--done]
      lists every item with its fate. Fails when an item has no fate, a fate isn't one of FATES below, or a fate has
      neither a ref nor a note; with --done, also when a fate still waits on him or on a check (question, card,
      applying). With --article, lists the items whose quotes are no longer in the article: the text changed since the
      read, so read those parts again.

EXTRACT.md: one "### ID title" heading per item (ID like 3 or 2.3), its quotes as lines '- line N: "quote"', a line
'- What differs: ...', and '- Explained in the text: no' or '- Explained in the text: yes, line N, "quote"'. Items
without a "What differs" line (an extract's other sections) aren't contradictions and are skipped.

FATES.json: {"article": "...", "extract": "...", "items": {"ID": {"fate": F, "ref": "...", "note": "..."}}}.
"""
import argparse
import json
import pathlib
import re
import sys

FATES = {
    'explained': 'the article itself explains the difference (ref: the line that does)',
    'not-a-conflict': 'the two statements are about different things (note: what each is about)',
    'settled': 'an earlier change he approved settled it (ref: the record)',
    'answered': 'his answer is in the article (ref: the record of what went in)',
    'applying': 'he has answered; the text that carries his answer waits on its checks (ref: the work)',
    'question': 'open on his questions page (ref: the question)',
    'card': 'open on his cards page (ref: the card)',
}
OPEN = ('applying', 'question', 'card')

BRIEF = """You are reading a long article by Joel, a Substack writer: __ABOUT__.

Your one job: find every place where the article says two things that can't both be followed or can't both be true.
This is extraction only. Don't judge which one is right, don't suggest a fix, and don't use outside knowledge: go only by
what the article itself says.

What counts:
- two different amounts, timings, lengths, limits or units for the same thing;
- one thing given two different uses, or one use given two different things;
- an instruction, and another that forbids it or changes it, for the same moment;
- the article's own numbers not adding up to what it says they come to;
- a claim, and a later claim against it.

Read every part, the lists and asides too: the clearest contradictions are often between a section's rule and a later
schedule or checklist. For each pair, check whether the article explains the difference (a later stage that changes the
plan and says so, an exception it states, two different cases it names). Say so either way; an explained pair still goes
in the list, marked as explained.

Write each item like this, numbered 1, 2, 3 ... in the order its first quote appears:

### 1 [a short title: what the two statements are about]
- line N: "[the exact words from that line, copied character for character]"
- line M: "[the exact words]"
- What differs: [one or two plain sentences: what each says, and why both can't hold]
- Explained in the text: no
  (or: yes, line K, "[the exact words that explain it]")

Quote exactly, keeping the article's own spelling, dashes, asterisks and spacing: a checker looks for each quote on its
line. Use as many quote lines as the item needs. After the last item, write one line: ITEMS: [how many].

The article, one numbered line per line:

__TEXT__
"""


def brief(article, about='a long article for adult readers'):
    lines = pathlib.Path(article).read_text(encoding='utf-8').split('\n')
    text = '\n'.join('%d: %s' % (i, l) for i, l in enumerate(lines, 1))
    return BRIEF.replace('__ABOUT__', about).replace('__TEXT__', text)


ITEM = re.compile(r'^###\s+(\S+)\s+(.*)$')
QUOTE = re.compile(r'^-\s+line\s+(\d+):\s+"(.*)"\s*$')


def parse(text):
    """The contradiction items of an extract: [{id, title, quotes: [(line, quote)], differs, explained}]."""
    items, cur = [], None
    for raw in text.split('\n'):
        line = raw.rstrip()
        m = ITEM.match(line)
        if m or line.startswith('## ') or line.startswith('# '):
            if cur and cur['differs']:
                items.append(cur)
            cur = {'id': m.group(1).rstrip('.'), 'title': m.group(2).strip(), 'quotes': [], 'differs': '',
                   'explained': None} if m else None
            continue
        if not cur:
            continue
        q = QUOTE.match(line.strip())
        if q:
            cur['quotes'].append((int(q.group(1)), q.group(2)))
        elif line.strip().startswith('- What differs:'):
            cur['differs'] = line.strip()[len('- What differs:'):].strip()
        elif line.strip().startswith('- Explained in the text:'):
            cur['explained'] = line.strip()[len('- Explained in the text:'):].strip()
    if cur and cur['differs']:
        items.append(cur)
    return items


def check(extract_text, fates, article_text=None, done=False):
    """(ok, lines): every item with its fate, and the problems."""
    items = parse(extract_text)
    have = fates.get('items', {})
    out, bad = [], []
    ids = [it['id'] for it in items]
    for it in items:
        f = have.get(it['id'])
        if not f:
            bad.append('%s (%s): no fate' % (it['id'], it['title']))
            continue
        kind = f.get('fate')
        if kind not in FATES:
            bad.append('%s: fate %r is not one of %s' % (it['id'], kind, ', '.join(FATES)))
            continue
        if not (f.get('ref') or f.get('note')):
            bad.append('%s: fate %s with neither a ref nor a note' % (it['id'], kind))
            continue
        if done and kind in OPEN:
            bad.append('%s (%s): still %s (%s)' % (it['id'], it['title'], kind, f.get('ref') or f.get('note')))
        out.append('%s %s: %s (%s)' % (it['id'], it['title'], kind, f.get('ref') or f.get('note')))
    for k in have:
        if k not in ids:
            bad.append('%s: a fate for an item the extract does not have' % k)
    if article_text is not None:
        norm = lambda s: re.sub(r'\s+', ' ', s).strip()
        body = norm(article_text)
        for it in items:
            gone = [q for _, q in it['quotes'] if norm(q) not in body]
            if gone:
                out.append('%s: %d of its quotes are no longer in the article (changed since the read): %s'
                           % (it['id'], len(gone), '; '.join(g[:60] for g in gone)))
    counts = {}
    for it in items:
        k = (have.get(it['id']) or {}).get('fate', 'none')
        counts[k] = counts.get(k, 0) + 1
    out.append('items: %d; %s' % (len(items), ', '.join('%s %d' % kv for kv in sorted(counts.items()))))
    return not bad, out + ['PROBLEM ' + b for b in bad]


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    sub = ap.add_subparsers(dest='cmd', required=True)
    b = sub.add_parser('brief')
    b.add_argument('article')
    b.add_argument('out_dir')
    b.add_argument('--about', default='a long article for adult readers')
    c = sub.add_parser('check')
    c.add_argument('extract')
    c.add_argument('fates')
    c.add_argument('--article')
    c.add_argument('--done', action='store_true')
    a = ap.parse_args(argv)
    if a.cmd == 'brief':
        out = pathlib.Path(a.out_dir)
        out.mkdir(parents=True, exist_ok=True)
        (out / 'BRIEF.txt').write_text(brief(a.article, a.about), encoding='utf-8')
        print('wrote %s; give it to a fresh reader, who writes %s' % (out / 'BRIEF.txt', out / 'EXTRACT.md'))
        return 0
    fates = json.loads(pathlib.Path(a.fates).read_text(encoding='utf-8'))
    art = pathlib.Path(a.article).read_text(encoding='utf-8') if a.article else None
    ok, lines = check(pathlib.Path(a.extract).read_text(encoding='utf-8'), fates, art, a.done)
    for l in lines:
        print(l)
    print('verdict: %s' % ('PASS' if ok else 'FAIL'))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
