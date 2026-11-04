"""Neuro De-Armoring Cards, 4 November: the two uridine paragraphs after his, done his way one at a time, for his help.

After his message of 2026-11-04 10:01 UTC ("i don't want to do everything myself the point is to teach you ... just work
on one paragraph at a time"), the paragraphs after his "Who this is for" were rewritten the way it is built (gate E338
(gut); his B081) and each checked by itself (../checks/, batches x1104a to x1104d). Neither reached Human (High) in four
tries, so each goes to him the way he asked to be asked (preferences: "I can't find any more AI tells here, and I see some
human tells, like these... can you help show me the tells I'm missing?"):
- the evidence paragraph (block 82): my best try (try 3, AI Assisted, 0.0% AI), a card he can approve or revise;
- Scott's signal (block 83): four tries, all 100% AI, a stretch for him to edit.

  python3 articles/neuro-de-armoring/humanize/fix-20261104/cards/build_page_x1104.py
Writes REVIEW-X1104.json, .html, .artifact.html and .md here.
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
GIT_FILE = LANE + 'fix-20261104/cards/REVIEW-X1104.html'
ARTICLE = H / 'HUMANIZED-SO-FAR.md'
MD = ARTICLE.read_text(encoding='utf-8')
SHA = hashlib.sha256(MD.encode('utf-8')).hexdigest()
BL = sr.blocks(MD)
P = 'https://www.pangram.com/history/'
B082 = {1: P + 'cccbd201-be29-4717-b177-f6e88225fa3d', 2: P + '7cf017d1-316d-4488-a25e-d1d30b2e0baa',
        3: P + '97296cac-f177-4661-b7c9-b05d2cdb6e18', 4: P + '3e7be4a8-0cbc-4ca0-8e2c-04289e790009'}
B083 = {1: P + '7a3942ef-bf69-4614-a5a6-4c227e661ef4', 2: P + '3d8a3585-50e0-4b8a-85aa-f5db6e46ca29',
        3: P + '44586ae5-999d-408a-b211-051da1e2348f', 4: P + '2d363d6b-c10b-4ee8-9a0b-a484a2db8c98'}
ROUND2 = P + '3652a572-48a6-471a-9b10-180a37fabb34'
TYPES = {
    'help': {'label': 'Help me see what I\'m missing',
             'about': 'A paragraph I rewrote the way your version of "Who this is for" is built and checked by itself, '
                      'four times. It got close but not to Human (High): approve it, or revise it and show me.'},
    'stuck': {'label': 'A paragraph I can\'t get Human',
              'about': 'Four tries, each checked by itself, all 100% AI. Edit it the way you would, and I learn from it.'},
}


def block_with(s):
    hits = [b['i'] for b in BL if b['text'].startswith(s)]
    assert len(hits) == 1, (s, hits)
    return hits[0]


def main():
    i82 = block_with('The tool:Uridine monophosphate (UMP).')
    i83 = block_with("Scott's signal: Scott already had choline")
    mine82 = sr.blocks((F / 'r3' / 'blocks-try3' / '082.md').read_text(encoding='utf-8'))[0]['text']
    mine83 = sr.blocks((F / 'r3' / 'blocks' / '083.md').read_text(encoding='utf-8'))[0]['text']
    S = [
        {'id': 'Y-82', 'type': 'help', 'title': '"The tool: Uridine monophosphate (UMP). There\'s no study showing ..."',
         'advice': 'approve', 'approve_label': 'use this wording',
         'spans': [{'block': i82, 'start': 0, 'end': len(sr.block_text(BL, i82))}],
         'edits': [{'block': i82, 'before': sr.block_text(BL, i82), 'after': mine82}],
         'what': 'Your post\'s evidence paragraph, uncompressed the way your "Who this is for" is: the fragment made a '
                 'sentence, each term with its plain meaning, each study finding said plainly with its link kept.',
         'why': 'In round 2 the whole uridine section read 100% AI. One paragraph at a time, this one went 62.2%, 30.9%, '
                '0.0% and 2.6% AI in four tries; this is the third.',
         'deciding': 'Whether my wording of the evidence paragraph goes in, or your revision of it, and what my two study sentences still do that reads AI.',
         'stays': 'Every compound and the caveat ("plausible", "cautious", "extrapolation", "DAWS"); the three study links.',
         'reading': 'your post\'s uridine section, AI Generated, 100%%: [round 2](%s)' % ROUND2,
         'tested': 'this version by itself, AI Assisted, 0.0%% AI: the first and last sentences Human (High), the Wurtman '
                   'sentence Human (Low), the animal findings AI Assisted (Low): [try 3](%s); the others: [try 1](%s), '
                   '[try 2](%s), [try 4](%s)' % (B082[3], B082[1], B082[2], B082[4]),
         'advice_note': 'I can\'t find any more AI tells here, and I see some human tells, like "There\'s no study showing '
                        'that \'UMP cures DAWS\', so the best evidence we have is more basic than that" and "plus anecdotes '
                        'like Scott\'s", both Human (High). Can you help show me the tells I\'m missing in the two study '
                        'sentences in the middle?',
         'found_by': 'Paragraph checks through the API, 4 November (batches x1104a to x1104d)'},
        {'id': 'Y-83', 'type': 'stuck', 'title': '"Scott\'s signal: Scott already had choline from eggs ..."',
         'advice': 'edit', 'keep_label': 'keep it as it is',
         'spans': [{'block': i83, 'start': 0, 'end': len(sr.block_text(BL, i83))}],
         'why': 'Four tries, each by itself, all 100%% AI: the colon list split into sentences, then one joined account, '
                'then a line pointing it at the reader, then the label "Scott\'s signal:" taken off and the reasoning put '
                'in order. My last try: "%s"' % mine83,
         'reading': 'my four tries, each AI Generated, 100%%: [try 1](%s), [try 2](%s), [try 3](%s), [try 4](%s)' % (
             B083[1], B083[2], B083[3], B083[4]),
         'advice_note': 'I can\'t find any more AI tells here, and I see some human tells, like "so he wasn\'t short on '
                        'those", "fell off hard" and "the uridine looks like the piece he was missing". Can you help show me '
                        'the tells I\'m missing? Anything about Scott you add is yours to add; I won\'t make any up.',
         'found_by': 'Paragraph checks through the API, 4 November (batches x1104a to x1104d)'},
    ]
    review = {
        'format': sr.FORMAT, 'review_id': 'neuro-de-armoring-cards-20261104-x1104',
        'title': 'Neuro De-Armoring Cards, 4 November',
        'intro': [
            'Your "Who this is for" reads <b>Human Written, 0.0% AI</b> (High) by itself, and so does it with the two drug '
            'names you left out put back in brackets (question 3). I did the next two paragraphs your way, one at a time, '
            'four tries each. The evidence paragraph got close, and Scott\'s didn\'t move, so here they are, the way you '
            'asked me to ask.',
            'Your answers save as you click. When you\'re done, click <b>Copy my answers</b> (or <b>Save them as a file</b>) '
            'and send them to me.'],
        'git_file': GIT_FILE, 'article': {'file': LANE + 'HUMANIZED-SO-FAR.md', 'sha256': SHA},
        'links': {'guide': BLOB + LANE + 'HUMANIZED-SO-FAR.md', 'review': BLOB + LANE + 'fix-20261104/cards/REVIEW-X1104.md'},
        'built': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M UTC'),
        'types': TYPES, 'suggestions': S,
    }
    probs = sr.check(review, BL)
    for p in probs:
        print('PROBLEM', p)
    (HERE / 'REVIEW-X1104.json').write_text(json.dumps(review, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    if probs:
        sys.exit(1)
    page = sr.page(review, MD, BL)
    (HERE / 'REVIEW-X1104.html').write_text(page, encoding='utf-8')
    (HERE / 'REVIEW-X1104.artifact.html').write_text(sr.artifact_view(page), encoding='utf-8')
    md = ['# %s: every card' % review['title'], '',
          'The page\'s cards as text. Built %s from [your post with your versions in](%s). To answer, use the page; or write '
          'your version under a card\'s number in a message to me.' % (review['built'], review['links']['guide']), '']
    for s in S:
        md += ['## %s: %s (%s)' % (s['id'], s['title'], TYPES[s['type']]['label']), '', '*%s*' % sr.where(BL, s['spans'][0]['block']), '']
        md += ['**Pangram read:** %s' % s['reading'], '']
        if s.get('tested'):
            md += ['**This version:** %s' % s['tested'], '']
        md += ['> %s' % BL[s['spans'][0]['block']]['text'], '']
        if s.get('edits'):
            md += ['**As it would read:**', '', '> %s' % sr.blocks(s['edits'][0]['after'])[0]['text'], '']
        md += ['**Why:** %s' % s['why'], '', '**My ask:** %s' % s['advice_note'], '']
    (HERE / 'REVIEW-X1104.md').write_text('\n'.join(md) + '\n', encoding='utf-8')
    print('ok', [s['id'] for s in S])


if __name__ == '__main__':
    main()
