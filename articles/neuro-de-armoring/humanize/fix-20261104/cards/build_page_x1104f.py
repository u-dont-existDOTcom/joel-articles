"""Neuro De-Armoring Cards, 4 November (5): one card, a fix of mine on his Y-93 (his answers of 2026-11-04 22:34 UTC on
Cards (4)). His version said "like this MedlinePlus case report"; the case report is Patel and Marzella 2017 on PubMed
Central (PMC5580516, read in full in the lane's turn of 20:19 UTC), not MedlinePlus, whose page on serotonin syndrome his
version folded in. The article now reads "like this case report", with the MedlinePlus page linked on his first words,
"Serotonin syndrome" (apply_cards_x1104e.py). E348: a point that doesn't hold is changed and put to him with its reason.
His version read Human (High) in his own check; the one-word change is checked by the lane next turn (this turn's link
fetch asked for an approval nobody answered).

  python3 articles/neuro-de-armoring/humanize/fix-20261104/cards/build_page_x1104f.py
Writes REVIEW-X1104F.json, .html, .artifact.html and .md here.
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
GIT_FILE = LANE + 'fix-20261104/cards/REVIEW-X1104F.html'
ARTICLE = H / 'HUMANIZED-SO-FAR.md'
MD = ARTICLE.read_text(encoding='utf-8')
SHA = hashlib.sha256(MD.encode('utf-8')).hexdigest()
BL = sr.blocks(MD)
P = 'https://www.pangram.com/history/'
PANEL = BLOB + LANE + 'fix-20261104/panel/%s/PANEL.md'
ASK = ('I can\'t find any more AI tells here, and I see some human tells, like %s... can you help show me the tells I\'m '
       'missing? ([The readers\' notes](%s))')
TYPES = {'fix': {'label': 'A fix to your version',
                 'about': 'Something in your version that doesn\'t hold, changed in the article, with the reason. Keep '
                          'the fix, or edit the paragraph your way.'}}


def block_with(s):
    hits = [b['i'] for b in BL if b['text'].startswith(s)]
    assert len(hits) == 1, (s, hits)
    return hits[0]


def whole(i):
    return [{'block': i, 'start': 0, 'end': len(sr.block_text(BL, i))}]


def main():
    i93 = block_with('Serotonin syndrome usually comes from mixing 5-HTP casually')
    t93 = sr.block_text(BL, i93)
    a = t93.index('Reviews keep warning')
    b = t93.index('where a young guy')
    S = [
        {'id': 'Y-93b', 'type': 'fix', 'title': '"Reviews keep warning about the risk with 5-HTP, like this case report ..."',
         'advice': 'edit', 'keep_label': 'keep the fix', 'spans': [{'block': i93, 'start': a, 'end': b}],
         'reading': 'your version, with "MedlinePlus" in it, in your check: "high conf human" '
                    '([link](%s67441215-b92b-4ca5-a6ff-86941d93f7c2)). This one-word change isn\'t checked yet; I check it '
                    'next turn.' % P,
         'why': 'Your version said "like this MedlinePlus case report", but the case report isn\'t MedlinePlus\'s: it\'s '
                'Patel and Marzella 2017 on PubMed Central ([the report](https://pmc.ncbi.nlm.nih.gov/articles/PMC5580516/)). '
                'MedlinePlus was the page on what serotonin syndrome looks like, which your version folded in. So the article '
                'now says "like this case report", and the MedlinePlus page is linked on your first words, "Serotonin '
                'syndrome", where the reader meets the term. I left "Reviews keep warning ..., like this case report" as you '
                'wrote it: the reviews do warn, and the case report shows the risk they warn about.',
         'advice_note': 'Keep the fix. If you want MedlinePlus named, say where, and I\'ll check that wording.',
         'found_by': 'Reading your version beside the links it carries, 4 November'},
    ]
    review = {
        'format': sr.FORMAT, 'review_id': 'neuro-de-armoring-cards-20261104-x1104f',
        'title': 'Neuro De-Armoring Cards, 4 November (5)',
        'intro': [
            'Both of your versions from the last page are in the article. One word of your 5-HTP interactions paragraph '
            'changed, because it named the wrong source; this card says why.',
            'Your answers save as you click. When you\'re done, click <b>Copy my answers</b> (or <b>Save them as a file</b>) '
            'and send them to me.'],
        'git_file': GIT_FILE, 'article': {'file': LANE + 'HUMANIZED-SO-FAR.md', 'sha256': SHA},
        'links': {'guide': BLOB + LANE + 'HUMANIZED-SO-FAR.md', 'review': BLOB + LANE + 'fix-20261104/cards/REVIEW-X1104F.md'},
        'built': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M UTC'),
        'types': TYPES, 'suggestions': S,
    }
    probs = sr.check(review, BL)
    for p in probs:
        print('PROBLEM', p)
    (HERE / 'REVIEW-X1104F.json').write_text(json.dumps(review, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    if probs:
        sys.exit(1)
    page = sr.page(review, MD, BL)
    (HERE / 'REVIEW-X1104F.html').write_text(page, encoding='utf-8')
    (HERE / 'REVIEW-X1104F.artifact.html').write_text(sr.artifact_view(page), encoding='utf-8')
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
    (HERE / 'REVIEW-X1104F.md').write_text('\n'.join(md) + '\n', encoding='utf-8')
    print('ok', [s['id'] for s in S])


if __name__ == '__main__':
    main()
