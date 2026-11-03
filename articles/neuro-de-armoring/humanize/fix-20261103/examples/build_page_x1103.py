"""Neuro De-Armoring Cards, 3 November: three examples for Joel to rewrite (REVIEW-X1103.json, .html, .artifact.html, .md).

His answer, in the turn after his message of 2026-11-03 15:22 UTC (`../joel-20261103-1522-answers.txt`), when round 1
had read AI in 19 of 26 stretches and Emulate had no words left: "yout old me emulate doens't even pass pangram 4.1 very
well anymore so that's pointless and emulate has done so much damage to my guides that took too long to fix as you saw
with hypnosis guide. give me a couple examples i will see how to rewrite it to train you".

So three paragraphs of his post, one of each kind the article has, each read AI in the baseline and again in my round-1
rewrite (../r1/b/RESULTS.md): the science (the underpinning paragraph), a dose-and-instructions paragraph (the UMP
trial), and a list of warnings (agmatine's interactions). Each is a stretch to edit (advice "edit"), with no suggestion of
mine on it, so nothing for the owner-delivery gate. What his versions change is what round 2 learns.

  python3 articles/neuro-de-armoring/humanize/fix-20261103/examples/build_page_x1103.py
"""
import datetime
import hashlib
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
F = HERE.parent
H = F.parent
ART = H.parent
ROOT = ART.parents[1]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import suggestion_review as sr  # noqa: E402

