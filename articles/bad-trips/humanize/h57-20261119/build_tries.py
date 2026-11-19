#!/usr/bin/env python3
"""build_tries.py - batch h57b: the lesson-19b tries (lesson bad-trips-2026-11-19b) on the paragraphs of mine that read
below Human High by themselves in batch h57a. Each try starts from that check (the near miss) and changes only the words
in its windows below High that a reader could take two ways, or a model's join (a semicolon pair, way 8 of his fixes),
a word or two each; the ledger refuses more than 20% of the words from a near miss (NEAR_MISS).

Each try is a list of (block, old words, new words) on the guide's Markdown, so the text checked and the text that goes in
are the same; the check's text is made from the edited blocks as build_baseline.py makes it.

  python3 build_tries.py      writes TEST-b*.txt, MD-b*.md (the edited blocks, Markdown) and ITEMS-h57b.json
"""
import hashlib, json, pathlib

HERE = pathlib.Path(__file__).resolve().parent
import sys
sys.path.insert(0, str(HERE))
import build_baseline as BB  # noqa: E402

# key: (baseline unit it starts from, [(block, old, new), ...], what changed and why)
TRIES = {
    'b05-dmso-overlap': ('a05-dmso-overlap', [
        ('B201', 'Sometimes DMSO works better; sometimes the water does.',
                 'Sometimes DMSO works better, and sometimes the water does.'),
        ('B201', 'Ozonated-charcoal water has what I consider a perfect safety profile; DMSO is a close second in my experience.',
                 'Ozonated-charcoal water has what I consider a perfect safety profile, and DMSO is a close second.')],
        'the two Medium windows: each semicolon pair joined (his fixes, way 8); "in my experience", said in the sentence '
        'before, not said twice. "Safety profile" (the fit read: drug-label wording) and joining "I don\'t yet know why" '
        'wait for the next try: the ledger holds a near miss\'s next try to 20% of its words'),
    'b06-dmso-side': ('a06-dmso-side', [
        ('B203', 'When it itches, dilute it with', 'When the skin itches, dilute the DMSO with'),
        ('B203', 'can crenate it,', 'can crenate (shrivel) it,'),
        ('B203', 'so the mouth should be moist first.', 'so wet your mouth first.'),
        ('B203', ' Sensitivity varies.', ''),
        ('B203', 'In rats, higher doses made sleep lighter', 'In rats, higher doses made sleep less deep')],
        'the two Medium windows: "Sensitivity varies", which every read found gives the reader nothing to do, cut; '
        '"lighter" (easier, or less deep?) said as the study has it (Cavas et al. 2005, round 3\'s W-SLEEP: more light '
        'sleep and less deep sleep). Words a reader could take two ways in the High windows, from the reads: the two '
        '"it"s named, "crenate" explained where it is used, the mouth line said as what to do'),
    'b07-niacin-side': ('a07-niacin-side', [
        ('B214', 'This is normal, although', 'The flush is normal, although'),
        ('B214', 'can create real risk, especially with liver problems, alcohol, medications, or sensitive physiology.',
                 'can create a real risk of liver damage, especially with liver problems, alcohol, or medications.')],
        'the Medium window: "real risk" (a risk of what?) said as liver damage, the risk the reasons after it are about '
        '(NIH ODS: long-term use, especially extended-release, can cause liver problems; LiverTox: high doses and some '
        'formulations linked to acute liver injury; MSD Manual: complications with a liver disorder); "sensitive '
        'physiology", which no reader can check in themselves (the fit read), out. "This", the flush or the heat?, '
        'named'),
    'b08-niacin-forms': ('a08-niacin-forms', [
        ('B214', 'This is normal, although', 'The flush is normal, although'),
        ('B214', 'can create real risk, especially with liver problems, alcohol, medications, or sensitive physiology.',
                 'can create a real risk of liver damage, especially with liver problems, alcohol, or medications.'),
        ('B215', 'seem less reliable for relaxation.', 'seem less reliable than niacin for relaxation.'),
        ('B215', 'the useless non-flush hexanicotinate form.', 'the useless "no-flush" kind (inositol hexanicotinate).')],
        'b07\'s fixes, and B215\'s Low window: less reliable than what said; the non-flush form named the way a label '
        'has it'),
    'b10-anchor-lead': ('a10-anchor-lead', [
        ('B255', 'too much for them, or keeping everyone safe does,', 'too much for the anchor, or keeping everyone from getting hurt does,'),
        ('B255', 'and do it right away', 'and get that help right away')],
        'the Low window: "them" (the anchor, or the person tripping?) said as the anchor; "safe" said as what it means '
        'here (his "if it\'s safe" rule); "do it" said as getting that help. The first two sentences are his approved '
        'wording (OWNER-EDITS r13-anchor-backup), so they stay'),
    'b12-move-list': ('a12-move-list', [
        ('B312', 'The same goes after a stimulant or an unknown mixture, or with any medical concern.',
                 'Skip exercise too if you\'ve taken a stimulant or an unknown mixture, or have any other medical concern.')],
        'the Medium window: "The same goes" (skip everything above, or only exercise? the fit read: it alarms) said as '
        'what to skip; "after a stimulant" said as having taken one; "with any medical concern" said as theirs'),
    'b13-shadow-def': ('a13-shadow-def', [
        ('B344', '[Inner-child reparenting ](http://innerchild.u-dont-exist.com)is central.',
                 '[Inner-child reparenting](http://innerchild.u-dont-exist.com), giving yourself the parenting you missed, is central to this work.')],
        'the Medium window on the post\'s sentence: central to what said; the term explained where it is used (the fit '
        'read: "reparenting" read fast sounds like blaming or replacing your parents); the link\'s space put back '
        'outside it. His first sentence, Medium too, stays'),
    'b17-opposites': ('a17-opposites', [
        ('B414', 'In the subconscious world of concepts, however, two sides are often considered together.',
                 'In the subconscious world of concepts, however, the mind often keeps both together.')],
        'the Medium window: who considers them (the mind) said, the passive made active; "the two sides" (love and hate, '
        'or the Hermetic opposites? the his-fixes read) said as both, the love and hate just named'),
    'b19-appendix': ('a19-appendix', [
        ('B433', 'U.C. Berkeley', 'UC Berkeley')],
        'the Medium window, "U.C." read as a sentence of its own: the university\'s own spelling, UC Berkeley'),
}


