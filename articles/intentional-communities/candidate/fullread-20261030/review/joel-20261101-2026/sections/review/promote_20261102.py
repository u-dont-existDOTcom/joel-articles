"""The community article's registered master, brought up to his post as of 2026-11-02: WORKING-20261102.md here, the
master of 2026-11-01 (promote_20261101.py) with the six edits of his answers to Community Article Cards, 1 November
(apply_ic1101.py, SUBSTACK-EDITS-IC1101.json: 4 approved, 2 his own versions), sent with his message of 2026-11-02
16:43 UTC.

The edits went into his post through its editor, as on 1 November (the card page said "Once you've marked them, I'll
make the changes in your post's editor"), and the public post, read through Substack's API afterwards, has all six and
the working copy's words (LIVE-CHECK-20261102.json). The steps after an accepted change are the last promotion's: the
receipt's line, the owner locks' note of which file is which, the editorial status, the current state, and the
registry's hashes. original.md, the text first published, stays as the published source and is never edited.

  python3 articles/intentional-communities/candidate/fullread-20261030/review/joel-20261101-2026/sections/review/promote_20261102.py
"""
import hashlib
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
A = HERE.parents[5]
REPO = A.parents[1]
INDEX = REPO / 'articles' / 'INDEX.json'
WORK = HERE / 'WORKING-20261102.md'
EDITS = HERE / 'SUBSTACK-EDITS-IC1101.json'
LIVE = HERE / 'LIVE-CHECK-20261102.json'
WHEN = '2026-11-02 16:43 UTC (his answers to Community Article Cards, 1 November: 4 approved, 2 his own versions)'


def sha(p):
    return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()


def rel(p):
    return pathlib.Path(p).relative_to(REPO).as_posix()


def main():
    out = A / 'master.md'
    old = out.read_text(encoding='utf-8')
    work = WORK.read_text(encoding='utf-8')
    edits = json.loads(EDITS.read_text(encoding='utf-8'))
    x = old
    if old != work:
        assert sha(out) == edits['master_before_sha256'], 'master.md is not the one the edits were made from'
        for e in edits['edits']:
            assert x.count(e['find']) == 1, e['find']
            x = x.replace(e['find'], e['replace'])
        assert x == work, 'the working copy is not the master with the six edits'
    live = json.loads(LIVE.read_text(encoding='utf-8'))
    assert live['all_six'] and live['live_against_working']['word_differences'] == 0
    old_sha = sha(out)
    out.write_text(work, encoding='utf-8')
    new_sha = sha(out)

    receipt = A / 'PROMOTION-RECEIPT-20261017.md'
    r = receipt.read_text(encoding='utf-8')
    line = ('- 2026-11-02 (after his message of 16:43 UTC): `master.md` is now `%s` (`%s`; %d UTF-8 bytes, SHA-256 %s; it '
            'was %s). That file is the last master with the six edits of his answers to Community Article Cards, 1 '
            'November (4 approved, 2 his own versions; `%s`), which went into his post through its editor; his post was '
            'read through Substack\'s API afterwards and has every edit and the working copy\'s words (`%s`).'
            % (rel(WORK), rel(pathlib.Path(__file__)), len(work.encode('utf-8')), new_sha, old_sha, rel(EDITS), rel(LIVE)))
    if '2026-11-02 (after his message of 16:43 UTC)' not in r:
        r = r.rstrip('\n') + '\n' + line + '\n'
        receipt.write_text(r, encoding='utf-8')

    locks = json.loads((A / 'OWNER-LOCKS.json').read_text(encoding='utf-8'))
    for f in locks['protected_functions']:
        if f['id'] == 'working-master-source-identity':
            f['description'] = ('The registered master is master.md: since 2026-11-02, %s (the master of 2026-11-01 with '
                                'the six edits of his answers to Community Article Cards, 1 November, accepted by him on '
                                '%s), put in place by %s; PROMOTION-RECEIPT-20261017.md lists each promotion. The published '
                                'Substack text first imported stays as original.md (97920 UTF-8 bytes, SHA-256 '
                                '5d2892335ba53e93147caf5588a11e660d3ff2180d1ab1b23ff9fc5b2eb99aa6); it is never edited.'
                                % (rel(WORK), WHEN, rel(pathlib.Path(__file__))))
    (A / 'OWNER-LOCKS.json').write_text(json.dumps(locks, ensure_ascii=False, indent=2), encoding='utf-8')   # its own format

    ed = json.loads((A / 'EDITORIAL-STATUS.json').read_text(encoding='utf-8'))
    if not any(a.get('section') == 'batch ic1101\'s cards (2 November)' for a in ed['accepted']):
        ed['accepted'].append({'section': 'batch ic1101\'s cards (2 November)', 'by': 'Joel', 'when': WHEN,
                               'words': 'his answers file: W-1, W-3, W-4 and W-6 approved; his own versions of W-2 and W-5',
                               'record': '%s, %s, %s' % (rel(HERE / 'ANSWERS-20261102-0029.json'), rel(EDITS), rel(LIVE))})
    if '2026-11-02' not in ed.get('note', ''):
        ed['note'] = ed.get('note', '') + (' 2026-11-02: the six edits of batch ic1101\'s cards are in his post and in '
                                           'master.md (PROMOTION-RECEIPT-20261017.md, "Changes since").')
    (A / 'EDITORIAL-STATUS.json').write_text(json.dumps(ed, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

    cs = (A / 'CURRENT-STATE.md').read_text(encoding='utf-8')
    note = ('## Now (2026-11-02)\n\n`master.md` is his post as of 2 November: the master of 1 November with the six edits '
            'of his answers to Community Article Cards, 1 November (his message of 2026-11-02 16:43 UTC), made in his post '
            'through its editor and read back from the public post (`%s`). Next: the two sections those edits touched, '
            'checked again by themselves (their second and last section check, lineages IC1101-01 and IC1101-02), and a '
            'fix for any window that reads AI or Human (Low) (E306). The sections below are the history of how the article '
            'got here.\n\n' % rel(LIVE))
    if '## Now (2026-11-02)' not in cs:
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
