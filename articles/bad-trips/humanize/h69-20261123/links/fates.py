"""fates.py - LINKS.md: the fate of every mention candidates.py found, from the guide as it now stands.

  python3 fates.py > LINKS.md
"""
import json, pathlib, re

ART = pathlib.Path(__file__).resolve().parents[3]
blocks = {x['id']: x for x in json.loads((ART / 'GUIDE-SO-FAR-blocks.json').read_text(encoding='utf-8'))}
U = 'https://ibogaqueen.substack.com/i/170920118/'
CALL = 'an act ("call medics"): the Call Medics For list says when to call, not how, so a link there sends the reader in a circle'
SAME = 'the section already has this link on an earlier mention, where the reader first acts on it'
INSIDE = 'the words are inside a link he chose to his own site, which stays'
WHY = {
    ('B94', 'my-brain-feels-damaged'): 'the same item links "a basic neurological check" to that section, the check it means',
    ('B144', 'mdma-magnesium-alarm'): 'the same step links "the broader electrolyte branch" to that section',
    ('B104', 'dmso'): 'the paragraph before links DMSO to his DMSO site, and this sentence is the check to do while it works',
    ('B106', 'dmso'): SAME + ' (the brain section\'s action list, B144)',
    ('B103', 'humic-acid-for-the-brain'): INSIDE, ('B219', 'humic-acid-for-the-brain'): INSIDE,
    ('B144', 'humic-acid-for-the-brain'): 'item 1 already has his humic acid evidence link and says how to use it (smell, then a 5mg lick)',
    ('B144', 'active-seizure'): SAME + ' (the brain checks list)', ('B144', 'chest-pain-and-injury'): SAME + ' (the brain checks list)',
    ('B144', 'need-to-stop-the-trip'): 'the same words link to Beach Morning Glory, the remedy the step names',
    ('B144', 'metta-sniffer-chill-love'): 'linked once in the item ("Smell the Metta NMT sniffer")',
    ('B105', 'dmso'): INSIDE,
    ('H49-SEIZE-CALL', 'my-brain-feels-damaged'): 'says a seizure here does not mean brain damage; nothing to send the reader to',
    ('N-CBD-3', 'dmso'): SAME + ' (B111, the line before it on topical DMSO)',
    ('B111', 'mdma-magnesium-alarm'): 'topical magnesium during a seizure; the MDMA section is about magnesium by mouth with MDMA',
    ('B118', 'active-seizure'): 'his story of his second wife\'s convulsions in hospital, not a step',
    ('B123', 'dmso'): SAME + ' (B122)', ('B124', 'dmso'): SAME + ' (B122)', ('R37-CHEST-2', 'dmso'): SAME + ' (B122)',
    ('B124', 'mdma-magnesium-alarm'): 'magnesium chloride on the chest; the MDMA section is about magnesium by mouth',
    ('B126', 'active-seizure'): 'one of the signs of serotonin toxicity, which links to How to Check for SS in the same sentence',
    ('B127', 'activated-charcoal'): 'linked once ("Activated charcoal may help")',
    ('B128', 'activated-charcoal'): SAME + ' (B127)',
    ('B128', 'who-to-contact'): 'Who to Contact has no poison control number (its lines are peer support, crisis and integration)',
    ('B136', 'who-to-contact'): 'Who to Contact has no poison control number',
    ('B136', 'active-seizure'): 'step 7 links Active Seizure where the reader acts on a seizure',
    ('B136', 'mdma-magnesium-alarm'): 'steps 6 and 8 link MDMA: Magnesium Alarm where the reader needs the amounts',
    ('B136', 'niacin-flushes-trips-out'): 'step 8 links niacin to its section; this one is inside the NIH link',
    ('B136', 'need-to-stop-the-trip'): 'step 8 links niacin to its own section, inside Need to Stop the Trip',
    ('B141', 'mdma-magnesium-alarm'): 'a sign in the list of what belongs in the remedies part, which this section is',
    ('B154', 'activated-charcoal'): 'linked once ("requires activated charcoal")',
    ('B160', 'zeocharge-and-ferment'): 'says charcoal and zeolite aren\'t interchangeable; the next paragraph links zeolite where he prefers it',
    ('B167', 'need-to-stop-the-trip'): 'what coffee cherry can do to a trip, not a way to end one',
    ('B182', 'creatine-for-brain-and-bliss'): 'ingredients of his sniffer formula; their own sections follow right after',
    ('B182', 'mango-leaf-tea-chill-bliss'): 'ingredients of his sniffer formula; their own sections follow right after',
    ('H54-CREATINE', 'dmso'): 'a comparison of how creatine feels, not a step',
    ('R30-OILS2', 'metta-sniffer-chill-love'): 'linked once ("If you don\'t have the Metta NMT sniffer")',
    ('B201', 'activated-charcoal'): 'the words link to Shungite, Holy Water, where the aged ozonated-charcoal water is',
    ('B207', 'active-seizure'): 'the line already links Active Seizure ("more on that in Active Seizure")',
    ('B207', 'mdma-magnesium-alarm'): 'magnesium chloride with DMSO on the skin, not the MDMA amounts',
    ('R30-RUE3', 'dmso'): 'his story of a man who used the oil in psychosis, comparing remedies',
    ('R30-RUE3', 'niacin-flushes-trips-out'): 'his story of a man who used the oil in psychosis, comparing remedies',
    ('B188', 'dmso'): 'how ocean water feels beside DMSO, not a step', ('B188', 'grounding-menu'): '"grounding" as a feeling of the water',
    ('B190', 'activated-charcoal'): 'aged ozonated-charcoal water, the water this section is about, not the activated charcoal remedy',
    ('B190', 'ocean-water-calms'): 'the section right before, compared in the same breath',
    ('B190', 'zeocharge-and-ferment'): 'a comparison of the waters in this section',
    ('B192', 'activated-charcoal'): 'charcoal as what the water is ozonated with, not the remedy',
    ('B193', 'zeocharge-and-ferment'): 'a comparison of the waters in this section',
    ('B194', 'activated-charcoal'): 'the water this section is about', ('B195', 'activated-charcoal'): 'the water this section is about',
    ('B195', 'zeocharge-and-ferment'): 'a comparison of the waters in this section',
    ('B197', 'activated-charcoal'): 'the water this section is about', ('B197', 'dmso'): 'his story of smelling ozone gas, not a step',
    ('B198', 'activated-charcoal'): 'charcoal boiled with water, a way to make this section\'s water',
    ('B198', 'zeocharge-and-ferment'): 'how holding shungite feels, beside cleaned zeolite',
    ('B178', 'active-seizure'): 'the same sentence links the MDMA branch, which has the seizure line',
    ('B212', 'beach-morning-glory'): SAME + ' (B211, the sentence before)',
    ('B219', 'too-intense-stabilizers'): '"destabilize" as a word, not the section',
    ('R33-SMELL-L', 'humic-acid-for-the-brain'): 'his line ends "(see Too Intense? Stabilizers)", already linked, where all three are',
    ('R33-SMELL-L', 'metta-sniffer-chill-love'): 'his line ends "(see Too Intense? Stabilizers)", already linked, where all three are',
    ('R33-SMELL-L', 'lime-or-eos-for-calm'): 'his line ends "(see Too Intense? Stabilizers)", already linked, where all three are',
    ('B302', 'chest-pain-and-injury'): 'a sign to stop a breathing exercise, said with the others; the exercise stops, nothing to look up',
    ('B312', 'chest-pain-and-injury'): 'a reason to skip strenuous exercise, not a step',
    ('B304', 'too-intense-stabilizers'): '"stabilizing" as a word in the music line', ('B258', 'grounding-menu'): 'words in the script someone sends',
    ('B324', 'grounding-menu'): 'says bliss makes grounding less welcome; the Grounding Menu is the section before, a click away',
    ('B337', 'who-to-contact'): '"tripsitting" as a practice, not TripSit', ('B408', 'too-intense-stabilizers'): '"destabilized" as a word',
    ('B428', 'too-intense-stabilizers'): '"destabilized" as a word', ('B354', 'lingering-symptoms'): 'inside a Reddit link',
    ('B426', 'grounding-menu'): 'daily grounding routines, not the trip\'s Grounding Menu',
    ('B426', 'syrian-rue-oil-gentler'): 'linked once in the list ("syrian rue OIL")',
    ('B426', 'dmso'): 'linked once in the list (the HPPD line)', ('B426', 'niacin-flushes-trips-out'): 'linked once in the list (the HPPD line)',
    ('B426', 'metta-sniffer-chill-love'): 'linked once in the list', ('B426', 'beach-morning-glory'): 'linked once in the list',
    ('B278', 'who-to-contact'): 'linked once ("crisis line")',
}
import importlib.util
spec = importlib.util.spec_from_file_location('cand', pathlib.Path(__file__).parent / 'candidates.py')
SUBJ = None
src = (pathlib.Path(__file__).parent / 'candidates.py').read_text(encoding='utf-8')
SUBJ = eval(src[src.index('SUBJ = {') + 7:src.index('}\nheads') + 1])
order = json.loads((ART / 'GUIDE-SO-FAR-blocks.json').read_text(encoding='utf-8'))
heads = json.loads((ART / 'SECTION-LINKS.json').read_text(encoding='utf-8'))['headings']
anchor_of = {h['text']: h['anchor'] for h in heads}
path, where = [], {}
for x in order:
    if x['kind'] in ('h1', 'h2', 'h3'):
        lv = int(x['kind'][1])
        txt = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', re.sub(r'^#+\s*', '', x['md'])).replace('**', '').strip()
        path = [p for p in path if p[0] < lv] + [(lv, anchor_of.get(txt, txt))]
    where[x['id']] = [p[1] for p in path]