# batch h57c: the next try from each near miss still below High after h57b (the ledger measures each from its lineage's
# best try with a Human window: a05, b08, a13, a17); built on the guide as it now stands (B214's fix is in)
TRIES_C = {
    'c05-dmso-overlap': ('a05-dmso-overlap', [
        ('B201', 'Sometimes DMSO works better; sometimes the water does.',
                 'Sometimes DMSO calms a trip better, and sometimes the charcoal water does.')],
        'from a05 (b05\'s two joins changed nothing): in the first Medium window, "the water" (plain water, or the '
        'charcoal water just named?) said as the charcoal water, and "works better" said as what it does better, calming '
        'a trip; the last sentence as the guide has it, its window the next try\'s'),
    'c08-niacin-forms': ('a08-niacin-forms', [
        ('B215', 'seem less reliable for relaxation.', 'seem less reliable than niacin for relaxation.'),
        ('B215', 'Niacinamide sometimes relaxes people and sometimes creates hyperfocus, depending on their state.',
                 'Niacinamide relaxes some people, but it can make others hyperfocused, depending on the state the person is in.'),
        ('B215', 'the useless non-flush hexanicotinate form.', 'the useless "no-flush" kind (inositol hexanicotinate).')],
        'from b08 (B214 now in the guide with its fix): the Medium window over B215, "their state" (what state?) said as '
        'the state they\'re in, and "sometimes ... and sometimes" built two ways, as his fixes build a pair'),
    'c13-shadow-def': ('a13-shadow-def', [
        ('B344', '[Inner-child reparenting ](http://innerchild.u-dont-exist.com)is central.',
                 '[Inner-child reparenting](http://innerchild.u-dont-exist.com) is central to shadow work.')],
        'from a13 (b13\'s explanation read worse, its three sentences one Medium window): only "central" said as central '
        'to what, the thing named, as his "the evidence for this med"; the link\'s space put back outside it'),
    'c17-opposites': ('a17-opposites', [
        ('B414', 'In the subconscious world of concepts, however, two sides are often considered together.',
                 'In the subconscious world of concepts, though, each idea often comes paired with its opposite.')],
        'from a17 (b17\'s "the mind ... both" read the same, Medium): what "two sides ... considered together" means said '
        'as what happens to a concept, it comes paired with its opposite, which is why the shadow thought shows up'),
}


def edited(base, edits):
    ids = BB.UNITS[base][0]
    md = {i: BB.md_of(i) for i in ids}
    for blk, old, new in edits:
        assert md[blk].count(old) == 1, (blk, old)
        md[blk] = md[blk].replace(old, new)
    return ids, md


if __name__ == '__main__':
    batch = sys.argv[1] if len(sys.argv) > 1 else 'h57b'
    which = {'h57b': TRIES, 'h57c': TRIES_C}[batch]
    items = []
    for key, (base, edits, why) in which.items():
        ids, md = edited(base, edits)
        t = '\n\n'.join(BB.plain(md[i]) for i in ids)
        (HERE / ('TEST-%s.txt' % key)).write_text(t + '\n', encoding='utf-8')
        (HERE / ('MD-%s.md' % key)).write_text('\n\n'.join(md[i] for i in ids) + '\n', encoding='utf-8')
        items.append([key, t, hashlib.sha256(t.encode('utf-8')).hexdigest()])
        near = {'c08-niacin-forms': 'b08-niacin-forms'}.get(key, base)
        a = (HERE / ('TEST-%s.txt' % near)).read_text(encoding='utf-8').split()
        b = t.split()
        import difflib
        sm = difflib.SequenceMatcher(None, a, b)
        changed = sum(max(i2 - i1, j2 - j1) for op, i1, i2, j1, j2 in sm.get_opcodes() if op != 'equal')
        print('%-20s %3d words, %2d changed (%.0f%%)' % (key, len(b), changed, 100.0 * changed / len(a)))
    (HERE / ('ITEMS-%s.json' % batch)).write_text(json.dumps(items, ensure_ascii=False) + '\n', encoding='utf-8')
