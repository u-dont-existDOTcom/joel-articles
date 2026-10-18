#!/usr/bin/env python3
"""paragraphs_alone.py - before a section goes into the article, show that every paragraph read Human alone in Pangram.

Joel's rule of 2026-10-01 (docs/HUMANIZATION-GATE.md, "Every paragraph passes alone"): a section that passes with a paragraph
that fails alone doesn't count, "usually there are still ai tells you're missing in the paragraph". A paragraph under 50 words
(Pangram's minimum, counted by spaces) is checked with the paragraph before it in its subsection, or the one after it.
A short entry of a list (a reading list's one-line entries, 2026-10-17) that stays under 50 words even with its neighbor in its
subsection, or that has none there, is checked inside the shortest run around it that Pangram can read: consecutive
paragraphs in reader order, the headings between them included, at least 50 words, and dropping its first or last paragraph
(other than the entry) takes it under 50 (`minimal_runs`). The appendix of the community article was the first such list:
its subsections hold two or three entries of 8 to 40 words, so no pair under one heading reaches 50.

Why this exists (2026-10-16): section 13 went into the article checked only in groups and as a whole, and Joel asked at 23:38
UTC "no ai tells you see, and it has human tells? isn't that part of the rules?" Batch 312g then checked each paragraph alone
for the first time and found the short visit reading AI.

Usage: python3 tools/humanization/paragraphs_alone.py DRAFT.md BATCH_DIR [BATCH_DIR ...]
Each BATCH_DIR holds drafts.json (key -> the exact text Pangram read) and bNNN-results.json (key -> [headline, ai, words,
windows, time, link tail, flagged], as the in-page reader writes it, or key -> {"headline": ...} from the older reader). Exit 0 when every paragraph has a Human result alone
(or with its neighbor), 1 otherwise; the report names each paragraph without one.
"""
import json
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / 'articles' / 'intentional-communities' / 'candidate'
                       / 'fix-20261014'))
from ptext import plain  # noqa: E402


# The page's embed lines, which no reader reads as prose (2026-10-17, section 15): a linked post card ("[Title](url)Copy
# link") and a video's "Double click to interact with video".
EMBED = re.compile(r'^(\[[^\]]+\]\([^)\s]+\)Copy link|Double click to interact with video)$')


def paragraphs(md):
    """(heading or None, paragraph text) for each paragraph; images, captions, embed lines and comments are skipped."""
    out, head = [], None
    for b in re.split(r'\n\s*\n', md):
        b = b.strip()
        if not b or b.startswith('<!--') or b.startswith('[image') or b.startswith('[caption') or EMBED.match(b):
            continue
        if b.startswith('#'):
            head = b
            continue
        out.append((head, b))
    return out


def reader_blocks(md):
    """('h', heading) and ('p', paragraph) in reader order, skipped as paragraphs() skips them."""
    out = []
    for b in re.split(r'\n\s*\n', md):
        b = b.strip()
        if not b or b.startswith('<!--') or b.startswith('[image') or b.startswith('[caption') or EMBED.match(b):
            continue
        out.append(('h' if b.startswith('#') else 'p', b))
    return out


def _run(seq, pidx, a, b, lead=False):
    """The text Pangram reads for paragraphs a..b (indexes into the paragraph list), with the headings between them; with
    lead, also the headings right before paragraph a."""
    start = pidx[a]
    if lead:
        while start > 0 and seq[start - 1][0] == 'h':
            start -= 1
    return '\n\n'.join(plain(x.lstrip('#').strip()) if k == 'h' else plain(x) for k, x in seq[start:pidx[b] + 1])


def minimal_runs(md, i):
    """The shortest runs around paragraph i that Pangram can read (see the docstring): [(a, b, text, text with the leading
    headings)], a and b indexes into the paragraph list."""
    seq = reader_blocks(md)
    pidx = [n for n, (k, _) in enumerate(seq) if k == 'p']
    w = lambda a, b: len(_run(seq, pidx, a, b).split()) if a <= b else 0
    out = []
    for a in range(i, -1, -1):
        for b in range(i, len(pidx)):
            if w(a, b) >= 50 and (a == i or w(a + 1, b) < 50) and (b == i or w(a, b - 1) < 50):
                out.append((a, b, _run(seq, pidx, a, b), _run(seq, pidx, a, b, lead=True)))
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
                    seen.setdefault(text, []).append((k, r['headline'] if isinstance(r, dict) else r[0], d.name))
    return seen


def tries_for(md, paras, i):
    """(paragraph i's text, the texts any of which gives it its check). paras is paragraphs(md). A batch builder picks one
    of these to send (2026-10-18, the hypnosis guide's paragraph checks), so it sends what check() will look for."""
    head, p = paras[i]
    t = plain(p)
    tries = [t]
    if len(t.split()) < 50:
        same = lambda j: 0 <= j < len(paras) and paras[j][0] == head
        tries = ([plain(paras[i - 1][1]) + '\n\n' + t] if same(i - 1) else []) + \
                ([t + '\n\n' + plain(paras[i + 1][1])] if same(i + 1) else [])
    if len(t.split()) < 50 and not any(len(x.split()) >= 50 for x in tries):
        # a short list entry: the shortest runs around it that Pangram can read
        tries += [x for _, _, r, rl in minimal_runs(md, i) for x in (r, rl)]
    if head and (i == 0 or paras[i - 1][0] != head):
        # the first paragraph under a heading also counts when checked with its heading in front
        tries += [plain(head.lstrip('#').strip()) + '\n\n' + x for x in tries]
    return t, tries


def check(md, dirs):
    paras = paragraphs(md)
    seen = results(dirs)
    report, ok = [], True
    for i in range(len(paras)):
        t, tries = tries_for(md, paras, i)
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
