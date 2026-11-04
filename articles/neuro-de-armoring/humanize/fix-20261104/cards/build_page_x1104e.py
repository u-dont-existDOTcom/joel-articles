"""Neuro De-Armoring Cards, 4 November (4): two stretches to edit, after the lane's checks in Pangram's web app (Joel's
message of 2026-11-04 20:19 UTC: "so then are we done can we publish it?").

- His post's block 92 (the 5-HTP stop signs): four tries of mine and Codex's rewrite (the writer of another family, E253)
  read AI Generated, 100% AI, by themselves; the readers' panel on my second try and on Codex's draft is linked. Both of
  its lists are the protocol's (E336), so every side effect stays. His post's paragraph is the one he edits.
- His post's block 93 (the 5-HTP interactions), my fourth try, in the article: Human Written, 0.0% AI, with the case
  report's story at Low. A one-sentence fix of a Low window has moved the other windows before (E350), so the stretch is
  his, and the story is my addition (from the linked report, read in full), which he may cut.
Each ask is in his words (E253): "I can't find any more AI tells here, and I see some human tells, like these... can you
help show me the tells I'm missing?", with the human tells I see (his words, a fact he gave, a rough edge: E251).

  python3 articles/neuro-de-armoring/humanize/fix-20261104/cards/build_page_x1104e.py
Writes REVIEW-X1104E.json, .html, .artifact.html and .md here.
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
import suggestion_review as sr  # noqa: E402

BLOB = 'https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/community-joel-1018/'
LANE = 'articles/neuro-de-armoring/humanize/'
GIT_FILE = LANE + 'fix-20261104/cards/REVIEW-X1104E.html'
ARTICLE = H / 'HUMANIZED-SO-FAR.md'
MD = ARTICLE.read_text(encoding='utf-8')
SHA = hashlib.sha256(MD.encode('utf-8')).hexdigest()
BL = sr.blocks(MD)
P = 'https://www.pangram.com/history/'
PANEL = BLOB + LANE + 'fix-20261104/panel/%s/PANEL.md'
ASK = ('I can\'t find any more AI tells here, and I see some human tells, like %s... can you help show me the tells I\'m '
       'missing? ([The readers\' notes](%s))')
HTP = '[its section, AI Detected, 82.1%% AI](%s1239d2f8-ca44-4713-b0b7-e9791b5211e3)' % P
TYPES = {'help': {'label': 'Help me see what I\'m missing',
                  'about': 'A paragraph my tries couldn\'t get to read Human (High). Edit it the way you would, or keep it '
                           'as it is.'}}


def block_with(s):
    hits = [b['i'] for b in BL if b['text'].startswith(s)]
    assert len(hits) == 1, (s, hits)
    return hits[0]


def whole(i):
    return [{'block': i, 'start': 0, 'end': len(sr.block_text(BL, i))}]


def main():
    i92 = block_with('Side effects / stop signs: Nausea, stomach discomfort')
    i93 = block_with('Don\'t mix 5-HTP casually with anything else that raises serotonin')
    t93 = sr.block_text(BL, i93)
    low0 = t93.index('Case reports and reviews keep warning')
    low1 = t93.index('Luckily he recovered.')
    S = [
        {'id': 'Y-92', 'type': 'help', 'title': '"Side effects / stop signs: Nausea, stomach discomfort, loose stools ..."',
         'advice': 'edit', 'keep_label': 'keep it as it is', 'spans': whole(i92),
         'reading': 'your post\'s version, in the baseline: %s' % HTP,
         'why': 'Five versions read AI Generated, 100%% AI, by themselves in Pangram: my '
                '[first](%sb41d1fdd-9d7f-4d04-8cbd-8e10113c0fdd), with the dangerous pattern first, came closest (Medium, Low, '
                'Medium); my [second](%s4ab27097-dcd1-4ee8-82b5-5052ac1e80e2), [third](%s7c0961a8-6334-4310-b68c-8b5dfa33e032) '
                'and [fourth](%sdf854bc0-34cd-4c30-b272-efc81dbd24ba), and Codex\'s rewrite '
                '([fifth](%s16fdad52-4fd8-45d8-b765-0c1c3d74e202)), each one AI (High) window. The readers called it a '
                'two-tier checklist every time: the "+" chain, the near-synonyms ("anxiety, irritability, emotional '
                'agitation"), the hedged "can be ... which can become dangerous" ([their notes on my second](%s), [on '
                'Codex\'s](%s)). Both lists are the protocol\'s, so every side effect and every sign of the dangerous pattern '
                'stays.' % (P, P, P, P, P, PANEL % 'b092-n2', PANEL % 'b092-c1'),
         'advice_note': ASK % ('your "a too-bright / hypomanic feeling"', PANEL % 'b092-c1'),
         'found_by': 'Paragraph checks in Pangram\'s web app, 4 November (batches x1104p to x1104t)'},
        {'id': 'Y-93', 'type': 'help', 'title': '"Case reports and reviews keep warning about the risk with 5-HTP ..."',
         'advice': 'edit', 'keep_label': 'keep it as it is', 'spans': [{'block': i93, 'start': low0, 'end': low1}],
         'reading': 'the paragraph by itself, Human Written, 0.0%% AI: High, Medium, then Low on this sentence, Medium, '
                    'High ([check](%s2be95f74-b2cf-45ec-a669-1807880af623))' % P,
         'why': 'This is my fourth try, now in the article, with your post\'s label "Hard interaction rule:" gone, as you '
                'dropped "Scott\'s version:" and "Trial:". The story is my addition: what happened in the case report your '
                'post links, which I read in full (a 28-year-old man on sertraline took 5-HTP with many weight-loss and energy '
                'supplements on the day of a workout; serotonin syndrome led to emergency surgery on both lower legs and his '
                'right forearm, and he recovered completely). Cut it if you don\'t want it. My tries before it read AI: '
                '[first](%s5e797c26-95a2-4caa-aedb-6a88b723f6f5), 100%% AI; '
                '[second](%scb693d91-b9c2-41cc-9a8e-20bd56779126), 46.5%% AI, with the story AI (Medium); '
                '[third](%sd2dffc85-efd5-42d0-af45-13a7c3917e05), 24.3%% AI. A one-sentence fix of a Low window has moved the '
                'other windows before (E350), so the stretch is yours.' % (P, P, P),
         'advice_note': ASK % ('your "psychedelic days"', PANEL % 'b093-n2'),
         'found_by': 'Paragraph checks in Pangram\'s web app, 4 November (batches x1104p to x1104s)'},
    ]
    review = {
        'format': sr.FORMAT, 'review_id': 'neuro-de-armoring-cards-20261104-x1104e',
        'title': 'Neuro De-Armoring Cards, 4 November (4)',
        'intro': [
            'Two stretches of the 5-HTP section for you to edit. I checked both myself in Pangram\'s web app, one paragraph '
            'at a time. The stop signs read AI in all five versions, mine and Codex\'s. The interactions paragraph reads '
            'Human now, with one Low window over a case story I added.',
            'The first card shows your post\'s paragraph; the second shows my version, which is in the article. Edit it the '
            'way you would, or keep it as it is.',
            'Your answers save as you click. When you\'re done, click <b>Copy my answers</b> (or <b>Save them as a file</b>) '
            'and send them to me.'],
        'git_file': GIT_FILE, 'article': {'file': LANE + 'HUMANIZED-SO-FAR.md', 'sha256': SHA},
        'links': {'guide': BLOB + LANE + 'HUMANIZED-SO-FAR.md', 'review': BLOB + LANE + 'fix-20261104/cards/REVIEW-X1104E.md'},
        'built': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M UTC'),
        'types': TYPES, 'suggestions': S,
    }
    probs = sr.check(review, BL)
    for p in probs:
        print('PROBLEM', p)
    (HERE / 'REVIEW-X1104E.json').write_text(json.dumps(review, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    if probs:
        sys.exit(1)
    page = sr.page(review, MD, BL)
    (HERE / 'REVIEW-X1104E.html').write_text(page, encoding='utf-8')
    (HERE / 'REVIEW-X1104E.artifact.html').write_text(sr.artifact_view(page), encoding='utf-8')
    md = ['# %s: every card' % review['title'], '',
          'The page\'s cards as text. Built %s from [your post with your versions in](%s). To answer, use the page; or write '
          'your version under a card\'s number in a message to me.' % (review['built'], review['links']['guide']), '']
    for s in S:
        md += ['## %s: %s (%s)' % (s['id'], s['title'], TYPES[s['type']]['label']), '',
               '*%s*' % sr.where(BL, s['spans'][0]['block']), '']
        md += ['**Pangram read:** %s' % s['reading'], '']
        sp = s['spans'][0]
        md += ['> %s' % BL[sp['block']]['text'][sp['start']:sp['end']], '']
        md += ['**Why:** %s' % s['why'], '', '**My ask:** %s' % s['advice_note'], '']
    (HERE / 'REVIEW-X1104E.md').write_text('\n'.join(md) + '\n', encoding='utf-8')
    print('ok', [s['id'] for s in S])


if __name__ == '__main__':
    main()
