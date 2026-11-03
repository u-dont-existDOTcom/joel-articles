"""Joel's marking page for the community article's batch ic1101 (REVIEW-IC1101.json, .html, .artifact.html, .md).

Batch ic1101 (../RESULTS.md) checked in Pangram, each by itself, the sections of his live post that the 19 changes of
1 November touched (gate E307). Six windows read AI or Human (Low), in The New Age May Dawn Suddenly and Communes Are Hot
Again (a seventh was an image's alt text, not prose). Every one is in his post's words, so each comes to him here as a
card (gate E306; tools/humanization/suggestion_review.py, gate E265): a suggestion where the words are vague or read as a
formula, and "Keep it as it is" where the line is clear and his (two). What he approves goes into his post through its
editor, as on 1 November ("i didn't make the edits to community guide, that's too much. you can do that."), and each
section is then checked again by itself, its second and last try (lineage IC1101-NN).

  python3 articles/intentional-communities/candidate/fullread-20261030/review/joel-20261101-2026/sections/review/build_page_ic1101.py
"""
import collections
import datetime
import hashlib
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
SEC = HERE.parent
ART = HERE.parents[5]
ROOT = ART.parents[1]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import suggestion_review as sr  # noqa: E402

BLOB = 'https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/community-joel-1018/'
REL = 'articles/intentional-communities/candidate/fullread-20261030/review/joel-20261101-2026/sections/review/'
ARTICLE = 'articles/intentional-communities/master.md'
MD = (ART / 'master.md').read_text(encoding='utf-8')
BL = sr.blocks(MD)
RES = json.loads((SEC / 'RESULTS.json').read_text(encoding='utf-8'))
FOUND = 'Batch ic1101: each section your 19 changes touched, checked in Pangram by itself (1 November)'
DECIDE = 'Approve uses the suggestion; Reject keeps your words; Revise lets you write your own.'

TYPES = {
    'yours': {'label': 'Your post\'s words',
              'about': 'Words in your live post where Pangram read AI or Human (Low). Approve uses the suggestion; Reject '
                       'keeps your words; Revise lets you write your own. What you approve, I put into your post.'},
}


def window(key, start):
    """The window of section KEY whose text starts with START: 'AI (High), 22 words'."""
    hits = [w for w in RES[key]['windows'] if w.get('text', '').startswith(start)]
    assert len(hits) == 1, (key, start, len(hits))
    w = hits[0]
    return '%s (%s), %d words' % ('Human' if w['label'] == 'Human' else 'AI', w['confidence'], w['words'])


def block_with(s):
    hits = [b['i'] for b in BL if s in b['text']]
    assert len(hits) == 1, (s[:60], hits)
    return hits[0]


def card(cid, title, i, old, new, what, why, stays, note, read):
    t = BL[i]['text']
    assert t.count(old) == 1, (cid, old[:60])
    k = t.find(old)
    return {'id': cid, 'type': 'yours', 'title': title, 'where': sr.where(BL, i),
            'spans': [{'block': i, 'start': k, 'end': k + len(old.rstrip())}],
            'edits': [{'block': i, 'before': t, 'after': t.replace(old, new)}], 'inserts': [], 'moves': [],
            'what': what, 'why': why, 'stays': stays, 'advice': 'approve', 'advice_note': note, 'found_by': FOUND,
            'deciding': DECIDE, 'reading': read}


def edit_card(cid, title, i, old, why, note, read):
    t = BL[i]['text']
    assert t.count(old) == 1, (cid, old[:60])
    k = t.find(old)
    return {'id': cid, 'type': 'yours', 'title': title, 'where': sr.where(BL, i), 'advice': 'edit', 'why': why,
            'reading': read, 'advice_note': note, 'keep_label': 'keep it as it is', 'found_by': FOUND,
            'spans': [{'block': i, 'start': k, 'end': k + len(old)}]}


