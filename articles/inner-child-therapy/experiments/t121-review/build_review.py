#!/usr/bin/env python3
"""Turn 121: the marking page for round 9's windows below High (Joel, 2026-11-04 12:02 UTC: "yes i do want to work on the low
windows especially, medium ones i can look at altho i might not bother changing"; experiments/t121-answers/).

Round 9 read his reorganized guide whole, in two halves (experiments/t120-results/: SPOTS.json, 26 windows that aren't
High-confidence Human). Eight of them are in one section, Hearthwork: Taking Turns: both Low windows, the one AI window
(before his aside went back this turn) and five Medium ones. That section was checked alone this turn (experiments/
t121-check/: the section, then each paragraph, E343), so its three paragraphs come first, each a stretch for him to edit
with both readings and what I'd look at. The other 18 windows, all Human at Medium, follow in the guide's order, each a
stretch to look at, my advice to leave the short ones. No card puts words of mine into his text, so nothing here needs the
owner-delivery gate; cards are "edit" stretches (Keep it as it is / Edit it), built with tools/humanization/
suggestion_review.py on GUIDE-PAGE.md (make_page_copy.py, the article with only its bold marks and list breaks changed for
the page). Writes REVIEW.json, then REVIEW.html and REVIEW-artifact.html through suggestion_review.py page, and
REVIEW-CARDS.md, the cards as a page GitHub shows.

  python3 articles/inner-child-therapy/experiments/t121-review/build_review.py"""
import datetime
import hashlib
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import suggestion_review as sr  # noqa: E402

ARTICLE = 'articles/inner-child-therapy/experiments/t121-review/GUIDE-PAGE.md'
BRANCH = 'handoff/claude-dangerous-adult-20260924-1631'
BLOB = 'https://github.com/u-dont-existDOTcom/joel-articles/blob/%s/articles/inner-child-therapy/' % BRANCH
MD = (ROOT / ARTICLE).read_text(encoding='utf-8')
BL = sr.blocks(MD)
SPOTS = json.loads((HERE.parent / 't120-results' / 'SPOTS.json').read_text(encoding='utf-8'))
FEED = {'A': 'https://www.pangram.com/feed/a3f14949-326d-492a-b65a-8b048ca74940',
        'B': 'https://www.pangram.com/feed/f3b33647-484f-4203-9709-db0b04ab8f2d'}
ROUND8_B = 'https://www.pangram.com/feed/bd483bd6-edab-4f39-834c-3d959b0abb72'
CHECK = {'section': 'https://www.pangram.com/history/f2d397ae-6c78-4c5c-a855-341ce23285ef',
         'p1': 'https://www.pangram.com/history/8668b6dc-7991-41fc-ba98-e361470ba1f5',
         'p2': 'https://www.pangram.com/history/197fd1b3-519e-47b9-b6ed-54457f4e5a86',
         'p3': 'https://www.pangram.com/history/1468591d-d54f-4d7a-9d8e-5b2a87027305'}
HW = 'Hearthwork: Taking Turns'
TYPES = {
    'low': {'label': 'Read AI or Low', 'about': 'Where Pangram read AI, or Human at Low confidence: the windows a next Pangram version is likeliest to call AI. All of them are in Hearthwork: Taking Turns.'},
    'medium': {'label': 'Read Human at Medium', 'about': 'Human, but not at High confidence. For you to look at; I\'d leave most of them.'},
}
S = []


def span(quote, near=None):
    """The span of QUOTE in the page copy: the longest of its lines that the page finds (a window can run across two
    paragraphs, and a span sits in one block)."""
    best = None
    for part in sorted((p.strip() for p in quote.split('\n') if p.strip()), key=len, reverse=True):
        try:
            best = sr.find_quote(BL, part, near)
            break
        except ValueError:
            continue
    if best is None:
        raise SystemExit('not on the page: %r' % quote[:100])
    b, s, e = best
    return {'block': b, 'start': s, 'end': e}


def heading_block(path):
    """The block index of the last heading in PATH (the headings above a window), found under the one before it: the
    nearest place for a quote the article holds more than once (\"I love you.\")."""
    plain = lambda t: sr.norm_map(t)[0].strip()
    hs = [b for b in BL if b['level'] and plain(b['text']) == plain(path[-1])]
    if len(hs) > 1 and len(path) > 1:
        hs = [b for b in hs if plain(path[-2]) in [plain(x) for x in b['path']]] or hs
    return hs[0]['i'] if hs else None


def para_span(start_words):
    b, s, e = sr.find_quote(BL, start_words)
    return {'block': b, 'start': 0, 'end': len(sr.block_text(BL, b))}


