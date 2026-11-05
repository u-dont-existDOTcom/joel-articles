#!/usr/bin/env python3
"""Try 2 of stretches C (the leaky gut list) and H (Phase 2), after try 1 read Mostly Human 4.7% AI and AI Detected 65%.

His usual fix first (gate E368; Joel, 2026-11-05 18:43 UTC: "payoffs coming too late for the reader ... why did you not
check the same issue i always fix?"): each term explained in the sentence that first uses it, never a sentence after it
(gate E369), the point of each sentence first, and short sentences joined. Narrowed first (E343): C's two groups of
blocks with the windows below High, and H's two changed paragraphs, then each stretch again.

Writes CHECK-<name>.txt and RECEIPT-<name>.json for C2-lead (blocks 18-19), C2-items (22-25), C2 (16-25), H2-open
(45-46) and H2 (45-47), and checks each receipt."""
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
TOOLS = HERE.parents[5] / 'tools' / 'humanization'
sys.path.insert(0, str(TOOLS))
import sense_receipt as S  # noqa: E402
import suggestion_review as sr  # noqa: E402

plain = lambda b: (''.join(s['t'] for s in b['segs']) if b.get('segs') else b['text']).strip()
b15 = sr.blocks((HERE.parent / 'r15.md').read_text(encoding='utf-8'))
HIS = (HERE / 'HIS.txt').read_text(encoding='utf-8')
TEXTS = {'C2-lead': [18, 19], 'C2-items': [22, 23, 24, 25], 'C2': list(range(16, 26)), 'H2-open': [45, 46],
         'H2': [45, 46, 47]}