def build_cards():
    S = []
    i = block_with('Escuelita means “little school.”')
    S.append(card('W-1', '“Escuelita means “little school.” …”', i,
                  'brought outsiders into their communities for a while to learn autonomy by living it.',
                  'had outsiders stay with Zapatista families for a while and learn self-government by taking part in '
                  'everyday life.',
                  '“brought outsiders into their communities for a while to learn autonomy by living it” becomes “had '
                  'outsiders stay with Zapatista families for a while and learn self-government by taking part in '
                  'everyday life”. The link on Escuelita stays.',
                  '“Learn autonomy by living it” is the abstract part. Your own section on the Escuelita, further down, '
                  'says what it was: “Outsiders lived with families and learned autonomy by participating in ordinary '
                  'life.”',
                  '“Escuelita means “little school.”” and the rest of the paragraph word for word.',
                  'I’d approve: the reader learns what the Escuelita was the first time it comes up.',
                  window('ic1101-01', 'Escuelita means')))
    S.append(edit_card('W-2', '“Otherwise, we’ve built a lovely refuge …”', i,
                       'Otherwise, we’ve built a lovely refuge for whoever got there first.',
                       'Pangram read these twelve words Human (Low). It’s the paragraph’s last line, and yours from the '
                       'first version of the post; it says what it means.',
                       'Keep it as it is, I’d say. If you’d rather change it, Edit it.',
                       window('ic1101-01', 'Otherwise, we')))
    i = block_with('I was usually just a visitor’s kid')
    S.append(card('W-3', '“I was usually just a visitor’s kid …”', i,
                  'I was usually just a visitor’s kid, close enough to see how people lived but never quite part of the '
                  'tribe.',
                  'I was usually just a visitor’s kid. I could see how people lived, but I was never really part of the '
                  'tribe.',
                  'One sentence becomes two, and “close enough to … but never quite …” becomes “I could see … but I was '
                  'never really …”.',
                  'AI (High), the only High AI window in the section. “Close enough to X but never quite Y” is a '
                  'balanced turn of phrase Pangram reads as a formula; said straight, it’s the same point.',
                  'The list of communities before it and the sentence after it.',
                  'I’d approve.', window('ic1101-01', 'I was usually')))
    S.append(card('W-4', '“At the time, that meant a lot of boredom …”', i,
                  'At the time, that meant a lot of boredom, with some adventures mixed in, but those years gave me a '
                  'great sample to compare against.',
                  'At the time it was mostly boring, with some adventures mixed in, but it means I’ve seen a lot of '
                  'communities to compare against.',
                  '“those years gave me a great sample to compare against” becomes “it means I’ve seen a lot of '
                  'communities to compare against”.',
                  'AI (Low). “A great sample to compare against” didn’t say a sample of what; it’s the communities '
                  'you grew up visiting, which is why the article can compare them.',
                  'The adventures, and the rest of the paragraph.',
                  'I’d approve.', window('ic1101-01', 'At the time')))
    i = block_with('We evolved to live in small groups where everybody knows everybody.')
    S.append(edit_card('W-5', '“We evolved to live in small groups …”', i,
                       'We evolved to live in small groups where everybody knows everybody.',
                       'Pangram read these eleven words Human (Low). The sentence is clear, and it’s the premise the '
                       'paragraph needs.',
                       'Keep it as it is, I’d say.', window('ic1101-02', 'We evolved')))
    S.append(card('W-6', '“… and nobody knows anybody well enough …”', i,
                  'and nobody knows anybody well enough to see what they’re really like.',
                  'and nobody knows anybody well enough to tell who can be trusted.',
                  '“to see what they’re really like” becomes “to tell who can be trusted”.',
                  'Human (Low), 30 words. This is the clause you approved on 1 November (C-4) as the reason large '
                  'societies end up run by psychopaths; “what they’re really like” left that reason vague. Who can be '
                  'trusted is what the next sentence turns on.',
                  'The rest of the sentence and of the paragraph word for word.',
                  'I’d approve, if that’s the reason you meant; if not, Revise.', window('ic1101-02', 'In a large')))
    return S


