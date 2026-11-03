"""Hypnosis Guide Cards, 2 November (3): what the two free checks of the whole guide (his result pages of 21:57 and 23:07
UTC) still read below High, after batch f1102's fixes (REVIEW-F1102.json, .html, .artifact.html, .md).

- Two suggestions on his words, each checked in its stretch through the API and through the owner-delivery gate
  (gate/GATE.md) before it reaches him: C-92 (his inner child guide's rent line, the joke in brackets) and C-480 (his Core
  prompts caveat joined to its sentence). A suggestion the gate didn't admit is left off.
- Stretches to edit (advice "edit": keep it as it is, or edit it): his Troubleshooting seam (AI (Low) in both whole checks;
  Substack's check leaves the heading out, so Nothing happens runs into It feels fake), and three of ours that read AI or
  Human (Low) in the whole after two tries each (the left-brain/right-brain pairs, the two-hand practice's breathing line,
  the sources line).
Every reading and every check carries its link (suggestion_review.py 1.5 refuses a card without).

  python3 articles/inner-signal/humanize/fix-20261102/f1102/build_page_f1102.py
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
sys.path.insert(0, str(F / 'review'))
sys.path.insert(0, str(HERE / 'gate'))
import build_page_r1102 as prev  # noqa: E402
import make_gate as mg  # noqa: E402
import suggestion_review as sr  # noqa: E402

BLOB, LANE = prev.BLOB, prev.LANE
GIT_FILE = LANE + 'fix-20261102/f1102/REVIEW-F1102.html'
MD = (H / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
BL = sr.blocks(MD)
P = 'https://www.pangram.com/history/'
FA1, FB1 = 'https://www.pangram.com/feed/e6bb0af2-11b7-42ac-9026-1a4c51ba75f8', 'https://www.pangram.com/feed/788969af-0de3-43b6-a37c-e28759c7a816'
FA2, FB2 = 'https://www.pangram.com/feed/0c89b980-8ffd-44fd-9cde-8a75f9ee4c8c', 'https://www.pangram.com/feed/27c8a2a4-399b-4a20-b8d1-e9ae2957bca4'
FOUND = 'The two free checks of the whole guide (2 November), your result pages of 21:57 and 23:07 UTC'
TYPES = dict(prev.TYPES)
TYPES['stuck'] = {'label': 'Our words, still below High', 'about': 'Words of ours that read AI or Human (Low) in the whole guide '
                  'after two tries each. Keep it as it is (the clear version stays in), or Edit it: your own versions have read '
                  'Human.'}


def admitted(name):
    return (HERE / 'gate' / name / 'FOR-JOEL.txt').exists()


def edit_card(cid, typ, title, blocks, why, note, read):
    return {'id': cid, 'type': typ, 'title': title, 'where': sr.where(BL, blocks[0]), 'advice': 'edit', 'why': why,
            'reading': read, 'advice_note': note, 'keep_label': 'keep it as it is', 'found_by': FOUND,
            'spans': [{'block': b, 'start': 0, 'end': len(BL[b]['text'])} for b in blocks]}


def block_with(s):
    hits = [b['i'] for b in BL if s in b['text']]
    assert len(hits) == 1, (s[:60], hits)
    return hits[0]


def build_cards():
    prev.BL = BL
    S = []
    if admitted('G-92'):
        i = block_with(mg.OLD92)
        s = prev.card(
            'C-92', 'icguide', '“It’s still one grown-up doing three jobs …”', [(i, mg.OLD92, mg.DRAFTS['G-92']['new'])],
            'Your inner child guide’s rent line keeps its joke and its point, with the joke in brackets: “It’s still one '
            'grown-up doing three jobs (nobody new is moving in to help with the rent), and each job keeps the others in '
            'balance.”',
            'In the whole guide your line read AI (Low) the first time and Human (Low) the second. Its shape is “That’s X, '
            'not Y”, the polished quip you called an AI pattern (E190), and with the joke in brackets that shape is gone.',
            'Your joke, your three jobs and your “each job keeps the others in balance”, and the party example after it.',
            'Approve if the bracket sounds like you: in its stretch it reads Human Written in one High window, where your '
            'line with its last clause cut read Human (Medium). Reject keeps your line.',
            FOUND,
            'AI (Low), 27 words: [the first check, part A](%s); Human (Low), 27 words: [the second, part A](%s)' % (FA1, FA2),
            'With the bracket: Human Written, one window, High: [check](%sa1aff5ea-da51-415b-a4eb-cc3aef09e8e3). With the '
            'clause cut instead: Human (Medium) on the line: [check](%sc48a4926-1585-46dc-921a-6aaa03fd5972)' % (P, P))
        s['where'] = sr.where(BL, i)
        S.append(s)
    if admitted('G-480'):
        i = block_with(mg.OLD480)
        s = prev.card(
            'C-480', 'yours', '“… though that doesn’t make the answers any more true.”', [(i, mg.OLD480, mg.NEW480)],
            'Your two last sentences of Core prompts become one: “Used together properly, the subconscious can feel safer in '
            'giving its response, though that doesn’t make the answers any more true.”',
            'Your short last line read Human (Low) by itself in both whole checks. Joined to the sentence it qualifies, it '
            'isn’t a line on its own any more.',
            'Every word of yours; only “That” becomes “that”, and your “though” moves to the front of the clause.',
            'Approve: same words, and in its stretch the joined sentence reads Human (High).',
            FOUND,
            'Human (Low), 10 words: [the first check, part B](%s) and [the second, part B](%s)' % (FB1, FB2),
            'Joined: Human Written, the sentence in a High window: [check](%s99c37345-2641-4db2-be55-e4324087321d)' % P)
        s['where'] = sr.where(BL, i)
        S.append(s)
    i = block_with('Check if there\'s a way you could try this on a smaller scale')
    S.append(edit_card(
        'E-380', 'yours', '“… “Show me whether today is for listening or resting.”” / “Well, what do you mean “it”…”', [i, i + 2],
        'Your Troubleshooting version read Human Written for you, with its headings ([your check](%sb7fc49b6-e142-4456-a1a5-9d0bc6c646e1)). '
        'Substack’s check leaves headings out, so there the end of Nothing happens runs straight into It feels fake, and '
        'that seam read AI (Low) in both whole checks, with Human (Low) on the lines around it.' % P,
        'Keep it as it is, if the seam doesn’t bother you: readers see the heading. Or edit the last line of Nothing happens '
        'or the first of It feels fake, and the next check reads it in place.',
        'AI (Low), 32 words: [the first check, part A](%s) and [the second, part A](%s)' % (FA1, FA2)))
    i = block_with('Your body has its own yes and no')
    S.append(edit_card(
        'E-61', 'stuck', '“Your body has its own yes and no …” / “Analysis with no love in it …”', [i, i + 1],
        'The pairs of minds read AI (Low) in the first check. My version read Human in its stretch ([check](%sc361e22f-9ae8-4b65-be8b-215e1d2794de)) '
        'and AI (Low) again in the whole.' % P,
        'Edit it, if you can say it your way; I’m out of versions that read Human in the whole. Or keep it as it is.',
        'AI (Low), two windows: [the first check, part A](%s), before my version, and [the second, part A](%s), with it' % (FA1, FA2)))
    i = block_with('Keep breathing gently through the whole practice.')
    S.append(edit_card(
        'E-119', 'stuck', '“Keep breathing gently through the whole practice.”', [i - 1, i],
        'The breathing line read Human (Low) in both whole checks. Joined differently it read Human (Low) again ([check](%sd9e3b9fa-1645-4a15-b29b-a200b1262447)); '
        'with the two sentences of ours before it cut, the stretch read AI Detected ([check](%s9a2c0524-9c4f-437b-ab2a-a1cfed0e3b47)).' % (P, P),
        'Edit it, if you like: the last lines of the practice are ours. Or keep it as it is.',
        'Human (Low), 7 words: [the first check, part A](%s) and [the second, part A](%s)' % (FA1, FA2)))
    i = block_with('The information on these techniques comes from these sources')
    S.append(edit_card(
        'E-762', 'stuck', '“The information on these techniques comes from these sources …”', [i],
        'The disclaimer about the sources read Human (Low) in both whole checks. Said plainly it read Human (Low) again '
        '([check](%s980fd19b-1041-45a1-8cd5-a70025b4c612)); said with an idiom it read AI Detected ([check](%s26f67e2c-984e-4a54-a3ff-138d1ef4e6f7)).' % (P, P),
        'Edit it, if you like; it has to keep that the sources don’t vouch for every NLP claim or every example for trauma '
        'work, and that Nimja didn’t write or endorse the guide. Or keep it as it is.',
        'Human (Low), 34 words: [the first check, part B](%s) and [the second, part B](%s)' % (FB1, FB2)))
    return S


def cards_md(review):
    """The cards as text: prev.cards_md's layout, with the edit cards (no suggestion) shown as the words to look at."""
    types = review['types']
    out = ['# %s: every card' % review['title'], '',
           'The page\'s cards as text, in the order of the guide. Built %s from [the guide so far](%s). To answer, use '
           'the page; or write your answer under a card\'s number in a message to me.' % (review['built'], review['links']['guide']), '']
    for s in review['suggestions']:
        out += ['## %s: %s (%s)' % (s['id'], s['title'], types[s['type']]['label']), '', '*%s*' % s['where'], '']
        if s.get('reading'):
            out += ['**Pangram read:** %s' % s['reading'], '']
        if s['advice'] == 'edit':
            for sp in s['spans']:
                out += ['> %s' % BL[sp['block']]['text'], '']
        else:
            out += ['**Pangram on the suggestion:** %s' % s['tested'], '']
            for e in s['edits']:
                out += ['**Now** (the words it changes in bold):', '', '> %s' % prev.marked(e['block'], s['spans']), '',
                        '**How it would read:**', '', '> %s' % e['after'], '']
        out += ['**Why:** %s' % s['why'], '', '**My advice:** %s' % s['advice_note'], '']
    return '\n'.join(out).replace('\n\n\n', '\n\n') + '\n'


