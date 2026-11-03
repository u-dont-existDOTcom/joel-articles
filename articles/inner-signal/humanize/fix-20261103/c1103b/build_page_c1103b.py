"""Hypnosis Guide Cards, 3 November (2): what the fourth free check of the whole guide (Joel's result pages of 2026-11-03
12:18 UTC; ../free-whole-2/read/WINDOWS.md) still read below High that a fix of mine couldn't clear (REVIEW-C1103B.json,
.html, .artifact.html, .md).

No window read AI. Two read Human (Low): his own line in Don't rush the repair, which he rewrote in the same message (his
E-157, in the guide now), and Pattern 10's questions, ours, after two tries (F-528 on 2 November, F-522 and F-523 today,
which read lower and stay out, ../l1103/apply_l1103.py). So Pattern 10 is a stretch to edit (advice "edit": keep it as it
is, or edit it), with no suggestion of mine on it, so nothing for the owner-delivery gate.

  python3 articles/inner-signal/humanize/fix-20261103/c1103b/build_page_c1103b.py
"""
import datetime
import hashlib
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
F = HERE.parent
H = F.parent
ROOT = H.parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
sys.path.insert(0, str(H / 'fix-20261102' / 'review'))
sys.path.insert(0, str(F / 'c1103'))
import build_page_r1102 as prev  # noqa: E402
import build_page_c1103 as first  # noqa: E402
import suggestion_review as sr  # noqa: E402

BLOB, LANE = prev.BLOB, prev.LANE
GIT_FILE = LANE + 'fix-20261103/c1103b/REVIEW-C1103B.html'
MD = (H / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
GUIDE_SHA = '94ffd381f8a15b8a2116c220403c114211553db31379790532c0971658f3e1ec'
BL = sr.blocks(MD)
FB3, FB4 = first.FB3, 'https://www.pangram.com/feed/93dac4dd-cdea-49f2-8103-83211c1ebb4d'
FOUND = 'The third and fourth free checks of the whole guide (3 November), your result pages of 11:19 and 12:18 UTC'
TYPES = dict(prev.TYPES)
TYPES['stuck'] = {'label': 'Our words, still below High', 'about': 'Words of ours that read Human (Low) in the whole guide '
                  'after two tries. Keep it as it is (the clear version stays in), or Edit it: your own versions have read '
                  'Human.'}


def block_with(s):
    hits = [b['i'] for b in BL if s in b['text']]
    assert len(hits) == 1, (s[:60], hits)
    return hits[0]


def build_cards():
    i = block_with('You need both to be ethical with people, so when something sounds true but vague, ask:')
    assert BL[i - 1]['text'].startswith('Milton Model language opens things up')
    return [{
        'id': 'E-%d' % i, 'type': 'stuck', 'title': '“You need both to be ethical with people, so when something sounds true but vague, ask …”',
        'where': sr.where(BL, i), 'advice': 'edit',
        'why': 'Pattern 10’s six questions read Human (Low) in both of today’s checks. In the third, with this lead-in (as it is '
               'now). In the fourth, with my second try: the ethics point moved up to lead the two models, and the questions on '
               'their own after a plain “When something sounds true but vague, ask:”. That read lower (21 words), so this '
               'version stays. Nothing else in Pattern 10 or around it was flagged.',
        'reading': 'Human (Low), 37 words: [the third check, part B](%s); with my second try, Human (Low), 21 words: '
                   '[the fourth check, part B](%s)' % (FB3, FB4),
        'advice_note': 'Keep it as it is: they’re the Meta Model’s own questions, and with both lead-ins I tried, the run of '
                       'six questions read Low in the whole guide. Or edit it, if you’d put the questions another way; the '
                       'next check reads it in place.',
        'keep_label': 'keep it as it is', 'found_by': FOUND,
        'spans': [{'block': i - 1, 'start': 0, 'end': len(BL[i - 1]['text'])}, {'block': i, 'start': 0, 'end': len(BL[i]['text'])}]}]


def main():
    assert hashlib.sha256(MD.encode('utf-8')).hexdigest() == GUIDE_SHA, 'the guide changed'
    S = build_cards()
    review = {
        'format': sr.FORMAT, 'review_id': 'inner-signal-hypnosis-guide-cards-20261103-c1103b',
        'title': 'Hypnosis Guide Cards, 3 November (2)',
        'intro': [
            'Your hypnosis guide as it is in Git, after the fourth free check of the whole guide: both parts read Human '
            'Written, with no AI window. Your new line in Don’t rush the repair is in. This <b>one card</b> is the only '
            'stretch of mine still below High after two tries. It links both checks.',
            'Your answer saves as you click. When you\'re done, click <b>Copy my answers</b> (or <b>Save them as a file</b>) and '
            'send them to me.'],
        'git_file': GIT_FILE, 'article': {'file': LANE + 'HUMANIZED-SO-FAR.md', 'sha256': GUIDE_SHA},
        'links': {'guide': BLOB + LANE + 'HUMANIZED-SO-FAR.md', 'review': BLOB + LANE + 'fix-20261103/c1103b/REVIEW-C1103B.md'},
        'built': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M UTC'),
        'types': TYPES, 'suggestions': S,
    }
    probs = sr.check(review, BL)
    for p in probs:
        print('PROBLEM', p)
    (HERE / 'REVIEW-C1103B.json').write_text(json.dumps(review, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    if probs:
        sys.exit(1)
    page = sr.page(review, MD, BL)
    (HERE / 'REVIEW-C1103B.html').write_text(page, encoding='utf-8')
    (HERE / 'REVIEW-C1103B.artifact.html').write_text(sr.artifact_view(page), encoding='utf-8')
    first.BL = BL
    (HERE / 'REVIEW-C1103B.md').write_text(first.cards_md(review), encoding='utf-8')
    print(len(S), 'card:', S[0]['id'], S[0]['where'])


if __name__ == '__main__':
    main()