linked_rows, left_rows, seen_in_section = [], [], set()
for x in order:
    bid, md = x['id'], x['md']
    if x['kind'] in ('h1', 'h2', 'h3', 'image', 'youtube', 'hr'):
        continue
    links = [(m.start(), m.end(), m.group(2)) for m in re.finditer(r'\[([^\]]*)\]\(([^)]+)\)', md)]
    for anc, pats in SUBJ.items():
        if anc in where[bid]:
            continue
        spans = sorted({(m.start(), m.end()) for pat in pats for m in re.finditer(pat, md, re.I)})
        merged = []
        for a, b in spans:
            if merged and a < merged[-1][1]:
                merged[-1] = (merged[-1][0], max(b, merged[-1][1]))
            else:
                merged.append((a, b))
        first_link = min([a for a, b, h in links if h == U + anc] or [None], key=lambda v: v if v is not None else 1e9)
        sec_key = (' > '.join(where[bid][-2:]), anc)
        for a, b in merged:
            word = md[a:b]
            inl = [h for la, lb, h in links if la <= a < lb]
            ctx = '%s (%s)' % (' > '.join(where[bid][-2:]), bid)
            if inl and inl[0] == U + anc:
                linked_rows.append('| %s | "%s" | %s |' % (ctx, word, anc))
                seen_in_section.add(sec_key)
                continue
            if inl:
                fate = INSIDE if 'u-dont-exist' in inl[0] else 'inside another link (%s)' % inl[0][:50]
            elif first_link is not None and first_link < a:
                fate = 'a later mention; the first in this paragraph is linked'
            elif (bid, anc) in WHY:
                fate = WHY[(bid, anc)]
            elif anc == 'call-medics-for':
                fate = CALL
            elif sec_key in seen_in_section:
                fate = SAME
            else:
                fate = 'NO FATE'
            left_rows.append('| %s | "%s" | %s | %s |' % (ctx, word, anc, fate))
