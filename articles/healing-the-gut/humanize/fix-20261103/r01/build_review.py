#!/usr/bin/env python3
"""Build REVIEW.json for the r01 marking page: the structure Joel approved on 2026-11-03 18:01 UTC, realized on the
article, with every new word of mine marked for his decision. No API calls.

Usage: python3 build_review.py   (writes REVIEW.json beside it; then suggestion_review.py check/page)
"""
import hashlib, json, pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[4]
sys.path.insert(0, str(REPO / 'tools' / 'humanization'))
import suggestion_review as sr  # noqa: E402

MD = HERE / 'MASTER.md'
md = MD.read_text(encoding='utf-8')
bl = sr.blocks(md)
T = lambda i: bl[i]['text']
ANSWERS = 'experiments/t02-answers/joel-20261103-1801-structure-answers.txt'


def span(i, a=0, b=None):
    return {'block': i, 'start': a, 'end': len(T(i)) if b is None else b}


def label_span(i):
    return span(i, 0, T(i).index(':'))


def with_pointer(i, ptr):
    t = T(i)
    k = t.index(':')
    return t[:k] + ' ' + ptr + t[k:]


S = []

# S1 (his "an explainer if it's not there already that the gem will not have my notes")
S.append({
    'id': 'G1', 'type': 'explainer', 'title': 'Say plainly that the Gem only has the books', 'advice': 'approve',
    'spans': [span(36)],
    'edits': [{'block': 36, 'before': T(36), 'after': T(36) + ' So the phases below are only what the Gem will tell you, from the nine books. Where my notes in the causes above change or add to a phase, I point back to them under "My notes" in that phase.'}],
    'what': 'Two sentences added to your NOTE, at the top of the recipe.',
    'why': 'You asked for an explainer that the Gem will not have your notes. Your NOTE already says the Gem leaves out some of your research; this says what that means for the phases and tells the reader where your notes are.',
    'stays': 'Your NOTE as it is, word for word, before the new sentences.',
    'deciding': 'New wording, mine: approve it, or Revise with your own.',
    'advice_note': 'I\'d take it. It\'s short, and without it a reader can\'t tell which advice is the books\' and which is yours.',
    'approve_label': 'use this wording',
})

# S2 (approved): the pointers from each cause to its phase, in the Gem's numbering (S6)
ptr = {5: '(Phase 1)', 6: '(Phase 5)', 9: '(closest: Phase 4)', 13: '(Phase 2)', 14: '(Phases 3 and 6)',
       15: '(Phases 3 and 5)', 16: '(Phases 2 and 5)', 18: '(Phase 5)', 32: '(Phase 4)', 33: '(Phase 1)'}
S.append({
    'id': 'G2', 'type': 'structure', 'title': 'Each cause points to its phase', 'advice': 'approve',
    'spans': [label_span(i) for i in ptr],
    'edits': [{'block': i, 'before': T(i), 'after': with_pointer(i, p)} for i, p in ptr.items()],
    'what': 'A phase number after each cause\'s name, using the Gem\'s numbering from G3.',
    'why': 'Your S2 approval. The causes tell the reader where to look; the numbers tell them which step of the recipe deals with it.',
    'stays': 'Every cause and every word of it; only the phase number is added after its name.',
    'deciding': 'The mapping is the one you approved; the numbers follow the Gem\'s phases (G3). "(closest: Phase 4)" is for Pooyan\'s impaction, which your text already says the books don\'t cover.',
    'advice_note': 'Approve, unless a number looks wrong to you.',
    'decided': {'status': 'approved', 'text': '', 'comment': 's2 approve (the mapping)', 'by': 'Joel', 'at': '2026-11-03 18:01 UTC'},
})

# S6 (approved): the article's phases follow the Gem's
old61, old62, old63, old64, old65 = T(61), T(62), T(63), T(64), T(65)
nuclear = 'The “Nuclear” Option (Ruscio): If herbs failed, the overgrowth is too severe or the gut lining is too damaged for solids. ' + old65
p6 = [('h4', 'Phase 6: Refractory Cases (The Hazmat Team)'),
      ('p', 'Source: Neil Nathan (Toxic), Annie Hopper (Wired for Healing)'),
      ('p', 'The Logic: For cases that are "sensitive to everything," or that relapse right away despite perfect adherence.'),
      ('p', 'The Protocol:')]
reads = []
for i in range(53, 61):
    reads.append({'text': T(i), 'kind': bl[i]['kind'] if bl[i]['kind'].startswith('h') else 'p'})
