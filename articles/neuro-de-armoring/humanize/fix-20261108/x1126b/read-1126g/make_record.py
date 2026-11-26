#!/usr/bin/env python3
"""The comparison read's record for the 5-HTP section's interaction paragraph after its fixes: the paragraph read beside
his own card version in read-1126f (x1126b/read-1126f/READER-1.md) with the changes its findings asked for (F1.6, F1.7,
F1.9). No finding rated 2 or 3 is left in it."""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[6]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import compare_read as cr  # noqa: E402

HERE = pathlib.Path(__file__).resolve().parent
ARTICLE = HERE.parents[2] / 'HUMANIZED-SO-FAR.md'
STARTS = ['Serotonin syndrome usually comes from mixing']
blocks = cr.sr.blocks(ARTICLE.read_text(encoding='utf-8'))
cov = []
for s in STARTS:
    hit = [b for b in blocks if b['text'].startswith(s)]
    assert len(hit) == 1, (s, len(hit))
    cov.append(cr.phash(hit[0]['text']))
rec = {'format': 'compare-read-record-v1',
       'article': 'HUMANIZED-SO-FAR.md: the 5-HTP section\'s interaction paragraph, read beside his card version in '
                  'read-1126f with the changes its findings asked for (F1.6, F1.7, F1.9)',
       'coverage': cov, 'findings': [], 'dispositions': {}}
(HERE / 'READ-RECORD.json').write_text(json.dumps(rec, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
print(len(cov), 'covered')
