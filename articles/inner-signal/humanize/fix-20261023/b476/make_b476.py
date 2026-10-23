"""Batch 476: spelling (2026-10-23, after Joel's message of 16:55 UTC): the misspellings and British spellings that Emulate's
samples brought into the guide's working copy, put back to the published guide's spelling (master.html has none of them:
"solar plexus" four times, "behavior", "stabilize", "recognize", "realize"). The linter's O15 had flagged them ("a
misspelling gets fixed"), and the installs let them through; Joel, 2026-10-06: "don't preserve my obvious typos. no need
to recheck pangram to fix a typo". Each occurrence is one edit with enough of its sentence around it to be unique.

  python3 articles/inner-signal/humanize/fix-20261023/b476/make_b476.py   (from the repo root)
  then: python3 articles/inner-signal/humanize/fix-20261020/apply_edits41.py --add articles/inner-signal/humanize/fix-20261023/b476/EDITS-b476.json
"""
import json, pathlib, re

B = pathlib.Path(__file__).resolve().parent
H = B.parents[1]
FIXES = [  # (a whole word as it stands, the published spelling)
    ('plexis', 'plexus'), ('carefuly', 'carefully'), ('subconcious', 'subconscious'), ('supress', 'suppress'),
    ('somedays', 'some days'), ('neuroscientifcally', 'neuroscientifically'),
    ('realise', 'realize'), ('recognise', 'recognize'), ('visualise', 'visualize'), ('visualising', 'visualizing'),
    ('stabilise', 'stabilize'), ('stabilising', 'stabilizing'), ('destabilisation', 'destabilization'),
    ('lateralisation', 'lateralization'), ('behaviour', 'behavior'), ('behaviours', 'behaviors'),
    ('behavioural', 'behavioral'),
    ('analyse', 'analyze'), ('analysing', 'analyzing'),
]


def unique_context(md, a, b):
    """The shortest stretch around md[a:b], grown a word at a time on both sides within its line, that occurs once in md."""
    ls = md.rfind('\n', 0, a) + 1
    le = md.find('\n', b)
    le = len(md) if le < 0 else le
    lo, hi = a, b
    # at least three words on each side (within the line), so the fixed stretch can't already be somewhere else: the
    # list's runner counts an edit as in when its new text is in the working copy (a one-word "suppress" was)
    for _ in range(3):
        lo = max(ls, md.rfind(' ', ls, lo - 1) + 1) if lo > ls else ls
        nhi = md.find(' ', hi + 1, le)
        hi = le if nhi < 0 else nhi
    while md.count(md[lo:hi]) > 1:
        nlo = max(ls, md.rfind(' ', ls, lo - 1) + 1) if lo > ls else ls
        nhi = md.find(' ', hi + 1, le)
        nhi = le if nhi < 0 else nhi
        if (nlo, nhi) == (lo, hi):
            break
        lo, hi = nlo, nhi
    assert md.count(md[lo:hi]) == 1, md[lo:hi]
    return lo, hi


def main():
    """One edit per paragraph that has a misspelling, its whole line, all its fixes in: two in one sentence ("notice,
    realise, recognise") would otherwise make two edits whose stretches overlap, and the list's runner can't follow that."""
    md = (H / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
    pats = [(re.compile(r'(?<![\w/.-])%s(?![\w/-])(?!\.\w)' % re.escape(old)), old, new) for old, new in FIXES]
    edits = []
    for line in md.split('\n'):
        fixed, words = line, []
        for rx, old, new in pats:
            if rx.search(fixed):
                words.append('%s (%d)' % (old, len(rx.findall(fixed))))
                fixed = rx.sub(new, fixed)
        if fixed == line:
            continue
        assert md.count(line) == 1 and fixed not in md, line[:80]
        edits.append({'key': 'b476-spelling-%02d' % (len(edits) + 1), 'section': None, 'batch': '476',
                      'source': 'spelling: Emulate\'s %s back to the published guide\'s spelling (O15)' % ', '.join(words),
                      'old': line, 'new': fixed,
                      'paragraph_check': None, 'paragraph_result': 'a spelling fix: no Pangram check (Joel, 2026-10-06)',
                      'section_check': None, 'section_result': 'read in place in the next recheck', 'review': None})
    (B / 'EDITS-b476.json').write_text(json.dumps(edits, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print('EDITS-b476.json: %d paragraphs' % len(edits))
    for e in edits:
        print(' ', e['key'], '|', e['source'][10:90])


if __name__ == '__main__':
    main()
