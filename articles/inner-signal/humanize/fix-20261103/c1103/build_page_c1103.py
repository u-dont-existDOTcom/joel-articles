"""Hypnosis Guide Cards, 3 November: what the third free check of the whole guide (Joel's result pages of 2026-11-03 11:19
UTC; ../free-whole/read/WINDOWS.md) still read below High in his own words (REVIEW-C1103.json, .html, .artifact.html, .md).

No window read AI in either part. Of the five Human (Low) windows, four are ours, and their fixes are in the fourth free
check (../l1103/, ../free-whole-2/). One is his own line in Don't rush the repair, so it is a stretch to edit (advice
"edit": keep it as it is, or edit it): no suggestion of mine, so nothing for the owner-delivery gate. Every reading carries
its link (suggestion_review.py 1.5).

  python3 articles/inner-signal/humanize/fix-20261103/c1103/build_page_c1103.py
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
import build_page_r1102 as prev  # noqa: E402
import suggestion_review as sr  # noqa: E402

BLOB, LANE = prev.BLOB, prev.LANE
GIT_FILE = LANE + 'fix-20261103/c1103/REVIEW-C1103.html'
MD = (H / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
GUIDE_SHA = 'e4c620ed660c6ddf7e2f141a9b9d15dc49307e57cf954f39715a8562808d1aae'
BL = sr.blocks(MD)
FA3 = 'https://www.pangram.com/feed/4796254d-deaa-43f1-8bc9-25979960da03'
FB3 = 'https://www.pangram.com/feed/75baa67a-da78-4f74-b814-819444865b9c'
FOUND = 'The third free check of the whole guide (3 November), your result pages of 11:19 UTC'
TYPES = dict(prev.TYPES)


def block_with(s):
    hits = [b['i'] for b in BL if s in b['text']]
    assert len(hits) == 1, (s[:60], hits)
    return hits[0]


def build_cards():
    i = block_with('You don’t have to work to explain anything.')
    return [{
        'id': 'E-%d' % i, 'type': 'yours', 'title': '“You don’t have to work to explain anything.”', 'where': sr.where(BL, i),
        'advice': 'edit',
        'why': 'Your line to the little one read Human (Low) in the third free check, 9 words, with the lines around it High '
               'or Medium. Nothing else in Don’t rush the repair was flagged, and nothing in the whole guide read AI.',
        'reading': 'Human (Low), 9 words: [the third check, part A](%s)' % FA3,
        'advice_note': 'Keep it as it is, if it sounds like you: it’s a spoken line to your little one, and short lines '
                       'like this one have moved between Low and Medium from one check to the next with the same words. Or '
                       'edit it, and the next check reads it in place.',
        'keep_label': 'keep it as it is', 'found_by': FOUND,
        'spans': [{'block': i, 'start': 0, 'end': len(BL[i]['text'])}]}]


def cards_md(review):
    out = ['# %s: every card' % review['title'], '',
           'The page\'s cards as text, in the order of the guide. Built %s from [the guide so far](%s). To answer, use '
           'the page; or write your answer under a card\'s number in a message to me.' % (review['built'], review['links']['guide']), '']
    for s in review['suggestions']:
        out += ['## %s: %s (%s)' % (s['id'], s['title'], review['types'][s['type']]['label']), '', '*%s*' % s['where'], '',
                '**Pangram read:** %s' % s['reading'], '']
        for sp in s['spans']:
            out += ['> %s' % BL[sp['block']]['text'], '']
        out += ['**Why:** %s' % s['why'], '', '**My advice:** %s' % s['advice_note'], '']
    return '\n'.join(out).replace('\n\n\n', '\n\n') + '\n'


def main():
    assert hashlib.sha256(MD.encode('utf-8')).hexdigest() == GUIDE_SHA, 'the guide changed'
    S = build_cards()
    review = {
        'format': sr.FORMAT, 'review_id': 'inner-signal-hypnosis-guide-cards-20261103-c1103',
        'title': 'Hypnosis Guide Cards, 3 November',
        'intro': [
            'Your hypnosis guide as it is in Git, after the third free check of the whole guide: both parts read Human '
            'Written, with no AI window at all. Five short windows read Human (Low); four are mine, and their fixes are in '
            'the next check. This <b>one card</b> is the fifth, in your own words. It links the check.',
            'Your answer saves as you click. When you\'re done, click <b>Copy my answers</b> (or <b>Save them as a file</b>) and '
            'send them to me.'],
        'git_file': GIT_FILE, 'article': {'file': LANE + 'HUMANIZED-SO-FAR.md', 'sha256': GUIDE_SHA},
        'links': {'guide': BLOB + LANE + 'HUMANIZED-SO-FAR.md', 'review': BLOB + LANE + 'fix-20261103/c1103/REVIEW-C1103.md'},
        'built': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M UTC'),
        'types': TYPES, 'suggestions': S,
    }
    probs = sr.check(review, BL)
    for p in probs:
        print('PROBLEM', p)
    (HERE / 'REVIEW-C1103.json').write_text(json.dumps(review, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    if probs:
        sys.exit(1)
    page = sr.page(review, MD, BL)
    (HERE / 'REVIEW-C1103.html').write_text(page, encoding='utf-8')
    (HERE / 'REVIEW-C1103.artifact.html').write_text(sr.artifact_view(page), encoding='utf-8')
    (HERE / 'REVIEW-C1103.md').write_text(cards_md(review), encoding='utf-8')
    print(len(S), 'card:', S[0]['id'], S[0]['where'])


if __name__ == '__main__':
    main()
