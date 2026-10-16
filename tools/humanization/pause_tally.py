#!/usr/bin/env python3
"""pause_tally.py - the phrases two or more cold reads paused at, across rounds, in text that isn't Joel's (2026-10-16).

Joel, 2026-10-16 18:22 UTC, on section 13's "From Visitor to Member—Slowly", where a paragraph opened with my "How do
you know?" right after a paragraph of questions to write down: "i would cut the first sentence "How do you know?" ...
why did the reviewer not cut that, what's that? know what? doesn't seem to follow...". Four cold reads in three rounds
(r9, r11, r14 twice) had paused there and then settled it from the next sentence ("read as how to judge a newcomer"),
so the cold-read prompt's "a reader who pauses and then gets it isn't lost" kept it out of their findings, and the
dispositions only answered findings. The traces listed it as an added "lead-in", "frame" or "hook" and, as their brief
says of additions, asked for no fix. The signal was there four times; nothing counted it.

This counts it. Each cold read ends with a "Paused:" line (sense_section.txt, 2026-10-16); older reports mention their
pauses in prose. A phrase quoted with its paragraph number (P20 "How do you know?") on such a line counts once per report.

  python3 tools/humanization/pause_tally.py REPORT.md [REPORT.md ...] [--draft DRAFT.md] [--ledger OWNER-EDITS.json]
      [--owner-text FILE ...] [--min 2] [--dispositions DISPOSITIONS.md]

--draft keeps only phrases still in the draft. --ledger and --owner-text leave out phrases inside Joel's own sentences
(the author marks of meaning_sweep.py). With --dispositions, each repeated pause needs a line in that file quoting it
(fixed, or kept with a reason); exit 1 lists the ones without one.
"""
import argparse
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import meaning_sweep  # noqa: E402

PAUSE_LINE = re.compile(r'paus', re.I)
PHRASE = re.compile(r'\bP(\d+)[\s:,]+(?:"([^"\n]+)"|“([^”\n]+)”)')


def norm(s):
    s = s.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')
    s = re.sub(r'[*_`]', '', s)
    s = re.sub(r'\s+', ' ', s).strip().lower()
    return s.strip(' .,;:!?"\'')


def pauses(report_text):
    """[(paragraph number, quoted phrase)] from the lines of one report that talk about pausing."""
    out = []
    for line in report_text.splitlines():
        if not PAUSE_LINE.search(line):
            continue
        if re.match(r'\s*paused:\s*none\b', line, re.I):
            continue
        for m in PHRASE.finditer(line):
            out.append((int(m.group(1)), m.group(2) or m.group(3)))
    return out


def tally(reports):
    """{normalized phrase: {'quote': spelling, 'seen': [(report, P-number)]}}, one count per report. Readers quote more or
    less of the same words ("the full sequence", "For the full sequence"), so a phrase that holds a shorter one counts with
    it, under the shorter spelling."""
    raw = []
    for rep in reports:
        text = pathlib.Path(rep).read_text(encoding='utf-8')
        for p, q in pauses(text):
            k = norm(q)
            if k:
                raw.append((k, q, rep, p))
    keys = sorted({k for k, _, _, _ in raw}, key=len)
    root = {}
    for k in keys:
        root[k] = next((r for r in keys if len(r) < len(k) and r in k and root.get(r) == r), k)
    seen = {}
    for k, q, rep, p in raw:
        g = root[k]
        e = seen.setdefault(g, {'quote': q if k == g else None, 'seen': []})
        if k == g and e['quote'] is None:
            e['quote'] = q
        if rep not in [r for r, _ in e['seen']]:
            e['seen'].append((rep, p))
    for g, e in seen.items():
        if e['quote'] is None:
            e['quote'] = g
    return seen


def owner_spans(draft_text, ledger=None, owner_files=None):
    """The draft's visible text with Joel's sentences wrapped in author marks (empty marks when no owner input)."""
    owners = meaning_sweep.owner_strings(ledger, owner_files)
    vis = meaning_sweep.visible(draft_text)
    return meaning_sweep.mark_author(vis, owners) if owners else vis


def in_marks(marked, phrase):
    """True when every place the phrase occurs in the marked text is inside author marks."""
    t = norm(marked.replace(meaning_sweep.MARK_OPEN, ' \x01 ').replace(meaning_sweep.MARK_CLOSE, ' \x02 '))
    k = norm(phrase)
    hits = [m.start() for m in re.finditer(re.escape(k), t)]
    if not hits:
        return False
    for h in hits:
        before = t[:h]
        if before.count('\x01') <= before.count('\x02'):
            return False
    return True


def repeated(reports, draft=None, ledger=None, owner_files=None, minimum=2):
    found = []
    marked = None
    if draft:
        marked = owner_spans(pathlib.Path(draft).read_text(encoding='utf-8'), ledger, owner_files)
    for k, v in sorted(tally(reports).items(), key=lambda kv: -len(kv[1]['seen'])):
        if len(v['seen']) < minimum:
            continue
        if marked is not None:
            plain = norm(marked.replace(meaning_sweep.MARK_OPEN, ' ').replace(meaning_sweep.MARK_CLOSE, ' '))
            if k not in plain:
                continue
            if in_marks(marked, v['quote']):
                continue
        found.append({'quote': v['quote'], 'count': len(v['seen']), 'seen': v['seen']})
    return found


def unanswered(found, dispositions_text):
    d = norm(dispositions_text)
    return [f for f in found if norm(f['quote']) not in d]


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n\n')[0])
    ap.add_argument('reports', nargs='+')
    ap.add_argument('--draft')
    ap.add_argument('--ledger')
    ap.add_argument('--owner-text', action='append', default=[])
    ap.add_argument('--min', type=int, default=2)
    ap.add_argument('--dispositions')
    a = ap.parse_args(argv)
    found = repeated(a.reports, a.draft, a.ledger, a.owner_text, a.min)
    for f in found:
        where = ', '.join('%s P%d' % (r, p) for r, p in f['seen'])
        print('REPEATED PAUSE (%d reports): "%s" -- %s' % (f['count'], f['quote'], where))
    if not found:
        print('no phrase paused at in %d or more reports' % a.min)
    if a.dispositions:
        left = unanswered(found, pathlib.Path(a.dispositions).read_text(encoding='utf-8'))
        for f in left:
            print('NOT ANSWERED in %s: "%s"' % (a.dispositions, f['quote']))
        print('verdict: %s' % ('FAIL' if left else 'PASS'))
        return 1 if left else 0
    return 0


if __name__ == '__main__':
    sys.exit(main())
