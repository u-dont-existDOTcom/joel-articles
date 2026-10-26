#!/usr/bin/env python3
"""Turn 113: print sections of the article with paragraph and sentence numbers (P.S), the way the reshape scripts count
them, for the triage of which sections get the plain-path-first shape or case headings.
  show_sections.py "Heading one" "Heading two" ..."""
import pathlib, re, sys
ART = pathlib.Path(__file__).resolve().parents[2] / 'HUMANIZED-ARTICLE-SO-FAR.md'
SPLIT = re.compile(r'(?<=[.!?"”)])\s+(?=[A-Z"“(])')
md = re.sub(r'<!--.*?-->', '', ART.read_text(encoding='utf-8'), flags=re.S)
blocks = [b.strip() for b in re.split(r'\n\s*\n', md) if b.strip()]
want = sys.argv[1:]
cur = None
for b in blocks:
    m = re.match(r'^(#{1,6})\s+(.*)', b)
    if m:
        cur = m.group(2).strip() if m.group(2).strip() in want else None
        if cur:
            print('\n' + '=' * 8, m.group(1), cur); n = 0
        continue
    if cur:
        n += 1
        ss = SPLIT.split(b)
        print('P%d (%d words)' % (n, len(b.split())))
        for k, s in enumerate(ss, 1):
            print('  %d.%d %s' % (n, k, s))
