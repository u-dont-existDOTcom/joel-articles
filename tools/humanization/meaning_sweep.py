#!/usr/bin/env python3
"""meaning_sweep.py - a fresh reader's sweep of rewritten sections for the breaks Joel found in community section 12.

Joel, 2026-10-12 05:33 UTC, on section 12: "p3 got b roken ... then you broke p7 ... p16 also broke the meaning". The gate's
correction rule asks for a sweep of the whole article for the same problem; the first sweep (community lane,
sweep-20261012/) was a hand-built prompt, and 14 of its 18 flags fell in Joel's own paragraphs. Joel, 17:23: "rather than
just ignoring rules that fail my prose, we should fix the rules so they don't fail my prose". So this builds the sweep
from the published and rewritten article, and marks every sentence that is his (in the owner-edits ledger, or in a file
of his own texts) with ⟦author⟧ ... ⟦/author⟧, which the reader is told to leave alone.

Usage:
  python3 tools/humanization/meaning_sweep.py --article ART.md --source PUB.md --section 2 [--section 3 ...]
      --input IN.md --report REPORT.md --out PROMPT.txt [--ledger OWNER-EDITS.json] [--owner-text FILE ...] [--words 500]

--section is a top-level section's number (its "# " heading, counted from the top; the published article and the rewrite
must have their top-level headings in the same order). Give the reader PROMPT.txt; it reads IN.md and writes REPORT.md.
"""
import argparse, json, pathlib, re

MARK_OPEN, MARK_CLOSE = '⟦author⟧', '⟦/author⟧'
QUOTES = str.maketrans({'‘': "'", '’': "'", '“': '"', '”': '"'})

BRIEF = '''You are checking a rewrite of an essay against the published essay. Read `{input}`. It holds {n} of the essay, each as PUBLISHED and then REWRITE. The rewrite keeps the published order; it also has whole paragraphs that are new, which you skip.

Your only job is to find where the rewrite has lost or swapped a word that a claim rests on. Report only these three kinds:
1. A pronoun or vaguer word ("it", "this", "that", "they", "the thing") standing where the published sentence names something, when a reader could take it two ways and the sentence would say something different with each, or when nothing in reach names it. An "it" that is clear in its place is fine.
2. A narrower thing in place of a general one: one example, one quoted phrase, one case or a smaller group in place of the published category.
3. A dropped word that says what a claim is measured against (a "for ..." or "than ..." that sets the standard), how long it holds ("remains", "still", "already", "yet", "anymore", "again", "long after"), or the section's own term for its subject.

Text between {open_} and {close} is the author's own: he wrote or approved those words, often to change the published meaning on purpose. Report nothing inside those marks.

Plainer, looser, more conversational wording around a claim is fine, and so are changes of order, rhythm and tone. Don't report style, additions, cuts of whole sentences or anything outside the three kinds. Report a finding only when an ordinary reader of the rewrite would now believe something different, or couldn't tell what is meant, and say which.

Write the report to `{report}` with a single Write call, at most {words} words: "# Sweep" then, for each finding, one line: the section heading's first words, kind 1, 2 or 3, the published words in quotes, the rewrite's words in quotes, and what a reader would now wrongly believe or can't tell. If there are none, write "No findings." Don't read any other file. Reply with only the number of findings.

Keep your working short: go through each published paragraph once, and don't redraft the report.'''


def norm(t):
    return re.sub(r'\s+', ' ', t.translate(QUOTES)).strip()


def visible(text):
    text = re.sub(r'<!--.*?-->', '', text, flags=re.S)
    blocks = []
    for b in re.split(r'\n\s*\n', text):
        b = b.strip()
        if not b or re.match(r'^\[image \d+\]\(', b) or re.match(r'^https?://\S+$', b):
            continue
        b = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', b)
        b = re.sub(r'(?<!\w)\*([^*\n]+)\*(?!\w)', r'\1', b)
        blocks.append(b)
    return '\n\n'.join(blocks)


