#!/usr/bin/env python3
"""REVIEW.json for batch 8: what the pre-publish reads found in his own words and in wording of mine he approved, marked on
r11 (the text now in his post, since 2026-11-04 20:44 UTC). Joel, 2026-11-04 20:27 UTC: "publish it (don't email anyone)".
Before it went in: the word-for-sense read (gate E331; 3 of 3 planted errors found, so its silence counts), the clarity read
and the compare read beside his published post (E284). The one slip in wording of mine he hadn't seen was fixed before the
update (r11). Every finding's fate is in ../../r10/prepublish/FINDINGS.md. No API calls."""
import hashlib
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
R11 = HERE.parent
REPO = HERE.parents[5]
sys.path.insert(0, str(REPO / 'tools' / 'humanization'))
import suggestion_review as sr  # noqa: E402

MD = R11 / 'r11.md'
bl = sr.blocks(MD.read_text(encoding='utf-8'))
GH = 'https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/gut-r07-20261104/articles/healing-the-gut/humanize/fix-20261103/'
POST = 'https://ibogaqueen.substack.com/p/healing-the-gut-naturally'


def card(sid, typ, title, changes, why, stays, whose, advice='approve', note=None):
    """changes: [(block, [(old, new), ...]), ...]: each old must occur once in its block."""
    spans, edits, reads = [], [], []
    for block, pairs in changes:
        before = bl[block]['text']
        after = before
        for old, new in pairs:
            assert before.count(old) == 1, (sid, block, old)
            s = before.index(old)
            spans.append({'block': block, 'start': s, 'end': s + len(old)})
            assert after.count(old) == 1, (sid, block, old)
            after = after.replace(old, new)
        edits.append({'block': block, 'before': before, 'after': after})
        reads.append({'text': after, 'kind': 'p'})
    what = '; '.join('"%s" for "%s"' % (new, old) for _, pairs in changes for old, new in pairs)
    return {'id': sid, 'type': typ, 'title': title, 'advice': advice, 'spans': spans, 'edits': edits, 'reads': reads,
            'reads_label': 'As it would read', 'what': what, 'why': why, 'stays': stays, 'whose': whose,
            'deciding': 'Only whether to fix it.' if typ == 'typo' else 'Whether it says what you meant.',
            'advice_note': note or 'Approve, Reject, or Revise with your own words.'}


def b(start):
    i = [x['i'] for x in bl if x['text'].startswith(start)]
    assert len(i) == 1, (start, i)
    return i[0]


