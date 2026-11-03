"""The hypnosis guide's cards of 2 November (2): the changes to his words that the w1102 windows round found, each checked in
Pangram in its section and in the whole guide before it reaches him (REVIEW-W1102.json, .html, .artifact.html, .md).

Joel, 2026-11-02 19:11 UTC: "but you're saying we still ahve to fix some stretches" and "28a". The round's fixes and their
checks: fixes_w1102.py, batch w1102f (RESULTS.md), APPLIED-W1102F.json. Two cards put his inner child guide's lines back as
he wrote them where this guide had shortened them (E314); one is a change to his own quote of 2 November (W-685), through
the owner-delivery gate first (gate/G-672). His inner child guide's line in Inner child love read AI (High) here, so it is
not offered (C-626). Every reading and every check carries its link (suggestion_review.py 1.5 refuses a card without).

  python3 articles/inner-signal/humanize/fix-20261102/w1102fix/build_page_w1102.py [--without C-672]
"""
import argparse
import collections
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
sys.path.insert(0, str(F / 'review'))
sys.path.insert(0, str(HERE))
import build_page_r1102 as prev  # noqa: E402
import fixes_w1102 as fx  # noqa: E402
import suggestion_review as sr  # noqa: E402

BLOB = prev.BLOB
LANE = prev.LANE
ARTICLE = LANE + 'HUMANIZED-SO-FAR.md'
GIT_FILE = LANE + 'fix-20261102/w1102fix/REVIEW-W1102.html'
MD = (H / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
BL = sr.blocks(MD)
L = 'https://www.pangram.com/history/'


def res(path, key):
    r = json.loads((F / path / 'RESULTS.json').read_text(encoding='utf-8'))[key]
    assert r['link'].startswith(L), key
    return r['link']


WA, WB = res('whole', 'w1102-A'), res('whole', 'w1102-B')
S23, S55, S84 = res('w1102fix', 'w1102f-23'), res('w1102fix', 'w1102f-55'), res('w1102fix', 'w1102f-84')
FA, FB = res('w1102fix', 'w1102f-A'), res('w1102fix', 'w1102f-B')
EDIT = {e[0]: e for e in fx.EDITS}


def block_with(s):
    hits = [b['i'] for b in BL if s in b['text']]
    assert len(hits) == 1, (s[:60], hits)
    return hits[0]


def card(cid, typ, title, old, new, what, why, stays, note, found, reading, tested):
    i = block_with(old)
    prev.BL = BL
    s = prev.card(cid, typ, title, [(i, old, new)], what, why, stays, note, found, reading, tested)
    s['where'] = sr.where(BL, i)
    return s


def build_cards(without=()):
    S = []
    e = EDIT['C-141']
    S.append(card(
        'C-141', 'icguide', '“I see you. I\'m not going to force my way past you.”', e[3], e[4],
        'Your inner child guide’s lines go back in as you wrote them: “You can tell that part something like, … Or however '
        'you’d actually say that. … If nothing comes, that’s fine for now. No need to answer for that part just because '
        'you’d set this up as a healing session.”',
        'When they came into this guide they were shortened and reworded (“Talk to the guard the way your Nurturer talks to '
        'your inner child:”, “If nothing comes back, that’s okay, you don’t need to push for an answer.”), and in the whole '
        'guide those lines read AI (Low) and Human (Low). I also took out a sentence of mine just before them (“So before '
        'you decide where it’s coming from, ask it. What is it trying to stop? What does it want from you?”), which read AI '
        'in the whole and asked what your lines ask.',
        'Everything else in the section, and “Later on, you can ask it…” right after your lines.',
        'Approve: it’s your own wording, and in place it reads Human in its section and in the whole.',
        'The whole-guide check in two halves (2 November), round w1102f',
        'AI (Low), 26 words, on “Talk to the guard … force my way past you.”, and Human (Low) on the two lines after it: '
        '[the whole guide’s first half](%s)' % WA,
        'The section with your lines: Human Written, 0%% AI: [check](%s). The whole first half with them: none of these '
        'lines flagged: [check](%s)' % (S23, FA)))
    e = EDIT['C-384']
    S.append(card(
        'C-384', 'icguide', '“… that one can sting …”', e[3], e[4],
        'Your inner child guide’s lines go back as you wrote them (“that one can sting”, “that part remembers”), with your '
        'sentence that says why the question works: “It puts you into the role of the Nurturer, which alleviates the '
        'instinct to argue back.”',
        'They were shortened when they came in, and your reason was left out. That stretch read Human (Low) in the whole '
        'guide, and with your lines it still does, so this card is about your words and your reason, not a better reading. '
        'In its section, it reads Human Written, 0% AI.',
        'The three questions before it, and the rest of It feels fake.',
        'Approve: the reader gets your reason for asking, in your words, and the reading is no worse.',
        'The whole-guide check in two halves (2 November), round w1102f',
        'Human (Low), 38 words: [the whole guide’s second half](%s)' % WB,
        'The section with your lines: Human Written, 0%% AI: [check](%s). The whole second half: Human (Low), 36 words, as '
        'before: [check](%s)' % (S55, FB)))
    if 'C-672' not in without:
        e = EDIT['C-672']
        S.append(card(
            'C-672', 'yours', '“But I’m also not going to build our whole life around this wound forever.”', e[3], e[4],
            'The second half of your quote becomes “We’re not moving into this wound for good, either.”',
            'Your quote (W-685) read Human (High) for you by itself, but in the whole guide it read AI (High) and AI (Low). '
            'The pattern is the matched pair: “I’m not going to … But I’m also not going to …”. This keeps your point, '
            'that the hurt doesn’t get to run your whole life, with a picture in place of the second “not going to”.',
            'The first half of your quote, word for word, and the rest of the section.',
            'Approve if the picture sounds like you: with it, the section reads Human Written, 0% AI, and the whole half no '
            'longer flags your quote. Reject keeps your line, which reads Human by itself.',
            'The whole-guide check in two halves (2 November), round w1102f',
            'AI (High), 32 words, and AI (Low), 32 words: [the whole guide’s second half](%s)' % WB,
            'The section with the change: Human Written, 0%% AI: [check](%s). The whole second half with it: your quote not '
            'flagged: [check](%s)' % (S84, FB)))
    return S


def build(without=()):
    S = build_cards(without)
    S.sort(key=lambda s: (s['spans'][0]['block'], s['spans'][0]['start']))
    n = collections.Counter(s['type'] for s in S)
    review = {
        'format': sr.FORMAT, 'review_id': 'inner-signal-hypnosis-guide-cards-20261102-w1102',
        'title': 'Hypnosis Guide Cards, 2 November (2)',
        'intro': [
            'Your hypnosis guide as it is in Git, after this round’s fixes of the stretches that still read AI or Human (Low) '
            'when the whole guide was checked. These <b>%d cards</b> are the changes that touch your words. Every '
            'suggestion was checked in Pangram in its section and in the whole guide before it reached you, and each card '
            'links each check.' % len(S),
            'Your answers save as you click. When you’re done, click <b>Copy my answers</b> (or <b>Save them as a '
            'file</b>) and send them to me.',
        ],
        'git_file': GIT_FILE, 'article': {'file': ARTICLE, 'sha256': hashlib.sha256(MD.encode('utf-8')).hexdigest()},
        'links': {'guide': BLOB + ARTICLE, 'review': BLOB + LANE + 'fix-20261102/w1102fix/REVIEW-W1102.md'},
        'built': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M UTC'),
        'types': prev.TYPES, 'suggestions': S,
    }
    return review, n


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--without', nargs='*', default=[])
    a = ap.parse_args()
    review, n = build(a.without)
    probs = sr.check(review, BL)
    for p in probs:
        print('PROBLEM', p)
    (HERE / 'REVIEW-W1102.json').write_text(json.dumps(review, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    if probs:
        sys.exit(1)
    prev.BL = BL
    page = sr.page(review, MD, BL)
    (HERE / 'REVIEW-W1102.html').write_text(page, encoding='utf-8')
    (HERE / 'REVIEW-W1102.artifact.html').write_text(sr.artifact_view(page), encoding='utf-8')
    (HERE / 'REVIEW-W1102.md').write_text(prev.cards_md(review), encoding='utf-8')
    print(len(review['suggestions']), 'cards:', dict(n))


if __name__ == '__main__':
    main()