G = 'https://github.com/u-dont-existDOTcom/joel-articles/blob/main/'
H = 'https://github.com/u-dont-existDOTcom/joel-articles/blob/main/articles/bad-trips/humanize/h69-20261123/links/'
print('# Section links: every mention read (turn 61, 2026-11-23)\n')
print('Joel, 2026-11-23 19:13 UTC: "make sure that sections are linked to when mentioned or when they should be referenced".')
print('[candidates.py](%scandidates.py) found every unlinked mention of a section\'s subject outside that section' % H)
print('([the list before the links](%sCANDIDATES.md)); each was read for whether the reader there would want what the' % H)
print('section says (how, how much, what to watch for). A mention gets a link the first time a paragraph, list or list item')
print('sends the reader to act on it; a comparison, a story, a word used another way, or a second mention in the same place')
print('stays as it is. Pointers with no name ("the remedies below", "the triage above", "the brain checks above", "a separate')
print('branch") were read too and linked to what they point at. No word changed: the links go on words already there')
print('([apply_links.py](%sapply_links.py), which also adds each to the guide\'s section link catalog), and' % H)
print('[section_links.py](%stools/humanization/section_links.py) check finds every one landing on a heading. This page is' % G)
print('made from the guide as it now stands ([fates.py](%sfates.py)).\n' % H)
asrc = (pathlib.Path(__file__).parent / 'apply_links.py').read_text(encoding='utf-8')
AL = eval(asrc[asrc.index('LINKS = [') + 8:asrc.index(']\n\n\ndef section_of')] + ']', {'U': U})
AA = eval(asrc[asrc.index('A = {') + 4:asrc.index('}\n\n# (block') + 1])
print('## Added this turn (%d links)\n' % len(AL))
print('| Where | Words linked | Section |\n|---|---|---|')
for bid, before, words, after, tgt in AL:
    print('| %s (%s) | "%s" | %s |' % (' > '.join(where[bid][-2:]), bid, words.strip('*'), AA[tgt]))
print()
print('## Every mention now linked (%d, the earlier rounds\' links among them)\n' % len(linked_rows))
print('| Where | Mention | Section |\n|---|---|---|')
print('\n'.join(linked_rows))
print('\n## Left as they are (%d mentions), each with why\n' % len(left_rows))
print('| Where | Mention | Section it could link to | Why it stays |\n|---|---|---|---|')
print('\n'.join(left_rows))
