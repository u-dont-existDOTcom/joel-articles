"""The community article's registered master, brought up to the version in Joel's post since 2026-11-01:
candidate/fullread-20261030/review/WORKING-20261101.md, the last master (promote_20261026.py) with the 19 changes of his
answers of 2026-11-01 18:57 UTC to the full read's cards page (17 approved, C-9 "2nd yeah", C-15 "both";
apply_answers.py, RECORD-FULLREAD.json).

He was to make the 19 changes in his post himself (SUBSTACK-EDITS.md); at 20:26 UTC he wrote "i didn't make the edits
to community guide, that's too much. you can do that." (joel-20261101-2026-message.txt). They went in through his post's
editor in the app's browser, and the public post, read through Substack's API afterwards, has every one of them and the
working copy's words in order, apart from structure (LIVE-CHECK-20261101.json: horizontal rules, list numbers, an embed's
own text, list items run together in the HTML text, a line break). The changed paragraphs haven't had a Pangram check
yet (CURRENT-STATE.md says so; it is the lane's next step). The steps after an accepted change are the last
promotion's: the receipt's line, the owner locks' note of which file is which, the editorial status, the current state,
and the registry's hashes. original.md, the text first published, stays as the published source and is never edited.

  python3 articles/intentional-communities/candidate/fullread-20261030/review/joel-20261101-2026/promote_20261101.py
"""
import hashlib
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
REVIEW = HERE.parent
CAND = REVIEW.parents[1]
A = CAND.parent
REPO = A.parents[1]
INDEX = REPO / 'articles' / 'INDEX.json'
WORK = REVIEW / 'WORKING-20261101.md'
EDITS = REVIEW / 'SUBSTACK-EDITS.md'
LIVE = HERE / 'LIVE-CHECK-20261101.json'
WHEN = ('2026-11-01 18:57 UTC (his answers to the full read\'s cards) and 20:26 UTC ("you can do that": the 19 changes '
        'made in his post for him)')


def sha(p):
    return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()


def rel(p):
    return pathlib.Path(p).relative_to(REPO).as_posix()


