"""Neuro De-Armoring Cards, 4 November (3): six stretches to edit, after the lane's checks in Pangram's web app (Joel,
2026-11-04 16:12 UTC: "you don't need me to do that ... every other lane is doing gui checks"; gate E356).

- Blocks 85, 86, 89 and 91 (the uridine stop signs and psychedelic caution, the 5-HTP tool and trial): two tries of mine
  and Codex's rewrite (the writer of another family, E256 (Inner Child)) read AI by themselves; the tell panel on each
  is linked (E253). His post's paragraph is the one he edits; the cards give my best try and its reading.
- Block 88 (the 5-HTP "Who this is for", my second try, in the article): Human Written with its last two sentences Low;
  the one-sentence fix moved every window and read AI Detected, so the stretch is his (E350).
- Block 90 (Scott's 5-HTP and P5P): my try read AI Detected with only its last sentence AI (Low); the one-sentence fix
  turned the untouched sentences AI (E350).
Each ask is in his words (E253): "I can't find any more AI tells here, and I see some human tells, like these... can you
help show me the tells I'm missing?", with the human tells I see (his words, a fact he gave, a rough edge: E251).

  python3 articles/neuro-de-armoring/humanize/fix-20261104/cards/build_page_x1104d.py
Writes REVIEW-X1104D.json, .html, .artifact.html and .md here.
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
GIT_FILE = LANE + 'fix-20261104/cards/REVIEW-X1104D.html'
ARTICLE = H / 'HUMANIZED-SO-FAR.md'
MD = ARTICLE.read_text(encoding='utf-8')
SHA = hashlib.sha256(MD.encode('utf-8')).hexdigest()
BL = sr.blocks(MD)
P = 'https://www.pangram.com/history/'
PANEL = BLOB + LANE + 'fix-20261104/panel/%s/PANEL.md'
ASK = ('I can\'t find any more AI tells here, and I see some human tells, like %s... can you help show me the tells I\'m '
       'missing? ([The readers\' notes](%s))')
URIDINE = '[its section, AI Generated, 100.0%% AI](%sf04ffdea-2c78-4093-883f-fdc1b287dc37)' % P
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
    i85 = block_with('Side effects / stop signs: In practice, the most common problem')
    i86 = block_with('Psychedelic caution: If UMP makes dreams vivid')
    i88 = block_with('Who this is for: 5-HTP is not for every depressed person either.')
    i89 = block_with('The tool:5-HTP bypasses')
    i90 = block_with('Scott\'s version: 100 mg 5-HTP')
    i91 = block_with('Trial: Start lower if you are sensitive')
    t88 = sr.block_text(BL, i88)
    low = t88.index('It makes more sense if there\'s also')
    S = [
        {'id': 'Y-85', 'type': 'help', 'title': '"Side effects / stop signs: In practice, the most common problem is the "choline headache" ..."',
         'advice': 'edit', 'keep_label': 'keep it as it is', 'spans': whole(i85),
         'reading': 'your post\'s version, in the baseline: %s' % URIDINE,
         'why': 'Three versions read 100%% AI by themselves in Pangram: my [first](%sf8f019d8-fd62-42bd-8a2a-129a55b7d3dc) and '
                '[second](%s2627124f-1cc3-4582-8fc1-c6815a2d7006), and Codex\'s rewrite '
                '([third](%s25723773-0dc0-47cd-937b-545dd60d3b93)), which put the case first and the reason last. The three '
                'readers flagged the label opener, the even symptom list, the "wired, numb, or weirdly irritable" triplet and its '
                'closing instruction, and the build: claim, caveat, mechanism, list, instruction ([their notes](%s)). The lists '
                'are the protocol\'s, so all eight stop signs stay.' % (P, P, P, PANEL % 'b085-n2'),
         'advice_note': ASK % ('"weirdly irritable" and the "choline headache"', PANEL % 'b085-n2'),
         'found_by': 'Paragraph checks in Pangram\'s web app, 4 November (batches x1104k and x1104m), and the API before it ran out (x1104j)'},
        {'id': 'Y-86', 'type': 'help', 'title': '"Psychedelic caution: If UMP makes dreams vivid or suddenly lowers psychedelic tolerance ..."',
         'advice': 'edit', 'keep_label': 'keep it as it is', 'spans': whole(i86),
         'reading': 'your post\'s version, in the baseline: %s' % URIDINE,
         'why': 'My two versions read 100%% AI ([first](%s6e54db82-deb2-4bc5-afe6-913107aa485e), '
                '[second](%s71f224dd-2467-40d7-823e-d4ecba72035b)). Codex\'s came closest, AI Detected, 39.4%% AI '
                '([third](%sb7361905-0595-40c0-a14f-e3c0abea6628)): "Psychedelic caution: Say your dreams get vivid again on UMP. '
                'Take that as a warning that your sensitivity may be returning. The same goes if UMP suddenly lowers your '
                'psychedelic tolerance. Don\'t take UMP on psychedelic days." read Human (Medium, then Low, Low), and its last two '
                'sentences AI (Low): "If you use psychedelics later, assume your old dose may be too strong. You can end up taking '
                'too much trying to get the visuals you remember." The readers\' notes on my second: [here](%s).'
                % (P, P, P, PANEL % 'b086-n2'),
         'advice_note': ASK % ('"chasing the old visual threshold can overshoot" and "Do not take UMP on psychedelic days"', PANEL % 'b086-n2'),
         'found_by': 'Paragraph checks in Pangram\'s web app, 4 November (batches x1104k and x1104m), and the API before it ran out (x1104j)'},
        {'id': 'Y-88', 'type': 'help', 'title': '"It makes more sense if there\'s also a genetic or clinical reason ..."',
         'advice': 'edit', 'keep_label': 'keep it as it is', 'spans': [{'block': i88, 'start': low, 'end': len(t88)}],
         'reading': 'the paragraph by itself, Human Written, 0.0%% AI: Medium, High, Medium, then Low on these two sentences '
                    '([check](%s8d2d4cf1-13da-4c6c-83ae-eddb774ef930))' % P,
         'why': 'This is my second try, now in the article, built the way your uridine "Who this is for" is ("It could help, '
                'though, ..."). Changing only the last sentence, giving the article\'s reasons in brackets, read AI Detected, '
                '13.8%% AI, with every window moved ([check](%s4079bcd3-65eb-43f8-97bb-ec8436fc5f19)), so the stretch is yours '
                '(E350). The readers\' notes on my first try: [here](%s).' % (P, PANEL % 'b088-n1'),
         'advice_note': ASK % ('your "low-serotonin-looking" and Scott\'s TPH2 bottleneck', PANEL % 'b088-n1'),
         'found_by': 'Paragraph checks in Pangram\'s web app, 4 November (batches x1104k and x1104l)'},
        {'id': 'Y-89', 'type': 'help', 'title': '"The tool:5-HTP bypasses the tryptophan-to-5-HTP step ..."',
         'advice': 'edit', 'keep_label': 'keep it as it is', 'spans': whole(i89),
         'reading': 'your post\'s version, in the baseline: %s' % HTP,
         'why': 'Three versions read 100%% AI: my [first](%s6f01153b-25fa-4bec-900f-7ed9102c81be) and '
                '[second](%s07a72325-fa0a-4478-91cd-cd46c866e1fa), and Codex\'s ([third](%sde493dec-a509-4688-ab16-bf60bde8adb7)). '
                'The readers flagged "discusses its role in", the list of uses and the "mixed ... but real enough" verdict '
                '([their notes](%s)). One fix of meaning is in my tries: the review treats serotonin syndrome as a risk of 5-HTP '
                '(its sections 8.2.1 and 9), not one of its uses, so they say "the serotonin-toxicity risk".'
                % (P, P, P, PANEL % 'b089-n2'),
         'advice_note': ASK % ('your "people online"', PANEL % 'b089-n2'),
         'found_by': 'Paragraph checks in Pangram\'s web app, 4 November (batches x1104k and x1104m), and the API before it ran out (x1104j)'},
        {'id': 'Y-90', 'type': 'help', 'title': '"Scott\'s version: 100 mg 5-HTP sublingually at night ..."',
         'advice': 'edit', 'keep_label': 'keep it as it is', 'spans': whole(i90),
         'reading': 'your post\'s version, in the baseline: %s' % HTP,
         'why': 'My version read AI Detected, 27.2%% AI ([check](%s6343d2c6-2a62-473a-b8c9-52fd8059a3f0)): "Scott took 100 mg '
                '5-HTP sublingually at night, with 10–20 mg P5P sublingually in the morning." Human (High); "The P5P isn\'t there '
                'as a stimulant, but as the active form of B6, which the enzyme that turns 5-HTP into serotonin (aromatic '
                'amino-acid decarboxylase) needs." Human (Medium); "He\'s slow-COMT and sensitive to too much P5P, so the low dose '
                'matters, and more isn\'t better." AI (Low). Changing only that last sentence turned the first two AI as well '
                '([check](%se0a823e1-b205-4120-971a-bd4ad47a7d16)), so the stretch is yours (E350); you can start from my '
                'version.' % (P, P),
         'advice_note': ASK % ('"Scott is slow-COMT"', PANEL % 'b090-n1'),
         'found_by': 'Paragraph checks in Pangram\'s web app, 4 November (batches x1104k and x1104l)'},
        {'id': 'Y-91', 'type': 'help', 'title': '"Trial: Start lower if you are sensitive: 50 mg 5-HTP at night ..."',
         'advice': 'edit', 'keep_label': 'keep it as it is', 'spans': whole(i91),
         'reading': 'your post\'s version, in the baseline: %s' % HTP,
         'why': 'Three versions read 100%% AI: my [first](%s0c28bab4-9e88-4c8c-b995-82d72c7067d8), my '
                '[second](%s0250acd1-dd68-48f8-a284-bdd074678d54), built the way your uridine trial is, and Codex\'s '
                '([third](%sea357474-7e94-4d66-9008-1e14dc1efdfe)). The readers flagged the four-item list of first signs, the '
                'bracketed list of what not to combine and the stepwise build ([their notes](%s)). Both lists are the '
                'protocol\'s, so the five things not to combine and the four first signs stay.' % (P, P, P, PANEL % 'b091-n2'),
         'advice_note': ASK % ('"almost works" and "not converting cleanly"', PANEL % 'b091-n2'),
         'found_by': 'Paragraph checks in Pangram\'s web app, 4 November (batches x1104k, x1104l and x1104m)'},
    ]
    review = {
        'format': sr.FORMAT, 'review_id': 'neuro-de-armoring-cards-20261104-x1104d',
        'title': 'Neuro De-Armoring Cards, 4 November (3)',
        'intro': [
            'Six stretches for you to edit. I checked all of them myself in Pangram\'s web app, one paragraph at a time. '
            'For four of them, my two tries and Codex\'s rewrite read AI. For the other two, the paragraph read better, but '
            'fixing its one weak sentence moved the others. Each card links every check and the readers\' notes.',
            'Each card shows your post\'s paragraph, or my version where it\'s already in the article (the 5-HTP "Who this is '
            'for"). Edit it the way you would, or keep it as it is.',
            'Your answers save as you click. When you\'re done, click <b>Copy my answers</b> (or <b>Save them as a file</b>) '
            'and send them to me.'],
        'git_file': GIT_FILE, 'article': {'file': LANE + 'HUMANIZED-SO-FAR.md', 'sha256': SHA},
        'links': {'guide': BLOB + LANE + 'HUMANIZED-SO-FAR.md', 'review': BLOB + LANE + 'fix-20261104/cards/REVIEW-X1104D.md'},
        'built': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M UTC'),
        'types': TYPES, 'suggestions': S,
    }
    probs = sr.check(review, BL)
    for p in probs:
        print('PROBLEM', p)
    (HERE / 'REVIEW-X1104D.json').write_text(json.dumps(review, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    if probs:
        sys.exit(1)
    page = sr.page(review, MD, BL)
    (HERE / 'REVIEW-X1104D.html').write_text(page, encoding='utf-8')
    (HERE / 'REVIEW-X1104D.artifact.html').write_text(sr.artifact_view(page), encoding='utf-8')
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
    (HERE / 'REVIEW-X1104D.md').write_text('\n'.join(md) + '\n', encoding='utf-8')
    print('ok', [s['id'] for s in S])


if __name__ == '__main__':
    main()
