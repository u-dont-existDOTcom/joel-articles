#!/usr/bin/env python3
"""r33 = r32 with AskRigor linked to askrigor.com (Joel, 2026-11-07 12:10 UTC: "link askrigor to askrigor.com and then
post the article"): the name in Pooyan's item, where a reader first meets it, and the domain written out in the plant
foods item ("re-check it with askrigor.com"). The words stay the same. Writes r33.md."""
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
md = (HERE.parent / 'r32' / 'r32.md').read_text(encoding='utf-8')
for old, new in (('AskRigor, my research tool, is what told me', '[AskRigor](https://askrigor.com), my research tool, is what told me'),
                 ('re-check it with askrigor.com for', 're-check it with [askrigor.com](https://askrigor.com) for')):
    assert md.count(old) == 1, old
    md = md.replace(old, new)
(HERE / 'r33.md').write_text(md, encoding='utf-8')
print('r33.md', len(md.split()), 'words')