def hearthwork_cards():
    p1 = para_span('The basic premise of Hearthwork, my peer-counseling framework')
    p2 = para_span('Some of what the three grown-up jobs do can come from outside you, too.')
    p3 = para_span('The peer doesn\'t become your permanent parent, though.')
    S.append({
        'id': 'HW-1', 'type': 'low', 'advice': 'edit', 'title': 'Hearthwork\'s premise, as a list',
        'spans': [p1],
        'why': ('In the whole guide, this paragraph holds round 9\'s Low window, "You speak. I listen. Then we switch.", with '
                'Medium windows on either side of it. Alone, it reads AI (81%). Its list is Hearthwork\'s premise word for word '
                'as your Hearthwork article gives it.'),
        'reading': ('Round 9, half B, in the whole guide ([result](%s)): "Attention without interpretation, advice, or fixing." '
                    'Human (Medium); "You speak. I listen. Then we switch." Human (Low); "Presence, Warmth, Discipline, '
                    'Confidentiality." Human (Medium). This paragraph alone ([check](%s)): AI Detected, 81%% AI: its first '
                    'sentence Human (Low), then the rest of the list and the sentence after it AI (Low). The section alone '
                    '([check](%s)): AI in every window.' % (FEED['B'], CHECK['p1'], CHECK['section'])),
        'advice_note': ('This is one of the two to work on. What reads as a model\'s: the run of fragments, the three-beat "You '
                        'speak. I listen. Then we switch.", and "interpretation, advice, or fixing", a list of three with no '
                        'catch-all, which your rule says to avoid. Here the premise describes Hearthwork for someone who hasn\'t '
                        'met it, so I\'d say it in a sentence or two of yours and keep the list as it is for the Hearthwork '
                        'article. The sentence after it ("because modern life rarely gives you anything like it") may read better '
                        'with something concrete in place of "modern life".'),
        'keep_label': 'Keep it as it is'})
    S.append({
        'id': 'HW-2', 'type': 'low', 'advice': 'edit', 'title': 'The three jobs a peer can lend you',
        'spans': [p2],
        'why': ('Alone, this paragraph reads Human (0% AI), with one Low window, "Keeping what you say private, and stopping '
                'when the time\'s up, lends you the Protector." In the whole guide it read Human at Medium.'),
        'reading': ('Round 9, half B ([result](%s)): "Keeping what you say private, ... If you say no, they don\'t push. But '
                    'they don\'t act as your Guide, ..." Human (Medium, 38 words); "Then you trade places, ..." Human (Medium). '
                    'This paragraph alone ([check](%s)): Human Written, 0%% AI; "Keeping what you say private, ..." Human '
                    '(Low), three windows Medium, two High.' % (FEED['B'], CHECK['p2'])),
        'advice_note': ('The lowest priority of the three, since it reads Human alone. If anything, Pangram is least sure of the '
                        'job-by-job pairing ("lend you the Nurturer", "lends you the Protector"). I\'d leave it.'),
        'keep_label': 'Keep it as it is'})
    S.append({
        'id': 'HW-3', 'type': 'low', 'advice': 'edit', 'title': 'Borrowed adulthood, and whether it\'s therapy',
        'spans': [p3],
        'why': ('Your driving-instructor aside is back, as you said. Even so, this paragraph alone reads AI in every window '
                '(100%), the aside\'s sentence at High. In the whole guide, round 9 read its first two sentences AI (Low) without '
                'the aside, and round 8 read them Human with it.'),
        'reading': ('Round 9, half B, without the aside ([result](%s)): the first two sentences AI (Low, 35 words); "Is that '
                    'therapy?" Human (Low); "Well, not the mainstream kind, but yes, for sure." Human (Medium). Round 8, half B, '
                    'with the aside ([result](%s)): "The peer doesn\'t become your permanent parent, though." Human (Medium), the '
                    'aside\'s sentence Human (High). This paragraph alone, with the aside ([check](%s)): AI Generated, 100%% AI. '
                    'The section alone ([check](%s)): AI in every window.' % (FEED['B'], ROUND8_B, CHECK['p3'], CHECK['section'])),
        'advice_note': ('The other one to work on, and the more important. Three things read as a model\'s: the list of three with '
                        'no catch-all ("show you a capacity, help you get the hang of it, and give it back to you"), which your '
                        'rule says to avoid; the question and answer ("Is that therapy? Well, not the mainstream kind, but yes, '
                        'for sure."); and the both-sides closer ("Professional therapy\'s still useful for what it does, and peers '
                        'and community do something else, so a serious healing path can include both."). Your aside stays either '
                        'way.'),
        'keep_label': 'Keep it as it is'})


