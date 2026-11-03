#!/usr/bin/env python3
"""Turn 116: Joel's reorganized guide (his ODT of 2026-11-03 21:00 UTC, "inner-child-guide-reorganized-clean.odt",
SHA-256 998baaa98b29967b1de88070424c765ced33d6090bac69ad2325b32a322d7b53, 11.5 MB with its three images) as Markdown, so
the repository's tools can read it: JOEL-GUIDE-20261103.md.

PANDOC-RAW.md is `pandoc -f odt -t gfm --wrap=none` of his file (pandoc 3.1.3), untouched. This script changes only
what the conversion added, never his words or characters:
  - the empty bookmark spans LibreOffice left in headings (<span id="anchor-N"></span>) go;
  - each image tag becomes an "[image N](Pictures/...)" line, which the readers skip as the article's images;
  - pandoc's backslash escapes go (\\[ \\] \\. \\*), so text he typed as Markdown, like "[Buddhist enlightenment](...)",
    reads as he typed it; whether those are real links in his file is in LINKS.md.

  python3 to_markdown.py"""
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
raw = (HERE / 'PANDOC-RAW.md').read_text(encoding='utf-8')
out = re.sub(r'<span id="anchor(?:-\d+)?"></span>', '', raw)
n = [0]


def img(m):
    n[0] += 1
    return '[image %d](%s)' % (n[0], m.group(1))


out = re.sub(r'<img src="([^"]+)"[^>]*/>', img, out)
out = re.sub(r'\\([\[\]\.\*_#>`])', r'\1', out)
(HERE / 'JOEL-GUIDE-20261103.md').write_text(out, encoding='utf-8')
print('images', n[0], '| words', len(out.split()), '| headings', len(re.findall(r'^#{1,6} ', out, flags=re.M)))
