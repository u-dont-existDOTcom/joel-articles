"""Put Joel's answers to the fix page (question 24, REVIEW-28) into the hypnosis guide, with every card's fate recorded.

  python3 articles/inner-signal/humanize/fix-20261028/comprehension/apply_answers_28.py ANSWERS.json [--take-advice] [--check]

ANSWERS.json is the page's export ("Copy my answers" or "Save them as a file"), saved word for word in this folder. A
fix card he approved goes in as the card shows it (every fix of its paragraph, from fix/KEPT.json, links kept on their
words); one he revised goes in as his version of the paragraph, word for word (obvious typos only, by hand, recorded);
one he rejected stays out. A card in his own words (advice "edit"): Keep changes nothing, his version replaces the
paragraph. An item may carry "fate" (what to record, e.g. for answers built from his message) and "also" (the same
replacement in another paragraph, on top of that paragraph's own card). A card he left unmarked follows my advice only with --take-advice, when he has said to. Writes
HUMANIZED-SO-FAR.md and APPLIED-28.json; then every paragraph whose words changed and aren't his needs a read beside his
published version before the push (make_verify.py, collect_verify.py, write_records.py; the comparison gate checks it).
"""
import argparse
import hashlib
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parents[1]
ROOT = H.parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
sys.path.insert(0, str(H / 'fix-20261025' / 'review'))
import suggestion_review as sr  # noqa: E402
from apply_answers import set_block_text  # noqa: E402

GUIDE = H / 'HUMANIZED-SO-FAR.md'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('answers')
    ap.add_argument('--take-advice', action='store_true', help='he said to take my advice on the cards he left unmarked')
    ap.add_argument('--check', action='store_true', help='report only')
    a = ap.parse_args()
    review = json.loads((HERE / 'REVIEW-28.json').read_text(encoding='utf-8'))
    answers = json.loads(pathlib.Path(a.answers).read_text(encoding='utf-8'))
    md = GUIDE.read_text(encoding='utf-8')
    sha = hashlib.sha256(md.encode('utf-8')).hexdigest()
    assert sha == review['article']['sha256'], 'the guide changed since the fix page was made'
    assert answers.get('review_id') == review['review_id'], 'these answers are for another page'
    bl = sr.blocks(md)
    raw = re.split(r'\n\s*\n', md.rstrip('\n'))
    assert len(raw) == len(bl)
    kept = json.loads((HERE / 'fix' / 'KEPT.json').read_text(encoding='utf-8'))['fixes']
    A = {x['id']: x for x in answers['items']}
    new_raw, fates, lost, cur = {}, {}, [], {}
    # the cards in his own words first: where one shares its paragraph with a fix card (C-91 and C-92 on 2026-10-29),
    # the fix's words go in on top of his version (or my advised wording) instead of the fix card overwriting it
    for s in sorted(review['suggestions'], key=lambda s: s['advice'] != 'edit'):
        x = A.get(s['id'], {'status': 'pending'})
        st = x['status']
        i = s['spans'][0]['block']
        if st == 'pending' and a.take_advice and s['advice'] == 'approve':
            st = 'approved'
            fates[s['id']] = 'accepted (unmarked, my advice approve)'
        if s['advice'] == 'edit':
            if st == 'revise' and x.get('your_version', '').strip():
                cur[i] = x['your_version'].strip()
                new_raw[i] = [set_block_text(raw[i], cur[i], lost)]
                fates[s['id']] = x.get('fate') or 'his version'
            else:
                fates.setdefault(s['id'], 'kept as it is' if st in ('rejected', 'approved') else 'not marked')
            continue
        if st == 'approved':
            after = s['edits'][0]['after']
            if '\n\n' in after:     # a list given back its line breaks: a lead-in line and "- " items
                assert i not in cur, (s['id'], 'a list card shares its paragraph with another answer')
                new_raw[i] = [ln.strip() for ln in after.split('\n\n') if ln.strip()]
            else:
                text = bl[i]['text']
                for fx in [f for f in kept if f['block'] == i]:
                    text = text.replace(fx['replace'], fx['with'])
                assert text == after, (s['id'], 'the card and KEPT.json disagree')
                if i in cur:
                    after = cur[i]
                    for fx in [f for f in kept if f['block'] == i]:
                        assert after.count(fx['replace']) == 1, (s['id'], 'the fix no longer fits the answer before it')
                        after = after.replace(fx['replace'], fx['with'])
                cur[i] = after
                new_raw[i] = [set_block_text(raw[i], after, lost)]
            fates.setdefault(s['id'], x.get('fate') or 'approved')
        elif st == 'revise' and x.get('your_version', '').strip():
            assert i not in cur, (s['id'], 'his version of a fix card shares its paragraph with another answer')
            cur[i] = x['your_version'].strip()
            new_raw[i] = [set_block_text(raw[i], cur[i], lost)]
            fates[s['id']] = 'his version'
        else:
            fates[s['id']] = {'rejected': 'rejected', 'pending': 'not marked'}.get(st, st)
    # an answer that goes for another paragraph too ("also": the same words where the same line stands elsewhere, as
    # C-59's note said of Working with your guards, P6), on top of whatever that paragraph's own card did
    for s in review['suggestions']:
        for al in A.get(s['id'], {}).get('also', []):
            j = al['block']
            cur = new_raw.get(j, [raw[j]])
            assert len(cur) == 1, (s['id'], j)
            cur_text = sr.blocks(cur[0])[0]['text']
            assert cur_text.count(al['replace']) == 1, (s['id'], j, al['replace'])
            new_raw[j] = [set_block_text(cur[0], cur_text.replace(al['replace'], al['with']), lost)]
            fates[s['id']] = fates.get(s['id'], '') + '; the same words in %s' % al.get('where', 'block %d' % j)
    out = []
    for j, r in enumerate(raw):
        out += new_raw.get(j, [r])
    new = '\n\n'.join(out) + '\n'
    rec = {'answers': str(a.answers), 'take_advice': a.take_advice, 'before_sha256': sha,
           'after_sha256': hashlib.sha256(new.encode('utf-8')).hexdigest(), 'fates': fates, 'links_dropped': lost,
           'changed_blocks': sorted(new_raw)}
    print(json.dumps({k: v for k, v in rec.items() if k != 'fates'}, indent=1))
    from collections import Counter
    print(Counter(fates.values()))
    if not a.check:
        GUIDE.write_text(new, encoding='utf-8')
        (HERE / 'APPLIED-28.json').write_text(json.dumps(rec, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')


if __name__ == '__main__':
    main()
