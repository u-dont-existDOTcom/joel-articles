"""Put Joel's answers to question 20, the Emulate check page, into the hypnosis guide (HUMANIZED-SO-FAR.md).

His message of 2026-10-25 23:05 UTC (../joel-20261025-2305-message.txt) came with his answers file
(ANSWERS-20261025-2300.json, exported from the page at 23:00:29Z): 17 cards approved, 2 revised and 1 rejected.
- Approved: the card's paragraph as the page showed it.
- Revised: his version, word for word. EM-Q1 (the quote marks, 51 paragraphs) comes back as one text of 51 paragraphs,
  taken paragraph by paragraph; beside the quote marks he changed four things in it: "coming back" keeps its quote marks
  (he typed them, straight), "Just because an idea should be a resource, that doesn't mean that it will be." goes,
  "force down protectors" is "force down guard parts", and "a childhood protector part" is "a childhood guard part".
  EM-16: his "if it's a guard".
- Rejected, EM-11, with his comment "actually emulate's version is better, hypnosis is for pain btw, surprised you
  didn't know that": the paragraph stays as Emulate wrote it, its quote marks too (the card took them off with the
  change, and his answer keeps the card's "before").
His comment on EM-Q1, "make sure we are not using "protector" to mean "guard", i saw that in finish without forcing, p2",
is a pass over the whole guide, done after this by guard_sweep.py.

Links and italics stay on their words (review/apply_answers.py's set_block_text, html_text_edit.set_text).

  python3 articles/inner-signal/humanize/fix-20261025/emulate-check/apply_answers_20.py [--check]
Writes HUMANIZED-SO-FAR.md and APPLIED-20.json (every card's fate, each paragraph before and after).
"""
import argparse
import hashlib
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
sys.path.insert(0, str(HERE.parent / 'review'))
import suggestion_review as sr  # noqa: E402
import apply_answers as AA  # noqa: E402

ARTICLE = ROOT / 'articles/inner-signal/humanize/HUMANIZED-SO-FAR.md'
REVIEW = HERE / 'REVIEW-EMULATE.json'
ANSWERS = HERE / 'ANSWERS-20261025-2300.json'
OUT = HERE / 'APPLIED-20.json'
# a link whose words the change rewrote goes back on the words the card named for it (EM-S2's note: "the link stays on
# 'article about self hypnosis'"); set_text drops a tag whose words are gone
LINK_ON = {'EM-S2': ('article about self hypnosis', 'https://www.ishhypnosis.org/encyclopedia/self-hypnosis/')}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--check', action='store_true')
    args = ap.parse_args()
    md = ARTICLE.read_text(encoding='utf-8')
    review = json.loads(REVIEW.read_text(encoding='utf-8'))
    answers = json.loads(ANSWERS.read_text(encoding='utf-8'))
    sha = hashlib.sha256(md.encode('utf-8')).hexdigest()
    assert answers['review_id'] == review['review_id'], answers['review_id']
    assert sha == review['article']['sha256'] == answers['article']['sha256'], 'the guide changed since the page was made'
    bl = sr.blocks(md)
    raw = re.split(r'\n\s*\n', md.rstrip('\n'))
    assert len(raw) == len(bl), (len(raw), len(bl))
    A = {x['id']: x for x in answers['items']}
    S = {s['id']: s for s in review['suggestions']}
    assert set(A) == set(S), (sorted(set(A) ^ set(S)))
    changed, fates, lost = {}, {}, []
    for sid, s in S.items():
        a = A[sid]
        fates[sid] = {'approved': 'approved', 'revise': 'revised (his version)', 'rejected': 'rejected'}[a['status']]
        if a['status'] == 'rejected':
            continue
        if a['status'] == 'revise':
            parts = a['your_version'].split('\n\n')
            assert len(parts) == len(s['edits']), (sid, len(parts), len(s['edits']))
            new = [p.strip() for p in parts]
        else:
            new = [e['after'] for e in s['edits']]
        for e, t in zip(s['edits'], new):
            i = e['block']
            assert bl[i]['text'] == e['before'], (sid, i)
            assert i not in changed, (sid, i)
            changed[i] = (sid, t)
    new_raw = {}
    for i, (sid, t) in changed.items():
        dropped = []
        new_raw[i] = AA.set_block_text(raw[i], t, dropped)
        if sid in LINK_ON and dropped:
            words, url = LINK_ON[sid]
            assert len(dropped) == 1 and url in dropped[0], dropped
            assert new_raw[i].count(words) == 1 and '](%s)' % url not in new_raw[i], sid
            new_raw[i] = new_raw[i].replace(words, '[%s](%s)' % (words, url), 1)
            dropped = []
        lost += dropped
        got = ''.join(x['t'] for x in sr.segments(AA.split_block(new_raw[i])[1]))
        assert got == t, (sid, i, got[:80], t[:80])
    out = [new_raw.get(i, raw[i]) for i in range(len(raw))]
    new_md = '\n\n'.join(out) + ('\n' if md.endswith('\n') else '')
    old_links = re.findall(r'\]\(([^)\s]+)\)', md)
    new_links = re.findall(r'\]\(([^)\s]+)\)', new_md)
    missing = [u for u in set(old_links) if new_links.count(u) < old_links.count(u)]
    assert not lost and not missing, (lost, missing)
    record = {
        'answers': ANSWERS.name, 'review': REVIEW.name, 'article_before_sha256': sha,
        'article_after_sha256': hashlib.sha256(new_md.encode('utf-8')).hexdigest(),
        'counts': {f: sum(1 for x in fates.values() if x == f) for f in sorted(set(fates.values()))},
        'fates': fates, 'comments': {sid: A[sid]['comment'] for sid in A if A[sid].get('comment')},
        'paragraphs': [{'block': i, 'where': sr.where(bl, i), 'by': sid, 'before': bl[i]['text'], 'after': t}
                       for i, (sid, t) in sorted(changed.items())],
    }
    print(json.dumps(record['counts']), '| paragraphs changed:', len(changed), '| links lost:', lost, '| missing:', missing)
    if args.check:
        return
    OUT.write_text(json.dumps(record, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    ARTICLE.write_text(new_md, encoding='utf-8')
    print('wrote', ARTICLE.relative_to(ROOT), 'and', OUT.relative_to(ROOT))


if __name__ == '__main__':
    main()
