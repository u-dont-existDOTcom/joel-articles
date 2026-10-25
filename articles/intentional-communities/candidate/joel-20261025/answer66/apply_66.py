"""The community article with Joel's answers to question 66, the Emulate check page, put in. His message of 2026-10-25
23:05 UTC (../joel-20261025-2305-message.txt): "66a", with his answers file (../emulate-check/ANSWERS-20261025-2304.json,
exported from the page at 23:04:36Z): IC-E1, IC-E2, IC-E3 and IC-T1 approved; IC-Q1 (the three quote marks) and IC-E4
(autonomy and rights) rejected, so those stay as they are.

The input is ../../joel-20261024/answer65/WORKING.html, the version his post has had since he pasted it on 2026-10-25
(his post at https://ibogaqueen.substack.com/p/building-healing-community-escuelitas, "Updated: Oct 25 2026", read in the
browser at 23:13 UTC: it has the How-To Manual, his kibbutz image and the four sentences as they were). Each approved
card's changes (../emulate-check/build_emulate_review.py, CARDS) go into the matching paragraph of WORKING.html as
plain-text edits with links and bold kept on their words (tools/humanization/html_text_edit.set_text). The words that
change are exactly the cards' words: the script checks that the article's text before and after differs only there.
Because his post is already up, the same four changes go to him as words to change in Substack (SUBSTACK-EDITS.md).

Writes WORKING.html, ARTICLE.txt, READING-COPY.md, RECORD-66.json and SUBSTACK-EDITS.md beside this file.

  python3 articles/intentional-communities/candidate/joel-20261025/answer66/apply_66.py   (from the repo root)
"""
import collections
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
J25 = HERE.parent
CAND = J25.parent
REPO = HERE.parents[4]
sys.path.insert(0, str(REPO / 'tools' / 'humanization'))
sys.path.insert(0, str(J25 / 'emulate-check'))
import clarity_read as C  # noqa: E402
import html_text_edit as T  # noqa: E402
import build_emulate_review as B  # noqa: E402

SRC = CAND / 'joel-20261024' / 'answer65' / 'WORKING.html'
ANSWERS = J25 / 'emulate-check' / 'ANSWERS-20261025-2304.json'
FLAT = str.maketrans({'“': '"', '”': '"', '‘': "'", '’': "'", '\xa0': ' '})


def words(s):
    return re.sub(r'[^\w]+', ' ', s.translate(FLAT).lower()).split()


def find(doc, quote):
    hits = [p for p in T.paragraphs(doc) if p[4].translate(FLAT).count(quote.translate(FLAT)) == 1]
    assert len(hits) == 1, (quote[:60], len(hits))
    return hits[0]


def main():
    ans = json.loads(ANSWERS.read_text(encoding='utf-8'))
    assert ans['review_id'] == 'intentional-communities-emulate-check-20261025', ans['review_id']
    status = {x['id']: x for x in ans['items']}
    cards = {c[0]: c for c in B.CARDS}
    assert set(status) == set(cards), (sorted(status), sorted(cards))
    doc = SRC.read_text(encoding='utf-8')
    rec, added, removed, edits = [], collections.Counter(), collections.Counter(), []
    for cid in [c[0] for c in B.CARDS]:
        x, (_id, typ, _anchor, pairs, title, *_rest) = status[cid], cards[cid]
        entry = {'card': cid, 'title': title, 'answer': x['status'], 'comment': x.get('comment') or ''}
        if x['status'] != 'approved':
            assert x['status'] == 'rejected' and not x.get('your_version'), (cid, x['status'])
            entry['done'] = 'stays as it is (rejected)'
            rec.append(entry)
            continue
        assert pairs, cid
        changes = []
        for old, new in pairs:
            start, end, ia, ib, plain = find(doc, old)
            k = plain.translate(FLAT).find(old.translate(FLAT))
            old_here = plain[k:k + len(old)]
            new_text = plain[:k] + new + plain[k + len(old):]
            inner, dropped, moved = T.set_text(doc[ia:ib], new_text)
            assert not dropped, (cid, dropped)
            doc = doc[:ia] + inner + doc[ib:]
            a, b = collections.Counter(words(old_here)), collections.Counter(words(new))
            added.update(b - a)
            removed.update(a - b)
            changes.append({'old': old_here, 'new': new, 'paragraph_after': new_text, 'markup_moved': moved})
            edits.append((cid, title, old_here, new))
        # his page showed the paragraph as it would read; check the article now says exactly that
        mine = re.sub(r'\s+', ' ', x['my_version']).strip().translate(FLAT)
        assert all(mine.find(re.sub(r'\s+', ' ', c['new']).translate(FLAT)) >= 0 for c in changes), cid
        entry.update(done='in', changes=changes)
        rec.append(entry)
    before = collections.Counter(words(C.reading_text(SRC.read_text(encoding='utf-8'), 'html')))
    after = collections.Counter(words(C.reading_text(doc, 'html')))
    assert after == before - removed + added, 'something besides the approved cards changed'
    (HERE / 'WORKING.html').write_text(doc, encoding='utf-8')
    (HERE / 'ARTICLE.txt').write_text(C.reading_text(doc, 'html'), encoding='utf-8')
    (HERE / 'RECORD-66.json').write_text(json.dumps(rec, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    nums = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six'}
    ncards = len({e[0] for e in edits})
    lines = ['# %s changes for your post in Substack (question 66)' % nums[len(edits)].capitalize(), '',
             'Your post is up with the version of 2026-10-25, so here are your %s approved cards as %s changes to make in '
             'Substack\'s editor, in the order they come in the post. For each: find the old words (ctrl+f in the editor), '
             'select them, and type or paste the new ones. Links and bold aren\'t touched by any of them.'
             % (nums[ncards], nums[len(edits)]), '']
    for n, (cid, title, old, new) in enumerate(edits, 1):
        lines += ['%d. %s (%s)' % (n, title, cid), '', '   Old: %s' % old, '', '   New: %s' % new, '']
    (HERE / 'SUBSTACK-EDITS.md').write_text('\n'.join(lines).rstrip() + '\n', encoding='utf-8')
    try:
        from markdownify import markdownify
        md = re.sub(r'\n{3,}', '\n\n', markdownify(re.sub(r'<(strong|em|b|i|u|s|a)\b[^>]*>(\s+)</\1>', r'\2', doc),
                                                    heading_style='ATX', bullets='-', strip=['span'])).strip()
        (HERE / 'READING-COPY.md').write_text(
            '> A reading copy of the article with your answers to 66 in (WORKING.html beside this file; apply_66.py, '
            'RECORD-66.json). Before them it was your post as you pasted it on 2026-10-25 '
            '(../../joel-20261024/answer65/).\n\n' + md + '\n', encoding='utf-8')
    except ImportError:
        print('no markdownify here: READING-COPY.md not rebuilt')
    print('%d in, %d rejected; words added %s, removed %s' % (
        sum(r['done'] == 'in' for r in rec), sum(r['done'].startswith('stays') for r in rec), sum(added.values()),
        sum(removed.values())))


if __name__ == '__main__':
    main()
