#!/usr/bin/env python3
"""REVIEW.json for batch 14, marked on r22 (r17 with batch 13's F13-1, the article with every answer in): the fixes of
Phase 4's organ check and of Phase 5's opener and three steps, the paragraphs and sections that tested AI by themselves.
Joel, 2026-11-06 23:59 UTC (gate gut-2026-11-07a): "make sure you're fixing any paras or sections that test ai before you
ask for whole articel checks". Each fix reads Human in its own check and in the protocol section (#207). These replace
tries 2 and 3 of Phase 5's steps (drafts C and D), so draft D's reading decides nothing now. Gate E363: the page goes out
the turn its cards are written; E364: a new review id."""
import hashlib
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
R30 = HERE.parent
FIX = R30.parent
REPO = HERE.parents[5]
sys.path.insert(0, str(REPO / 'tools' / 'humanization'))
import sense_receipt as S  # noqa: E402
import suggestion_review as sr  # noqa: E402

MD = FIX / 'r22' / 'r22.md'
b22 = sr.blocks(MD.read_text(encoding='utf-8'))
b30 = sr.blocks((R30 / 'r30.md').read_text(encoding='utf-8'))
assert len(b22) == len(b30) + 1
GH = 'https://github.com/u-dont-existDOTcom/joel-articles/blob/main/articles/healing-the-gut/humanize/fix-20261103/'
PG = 'https://www.pangram.com/history/'
FEED_B = 'https://www.pangram.com/feed/bb64a934-cf2c-47b3-ae93-af2a363a0644'
FEED_C = 'https://www.pangram.com/feed/154d7a1d-7062-492b-96c1-ed381d39eb0b'
REL = 'articles/healing-the-gut/humanize/fix-20261103/r30/b14/'
NICE = 'https://nice.org.uk/guidance/dg44/documents/topic-description'
DAVIS = 'https://www.buzzsprout.com/1795054/episodes/17783323-here-s-a-microbe-you-should-know-about-bacillus-subtilis'
BULS = 'https://plantbasednews.org/lifestyle/health/gut-doctor-survival-guide-bloating-plant-based-diet/'
R186, R187 = PG + 'd8911a47-187f-4603-9bf2-3133571457fa', PG + 'fd9ef004-3ba4-4386-bf49-fdb31df764ea'
R191, R194 = PG + '8dc695e5-8976-40c8-a4f4-f88bd96ef5e9', PG + '78f5136f-90f6-46ad-9202-afa90825dd52'
R206, R207 = PG + 'a45f149e-419f-4a39-be1a-4fd02dd738cb', PG + '3ff02029-f214-43d0-a5f9-84ba75f13c07'

# r22's blocks and r30's: Phase 4's paragraph (58) and its one numbered step (59) are one paragraph in r30 (58), so
# Phase 5's opener and steps are r22's 62-65 and r30's 61-64.
P4, STEP = 58, 59
assert b22[P4]['text'].startswith('Benjamin Brown') and b22[STEP]['text'].startswith('So check your organs (Brown).')
assert b30[P4]['text'].startswith('Benjamin Brown') and 'Or is it your bile?' in b30[P4]['text']
OPEN, Y, PL, SP = 62, 63, 64, 65
for i, start in ((OPEN, 'Once you\'re clear'), (Y, 'Start by re-seeding'), (PL, 'Then feed'), (SP, 'Continue Pimentel')):
    assert b22[i]['text'].startswith(start), i
for i, start in ((61, 'Cleared the infection?'), (62, 'Start by re-seeding your gut'), (63, 'Then feed the new healthy'),
                 (64, 'Keep spacing')):
    assert b30[i]['text'].startswith(start), i
assert all(b22[i]['text'] == b30[i]['text'] for i in range(P4)) and \
    all(b22[i + 1]['text'] == b30[i]['text'] for i in range(65, len(b30)))


