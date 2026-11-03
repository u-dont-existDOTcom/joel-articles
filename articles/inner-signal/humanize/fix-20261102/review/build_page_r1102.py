"""The hypnosis guide's cards of 2 November: the three changes to his words that batch r1102 and the redundancy read found,
each checked in Pangram before it reaches him (REVIEW-R1102.json, .html, .artifact.html, .md).

His notes on the cards of 1 November set the rules for this page (ANSWERS-20261102-1643.json): every Pangram reading
carries its link ("why are you not giving me the pangram link so i can see? always give me the links"), every suggestion
was checked first and carries its own link ("you didn't check if your changes passed.. they didn't. don't waste my
time"), the advice gives its reason ("\\"I'd approve\\" is not a reason for suggesting to approve lol"), and repeats are
cut ("let's see what other redundancy remains in this article and cut that also"). suggestion_review.py 1.5 refuses a
card whose reading has no link, or whose suggestion has no Pangram check of its own.

  python3 articles/inner-signal/humanize/fix-20261102/review/build_page_r1102.py
"""
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
import suggestion_review as sr  # noqa: E402

BLOB = 'https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/community-joel-1018/'
LANE = 'articles/inner-signal/humanize/'
ARTICLE = LANE + 'HUMANIZED-SO-FAR.md'
GIT_FILE = LANE + 'fix-20261102/review/REVIEW-R1102.html'
MD = (H / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
BL = sr.blocks(MD)
L = 'https://www.pangram.com/history/'


def res(path, key):
    """A check's public link from its RESULTS.json."""
    r = json.loads((F / path / 'RESULTS.json').read_text(encoding='utf-8'))[key]
    assert r['link'].startswith(L), key
    return r['link']


R15, R40 = res('recheck', 'r1102-15'), res('recheck', 'r1102-40')
A1, B0, B3 = res('recheck/round2', 'r1102b-A1'), res('recheck/round2', 'r1102b-B0'), res('recheck/round2', 'r1102b-B3')
B4 = res('recheck/round2/r3', 'r1102b-B4')
B5, B6 = res('recheck/round2/r4', 'r1102b-B5'), res('recheck/round2/r4', 'r1102b-B6')
E1 = res('recheck/round2/r5', 'r1102b-E1')

TYPES = {
    'yours': {'label': 'Your own words',
              'about': 'A paragraph you wrote or rewrote. Approve uses the suggestion; Reject keeps your words; Revise '
                       'lets you write your own.'},
    'icguide': {'label': 'From your inner child guide',
                'about': 'Your inner child guide\'s words in this guide. Approve uses the suggestion; Reject keeps them; '
                         'Revise lets you write your own.'},
    'repeat': {'label': 'Said twice',
               'about': 'A passage that says what another part of the guide already says (your note on W-685). Approve '
                        'cuts it; Reject keeps it; Revise lets you write your own.'},
}
DECIDE = 'Approve uses the suggestion; Reject keeps your words; Revise lets you write your own.'


def block_with(s):
    hits = [b['i'] for b in BL if s in b['text']]
    assert len(hits) == 1, (s[:60], hits)
    return hits[0]


def card(cid, typ, title, changes, what, why, stays, note, found, reading, tested):
    spans, edits = [], {}
    for i, old, new in changes:
        assert BL[i]['text'].count(old) == 1, (cid, old[:60])
        k = BL[i]['text'].find(old)
        spans.append({'block': i, 'start': k, 'end': k + len(old.rstrip())})
        t = edits[i]['after'] if i in edits else BL[i]['text']
        after = '' if (old == BL[i]['text'] and not new) else t.replace(old, new).strip()
        edits[i] = {'block': i, 'before': BL[i]['text'], 'after': after}
    s = {'id': cid, 'type': typ, 'title': title, 'where': sr.where(BL, changes[0][0]), 'spans': spans,
         'edits': [edits[i] for i in sorted(edits)], 'inserts': [], 'moves': [], 'what': what, 'why': why,
         'stays': stays, 'advice': 'approve', 'advice_note': note, 'found_by': found, 'deciding': DECIDE,
         'tested': tested}
    if reading:
        s['reading'] = reading
    return s


def build_cards():
    S = []
    rent = 'That’s one grown-up doing three jobs, not three more people moving in to help with the rent, and each job ' \
           'keeps the others in balance.'
    party = (' Say a party gets to be too much for your little one. The Protector gets you both out of there, and on the '
             'way home the Nurturer tells them they did great, even though mostly they hid in the bathroom. And the Guide '
             'helps them think twice about the next weird party they might go to, avoiding another cycle of bathroom '
             'vacationing. 🙈')
    i = block_with(rent)
    S.append(card(
        'W-92b', 'icguide', '“… not three more people moving in to help with the rent …”', [(i, rent, rent + party)],
        'Your inner child guide’s party example goes in right after the rent line, word for word, the way it follows '
        'that line in your inner child guide.',
        'The rent line (your inner child guide’s, which you approved on W-92) read AI (High) when the section was checked '
        'by itself. In your inner child guide the line goes on to the party example, which shows the three jobs working '
        'together; with it, the two paragraphs read 100% Human.',
        'Everything else in the paragraph, word for word.',
        'Approve: with your example after it, the line reads Human, and the reader sees the three jobs in action '
        'instead of only their names.',
        'Batch r1102: each section your answers changed, checked by itself (2 November)',
        'AI (High), 27 words, on the rent line: [the section’s check](%s)' % R15,
        'Human Written, 100%% Human, every window High: [the two paragraphs with your example](%s)' % A1))
    say = ' Say something like,'
    j = block_with('That hand movement is the mental escape into the body\'s flow.' + say)
    k = block_with('Starting with your eyes open, press your thumb to your forefinger')
    assert k == j + 1
    S.append(card(
        'W-283b', 'repeat', 'The script after “Say something like,”', [(j, say, ''), (k, BL[k]['text'], '')],
        'The script goes, and your paragraph above it ends at “That hand movement is the mental escape into the body’s '
        'flow.”',
        'The script (your W-283, approved; you checked it Human by itself) read AI (High) twice when Stay awake and Make '
        'the hypnosis more alert were checked as their section, and pulled your rewrite above it to AI (Low) in five '
        'places. Your paragraph already says each step of it: eyes open, a small hand movement with each suggestion of '
        'clarity, then stop the movement and see where your mind is at. Two rewrites of the script read AI too '
        '([one](%s), [two](%s)), so the script is the part to go, not your words.' % (B3, B4),
        'Every word of yours above it.',
        'Approve: every step is still in your paragraph, and without the script your whole passage from “Once you’ve got '
        'your bearings” reads Human. If you want a script to read aloud, Revise and write it your way.',
        'Batch r1102 (2 November), and the redundancy read your note on W-685 asked for',
        'AI Detected, 50%%: the script AI (High) twice, your rewrite AI (Low): [the section’s check](%s). Your passage '
        'from “Once you’ve got your bearings” with the script: AI Detected, 26%%: [check](%s)' % (R40, B0),
        'Without the script: your paragraph and its heading, 100%% Human, every window High: [check](%s). Your passage '
        'from “Once you’ve got your bearings”: Human Written: [check](%s)' % (B5, B6)))
    prayer = (' Simply say to yourself, “Dear subconscious, thank you for showing me images. If what you are showing me is '
              'helpful, then please also show me the guidance in it. If what you are showing me is a way of avoiding '
              'dealing with life, then please show me in a gentle but structured way how to deal with life as it is right '
              'now.”')
    m = block_with(prayer.strip())
    S.append(card(
        'R-638', 'repeat', 'Appendix E’s prayer to the subconscious', [(m, prayer, '')],
        'The prayer in Appendix E goes; “ask your subconscious to help you” stays, so the paragraph still says to ask.',
        'It asks what your prayer in Stay awake when your mind likes to escape asks (your rewrite, W-282): if it’s '
        'guidance, show me what to do with it; if I’m avoiding something, bring me back. The guide says it once that way.',
        'The rest of Appendix E, word for word.',
        'Approve: the guide says it once, in your newer words, and Appendix E still tells the reader to sit up, open '
        'their eyes, feel their feet and ask.',
        'The redundancy read of 2 November (your note on W-685)', None,
        'Human Written, 100%% Human, every window High: [Appendix E’s four paragraphs without the prayer](%s)' % E1))
    return S


def build():
    S = build_cards()
    S.sort(key=lambda s: (s['spans'][0]['block'], s['spans'][0]['start']))
    n = collections.Counter(s['type'] for s in S)
    review = {
        'format': sr.FORMAT, 'review_id': 'inner-signal-hypnosis-guide-cards-20261102-r1102',
        'title': 'Hypnosis Guide Cards, 2 November',
        'intro': [
            'Your hypnosis guide as it is in Git, with your answers of today in. Each section they changed was checked '
            'by itself in Pangram: 19 of 22 read Human Written. These <b>%d cards</b> are the changes to your words that '
            'checking found, and the repeats you asked me to look for. Every suggestion here was checked in Pangram '
            'before it reached you, and each card links each check.' % len(S),
            'Your answers save as you click. When you’re done, click <b>Copy my answers</b> (or <b>Save them as a '
            'file</b>) and send them to me.',
        ],
        'git_file': GIT_FILE, 'article': {'file': ARTICLE, 'sha256': hashlib.sha256(MD.encode('utf-8')).hexdigest()},
        'links': {'guide': BLOB + ARTICLE, 'review': BLOB + LANE + 'fix-20261102/review/REVIEW-R1102.md'},
        'built': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M UTC'),
        'types': TYPES, 'suggestions': S,
    }
    return review, n


def marked(j, spans):
    t = BL[j]['text']
    for sp in sorted((x for x in spans if x['block'] == j), key=lambda x: -x['start']):
        t = t[:sp['start']] + '**' + t[sp['start']:sp['end']] + '**' + t[sp['end']:]
    return t


def cards_md(review):
    types = review['types']
    out = ['# %s: every card' % review['title'], '',
           'The page\'s cards as text, in the order of the guide. Built %s from [the guide so far](%s). To answer, use '
           'the page; or write your answer under a card\'s number in a message to me.' % (
               review['built'], review['links']['guide']), '']
    for s in review['suggestions']:
        out += ['## %s: %s (%s)' % (s['id'], s['title'], types[s['type']]['label']), '', '*%s*' % s['where'], '']
        if s.get('reading'):
            out += ['**Pangram read:** %s' % s['reading'], '']
        out += ['**Pangram on the suggestion:** %s' % s['tested'], '']
        for e in s['edits']:
            out += ['**Now** (the words it changes in bold):', '', '> %s' % marked(e['block'], s['spans']), '']
            out += (['**How it would read:**', '', '> %s' % e['after'], ''] if e['after'] else
                    ['**How it would read:** this paragraph goes.', ''])
        out += ['**Why:** %s' % s['why'], '', '**My advice:** %s' % s['advice_note'], '']
    return '\n'.join(out).replace('\n\n\n', '\n\n') + '\n'


def main():
    review, n = build()
    probs = sr.check(review, BL)
    for p in probs:
        print('PROBLEM', p)
    (HERE / 'REVIEW-R1102.json').write_text(json.dumps(review, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    if probs:
        sys.exit(1)
    page = sr.page(review, MD, BL)
    (HERE / 'REVIEW-R1102.html').write_text(page, encoding='utf-8')
    (HERE / 'REVIEW-R1102.artifact.html').write_text(sr.artifact_view(page), encoding='utf-8')
    (HERE / 'REVIEW-R1102.md').write_text(cards_md(review), encoding='utf-8')
    print(len(review['suggestions']), 'cards:', dict(n))


if __name__ == '__main__':
    main()
