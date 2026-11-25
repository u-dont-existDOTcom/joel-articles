#!/usr/bin/env python3
"""The comparison read's record for version 10's three paragraphs: each is the paragraph the fresh reader read beside
his post in read-1125a (READER-1.md) with the one word that reader's finding asked for (F1.2 "any medication", F1.17
"starting uridine", F1.1 "Your lungs need to be clean too"), so the read holds for it; no finding rated 2 or 3."""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[6]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import compare_read as cr  # noqa: E402

HERE = pathlib.Path(__file__).resolve().parent
ARTICLE = HERE.parents[2] / 'HUMANIZED-SO-FAR.md'
STARTS = ['DMSO Safety: This protocol has you smell DMSO', 'Ethnobotanicals: The plant medicines in this protocol',
          'Uridine (the UMP in this protocol)']
blocks = cr.sr.blocks(ARTICLE.read_text(encoding='utf-8'))
cov = []
for s in STARTS:
    hit = [b for b in blocks if b['text'].startswith(s)]
    assert len(hit) == 1, (s, len(hit))
    cov.append(cr.phash(hit[0]['text']))
rec = {'format': 'compare-read-record-v1',
       'article': 'HUMANIZED-SO-FAR.md a65eaa1b: the three paragraphs of version 10, each the paragraph read beside his '
                  'post in read-1125a with the one word its finding asked for (READER.md here)',
       'coverage': cov, 'findings': [], 'dispositions': {}}
(HERE / 'READ-RECORD.json').write_text(json.dumps(rec, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
print(len(cov), 'covered')
