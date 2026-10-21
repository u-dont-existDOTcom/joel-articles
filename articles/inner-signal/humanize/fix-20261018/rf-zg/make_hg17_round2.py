"""Rounds 2 on of HG17's reviews (2026-10-21): the paragraphs a round of reviews changed (make_hg17_fixed.py, REVIEWS,
each edit tagged with its round), each read again for its meaning against the published passage, its sense in its place,
and the finding it answers; and the march read of each of them.

Run after make_hg17_fixed.py:
  python3 articles/inner-signal/humanize/fix-20261018/rf-zg/make_hg17_round2.py [--round N] [--parts]   (from the repo root)
Writes HG17-section.md and CANDIDATE.md from the text as it now stands (as make_hg17_reviews.py does), and in rN/:
  VERIFY-rN-PROMPT.txt            one Opus reader -> rN/VERIFY-rN.md
  march-draft.txt, march-map.json, march-prompt.txt   one Sonnet reader -> rN/march-labels.txt (ba's version of a
                                  paragraph first changed in this round, and every paragraph's version after it; the
                                  others' labels are an earlier round's, march/ for round 1)
With --parts (round 2), also the meaning check of the whole fixed section in three parts, in this folder
(HG17.fixed.verify.partN.prompt.txt, a Sonnet reader each -> HG17.fixed.verify.partN.out.md): round 1's single prompt
ran past its reader's output limit. Round 2 was run with --parts; round 3 answers the parts' findings.
"""
import argparse, json, pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parents[1]
REPO = H.parents[2]
sys.path.insert(0, str(H / 'tools'))
sys.path.insert(0, str(H / 'fix-20261020'))
sys.path.insert(0, str(REPO / 'tools' / 'humanization' / 'reviewer'))
import install_fixed as I     # noqa: E402
import apply_edits41 as E41   # noqa: E402
import reviewer as R          # noqa: E402

FIXED = HERE / 'HG17.fixed.json'
ABOUT = ('a long self-help guide to self-hypnosis ("the inner child", "the Nurturer", "the Adult" and "protectors" are '
         'the guide\'s terms; much of this part is a script the reader records or says to themselves)')
# each changed paragraph's published passage: the blocks of the published section (P0 is its heading), as the meaning
# check numbers them (HG17.ba.verify.out.md)
PUB = {(7, 1): [11], (7, 2): [12], (7, 3): [13], (7, 4): [14], (7, 5): [15], (9, 0): [17], (9, 5): [22], (9, 7): [24],
       (9, 8): [25], (9, 11): [28], (9, 12): [30], (11, 2): [35], (11, 3): [36], (11, 4): [37, 38], (17, 0): [54],
       (21, 1): [61], (23, 4): [67], (25, 3): [70, 71], (25, 5): [72], (25, 6): [73], (25, 8): [75]}
HEAD = (
    "You check {n} edited paragraphs of the induction section of a long self-hypnosis guide by Joel. The section was "
    "rewritten in a plainer, more personal voice, and its looser wording is fine. Each paragraph below was changed after "
    "an earlier review found something in it. For each item you get PUBLISHED (what the published guide says for that "
    "passage), BEFORE and AFTER (the paragraphs around it in the rewritten section), EARLIER FINDING (what the review "
    "found) and EDITED (the paragraph now).\n\n"
    "For each item, say in a few words each:\n"
    "1. MEANING: for every point of PUBLISHED (a claim, a step, a caution, a condition, a choice the reader is given, a "
    "hedge such as \"may\", a link), KEPT, CHANGED (how a reader would now understand or do it differently) or LOST in "
    "EDITED; then anything EDITED adds that a reader would act on or believe (ADDED).\n"
    "2. SENSE: would a reader who has read the guide up to here understand every sentence of EDITED in its place, between "
    "BEFORE and AFTER? OK, or the words that stop them and why. Give your best reading of words before calling them "
    "unclear, and leave them out when that reading is clearly what the writer means.\n"
    "3. FINDING: is the earlier finding answered? ANSWERED, or STILL and why.\n"
    "End each item with one line, `VERDICT: OK` (everything kept, nothing added, sense OK, finding answered) or "
    "`VERDICT: CHANGED`. Judge meaning and sense only, not style or which version is better, and don't suggest rewrites "
    "unless a finding is STILL.\n\n"
    "Write your report with a single Write call to `{out}`, one \"## Item N\" part per item, then reply with only the "
    "verdicts, one line per item. Don't read any other file, don't run commands, and don't use the web.\n\n")


SPLIT = ('## Already open? Contain before you deepen', '## Optional fractionation: practice coming back')
PART_NOTE = (
    "\n\nThis prompt is part {k} of 3: the section is checked in three parts, split at the same headings in both texts, so "
    "that each report stays short. THE PUBLISHED SECTION and THE REWRITE below are that part only, and the blocks are "
    "numbered from P{first}. Keep each line short and the whole report under 1,200 words.")


