"""HIS-STUDY.md: each of Joel's own versions of 2026-10-30 (his answers of 14:35 UTC, status "revise") beside the words it
replaced, the writers' two tries for the same words where his cards page had them (REVIEW-483's "why"), his comment, and
how his version read in place in the recheck of 30 October (SPOTS.json). The study behind gate E303: what his versions
do that the tries didn't. The reading of it is mine (the lead session); this only lays it out.

  python3 articles/inner-signal/humanize/fix-20261030/recheck/read/his_study.py
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parents[2]
REV = H / 'fix-20261029' / 'b483' / 'review'


def main():
    answers = json.loads((REV / 'ANSWERS-20261030-1435.json').read_text(encoding='utf-8'))
    cards = {c['id']: c for c in json.loads((REV / 'REVIEW-483.json').read_text(encoding='utf-8'))['suggestions']}
    spots = json.loads((HERE / 'SPOTS.json').read_text(encoding='utf-8'))['spots']
    lines = ['# His versions of 30 October beside the writers\' tries', '',
             'Each of his 19 versions (his cards page of 29 October, answered at 14:35 UTC on 30 October) with the words it '
             'replaced, the writers\' two tries where the page had them, his comment, and how his version read in place '
             'in the recheck of 30 October. Gate E303 says what his do that the tries didn\'t.', '']
    n = 0
    for it in answers['items']:
        if it.get('status') != 'revise':
            continue
        n += 1
        c = cards.get(it['id'], {})
        why = c.get('why', '')
        t1 = re.search(r'The paragraph as it read then:\n(.*?)(?=\n\nTry 2|$)', why, re.S)
        t2 = re.search(r'Try 2[^\n]*\n(.*?)(?=\n\n[A-Z]|$)', why, re.S)
        reads = [s['reading'] for s in spots if s['kind'].endswith('(%s)' % it['id'])]
        before = ' / '.join(e.get('before', '') for e in (c.get('edits') or []))
        lines += ['## %s (%s; %s)' % (it['id'], it.get('type', ''), it.get('where', '')), '',
                  '- **His comment:** %s' % ((it.get('comment') or '').strip() or '(none)'),
                  '- **The words before:** %s' % (before or '(see his cards page)')]
        if t1:
            lines.append('- **A writer\'s try:** %s' % t1.group(1).strip())
        if t2:
            lines.append('- **The other try:** %s' % t2.group(1).strip())
        lines += ['- **His version:** %s' % (it.get('your_version') or '').strip(),
                  '- **How his read in place:** %s' % (', '.join(reads) or 'in a paragraph listed under "Other changes" '
                                                      'in SPOTS.md (a typo fixed in it)'), '']
    (HERE / 'HIS-STUDY.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print(n, 'versions')


if __name__ == '__main__':
    main()
