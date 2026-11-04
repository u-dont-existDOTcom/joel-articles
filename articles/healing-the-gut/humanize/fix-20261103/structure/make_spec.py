#!/usr/bin/env python3
"""Build STRUCTURE-SPEC.json for Joel's structure page (tools/humanization/decision_page.py). No API calls."""
import hashlib, json, pathlib

HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parents[2]
master_sha = hashlib.sha256((ART / 'master.html').read_bytes()).hexdigest()
R = json.loads((HERE.parent / 'baseline' / 'RESULTS.json').read_text(encoding='utf-8'))


def link(k):
    return R[k]['link']


def t(s, m=''):
    return [s, m]


spec = {
    'review_id': 'healing-the-gut-structure-20261103',
    'title': 'Gut Article Structure',
    'source_sha256': master_sha,
    'source_name': 'Healing the Gut Naturally (your editor HTML, 3 Nov)',
    'repo_file': 'https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/gut-import-20261103/articles/healing-the-gut/humanize/fix-20261103/structure/STRUCTURE-PAGE.html',
    'intro': [
        'You asked how to line up the first part (what you and your friends found) with the second (the recipe from the books). Nothing below changes your post until you approve it, and the humanizing waits until the structure is settled, so no paragraph gets rewritten just before it moves.',
        'What Pangram 4.1 says about each block alone (API, 3 Nov): your whole first part reads Human at High confidence, the intro and every cause, Pooyan included, with one exception. Inside Leaky gut, the "Mitochondrial & Cellular Energy Starvation" stretch (glutamine, butyrate, TCA intermediates) reads AI at High confidence; the 255 words before it read Human. In the second part, Phases 1, 2, 4, 5 and 6 read 100% AI. Phase 3 reads mostly Human because of your H2O2 and Pooyan lines (87%). Every paragraph of "Optional Ready-Made Gut Stacks" reads 100% AI too. The paid Gem instructions weren\'t checked.',
        'So the two halves differ in voice as well as in logic: the first is organized by cause (what might be wrong) and sounds like you; the second is organized by phase (what to do, in what order) and sounds like the books\' summary. Items 1 and 2 are about the logic; 3 to 7 are the repeats and contradictions between the halves. Each item says what I\'d pick and why. Revise with a note if you want a different option, or your own words.',
    ],
    'groups': [
        {'id': 'shape', 'title': 'The shape', 'intro': 'How the two parts fit together.',
         'approve': 'I make the change on a draft and show it to you in place before it goes anywhere.',
         'reject': 'The order stays as it is.'},
        {'id': 'fix', 'title': 'Repeats and contradictions between the halves',
         'intro': 'Each one is small, but together they are why the article feels like two articles.',
         'approve': 'I make the change on the same draft.', 'reject': 'Left as it is.'},
    ],
    'items': [
        {'id': 'S1', 'group': 'shape', 'title': 'Keep two parts, but make them point at each other (my pick)',
         'section': 'The whole article', 'whose': 'Proposal: Claude',
         'fields': [
             {'label': 'What it means', 'text': 'Part 1 stays your list of causes, in your words: what might be wrong, with what you and your friends found. Part 2 stays the phases from the books: what to do, in order. Each cause gets a short pointer to the phase that deals with it, and the phases point back where your own finding changes the books\' advice (Phase 3 already does this with H2O2).'},
             {'label': 'Why this one', 'list': [
                 'Your first part already passes alone at High confidence; this keeps it whole instead of breaking it up across phases.',
                 'The Gem works in phases, so a phase-shaped Part 2 still matches what readers get when they ask the Gem.',
                 'It fixes the lining-up with the smallest change, so the real work goes into Part 2\'s voice, which is where the AI score comes from.']},
             {'label': 'The other ways', 'list': [
                 'A. One spine: dissolve the causes list into the phases, each finding of yours as a note inside the phase it belongs to (stress and bile into Phase 1, H. pylori into Phase 3, leaky gut into Phase 6, Pooyan\'s impaction into Phase 5). One logic, but your passing paragraphs get split up and surrounded by the summary\'s voice.',
                 'C. Cause first: each cause becomes its own section (what it is, how to tell, what to do), with a short order-of-operations box on top. Most reader-friendly, but the biggest rewrite, and it no longer mirrors the Gem.',
                 'Leave it: only humanize, no structural change.']},
         ],
         'approve': 'Option B (this one).', 'reject': 'Leave the structure; humanize only.'},
        {'id': 'S2', 'group': 'shape', 'title': 'The pointers: which cause goes with which phase',
         'section': 'Some Causes of poor gut health -> Text Summary of the Protocol', 'whose': 'Proposal: Claude',
         'fields': [
             {'label': 'The mapping', 'list': [
                 'Severe stress / adrenal fatigue / poor sleep -> Phase 1 (autonomic tone, the vagus exercises)',
                 'Sitting, lack of exercise -> Phase 6 (maintenance)',
                 'Years of accumulated shit (Pooyan) -> not in the books; closest is Phase 5, so I\'d say that plainly',
                 'Poor diet now -> Phase 2 (the reset diet)',
                 'Parasites, H. pylori, mold, metals -> Phase 3 (the purge), and Phase 5 for mold',
                 'SIBO -> Phase 3, and Phase 6 for SIBO yogurt',
                 'Plant foods -> Phase 2 (low FODMAP), then Phase 6 (bringing plants back)',
                 'Leaky gut -> Phase 6 (repair)',
                 'IBS -> Phase 5 (investigation)',
                 'Low stomach acid, enzymes, thick bile -> Phase 1 (bile flow)']},
             {'label': 'How it would look', 'text': 'A few words at the end of each cause, like "(Phase 1 below)", plus one or two sentences at the top of Part 2 saying the phases are the order to work in and the causes above tell you where to look first. Those sentences would be new wording, so I\'d draft them for you to rewrite or replace.'},
         ],
         'approve': 'Use this mapping.', 'reject': 'No pointers.'},
        {'id': 'S3', 'group': 'fix', 'title': 'Move the mitochondrial-fuels stretch out of Leaky gut into Phase 6',
         'section': 'Leaky gut -> Phase 6', 'whose': 'Proposal: Claude',
         'blocks': [
             {'label': 'Leaky gut now (the part that reads AI)', 'paras': [[
                 t('... Ozonated zeolite (or ZeoCharge ): I find regular zeolite to be ineffective, because the pores on it are clogged up, so it can\'t adsorb excess zonulin, metals, and other toxins. '),
                 t('Mitochondrial & Cellular Energy Starvation (Glutamine, Butyrate, TCA Intermediates): Your gut barrier requires massive amounts of immediate, localized energy [... about 300 words: glutamine dosing 5g and 10-30g, the cancer caveat, butyrate, malic and citric acid ...] accelerating mucosal healing from a different biochemical angle.', 'del')]]},
             {'label': 'Phase 6 now', 'paras': [[
                 t('... Maintain (Pimentel): Continue strict meal spacing (4+ hours) forever to keep the MMC cleaning wave active. '),
                 t('Fuel the Mitochondria: Deploy L-Glutamine (5–30g based on inflammatory load), butyrate-producing substrates (resistant starch), and TCA cycle intermediates (malic acid/citrate) ...', 'mark')]]},
         ],
         'fields': [
             {'label': 'Why', 'text': 'The same three fuels and the same glutamine range are in both places. Moving the long version into Phase 6 puts the dosing in one spot, ends your leaky gut list on your own items (colostrum, charcoal, zinc carnosine, BPC-157, zeolite), and takes the one AI-reading stretch out of your first part. Every number, the cancer caveat and the Dr. Rhonda link go with it unchanged; it gets humanized in its new place.'},
         ],
         'links': [{'text': 'Pangram: Leaky gut alone', 'url': link('GH-12')}, {'text': 'Pangram: Phase 6 alone', 'url': link('GH-32-34')}],
         'approve': 'Move it into Phase 6 and merge it with "Fuel the Mitochondria".', 'reject': 'Keep it in Leaky gut.'},
        {'id': 'S4', 'group': 'fix', 'title': 'The "Optional Ready-Made Gut Stacks" section',
         'section': 'Optional Ready-Made Gut Stacks', 'whose': 'Question for you',
         'fields': [
             {'label': 'What I see', 'text': 'Every paragraph reads 100% AI, nearly all at High confidence. Its first paragraph repeats the phase order in different words, and its last is a stock list of who should see a clinician. Its real content is three product picks (Microbiome Labs Total Gut Restoration, Dr. Ruscio\'s Leaky Gut Support Kit, Designs for Health GI Revive) and the advice to start low.'},
             {'label': 'My question', 'text': 'Are those three picks your own view? I can\'t tell from the text, and I won\'t write them up as yours unless you say so.'},
             {'label': 'Options', 'list': [
                 'A. If they\'re yours: shrink it to a short note at the end of Phase 6 (if you\'d rather buy a kit than separate ingredients, these three, and start low), keeping the product names and the start-low warning. (my pick)',
                 'B. Keep it as its own section and humanize it as it is.',
                 'C. Cut it.']},
         ],
         'links': [{'text': 'Pangram: the first paragraph alone', 'url': link('GH-35')}, {'text': 'Pangram: the product picks alone', 'url': link('GH-40')}],
         'approve': 'Option A (shrink into Phase 6), and yes, the picks are mine.', 'reject': 'Cut it (C).'},
        {'id': 'S5', 'group': 'fix', 'title': 'Berberine: recommended twice, then listed as something not to start with',
         'section': 'Parasites / Phase 3 / Gut Stacks', 'whose': 'Proposal: Claude',
         'blocks': [{'label': 'The three places', 'paras': [
             [t('Parasites: "For H. Pylori specifically: if you get heartburn when your stomach is empty only, that\'s usually H. Pylori, and it\'s easily treated with '), t('berberine', 'mark'), t('."')],
             [t('Phase 3: "There is one herbal antibiotic that works really well tho for H. pylori: '), t('Berberine', 'mark'), t('."')],
             [t('Gut Stacks: "I would not recommend general \'gut cleanse\' stacks built around oregano oil, wormwood, black walnut, '), t('berberine', 'mark'), t(', or other antimicrobial herbs as a universal starting point."')]]}],
         'fields': [{'label': 'Fix', 'text': 'They don\'t really disagree (H. pylori is a specific reason, the stacks line is about starting blind), but read in a row they seem to. If the stacks section stays in any form, say berberine for H. pylori is the exception. If it\'s cut (S4 C), there\'s nothing to fix.'}],
         'approve': 'Mark the H. pylori exception.', 'reject': 'Leave it.'},
        {'id': 'S6', 'group': 'fix', 'title': 'The article\'s six phases don\'t match the Gem\'s six phases',
         'section': 'Text Summary of the Protocol vs. the paid Gem instructions', 'whose': 'Proposal: Claude',
         'fields': [
             {'label': 'The article', 'list': ['1 Pre-flight (Hale, Rosenberg)', '2 Reset (Ruscio, Pimentel)', '3 Purge (Davis, Ruscio)', '4 Nuclear option: elemental diet (Ruscio)', '5 Investigation (Brown, Nathan, Hopper)', '6 Restoration (Davis, Bulsiewicz)']},
             {'label': 'The Gem', 'list': ['1 Pre-flight (Hale, Rosenberg)', '2 Reset (Ruscio, Pimentel)', '3 Purge (Davis, Ruscio, Brown), with the semi-elemental diet as its escalation', '4 Investigation (Brown only)', '5 Restoration (Davis, Bulsiewicz)', '6 Refractory cases (Nathan, Hopper)']},
             {'label': 'Why it matters', 'text': 'A reader who reads Phase 5 here and then asks the Gem about Phase 5 gets restoration instead of investigation, and mold and limbic retraining land in different places. I\'d make the article\'s summary follow the Gem, since the Gem is what readers will actually consult; the content stays, only the grouping and numbers change.'},
         ],
         'approve': 'Make the article follow the Gem.', 'reject': 'Leave both as they are.'},
        {'id': 'S7', 'group': 'fix', 'title': 'The paid Gem instructions: leave them as a prompt?',
         'section': 'Paid Subscribers can see my Gem\'s custom instructions below', 'whose': 'Question for you',
         'fields': [
             {'label': 'What I\'d do', 'text': 'Leave the instructions as they are: they\'re a prompt for Gemini that readers copy, not prose for a reader, so humanizing them would only make them a worse prompt. I\'d fix three obvious slips: "Gem Name" appears twice, two "[cite_start]" and "[cite: ...]" leftovers from Gemini\'s output are in the bibliography, and Phase 3 has run-together asterisks ("*** **Action:**").'},
             {'label': 'The catch', 'text': 'If your Pangram extension reads the paid part too, the prompt will always pull the whole-post score toward AI. Your 59% share may include it. If you want the post itself to pass, the prompt could move to a linked page (gut.u-dont-exist.com already holds a copy, per item 10 of the prompt\'s own bibliography).'},
         ],
         'approve': 'Leave the prompt, fix the three slips.', 'reject': 'Humanize it too.'},
    ],
}
(HERE / 'STRUCTURE-SPEC.json').write_text(json.dumps(spec, ensure_ascii=False, indent=1), encoding='utf-8')
print('items', len(spec['items']))