def build():
    S = build_cards()
    S.sort(key=lambda s: (s['spans'][0]['block'], s['spans'][0]['start']))
    n = collections.Counter(s['type'] for s in S)
    review = {
        'format': sr.FORMAT, 'review_id': 'inner-signal-hypnosis-guide-cards-20261102-f1102',
        'title': 'Hypnosis Guide Cards, 2 November (3)',
        'intro': [
            'Your hypnosis guide as it is in Git, after the two free checks of the whole guide. Part B read Human Written with '
            'no AI window; part A read Human Written with three short AI (Low) windows. These <b>%d cards</b> are what\'s '
            'left below High that a fix of mine couldn\'t clear, or that touches your words. Each card links each check.' % len(S),
            'Your answers save as you click. When you\'re done, click <b>Copy my answers</b> (or <b>Save them as a file</b>) and '
            'send them to me.'],
        'git_file': GIT_FILE, 'article': {'file': LANE + 'HUMANIZED-SO-FAR.md', 'sha256': hashlib.sha256(MD.encode('utf-8')).hexdigest()},
        'links': {'guide': BLOB + LANE + 'HUMANIZED-SO-FAR.md', 'review': BLOB + LANE + 'fix-20261102/f1102/REVIEW-F1102.md'},
        'built': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M UTC'),
        'types': TYPES, 'suggestions': S,
    }
    return review, n


def main():
    review, n = build()
    probs = sr.check(review, BL)
    for p in probs:
        print('PROBLEM', p)
    (HERE / 'REVIEW-F1102.json').write_text(json.dumps(review, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    if probs:
        sys.exit(1)
    page = sr.page(review, MD, BL)
    (HERE / 'REVIEW-F1102.html').write_text(page, encoding='utf-8')
    (HERE / 'REVIEW-F1102.artifact.html').write_text(sr.artifact_view(page), encoding='utf-8')
    (HERE / 'REVIEW-F1102.md').write_text(cards_md(review), encoding='utf-8')
    print(len(review['suggestions']), 'cards:', dict(n))


if __name__ == '__main__':
    main()
