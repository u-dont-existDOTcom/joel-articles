"""Neuro De-Armoring Cards, 6 November: the dynorphin paragraph, yours to write.

His answer to DFB-2 (2026-11-06 16:35 UTC) sent the paragraph back to its original wording: "you've added something here
but now it's not really clear what is doing what for the reader. 'the two aren't one mechanism' doesn't give useful
info, are you able to understand that? what do we need to know? make it all make sense".

Two tries at saying what each of the two does both read AI Detected, 100% AI, one window at High, in his account's web
app. So the paragraph goes to him as a stretch to edit (advice "edit"), the route for a stretch my versions can't carry
(AGENTS.md: "where my versions keep reading AI, a few examples go to him to rewrite on the marking page"; gates E291 and
E333). His original stays in the article meanwhile, untouched.

His other three answers are already in (apply_dfb.py beside this). The schema finding from this turn (SCHEMA-CHECK.md)
is question 10 on the questions page, not a card: it would change what the article argues, which is his (gate E348).

  python3 articles/neuro-de-armoring/humanize/fix-20261106/build_page_x1106a.py
Writes REVIEW-X1106A.json, .html, .artifact.html and .md in cards/ here.
"""
import datetime
import hashlib
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
CARDS = HERE / 'cards'
H = HERE.parent
ROOT = H.parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import suggestion_review as sr  # noqa: E402

BRANCH = 'claude/community-joel-1018'
BLOB = 'https://github.com/u-dont-existDOTcom/joel-articles/blob/%s/' % BRANCH
LANE = 'articles/neuro-de-armoring/humanize/'
REL = LANE + 'fix-20261106/'
GIT_FILE = REL + 'cards/REVIEW-X1106A.html'
SCHEMA = BLOB + REL + 'SCHEMA-CHECK.md'
ARTICLE = H / 'HUMANIZED-SO-FAR.md'
MD = ARTICLE.read_text(encoding='utf-8')
SHA = hashlib.sha256(MD.encode('utf-8')).hexdigest()
BL = sr.blocks(MD)

P = 'https://www.pangram.com/history/'
TRY1 = P + '6e5452c4-3a59-480a-ae28-b9370928c6f5'
TRY2 = P + '3bd08080-1b34-43f9-be56-fbb5171d08de'
ZACH = 'https://pubmed.ncbi.nlm.nih.gov/16415864/'

TYPES = {
    'help': {'label': 'Yours to write',
             'about': 'The paragraph is missing something the reader needs, and nothing I wrote to add it reads Human. '
                      'Keep it as it is, or open it and write your own version.'},
}


