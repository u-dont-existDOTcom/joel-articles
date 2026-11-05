"""Neuro De-Armoring Cards, 5 November (2): the ATP section's two ketone-strategy paragraphs, which read AI in three tries
each and after the tell panel (checks x1105a to x1105c; ../panel/x1105-ketone/PANEL.md). His to rewrite, the way his
5-HTP versions showed (gate E333: where my versions keep reading AI, a few examples go to him). A new page with its own
review id, so nothing he answered on the last page is asked again (his answer of 15:55 UTC on Y-93b: "already said keep
this fix in last turn?").

  python3 articles/neuro-de-armoring/humanize/fix-20261104/cards/build_page_x1105b.py
Writes REVIEW-X1105B.json, .html, .artifact.html and .md here.
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
GIT_FILE = LANE + 'fix-20261104/cards/REVIEW-X1105B.html'
ARTICLE = H / 'HUMANIZED-SO-FAR.md'
MD = ARTICLE.read_text(encoding='utf-8')
SHA = hashlib.sha256(MD.encode('utf-8')).hexdigest()
BL = sr.blocks(MD)
P = 'https://www.pangram.com/history/'
PANEL = BLOB + LANE + 'fix-20261104/panel/%s/PANEL.md'
ASK = ('I can\'t find any more AI tells here, and I see some human tells, like %s... can you help show me the tells I\'m '
       'missing? ([The readers\' notes](%s))')
TYPES = {'help': {'label': 'Help me see what I\'m missing',
                  'about': 'A paragraph my tries couldn\'t get to read Human. Edit it the way you would, or keep it as '
                           'it is.'},
         'fix': {'label': 'A fix to your version',
                 'about': 'Something in your version that doesn\'t hold, changed in the article, with the reason. Keep '
                          'the fix, or edit the paragraph your way.'}}


def block_with(s):
    hits = [b['i'] for b in BL if b['text'].startswith(s)]
    assert len(hits) == 1, (s, hits)
    return hits[0]


def whole(i):
    return [{'block': i, 'start': 0, 'end': len(sr.block_text(BL, i))}]


def main():
    i1 = block_with('You must pick one of two ketone strategies')
    i2 = block_with('For the long run there')
    pan = BLOB + LANE + 'fix-20261104/panel/x1105-ketone/PANEL.md'
    S = [
        {'id': 'K-1', 'type': 'help', 'title': '"You must pick one of two ketone strategies ..."',
         'advice': 'edit', 'keep_label': 'keep it as it is', 'spans': whole(i1),
         'reading': 'three tries, checked with the next paragraph (it is 40 words, under Pangram\'s 50): [100%% AI](%s24187764-'
                    '991e-4d12-8072-963e7219314e), [100%%](%sd4a60ac2-e97c-4522-a960-b206aaf8eb73), and this one, '
                    '[100%%](%s2d2d6dc2-2232-4460-8b86-751f044f80a3) (AI High on the first sentence, Low on the last).' % (P, P, P),
         'why': 'Your post had "KETONE DECISION: You must choose your fuel strategy. This determines your electrolyte '
                'protocol." and "Strategy A: The \"Crisis Mode\" ... Method: You eat a standard low-sugar diet but drink '
                'Ketones (BHB Salts) to clear the fog." What I changed for sense: why the choice touches the electrolytes '
                '(BHB salts bring their own sodium, and a keto diet drains it, which is why your Part 3 says not to load extra '
                'salt on Strategy A), and Strategy A said by the case it is for. The names Strategy A and "Crisis Mode" stay, '
                'because Part 3 and the timeline refer back to them. ' + (ASK % ('"need the fog gone fast"', pan)),
         'advice_note': 'Edit it your way; it stays as it is in the article meanwhile.',
         'found_by': 'This turn\'s checks in your account, 5 November'},
        {'id': 'K-2', 'type': 'help', 'title': '"For the long run there\'s Strategy B, the \"Resilience Mode\" ..."',
         'advice': 'edit', 'keep_label': 'keep it as it is', 'spans': whole(i2),
         'reading': 'three tries: [100%% AI](%s94d586d1-bab4-40c9-9ff8-fc5240043f75), [70%%](%sa6cec41f-20a3-4a13-86ff-'
                    '6e09a28ca63d) and this one, [71%%](%s2c76e3b4-deac-493c-9aab-a5affbedfb1e): the first sentence Human '
                    '(Medium), then "That only works if fat becomes your fuel ..." AI Low, the protein warning AI High and the '
                    'guide line AI Medium.' % (P, P, P),
         'why': 'Your post had "Strategy B: The \"Resilience Mode\" (Keto Diet) Method: You restrict carbs (<20g/day) to '
                'force your liver to produce Ketones.", "Fat: EAT FAT TO SATIETY. This is your new energy source. Do not rely '
                'on lean protein alone (chicken breast), or your body will convert the protein to sugar (Gluconeogenesis), '
                'keeping you out of ketosis." and the Keto Adaptation Guide line. What I changed for sense: Strategy B said as '
                'the long-run one (your timeline moves people to it "for long-term repair"), the protein warning said as '
                'what it is instead of ("Don\'t fill up on lean protein ... instead"), and the side effects named as the keto '
                'flu. The protein warning is the part that won\'t move. ' + (ASK % ('"eat fat until you\'re full"', pan)),
         'advice_note': 'Edit it your way, the protein warning especially; it stays as it is in the article meanwhile.',
         'found_by': 'This turn\'s checks in your account, 5 November'},
    ]
    review = {
        'format': sr.FORMAT, 'review_id': 'neuro-de-armoring-cards-20261105-x1105b',
        'title': 'Neuro De-Armoring Cards, 5 November (2)',
        'intro': [
            'Your ATP-2 version is in the article (Human, High). The next two paragraphs, the two ketone strategies, still '
            'read AI after three tries each; these two cards ask for your versions.',
            'Your answers save as you click. When you\'re done, click <b>Copy my answers</b> (or <b>Save them as a file</b>) '
            'and send them to me.'],
        'git_file': GIT_FILE, 'article': {'file': LANE + 'HUMANIZED-SO-FAR.md', 'sha256': SHA},
        'links': {'guide': BLOB + LANE + 'HUMANIZED-SO-FAR.md', 'review': BLOB + LANE + 'fix-20261104/cards/REVIEW-X1105B.md'},
        'built': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M UTC'),
        'types': TYPES, 'suggestions': S,
    }
    probs = sr.check(review, BL)
    for p in probs:
        print('PROBLEM', p)
    (HERE / 'REVIEW-X1105B.json').write_text(json.dumps(review, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    if probs:
        sys.exit(1)
    page = sr.page(review, MD, BL)
    (HERE / 'REVIEW-X1105B.html').write_text(page, encoding='utf-8')
    (HERE / 'REVIEW-X1105B.artifact.html').write_text(sr.artifact_view(page), encoding='utf-8')
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
    (HERE / 'REVIEW-X1105B.md').write_text('\n'.join(md) + '\n', encoding='utf-8')
    print('ok', [s['id'] for s in S])


if __name__ == '__main__':
    main()
