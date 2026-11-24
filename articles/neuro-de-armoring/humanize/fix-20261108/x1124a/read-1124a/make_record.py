#!/usr/bin/env python3
"""The comparison read's record for x1124a: the coverage hashes of the paragraphs his answers 57 to 61 changed or added
(read beside their words before in READER.md), with no finding rated 2 or 3."""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[6]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import compare_read as cr  # noqa: E402

HERE = pathlib.Path(__file__).resolve().parent
ARTICLE = HERE.parents[2] / 'HUMANIZED-SO-FAR.md'
STARTS = ['The Void Bridge (Apathy / DAWS-pattern Void):', 'Mechanism: DeltaFosB is still holding the armor',
          'The idea is that D-serine facilitates', "For the zinc, I'd use zinc carnosine, since",
          'So you can tell what each new thing does', "Lion's Mane & Ashwagandha: I'm not advising",
          'Agmatine can leave some folks flat and numb', 'Step 2: Check Your Baseline: Once your heart rate']
blocks = cr.sr.blocks(ARTICLE.read_text(encoding='utf-8'))
cov = []
for s in STARTS:
    hit = [b for b in blocks if b['text'].startswith(s)]
    assert len(hit) == 1, (s, len(hit))
    cov.append(cr.phash(hit[0]['text']))
rec = {'format': 'compare-read-record-v1',
       'article': 'HUMANIZED-SO-FAR.md after his cards W-LMA and W-AGM and his answers of 2026-11-24 18:47 UTC (57 to 61): '
                  'each changed or new paragraph read beside its words before, in its section (READER.md)',
       'coverage': cov, 'findings': [], 'dispositions': {}}
(HERE / 'READ-RECORD.json').write_text(json.dumps(rec, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
print(len(cov), 'covered')