def block_receipt(name, stretch_receipt, text, why_reading):
    """The making-sense receipt for one paragraph as it would read, cut from the section's receipt (each sentence's
    payoff, follows and link as the section's receipt has them)."""
    st = json.loads(stretch_receipt.read_text(encoding='utf-8'))
    by = {x['s']: x for x in st['sentences']}
    sents = S.sentences(text)
    r = dict(st, text=text, text_sha256=S.sha256(text), sentences=[by[s] for s in sents],
             opens={'first_sentence': sents[0], 'why_reading': why_reading})
    probs = S.check(text, r)
    assert not probs, (name, probs)
    (HERE / name).write_text(json.dumps(r, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    return REL + name


def span(i, phrase=None):
    t = b22[i]['text']
    if phrase is None:
        return {'block': i, 'start': 0, 'end': len(t)}
    k = t.find(phrase)
    assert k >= 0 and t.count(phrase) == 1, phrase
    return {'block': i, 'start': k, 'end': k + len(phrase)}


PR = R30 / 'checks' / 'RECEIPT-r30-PR.json'
P4_RECEIPT = R30 / 'checks' / 'RECEIPT-r30-p4.json'
assert json.loads(P4_RECEIPT.read_text(encoding='utf-8'))['text'] == b30[P4]['text']
SECTION = ('the protocol section from its first line through Phase 6: [Human Written, 0%% AI](%s), all High or Medium '
           '(#207)' % R207)
WHOSE = 'My fix of the model\'s text, which read AI in its section.'
S_ = [{
    'id': 'F14-1', 'type': 'window',
    'title': 'Phase 4: the organ check joins the paragraph that gives its reason, and the bile case says what it is',
    'advice': 'approve', 'spans': [span(STEP)],
    'edits': [{'block': P4, 'before': b22[P4]['text'], 'after': b30[P4]['text']},
              {'block': STEP, 'before': b22[STEP]['text'], 'after': ''}],
    'reads': [{'text': b30[P4]['text'], 'kind': 'p'}], 'reads_label': 'Phase 4\'s first paragraph as it would read',
    'what': 'The one numbered step joins the paragraph above it, and the bile case asks the reader first',
    'why': 'The step read AI in the cut of Phases 3 to 6 and Low in the cut of Phases 4 and 5, and its Bile Acid Diarrhea '
           'case read Low in the whole article (draft C). By itself the step read AI in every wording I tried, because '
           'alone it has no reason in it: its "So" points to the paragraph above ("The problem is likely an organ ..."). '
           'So the step joins that paragraph, without its number, and without "(Brown)", since the paragraph already '
           'names Brown as the phase\'s only source. The bile case was the last part that read AI, when it copied the '
           'pancreas case\'s pattern word for word. It now asks the reader first, the way Phase 6 asks about mold, and '
           'says what Bile Acid Diarrhea is: too much bile reaching your colon gives you diarrhea ([NICE DG44](%s): bile '
           'acids that aren\'t absorbed reach the colon, and the excess there causes diarrhoea).' % NICE,
    'stays': 'Both organs, both tests (Stool Elastase, SeHCAT) and both treatments (high-dose enzymes, bile binders); the '
             'paragraph\'s first three sentences, word for word.',
    'whose': WHOSE,
    'deciding': 'Whether the organ check can lose its number "1." and sit in the paragraph above, and whether the bile '
                'case says it right.',
    'advice_note': 'Approve, Reject, or Revise.',
    'reading': 'The step\'s two cases read [AI, Low](%s) in the cut of Phases 3 to 6 (#187); its bile case read [Human, '
               'Low](%s) in the cut of Phases 4 and 5 (#186) and Low in the whole article ([draft C](%s), #189).'
               % (R187, R186, FEED_C),
    'tested': 'Phase 4\'s first paragraph with the change, by itself: [Human Written, 0%% AI](%s) (#206), High, with two '
              'short Medium windows ("Or is it your bile?" and the SeHCAT sentence); %s.' % (R206, SECTION),
    'receipt': [str(P4_RECEIPT.relative_to(REPO))],
}, {
    'id': 'F14-2', 'type': 'window', 'title': 'Phase 5 opens on the reader\'s own question',
    'advice': 'approve',
    'spans': [span(OPEN, 'Once you\'re clear of infection, you have to rebuild a diverse ecosystem to prevent relapse.')],
    'edits': [{'block': OPEN, 'before': b22[OPEN]['text'], 'after': b30[61]['text']}],
    'reads': [{'text': b30[61]['text'], 'kind': 'p'}], 'reads_label': 'As it would read',
    'what': '"Cleared the infection? Then it\'s time to rebuild ..." for "Once you\'re clear of infection, you have to '
            'rebuild ..."',
    'why': 'The opener read AI, Low in the cut of Phases 3 to 6 and Low in the cut of Phases 4 and 5. It now asks the '
           'reader whether they\'re there yet, then says what to do, and "so the overgrowth doesn\'t come back" says '
           'what "to prevent relapse" meant.',
    'stays': 'Davis and Bulsiewicz as the phase\'s sources, word for word.',
    'whose': WHOSE, 'deciding': 'Whether the question opens the phase the way you\'d say it.',
    'advice_note': 'Approve, Reject, or Revise.',
    'reading': 'It read [AI, Low](%s) in the cut of Phases 3 to 6 (#187) and [Human, Low](%s) in the cut of Phases 4 and 5 '
               '(#186).' % (R187, R186),
    'tested': 'In the cut of Phases 4 and 5: [Human Written](%s) (#191), "Cleared the infection?" Medium and the rest '
              'High; %s.' % (R191, SECTION),
    'receipt': [block_receipt('RECEIPT-F14-2.json', PR, b30[61]['text'],
                              'The reader whose infection is cleared knows this phase is theirs.')],
}, {
    'id': 'F14-3', 'type': 'window', 'title': 'Phase 5, step 1: the yogurt, with you and Davis doing things',
    'advice': 'approve', 'spans': [span(Y)],
    'edits': [{'block': Y, 'before': b22[Y]['text'], 'after': b30[62]['text']}],
    'reads': [{'text': b30[62]['text'], 'kind': 'p'}], 'reads_label': 'As it would read',
    'what': 'You ferment the yogurt, Davis picked its bacteria, and oxytocin and bacteriocins are explained',
    'why': 'The step read Low in your whole article (draft B) and AI, Medium in both cuts. The yogurt and its bacteria '
           'were the subjects, with "to heal ..." and "to produce ..." clauses. Now you ferment it and Davis picked its '
           'bacteria for what they do, each bacterium does its job, and the two terms a reader wouldn\'t know get a '
           'plain gloss where they come up: oxytocin (the "love hormone"), bacteriocins (natural antibiotics). Davis '
           'says he chose the strains of his original SIBO yogurt himself, and that they make bacteriocins that kill '
           'SIBO\'s species ([Defiant Health Radio](%s)).' % DAVIS,
    'stays': 'The yogurt, its 36 hours, both bacteria and what each does.', 'whose': WHOSE,
    'deciding': 'Whether it says what the yogurt does the way you would.', 'advice_note': 'Approve, Reject, or Revise.',
    'reading': 'It read Low in the whole article ([draft B](%s), #183) and [AI, Medium](%s) in both cuts (#186, #187).'
               % (FEED_B, R187),
    'tested': 'In the cut of Phases 4 and 5: [Human Written](%s) (#194), High; %s.' % (R194, SECTION),
    'receipt': [block_receipt('RECEIPT-F14-3.json', PR, b30[62]['text'],
                              'The reader knows the first step of rebuilding: re-seeding with the yogurt.')],
}, {
    'id': 'F14-4', 'type': 'window', 'title': 'Phase 5, step 2: feeding the bacteria with plants, slowly',
    'advice': 'approve',
    'spans': [span(PL, 'Then feed the new healthy bacteria. Bulsiewicz says to slowly titrate plant diversity back into '
                       'your diet, aiming for 30+ different plants per week.')],
    'edits': [{'block': PL, 'before': b22[PL]['text'], 'after': b30[63]['text']}],
    'reads': [{'text': b30[63]['text'], 'kind': 'p'}], 'reads_label': 'As it would read',
    'what': 'One sentence that says how: "with plants, slowly, the way Bulsiewicz says: add a few new kinds at a time"',
    'why': 'The step read Low in your whole article (draft B) and AI, High in both cuts. The short "Then feed the new '
           'healthy bacteria." now carries its how in the same sentence, and "add a few new kinds at a time" says what '
           '"slowly titrate plant diversity back" meant. Bulsiewicz\'s reason for going slowly: more fiber at once can '
           'bring gas and bloating while your gut bacteria adapt ([Plant Based News](%s)). Your "Does anyone count '
           'their plants?" stays right after the number it jokes about.' % BULS,
    'stays': 'The 30+ plants a week, Bulsiewicz, and your "Does anyone count their plants?"', 'whose': WHOSE,
    'deciding': 'Whether "add a few new kinds at a time" says it right.', 'advice_note': 'Approve, Reject, or Revise.',
    'reading': 'It read Low in the whole article ([draft B](%s), #183) and [AI, High](%s) in both cuts (#186, #187).'
               % (FEED_B, R187),
    'tested': 'In the cut of Phases 4 and 5: [Human Written](%s) (#194), High; %s.' % (R194, SECTION),
    'receipt': [block_receipt('RECEIPT-F14-4.json', PR, b30[63]['text'],
                              'The reader knows the second step: feed the new bacteria with plants, slowly.')],
}, {
    'id': 'F14-5', 'type': 'window', 'title': 'Phase 5, step 3: keep spacing meals, with its reason left in Phase 2',
    'advice': 'approve', 'spans': [span(SP)],
    'edits': [{'block': SP, 'before': b22[SP]['text'], 'after': b30[64]['text']}],
    'reads': [{'text': b30[64]['text'], 'kind': 'p'}], 'reads_label': 'As it would read',
    'what': '"Keep spacing your meals 4+ hours apart, as in Phase 2, forever." for "Continue Pimentel\'s strict meal '
            'spacing from Phase 2 (4+ hours), forever, to keep the MMC cleaning wave active."',
    'why': 'The step read AI, High in the cut of Phases 3 to 6 and AI, Medium in the cut of Phases 4 and 5 (the whole '
           'article read it High). Its reason, the MMC sweeping your gut clean between meals, is said in Phase 2 with '
           'Pimentel ("so the Migrating Motor Complex (MMC) gets to sweep your gut clean in between"). What only this '
           'step says is to keep it up forever, so it keeps that and points to Phase 2.',
    'stays': 'The 4+ hours, "forever", and Phase 2\'s reason, where Phase 2 gives it.', 'whose': WHOSE,
    'deciding': 'Whether the step can leave its reason to Phase 2.', 'advice_note': 'Approve, Reject, or Revise.',
    'reading': 'It read [AI, High](%s) in the cut of Phases 3 to 6 (#187) and [AI, Medium](%s) in the cut of Phases 4 '
               'and 5 (#186); High in the whole article ([draft B](%s), #183).' % (R187, R186, FEED_B),
    'tested': 'In the cut of Phases 4 and 5: [Human Written](%s) (#194), High; %s.' % (R194, SECTION),
    'receipt': [block_receipt('RECEIPT-F14-5.json', PR, b30[64]['text'],
                              'The reader knows to keep spacing meals for good, and where the reason is.')],
}]
review = {
    'format': 'joel-suggestion-review-v1', 'review_id': 'healing-the-gut-b14-r30-20261107',
    'title': 'Gut Article, Phases 4 and 5 (Batch 14)',
    'intro': ['Phase 4\'s organ check and Phase 5\'s opener and steps read AI when Pangram checked their sections by '
              'themselves. Each card has the fixed version, and the whole protocol section reads [Human Written, 0%% AI]'
              '(%s) with them in, all High or Medium.' % R207,
              'These replace both tries of Phase 5\'s first two steps (drafts C and D), so draft D\'s reading isn\'t needed '
              'anymore.'],
    'git_file': REL + 'REVIEW-PAGE.html',
    'article': {'file': 'articles/healing-the-gut/humanize/fix-20261103/r22/r22.md',
                'sha256': hashlib.sha256(MD.read_bytes()).hexdigest()},
    'built': '2026-11-07',
    'links': {'guide': GH + 'r30/r30.md', 'review': GH + 'r30/b14/REVIEW-CARDS.md'},
    'types': {'window': {'label': 'Fixed window', 'about': 'A paragraph Pangram read AI in its section, fixed and checked'}},
    'suggestions': S_,
}
probs = sr.check(review, b22)
assert not probs, probs
(HERE / 'REVIEW.json').write_text(json.dumps(review, ensure_ascii=False, indent=1), encoding='utf-8')
out = ['# ' + review['title'], ''] + [p + '\n' for p in review['intro']]
for s in S_:
    out += ['## %s. %s' % (s['id'], s['title']), '', '*%s*' % s['whose'], '']
    for r in s['reads']:
        out += ['**%s:**' % s['reads_label'], '', '> ' + r['text'], '']
    out += ['**Why:** ' + s['why'], '', '**Pangram read:** ' + s['reading'], '',
            '**Pangram on the suggestion:** ' + s['tested'], '', '**What stays:** ' + s['stays'], '']
(HERE / 'REVIEW-CARDS.md').write_text('\n'.join(out) + '\n', encoding='utf-8')
print(len(S_), 'cards')