def build():
    S = build_cards()
    S.sort(key=lambda s: (s['spans'][0]['block'], s['spans'][0]['start']))
    n = collections.Counter(s['advice'] for s in S)
    review = {
        'format': sr.FORMAT, 'review_id': 'intentional-communities-ic1101-20261101',
        'title': 'Community Article Cards, 1 November',
        'intro': [
            'Your live post, as it has been since the 19 changes went in on 1 November. Each section those changes '
            'touched was checked in Pangram by itself: 13 sections, 10 of them Human Written, and three Mostly Human '
            'Written. Six windows read AI or Human (Low), all in your post’s words, so they’re here: <b>%d '
            'suggestions</b>, and <b>%d lines</b> I’d keep as they are. (The seventh was the alt text of the '
            'infographic, which isn’t prose.)' % (n['approve'], n['edit']),
            'What you approve, I put into your post through its editor, as on 1 November. Then each of the two '
            'sections gets its second and last check by itself.',
            'Your answers save as you click. When you’re done, click <b>Copy my answers</b> (or <b>Save them as a '
            'file</b>) and send them to me.',
        ],
        'git_file': REL + 'REVIEW-IC1101.html',
        'article': {'file': ARTICLE, 'sha256': hashlib.sha256(MD.encode('utf-8')).hexdigest()},
        'links': {'guide': BLOB + ARTICLE, 'review': BLOB + REL + 'REVIEW-IC1101.md'},
        'built': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M UTC'),
        'types': TYPES, 'suggestions': S,
    }
    return review


def marked(j, spans):
    t = BL[j]['text']
    for sp in sorted((x for x in spans if x['block'] == j), key=lambda x: -x['start']):
        t = t[:sp['start']] + '**' + t[sp['start']:sp['end']] + '**' + t[sp['end']:]
    return t


def cards_md(review):
    types = review['types']
    out = ['# %s: every card' % review['title'], '',
           'The page\'s cards as text, in the order of the post. Built %s from [your post as it is live](%s). To answer, '
           'use the page; or write your answer under a card\'s number in a message to me.' % (
               review['built'], review['links']['guide']), '']
    section = None
    for s in review['suggestions']:
        b = s['spans'][0]['block']
        if BL[b]['section'] != section:
            section = BL[b]['section']
            out += ['## %s' % (section or 'The opening'), '']
        out += ['### %s: %s (%s)' % (s['id'], s['title'], types[s['type']]['label']), '',
                '**Pangram read:** %s' % s['reading'], '']
        if s['advice'] == 'edit':
            out += ['**As it is now** (the words Pangram read in bold):', '', '> %s' % marked(b, s['spans']), '']
        else:
            for e in s['edits']:
                out += ['**Now** (the words it changes in bold):', '', '> %s' % marked(e['block'], s['spans']), '',
                        '**How it would read:**', '', '> %s' % e['after'], '']
        out += ['**Why:** %s' % s['why'], '', '**My advice:** %s' % s['advice_note'], '']
    return '\n'.join(out).replace('\n\n\n', '\n\n') + '\n'


def main():
    review = build()
    probs = sr.check(review, BL)
    for p in probs:
        print('PROBLEM', p)
    (HERE / 'REVIEW-IC1101.json').write_text(json.dumps(review, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    if probs:
        sys.exit(1)
    page = sr.page(review, MD, BL)
    (HERE / 'REVIEW-IC1101.html').write_text(page, encoding='utf-8')
    (HERE / 'REVIEW-IC1101.artifact.html').write_text(sr.artifact_view(page), encoding='utf-8')
    (HERE / 'REVIEW-IC1101.md').write_text(cards_md(review), encoding='utf-8')
    print(len(review['suggestions']), 'cards')


if __name__ == '__main__':
    main()