reads.append({'text': '5. ' + nuclear, 'new': ['The “Nuclear” Option (Ruscio):']})
reads += [{'text': 'Phase 4: The Investigation (The Detective)', 'kind': 'h4', 'new': [['Phase ', '4'], ['(The Detective', ')']]},
          {'text': 'Source: Benjamin Brown (Digestive Health Solution)'},
          {'text': T(68) + ' (The last two are Phase 6, below.)', 'new': ['(The last two are Phase 6, below.)']},
          {'text': T(69)}, {'text': '1. ' + T(70)},
          {'text': 'Phase 5: Restoration & Maintenance (The Gardener)', 'kind': 'h4', 'new': [['Phase ', '5']]}]
for i in range(74, 81):
    reads.append({'text': ('%s ' % bl[i]['marker'] if bl[i]['kind'] == 'oli' else '') + T(i)})
reads += [{'text': p6[0][1], 'kind': 'h4', 'new': ['Phase 6: Refractory Cases (The Hazmat Team)']},
          {'text': p6[1][1], 'new': [p6[1][1]]}, {'text': p6[2][1], 'new': ['For cases that are "sensitive to everything," or that relapse right away despite perfect adherence.']},
          {'text': p6[3][1]}, {'text': '1. ' + T(71)}, {'text': '2. ' + T(72)}]
S.append({
    'id': 'G3', 'type': 'structure', 'title': 'The phases follow the Gem\'s six', 'advice': 'approve',
    'spans': [span(61), span(66), span(73)],
    'edits': [{'block': 61, 'before': old61, 'after': ''}, {'block': 62, 'before': old62, 'after': ''},
              {'block': 63, 'before': old63, 'after': nuclear}, {'block': 64, 'before': old64, 'after': ''},
              {'block': 65, 'before': old65, 'after': ''},
              {'block': 66, 'before': T(66), 'after': 'Phase 4: The Investigation (The Detective)'},
              {'block': 67, 'before': T(67), 'after': 'Source: Benjamin Brown (Digestive Health Solution)'},
              {'block': 68, 'before': T(68), 'after': T(68) + ' (The last two are Phase 6, below.)'},
              {'block': 73, 'before': T(73), 'after': 'Phase 5: Restoration & Maintenance (The Gardener)'}],
    'inserts': [{'before': 81, 'kind': k, 'text': t, 'seq': 2 + n} for n, (k, t) in enumerate(p6)],
    'moves': [{'blocks': [71, 72], 'before': 81, 'seq': 6}],
    'reads': reads, 'reads_label': 'Phases 3 to 6 as they would read',
    'card_after': 80,
    'what': 'The elemental diet becomes the Purge\'s last step, as in the Gem. Investigation becomes Phase 4 (Brown), Restoration Phase 5, and Nathan\'s mold and Hopper\'s brain retraining go to a new Phase 6 for refractory cases.',
    'why': 'Your S6 approval: a reader who asks the Gem about "Phase 5" should get what the article calls Phase 5.',
    'stays': 'Every sentence of every phase. The Nuclear option\'s two sentences and the elemental diet keep their words; Nathan\'s and Hopper\'s checks move word for word.',
    'deciding': 'The move is approved. What\'s mine: the new Phase 6 title "Refractory Cases (The Hazmat Team)", its Logic line (the Gem\'s own trigger, "sensitive to everything" or immediate relapse despite perfect adherence), "(The Detective)" for Phase 4, and "(The last two are Phase 6, below.)" after Investigation\'s Logic.',
    'advice_note': 'Approve, or Revise with your own title or Logic line for Phase 6.',
    'decided': {'status': 'approved', 'text': '', 'comment': 's6 approve (the regrouping; the new labels are still his call)', 'by': 'Joel', 'at': '2026-11-03 18:01 UTC'},
})

# S3 (his: fuels stay in Leaky gut; "maintain could simply reference back to them without repeating")
S.append({
    'id': 'G4', 'type': 'dedupe', 'title': 'Phase 5 points back to the fuels instead of repeating them', 'advice': 'approve',
    'spans': [span(80)],
    'edits': [{'block': 80, 'before': T(80), 'after': 'Fuel the Mitochondria: see the fuels under Leaky gut, above (glutamine, butyrate and TCA intermediates).'}],
    'what': 'The Fuel the Mitochondria step keeps its name and points to the fuels in Leaky gut.',
    'why': 'Your S3 answer: the fuels stay in Leaky gut, where glutamine is a key remedy, and this step refers back without repeating.',
    'stays': 'The fuels, their doses (5g baseline, 10–30g) and the cancer caveat, all in Leaky gut.',
    'deciding': 'The wording of the pointer is mine.',
    'advice_note': 'Approve.',
})

