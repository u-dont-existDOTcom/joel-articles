#!/usr/bin/env python3
"""REVIEW.json for batch 7: the two windows left in the stacks section, marked on r09 (his batch-6 answers in). In the
section's own check his start-low and doctor paragraphs read AI though they read Human Written, 100% as a pair in his
check; my two tries (a move, then a referent) didn't fix it. One question about his "That said" after my P1, which two
fresh readers asked. No API calls."""
import hashlib, json, pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent
R09 = HERE.parent
REPO = HERE.parents[5]
sys.path.insert(0, str(REPO / 'tools' / 'humanization'))
import suggestion_review as sr  # noqa: E402

MD = R09 / 'r09.md'
bl = sr.blocks(MD.read_text(encoding='utf-8'))
GH = 'https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/gut-r07-20261104/articles/healing-the-gut/humanize/fix-20261103/'
H = 'https://www.pangram.com/history/'


def find(start):
    i = [b['i'] for b in bl if b['text'].startswith(start)]
    assert len(i) == 1, start
    return i[0]


sl, doc, his, p1 = find('Start any kit at a low dose'), find('Some severe symptoms warrant'), find('That said, some people'), find("I don't think there's one supplement stack")
S = [
 {'id': 'F7-1', 'type': 'help', 'title': 'Start low and the doctor paragraph, in the whole section', 'advice': 'edit',
  'spans': [{'block': sl, 'start': 0, 'end': len(bl[sl]['text'])}, {'block': doc, 'start': 0, 'end': len(bl[doc]['text'])}],
  'why': 'Your two paragraphs read [Human Written, 100%](' + H + '6b3c14e0-d672-43be-9717-81af23861d75?ucc=4rq5Ko7gBiW) '
         'together. In the whole section (with your kits and everything else in), the section read [AI Detected, 18% AI]('
         + H + '3217da78-355a-4536-a491-004ef95ca3cd), and the only AI windows were here: "Start any kit at a low dose and '
         'build up as your gut gets used to it." (AI Low), "The prebiotic part especially can give you gas at first..." (AI '
         'Low), "If your immune system is weak..." (AI Low) and "If you have an IBD flare, cancer or another serious '
         'illness..." (AI Medium). Everything above them read Human, High mostly. Two of those four sentences are mine that '
         'you kept (the first and the last). I tried two things, each with its own section check: moving start low up to '
         'right after the kits, no word changed, which re-segmented the whole section and made it worse ([AI Detected, 52% '
         'AI](' + H + '05f663cd-bc40-4317-b7fb-1e280ed4a6bd); even P1 flipped); and "Start any of those repair kits", since '
         'after the cleanse stacks "any kit" can mean a cleanse kit ([AI Detected, 20% AI](' + H + '4e9d0cb3-3679-474d-a4b5-9b4971e6c002); '
         'the start-low sentences stayed AI Low and the pregnancy sentence went AI Low too). I can\'t find any more AI tells '
         'here, and I see some human tells, like these: "black & tarry, not red like from lower GI", "Take it seriously if '
         'you notice blood in your stool", "since gas is what your bacteria make". Can you help show me the tells I\'m '
         'missing?',
  'advice_note': 'Rewrite either paragraph with Edit, or tell me what to look at. The article check waits until these read '
                 'Human in the section (your rule of 14:41 UTC, E354).',
  'reading': 'The section in your order: [AI Detected, 18% AI](' + H + '3217da78-355a-4536-a491-004ef95ca3cd) (Human High 244, '
             'Human Low 1, Human High 58, Human Medium 19, Human High 75, AI Low 17, AI Low 39, Human High 46, Human Medium 21, '
             'Human Low 14, AI Low 26, AI Medium 26).'},
 {'id': 'F7-2', 'type': 'help', 'title': 'Does your "That said" still follow?', 'advice': 'ask',
  'spans': [{'block': his, 'start': 0, 'end': len('That said')}],
  'question': 'Two fresh readers asked what your "That said" pulls back from. It concedes against "I don\'t think there\'s one '
              'supplement stack that heals everyone\'s gut", but my P1 (F6-1) now ends between them on "Then a stack can help '
              'with the rebuilding in Phase 5". Leave it, or should P1\'s last sentence go somewhere else?',
  'why': 'P1 and your three categories read [Human Written, 100%](' + H + 'f24f66fe-78b9-4edc-91c7-a7ee15934ea4?ucc=4rq5Ko7gBiW) '
         'together, so this is about the sense, not Pangram. Your "That said" sentence read Human Low by itself in an earlier '
         'check ([Human, Low and High](' + H + 'db2815e1-22ed-4439-811e-fc225390ab14)).'},
]
review = {
    'format': 'joel-suggestion-review-v1', 'review_id': 'healing-the-gut-b7-stacks-20261104',
    'title': 'Gut Stacks, the Last Windows',
    'intro': ['Your batch-6 answers are in word for word (r09). The section went from 5% human to 18% AI in its own check; '
              'every window before your start-low paragraph reads Human. What\'s left is two paragraphs, which read Human by '
              'themselves, and one question about "That said".',
              'From your answers: a fresh reader now reads every draft itself before a check, so a word changed for a newcomer '
              'can\'t break the sentence around it ("three kits" and your "but"), and "that" or "it" has to point somewhere '
              'clear (E355, enforced).'],
    'git_file': 'articles/healing-the-gut/humanize/fix-20261103/r09/b7/REVIEW-PAGE.html',
    'article': {'file': 'articles/healing-the-gut/humanize/fix-20261103/r09/r09.md', 'sha256': hashlib.sha256(MD.read_bytes()).hexdigest()},
    'built': '2026-11-04',
    'links': {'guide': GH + 'r09/r09.md', 'review': GH + 'r09/b7/REVIEW-CARDS.md'},
    'types': {'help': {'label': 'Your help', 'about': 'Reads Human alone, AI in the section'}},
    'suggestions': S,
}
(HERE / 'REVIEW.json').write_text(json.dumps(review, ensure_ascii=False, indent=1), encoding='utf-8')
out = ['# ' + review['title'], ''] + [p + '\n' for p in review['intro']]
for s in S:
    out += ['## %s. %s' % (s['id'], s['title']), '']
    if s.get('question'):
        out += ['**Question:** ' + s['question'], '']
    out += ['**Why:** ' + s['why'], '']
    if s.get('advice_note'):
        out += ['**What I\'d like:** ' + s['advice_note'], '']
    if s.get('reading'):
        out += [s['reading'], '']
(HERE / 'REVIEW-CARDS.md').write_text('\n'.join(out), encoding='utf-8')
print(len(S), 'cards')
