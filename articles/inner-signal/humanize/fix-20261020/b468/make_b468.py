"""Batch 468g (2026-10-21): the second tries for batch 467g's two misses, and the two lines of Appendix F that read AI in
its section check.

Batch 467g (../b467/batch/b467-results.json) passed four edits, installed through ../apply_edits41.py. Two read AI:
HG15-p9e ("Those can all be real gifts, but if ..., it has become a way to buy belonging.", AI medium) and HG35-forgive-e2
(the forgiveness list as two couplets, AI medium and high). The section check of Appendix F (HG35-w467) also read two
installed lines AI, low: the adult's three short promises (HG35-p15) and the two self-forgiveness instructions (HG35-p18),
both light green in the whole guide (part B). Each edit below names what the miss or the red line showed and the
mechanism it tries instead, with the evidence for it; every point of the installed paragraph is kept.

  python3 articles/inner-signal/humanize/fix-20261020/b468/make_b468.py   (from the repo root)

Writes CANDIDATE.md (the working copy with the edits), drafts.json (each changed paragraph as Pangram reads it: alone,
or with the neighbor tools/humanization/paragraphs_alone.py accepts when it is under 50 words; and each section whole,
for the recheck after the paragraphs pass), the march draft and map, REWRITE.md (for the stance check) and
VERIFY-PROMPT.txt (the meaning check of each edit against the installed paragraph).
"""
import json, pathlib, sys

REPO = pathlib.Path(__file__).resolve().parents[5]
H = REPO / 'articles' / 'inner-signal' / 'humanize'
OUT = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(H / 'tools'))
sys.path.insert(0, str(REPO / 'tools' / 'humanization'))
sys.path.insert(0, str(REPO / 'tools' / 'humanization' / 'reviewer'))
import sections as S          # noqa: E402
import paragraphs_alone as PA  # noqa: E402
import reviewer as R          # noqa: E402