def main():
    out = A / 'master.md'
    old = out.read_text(encoding='utf-8')
    work = WORK.read_text(encoding='utf-8')
    pairs = re.findall(r'\*\*Find:\*\*\n\n> (.*?)\n\n\*\*Replace with:\*\*\n\n> (.*?)\n', EDITS.read_text(encoding='utf-8'))
    assert len(pairs) == 19, len(pairs)
    x = old
    if old != work:
        for o, n in pairs:
            assert x.count(o) == 1, o
            x = x.replace(o, n)
        assert x == work, 'the working copy is not the master with the 19 changes'
    live = json.loads(LIVE.read_text(encoding='utf-8'))
    assert live['the_19_changes_live']['all_19'] and live['live_against_working']['word_differences'] == 0
    old_sha = sha(out)
    out.write_text(work, encoding='utf-8')
    new_sha = sha(out)

    receipt = A / 'PROMOTION-RECEIPT-20261017.md'
    r = receipt.read_text(encoding='utf-8')
    line = ('- 2026-11-01 (after his messages of 18:57 and 20:26 UTC): `master.md` is now '
            '`candidate/fullread-20261030/review/WORKING-20261101.md` '
            '(`candidate/fullread-20261030/review/joel-20261101-2026/promote_20261101.py`; %d UTF-8 bytes, SHA-256 %s; it was '
            '%s). That file is the last master with the 19 changes of his answers to the full read\'s cards page (17 approved, '
            'C-9 "2nd yeah", C-15 "both"; `candidate/fullread-20261030/review/apply_answers.py`), which went into his post '
            'through its editor at his word ("i didn\'t make the edits to community guide, that\'s too much. you can do '
            'that."); his post was read through Substack\'s API afterwards and has every change and the working copy\'s words '
            '(`candidate/fullread-20261030/review/joel-20261101-2026/LIVE-CHECK-20261101.json`). No Pangram check of the '
            'changed paragraphs yet.' % (len(work.encode('utf-8')), new_sha, old_sha))
    if '2026-11-01 (after his messages of 18:57 and 20:26 UTC)' not in r:
        r = r.rstrip('\n') + '\n' + line + '\n'
        receipt.write_text(r, encoding='utf-8')

    locks = json.loads((A / 'OWNER-LOCKS.json').read_text(encoding='utf-8'))
    for f in locks['protected_functions']:
        if f['id'] == 'working-master-source-identity':
            f['description'] = ('The registered master is master.md: since 2026-11-01, '
                                'candidate/fullread-20261030/review/WORKING-20261101.md (the master of 2026-10-26 with the 19 '
                                'changes of his answers to the full read\'s cards, accepted by him on %s), put in place by '
                                'candidate/fullread-20261030/review/joel-20261101-2026/promote_20261101.py; '
                                'PROMOTION-RECEIPT-20261017.md lists each promotion. The published Substack text first imported '
                                'stays as original.md (97920 UTF-8 bytes, SHA-256 '
                                '5d2892335ba53e93147caf5588a11e660d3ff2180d1ab1b23ff9fc5b2eb99aa6); it is never edited.' % WHEN)
    (A / 'OWNER-LOCKS.json').write_text(json.dumps(locks, ensure_ascii=False, indent=2), encoding='utf-8')   # its own format

    ed = json.loads((A / 'EDITORIAL-STATUS.json').read_text(encoding='utf-8'))
    if not any(a.get('section') == 'the full read\'s cards (1 November)' for a in ed['accepted']):
        ed['accepted'].append({'section': 'the full read\'s cards (1 November)', 'by': 'Joel', 'when': WHEN,
                               'words': 'his answers file: 17 approved, C-9 "2nd yeah", C-15 "both"; on C-3, "you didn\'t need to '
                                        'ask me for commas if they are clearly needed"; then "i didn\'t make the edits to '
                                        'community guide, that\'s too much. you can do that."',
                               'record': 'fullread-20261030/review/ANSWERS-20261101-1857.json, '
                                         'fullread-20261030/review/RECORD-FULLREAD.json, '
                                         'fullread-20261030/review/joel-20261101-2026/joel-20261101-2026-message.txt, '
                                         'fullread-20261030/review/joel-20261101-2026/LIVE-CHECK-20261101.json'})
    if '2026-11-01' not in ed.get('note', ''):
        ed['note'] = ed.get('note', '') + (' 2026-11-01: the full read\'s 19 changes are in his post (made for him, at his '
                                           'word) and in master.md (PROMOTION-RECEIPT-20261017.md, "Changes since").')
    (A / 'EDITORIAL-STATUS.json').write_text(json.dumps(ed, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

    cs = (A / 'CURRENT-STATE.md').read_text(encoding='utf-8')
    note = ('## Now (2026-11-01)\n\nThe working copy is `candidate/fullread-20261030/review/WORKING-20261101.md`: the '
            '2026-10-26 master with the 19 changes of his answers to the full read\'s cards (his message of 2026-11-01 18:57 '
            'UTC). He asked me to make them in his post (20:26 UTC: "you can do that"); they went in through its editor, his '
            'post matches the working copy (`candidate/fullread-20261030/review/joel-20261101-2026/LIVE-CHECK-20261101.json`), '
            'and `master.md` is that version (PROMOTION-RECEIPT-20261017.md). Next: a Pangram check of the sections the 19 '
            'changes touched, each by itself (gate E307), and a fix for any window that reads AI or Human (Low) (E306). The '
            'sections below are the history of how the article got here.\n\n')
    if '## Now (2026-11-01)' not in cs:
        k2 = cs.index('\n## ')
        cs = cs[:k2 + 1] + note + cs[k2 + 1:]
        (A / 'CURRENT-STATE.md').write_text(cs, encoding='utf-8')

    idx = json.loads(INDEX.read_text(encoding='utf-8'))
    arts = idx['articles'] if isinstance(idx, dict) else idx
    art = next(a for a in arts if a['id'] == 'intentional-communities')
    art['authority']['master']['sha256'] = new_sha
    art['authority']['owner_locks']['sha256'] = sha(A / 'OWNER-LOCKS.json')
    art['authority']['current_state']['sha256'] = sha(A / 'CURRENT-STATE.md')
    art['review']['editorial']['sha256'] = sha(A / 'EDITORIAL-STATUS.json')
    art['review']['detector']['sha256'] = sha(A / 'DETECTOR-EVIDENCE.json')
    e = next(x for x in art['additional_artifacts'] if x['path'] == rel(receipt))
    e['sha256'] = sha(receipt)
    INDEX.write_text(json.dumps(idx, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print('master.md', new_sha, len(work.encode('utf-8')), 'bytes (was %s)' % old_sha[:12])


if __name__ == '__main__':
    main()