def h1_sections(text):
    parts = re.split(r'(?m)^(# [^\n]+)\n', text)
    return [(parts[i].strip(), visible(parts[i + 1])) for i in range(1, len(parts), 2)]


def owner_strings(ledger_path, owner_files):
    out = []
    if ledger_path:
        led = json.loads(pathlib.Path(ledger_path).read_text(encoding='utf-8'))
        entries = led['entries'] if isinstance(led, dict) else led
        for e in entries:
            if e.get('status') != 'applied':
                continue
            out += [norm(m) for m in e.get('must_contain', []) if len(m) >= 25]
            if isinstance(e.get('joel'), str) and len(e['joel']) >= 25:
                out.append(norm(e['joel']))
    for f in owner_files or []:
        raw = pathlib.Path(f).read_text(encoding='utf-8')
        if f.endswith('.json'):
            try:
                raw = '\n'.join(_strings(json.loads(raw)))
            except ValueError:
                pass
        out.append(norm(raw))
    return out


def _strings(o):
    if isinstance(o, str):
        yield o
    elif isinstance(o, dict):
        for v in o.values():
            yield from _strings(v)
    elif isinstance(o, list):
        for v in o:
            yield from _strings(v)


SENT = re.compile(r'(?<=[.!?…])["”’)]*\s+(?=["“‘(]?[A-Z0-9])')


def mark_author(section_text, owners):
    """Wrap each sentence that is the author's in the marks: the sentence appears in one of his texts, or contains a phrase
    the ledger locks as his (25 characters or more)."""
    out_blocks = []
    for block in section_text.split('\n\n'):
        sents = SENT.split(block)
        marked = []
        for s in sents:
            ns = norm(s)
            his = len(ns) >= 12 and any(ns in o or (len(o) >= 25 and o in ns) for o in owners)
            marked.append(MARK_OPEN + s + MARK_CLOSE if his else s)
        text = ' '.join(marked)
        text = text.replace(MARK_CLOSE + ' ' + MARK_OPEN, ' ')
        out_blocks.append(text)
    return '\n\n'.join(out_blocks)


def build(article, source, sections, ledger=None, owner_files=None):
    pub = h1_sections(pathlib.Path(source).read_text(encoding='utf-8'))
    art = h1_sections(pathlib.Path(article).read_text(encoding='utf-8'))
    owners = owner_strings(ledger, owner_files)
    out = ['# Sections, published and rewritten', '']
    for k in sections:
        ph, pb = pub[k - 1]
        ah, ab = art[k - 1]
        out += ['=' * 20, 'SECTION: ' + ph.lstrip('# '), '', 'PUBLISHED:', '', pb, '',
                'REWRITE' + (' (heading in the rewrite: ' + ah.lstrip('# ') + ')' if ah != ph else '') + ':', '',
                mark_author(ab, owners), '']
    return '\n'.join(out)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n\n')[0])
    ap.add_argument('--article', required=True)
    ap.add_argument('--source', required=True)
    ap.add_argument('--section', type=int, action='append', required=True)
    ap.add_argument('--input', required=True)
    ap.add_argument('--report', required=True)
    ap.add_argument('--out', required=True)
    ap.add_argument('--ledger')
    ap.add_argument('--owner-text', action='append', default=[])
    ap.add_argument('--words', type=int, default=500)
    a = ap.parse_args(argv)
    text = build(a.article, a.source, a.section, a.ledger, a.owner_text)
    pathlib.Path(a.input).write_text(text, encoding='utf-8')
    n = '%d section%s' % (len(a.section), '' if len(a.section) == 1 else 's')
    prompt = BRIEF.format(input=str(pathlib.Path(a.input).resolve()), report=str(pathlib.Path(a.report).resolve()), n=n,
                          words=a.words, open_=MARK_OPEN, close=MARK_CLOSE)
    pathlib.Path(a.out).write_text(prompt, encoding='utf-8')
    print('%s: %d sections, %d author marks' % (a.input, len(a.section), text.count(MARK_OPEN)))


if __name__ == '__main__':
    main()