READER = {
    'C': "Someone with poor gut health reading the plant-food and leaky gut causes, choosing among the leaky gut "
         "treatments the list gives, who has never heard of zonulin, colostrum or BPC-157.",
    'H': "Someone starting Phase 2 after Phase 1's checks, to calm the inflammation and starve an overgrowth in the "
         "small intestine with diet and meal spacing, who doesn't know what FODMAPs are.",
}
# sentence prefix -> (payoff, follows), for every sentence of mine in these texts
P = {
    "Plant foods (Phases 2 and 5)": (
        "The reader learns what oxalates and phytates are (plant compounds that bind minerals) when deciding if they're "
        "why plants bother them.", "It opens the next cause in the list, after SIBO."),
    "Leaky gut (Phase 5)": (
        "IBS gets its full name at its first mention, so its own item later and the stacks section read without guessing.",
        "It opens the leaky gut cause after the plant-food one it overlaps with, as before."),
    "It's associated clinically with increased levels of zonulin": (
        "The reader learns what zonulin does (it opens the tight junctions) and what tight junctions are (the seals between "
        "the gut lining's cells) in the sentence that first names them, so the leaking in the next sentence and the fuels "
        "later make sense.",
        "It says how leaky gut shows up, right after what leaky gut is, as his two sentences did; joined, so zonulin is "
        "explained where it is named."),
    "Liposomal first-milking colostrum, the first milk": (
        "The reader knows what they'd be buying (a cow's first milk, in fat bubbles that help it absorb) at the item's "
        "name, before how Matt's protocol ferments it.",
        "It opens the list of leaky gut treatments the item above announced."),
    "Matt from EndSickness.org finds": (
        "The reader learns mycotoxins are mold toxins at their first mention, so the colostrum's job and the mold check in "
        "Phase 6 make sense.", "It gives what the colostrum is good for after saying what it is."),
    "BPC-157 is a lab-made short protein": (
        "The reader knows what BPC-157 is where it is first named, and so why Barrier's claim that it's made from plants "
        "is false, and that it can help.",
        "Next treatment in the list, after zinc carnosine; his note on Barrier follows it."),
    "Beta-glucans, a kind of fiber": (
        "The reader knows beta-glucans are a fiber, the kind of thing they'd be buying.", "Next item in the list."),
    "Resistant starch to feed the good bacteria": (
        "The reader knows what it's for first (feeding the good bacteria), then why it gets to them: the body can't digest "
        "it.", "Next item in the list."),
    "Ozonated zeolite (or ZeoCharge)": (
        "The reader knows zeolite is a mineral full of pores, so 'the pores are clogged' and 'adsorb' make sense.",
        "Next item in the list."),
    "Once the mechanics work, calm the inflammation down": (
        "The reader knows what Phase 2 is for before anything else (calm the inflammation, starve the overgrowths, no "
        "harsh chemicals), and that it comes once Phase 1's checks are done.",
        "It opens Phase 2 right after Phase 1, whose point was getting the mechanics to work, as Phases 1, 3 and 5 open "
        "with what they do."),
    "This one's from Dr. Michael Ruscio": (
        "The reader knows whose advice this phase is, and which books to read for more.",
        "Whose phase it is comes after what it does, as in Phases 1, 3 and 5."),
    "Either way you stop feeding the bacteria in your small intestine": (
        "The reader knows what both diets do and why it works: they cut the carbs the bacteria ferment most easily, which "
        "is what FODMAPs are, so the bacteria overgrowing in the small intestine starve.",
        "It follows his 'go A or B' with what both diets do, his 'Either way'."),
}
Q = {
    'Q1': 'PASS: each term is explained in the sentence that first uses it (zonulin, tight junctions, colostrum, liposomal, '
          'BPC-157, resistant starch, FODMAP), none in a sentence after; each sentence\'s point comes before its explanation '
          '(resistant starch\'s job, then why; Phase 2\'s aim, then whose it is)',
    'Q2': 'PASS: the only instructions are his (go Paleo-Low FODMAP or Low Fermentation Eating; no snacking) and Phase 2\'s '
          'opening, which says what the reader does (calm the inflammation down and starve the overgrowths)',
    'Q3': 'PASS: each explanation names the exact thing (the seals between the cells of your gut lining; the first milk a '
          'cow makes after giving birth; the carbs they ferment most easily)',
    'Q4': 'PASS: zonulin, tight junctions, colostrum, liposomal, BPC-157, beta-glucans, resistant starch and FODMAPs are '
          'explained once, where first used; mycotoxins and bifidobacterium were explained in try 1; vitamins and '
          'common words left alone',
    'Q5': 'PASS: the "since" in the resistant starch and FODMAP sentences each give the reason for the point before them; '
          '"Once the mechanics work" turns on Phase 1\'s point',
    'Q6': 'PASS: nothing moved between paragraphs; inside them, Phase 2 now says what it does before whose it is',
    'Q7': 'PASS: each explanation is what a reader needs to buy or follow the item it is in',
    'Q8': 'PASS: no item moved between groups',
    'Q9': 'PASS: "no harsh chemicals" uncompressed to "without any harsh chemicals"; each explanation is a clause of the '
          'sentence that uses the term, one step each',
}
PLACEMENT = {
    'C': 'The plant-food cause and the leaky gut list, in his order; each explanation inside the sentence that first names '
         'the term, the colostrum and BPC-157 ones joined into their items instead of the sentences after them.',
    'H': 'Phase 2, between Phase 1\'s checks and Phase 3\'s purge, in his order; its opening says what the phase does, then '
         'whose it is; the FODMAP explanation after his "Either way", not inside his "go A or B".',
}
CHECKED = {
    'C': [{'point': 'zonulin opens the tight junctions between the gut lining\'s cells', 'found': 'Sturgeon and '
           'Fasano 2016: zonulin is the only known physiological modulator of the tight junctions between cells, and more '
           'of it means a leakier barrier (https://www.ncbi.nlm.nih.gov/pubmed/28123927)', 'still_needed': 'yes: the leaking in the next sentence '
           'depends on it', 'fate': 'kept'},
          {'point': 'colostrum is the first milk after giving birth; liposomal means in fat bubbles that help absorption',
           'found': 'bovine colostrum is the first milk a cow\'s mammary gland makes after calving (https://www.alice.cnptia.'
           'embrapa.br/alice/bitstream/doc/1135735/1/Bovine-colostrum.pdf); liposomal supplements put the nutrient inside '
           'tiny spheres of phospholipid, a fat, which can protect it in digestion and often help absorption (https://'
           'neuroganhealth.com/blogs/news/liposomal-vs-capsule-supplements)', 'still_needed': 'yes: the '
           'reader buys it', 'fate': 'kept'},
          {'point': 'BPC-157 is lab-made, based on a stomach juice protein', 'found': 'a synthetic 15-amino-acid peptide '
           'derived from a protein in human gastric juice (https://en.wikipedia.org/wiki/BPC-157)', 'still_needed': 'yes: '
           'it shows why the plant claim is false', 'fate': 'kept'},
          {'point': 'resistant starch is starch the body can\'t digest, so it reaches the gut bacteria', 'found': 'starch '
           'that escapes digestion in the small intestine and is fermented by the bacteria in the colon (https://www.'
           'frontiersin.org/articles/10.3389/fnut.2024.1369950/full)',
           'still_needed': 'yes: it is why it feeds them', 'fate': 'kept'},
          {'point': 'zeolite is a volcanic mineral full of pores', 'found': 'porous minerals, mostly from volcanic ash '
           '(https://pubmed.ncbi.nlm.nih.gov/30999685/)', 'still_needed': 'yes: the pores are the point', 'fate': 'kept'}],
    'H': [{'point': 'FODMAPs are the carbs gut bacteria ferment most easily, and both diets cut them', 'found': 'short-chain '
           'carbohydrates, poorly absorbed and rapidly fermented (https://pubmed.ncbi.nlm.nih.gov/23588241/); Pimentel\'s '
           'low fermentation diet limits the foods bacteria ferment', 'still_needed': 'yes: it says what both diets cut',
           'fate': 'kept'}],
}
ok = True
for name, ids in TEXTS.items():
    t = '\n\n'.join(plain(b15[i]) for i in ids)
    (HERE / ('CHECK-%s.txt' % name)).write_text(t, encoding='utf-8')
    k = name[0]
    r = S.make(t, b15[ids[0]].get('section', '') or 'the causes', READER[k], HIS)
    for s in r['sentences']:
        if s.get('his'):
            continue
        hit = [v for pre, v in P.items() if s['s'].startswith(pre)]
        assert len(hit) == 1, (name, s['s'][:70], len(hit))
        s['payoff'], s['follows'] = hit[0]
    r['questions'] = dict(Q)
    r['placement'] = PLACEMENT[k]
    r['checked'] = CHECKED[k]
    (HERE / ('RECEIPT-%s.json' % name)).write_text(json.dumps(r, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    probs = S.check(t, r)
    ok = ok and not probs
    print(name, len(t.split()), 'words', 'PASS' if not probs else probs)
sys.exit(0 if ok else 1)