BATCH = '468'
EDITS = [
    {'key': 'HG15-p9e2', 'lineage': 'HG15-p9', 'section': 'HG15', 'kind': 'edit', 'with': None,
     'old': "Those can all be real gifts. They become a bargain for belonging when failing in these areas feels like losing "
            "yourself.",
     'new': "I’m not saying those can’t be real gifts, but if failing at one of them feels like losing yourself, then you’re "
            "using it to buy belonging.",
     'was_try': 'HG15-p9e (467g, try 1): "Those can all be real gifts, but if failing at one of them feels like losing '
                'yourself, it has become a way to buy belonging." read AI, medium (the whole sentence)',
     'diagnosis': 'try 1 still closed on a concession and a reframe in one balanced sentence, with the reframe said as what '
                  'the gifts "have become". Try 2 says the concession as the author\'s own position, in the frame that read '
                  'dark green in Joel\'s community final under 4.1 ("I\'m not saying paid help can\'t be good sometimes, but '
                  'to me it seems way too much of a gamble if I have a better alternative.", '
                  'articles/intentional-communities/candidate/joel-20261020/PANGRAM41-EDITS.md, run 9), and the reframe as '
                  'what the reader does, as the paragraph\'s own second sentence has the reader doing it ("you will try to '
                  'become good enough as a human doer"). Round 1 said "your sense of belonging", from the section\'s '
                  'questions; the meaning check read that as a felt state rather than belonging itself (r1/VERIFY.md, pair '
                  '1), so it is "belonging" as installed'},
    {'key': 'HG35-forgive-e3', 'lineage': 'HG35-p13', 'section': 'HG35', 'kind': 'edit', 'with': None,
     'old': "We simply remember that it can all be true: the harm happened, the boundary still matters, the person is still "
            "accountable, and forgiveness may come later on its own.",
     'new': "We just remember that it can all be true at once. They really did hurt us and they still have to answer for it, "
            "and our boundary with them still matters, but one day we may find that we have forgiven them.",
     'was_try': 'HG35-forgive-e2 (467g, try 1): "... at once. The harm happened, and the boundary still matters. The person '
                'is still accountable, and forgiveness may come later on its own." read AI, medium and high (each couplet); '
                'its first sentence read Human, low',
     'diagnosis': 'try 1 split the colon list into two balanced couplets, so the four points stayed four crisp abstract '
                  'clauses ("the harm", "the boundary", "the person", "forgiveness") in parallel, ending on the '
                  'reassurance. Try 2 keeps its first sentence (Human) and says the points about the people ("They really did '
                  'hurt us and they still have to answer for it"), in one uneven sentence joined by "and" and "but", with the '
                  'forgiveness as something we may find has happened rather than a fourth item (no "anyway" at the end: the '
                  'linter\'s finished-principle check, B1, has it): the published list\'s '
                  'abstractions are what 4.1 read, and the clauses that read Human in this section are about people '
                  '("they could only make the moves they made", the paragraph after)'},
    {'key': 'HG35-quote-e', 'lineage': 'HG35-p15', 'section': 'HG35', 'kind': 'edit', 'with': 'prev',
     'old': "“You don’t have to forgive before you’re ready. I won’t use spirituality to silence your pain. And I won’t build "
            "our whole life around this wound forever.”",
     'new': "“You don’t have to forgive before you’re ready. I’m not going to use spirituality to silence your pain, and I "
            "also won’t build our whole life around this wound forever.”",
     'was_try': 'installed (453g HG35-rfix, Pangram 4.0, 100% Human); Pangram 4.1, the section check HG35-w467: its first two '
                'sentences read AI, low (19 words), the third Human; light green in the whole guide (part B)',
     'diagnosis': 'three short parallel declaratives, the first two a stock reassurance ("You don\'t have to forgive before '
                  'you\'re ready.") and a polished one-line promise (pattern 3, tidy reassurance); the third, with "our whole '
                  'life", read Human. The two promises are said as one spoken sentence, the way the adult talks to the child '
                  '(Emulate\'s own rendering of this line was one run-on: fix-20261018/emu-c/HG35-r1-s5.out.txt), so the red '
                  'one is read with the one that read Human, every promise kept. Round 1 put all three in one sentence: the '
                  'march read the installed line B S S and that S, so the permission, its break, went (r1/march-labels.txt, '
                  'T5 and T6), and the meaning check found "forgive them" narrowing whom to forgive and "but I also" setting '
                  'the last promise against the others (r1/VERIFY.md, pair 3); so the permission stays its own sentence, as '
                  'installed, and the promises are joined by "and". Under 50 words, so it is checked with the paragraph '
                  'before it (Human, high in the section check)'},
    {'key': 'HG35-selfforgive-e', 'lineage': 'HG35-p18', 'section': 'HG35', 'kind': 'edit', 'with': 'next',
     'old': "For self-forgiveness, name what you did, without taking responsibility for what wasn't yours. Let the remorse "
            "register the harm, or how it went against your values, without making yourself a permanent criminal.",
     'new': "For self-forgiveness, name what you did, but don't take responsibility for what wasn't yours. Let yourself feel "
            "the remorse and take in the harm, or how it went against your values, and stop short of making yourself a "
            "permanent criminal.",
     'was_try': 'installed (453g HG35-rfix, Pangram 4.0, 100% Human); Pangram 4.1, the section check HG35-w467: the paragraph '
                'read AI, low (34 words); light green in the whole guide (part B)',
     'diagnosis': 'two parallel imperatives, each closing on a "without ...ing" clause (pattern 4; E186, which the linter '
                  'found in 13% of the paragraphs that read AI and 3% of those that read Human), and remorse as the one doing '
                  'it ("Let the remorse register the harm", W78). The person feels the remorse and takes in the harm, and '
                  'the two cautions are said in different shapes ("but don\'t take responsibility for ...", "and stop short '
                  'of making yourself ..."), so the two sentences no longer share one. Round 1 said "take responsibility only '
                  'for what was yours" and "feel remorse for the harm": the meaning check read the first as a new instruction '
                  'to own your part and the second as losing what the remorse is for, registering the harm (r1/VERIFY.md, '
                  'pair 4). Under 50 words, so it is checked with the paragraph after it (Human in the section check)'},
]
SECTIONS = {'HG15': 'When “your voice” is everybody else’s voice',
            'HG35': 'Appendix F: Self-trust, outside guidance, and oracle-like states'}


