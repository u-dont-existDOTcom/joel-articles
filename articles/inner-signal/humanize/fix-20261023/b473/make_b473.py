"""Batch 473's seam (question 14) as two 4.1 edits for EDITS41.json (2026-10-23): EDITS-b473.json.

The seam between the shortcut's section and the return read AI, High, in the whole guide (recheck A of 2026-10-22,
https://www.pangram.com/feed/47610d4b-fb69-4966-896f-317b029fc1af, windows 77 to 79) and in six versions of mine (E227).
Joel, 2026-10-23 12:30 UTC: "there is another emulate trick, you can take text emulate gives which doesn't pass, and
re-run it, and then it can pass". The installed pair was re-run through Emulate three times (../emu-seam/: emu-hg-bi, bj,
bk). Its new versions:
- the shortcut section's last paragraph is re-run bj's, with the two points it dropped put back ("qualified", "right away";
  FIXES.json): Human, High, alone (b473_seam_bj_p1);
- the return's first paragraph is re-run bk's as Emulate wrote it, the only sample that keeps "your body belongs to you":
  with the paragraph above, Human, High, as one window (b473_seam_pair).
Both checks are on API-CHECKS.md with their Pangram pages. The second reader's report is REVIEW.md, and its triage is in
TRIAGE.json; any fix it makes is applied below (TRIAGE_FIXES) and the result is read in place in the next recheck of part A.

  python3 articles/inner-signal/humanize/fix-20261023/b473/make_b473.py   (from the repo root)
  then: python3 articles/inner-signal/humanize/fix-20261020/apply_edits41.py --add articles/inner-signal/humanize/fix-20261023/b473/EDITS-b473.json
"""
import json, pathlib

B = pathlib.Path(__file__).resolve().parent
H = B.parents[1]
OLD1 = 'To turn this off, stop rehearsing it,'
OLD2 = "Make sure to reverse anything you've done to alter your state when you come out of it."  # straight, as the working copy
# (replace, with) pairs from TRIAGE.json, applied to the checked text: the first was checked alone (b473_seam_bj_p1_t:
# Human, High and Medium), the second (three of the published words) is read in place in the next recheck
TRIAGE_FIXES = [('You may want to say that you won’t use this one anymore in your waking life,',
                 'You’ll want to say, while you’re awake, that you won’t use this one anymore,'),
                ('If you have regressed or are working with parts,', 'If you have met a younger state or are working with parts,')]


def paragraph(md, first):
    a = md.index(first)
    b = md.index('\n', a)
    assert md.count(first) == 1
    return md[a:b]


def main():
    md = (H / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
    t = json.loads((B / 'TEXTS.json').read_text(encoding='utf-8'))
    p1, p2 = t['b473_seam_pair'].split('\n')
    assert p1 == t['b473_seam_bj_p1']
    for a, b in TRIAGE_FIXES:
        hit = [p for p in (p1, p2) if a in p]
        assert len(hit) == 1 and hit[0].count(a) == 1, a
        p1, p2 = p1.replace(a, b), p2.replace(a, b)
    assert p1 == t['b473_seam_bj_p1_t'], 'the shortcut paragraph must be the text that try 5 checked'
    # the working copy keeps straight quotes, as the earlier edits did; the check's text (substack_check_text) and
    # Substack's editor make them curly again, which is how the API read them
    plain = str.maketrans({'’': "'", '‘': "'", '“': '"', '”': '"'})
    p1, p2 = p1.translate(plain), p2.translate(plain)
    links = {r['name']: r['dashboard_link'] for f in sorted(B.glob('API-RESULTS-*.jsonl'))
             for r in map(json.loads, f.read_text(encoding='utf-8').splitlines()) if r}
    src = ('Emulate\'s re-run of the installed pair (Joel, 2026-10-23 12:30 UTC: "you can take text emulate gives which '
           'doesn\'t pass, and re-run it, and then it can pass"; ../emu-seam/)')
    edits = [
        {'key': 'HG17-b473', 'section': 'HG17', 'source': src + ', sample bj, with "qualified" and "right away" put back',
         'batch': '473', 'old': paragraph(md, OLD1), 'new': p1,
         'paragraph_check': links['b473_seam_bj_p1_t'],
         'paragraph_result': ('Human Written, 0% AI, High and Medium windows (144 words), with the reader\'s fix in; without it, '
                              'Human Written, 0% AI, one window, High (146 words): ' + links['b473_seam_bj_p1']),
         'section_check': links['b473_seam_pair'],
         'section_result': 'before the reader\'s two fixes, with the return paragraph below: Human Written, 0% AI, one window, High (275 words)',
         'review': 'fix-20261023/b473/REVIEW.md', 'triage_fixes': [list(x) for x in TRIAGE_FIXES[:1]], 'triage': 'fix-20261023/b473/TRIAGE.json'},
        {'key': 'HG18-b473', 'section': 'HG18', 'source': src + ', sample bk, as Emulate wrote it',
         'batch': '473', 'old': paragraph(md, OLD2), 'new': p2,
         'paragraph_check': links['b473_seam_pair'],
         'paragraph_result': ('before the reader\'s fix ("met a younger state", the published words), with the paragraph above: Human '
                              'Written, 0% AI, one window, High (275 words); the pair\'s lineage has used its six tries, so the fix '
                              'is read in place'),
         'section_check': None, 'section_result': 'read in place in the next recheck of part A',
         'review': 'fix-20261023/b473/REVIEW.md', 'triage_fixes': [list(x) for x in TRIAGE_FIXES[1:]], 'triage': 'fix-20261023/b473/TRIAGE.json'},
    ]
    (B / 'EDITS-b473.json').write_text(json.dumps(edits, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print('EDITS-b473.json: 2 edits (%d and %d words)' % (len(p1.split()), len(p2.split())))


if __name__ == '__main__':
    main()
