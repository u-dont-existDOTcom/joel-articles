#!/usr/bin/env python3
"""The check texts and making-sense receipts (gate E365) for r18's two fixed stretches, each checked as the section it
sits in (E349): Phase 1 from its heading to its notes (blocks 39-43, where r12-g07 read the heading with the first
sentence AI Low) and the stacks from their heading to the kits (73-79, where r12-g13 and r11c-g13 read the list AI Low).
Under E373 none of this is his own writing (the article was drafted with Gemini and he humanized it), so every sentence
gets its payoff here, the headings too. Also "opens" and "same_point" (E374, E376). Writes CHECK-<name>.txt and
RECEIPT-<name>.json and checks each."""
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
R18 = HERE.parent
sys.path.insert(0, str(HERE.parents[5] / 'tools' / 'humanization'))
import sense_receipt as S  # noqa: E402
import suggestion_review as sr  # noqa: E402

b18 = sr.blocks((R18 / 'r18.md').read_text(encoding='utf-8'))
TEXTS = {'r18-P': list(range(39, 44)), 'r18-S': list(range(73, 80))}
assert b18[39]['text'].startswith('Phase 1') and b18[44]['text'].startswith('Phase 2')
assert b18[73]['text'].startswith('Optional Ready-Made') and b18[79]['text'].startswith('Gemini suggested')
P = {'r18-P': [
    ('the reader knows this phase is a safety check, made before anything else', 'opens Phase 1'),
    ('the reader knows what to check first, their nervous system and their bile, and why: supplements and '
     'antimicrobials need them to work', 'the phase\'s aim, right under its heading'),
    ('the reader knows whose advice this is', 'after the aim, the sources (the sentence is split at "T.C.")'),
    ('the reader knows the two books it comes from', 'the rest of the sources sentence'),
    ('the reader can test the first sign of being stuck in fight or flight on themselves',
     'the nervous system check, the first of the two the aim named'),
    ('the reader can test the second sign', 'the next sign of the same state'),
    ('the reader learns what the two signs mean, its medical name, and why it matters: digestion is offline',
     'what the signs just tested say'),
    ('the reader knows the two fixes and where to watch one', 'the fix for the state just named'),
    ('the reader learns how the fixes work and what they get from them, rest and digest mode', 'why the fixes work'),
    ('the reader knows the second check, bile, starts here', 'the bile check, the second of the two the aim named'),
    ('the reader can test the first sign of stagnant bile', 'the first bile sign'),
    ('the reader can test the next signs', 'more signs of the same state'),
    ('the reader learns what the signs mean, and that antimicrobials now would give them a herx reaction, explained',
     'what the bile signs say'),
    ('the reader knows what to take first to thin the bile, what each is, and before what', 'the fix for stagnant bile'),
    ('the reader knows where his notes on stress, sleep, stomach acid and bile are', 'closes the phase with his '
     'pointers'),
], 'r18-S': [
    ('the reader knows this section is about ready-made stacks, and that they are optional', 'opens the stacks'),
    ('the reader learns what a stack is, and what no stack can do for them', 'after the heading, what a stack can\'t do'),
    ('the reader knows to do the phases first, in order, and when to go after bugs and parasites',
     'what follows from "no stack can do the phases"'),
    ('the reader knows when a stack does help: rebuilding, in Phase 5', 'where a stack fits in the phases'),
    ('the reader knows what to look for in a stack, and that the list says what', 'once a stack helps, which one'),
    ('the reader knows the first category, a probiotic easy on the stomach, and why: to bring back good bacteria',
     'first category'),
    ('the reader knows the second category, what a prebiotic is, and the butyrate choice', 'second category: feeding '
     'the bacteria the first brought back'),
    ('the reader knows the third category, what it is for, and what to take for it', 'last category'),
    ('the reader knows where the kits came from and how far to trust them', 'after what a stack should cover, kits that '
     'do'),
    ('the reader knows the best general kit and why', 'first kit'),
    ('the reader knows the kit for leaky gut and what it lacks', 'second kit'),
    ('the reader knows the third kit and what it would need added', 'third kit'),
]}
READER = {
    'r18-P': 'Someone about to start the protocol, who needs to know whether their body is ready for supplements and '
             'antimicrobials before buying any.',
    'r18-S': 'Someone thinking of buying a gut stack, who needs to know when one helps, what it should have, and which '
             'kit has it.',
}
OPENS = {
    'r18-P': 'The heading says this is a safety check, and the first sentence under it tells the reader what to check '
             'before they spend money on supplements or antimicrobials: their nervous system and their bile.',
    'r18-S': 'The heading says the stacks are optional; the first sentence tells the reader, before they buy one, that '
             'no stack heals everyone or does the phases for them.',
}
SAME = {
    'r18-P': 'none: read Phase 1 from its heading to Phase 2: the first sentence names the two checks and each is made '
             'once below it; "the mechanics" comes back as Phase 2\'s first words, pointing back here',
    'r18-S': 'none: read the stacks from their heading to the end: the three categories are listed once, and the kits '
             'paragraph says which kit has which; "the good bacteria" comes back from the intro as the first '
             'category\'s reason',
}
Q = {
    'Q1': 'PASS: Phase 1\'s first sentence names the act (check your nervous system and your bile), then why; the list '
          'opens on the act (look for); each item opens on what it is for; "prebiotic" is explained in the sentence '
          'that first uses it',
    'Q2': 'PASS: each instruction is the reader\'s act, with its reason: check, look for, take a probiotic, keep them '
          'fed with a prebiotic',
    'Q3': 'PASS: each supplement is named as before (glutamine, zinc carnosine, colostrum, butyrate); "herbs that '
          'soothe it" says which herbs, the plain words for "mucosal-support herbs"',
    'Q4': 'PASS: "prebiotic" is explained where first used (the kind of fiber they eat); short-chain fatty acids and '
          'butyrate were explained earlier, under the fuels; "probiotic" is a word a high-school graduate knows',
    'Q5': 'PASS: "so take" turns item 1\'s reason into its act; "Then keep them fed" feeds the bacteria item 1 brought '
          'back; "the mechanics they need to work" is why the reader checks first',
    'Q6': 'PASS: nothing moved between paragraphs; the categories keep their order',
    'Q7': 'PASS: each change is what the reader needs to choose and act',
    'Q8': 'PASS: no item moved between groups',
    'Q9': 'PASS: one step per item; the small words carry the relations (so, then, to help)',
}
CHECKED = [{'point': 'a prebiotic is what the gut\'s bacteria feed on, mostly fermentable fibers',
            'found': 'ISAPP consensus (Gibson et al. 2017): a prebiotic is "a substrate that is selectively utilized by '
                     'host microorganisms conferring a health benefit", https://pubmed.ncbi.nlm.nih.gov/28611480/; the '
                     'best-documented ones are fermentable carbohydrates in the gut, '
                     'https://isappscience.org/for-scientists/resources/prebiotics/',
            'still_needed': 'yes: the term was used here unexplained', 'fate': 'kept'},
           {'point': 'mucosal-support herbs soothe the gut lining',
            'found': 'demulcent herbs (slippery elm, marshmallow root, licorice) soothe and protect irritated or inflamed '
                     'tissue (Hoffman, Medical Herbalism, quoted at https://publications.achs.edu/herb201-demulcent-herbs-'
                     'and-gastritis/1)',
            'still_needed': 'yes: "mucosal-support" told the reader nothing', 'fate': 'changed'}]
