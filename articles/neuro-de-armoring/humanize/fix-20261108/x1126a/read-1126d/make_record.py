#!/usr/bin/env python3
"""The comparison read's record for the two paragraphs changed after read-1126c: each is the paragraph that fresh reader
read beside his text (read-1126c/READER-1.md) with the change its findings asked for, so the read holds for it:
The Rule with "either one" named as "a new romance or drama" (F1.2), and the 5-HTP section's interaction paragraph with
the same-day line for ayahuasca and iboga said outright (F1.7) and the three waits after iboga told apart (F1.8). No
finding rated 2 or 3 is left in either."""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[6]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import compare_read as cr  # noqa: E402

HERE = pathlib.Path(__file__).resolve().parent
ARTICLE = HERE.parents[2] / 'HUMANIZED-SO-FAR.md'
STARTS = ['The Rule: Seek "Boring Love"', 'Serotonin syndrome usually comes from mixing']
blocks = cr.sr.blocks(ARTICLE.read_text(encoding='utf-8'))
cov = []
for s in STARTS:
    hit = [b for b in blocks if b['text'].startswith(s)]
    assert len(hit) == 1, (s, len(hit))
    cov.append(cr.phash(hit[0]['text']))
rec = {'format': 'compare-read-record-v1',
       'article': 'HUMANIZED-SO-FAR.md 5864cc2f: The Rule and the 5-HTP section\'s interaction paragraph, each the paragraph '
                  'read beside his text in read-1126c with the change its findings asked for (F1.2; F1.7 and F1.8)',
       'coverage': cov, 'findings': [], 'dispositions': {}}
(HERE / 'READ-RECORD.json').write_text(json.dumps(rec, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
print(len(cov), 'covered')
