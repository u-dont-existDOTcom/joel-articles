#!/usr/bin/env python3
"""link_flags.py - the review flags that touch a linked phrase, with where each link goes (2026-10-15).

Joel, 2026-10-15 18:28 UTC, on question 32. Four cold reads had asked "why is this here?" of "My research initially
leaned too far that way", where "My research" is a link to his research report, and I proposed cutting the sentence:
"this is the same problem we had before where you forgot to notice that "research" is a link to my research report, so
it's about that." E174 (2026-10-14) had shown the readers the links; nothing made me look at a link before acting on a
flag. This lists every flag in the review reports whose quoted words sit in a sentence of the draft that has a link, with
the linked words and the address, so the disposition starts from what the link tells a reader.

  python3 tools/humanization/link_flags.py DRAFT.md REPORT.md [REPORT.md ...] [--dispositions DISPOSITIONS.md]

With --dispositions, each listed flag needs a line in that file that quotes some of its words (four or more in a row)
and says "link"; exit 1 lists the flags without one. Reports are any review output that quotes the text in double
quotes: cold reads, traces, stance checks. Quotes with "..." or "…" are matched by their longest piece.
"""
import argparse
import pathlib
import re
import sys

LINK = re.compile(r'\[([^\]]+)\]\(([^)\s]+)[^)]*\)')
QUOTE = re.compile(r'"([^"\n]{8,}?)"|“([^”\n]{8,}?)”')
MARK = re.compile(r'\s*\[a link to [^\]]*\]')


def norm(s):
    s = MARK.sub('', s)
    s = s.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')
    s = re.sub(r'[*_`]', '', s)
    return re.sub(r'\s+', ' ', s).strip().lower()


def sentences(md):
    """(plain sentence, [(linked words, address)]) for every sentence of every paragraph; headings left out."""
    out = []
    for block in re.split(r'\n\s*\n', md):
        block = block.strip()
        if not block or block.startswith('#'):
            continue
        for s in re.split(r'(?<=[.!?)])\s+(?=[A-Z"“\'(\[])', block):
            links = [(t, u) for t, u in LINK.findall(s)]
            out.append((norm(LINK.sub(lambda m: m.group(1), s)), links))
    return out


def pieces(q):
    parts = [norm(p) for p in re.split(r'\.\.\.|…', q)]
    parts = [p.strip(' ,;:()') for p in parts if len(p.split()) >= 2]
    return sorted(parts, key=len, reverse=True)


def flags(draft, reports):
    sents = sentences(draft)
    found = []
    for rep in reports:
        text = pathlib.Path(rep).read_text(encoding='utf-8')
        for line in text.splitlines():
            # a trace's EQUIVALENT line or a reader's OK isn't a flag (2026-10-15: round r14's traces quoted linked
            # sentences in EQUIVALENT lines, and each one asked for a disposition)
            if re.search(r'\bEQUIVALENT\b', line) and not re.search(r'\b(SHIFT|LOST|ADDED)\b', line):
                continue
            if re.match(r'^\s*\[P\d+\]\s*OK\b', line):
                continue
            for m in QUOTE.finditer(line):
                q = m.group(1) or m.group(2)
                ps = pieces(q)
                if not ps:
                    continue
                hits = []
                for piece in ps:  # every piece of a quote cut with "...", longest first
                    hits += [(s, l) for s, l in sents if l and piece in s and (s, l) not in hits]
                    if len(piece.split()) >= 4:
                        # a piece that runs across two sentences: look for its first and last four words
                        for part in (' '.join(piece.split()[:4]), ' '.join(piece.split()[-4:])):
                            hits += [(s, l) for s, l in sents if l and part in s and (s, l) not in hits]
                for s, links in hits:
                    found.append({'report': rep, 'line': line.strip()[:160], 'quote': q, 'sentence': s, 'links': links})
    return found


def disposed(flag, disp_lines):
    words = norm(flag['quote']).split()
    for line in disp_lines:
        n = norm(line)
        if 'link' not in n:
            continue
        for i in range(max(1, len(words) - 3)):
            if ' '.join(words[i:i + 4]) in n:
                return True
    return False


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('draft')
    ap.add_argument('reports', nargs='+')
    ap.add_argument('--dispositions')
    a = ap.parse_args(argv)
    found = flags(pathlib.Path(a.draft).read_text(encoding='utf-8'), a.reports)
    seen, uniq = set(), []
    for f in found:
        k = (f['report'], f['quote'])
        if k not in seen:
            seen.add(k)
            uniq.append(f)
    for f in uniq:
        print('%s: "%s"' % (f['report'], f['quote']))
        for t, u in f['links']:
            print('   link: "%s" -> %s' % (t, u))
    if not uniq:
        print('no flag touches a linked phrase')
    if a.dispositions:
        lines = pathlib.Path(a.dispositions).read_text(encoding='utf-8').splitlines()
        missing = [f for f in uniq if not disposed(f, lines)]
        for f in missing:
            print('NO DISPOSITION THAT SAYS WHAT THE LINK TELLS A READER: "%s" (%s)' % (f['quote'], f['report']))
        print('verdict:', 'FAIL' if missing else 'PASS')
        return 1 if missing else 0
    return 0


if __name__ == '__main__':
    sys.exit(main())