# S1 (his: "any phases that would benefit from my notes to refer back to them explicitly")
notes = [
    ('G5', 47, None, 'Phase 1', 'My notes: for stress and sleep see Severe stress above, and for stomach acid and bile see Low stomach acid.',
     'Your stress, sleep and bile notes (your mindset, loveyhuasca and sleep pages; T.C. Hale) belong with the pre-flight check.'),
    ('G6', 53, None, 'Phase 2', 'My notes: see Poor diet now and Plant foods, above.',
     'Your notes on industrial oils and on the carnivore diet and plant intolerance go with the reset diet.'),
    ('G7', 66, None, 'Phase 3', 'My notes: the H2O2 swap above is mine, not the books\'. For berberine and H. pylori see Parasites, and for SIBO yogurt see SIBO, above.',
     'Phase 3 already has your H2O2 change inside it; this marks it as yours and points to your berberine and SIBO yogurt notes.'),
    ('G8', 73, None, 'Phase 4 (Investigation)', 'My notes: two things the books don\'t cover, old impaction and colon hydrotherapy (Years of accumulated shit, above) and psychedelics for IBS (IBS, above).',
     'Your two findings that the books have no place for sit closest to investigation.'),
    ('G9', 81, 1, 'Phase 5 (Restoration)', 'My notes: see Leaky gut above for colostrum, zinc carnosine, BPC-157, ozonated zeolite and the fuels, and Sitting above for movement and yoga.',
     'Your leaky gut list and your movement notes are the repair and maintenance side the books\' Phase 5 doesn\'t have.'),
    ('G10', 81, 7, 'Phase 6 (Refractory)', 'My notes: Matt\'s note on mopping up mycotoxins with fermented colostrum is under Leaky gut, above.',
     'Nathan\'s mold step is where a reader with mycotoxins will look; Matt\'s finding is in your leaky gut list.'),
]
for sid, before, seq, where_, text, why in notes:
    ins = {'before': before, 'kind': 'p', 'text': text}
    if seq is not None:
        ins['seq'] = seq
    S.append({'id': sid, 'type': 'pointer', 'title': '"My notes" line for %s' % where_, 'advice': 'approve',
              'inserts': [ins], 'card_after': before - 1,
              'what': 'One line at the end of %s pointing back to your notes.' % where_,
              'why': why + ' You asked that phases which benefit from your notes refer back to them explicitly.',
              'stays': 'The phase itself, word for word.',
              'deciding': 'New wording, mine. Reject it if this phase doesn\'t need the pointer.',
              'advice_note': 'Approve.', 'approve_label': 'use this wording'})

# S5 (approved): berberine, if the stacks section stays in any form (S4)
S.append({
    'id': 'G11', 'type': 'conflict', 'title': 'Berberine for H. pylori is your exception', 'advice': 'approve',
    'spans': [span(88, T(88).index('berberine'), T(88).index('berberine') + len('berberine'))],
    'edits': [{'block': 88, 'before': T(88), 'after': T(88) + ' (My own advice is different for H. pylori, where berberine works well: see Parasites, above.)'}],
    'what': 'A note after the stacks line, saying your advice differs for H. pylori.',
    'why': 'Your S5 approval: your advice and Gemini\'s differ here, though not as a hard conflict.',
    'stays': 'Gemini\'s line as it is.',
    'deciding': 'Only if the stacks section stays in some form (G13). If you cut it, this goes with it.',
    'advice_note': 'Approve, conditional on G13.',
    'decided': {'status': 'approved', 'text': '', 'comment': 's5 approve', 'by': 'Joel', 'at': '2026-11-03 18:01 UTC'},
})

S.append({
    'id': 'G12', 'type': 'question', 'title': 'Straighten every curly apostrophe and quote mark?', 'advice': 'ask',
    'spans': [span(3, T(3).index('“second brain.”'), T(3).index('“second brain.”') + len('“second brain.”'))],
    'question': 'The post uses curly apostrophes and quote marks throughout (don’t, “second brain”), which you type straight and which read as AI. Shall I straighten all of them in the humanized version? Every word stays; only the marks change. (My pick: yes.)',
    'why': 'You said the curly ones are an AI tell. Your fixes catalogue has one of your paragraphs reading 100% Human with straight apostrophes and 100% AI with the same words curled.',
    'stays': 'The text as it is until you answer.',
    'advice_note': 'Yes, straighten them all.',
})

