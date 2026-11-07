"""Neuro De-Armoring Cards, 7 November (3): the two paragraphs to teach me on.

Gate bad-trips-2026-11-07c: when no wording I try reads human, he gets the one or two paragraphs he could teach me the
most from, each with my best tested tries, and the rest stays mine and is done the way his fixes show. Section B's
humanizing pass (../RESULTS.md) read AI in four of five, after both tell panels; only the paragraph built around his own
sentence read Human.

  python3 articles/neuro-de-armoring/humanize/fix-20261107/hum/teach/build_x1107c.py
"""
import datetime
import hashlib
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
HUM = HERE.parent
H = HUM.parents[1]
ROOT = H.parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import suggestion_review as sr  # noqa: E402

BLOB = 'https://github.com/u-dont-existDOTcom/joel-articles/blob/main/'
LANE = 'articles/neuro-de-armoring/humanize/'
REL = LANE + 'fix-20261107/hum/teach/'
RESULTS = BLOB + LANE + 'fix-20261107/hum/RESULTS.md'
GIT_FILE = REL + 'REVIEW-X1107C.html'
ARTICLE = H / 'HUMANIZED-SO-FAR.md'
MD = ARTICLE.read_text(encoding='utf-8')
SHA = hashlib.sha256(MD.encode('utf-8')).hexdigest()
BL = sr.blocks(MD)
P = 'https://www.pangram.com/history/'
B037H = P + '4026db4c-d192-4673-8adc-c56d711b8087'
B038H2 = P + 'fa44a654-ae02-432f-b2aa-6dd033ca41f6'
B038S = P + '4c0e1a5b-51fe-4d93-854e-451a187daff3'
HIS38 = P + 'f2a4727d-a109-46d4-a907-40efa6350e96'
B042OK = P + '67dd2887-06b0-4c66-8ff2-dbf0bf389e24'
B039H = P + '60a9335d-05f1-4227-a6e4-9956415a2a71'
PAIR = P + '4312584e-a4de-471b-aaba-5459ffaa4cd9'
WHOSE = ('he asked: "ok fixing block 38 for you" (2026-11-07 01:00 UTC), and "i\'ll fix the first one for you ... see '
         'if you can learn something and try now" (2026-11-06 23:01 UTC)')

TYPES = {
    'teach': {'label': 'Yours to fix, so I can learn the move',
              'about': 'Every wording I tried for this paragraph read AI, after its tell panel. The card has my best '
                       'tries with what each read. Keep it as it is, or open it and write your own version.'},
}


def block(prefix):
    hits = [b['i'] for b in BL if b['text'].startswith(prefix)]
    assert len(hits) == 1, (prefix, hits)
    return hits[0]


def stretch(sid, title, i, reading, why, note):
    t = sr.block_text(BL, i)
    return {'id': sid, 'type': 'teach', 'title': title, 'advice': 'edit', 'whose': WHOSE,
            'keep_label': 'keep it as it is',
            'spans': [{'block': i, 'start': 0, 'end': len(t)}],
            'reading': reading, 'why': why, 'advice_note': note,
            'found_by': 'Section B\'s humanizing pass, 7 November ([every result and link](%s))' % RESULTS}