PUB = 'Your published words (live before today too).'
HIS = 'Your own version, from your answers.'
MINE = 'My wording, which you approved.'
S = [
 card('F8-1', 'typo', 'Three slips in the diverticulosis paragraph', [(b('This is likely caused by diverticulosis'), [
      ('based one one incompleted clinical trial', 'based on one incomplete clinical trial'),
      ('Glutamine an amino acid', 'Glutamine is an amino acid')])],
      'The word-for-sense read found all three ("one one", "incompleted", the missing "is"), and the non-word check found '
      '"incompleted".', 'Everything else in the paragraph.', PUB),
 card('F8-2', 'typo', '"with regard to"', [(b('Plant foods (Phases 2 and 5)'), [('with regard vitamins', 'with regard to vitamins')])],
      'A missing "to".', 'The rest.', PUB),
 card('F8-3', 'typo', '"junctions"', [(b('Leaky gut (Phase 5)'), [('jungtions', 'junctions')])],
      'A typo the non-word check and the reader both found.', 'The rest.', PUB),
 card('F8-4', 'typo', '"H. pylori" with a small p', [(b('Parasites, H. pylori, mold, metals'), [
      ('For H. Pylori specifically', 'For H. pylori specifically'), ("that's usually H. Pylori", "that's usually H. pylori")])],
      'The species name takes a small p, as the heading of this same item and the rest of the article write it.',
      'The rest.', PUB),
 card('F8-5', 'typo', '"EndSickness.org" as everywhere else', [(b('Liposomal first-milking colostrum'), [
      ('Matt from Endsickness.org finds', 'Matt from EndSickness.org finds')])],
      'Every other mention writes it EndSickness.org.', 'The link and the rest.', PUB),
 card('F8-6', 'typo', 'What H2O2 and berberine don\'t clear', [(b('H2O2 actually works better'), [
      ("with something that those don't help quickly", "with something that H2O2 and berberine don't clear quickly")])],
      'Two readers: "help" takes the infection as its object, so it says they don\'t help the infection; and "those" comes '
      'right after berberine alone, so a reader looks back to work out it means H2O2 and berberine.',
      'Escalating to secnidazole, then paromomycin, with medical supervision.', PUB),
 card('F8-7', 'typo', '"BIND the toxins"', [(b('BIND to the toxins'), [('BIND to the toxins', 'BIND the toxins')])],
      'As an instruction it tells the reader to bind to the toxins; it\'s the binder (Zholy3O) that binds them.',
      'The capitals and the rest.', PUB),
 card('F8-8', 'reread', 'What the gut "cements"', [(b('Keep in mind that gut health'), [
      ('can cement other stress vectors', 'can cement the stress coming from those other vectors')])],
      'A clarity reader (most would reread): the gut can\'t cement the vectors themselves; it locks in the stress that '
      'started elsewhere. This is the reader\'s smallest change.', 'Your "vectors" and the Hippocrates point.', PUB),
 card('F8-9', 'reread', 'Where zinc carnosine stays', [(b('Zinc carnosine, the form of zinc'), [
      ('which stays in your intestinal gaps', 'which sticks to your intestinal lining')])],
      'The word-for-sense reader: zinc doesn\'t stay "in gaps"; zinc carnosine is the form that sticks to the gut lining '
      'and works there instead of being absorbed right away. If you meant it seals the gaps, Revise.',
      'That it\'s the form of zinc for the gut.', PUB),
 card('F8-10', 'reread', 'What Hale\'s urine test is for', [(b('Low stomach acid, enzymes, and thick bile'), [
      ('his urine pH testing for anabolic/catabolic state freezes',
       'his urine pH testing for whether your body is frozen in a building-up or a breaking-down state (anabolic or catabolic)')])],
      'A clarity reader (most would reread): "anabolic/catabolic state freezes" is never explained, so a reader can\'t tell '
      'what the test looks for. This is the reader\'s wording; Revise if Hale means something else.',
      'That he\'s controversial on it and has good suggestions.', PUB),
 card('F8-11', 'reread', 'The cells that don\'t get the energy', [(b('Mitochondrial and cellular energy starvation'), [
      ("don't do that, the barrier loosens up", "don't get that energy, the barrier loosens up")])],
      'Two readers: "don\'t do that" points back to keeping the tight junctions intact, which makes it a circle (if the '
      'junctions aren\'t kept intact, the barrier loosens). What you mean is that the cells are short of that energy.',
      'Everything else, the LPS sentence included.', HIS),
 card('F8-12', 'reread', 'What SCFAs do for the barrier', [(b('The colonocytes lining your large intestine'), [
      ('preventing the dangerous escape of substances from gut to blood, which then turns down inflammatory signals that '
       'would be needed otherwise to contain the damage',
       "so dangerous substances can't escape from gut to blood, and your body can turn down the inflammatory signals it "
       'would otherwise need to contain the damage')])],
      'Two readers: the "which" at the end has no clear subject, so a reader has to work out that less leaking means less '
      'need for inflammation. This is the clarity reader\'s wording.', 'The first two sentences.', HIS),
 card('F8-13', 'reread', 'Who needs glutamine', [(b('Some people will tell you to take malic'), [
      ('But glutamine is still the main thing they need', 'But glutamine is still the main thing your enterocytes need')])],
      'Two readers: "they" means the acids in the sentence before, so "the main thing they need" reads for a moment as the '
      'acids needing glutamine.', 'The rest of the paragraph.', HIS),
 card('F8-14', 'reread', 'What a herx reaction is', [(b('Now let\'s have a look at your bile function'), [
      ("you'll get a herx reaction you can't detoxify",
       "you'll get a herx reaction: the dying microbes release toxins you can't detoxify")])],
      'A clarity reader (most would reread): "herx" isn\'t explained anywhere, so a reader can\'t tell why it would need '
      'detoxifying. Explaining it at its first mention is your rule.', 'Your bile questions and Beet Flow.', HIS),
 card('F8-15', 'reread', 'Butyrate named twice', [(b('Then keep the probiotics well-fed'), [
      ('and take butyrate itself or something that helps short-chain fatty acid production, especially the main one, butyrate.',
       'and take something that helps short-chain fatty acid production, especially the main one, butyrate, or take butyrate itself.')])],
      'Two readers: with butyrate first, "especially the main one, butyrate" reads like a repeat. This is the clarity '
      'reader\'s order, every word yours. Your section read Human 100% as it is, so a change here gets a section check '
      'before it goes in.', 'Every word, in a new order.', HIS),
 card('F8-16', 'reread', 'The serious signs, as a list', [(b('Some severe symptoms warrant'), [
      ("Other serious signs to note: If you're losing weight fast, or if you have severe pain, a fever or dehydration.",
       'Other serious signs to note: losing weight fast, severe pain, a fever or dehydration.')])],
      'A compare reader: after the colon, the "If ..." has no main clause. Reject if you like it as speech.',
      'Every sign.', HIS),
 card('F8-17', 'point', 'The phases aren\'t only the Gem\'s', [(b('NOTE: this gut gem'), [
      ('So the phases below are only what the Gem will tell you, from the nine books.',
       'So the phases below are what the Gem will tell you, from the nine books (apart from my H2O2 swap in Phase 3).')])],
      'Two readers: Phase 3 has your H2O2 swap in its body, and its note says "the H2O2 swap above is mine, not the books\'", '
      'so "only" isn\'t quite true.', 'The pointer to "My notes".', MINE),
 card('F8-18', 'point', '"Don\'t skip ahead"', [(b('This protocol is meant to be done in phases'), [
      ("Don't skip any, since", "Don't skip ahead, since")])],
      'Two readers: "Don\'t skip any" sounds like "do every phase", but the reason says you stop once a phase works '
      '(and Phase 4 is only for when Phase 3 failed).', 'The rest.', MINE),
 card('F8-19', 'point', 'What "the problem" is in Phase 4', [(b('Benjamin Brown (Digestive Health Solution)'), [
      ('organ failure, or environmental toxicity or brain plasticity',
       "an organ that isn't working right, or environmental toxicity or your brain's false danger signals")])],
      'Three readers: "organ failure" names a life-threatening shutdown, but the examples (pancreatic insufficiency, bile '
      'acid diarrhea) are an organ not working well; and "brain plasticity" is the brain\'s healthy ability to change, '
      'what the retraining uses, not the problem. "False danger signals" is Phase 6\'s own phrase.',
      'Crossing the microbiome off the list, and the pointer to Phase 6.', MINE),
 card('F8-20', 'point', 'Say what the phase tags are, the first time', [(b('Severe stress/adrenal fatigue/poor sleep'), [
      ('(Phase 1):', '(Phase 1 of the recipe below):')])],
      'Two readers: nothing before this says the article has phases, so "(Phase 1)" makes a reader ask "Phase 1 of what?". '
      'Explaining at first mention is your rule; the later tags stay short.', 'Every other tag.', MINE),
 card('F8-21', 'point', '"closest: Phase 4"', [(b('Years of accumulated shit'), [
      ('(closest: Phase 4)', '(not in the phases, but Phase 4 comes closest)')])],
      'A compare reader: "closest:" is shorthand a reader has to guess at. Your next sentence says it isn\'t in the books.',
      'The rest.', MINE),
 card('F8-22', 'point', 'Section names in "My notes", in quote marks', [
      (b('My notes: for stress and sleep'), [('see Severe stress above', 'see "Severe stress" above'),
                                            ('see Low stomach acid.', 'see "Low stomach acid".')]),
      (b('My notes: see Poor diet now'), [('see Poor diet now and Plant foods, above', 'see "Poor diet now" and "Plant foods", above')]),
      (b('My notes: see Leaky gut above'), [('see Leaky gut above', 'see "Leaky gut" above'),
                                           ('and Sitting above for movement', 'and "Sitting" above for movement')])],
      'Two readers stumbled on these: "see Poor diet now" reads as "see poor diet, now", and "Sitting above for movement" '
      'reads as the activity. Quote marks make them names. The other "My notes" lines read fine without them.',
      'Every pointer.', 'Mine (Phases 1 and 2, approved) and yours (Phase 5).'),
]
review = {
    'format': 'joel-suggestion-review-v1', 'review_id': 'healing-the-gut-b8-prepublish-20261104',
    'title': 'Gut Article, After Publishing',
    'intro': ['It\'s in your post (%s) since 20:44 UTC, no email sent: r10, which read Human Written 100%% as a whole '
              'article, with one slip of mine fixed first (Phase 3\'s "if the herbs failed" is now "if all that failed", '
              'since you tell people to skip most herbs; Phase 3 reads Human 100%% with it). Settings untouched.' % POST,
              'Before it went in, three fresh reads: a word-for-sense read (it found all 3 errors I planted, so what it '
              'didn\'t flag counts), a clarity read, and a read beside your published post. These are what they found in '
              'your own words, which were already in the post, and in wording of mine you approved. Each is the smallest '
              'fix I could find.',
              'Your answers go in as you write them. Then each changed paragraph gets a web-app check, and your post gets '
              'a second update, again without email.'],
    'git_file': 'articles/healing-the-gut/humanize/fix-20261103/r11/b8/REVIEW-PAGE.html',
    'article': {'file': 'articles/healing-the-gut/humanize/fix-20261103/r11/r11.md', 'sha256': hashlib.sha256(MD.read_bytes()).hexdigest()},
    'built': '2026-11-04',
    'links': {'guide': GH + 'r11/r11.md', 'review': GH + 'r11/b8/REVIEW-CARDS.md'},
    'types': {'typo': {'label': 'A slip', 'about': 'A wrong or missing word'},
              'reread': {'label': 'A reader stumbles', 'about': 'The smallest change a reader would get first time'},
              'point': {'label': 'My approved wording', 'about': 'A logic slip in it'}},
    'suggestions': S,
}
(HERE / 'REVIEW.json').write_text(json.dumps(review, ensure_ascii=False, indent=1), encoding='utf-8')
out = ['# ' + review['title'], ''] + [p + '\n' for p in review['intro']]
for s in S:
    out += ['## %s. %s' % (s['id'], s['title']), '', '*%s*' % s['whose'], '']
    for r in s['reads']:
        out += ['**%s:**' % s['reads_label'], '', '> ' + r['text'], '']
    out += ['**What changes:** ' + s['what'], '', '**Why:** ' + s['why'], '', '**What stays:** ' + s['stays'], '']
(HERE / 'REVIEW-CARDS.md').write_text('\n'.join(out), encoding='utf-8')
print(len(S), 'cards')
