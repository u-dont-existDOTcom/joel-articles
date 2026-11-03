"""Joel's answers to Community Article Cards, 30 October (ANSWERS-20261101-1857.json, exported 2026-11-01 18:57 UTC):
17 approved, and his answers to the two questions (C-9 "2nd yeah", C-15 "both"). On C-3 he added: "you didn't need to ask
me for commas if they are clearly needed" (gate E308).

His post is live, so the changes go to him as old/new pairs to change in Substack's editor (SUBSTACK-EDITS.md), and into
a working copy of master.md (WORKING-20261101.md) made here, each pair checked to occur exactly once. When he says
they're in his post, read his post against the working copy and promote it (as joel-20261025/promote_20261026.py did).

  python3 articles/intentional-communities/candidate/fullread-20261030/review/apply_answers.py
"""
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parents[2]
ROOT = ART.parents[1]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import suggestion_review as sr  # noqa: E402

ANS = json.loads((HERE / 'ANSWERS-20261101-1857.json').read_text(encoding='utf-8'))
REV = json.loads((HERE / 'REVIEW-FULLREAD.json').read_text(encoding='utf-8'))
MD = (ART / 'master.md').read_text(encoding='utf-8')

# His answers to the two questions, as words (each read beside his published version: READ-ANSWERS.md).
QA = {
    'C-9': ('you can all meet in a rented or borrowed space, or at each other’s houses, long before anyone needs a land '
            'surveyor.',
            'you can all live together in a rented or borrowed space first, long before anyone needs a land surveyor.',
            '"2nd yeah": the second reading, living together there before anyone buys land, in the words the card gave '
            'for it.'),
    'C-15': ('but that’s something which varies a lot in every society also.',
             'but what counts as acceptable physical discipline varies a lot from one society to another, and it happens '
             'to some degree in every society, communes included.',
             '"both": the two readings the card gave, in one sentence (the card\'s "not only in communes" said as '
             '"communes included").'),
}


def main():
    cards = {s['id']: s for s in REV['suggestions']}
    assert ANS['review_id'] == REV['review_id']
    pairs, record = [], []
    for it in ANS['items']:
        cid = it['id']
        s = cards[cid]
        if it['advice'] == 'ask':
            old, new, why = QA[cid]
            pairs.append((cid, s['where'], old, new, why))
            record.append({'card': cid, 'answer': it['comment'], 'done': 'in, as his answer', 'old': old, 'new': new})
            continue
        assert it['status'] == 'approved' and not it['your_version'], cid
        assert it['my_version'] == s['edits'][0]['after'] and it['before'] == s['edits'][0]['before'], cid
        old, new = s['what'][1:-1].split('” becomes “')
        pairs.append((cid, s['where'], old, new, 'approved' + (' ("%s")' % it['comment'] if it['comment'] else '')))
        record.append({'card': cid, 'answer': 'approved', 'comment': it['comment'], 'done': 'in', 'old': old,
                       'new': new})
    text = MD
    for cid, where, old, new, _ in pairs:
        assert text.count(old) == 1, (cid, text.count(old))
        text = text.replace(old, new)
    (HERE / 'WORKING-20261101.md').write_text(text, encoding='utf-8')
    # every changed paragraph is the card's paragraph as it would read (the questions: with the answer's words)
    bl = sr.blocks(text)
    for cid, where, old, new, _ in pairs:
        hit = [b for b in bl if new in b['text']]
        assert len(hit) == 1, cid
    (HERE / 'RECORD-FULLREAD.json').write_text(json.dumps(record, ensure_ascii=False, indent=1) + '\n',
                                               encoding='utf-8')
    out = ['# Community article: the changes to make in Substack\'s editor (your answers of 1 November)', '',
           'Your post is live, so these are for you to change in Substack\'s editor: for each one, find the words under '
           '"Find" (Ctrl+F finds them) and replace them with the words under "Replace with", exactly as written. Then '
           'click Update. Nothing else changes. %d changes, in the order of the article.' % len(pairs), '']
    order = {b['text']: b['i'] for b in sr.blocks(MD)}

    def pos(p):
        return next(i for t, i in order.items() if p[2] in t)
    for n, (cid, where, old, new, why) in enumerate(sorted(pairs, key=pos), 1):
        out += ['## %d. %s (%s)' % (n, where, cid), '', '**Find:**', '', '> %s' % old, '', '**Replace with:**', '',
                '> %s' % new, '']
        if cid in QA:
            out += ['(Your answer %s)' % why, '']
    (HERE / 'SUBSTACK-EDITS.md').write_text('\n'.join(out), encoding='utf-8')
    print(len(pairs), 'changes; WORKING-20261101.md, SUBSTACK-EDITS.md, RECORD-FULLREAD.json')


if __name__ == '__main__':
    main()