S.append({
    'id': 'G13', 'type': 'question', 'title': 'The stacks section is Gemini\'s: cut, label or keep?', 'advice': 'ask',
    'spans': [span(81), span(87)],
    'question': 'A: cut it, keeping only the start-low advice and the list of who should see a clinician, as a short note at the end of Phase 5. B: keep the three kits, labeled as Gemini\'s suggestions, not yours. C: keep it as it is and humanize it. (My pick: A.)',
    'why': 'You said the AI parts are from Gemini, but this section says "I" throughout ("The best general commercial stack I have seen so far"), so it reads as your recommendation. It also repeats the phase order, and every paragraph reads 100% AI.',
    'stays': 'The section as it is until you answer.',
    'advice_note': 'A.',
})

S.append({
    'id': 'G14', 'type': 'question', 'title': 'The Gem prompt moves to a doc', 'advice': 'ask',
    'spans': [span(90)],
    'question': 'Send me the doc\'s link when it\'s up, and I\'ll replace the prompt in the post with a line pointing to it for paid subscribers. A clean copy to paste is ready (the duplicate "Gem Name" line, the two [cite_start]/[cite: …] leftovers and the run-together asterisks in Phase 3 fixed; nothing else changed).',
    'why': 'Your S7 answer: you\'ll move the instructions out of the post into a Google doc.',
    'stays': 'The prompt in the post until the link is in.',
    'advice_note': 'Paste the clean copy into the doc and send me its link.',
})

review = {
    'format': 'joel-suggestion-review-v1', 'review_id': 'healing-the-gut-r01-structure-20261103',
    'title': 'Gut Article r01',
    'intro': [
        'The structure you approved at 18:01, done on the article. G2, G3 and G11 carry your approvals; what\'s still yours to decide is every new word of mine (the explainer, the phase labels, the "My notes" lines, the pointers) and the three questions at the end.',
        'No humanizing yet: once this is settled, the AI-reading parts (Phases 1, 2, 4 and 5 as they now stand, the fuels stretch in Leaky gut and whatever stays of the stacks section) get rewritten on the next page, each one checked in Pangram before you see it.',
    ],
    'git_file': 'articles/healing-the-gut/humanize/fix-20261103/r01/REVIEW-PAGE.html',
    'article': {'file': 'articles/healing-the-gut/humanize/fix-20261103/r01/MASTER.md',
                'sha256': hashlib.sha256(MD.read_bytes()).hexdigest()},
    'built': '2026-11-03',
    'links': {'guide': 'https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/gut-import-20261103/articles/healing-the-gut/humanize/fix-20261103/r01/MASTER.md',
              'review': 'https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/gut-import-20261103/articles/healing-the-gut/humanize/fix-20261103/r01/REVIEW-CARDS.md'},
    'types': {'structure': {'label': 'Structure', 'about': 'Order and grouping you approved'},
              'explainer': {'label': 'Explainer', 'about': 'What the Gem has and doesn\'t'},
              'pointer': {'label': 'Pointer to your notes', 'about': 'A phase points back to your notes'},
              'dedupe': {'label': 'Repeat', 'about': 'Said once, pointed to elsewhere'},
              'conflict': {'label': 'Conflict', 'about': 'Your advice and Gemini\'s differ'},
              'question': {'label': 'Question', 'about': 'Needs your answer'}},
    'suggestions': S,
}
(HERE / 'REVIEW.json').write_text(json.dumps(review, ensure_ascii=False, indent=1), encoding='utf-8')
print(len(S), 'suggestions')

# The same cards as a Markdown page GitHub renders (AGENTS.md: the page's cards beside it, what Joel is linked to)
out = ['# ' + review['title'], ''] + [p + '\n' for p in review['intro']]
for s in S:
    out += ['## %s. %s' % (s['id'], s['title']), '', '*%s*' % review['types'][s['type']]['label'], '']
    if s.get('decided'):
        out += ['Already decided by you: %s (%s).' % (s['decided']['comment'], s['decided']['at']), '']
    if s['advice'] == 'ask':
        out += ['**Question:** ' + s['question'], '', '**Why:** ' + s['why'], '', '**Until you answer:** ' + s['stays'], '']
        continue
    shown = s.get('reads') and [r['text'] for r in s['reads']] or \
        [e['after'] for e in s.get('edits', []) if e['after']] + [i['text'] for i in s.get('inserts', [])]
    out += ['**As it would read:**', ''] + ['> ' + x + '\n>' for x in shown] + ['']
    for k, lab in (('what', 'What changes'), ('why', 'Why'), ('stays', 'What stays'), ('deciding', 'For you to decide'), ('advice_note', 'My advice')):
        out += ['**%s:** %s' % (lab, s[k]), '']
(HERE / 'REVIEW-CARDS.md').write_text('\n'.join(out), encoding='utf-8')
print('cards written')