def main():
    md = (H / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
    blocks = md.split('\n\n')
    paras = {}
    for e in EDITS:
        assert md.count(e['old']) == 1, (e['key'], md.count(e['old']))
        para = next(b for b in blocks if e['old'] in b)
        paras[e['key']] = (para, para.replace(e['old'], e['new']))
        md = md.replace(e['old'], e['new'])
    (OUT / 'CANDIDATE.md').write_text(md, encoding='utf-8')
    editor = H / 'source' / 'substack-editor-20260928.html'
    secs = {h: bl for h, bl in S.sections(md, str(editor))}
    drafts, meta = {}, {}
    pp = PA.paragraphs(md)
    for e in EDITS:
        was, new = paras[e['key']]
        i = next(j for j, (_, p) in enumerate(pp) if p == new.strip())
        t, tries = PA.tries_for(md, pp, i)
        if e['with'] is None:
            text = t
        else:
            j = i - 1 if e['with'] == 'prev' else i + 1
            assert pp[j][0] == pp[i][0], (e['key'], 'the neighbor is under another heading')
            text = PA.plain(pp[j][1]) + '\n\n' + t if e['with'] == 'prev' else t + '\n\n' + PA.plain(pp[j][1])
        assert text in tries and len(text.split()) >= 50, (e['key'], len(text.split()))
        drafts[e['key']] = text
        meta[e['key']] = {'section': e['section'], 'lineage': e['lineage'], 'words': len(text.split()), 'was_md': was,
                          'new_md': new, 'with': e['with']}
    for key, title in SECTIONS.items():
        bl = secs['# ' + title]
        k = '%s-w%s' % (key, BATCH)
        drafts[k] = S.text_of(bl)
        meta[k] = {'section': key, 'words': len(drafts[k].split()), 'parts': [e['key'] for e in EDITS if e['section'] == key]}
        (OUT / ('%s-section.md' % key)).write_text('\n\n'.join(m for m, _ in bl) + '\n', encoding='utf-8')
    (OUT / 'drafts.json').write_text(json.dumps(drafts, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    (OUT / 'meta.json').write_text(json.dumps({'edits': EDITS, 'texts': meta}, ensure_ascii=False, indent=1) + '\n',
                                   encoding='utf-8')
    # the march draft: each edited paragraph as installed and as edited, in turn
    mparas, mp = [], []
    for e in EDITS:
        for ver, p in (('was', paras[e['key']][0]), ('new', paras[e['key']][1])):
            p = S.plain(p)
            n = len(R.march_paragraphs(p))
            if n:
                mparas.append(p)
                mp.append({'key': e['key'], 'ver': ver, 'n': n, 'start': sum(m['n'] for m in mp)})
    if not (OUT / 'march-labels.txt').exists():
        (OUT / 'march-draft.txt').write_text('\n\n'.join(mparas), encoding='utf-8')
        (OUT / 'march-map.json').write_text(json.dumps(mp, indent=1) + '\n', encoding='utf-8')
    rw = []
    for key, title in SECTIONS.items():
        rw.append('# ' + title)
        rw += [paras[e['key']][1] for e in EDITS if e['section'] == key]
    (OUT / 'REWRITE.md').write_text('\n\n'.join(rw) + '\n', encoding='utf-8')
    pairs = []
    for i, e in enumerate(EDITS, 1):
        was, new = paras[e['key']]
        pairs.append('## Pair %d (%s)\n\nINSTALLED:\n%s\n\nEDITED:\n%s\n' % (i, e['key'], S.plain(was), S.plain(new)))
    prompt = (
        "You check that a small edit of a paragraph keeps its meaning. Below are %d pairs from a long self-hypnosis guide by "
        "Joel, written in his first person. In each pair the INSTALLED paragraph is the one in the guide now and the EDITED "
        "one changes a sentence or two of it.\n\nFor each pair, list every point the installed paragraph makes (a claim, a "
        "fact about Joel, a step, a caution, a condition, a hedge such as \"I suspect\" or \"may\") and say whether the edited "
        "paragraph keeps it: KEPT, CHANGED (how a reader would now understand it differently) or LOST. Then list anything the "
        "edited paragraph says that the installed one doesn't: ADDED. Judge meaning only, not style or which version is "
        "better, and don't suggest rewrites. Keep your reasoning short.\n\nWrite your report with a single Write call to "
        "`%s`, one \"## Pair N\" part per pair, ending each with one line `VERDICT: OK` (every point kept, nothing added) or "
        "`VERDICT: CHANGED` (anything changed, lost or added), then reply with only the verdicts. Don't read any other file, "
        "don't run commands, and don't use the web.\n\n%s" % (len(EDITS), OUT / 'VERIFY.md', '\n'.join(pairs)))
    (OUT / 'VERIFY-PROMPT.txt').write_text(prompt, encoding='utf-8')
    for k, v in drafts.items():
        print(k, len(v.split()), 'words')
    print(len(mp), 'march paragraphs')


if __name__ == '__main__':
    main()
