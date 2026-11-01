"""Joel's answers of 2026-11-01 20:29 UTC to Hypnosis Guide Cards, 1 November (../fullread2/review/REVIEW-FR2.json; his
answers: ../fullread2/review/ANSWERS-20261101-2029.json): all four approved, as the cards showed them.
- K9: step 3 of Before you begin, "intoxicated and/or more confused than usual" becomes "intoxicated and more confused
  than usual" (the contradiction with the guide's own sessions on loveyhuasca, ../fullread2/CONTRADICTIONS.md);
- F1.6: step 6 keeps the half of his dad's line it is about, "Be prepared to take what you get. The best might come
  afterwards!" (the whole line stays in Affirmations Done Right);
- F7.5: the fingers script's last press, "you bring yourself into the clearest state of awareness yet";
- F18.1: the care workshop's "Tell your little one, ..." is cut (the line stays at the end of Finish without forcing a
  revelation).
Then read/READ-RECORD.json records the four paragraphs at their new words, read by the lead session (each is the card's
version, which I wrote and read beside his text when I made the card, and he approved as it stood).

  python3 articles/inner-signal/humanize/fix-20261101/fr2-answers/apply_answers_fr2.py [--check]
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
import compare_read as cr  # noqa: E402
import suggestion_review as sr  # noqa: E402
from apply_answers import set_block_text  # noqa: E402

GUIDE = H / 'HUMANIZED-SO-FAR.md'
REVIEW = H / 'fix-20261101' / 'fullread2' / 'review' / 'REVIEW-FR2.json'
ANSWERS = H / 'fix-20261101' / 'fullread2' / 'review' / 'ANSWERS-20261101-2029.json'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--check', action='store_true')
    a = ap.parse_args()
    md = GUIDE.read_text(encoding='utf-8')
    before_sha = hashlib.sha256(md.encode('utf-8')).hexdigest()
    review = json.loads(REVIEW.read_text(encoding='utf-8'))
    answers = json.loads(ANSWERS.read_text(encoding='utf-8'))
    assert answers['review_id'] == review['review_id']
    assert before_sha == review['article']['sha256'] == answers['article']['sha256'], before_sha[:8]
    cards = {s['id']: s for s in review['suggestions']}
    done, lost, after_texts = [], [], []
    for it in answers['items']:
        s = cards[it['id']]
        assert it['status'] == 'approved' and not it['your_version'], it['id']
        e = s['edits'][0]
        assert it['before'] == e['before'] and it['my_version'] == e['after'], it['id']
        bl = sr.blocks(md)
        hit = [b['i'] for b in bl if b['text'] == e['before']]
        assert len(hit) == 1, (it['id'], len(hit))
        i = hit[0]
        sp = s['spans'][0]
        old = e['before'][sp['start']:sp['end']]
        # the new words: the card's edit, found by what the paragraph keeps around the span
        head, tail = e['before'][:sp['start']], e['before'][sp['end']:]
        assert e['after'].startswith(head) and e['after'].endswith(tail.lstrip() if not e['after'].endswith(tail) else tail)
        new = e['after'][len(head):len(e['after']) - len(tail)] if e['after'].endswith(tail) else \
            e['after'][len(head):len(e['after']) - len(tail.lstrip())]
        if md.count(old) == 1 and (old + tail[:1]) in md:
            k = md.find(old)
            z = k + len(old)
            # a cut takes the space after it too, as the card's edit does
            if not new and md[z:z + 1] == ' ' and md[k - 1:k] == ' ':
                z += 1
            md = md[:k] + new + md[z:]
        else:
            raw = re.split(r'\n\s*\n', md.rstrip('\n'))
            raw[i] = set_block_text(raw[i], e['after'], lost)
            md = '\n\n'.join(raw) + '\n'
        now = [b['text'] for b in sr.blocks(md)]
        assert e['after'] in now, it['id']
        after_texts.append(e['after'])
        done.append({'id': it['id'], 'where': it['where'], 'old': old, 'new': new, 'at': it['updated']})
    after_sha = hashlib.sha256(md.encode('utf-8')).hexdigest()
    rec = {'answers': ANSWERS.relative_to(ROOT).as_posix(), 'review': REVIEW.relative_to(ROOT).as_posix(),
           'before_sha256': before_sha, 'after_sha256': after_sha, 'links_dropped': lost, 'applied': done}
    print(json.dumps({k: rec[k] for k in ('before_sha256', 'after_sha256', 'links_dropped')}, indent=1),
          len(done), 'cards in')
    if a.check:
        return
    GUIDE.write_text(md, encoding='utf-8')
    (HERE / 'APPLIED-FR2.json').write_text(json.dumps(rec, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    (HERE / 'read').mkdir(exist_ok=True)
    cr.record(HERE / 'read', findings=[], coverage=sorted({cr.phash(t) for t in after_texts}), dispositions={},
              article='HUMANIZED-SO-FAR.md at %s: the four paragraphs his answers of 2026-11-01 20:29 UTC changed (K9, '
                      'F1.6, F7.5, F18.1), each the card\'s version he approved as it stood, read by the lead session '
                      'beside his published version when the card was made (E294)' % after_sha[:8])


if __name__ == '__main__':
    main()
