"""The standard typographic swap on the neuro de-armoring article (gate E337 (gut); Joel, 2026-11-03 22:02 UTC: "yes make
that swapping standard"): curly quote marks straight, each em dash his spaced en dash. tools/humanization/typography_swap.py
does it; nothing else changes.

Three paragraphs keep their curly marks: in the measurement behind the rule (pangram-humanization-lab,
state/experiments/quote-style-41-20261103/FINDINGS.md), this article was the only one where straightening hurt more than
it helped, and these three read worse straightened:
- "As we grow up, our “Role-Self” becomes calcified ...": Mixed, from 29% to 9% human
  (before https://www.pangram.com/history/3af7b498-1660-4d25-b5cd-36cdc286f9aa,
  after https://www.pangram.com/history/f4aca799-b6eb-41f3-8315-a91d8ad70171);
- "Advanced tactic: The D-Serine Memory Re-consolidator ...": Human below High to Mixed
  (after https://www.pangram.com/history/1629acf7-0fa9-413b-a1dd-05bcad93315d);
- "Mechanism: The Dynorphin block is active ...": Human below High to Mixed
  (after https://www.pangram.com/history/c7809c0a-4c7b-43dd-91b2-442e5dfb7b82).
A paragraph rewritten later is swapped then (its old marks don't carry over to new words).

  python3 articles/neuro-de-armoring/humanize/fix-20261104/swap/swap_x1104.py [--check]
Writes HUMANIZED-SO-FAR.md and SWAPPED.json (the blocks changed, and the three kept).
"""
import argparse
import hashlib
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parents[1]
ROOT = H.parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import suggestion_review as sr  # noqa: E402
import typography_swap as ts  # noqa: E402

ARTICLE = H / 'HUMANIZED-SO-FAR.md'
BEFORE = '6db92b7aff987195049b8af1f99883ec4a3f2e05e62af6a978679871c7957944'
KEEP = ('As we grow up, our “Role-Self” becomes calcified', 'Advanced tactic: The D-Serine Memory Re-consolidator',
        'Mechanism: The Dynorphin block is active')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--check', action='store_true')
    a = ap.parse_args()
    md = ARTICLE.read_text(encoding='utf-8')
    assert hashlib.sha256(md.encode('utf-8')).hexdigest() == BEFORE, 'the article changed'
    bl = sr.blocks(md)
    raw = re.split(r'\n\s*\n', md.rstrip('\n'))
    assert len(raw) == len(bl)
    kept = [b['i'] for b in bl if b['text'].startswith(KEEP)]
    assert len(kept) == 3, kept
    changed = []
    for i, r in enumerate(raw):
        if i in kept:
            continue
        new, n = ts.swap_text(r)
        if n:
            raw[i] = new
            changed.append({'block': i, 'where': sr.where(bl, i), 'marks': n})
    out = '\n\n'.join(raw) + '\n'
    after = hashlib.sha256(out.encode('utf-8')).hexdigest()
    nb = sr.blocks(out)
    assert len(nb) == len(bl)
    rec = {'about': 'the typographic swap (E337 (gut)) on the article; three paragraphs keep their marks (see the script)',
           'before_sha256': BEFORE, 'after_sha256': after, 'blocks_changed': len(changed),
           'marks_changed': sum(c['marks'] for c in changed), 'kept_curly': [{'block': i, 'where': sr.where(bl, i)} for i in kept],
           'changed': changed}
    print(json.dumps({k: v for k, v in rec.items() if k != 'changed'}, ensure_ascii=False, indent=1))
    if a.check:
        return
    ARTICLE.write_text(out, encoding='utf-8')
    (HERE / 'SWAPPED.json').write_text(json.dumps(rec, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')


if __name__ == '__main__':
    main()
