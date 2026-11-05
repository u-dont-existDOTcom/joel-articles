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
    i95 = block_with('If your cortisol is normal or low')
    t95 = sr.block_text(BL, i95)
    c = t95.index('In Calabrese')
    d = t95.index("So I'd trial")
    e = t95.index('with ketones')
    S = [
        {'id': 'Y-93b', 'type': 'fix', 'title': '"Reviews keep warning about the risk with 5-HTP, like this case report ..."',
         'advice': 'edit', 'keep_label': 'keep the fix', 'spans': [{'block': i93, 'start': a, 'end': b}],
         'reading': 'with "MedlinePlus" out: [Human Written, 0%%](%s3881db67-9c63-4207-9928-69655c68e7aa), High, Medium '
                    '(3 words: "Luckily he recovered."), High, the same as your version with it in '
                    '([link](%s67441215-b92b-4ca5-a6ff-86941d93f7c2)).' % (P, P),
         'why': 'Your version said "like this MedlinePlus case report", but the case report isn\'t MedlinePlus\'s: it\'s '
                'Patel and Marzella 2017 on PubMed Central ([the report](https://pmc.ncbi.nlm.nih.gov/articles/PMC5580516/)). '
                'MedlinePlus was the page on what serotonin syndrome looks like, which your version folded in. So the article '
                'now says "like this case report", and the MedlinePlus page is linked on your first words, "Serotonin '
                'syndrome", where the reader meets the term. I left "Reviews keep warning ..., like this case report" as you '
                'wrote it: the reviews do warn, and the case report shows the risk they warn about.',
         'advice_note': 'Keep the fix. If you want MedlinePlus named, say where, and I\'ll check that wording.',
         'found_by': 'Reading your version beside the links it carries, 4 November'},
        {'id': 'ATP-1', 'type': 'fix', 'title': '"In Calabrese, et al (2024), three adults on a ketogenic diet ..."',
         'advice': 'edit', 'keep_label': 'keep the change', 'spans': [{'block': i95, 'start': c, 'end': len(t95)}],
         'reading': 'the paragraph: [Human Written, 0%%](%s53b000ed-a200-44af-8eb7-051b992576a1), one window, High, on the '
                    'first try.' % P,
         'why': 'Your post said Calabrese, et al (2024) "have shown in one study that\'s part of much broader research that '
                'ketones and reduced carbohydrate intake are highly effective for anxiety, depression, and other mental '
                'illnesses". The paper is a case series of three adults on a ketogenic diet, all of whom went into full '
                'remission of depression and anxiety within 7 to 12 weeks ([the paper](https://pmc.ncbi.nlm.nih.gov/articles/'
                'PMC11182043/)). Three people can\'t show "highly effective", and it didn\'t look at other mental illnesses, '
                'so the paragraph now says what it found, and keeps your "part of much broader research". It also comes after '
                'the step it supports (the ketones), and the paragraph opens on its point: "If your cortisol is normal or low, '
                'low ATP signaling in the brain might be what\'s behind your anxiety or depression."',
         'advice_note': 'Keep the change.',
         'found_by': 'Reading both of the paragraph\'s sources before it went in (gate E348), 5 November'},
        {'id': 'ATP-2', 'type': 'fix', 'title': '"So I\'d trial 20mg of PQQ in the morning to boost ATP ..."',
         'advice': 'edit', 'keep_label': 'keep it as it is', 'spans': [{'block': i95, 'start': d, 'end': e}],
         'reading': 'in the same check as the card above ([Human Written, 0%%](%s53b000ed-a200-44af-8eb7-051b992576a1)): '
                    'High.' % P,
         'why': 'Not a change: a question about your argument, which is yours to decide. The mouse study (Wang, Gao and '
                'colleagues in JNeurosci, 2025, as [ScienceDaily](https://www.sciencedaily.com/releases/2025/11/'
                '251126025315.htm) reports it) found less ATP '
                '<i>released</i> by astrocytes in the hippocampus, through a protein called connexin 43, and restoring that '
                'protein restored the ATP and the mice\'s behavior. PQQ helps cells <i>make</i> more ATP. Whether making more '
                'means more gets released is your reasoning, not the study\'s; "I\'d trial" already says it\'s an '
                'experiment. I\'d keep it as it is.',
         'advice_note': 'Keep it as it is, unless you want to say why making more ATP should help its release.',
         'found_by': 'Reading the mouse study before the paragraph went in, 5 November'},
    ]
    review = {
        'format': sr.FORMAT, 'review_id': 'neuro-de-armoring-cards-20261104-x1104f',
        'title': 'Neuro De-Armoring Cards, 5 November',
        'intro': [
            'Both of your versions from the last page are in the article. One word of your 5-HTP interactions paragraph '
            'changed, because it named the wrong source; the first card says why. The other two are on the ATP section\'s '
            'first paragraph, now in the article: one change of a claim to what its source shows, and one question.',
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