BLOB = 'https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/community-joel-1018/'
LANE = 'articles/neuro-de-armoring/humanize/'
GIT_FILE = LANE + 'fix-20261103/examples/REVIEW-X1103.html'
MD = (H / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
MASTER_SHA = 'a4b4e05ae5b6930519e79708f0d7dbedf5cb4f9c6158bf2efd60121501fdef0f'
BL = sr.blocks(MD)
BASE = {'n1102-01': 'https://www.pangram.com/history/ddc8fda6-114b-42bc-85b6-7a82d9d0d8ab',
        'n1102-02': 'https://www.pangram.com/history/4a16dcc4-4000-4e0b-a6cc-c09b9bba32d4',
        'n1102-06': 'https://www.pangram.com/history/f04ffdea-2c78-4093-883f-fdc1b287dc37'}
R1 = {'r1-S01b': 'https://www.pangram.com/history/e5ba3763-76b8-43b1-8c66-58d4edae72b3',
      'r1-S02b': 'https://www.pangram.com/history/e11d3854-5741-41a7-94f2-82bcb5c2b86d',
      'r1-S02b-first': 'https://www.pangram.com/history/1aabde85-7988-45f3-9734-8180a1e4aff2',
      'r1-S06b': 'https://www.pangram.com/history/37568ac9-c712-406a-9ca0-f5e0801342e9'}
TYPES = {'example': {'label': 'An example to rewrite',
                     'about': 'A paragraph of your post that read AI as it is and again in my rewrite. Edit it the way you '
                              'would write it: I learn from your version and do the rest of the article the same way. Keep it '
                              'as it is if you would rather leave this one.'}}
FOUND = 'The baseline check of your post (2 November) and my round-1 rewrite (3 November), both through the API'
KEEP = 'Every dose, compound, timing and warning in it has to come out again (the check holds them), but how you say them is yours.'


def block_with(s):
    hits = [b['i'] for b in BL if b['text'].startswith(s)]
    assert len(hits) == 1, (s[:60], hits)
    return hits[0]


def card(i, title, why, reading, note):
    return {'id': 'X-%d' % i, 'type': 'example', 'title': title, 'where': sr.where(BL, i), 'advice': 'edit',
            'why': why, 'reading': reading, 'advice_note': note, 'keep_label': 'keep it as it is', 'found_by': FOUND,
            'spans': [{'block': i, 'start': 0, 'end': len(BL[i]['text'])}]}


def build_cards():
    a = block_with('Neurological De-Armoring is underpinning (not redecorating).')
    b = block_with('Trial: UMP 150–300 mg in the morning with food for 3–7 days.')
    c = block_with('Do not combine agmatine casually with opioids, kratom,')
    return [
        card(a, '“Neurological De-Armoring is underpinning (not redecorating) …”',
             'The science. In your post it read AI (High) inside Psychology is the Software. My rewrite read AI twice: '
             'first said plainly with fewer metaphors, then with your own short sentences around it put back.',
             'your post, AI (High), 47 words: [the baseline section](%s); my rewrites, AI Generated: [first](%s), '
             '[second](%s)' % (BASE['n1102-02'], R1['r1-S02b-first'], R1['r1-S02b']),
             'Edit it the way you’d explain it to a friend. ' + KEEP),
        card(b, '“Trial: UMP 150–300 mg in the morning with food for 3–7 days …”',
             'A dose with its instructions. The whole uridine section read 100% AI in your post, and again in my rewrite, '
             'which took the labels off and said each step in a sentence.',
             'your post, AI Generated, 100%%: [the baseline section](%s); my rewrite, AI Generated: [round 1](%s)' % (
                 BASE['n1102-06'], R1['r1-S06b']),
             'Edit it the way you’d tell someone to try it. ' + KEEP),
        card(c, '“Do not combine agmatine casually with opioids, kratom, …”',
             'A list of warnings. It read AI (High) in your post, in the long window over the disclaimers, and my rewrite '
             'read 100% AI with the list kept whole.',
             'your post, AI (High), in a 378-word window: [the baseline section](%s); my rewrite, AI Generated: '
             '[round 1](%s)' % (BASE['n1102-01'], R1['r1-S01b']),
             'Edit it the way you’d warn someone. ' + KEEP),
    ]


def cards_md(review):
    out = ['# %s: every card' % review['title'], '',
           'The page\'s cards as text, in the order of the article. Built %s from [your post as it stands](%s). To answer, '
           'use the page; or write your version under a card\'s number in a message to me.' % (
               review['built'], review['links']['guide']), '']
    for s in review['suggestions']:
        out += ['## %s: %s (%s)' % (s['id'], s['title'], review['types'][s['type']]['label']), '', '*%s*' % s['where'], '',
                '**Pangram read:** %s' % s['reading'], '']
        for sp in s['spans']:
            out += ['> %s' % BL[sp['block']]['text'], '']
        out += ['**Why:** %s' % s['why'], '', '**My advice:** %s' % s['advice_note'], '']
    return '\n'.join(out).replace('\n\n\n', '\n\n') + '\n'


def main():
    assert hashlib.sha256(MD.encode('utf-8')).hexdigest() == MASTER_SHA, 'the article changed'
    S = build_cards()
    review = {
        'format': sr.FORMAT, 'review_id': 'neuro-de-armoring-cards-20261103-x1103',
        'title': 'Neuro De-Armoring Cards, 3 November',
        'intro': [
            'Your neuro de-armoring post as it stands. My rewrite of every section in your voice still read AI in 19 of 26 '
            'stretches, so these are <b>three examples</b> for you to rewrite, one of each kind the article has: the science, '
            'a dose with its instructions, and a list of warnings. Each links what Pangram read.',
            'Your answers save as you click. When you\'re done, click <b>Copy my answers</b> (or <b>Save them as a file</b>) and '
            'send them to me.'],
        'git_file': GIT_FILE, 'article': {'file': LANE + 'HUMANIZED-SO-FAR.md', 'sha256': MASTER_SHA},
        'links': {'guide': BLOB + LANE + 'HUMANIZED-SO-FAR.md', 'review': BLOB + LANE + 'fix-20261103/examples/REVIEW-X1103.md'},
        'built': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M UTC'),
        'types': TYPES, 'suggestions': S,
    }
    probs = sr.check(review, BL)
    for p in probs:
        print('PROBLEM', p)
    (HERE / 'REVIEW-X1103.json').write_text(json.dumps(review, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    if probs:
        sys.exit(1)
    page = sr.page(review, MD, BL)
    (HERE / 'REVIEW-X1103.html').write_text(page, encoding='utf-8')
    (HERE / 'REVIEW-X1103.artifact.html').write_text(sr.artifact_view(page), encoding='utf-8')
    (HERE / 'REVIEW-X1103.md').write_text(cards_md(review), encoding='utf-8')
    for s in S:
        print(s['id'], s['where'])


if __name__ == '__main__':
    main()