PLACEMENT = {
    'r18-P': 'Phase 1 in its order, after the protocol\'s summary; its first sentence names the two checks the '
             'paragraphs below make.',
    'r18-S': 'The stacks after the phases, as before; the list follows the intro\'s "a stack can help with the '
             'rebuilding", and the kits follow the list.',
}
ok = True
for name, ids in TEXTS.items():
    t = '\n\n'.join(b18[i]['text'].strip() for i in ids)
    (HERE / ('CHECK-%s.txt' % name)).write_text(t, encoding='utf-8')
    r = S.make(t, b18[ids[0]]['text'], READER[name])
    sents = r['sentences']
    assert len(sents) == len(P[name]), (name, len(sents), len(P[name]))
    for s, (pay, fol) in zip(sents, P[name]):
        s['payoff'], s['follows'] = pay, fol
    r['opens']['why_reading'] = OPENS[name]
    r['same_point'] = SAME[name]
    r['questions'], r['placement'], r['checked'] = dict(Q), PLACEMENT[name], CHECKED
    (HERE / ('RECEIPT-%s.json' % name)).write_text(json.dumps(r, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    probs = S.check(t, r)
    ok = ok and not probs
    print(name, len(t.split()), 'words', 'PASS' if not probs else probs)
sys.exit(0 if ok else 1)
