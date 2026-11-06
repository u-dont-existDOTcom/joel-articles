#!/usr/bin/env python3
"""Making-sense receipts (gate E365) for r17's three stretches, each checked where its window read below High: the
leaky gut list (blocks 16-25, the resistant starch item read Human Low in #170), Phase 4 (58-60, Medium in #164) and the
stacks (79-82, the pregnancy line Medium in #166). Under E373 none of this is his own writing (the article was drafted
with Gemini and he humanized it), so every sentence gets its payoff here. Also "opens" and "same_point" (E374 and E376,
the neuro lane's). Writes RECEIPT-<name>.json and checks each."""
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[5] / 'tools' / 'humanization'))
import sense_receipt as S  # noqa: E402

P = {'r17-C': [
    ('the reader learns why so many drop plants, and what oxalates and phytates are', 'opens the plant-food cause'),
    ('the reader learns the carnivore diet\'s cost: what it leaves out, and why it is hard to leave',
     'the other side of the diet just introduced'),
    ('the reader knows where the research-backed advice is, what made it, and how to bring it up to date',
     'after the diet\'s cost, where to look for what the research supports'),
    ('the reader knows glutamine is worth a look, and that plant intolerance has many causes to tell apart',
     'what that research points to'),
    ('the reader learns what leaky gut is and what it overlaps with, IBS spelled out', 'opens the next cause'),
    ('the reader learns how leaky gut shows up and what zonulin and tight junctions are', 'how the condition is seen'),
    ('the reader learns why an open barrier matters: what leaks and what it costs the body', 'what the opening does'),
    ('the reader knows a list of treatments follows', 'after the problem, what helps'),
    ('the reader knows what colostrum is, how it is wrapped, and how Matt ferments it', 'first treatment'),
    ('the reader learns what colostrum does for them: it mops up mold toxins in the gut', 'what it is good for'),
    ('the reader learns charcoal helps too, and when not to take it', 'a second binder after colostrum'),
    ('the reader knows which juices, and to use the beet greens', 'next treatment'),
    ('the reader knows which zinc to buy and why that one', 'next treatment'),
    ('the reader knows what BPC-157 is and where to get a good one', 'next treatment'),
    ('the reader learns the catch with Barrier\'s marketing before buying', 'about the product just named'),
    ('the reader knows beta-glucans are a fiber, and where they come from', 'next treatment'),
    ('the reader knows what resistant starch is for, and why it reaches the bacteria', 'next treatment'),
    ('the reader knows zeolite is a porous mineral and why the ozonated kind is the one to use', 'last treatment'),
], 'r17-J': [
    ('the reader knows whose phase this is', 'opens Phase 4'),
    ('the reader learns when this phase applies: after even the Elemental Diet failed', 'when to be here'),
    ('the reader knows the three causes left, and where two of them are covered', 'what is left once the gut is cleared'),
    ('the reader knows the next step is checking their organs', 'the first of the causes left'),
    ('the reader recognizes the first case, low digestive enzymes, and knows its test and treatment',
     'the first organ to check'),
    ('the reader knows the second case\'s test and treatment', 'the second organ case'),
    ('the reader knows what else is covered above, impaction and psychedelics', 'closes the phase with his pointers'),
], 'r17-L': [
    ('the reader knows where the kits came from and how far to trust them', 'opens the kits'),
    ('the reader knows the best general kit and why', 'first kit'),
    ('the reader knows the kit for leaky gut and what it lacks', 'second kit'),
    ('the reader knows the third kit and what it would need added', 'third kit'),
    ('the reader learns what a gut cleanse stack is', 'after the kits, the other kind of stack'),
    ('the reader learns when a cleanse stack is for, and when not', 'what the stack does'),
    ('the reader learns why to mostly skip them', 'his view after when they apply'),
    ('the reader knows the one exception and how to take it', 'the exception to skipping'),
    ('the reader knows to start low and go slowly', 'how to start any of these'),
    ('the reader learns what side effects to expect at first, and why', 'why to go slowly'),
    ('the reader knows some symptoms mean a doctor first', 'opens the warnings'),
    ('the reader knows how to tell the two kinds of blood in their stool apart', 'the first warning sign'),
    ('the reader knows the other signs that need a doctor', 'more warning signs'),
    ('the reader knows to skip berberine if pregnant or breastfeeding, why, and to ask about the rest',
     'the next group the warnings cover'),
    ('the reader knows weak immunity makes probiotics risky, and why', 'the next group'),
    ('the reader knows serious illness means working out the plan with a doctor', 'closes the warnings'),
]}
READER = {
    'r17-C': 'Someone with poor gut health whose plants bother them or who suspects leaky gut, choosing which treatments '
             'to try and wanting to know what each one is.',
    'r17-J': 'Someone whose symptoms survived the diets and the purge, deciding what to check next.',
    'r17-L': 'Someone about to buy a gut kit or cleanse stack, who needs to know which one, how to start, and when to see '
             'a doctor instead.',
}
OPENS = {
    'r17-C': 'If plants bother them, this says they are not alone and why: the first line names their own case.',
    'r17-J': 'It tells the reader whose phase this is; the next sentence says it is for them if even the Elemental Diet '
             'failed, which is the case they would recognize.',
    'r17-L': 'It tells the reader these kits are suggestions to check, before they spend money on one.',
}
SAME = {
    'r17-C': 'none: read the causes from "Plant foods" to "Severe stress": glutamine is pointed to here and explained '
             'once under the fuels; zeolite and BPC-157 come back only as Phase 5 pointers',
    'r17-J': 'none: read Phase 4 from its heading to Phase 5: the organs are named once; impaction and psychedelics are '
             'pointers to the causes above',
    'r17-L': 'none: read the stacks section from its heading to the end: berberine is named for H. pylori and for '
             'pregnancy, two different points',
}
Q = {
    'Q1': 'PASS: the fixed sentences give their point first: resistant starch\'s job, then why; each organ case opens on '
          'what the reader would have; the pregnancy line names what to do, then why',
    'Q2': 'PASS: the instructions name the act (test for that with Stool Elastase; skip berberine; ask your doctor)',
    'Q3': 'PASS: each test, treatment and supplement is named exactly',
    'Q4': 'PASS: Exocrine Pancreatic Insufficiency is explained where it is named; SeHCAT and stool elastase are named as '
          'the tests; jaundice is a word a high-school graduate knows',
    'Q5': 'PASS: "so it all goes to them" turns on "can\'t digest it"; "If" opens each organ case',
    'Q6': 'PASS: nothing moved between paragraphs',
    'Q7': 'PASS: each change is what the reader needs to act',
    'Q8': 'PASS: no item moved between groups',
    'Q9': 'PASS: each question-and-answer pair is one sentence now, one step each; nothing compressed',
}
CHECKED = [{'point': 'berberine is not for pregnancy or breastfeeding: it can cause or worsen jaundice in newborns',
            'found': 'NCCIH, In the News: Berberine: people who are pregnant or breastfeeding should not use berberine; '
                     'it can cause or worsen jaundice in newborn infants (https://www.nccih.nih.gov/health/in-the-news-berberine)',
            'still_needed': 'yes: "some herbs and supplements, like berberine" didn\'t say what to do', 'fate': 'kept'},
           {'point': 'resistant starch escapes digestion and is fermented by the gut\'s bacteria',
            'found': 'https://www.frontiersin.org/articles/10.3389/fnut.2024.1369950/full', 'still_needed': 'yes',
            'fate': 'kept'}]
PLACEMENT = {
    'r17-C': 'The leaky gut list in its order; only the resistant starch item\'s why changed, after its point.',
    'r17-J': 'Phase 4 in its order; the two organ cases each open on what the reader would have.',
    'r17-L': 'The warnings in their order; the pregnancy line now names what to do and why.',
}
ok = True
for name in P:
    t = (HERE / ('CHECK-%s.txt' % name)).read_text(encoding='utf-8')
    r = S.make(t, 'the causes' if name == 'r17-C' else ('Phase 4' if name == 'r17-J' else 'the stacks'), READER[name])
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
    print(name, 'PASS' if not probs else probs)
sys.exit(0 if ok else 1)
