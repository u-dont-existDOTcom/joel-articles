"""Neuro De-Armoring Cards, 13 November (2): his ketone and DMSO answers, merged (SC-95b, SC-54, SC-DMSOc). His answers of
2026-11-12 20:16 UTC (SC-95) and 2026-11-13 14:04 UTC (SC-DMSO) were saved on the cards page and never read until
2026-11-13 15:25 UTC (lesson neuro-2026-11-13b); his SC-DMSOb answer came at 15:22 UTC. Texts in texts_x1113b.py, sources in
../coherence/ketone/KETONE-STRATEGY.md and ../dmso/DMSO-PTSD.md; the nine fresh reads are needed/, his-fixes/ and fit/,
each READ.md with what I did about it.

  python3 articles/neuro-de-armoring/humanize/fix-20261108/x1113b/build_x1113b.py
"""
import datetime
import hashlib
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
FIX = HERE.parent
H = FIX.parent
ROOT = H.parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(FIX / 'sci-cde'))
import sense_receipt as S  # noqa: E402
import suggestion_review as sr  # noqa: E402
import texts_x1113b as T  # noqa: E402
from build_x1108b import Q_ANS  # noqa: E402

BLOB = 'https://github.com/u-dont-existDOTcom/joel-articles/blob/main/'
LANE = 'articles/neuro-de-armoring/humanize/'
REL = LANE + 'fix-20261108/x1113b/'
MD = (H / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
BL = sr.blocks(MD)
P = T.plain
DMSO_READER = ('someone with trauma whose glutamate storms bring anxiety, rage and racing thoughts, going through the '
               'protocol\'s glutamate tools and wanting to know what each does and whether it is safe for them')

# the versions the fresh readers saw, for the sentences changed after their reads
OLD_K54_RCT = ('In a bigger trial against a low-fat diet, the keto diet eased fatigue, sleepiness and thinking problems more, '
               'while movement improved about the same on both (Phillips, et al, 2018).')
OLD_USES = ('It is used for humans routinely in stem cell transplants, including for children, and by many humans for all '
            'kinds of medical problems, from arthritis and bladder pain to brain and spinal cord injuries (Jacob & de la '
            'Torre, 2015).')
OLD_BROWN = ('In another study, all seven sheep given the two survived the smoke, while all seven untreated sheep died, and '
             'so did four of the six given DMSO alone (Brown, et al, 1988).')
OLD_RODENT = ('But it has shown some neurotoxic effects in rodent studies: in mice in their first month of life, even the '
              'smallest dose tested set off brain cell death, which worried the authors for children getting it in '
              'transplants (Hanslick, et al, 2009).')


def his_own_dmso():
    """What he wrote himself in his two DMSO answers: not the sentences of my cards he kept."""
    d1 = [p.strip() for p in T.HIS_D1.split('\n\n')]
    d2 = [p.strip() for p in T.HIS_D2.split('\n\n')]
    own = [d1[1], d1[2], ' '.join(S.sentences(d1[3])[-2:]), S.sentences(d2[1])[0], d2[2], d2[3]]
    assert own[2].startswith('But it also appears') and own[3].startswith('It is used for humans')
    # his "straightfoward", spelled right in the item
    own.append('Translating mouse research to humans isn\'t straightforward.')
    return P('\n'.join(own))


WHOSE_D = ('his own: what he wrote himself in his DMSO answers saved on the cards page on 2026-11-13 at 14:04 and 15:22 UTC '
           '(not the sentences of my cards he kept), with "straightforward" spelled right')
WHOSE_95 = 'his own: the sentence he added to his SC-95 answer, saved on the cards page on 2026-11-12 at 20:16 UTC'


def fill(r, spec):
    """spec: {sentence start: (payoff, follows, link)} for every sentence of mine."""
    for x in r['sentences']:
        if x.get('his'):
            continue
        (k,) = [k for k in spec if x['s'].startswith(k)]
        x['payoff'], x['follows'] = spec[k][0], spec[k][1]
        if 'link' in x:
            assert spec[k][2] and spec[k][2] in x['s'], (k, spec[k][2])
            x['link'] = spec[k][2]


def chk(rows):
    return [{'point': a, 'found': f, 'still_needed': s, 'fate': fate} for a, f, s, fate in rows]


def write_receipt(key, text, where, reader, spec, opens, checked, needed, his_fixes, fit, same, place, his='', whose=''):
    r = S.make(text, where, reader, his, whose)
    fill(r, spec)
    r['opens'] = {'first_sentence': r['sentences'][0]['s'], 'why_reading': opens}
    r['checked'] = chk(checked)
    r['needed'], r['his_fixes'], r['fit'] = needed, his_fixes, fit
    r['same_point'], r['placement'] = same, place
    r['questions'] = dict(Q_ANS)
    (HERE / ('%s.receipt.json' % key)).write_text(json.dumps(r, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    (HERE / ('%s.txt' % key)).write_text(text + '\n', encoding='utf-8')
    return ['%s: %s' % (key, x) for x in S.check(text, r)]


def reader_line(kind, key, extra=''):
    brief = {'needed': 'needed_read_brief.md', 'his-fixes': 'his_fixes_brief.md', 'fit': 'fit_read_brief.md'}[kind]
    return ('a fresh reader (Haiku) given tools/humanization/%s and only the text, one sentence a line (x1113b/%s/%s/'
            'READ.md)%s' % (brief, kind, key, extra))


# ---------------------------------------------------------------- SC-95b
def card_95b(bad):
    (b,) = [x['i'] for x in BL if x['text'].startswith('You must pick one of two ketone strategies')]
    assert sr.block_text(BL, b) == P(T.OLD95)
    text = P(T.K95)
    s = S.sentences(text)
    reader = ('someone with trauma and brain fog choosing between the two ketone strategies, about to drink BHB salts or '
              'start the keto diet, who wants to know what each asks of them and what the salts will do for the fog')
    spec = {
        'Your ketone strategy': ('they learn their strategy decides how they handle salt, and why',
                                 'it opens the choice between the two strategies, after the ATP paragraph that brings in '
                                 'ketones', None),
        'If you\'re in a crisis': ('they learn Strategy A is the one for a crisis, when the fog has to lift fast',
                                  'it turns from the salt plan to the first strategy', 'there\'s Strategy A'),
        'You drink BHB': ('they learn what Strategy A asks of them: drink the salts and keep a standard low-sugar diet',
                          'it says what the strategy just named asks', 'You drink BHB'),
        'In trials': ('they learn how much lift to expect for their thinking and how soon, so they don\'t count on the fog '
                      'being gone', 'it backs the strategy\'s promise with what trials found', 'In trials')}
    checked = [
        ('you must pick one of two ketone strategies',
         'his post: "You must choose your fuel strategy. This determines your electrolyte protocol."; the timeline uses '
         'both in turn (blocks 169, 177) and "Drink BHB" on the diet (block 179)',
         'yes: they learn the choice decides their salt plan, so they can follow the timeline from one to the other',
         'changed'),
        ('BHB salts clear the fog fast',
         'exogenous ketones improved cognition against placebo, SMD 0.29 over 29 protocols and 1,117 people, single doses '
         'and use over 13 days alike (Bonnechere et al. 2026); no effect in type 2 diabetes or hypoxia (2025)',
         'yes: they learn how much lift to expect and how soon', 'changed'),
        ('Data on ketones for PTSD specifically are sparse (his)',
         'block 48 gives the PTSD studies: Edwards 2024, two case reports, Youssef 2022, Engelhardt 2026',
         'no: block 48 says it, with the studies, so here it only repeats', 'cut'),
        ('one study shows large improvement for Parkinson\'s, and one woman\'s Alzheimer\'s was reversed (his)',
         'a ketogenic diet (VanItallie 2005, Phillips 2018) and coconut oil, then a ketone drink, in a man (Newport 2015), '
         'not BHB salts; see SC-54', 'yes: they learn what giving ketones did for brains short of sugar, in block 54 '
         'where the protocol says ketones fuel such brains (card SC-54)', 'changed')]
    needed = {'reader': reader_line('needed', 'sp95b'), 'unneeded': [T.H95_AMAZON],
              'kept': {T.H95_AMAZON: 'they learn what people who drink these ketones say about their fog, beyond the '
                                     'trials\' small average: his own sentence, added with the reviews he pasted'}}
    his_fixes = {'reader': reader_line('his-fixes', 'sp95b'),
                 'marked': [{'s': s[3], 'difference': '1'}, {'s': T.H95_AMAZON, 'difference': '4, 8'}],
                 'kept': {s[3]: 'he kept this sentence word for word in his own version of 2026-11-12, after reading it '
                                'on the card',
                          T.H95_AMAZON: 'his own sentence, which he added himself with the reviews he pasted'}}
    fit = {'reader': reader_line('fit', 'sp95b'), 'marked': [], 'kept': {}}
    same = ('none: read the section from its heading to the next for what each strategy does to the salt plan and what '
            'the salts do for the fog; block 94 brings in ketones as fuel for struggling neurons, block 97 is Strategy B. '
            'His PTSD sentence, which block 48 makes with the studies, is cut; his Parkinson\'s and Alzheimer\'s sentence '
            'goes to block 54 (SC-54)')
    bad += write_receipt('SP95B', text, sr.where(BL, b).rsplit(',', 1)[0], reader, spec,
                         'they learn the choice they are about to make decides how they handle salt', checked, needed,
                         his_fixes, fit, same, 'where the block is now (block %d), after the ATP paragraph that brings in '
                         'ketones and before Strategy B' % b, his=T.H95_AMAZON, whose=WHOSE_95)
    edit = {'block': b, 'before': sr.block_text(BL, b), 'after': text}
    return {
        'id': 'SC-95b', 'type': 'yours', 'title': 'Strategy A: your version, without the repeat', 'advice': 'approve',
        'spans': [{'block': b, 'start': 0, 'end': len(edit['before'])}], 'edits': [edit],
        'what': 'Your version of this paragraph, less two of its sentences. "Data on ketones for PTSD specifically are '
                'sparse." goes, because block 48 already says it, with the studies. Your Parkinson\'s and Alzheimer\'s '
                'sentence moves to block 54, on the next card. The trials\' link is back on its citation.',
        'why': 'You asked whether this was the place, and whether the benefits repeat in different places. Each place '
               'makes its own point: block 48 is PTSD, block 54 is ketones as fuel for a brain short of sugar, block 94 is '
               'mood and anxiety, and this paragraph is what the salts do. The one repeat was the PTSD line. Your Amazon '
               'sentence fits here, next to the trials: people drinking these say their fog lifts, more than the trials\' '
               'small average shows. The Parkinson\'s and Alzheimer\'s evidence came from a keto diet, coconut oil and a '
               'ketone drink, not the salts, so here it would read as what the salts did; block 54 already names '
               'Alzheimer\'s.',
        'stays': 'The four sentences you kept, word for word, and your Amazon sentence.',
        'deciding': 'Whether this paragraph becomes your version without the PTSD line, with Parkinson\'s and Alzheimer\'s '
                    'in block 54 instead.',
        'advice_note': 'Approve, with SC-54. If you\'d rather keep Parkinson\'s and Alzheimer\'s here, revise this card '
                       'with them back in and reject SC-54.',
        'ask_because': 'his own: your version of 2026-11-12, less your PTSD line, with your Parkinson\'s and Alzheimer\'s '
                       'sentence moved to block 54',
        'approve_label': 'use it',
        'found_by': 'His SC-95 answer of 2026-11-12 20:16 UTC, saved on the cards page and read on 2026-11-13',
        'whose': 'his own: the Amazon, Parkinson\'s and Alzheimer\'s, and PTSD sentences he added to his SC-95 answer, '
                 'saved on the cards page on 2026-11-12 at 20:16 UTC',
        'receipt': [REL + 'SP95B.receipt.json']}


# ---------------------------------------------------------------- SC-54
def card_54(bad):
    (b,) = [x['i'] for x in BL if x['text'].startswith('The Fix: If the brain is burning less sugar')]
    assert sr.block_text(BL, b) == P(T.OLD54)
    text = P(T.K54)
    s = S.sentences(text)
    reader = ('someone with trauma and brain fog reading why the protocol gives them ketones: whether their fog may be a '
              'brain short of fuel, and what giving ketones has done for brains like that')
    spec = {
        'The Fix': ('they learn the protocol\'s answer to the fuel problem the paragraph before describes: another fuel',
                    'it answers "The Problem" just before: some regions of PTSD brains burn less sugar', None),
        'Ketones are its backup fuel': ('they learn the other fuel is ketones, and that a brain taking up less sugar still '
                                        'takes them up', 'it names the fuel the sentence before promised',
                                        'Ketones are its backup fuel'),
        'And one man': ('they learn what giving ketones did for one brain short of sugar: a man with Alzheimer\'s got '
                        'markedly better', 'it goes from the Alzheimer\'s brain taking up ketones to what giving them did '
                        'for one', 'And one man\'s Alzheimer\'s'),
        'In Parkinson': ('they learn the same was seen in another brain disease short of fuel, and how weak that study '
                         'was', 'it adds a second disease to the first', 'In Parkinson\'s too'),
        'In a bigger trial': ('they learn the controlled test of it: fatigue, sleepiness and thinking, the fog they have, '
                              'eased more on the keto diet', 'it weighs the small study just named against a bigger, '
                              'controlled one', 'In a bigger trial'),
        'PQQ made': ('they learn why the protocol also gives PQQ for the fog, and how far that evidence goes',
                     'it turns from the fuel to the parts of the cell that burn it', 'burn fuel')}
    checked = [
        ('one woman\'s Alzheimer\'s was reversed (his, with his LongeCity link)',
         'his link (2008, quoting the Tampa Bay Times): Steve Newport, a man with early-onset Alzheimer\'s, on coconut oil: '
         'four points up on the mini-mental test the next day, tremor eased and reading back within five months; his wife: '
         'nothing could repair the damage. The case report: improved markedly over 20 months on a ketone monoester '
         '(Newport et al. 2015)', 'yes: they learn what giving ketones did for one brain short of sugar', 'changed'),
        ('one study shows large improvement for Parkinson\'s (his)',
         'VanItallie et al. 2005: five people, 28 days on a hyperketogenic diet, all improved, placebo not ruled out; '
         'Phillips et al. 2018: 47 randomized, the keto diet more than low-fat on non-motor symptoms (fatigue, sleepiness, '
         'thinking), the same on movement; reviews: possibly effective for non-motor symptoms, unproven for motor ones',
         'yes: they learn the big change he points to, and what the controlled trial found for fog-like symptoms',
         'changed')]
    needed = {'reader': reader_line('needed', 'sp54'), 'unneeded': [s[3], s[5]],
              'kept': {s[3]: 'they learn the big improvement he points to, which the next sentence weighs against the '
                             'randomized trial: his point, now with its source',
                       s[5]: 'they learn why the protocol also gives them PQQ for the fog, the paragraph\'s second fix, '
                             'which this card doesn\'t change'}}
    his_fixes = {'reader': reader_line('his-fixes', 'sp54', ', of the version before "while" became ", but"'),
                 'marked': [{'s': s[2], 'difference': '8'}, {'s': s[3], 'difference': '8'},
                            {'s': OLD_K54_RCT, 'difference': '1'}, {'s': s[5], 'difference': '8'}],
                 'kept': {s[2]: '"one" and "And" are his ("And one study shows ...", "one woman\'s Alzheimer\'s"), and '
                                '"one" says it is a single case',
                          s[3]: '"one" is his ("one study shows large improvement for Parkinson\'s"), and says it is a '
                                'single small study',
                          s[5]: 'the article\'s PQQ sentence as it stands, outside this change'}}
    fit = {'reader': reader_line('fit', 'sp54', ', of the version before "while" became ", but"'),
           'marked': [{'s': s[1], 'found': 'FROM: early Alzheimer\'s, not trauma fog'},
                      {'s': s[2], 'found': 'FROM: one man\'s Alzheimer\'s, a single case'},
                      {'s': s[3], 'found': 'FROM: Parkinson\'s'}, {'s': OLD_K54_RCT, 'found': 'FROM: Parkinson\'s'},
                      {'s': s[5], 'found': 'FROM: mouse cells'}],
           'kept': {s[1]: 'it names its condition, early Alzheimer\'s, and the paragraph before says PTSD brains burn '
                          'less sugar too, which is why fuel evidence from other brains short of it is here',
                    s[2]: 'it says it is one man with Alzheimer\'s, a single case, so the reader can weigh it',
                    s[3]: 'it names Parkinson\'s and says the study was small, with no comparison group, so the reader '
                          'can weigh it',
                    s[4]: 'the controlled trial of the study before it; fatigue, sleepiness and thinking are the fog the '
                          'reader has',
                    s[5]: 'the article\'s PQQ sentence as it stands, which says itself that it hasn\'t been shown in '
                          'people'}}
    same = ('none: read the section from its heading (D. The "Lagging" System) to the next for ketones as the brain\'s '
            'backup fuel and what giving them did; block 53 states the problem, this block the fix. Block 48 is PTSD, '
            'block 94 anxiety and depression, block 95 what the salts do: none gives this evidence')
    bad += write_receipt('SP54', text, sr.where(BL, b).rsplit(',', 1)[0], reader, spec,
                         'they learn the protocol\'s fix for the fuel problem they may have: a second fuel', checked,
                         needed, his_fixes, fit, same, 'block %d, "The Fix", after Cunnane\'s finding that '
                         'early-Alzheimer\'s brains still take up ketones, which the new sentences follow up, and before '
                         'the PQQ sentence' % b)
    edit = {'block': b, 'before': sr.block_text(BL, b), 'after': text}
    return {
        'id': 'SC-54', 'type': 'yours', 'title': 'Your Parkinson\'s and Alzheimer\'s evidence, in the fuel paragraph',
        'advice': 'approve', 'spans': [{'block': b, 'start': 0, 'end': len(edit['before'])}], 'edits': [edit],
        'what': 'Your sentence moves here from Strategy A, right after "brains that take up less glucose (as in early '
                'Alzheimer\'s) still take up ketones normally", with three fixes. The Alzheimer\'s case was a man, and he '
                'improved markedly rather than reversed. The Parkinson\'s study gets its source. The randomized trial '
                'goes with it.',
        'why': 'Your LongeCity link works: it\'s Steve Newport\'s story, a man with early-onset Alzheimer\'s whose wife, a '
               'doctor, gave him coconut oil. The next day he scored four points higher on the dementia test, and within '
               'five months his tremor had eased and he could read again. She wrote that nothing could repair the damage, '
               'only that the oil seemed to help. The 2015 case report says he "improved markedly" over 20 months on a '
               'ketone drink. The Parkinson\'s study the same thread quotes is VanItallie 2005: five people, a month on a '
               'keto diet, all better, with no comparison group. The randomized trial since (47 people) found the keto '
               'diet eased fatigue, sleepiness and thinking problems more than a low-fat diet, while movement improved '
               'about the same on both, and reviews call keto "possibly effective" for those symptoms in Parkinson\'s.',
        'stays': 'This paragraph\'s first two sentences and its PQQ sentence.',
        'deciding': 'Whether your Parkinson\'s and Alzheimer\'s evidence goes here, corrected as above.',
        'advice_note': 'Approve, with SC-95b. Block 94\'s "it\'s part of much broader research" could hold it instead; '
                       'say so in your comment if you\'d rather. Once you approve, my three sentences get a Pangram check '
                       'by themselves before they go in.',
        'ask_because': 'meaning: "one woman\'s Alzheimer\'s was reversed" becomes one man\'s that improved markedly, and '
                       'the randomized Parkinson\'s trial comes in',
        'approve_label': 'use it',
        'found_by': 'His SC-95 answer of 2026-11-12 20:16 UTC, its LongeCity link opened in his browser on 2026-11-13',
        'whose': 'his own: the Parkinson\'s and Alzheimer\'s sentence he added to his SC-95 answer, saved on the cards '
                 'page on 2026-11-12 at 20:16 UTC',
        'receipt': [REL + 'SP54.receipt.json']}


# ---------------------------------------------------------------- SC-DMSOc
def card_dmso(bad):
    (before,) = [x['i'] for x in BL if x['text'].startswith(T.BEFORE)]
    assert sr.block_text(BL, before - 1).startswith(T.AFTER)
    texts = [P(m) for m in T.DMSO]
    his = his_own_dmso()
    where = sr.where(BL, before - 1).rsplit(',', 1)[0]
    m1, m2, m3, m4 = [S.sentences(t) for t in texts]
    same = ('none: read the section (2. The Glutamate Shield) from its heading to the next for DMSO; the section names no '
            'DMSO. The safety note at the top (block 7) covers its purity and cleanliness, and the Fog table and the '
            'timeline (block 179) say when to smell it; this item says what it does and how safe it is')
    nreader = reader_line('needed', 'spdmsoc', ', the whole item, before the reads were acted on')
    hreader = reader_line('his-fixes', 'spdmsoc', ', the whole item, before the reads were acted on')
    freader = reader_line('fit', 'spdmsoc', ', the whole item, before the reads were acted on')
    # paragraph 1: my SC-DMSOb sentences he kept
    spec1 = {
        'DMSO (99.9%)': ('they learn how the protocol has them take DMSO, and at what purity',
                         'it opens the item, after Magnesium, the last glutamate tool', None),
        'In rat brain cells': ('they learn what DMSO did to the glutamate signals that drive their storms, and where '
                               'that was shown', 'it says what the dish study found', 'In rat brain cells'),
        'It also kept': ('they learn it also protected the cells from glutamate, the damage this protocol\'s glutamate '
                         'tools are for', 'it adds the dish study\'s second finding', 'It also kept'),
        'Back in 1967': ('they learn it has been given to people with anxiety like theirs, and when, where and how',
                         'it turns from the dish to people', 'Back in 1967'),
        'Within days': ('they learn what happened to those people, against what they were compared with',
                        'it says what the 1967 study found', 'Within days they grew calmer'),
        'There was no placebo': ('they learn how far that study can be trusted', 'it gives that study\'s limits',
                                 'There was no placebo')}
    bad += write_receipt(
        'SPDMSOC1', texts[0], where, DMSO_READER, spec1,
        'they learn the protocol has them smell DMSO, and that the item says why, among the glutamate tools for their '
        'storms',
        [('DMSO suppresses NMDA- and AMPA-mediated excitotoxicity (his study)',
          'in cultured rat hippocampal neurons, DMSO at 0.5 to 1.5% reversibly suppressed glutamate, NMDA and AMPA currents '
          'and calcium influx and prevented excitotoxic death (Lu and Mattson 2001)',
          'yes: they learn what DMSO did to the glutamate signals, in a dish', 'kept'),
         ('DMSO calmed mental patients (his 1967 paper)',
          '42 inpatients in Lima, nine with severe anxiety or obsessive-compulsive neurosis, 50 to 80% DMSO into the '
          'muscle; calmer within days, shorter stays than 16 non-randomized controls; no placebo (Ramirez and Luza 1967)',
          'yes: they learn what was seen in anxious people, with its limits', 'kept')],
        {'reader': nreader, 'unneeded': [], 'kept': {}},
        {'reader': hreader, 'marked': [{'s': m1[1], 'difference': '1'}, {'s': m1[4], 'difference': '4'}],
         'kept': {m1[1]: 'he kept this sentence word for word in his 15:22 version, after reading it on the card',
                  m1[4]: 'he kept it word for word in his 15:22 version; it names the treatments (electroshock, insulin '
                         'comas, tranquilizers)'}},
        {'reader': freader,
         'marked': [{'s': m1[0], 'found': 'CAN\'T TELL and FROM: the Fog table isn\'t in the excerpt'},
                    {'s': m1[1], 'found': 'FROM: a dish'}, {'s': m1[2], 'found': 'FROM: a dish'},
                    {'s': m1[3], 'found': 'FROM: a 1967 ward'}, {'s': m1[4], 'found': 'FROM: 1960s treatments'}],
         'kept': {m1[0]: 'the Fog table is in the article, under Scenario B, where the reader sees it',
                  m1[1]: 'a finding that says where it comes from, a dish, which is how far it goes',
                  m1[2]: 'the same dish finding, said as one, so the reader knows how far it goes',
                  m1[3]: 'it says its route and setting, injections in 1967 inpatients, so the reader can weigh it',
                  m1[4]: 'the comparison is the study\'s own, named so the reader can weigh it, with its limits next'}},
        same, 'the first paragraph of a new item after Magnesium (block %d), the last of the glutamate tools, before the '
              'Dynorphin Bridge' % (before - 1))
    # paragraph 2: how people use it
    spec2 = {
        'It is used for humans': ('they learn people already take it, in hospital transplants and for many ailments, so it '
                                  'is not new to the human body', 'it turns from the 1967 study\'s limits to how people '
                                  'use it now', None),
        'There is evidence': ('they learn that in people, more DMSO brought more side effects, the reason to keep the dose '
                              'down', 'it goes from transplant use to what the dose did there', 'too much DMSO'),
        'It hasn\'t been tested': ('they learn that for PTSD, the condition this protocol is for, it rests on what people '
                                   'report', 'it turns from what is known in people to what isn\'t, for PTSD',
                                   'It hasn\'t been tested')}
    bad += write_receipt(
        'SPDMSOC2', texts[1], where, DMSO_READER, spec2,
        'they learn how people use DMSO now, which tells them it is already in human use',
        [('it treats hundreds of medical problems (his, Jacob & De La Torre 2015)',
          'the publisher\'s page: the book reviews its clinical uses (osteoarthritis, interstitial cystitis, gut '
          'inflammation, scleroderma, myasthenia gravis, heart disease, brain injury, Alzheimer\'s, pain, cancer, stroke, '
          'spinal cord injury); no "hundreds"; Amazon refused the check',
          'yes: they learn people take it for many ailments, as the book names them', 'changed'),
         ('used by many humans, including children (his)',
          'children get it in stem cell transplants (Hanslick et al. 2009); nothing found on children taking it '
          'otherwise; in the uses sentence a fresh reader took it as a sign it is safe for children',
          'yes: they learn children get it in transplants, where the young-mouse authors\' worry is (next paragraph)',
          'changed'),
         ('10% vs 5% DMSO increases mild side effects (his, Kortleve 2023)',
          'Kortleve 2023 is a survey of 64 transplant centres about fluids; it cites Mitrus et al. 2018: 150 adults '
          'randomized to 10%, 7.5% or 5%, fewest side effects with 5% (p = 0.02 against 10%)',
          'yes: they learn more DMSO brought more side effects in people', 'changed'),
         ('no trial has tested it for PTSD', 'none found (DMSO-PTSD.md); lesson neuro-2026-11-13a: say "I found no ..."',
          'yes: they learn for PTSD it rests on reports', 'changed')],
        {'reader': nreader, 'unneeded': [m2[2]],
         'kept': {m2[2]: 'they learn that for PTSD, the condition this protocol is for, it rests on what people report; '
                         'the brief named the reader only by anxiety'}},
        {'reader': hreader, 'marked': [{'s': OLD_USES, 'difference': '1'}, {'s': m2[2], 'difference': '8'}],
         'kept': {m2[2]: 'he kept the "so" join in his 15:22 version, and the bracket is his own'}},
        {'reader': freader, 'marked': [{'s': OLD_USES, 'found': 'FROM and MISREAD: "including for children" read as a '
                                                                  'safety endorsement'},
                                       {'s': m2[1], 'found': 'CAN\'T TELL and FROM: transplant dosing'}],
         'kept': {m2[1]: 'his point from his first version: in people, more DMSO brought more side effects, the reason '
                         'for his own advice to cut the dose'}},
        same, 'the item\'s second paragraph, after the 1967 study: from what was done in 1967 to how people use it now',
        his=his, whose=WHOSE_D)
    # paragraph 3: animals
    spec3 = {
        'Nebulized DMSO with heparin': ('they learn that nebulized, the way the author takes it, DMSO with heparin '
                                        'protected sheep lungs from smoke', 'it opens the animal studies, after people',
                                        None),
        'In another study': ('they learn DMSO with heparin kept sheep alive through the smoke, and DMSO alone saved two of '
                             'six', 'it adds survival to the lung damage', 'In another study'),
        'But it has shown': ('they learn it has harmed nerve cells in animals too', 'it turns from the good animal '
                             'findings to the bad', 'But it has shown'),
        'In mice in their first month': ('they learn whom the harm concerns: young brains, children\'s included',
                                         'it says which rodents and what happened', 'In mice in their first month')}
    bad += write_receipt(
        'SPDMSOC3', texts[2], where, DMSO_READER, spec3,
        'they learn DMSO protected lungs when nebulized, the way the author takes it',
        [('nebulized DMSO prevented toxic cotton smoke from killing 4/6 sheep (his, Brown 1988)',
          'Brown et al. 1988: all seven controls died; four of six given DMSO alone died; all seven given DMSO with heparin '
          'lived; no route in the abstract. Kimura et al. 1988, the same lab: nebulized into the windpipe with heparin, '
          'much less lung fluid', 'yes: they learn DMSO with heparin kept sheep alive and, nebulized, protected their '
          'lungs', 'changed'),
         ('neurotoxic effects in other rodent studies under other conditions (his)',
          'Hanslick et al. 2009: brain cell death in mice from birth to a month, worst at a week, from 0.3 ml/kg; the '
          'authors\' concern for children in transplants', 'yes: they learn the harm was in young brains', 'changed')],
        {'reader': nreader, 'unneeded': [OLD_BROWN], 'kept': {}},
        {'reader': hreader, 'marked': [{'s': OLD_BROWN, 'difference': '4'}, {'s': OLD_RODENT, 'difference': '1'},
                                       {'s': m3[4], 'difference': '6'}],
         'kept': {m3[4]: 'his own sentence, from his first version'}},
        {'reader': freader, 'marked': [{'s': m3[0], 'found': 'FROM: sheep and smoke'},
                                       {'s': OLD_BROWN, 'found': 'FROM, and MISREAD: "so did" could read as survived'},
                                       {'s': OLD_RODENT, 'found': 'FROM: neonatal mice and children'}],
         'kept': {m3[0]: 'it says where it comes from, sheep breathing smoke, which is how far it goes; his point'}},
        same, 'the item\'s third paragraph: the animal studies, after what is known in people', his=his, whose=WHOSE_D)
    # paragraph 4: his experience
    spec4 = {
        'My experience': ('they learn what the author and people he knows feel on it: alert, smarter, brighter, bad trips '
                          'turned good', 'it turns from the studies to what people report, which the PTSD line said it '
                          'rests on', None),
        'But when used': ('they learn its one side effect for him, less sleep, and how to avoid it: mornings, a smaller '
                          'dose', 'it turns from the good to its cost', 'But when used')}
    bad += write_receipt(
        'SPDMSOC4', texts[3], where, DMSO_READER, spec4,
        'they learn what the author feels on it, the reports the item said PTSD rests on',
        [('it can reduce sleep (his)', 'his own experience; no study of smelling it found', 'yes: they learn when to '
          'take it and when to cut back', 'kept')],
        {'reader': nreader, 'unneeded': [m4[3], m4[4]],
         'kept': {m4[3]: 'they learn how he weighs the rodent harm against his own experience: his own words, his view',
                  m4[4]: 'they learn of one man who used it for decades and stayed sharp, his father: his own words'}},
        {'reader': hreader, 'marked': [{'s': m4[0], 'difference': '1'}, {'s': m4[2], 'difference': '8'},
                                       {'s': m4[3], 'difference': '6'}],
         'kept': {m4[0]: 'his own words, from his 15:22 version, ended where his first version\'s nebulizing sentence '
                         'comes in',
                  m4[2]: 'his own words: the sleep clause from his 15:22 version, the advice from his first version',
                  m4[3]: 'his own sentence, his view said as his'}},
        {'reader': freader, 'marked': [{'s': m4[i], 'found': f} for i, f in
                                       [(0, 'CAN\'T TELL and MISREAD'), (1, 'MISREAD'), (2, 'ANYWAY and CAN\'T TELL'),
                                        (3, 'CAN\'T TELL and MISREAD'), (4, 'CAN\'T TELL and MISREAD')]],
         'kept': {m4[0]: 'his own experience, said as his and that of people he knows',
                  m4[1]: 'his own experience of nebulizing it, said as his',
                  m4[2]: 'his own advice, from his own experience of sleeping less',
                  m4[3]: 'his own view, said as his ("I\'m pretty sure"); the evidence goes to him on the card',
                  m4[4]: 'his own words about his father, said as one man'}},
        same, 'the item\'s last paragraph: what people report, after the studies, as the PTSD line says it rests on',
        his=his, whose=WHOSE_D)
    return {
        'id': 'SC-DMSOc', 'type': 'yours', 'title': 'DMSO: your two versions as one', 'advice': 'approve',
        'inserts': [{'before': before, 'kind': 'p', 'text': t, 'seq': n + 1} for n, t in enumerate(texts)],
        'card_after': before - 1,
        'what': 'Your newer version (15:22), in its order, plus what your first one (saved at 14:04, which I missed) had '
                'and it didn\'t: the 10%% vs 5%% side effects in transplants, "(that I know of, yet)", the minute after '
                'nebulizing, taking it in the morning, and "Translating mouse research to humans isn\'t straightforward". '
                'Nothing else in the protocol repeats it: the safety note at the top is about purity and cleanliness, and '
                'the Fog table and the timeline say when to smell it. Four facts are fixed.'.replace('%%', '%'),
        'why': 'The sheep were the other way round: the smoke killed all seven untreated sheep and four of the six given '
               'DMSO alone, while all seven given DMSO with heparin lived. That abstract doesn\'t say how the DMSO was '
               'given; the nebulizing is from the same lab\'s other 1988 study, where DMSO with heparin nebulized into the '
               'windpipe cut the lung damage. 10%% vs 5%%: Kortleve 2023 is a survey of transplant centres about fluids, '
               'and the finding is the randomized trial it cites (Mitrus 2018, 150 adults), so that\'s the citation now. '
               'The book: Amazon blocks me ("unauthorized AI agent"), so the link goes to the publisher, whose page lists '
               'arthritis, bladder pain, brain and spinal cord injury, stroke and more, but not "hundreds". Children: in '
               'the uses sentence, a fresh reader took "including children" as a sign it\'s safe for kids. Children do get '
               'it in stem cell transplants, and the young-mouse study\'s authors worried about exactly them, so the '
               'children are in that sentence now. One thing to weigh: nothing I found shows DMSO killing only damaged '
               'neurons, and Hanslick\'s were healthy young ones; "I\'m pretty sure" keeps it as your view, so it '
               'stays.'.replace('%%', '%'),
        'stays': 'Everything else of yours as you wrote it: your experience, the bad trips, nebulizing, sleep, your dad.',
        'deciding': 'Whether the DMSO item goes in after Magnesium as this one merged text, with those fixes.',
        'advice_note': 'Approve. Once you do, the two paragraphs I changed (uses, and animals) get a Pangram check by '
                       'themselves before they go in.',
        'ask_because': 'downside: "including children" moves from the uses sentence to the young-mouse study, and the '
                       'sheep numbers turn the other way round',
        'approve_label': 'add it',
        'found_by': 'His DMSO answers of 2026-11-13 14:04 UTC (saved on the cards page, never sent) and 15:22 UTC',
        'whose': WHOSE_D,
        'receipt': [REL + 'SPDMSOC%d.receipt.json' % n for n in (1, 2, 3, 4)]}


def main():
    bad = []
    cards = [card_95b(bad), card_54(bad), card_dmso(bad)]
    (HERE / 'X1113B-TEXTS.md').write_text(
        '# x1113b: the texts as they would go in, with their links\n\n## SC-95b (block 95)\n\n%s\n\n## SC-54 (block 54)\n\n'
        '%s\n\n## SC-DMSOc (after Magnesium)\n\n%s\n' % (T.K95, T.K54, T.DMSO_TEXT), encoding='utf-8')
    review = {
        'format': 'joel-suggestion-review-v1',
        'review_id': 'neuro-de-armoring-cards-20261113-x1113b',
        'title': 'Neuro De-Armoring Cards, 13 November (2): your ketone and DMSO answers, merged',
        'intro': ['Your answers on the ketone strategies (from last night) and on DMSO (both versions), with the repeats '
                  'taken out and every new source checked.',
                  'Three cards: Strategy A, the fuel paragraph that gets your Parkinson\'s and Alzheimer\'s evidence, and '
                  'one DMSO item.',
                  'No compound, dose, unit or timing changes.'],
        'git_file': REL + 'REVIEW-X1113B.html',
        'article': {'file': LANE + 'HUMANIZED-SO-FAR.md', 'sha256': hashlib.sha256(MD.encode('utf-8')).hexdigest()},
        'built': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
        'links': {'guide': BLOB + LANE + 'HUMANIZED-SO-FAR.md', 'review': BLOB + REL + 'REVIEW-X1113B.md'},
        'types': {'yours': {'label': 'Your answer, merged',
                            'about': 'Your version, with the repeats taken out and its facts checked.'}},
        'suggestions': cards,
    }
    bad += ['PROBLEM ' + x for x in sr.check(review, BL)]
    (HERE / 'REVIEW-X1113B.json').write_text(json.dumps(review, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    for x in bad:
        print(x)
    if bad:
        return 1
    page = sr.page(review, MD, BL)
    (HERE / 'REVIEW-X1113B.html').write_text(page, encoding='utf-8')
    (HERE / 'REVIEW-X1113B.artifact.html').write_text(sr.artifact_view(page), encoding='utf-8')
    out = ['# %s' % review['title'], ''] + [p + '\n' for p in review['intro']]
    for c in cards:
        out += ['## %s: %s' % (c['id'], c['title']), '']
        for e in c.get('edits', []):
            out += ['*%s*' % sr.where(BL, e['block']), '', '**Now:**', '', '> %s' % e['before'], '',
                    '**As it would read:**', '', '> %s' % e['after'], '']
        if c.get('inserts'):
            out += ['*New item after %s*' % sr.where(BL, c['card_after']), '', '**As it would read:**', '']
            out += ['> %s\n>' % i['text'] for i in c['inserts']] + ['']
        out += ['**What changes:** %s' % c['what'], '', '**Why:** %s' % c['why'], '', '**What stays:** %s' % c['stays'],
                '', '**You\'re deciding:** %s' % c['deciding'], '', '**My advice:** %s' % c['advice_note'], '']
    (HERE / 'REVIEW-X1113B.md').write_text('\n'.join(out) + '\n', encoding='utf-8')
    print('ok', [c['id'] for c in cards])
    return 0


if __name__ == '__main__':
    sys.exit(main())