def verify_parts(md):
    """The meaning check in three parts (2026-10-21: the whole-section check, the prompt sample ba had, ran past the
    reader's 64,000-token output limit on the fixed text and wrote nothing). Each part is the published blocks and the
    rewrite's blocks between the same headings, with the same instructions and its own report."""
    head = (HERE / 'HG17.ba.verify.prompt.txt').read_text(encoding='utf-8').split('THE PUBLISHED SECTION:')[0]
    head = head.replace('The rewrite was made by a paraphrasing tool that writes in a plainer, more personal voice; its '
                        'looser wording is fine.',
                        'The rewrite was made by a paraphrasing tool that writes in a plainer, more personal voice, and '
                        'then edited; its looser wording is fine.')
    pub = published_blocks()
    new = [b for b in md.split('\n\n') if b.strip()]
    pi = [0] + [pub.index(s) for s in SPLIT] + [len(pub)]
    ni = [0] + [new.index(s) for s in SPLIT] + [len(new)]
    out = []
    for k in range(3):
        path = HERE / ('HG17.fixed.verify.part%d.out.md' % (k + 1))
        h = head.replace(str(HERE / 'HG17.ba.verify.out.md'), str(path))
        h = h.replace('(P0 is the heading; count every', '(P%d is the first block below; count every' % pi[k])
        assert str(path) in h and 'P0 is the heading' not in h
        h = h.rstrip() + PART_NOTE.format(k=k + 1, first=pi[k]) + '\n\n'
        text = (h + 'THE PUBLISHED SECTION:\n\n' + '\n\n'.join(pub[pi[k]:pi[k + 1]]) + '\n\nTHE REWRITE:\n\n'
                + '\n\n'.join(new[ni[k]:ni[k + 1]]) + '\n')
        p = HERE / ('HG17.fixed.verify.part%d.prompt.txt' % (k + 1))
        p.write_text(text, encoding='utf-8')
        out.append(p)
    return out


def published_blocks():
    t = (HERE / 'HG17.ba.verify.prompt.txt').read_text(encoding='utf-8')
    pub = t.split('THE PUBLISHED SECTION:')[1].split('THE REWRITE:')[0].strip()
    return [b for b in pub.split('\n\n') if b.strip()]


def main():
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('--round', type=int, default=2)
    ap.add_argument('--parts', action='store_true', help='also write the three-part meaning check (round 2)')
    a = ap.parse_args()
    rnd = a.round
    out = HERE / ('r%d' % rnd)
    out.mkdir(exist_ok=True)
    md = I.section_md(FIXED)
    (HERE / 'HG17-section.md').write_text(md + '\n', encoding='utf-8')
    art = (H / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
    cand, notes = I.install(art, [FIXED])
    (HERE / 'CANDIDATE.md').write_text(cand, encoding='utf-8')
    edits = E41.load()
    broken = [e['key'] for i, e in enumerate(edits) if not (E41.is_in(cand, e) or E41.superseded(e, edits[i + 1:], cand))]
    print('install notes:', notes or 'none', '| 4.1 edits not in the candidate:', broken or 'none')

    allfx = [x for x in json.loads((HERE / 'FIXES.json').read_text(encoding='utf-8')) if x.get('reviews')]
    missing = {(x['unit'], x['para']) for x in allfx} - set(PUB)
    assert not missing, 'PUB must name every paragraph a review round changed: %r' % (missing,)
    fixes = [x for x in allfx if rnd in x.get('rounds', [])]
    pub = published_blocks()
    blocks = [b for b in md.split('\n\n') if b.strip()]
    items = []
    for n, x in enumerate(fixes, 1):
        start = x['new'][:40]
        at = [i for i, b in enumerate(blocks) if b.startswith(start)]
        assert len(at) == 1, (x['unit'], x['para'], start)
        i = at[0]
        found = [f for f, r in zip(x['reviews'], x['rounds']) if r == rnd]
        items.append('## Item %d\n\nPUBLISHED:\n%s\n\nBEFORE:\n%s\n\nAFTER:\n%s\n\nEARLIER FINDING:\n%s\n\nEDITED:\n%s\n' % (
            n, '\n\n'.join(pub[k] for k in PUB[(x['unit'], x['para'])]), blocks[i - 1], blocks[i + 1] if i + 1 < len(blocks)
            else '(the section ends here)', '\n'.join('- ' + f for f in found), blocks[i]))
    name = 'VERIFY-r%d' % rnd
    (out / (name + '-PROMPT.txt')).write_text(HEAD.format(n=len(items), out=out / (name + '.md')) + '\n'.join(items),
                                              encoding='utf-8')

    paras, mp = [], []
    for x in fixes:
        first = min(x['rounds']) == rnd and x['kind'] == 'review'
        for ver in (('was', 'new') if first else ('new',)):
            k = len(R.march_paragraphs(x[ver]))
            if k:
                paras.append(x[ver])
                mp.append({'unit': x['unit'], 'para': x['para'], 'ver': ver, 'n': k, 'start': sum(m['n'] for m in mp)})
    draft = '\n\n'.join(paras)
    (out / 'march-draft.txt').write_text(draft + '\n', encoding='utf-8')
    (out / 'march-map.json').write_text(json.dumps(mp, indent=1) + '\n', encoding='utf-8')
    prompt = R.build_march(draft, ABOUT)
    prompt += ('\n\nWrite exactly those lines, one per paragraph from T1 to T%d, with a single Write call to `%s`, then reply '
               'with only "done". Don\'t read any other file, don\'t run commands, and don\'t use the web.\n'
               % (sum(m['n'] for m in mp), out / 'march-labels.txt'))
    (out / 'march-prompt.txt').write_text(prompt, encoding='utf-8')
    parts = verify_parts(md) if a.parts else []
    print('round %d:' % rnd, len(items), 'items;', sum(m['n'] for m in mp), 'march paragraphs;', ' '.join(
        '%s %d words' % (p.name, len(p.read_text(encoding='utf-8').split())) for p in parts))


if __name__ == '__main__':
    main()