def main():
    hits = [b['i'] for b in BL if b['text'].startswith('The Problem: To protect itself')]
    assert len(hits) == 1, hits
    i46 = hits[0]
    t46 = sr.block_text(BL, i46)

    S = [{
        'id': 'DFB-2b', 'type': 'help',
        'title': 'The section names two things in its heading and only says what one of them does',
        'advice': 'edit', 'keep_label': 'keep it as it is',
        'spans': [{'block': i46, 'start': 0, 'end': len(t46)}],
        'reading': 'my two tries, not your paragraph: [AI Detected, 100%% AI, one window at High](%s) and '
                   '[the same again](%s). Your paragraph on its own is under the web app\'s 50-word minimum, so it '
                   'has no reading of its own yet.' % (TRY1, TRY2),
        'what': 'Nothing, unless you write it. Your paragraph stays exactly as it is.',
        'why': 'You were right that "the two aren\'t one mechanism" told the reader nothing -- it was a fact about the '
               'literature, not about them. What they need is which of the two is doing the gray they are in, and what '
               'it means when the gray lifts, because the obvious reading is that the gray lifting means the armor is '
               'off, and that is where someone stops early. I tried twice to add that in two sentences. Both read '
               '[AI Detected, 100%% AI, one window at High](%s) and [again at High](%s). The first tried to explain '
               'the article\'s own structure to the reader ("that is the state you are in now ... which is why the '
               'timeline gives them separate phases"); the second dropped the structure talk and ended on a concrete '
               'instruction, and read the same. So the shape is mine, not the vocabulary, and a third try from me '
               'isn\'t the thing to spend your page on.' % (TRY1, TRY2),
        'stays': 'The whole paragraph, word for word -- dynorphin as the chemical blanket, the Void and its three '
                 'signs. Nothing is cut, and nothing changes if you keep it as it is.',
        'deciding': 'Whether the reader is told here that dynorphin is the state and DeltaFosB is the slower setting '
                    'under it, or whether that belongs later where the phases are, or not at all.',
        'advice_note': 'If you do write it, the two things worth landing are that dynorphin is what makes the gray, '
                       'and that the two don\'t clear together, so a better week isn\'t the armor coming off. One '
                       'thing to keep off the page: in the opiate work DeltaFosB in the accumbens represses dynorphin '
                       'rather than driving it ([Zachariou, et al, 2006](%s)), so they can\'t be written as one '
                       'mechanism -- but that is opiate work, not trauma work, so the reverse isn\'t a claim to make '
                       'either.' % ZACH,
        'found_by': 'Your answer to DFB-2, two paragraph checks in your account\'s web app, and the dynorphin check '
                    'in [this turn\'s pass](%s)' % SCHEMA,
    }]

    review = {
        'format': 'joel-suggestion-review-v1',
        'review_id': 'neuro-de-armoring-cards-20261106-x1106a',
        'title': 'Neuro De-Armoring Cards, 6 November: the dynorphin paragraph',
        'intro': [
            'One card, and it is yours to write rather than mine to propose.',
            'Your other three DeltaFosB answers are already in the article as you wrote them, including the loop '
            'sentence. That one was the point I had missed, and it is the right form of it: the protein lasts weeks, '
            'the loop is what is permanent.',
            'Separately, I checked your schema idea. It holds up better than my "weeks, not permanent" allowed, and '
            'the mechanism runs the other way round from cementing: DeltaFosB piles up in the cells that just fired '
            'and stops them switching on the gene they need to learn anything new, and in one study that pile-up in '
            'the amygdala and dentate gyrus went with mice that could not extinguish fear. That is question 10 on the '
            'questions page rather than a card, because it changes what the article argues. '
            '[The pass is here](%s).' % SCHEMA,
            'No compound, dose, unit, timing or warning is touched by any of this.',
        ],
        'git_file': GIT_FILE,
        'article': {'file': LANE + 'HUMANIZED-SO-FAR.md', 'sha256': SHA},
        'built': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
        'links': {'guide': BLOB + LANE + 'HUMANIZED-SO-FAR.md', 'review': BLOB + GIT_FILE},
        'types': TYPES,
        'suggestions': S,
    }
    CARDS.mkdir(parents=True, exist_ok=True)
    probs = sr.check(review, BL)
    for x in probs:
        print('PROBLEM', x)
    (CARDS / 'REVIEW-X1106A.json').write_text(json.dumps(review, indent=1, ensure_ascii=False) + '\n',
                                              encoding='utf-8')
    if probs:
        return 1
    page = sr.page(review, MD, BL)
    (CARDS / 'REVIEW-X1106A.html').write_text(page, encoding='utf-8')
    (CARDS / 'REVIEW-X1106A.artifact.html').write_text(sr.artifact_view(page), encoding='utf-8')
    s = S[0]
    md = ['# %s: the card' % review['title'], ''] + list(review['intro']) + [
        '', '## %s: %s (%s)' % (s['id'], s['title'], TYPES[s['type']]['label']), '',
        '*%s*' % sr.where(BL, s['spans'][0]['block']), '',
        '> %s' % t46, '',
        '**What changes:** %s' % s['what'], '',
        '**Why:** %s' % s['why'], '',
        '**What stays:** %s' % s['stays'], '',
        '**You\'re deciding:** %s' % s['deciding'], '',
        '**My ask:** %s' % s['advice_note'], '']
    (CARDS / 'REVIEW-X1106A.md').write_text('\n'.join(md) + '\n', encoding='utf-8')
    print('ok', [x['id'] for x in S])
    return 0


if __name__ == '__main__':
    sys.exit(main())