def medium_cards():
    for s in SPOTS:
        if HW in s['section']:
            continue
        assert s['label'] == 'Human' and s['confidence'] == 'Medium', s
        sp = span(s['text'], heading_block(s['section']))
        short = s['words'] <= 5
        path = BL[sp['block']]['path']   # the page's headings: round 9's checked text has none, so SPOTS.json can name the
        place = ' > '.join(path[-2:])    # section before when a window opens a section ("Repair it.", B 34)
        S.append({
            'id': 'M-%s%d' % (s['half'], s['i']), 'type': 'medium', 'advice': 'edit',
            'title': '%s (%d word%s)' % (path[-1], s['words'], '' if s['words'] == 1 else 's'),
            'spans': [sp],
            'why': 'Round 9 read this window Human at Medium confidence in the whole guide (%s).' % place,
            'reading': 'Round 9, half %s ([result](%s)): "%s" Human (Medium, %d word%s).' % (
                s['half'], FEED[s['half']], s['text'].replace('\n', ' '), s['words'], '' if s['words'] == 1 else 's'),
            'advice_note': ('A window this short often reads below High on its own; I\'d leave it.' if short else
                            'I\'d leave it: it reads Human, and nothing in it breaks your rules. Edit it only if it reads '
                            'flat to you.'),
            'keep_label': 'Keep it as it is'})


def cards_md(review):
    out = ['# %s' % review['title'], '']
    out += [p for p in review['intro']] + ['']
    for s in review['suggestions']:
        b = BL[s['spans'][0]['block']]
        out += ['## %s: %s' % (s['id'], s['title']), '',
                '- **Where:** %s' % sr.where(BL, b['i']),
                '- **The words:** "%s"' % sr.block_text(BL, b['i'])[s['spans'][0]['start']:s['spans'][0]['end']],
                '- **Why it\'s here:** %s' % s['why'],
                '- **Pangram read:** %s' % s['reading'],
                '- **My advice:** %s' % s['advice_note'], '']
    return '\n'.join(out).rstrip('\n') + '\n'


def main():
    hearthwork_cards()
    medium_cards()
    keymap = {'low': 'caveat', 'medium': 'reread'}
    review = {
        'format': sr.FORMAT, 'review_id': 'inner-child-t121-round9-spots', 'title': 'Inner Child Round 9 Spots',
        'intro': [
            ('Round 9 read your guide Human Written in both halves. These are the 26 windows where it was less sure, on 21 '
             'cards. The three paragraphs of Hearthwork: Taking Turns come first: eight of the windows are there, both Low ones '
             'and the one AI window among them. I checked that '
             'section alone this turn, with your driving-instructor aside back, and then each of its paragraphs. Alone, its first '
             'and last paragraphs read AI, so those two are the ones I\'d work on.'),
            ('Every card is a stretch for you: Keep it as it is, or Edit it, which opens the paragraph for your own version. No card '
             'puts words of mine into your text. The other 18 cards are windows that read Human at Medium; I\'d leave them, the '
             'short ones especially. Your answers save as you click. When you\'re done, tell me in the chat, and I\'ll put your '
             'versions in and check them.'),
        ],
        'git_file': 'articles/inner-child-therapy/experiments/t121-review/REVIEW.html',
        'article': {'file': ARTICLE, 'sha256': hashlib.sha256(MD.encode('utf-8')).hexdigest()},
        'built': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M UTC'),
        'links': {'guide': BLOB + 'experiments/t121-review/GUIDE-PAGE.md', 'review': BLOB + 'experiments/t121-review/REVIEW-CARDS.md'},
        'types': {keymap[k]: v for k, v in TYPES.items()}, 'suggestions': S,
    }
    for x in S:
        x['type'] = keymap[x['type']]
    probs = sr.check(review, BL)
    if probs:
        sys.exit('\n'.join(probs))
    (HERE / 'REVIEW.json').write_text(json.dumps(review, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    (HERE / 'REVIEW-CARDS.md').write_text(cards_md(review), encoding='utf-8')
    r = subprocess.run([sys.executable, str(ROOT / 'tools/humanization/suggestion_review.py'), 'page', str(HERE / 'REVIEW.json'),
                        str(HERE / 'REVIEW.html'), '--artifact', str(HERE / 'REVIEW-artifact.html')],
                       cwd=ROOT, capture_output=True, text=True)
    print((r.stdout + r.stderr).strip()[-600:])
    if r.returncode:
        sys.exit(r.returncode)
    print('REVIEW.json', len(S), 'cards:', sum(x['type'] == 'caveat' for x in S), 'Low or AI,', sum(x['type'] == 'reread' for x in S), 'Medium')


if __name__ == '__main__':
    main()