def main():
    i37, i38 = block('The Mechanism:'), block('The Signal Dial')
    tries37 = (HUM / 'B037h.txt').read_text(encoding='utf-8').strip()
    tries38 = (HUM / 'B038h2.txt').read_text(encoding='utf-8').strip()

    S = [
        stretch('T-37', 'The Mechanism: the science is right, the wording is still mine', i37,
                'the paragraph as it stands is my wording of the claims you approved; my humanized version of it read '
                '[AI Generated, 100%% AI, three windows (Medium 34, High 76, Medium 13)](%s)' % B037H,
                'This is the paragraph where you asked what the over-excitement was. The answer went in: the feeling '
                'follows the circuit the rise reaches, the amygdala, which is why it comes out as threat and not as '
                'joy. Then I rewrote it your way, payoff first in each sentence, terms glossed in place, the short '
                'sentences joined, and it read [AI at 100%% in three windows](%s). My version is in the card below '
                'this line.' % B037H + '  What I can\'t get is the voice of a mechanism paragraph: every sentence of mine lands as a '
                'finished step with its citation, and both panel readers said the same thing about the rhythm.',
                'If you fix this one, the move I\'d carry to blocks 39, 40 and 41, which read AI too '
                '([39](%s), [40 and 41](%s)), is whatever you do to break that step-by-step rhythm. Here is my try, '
                'to edit or to ignore:\n\n%s' % (B039H, PAIR, tries37)),
        stretch('T-38', 'The Signal Dial: your version read Human, mine with the corrected science reads AI', i38,
                'the paragraph as it stands is the corrected science you approved (SB-38b); my humanized version of it '
                'read [AI Generated, 100%% AI, one window at High](%s), and the science draft before it read '
                '[AI, Low](%s). Your own version of the old wording read [Human, High after the label sentence](%s)'
                % (B038H2, B038S, HIS38),
                'This is the clearest comparison we have. On 7 November you turned this paragraph Human with three '
                'moves on the old science: "well" for "according to", uncompressing the last sentence, and the '
                'question as the opener. I kept all three, carried the corrected claims in (GluD is a channel, the '
                'leak is what shows up in people, the armor part is a guess with a mechanism), ran the tell panel, cut '
                'everything the two readers agreed on, and it still read AI at High across the whole paragraph. So '
                'what carries your voice in this paragraph isn\'t those three moves on their own, and I can\'t see '
                'what it is.',
                'This is the one I\'d most like you to fix, because it is the same paragraph you already fixed once, '
                'so your two versions side by side would show me what I lost when the claims changed. Mine is below, '
                'and the claims in it are the ones you approved, so keep those and change the words:\n\n%s' % tries38),
    ]
    review = {
        'format': 'joel-suggestion-review-v1',
        'review_id': 'neuro-de-armoring-cards-20261107-x1107c',
        'title': 'Neuro De-Armoring Cards, 7 November (3): two paragraphs to teach me on',
        'intro': [
            'Section B\'s science is settled and in the article, all seven claims plus your three rewrites. The '
            'humanizing pass after it went badly: four of five read AI at 100%% after both tell panels, '
            '[the Mechanism](%s), [the Signal Dial](%s), [D-serine and DCS](%s) and [the Brake with the Lock](%s) '
            '([every result and link](%s)).' % (B037H, B038H2, B039H, PAIR, RESULTS),
            'The one that read Human is the one I barely touched: block 42 kept your own sentence from 6 November word '
            'for word and only split my stacked clause in two ([Human, High](%s)). It is in the article.' % B042OK,
            'So these two are yours if you want them, the two I\'d learn the most from. Blocks 39, 40 and 41 are '
            'still mine and I\'ll do them the way your fix here shows, rather than trying another wording of my own.',
            'No claim changes on this page: the science in both paragraphs is what you approved today.',
        ],
        'git_file': GIT_FILE,
        'article': {'file': LANE + 'HUMANIZED-SO-FAR.md', 'sha256': SHA},
        'built': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
        'links': {'guide': BLOB + LANE + 'HUMANIZED-SO-FAR.md', 'review': BLOB + REL + 'REVIEW-X1107C.md'},
        'types': TYPES,
        'suggestions': S,
    }
    probs = sr.check(review, BL)
    for x in probs:
        print('PROBLEM', x)
    (HERE / 'REVIEW-X1107C.json').write_text(json.dumps(review, indent=1, ensure_ascii=False) + '\n',
                                             encoding='utf-8')
    if probs:
        return 1
    page = sr.page(review, MD, BL)
    (HERE / 'REVIEW-X1107C.html').write_text(page, encoding='utf-8')
    (HERE / 'REVIEW-X1107C.artifact.html').write_text(sr.artifact_view(page), encoding='utf-8')
    md = ['# %s' % review['title'], ''] + [p + '\n' for p in review['intro']]
    for s in S:
        md += ['## %s: %s (%s)' % (s['id'], s['title'], TYPES[s['type']]['label']), '',
               '*%s*' % sr.where(BL, s['spans'][0]['block']), '',
               '**In the article now:**', '', '> %s' % sr.block_text(BL, s['spans'][0]['block']), '',
               '**Pangram read:** %s' % s['reading'], '', '**Why it comes to you:** %s' % s['why'], '',
               '**My ask:** %s' % s['advice_note'], '']
    (HERE / 'REVIEW-X1107C.md').write_text('\n'.join(md) + '\n', encoding='utf-8')
    print('ok', [x['id'] for x in S])
    return 0


if __name__ == '__main__':
    sys.exit(main())
