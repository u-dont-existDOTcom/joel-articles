#!/usr/bin/env python3
"""paragraphs_alone.py - before a section goes into the article, show that every paragraph read Human alone in Pangram.

Joel's rule of 2026-10-01 (docs/HUMANIZATION-GATE.md, "Every paragraph passes alone"): a section that passes with a paragraph
that fails alone doesn't count, "usually there are still ai tells you're missing in the paragraph". A paragraph under 50 words
(Pangram's minimum, counted by spaces) is checked with the paragraph before it in its subsection, or the one after it.

Why this exists (2026-10-16): section 13 went into the article checked only in groups and as a whole, and Joel asked at 23:38
UTC "no ai tells you see, and it has human tells? isn't that part of the rules?" Batch 312g then checked each paragraph alone
for the first time and found the short visit reading AI.

Usage: python3 tools/humanization/paragraphs_alone.py DRAFT.md BATCH_DIR [BATCH_DIR ...]
Each BATCH_DIR holds drafts.json (key -> the exact text Pangram read) and bNNN-results.json (key -> [headline, ai, words,
windows, time, link tail, flagged], as the in-page reader writes it). Exit 0 when every paragraph has a Human result alone
(or with its neighbor), 1 otherwise; the report names each paragraph without one.
"""
import json
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / 'articles' / 'intentional-communities' / 'candidate'
                       / 'fix-20261014'))
from ptext import plain  # noqa: E402


def paragraphs(md):
    """(heading or None, paragraph text) for each paragraph; images and comments are skipped."""
    out, head = [], None
    for b in re.split(r'\n\s*\n', md):
        b = b.strip()
        if not b or b.startswith('<!--') or b.startswith('[image') or b.startswith('[caption'):
            continue
        if b.startswith('#'):
            head = b
            continue
        out.append((head, b))
    return out


def results(dirs):
    seen = {}
    for d in dirs:
        d = pathlib.Path(d)
        drafts = json.loads((d / 'drafts.json').read_text(encoding='utf-8'))
        for f in d.glob('*-results.json'):
            for k, r in json.loads(f.read_text(encoding='utf-8')).items():
                if k in drafts:
                    text = drafts[k]['text'] if isinstance(drafts[k], dict) else drafts[k]
                    seen.setdefault(text, []).append((k, r[0], d.name))
    return seen


def check(md, dirs):
    paras = paragraphs(md)
    seen = results(dirs)
    report, ok = [], True
    for i, (head, p) in enumerate(paras):
        t = plain(p)
        tries = [t]
        if len(t.split()) < 50:
            same = lambda j: 0 <= j < len(paras) and paras[j][0] == head
            tries = ([plain(paras[i - 1][1]) + '\n\n' + t] if same(i - 1) else []) + \
                    ([t + '\n\n' + plain(paras[i + 1][1])] if same(i + 1) else [])
        got = [r for x in tries for r in seen.get(x, [])]
        human = [r for r in got if r[1].startswith('Human')]
        if human:
            report.append('ok   %s (%s)' % (t[:60], ', '.join('%s/%s' % (r[2], r[0]) for r in human)))
        else:
            ok = False
            report.append('MISS %s: %s' % (t[:60], 'read %s' % ', '.join('%s/%s %s' % (r[2], r[0], r[1]) for r in got)
                                           if got else 'never checked alone'))
    return ok, report


def main():
    md = pathlib.Path(sys.argv[1]).read_text(encoding='utf-8')
    ok, report = check(md, sys.argv[2:])
    print('\n'.join(report))
    print('paragraphs_alone: %s' % ('PASS' if ok else 'FAIL'))
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()
