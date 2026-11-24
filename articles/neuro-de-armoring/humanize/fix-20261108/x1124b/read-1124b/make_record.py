#!/usr/bin/env python3
"""The comparison read's record for x1124b: the coverage hashes of the paragraphs his answers 62a to 65a changed
(read beside their words before in READER.md), with no finding rated 2 or 3."""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[6]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import compare_read as cr  # noqa: E402

HERE = pathlib.Path(__file__).resolve().parent
ARTICLE = HERE.parents[2] / 'HUMANIZED-SO-FAR.md'
STARTS = ['The armored brain projects its own internal threat level', 'Precautions/Side Effects: Do not use concurrently',
          'Rule: do not take 5-HTP on the same day as a psychedelic trip', 'Uridine Monophosphate: The more targeted option',
          '5-HTP: Not a dopamine tool.', 'Step 2: Check Your Baseline: Once your heart rate is back down',
          'The Metabolic Red Line: If your resting heart rate is elevated or HRV reduced',
          'So you can tell what each new thing does', 'UMP trial if the Void looks like DAWS',
          '5-HTP trial if the bottleneck looks serotonergic', 'Serotonin syndrome usually comes from']
blocks = cr.sr.blocks(ARTICLE.read_text(encoding='utf-8'))
cov = []
for s in STARTS:
    hit = [b for b in blocks if b['text'].startswith(s)]
    assert len(hit) == 1, (s, len(hit))
    cov.append(cr.phash(hit[0]['text']))
rec = {'format': 'compare-read-record-v1',
       'article': 'HUMANIZED-SO-FAR.md after his answers of 2026-11-24 21:43 UTC (62a, 63a, 64a, 65a): each changed '
                  'paragraph read beside its words before, in its section (READER.md)',
       'coverage': cov, 'findings': [], 'dispositions': {}}
(HERE / 'READ-RECORD.json').write_text(json.dumps(rec, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
print(len(cov), 'covered')
