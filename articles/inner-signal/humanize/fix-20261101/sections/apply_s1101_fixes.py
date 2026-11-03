"""Fixes for the windows of batch s1101 that read AI or Human (Low) in our words (gate E306), and the record of the rest.

Joel, 2026-11-01 18:57 UTC: "if a section reads ai or human low, we don't need to check it again to verify that, we
need to fix it", and the windows below High "are often smoothed over and vague", while Emulate "might make some regions
high conf with confabulation". So each fix below says the sentence's meaning plainly from his published version
(source/published-20260928.md), with nothing added that the guide doesn't say; I read each beside the published
passage and the paragraphs around it (the lead session, E294). FIXES-S1101.json holds them: per window, the words that
read AI or Human (Low), whose they are, and either a fix (old words, new words) in our words, or "card" (his words, to
his cards page), or "not prose" (a button's label, a heading word), with why.

  python3 articles/inner-signal/humanize/fix-20261101/sections/apply_s1101_fixes.py [--check]
Writes HUMANIZED-SO-FAR.md and APPLIED-S1101.json (each changed paragraph before and after).
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
sys.path.insert(0, str(H / 'fix-20261025' / 'review'))
import suggestion_review as sr  # noqa: E402
from apply_answers import set_block_text  # noqa: E402

GUIDE = H / 'HUMANIZED-SO-FAR.md'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--check', action='store_true')
    a = ap.parse_args()
    fx = json.loads((HERE / 'FIXES-S1101.json').read_text(encoding='utf-8'))
    md = GUIDE.read_text(encoding='utf-8')
    sha = hashlib.sha256(md.encode('utf-8')).hexdigest()
    assert sha.startswith(fx['guide_sha256'][:8]), 'the guide changed since the results were read: %s' % sha[:8]
    before = [b['text'] for b in sr.blocks(md)]
    lost, done = [], []
    for f in fx['windows']:
        if f['fate'] != 'fixed':
            continue
        for old, new in f['fix']:
            k = md.count(old)
            if k == 1:
                md = md.replace(old, new)
            else:
                assert k == 0, (f['id'], k, old[:60])
                raw = re.split(r'\n\s*\n', md.rstrip('\n'))
                bl = sr.blocks(md)
                hit = [i for i, b in enumerate(bl) if b['text'].count(old) == 1]
                assert len(hit) == 1, (f['id'], len(hit), old[:60])
                i = hit[0]
                raw[i] = set_block_text(raw[i], bl[i]['text'].replace(old, new), lost)
                md = '\n\n'.join(raw) + '\n'
        done.append(f['id'])
    after = [b['text'] for b in sr.blocks(md)]
    import difflib
    changed = []
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, before, after, autojunk=False).get_opcodes():
        if op != 'equal':
            changed.append({'op': op, 'before': before[i1:i2], 'after': after[j1:j2], 'after_blocks': list(range(j1, j2))})
    rec = {'before_sha256': sha, 'after_sha256': hashlib.sha256(md.encode('utf-8')).hexdigest(), 'fixed': done,
           'links_dropped': lost, 'changed': changed}
    print(json.dumps({k: rec[k] for k in ('before_sha256', 'after_sha256', 'links_dropped')}, indent=1), len(done),
          'windows fixed,', len(changed), 'changes')
    if not a.check:
        GUIDE.write_text(md, encoding='utf-8')
        (HERE / 'APPLIED-S1101.json').write_text(json.dumps(rec, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')


if __name__ == '__main__':
    main()
