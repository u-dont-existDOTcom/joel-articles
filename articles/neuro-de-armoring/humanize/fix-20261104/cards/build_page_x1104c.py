"""Neuro De-Armoring Cards, 4 November (2): after his answers of 2026-11-04 12:06 UTC (all 12 cards approved; "5a and if
you can't figure it out i can help").

- Scott's paragraph (block 83): the card's version (Codex's) reads Human Written with its last three sentences Low; both of
  my 5a tries read worse (../checks/x1104h, x1104i), so that stretch goes to him to edit, with the tell panel on it linked
  (E253 (Inner Child): ../panel/b083-codex/PANEL.md) and the ask in his words.
- The last warnings card from ../warnings/WARNINGS-CHECK.md (item 4: 5-HTP and uridine "can change brain sensitivity
  quickly"), said as experience, as his answer 4a did for uridine. The rest of that check's "keep, or soften" lines stay as
  they are, and its five "your call" lines are question 6 on the questions page.

  python3 articles/neuro-de-armoring/humanize/fix-20261104/cards/build_page_x1104c.py
Writes REVIEW-X1104C.json, .html, .artifact.html and .md here.
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
GIT_FILE = LANE + 'fix-20261104/cards/REVIEW-X1104C.html'
ARTICLE = H / 'HUMANIZED-SO-FAR.md'
MD = ARTICLE.read_text(encoding='utf-8')
SHA = hashlib.sha256(MD.encode('utf-8')).hexdigest()
BL = sr.blocks(MD)
P = 'https://www.pangram.com/history/'
CARD83 = P + 'bdc81685-fdd0-420e-b74f-1a196b1ec606'
TRY1 = P + 'e8b5de85-2203-4504-b915-cd94e9fbf63e'
TRY2 = P + '7a054118-a4e0-411a-b9fa-3efb1ebf7850'
PANEL = BLOB + LANE + 'fix-20261104/panel/b083-codex/PANEL.md'
WC = BLOB + LANE + 'fix-20261104/warnings/WARNINGS-CHECK.md'
TYPES = {
    'help': {'label': 'Help me see what I\'m missing',
             'about': 'A stretch that reads Human, but at Low confidence, and that my tries made worse. Edit it the way you '
                      'would, or keep it as it is.'},
    'warning': {'label': 'A warning the research doesn\'t back',
                'about': 'What the warnings check found, with the source, and the change it supports. Approve it, revise '
                         'it, or keep the post\'s wording.'},
}


def block_with(s):
    hits = [b['i'] for b in BL if b['text'].startswith(s)]
    assert len(hits) == 1, (s, hits)
    return hits[0]


def main():
    i83 = block_with('Scott added a standard dose of UMP')
    t83 = sr.block_text(BL, i83)
    low = t83.index('You can\'t tell from this whether')
    i17 = block_with('Uridine & 5-HTP Warning for Psychedelic Users:')
    t17 = sr.block_text(BL, i17)
    old = 'They are repair-oriented levers that can change brain sensitivity quickly.'
    assert t17.count(old) == 1
    S = [
        {'id': 'Y-83b', 'type': 'help', 'title': '"You can\'t tell from this whether UMP rebuilt his D3 receptors overnight ..."',
         'advice': 'edit', 'keep_label': 'keep it as it is',
         'spans': [{'block': i83, 'start': low, 'end': len(t83)}],
         'reading': 'the paragraph by itself, Human Written, 0.0%%: High on the first two sentences, Medium on the '
                    'tolerance line, Low on these three: [check](%s)' % CARD83,
         'why': 'Your 5a gave it two more tries. Three fresh readers had agreed on two of these sentences ([their notes]'
                '(%s)), and I fixed those two twice. Rewriting all three read [84.6%% AI](%s); changing only the "It does '
                'suggest ..." sentence read [99.99%% AI](%s), the sentences I hadn\'t touched included. So that sentence, as '
                'Codex wrote it, holds the paragraph up, and I can\'t see why.' % (PANEL, TRY1, TRY2),
         'advice_note': 'I can\'t find any more AI tells here, and I see some human tells, like "again too" and your "real '
                        'childhood memories"... can you help show me the tells I\'m missing?',
         'found_by': 'Paragraph checks through the API, 4 November (batches x1104h and x1104i)'},
        {'id': 'W-17', 'type': 'warning', 'title': '"Uridine & 5-HTP Warning for Psychedelic Users: These are not "trip enhancers." ..."',
         'advice': 'approve', 'approve_label': 'use this wording',
         'spans': [{'block': i17, 'start': t17.index(old), 'end': t17.index(old) + len(old)}],
         'edits': [{'block': i17, 'before': t17,
                    'after': t17.replace(old, 'They are repair-oriented levers that, in practice, can change brain '
                                              'sensitivity quickly.')}],
         'what': '"in practice": the quick change in brain sensitivity said as experience, the way your 4a has uridine\'s '
                 'effects said.',
         'why': 'No study of 5-HTP or uridine changing brain sensitivity quickly turned up ([the warnings check](%s), item '
                '4). The 5-HTP section already says responders "can feel it quickly".' % WC,
         'deciding': 'Whether "in practice" goes in.',
         'stays': 'The rest of the warning, word for word: the 5-HTP interaction list, the ayahuasca and iboga lines.',
         'found_by': 'The warnings check, 4 November'},
    ]
    review = {
        'format': sr.FORMAT, 'review_id': 'neuro-de-armoring-cards-20261104-x1104c',
        'title': 'Neuro De-Armoring Cards, 4 November (2)',
        'intro': [
            'Your 12 cards are in. Of the 5a tries, the evidence paragraph\'s second one read better, with no Low window '
            'left, so it\'s in too. Scott\'s paragraph\'s Low window got worse both times, so it\'s here for you, as you '
            'offered.',
            'Then the last warnings card. The rest of the 5-HTP and iboga lines stay as they are: softening them would '
            'narrow real cautions. The five generic lines are question 6 on the questions page.',
            'Your answers save as you click. When you\'re done, click <b>Copy my answers</b> (or <b>Save them as a file</b>) '
            'and send them to me.'],
        'git_file': GIT_FILE, 'article': {'file': LANE + 'HUMANIZED-SO-FAR.md', 'sha256': SHA},
        'links': {'guide': BLOB + LANE + 'HUMANIZED-SO-FAR.md', 'review': BLOB + LANE + 'fix-20261104/cards/REVIEW-X1104C.md'},
        'built': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M UTC'),
        'types': TYPES, 'suggestions': S,
    }
    probs = sr.check(review, BL)
    for p in probs:
        print('PROBLEM', p)
    (HERE / 'REVIEW-X1104C.json').write_text(json.dumps(review, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    if probs:
        sys.exit(1)
    page = sr.page(review, MD, BL)
    (HERE / 'REVIEW-X1104C.html').write_text(page, encoding='utf-8')
    (HERE / 'REVIEW-X1104C.artifact.html').write_text(sr.artifact_view(page), encoding='utf-8')
    md = ['# %s: every card' % review['title'], '',
          'The page\'s cards as text. Built %s from [your post with your versions in](%s). To answer, use the page; or write '
          'your version under a card\'s number in a message to me.' % (review['built'], review['links']['guide']), '']
    for s in S:
        md += ['## %s: %s (%s)' % (s['id'], s['title'], TYPES[s['type']]['label']), '',
               '*%s*' % sr.where(BL, s['spans'][0]['block']), '']
        if s.get('reading'):
            md += ['**Pangram read:** %s' % s['reading'], '']
        sp = s['spans'][0]
        md += ['> %s' % BL[sp['block']]['text'][sp['start']:sp['end']], '']
        for e in s.get('edits', []):
            md += ['**As it would read:**', '', '> %s' % sr.blocks(e['after'])[0]['text'], '']
        if s.get('what'):
            md += ['**What changes:** %s' % s['what'], '']
        md += ['**Why:** %s' % s['why'], '']
        if s.get('stays'):
            md += ['**What stays:** %s' % s['stays'], '', '**You\'re deciding:** %s' % s['deciding'], '']
        if s.get('advice_note'):
            md += ['**My ask:** %s' % s['advice_note'], '']
    (HERE / 'REVIEW-X1104C.md').write_text('\n'.join(md) + '\n', encoding='utf-8')
    print('ok', [s['id'] for s in S])


if __name__ == '__main__':
    main()
