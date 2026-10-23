"""The induction section (HG17) from Emulate's sample bf, with the meaning put back that a reader would act on (2026-10-22).

Sample bf (fix-20261018/emu-bf/HG17-fx1.out.txt, made from the installed fixed section with Joel's 11 b) read Human in
every window of the first screening post (fix-20261022/screen/, Joel's result link of 21:41 UTC). Its second reader
compared it with the published section in three parts (VERIFY-part1.md to part3.md: kept 169, changed 52, lost 30, added
claims 10). Unlike the last sample (ba, every point put back in plain words, then AI in the guide), only what changes what a
reader does or believes goes back, each in the smallest edit inside bf's own sentence: an Opus reader per part drafted the
fixes against FIX-BRIEF-partN.md (FIXDRAFT-partN.json: 32 fixes, 3 links, 69 items let stand with a reason), and I read
each one. One draft fix is left out here: part 2's cut of "How does your body feel? Where are you grounded?" (two extra
orientation questions, harmless, and cutting them changes bf more). Joel's 11 b is in word for word.

The section keeps the published headings (the check doesn't read headings, and they carry three points bf's headings had
changed: what an induction does, "Contain before you deepen" and "when your mind likes to escape"). Where bf ran a heading
into a paragraph, the heading's words go and the paragraph keeps the rest: "Variations Open already" and "Staying awake"
are dropped; "Sleep Induction (different than inner work, ...):" becomes the sentence "Sleep induction is different than
inner work, ..."; "Fractionation (at some point in time you can add this, ...):" becomes "At some point in time you can
add this, ..."; "Trance Depth (if you want to check how deep you are):" goes, since the published heading "Optional trance
depth check" says it; "Deepening (...)" was a heading already. The list in "Before you begin" is numbered 1 to 6 (bf
switched to IV, V and VI after 3). The three published links go back on bf's words.

  python3 articles/inner-signal/humanize/fix-20261022/hg17-bf/make_hg17_bf_fixed.py   (from the repo root)
Writes HG17.bf-fixed.json (the units for tools/install_fixed.py), FIXES.json (each fix with the item it answers),
CHANGED-PARAS.json (each paragraph the fixes or the headings changed, bf's and now), SECTION.md
(the section as it will be installed) and CANDIDATE.md (the working copy with the section replaced; the 4.1 edits on top).
"""
import hashlib, json, pathlib, re, subprocess, sys

V = pathlib.Path(__file__).resolve().parent
H = V.parents[1]
REPO = H.parents[2]
sys.path.insert(0, str(H / 'tools'))
import install_fixed as IF  # noqa: E402

BF = H / 'fix-20261018' / 'emu-bf' / 'HG17-fx1.out.txt'
BF_SHA = 'ef88640d8e259d99924f8a9440437b6e5f8a1261a64b751f46bb3558210babb0'
LEAVE_OUT = {(2, 'How does your body feel? Where are you grounded? Can you feel')}
# Round 2: two drafted fixes brought linter rules bf's paragraph didn't have (lint-compare.json), so they are reworded with
# the same meaning: E23 (a paragraph of instructions) from "Look around and orient yourself.", and E36/E41 (heavy second
# person, from the shorter bracket) from "(make sure it is an appropriate time and place)".
REWORD = {(2, 'Orient yourself.'): 'Orient yourself by looking around.',
          (3, '(a good idea to pick an appropriate time and place)'): '(it needs to be an appropriate time and place)',
          # round 3: "You can change ..." brought E36/E41 (heavy second person) with the bracket's fix in the same paragraph
          (3, 'Be sure to change the direction you are going in, or stop this at some point.'):
              'It\'s fine to change the direction you are going in, or stop this at any point.'}
REWORD_ROUND = {(3, 'Be sure to change the direction you are going in, or stop this at some point.'): 3}
# Round 4: the stance check's findings (STANCE-HG17.md, read against the version before rounds 2 and 3), each inside bf's
# own sentence.
ROUND4 = [
    (33, 'and want to aim and stabilise it so that you can deepen it.', 'and want to aim and stabilise it.',
     'STANCE-HG17.md conflict 1: "so that you can deepen it" makes deepening the goal of the already-open practice, where '
     'the published practice says "The state is already open. I do not need to intensify it. I need to aim it, stabilize '
     'it, and keep it kind." and "Before you begin" calls it "for orientation, not permission to intensify an unstable state"'),
    (14, 'Preview, if you can, what you are going to do:', 'Preview what you are going to do:',
     'STANCE-HG17.md conflict 2: "if you can" makes the preview optional, where the published step has no hedge ("Preview '
     'eye closure, any repeated exit and re-entry, and the return.") and Appendix J makes it a step before every induction'),
    (14, 'You can also just open your eyes and be done.', 'You can also just open your eyes and stop, and then come all the way back anyway.',
     'STANCE-HG17.md conflict 3 (and the published text\'s own contradiction 2): "just open your eyes and be done" says an '
     'early stop needs no return, where the guide says "Use Come all the way back, even when you ended early." and "Use the '
     'complete waking return after every induction." (Appendix J); stopping stays a choice, and the return follows it'),
]
# (bf paragraph index, prefix as it reads after the fixes, what replaces it; None drops the paragraph)
RUN_IN = [(33, 'Variations Open already ', ''),
          (39, 'Staying awake ', ''),
          (50, 'Sleep Induction (different than inner work, where you need to come back up to write things down and do actions):',
           'Sleep induction is different than inner work, where you need to come back up to write things down and do actions.'),
          (53, 'Fractionation (at some point in time you can add this, but you must say you are doing it before doing it):',
           'At some point in time you can add this, but you must say you are doing it before doing it.'),
          (59, 'Trance Depth (if you want to check how deep you are):', None)]
NUMBERS = [(14, 'IV. ', '4. '), (15, 'V. ', '5. '), (16, 'VI. ', '6. ')]
# Round 2: the reviews' findings, each fixed inside bf's own sentence (bf paragraph index after the run-in headings and the
# fixes, old, new, the finding).
ROUND2 = [
    (15, 'The narrator can\'t add stuff if you don\'t say anything.',
     'The narrator can\'t add stuff just because you don\'t say anything.',
     'SENSE-HG17.md P12: "can\'t add stuff if you don\'t say anything" reads as what a narrator is able to do; the published '
     'point is that silence isn\'t a yes ("silence doesn\'t authorize a narrator to add something you haven\'t agreed to")'),
    (33, 'If you\'re already open for some reason', 'This is for when you\'re already open for some reason',
     'SENSE-HG17.md P30: with bf\'s run-in heading gone, the paragraph was an "if" with no "then", and the next one handed it '
     'back'),
    (72, 'For now, this will be over when you come out of it.', 'For now, today\'s trance will be over when you come out of it.',
     'SENSE-HG17.md P64: "this" could be the cue you were just told you can keep; the published says "Today\'s altered state '
     'ends with the return"'),
]
HEADINGS = {0, 3, 6, 10, 17, 44, 55, 64}
# (published blocks the stretch replaces, bf paragraphs, links: published anchor -> bf's words)
STRETCHES = [([1, 2], range(1, 3), {}),
             ([4, 5], range(4, 6), {}),
             ([7, 8, 9], range(7, 10), {}),
             ([11, 12, 13, 14, 15], range(11, 17), {'Utilization': 'Utilize'}),
             (list(range(17, 32)), range(18, 33), {}),
             ([33, 34, 35, 36, 37, 38], range(33, 39), {}),
             ([40, 41, 42, 43, 44, 45, 46], range(39, 44),
              {'hypnosis can become more alert rather than more relaxed':
               'Instead of getting more relaxed with the hypnosis, try getting more alert'}),
             ([48, 49, 50, 51, 52], range(45, 50), {}),
             ([54, 55], range(50, 53), {'Nimja’s sleep playlist': 'Nimja’s sleep playlist'}),
             ([57, 58], range(53, 55), {}),
             ([60, 61, 62], range(56, 59), {}),
             ([64, 65, 66, 67], range(59, 64), {}),
             ([69, 70, 71, 72, 73, 74, 75], range(65, 73), {})]
PUBLISHED_HEADINGS = [0, 3, 6, 10, 16, 32, 39, 47, 53, 56, 59, 63, 68]


def main():
    raw = BF.read_bytes()
    assert hashlib.sha256(raw).hexdigest() == BF_SHA
    paras = [p.strip() for p in re.split(r'\n\s*\n', raw.decode('utf-8')) if p.strip()]
    orig = list(paras)
    # the three parts the meaning check read, and the fixes on each
    cuts = [0, 33, 53, len(paras)]
    fixes = []
    for n in (1, 2, 3):
        part = '\n\n'.join(paras[cuts[n - 1]:cuts[n]])
        assert part + '\n' == (V / ('SAMPLE-part%d.txt' % n)).read_text(encoding='utf-8'), n
        draft = json.loads((V / ('FIXDRAFT-part%d.json' % n)).read_text(encoding='utf-8'))
        for f in draft['fixes']:
            if (n, f['old']) in LEAVE_OUT:
                fixes.append(dict(f, part=n, applied=False, note='left out: two harmless orientation questions; cutting them '
                                                                 'changes bf more'))
                continue
            assert part.count(f['old']) == 1, (n, f['old'])
            if (n, f['old']) in REWORD:
                f = dict(f, drafted=f['new'], new=REWORD[(n, f['old'])], note='reworded in round 2 for the linter')
            part = part.replace(f['old'], f['new'])
            fixes.append(dict(f, part=n, applied=True))
        ps = part.split('\n\n')
        assert len(ps) == cuts[n] - cuts[n - 1], n
        paras[cuts[n - 1]:cuts[n]] = ps
    for i, pre, new in RUN_IN:
        assert paras[i].startswith(pre), (i, paras[i][:80])
        paras[i] = None if new is None else (new + paras[i][len(pre):]).strip()
    for i, pre, new in NUMBERS:
        assert paras[i].startswith(pre), (i, paras[i][:20])
        paras[i] = new + paras[i][len(pre):]
    for rnd, items in ((2, ROUND2), (4, ROUND4)):
        for i, old, new, why in items:
            assert paras[i] is not None and paras[i].count(old) == 1, (i, old)
            paras[i] = paras[i].replace(old, new)
            fixes.append({'part': 'round %d' % rnd, 'p': 'bf %d' % i, 'old': old, 'new': new, 'answers': why, 'why': why,
                          'applied': True})
    changed = []
    for i, (w, n) in enumerate(zip(orig, paras)):
        if w != n:
            ans = [f['answers'] for f in fixes if f['applied'] and f['new'] and f['new'] in (n or '')]
            why = next((('run-in heading: "%s" goes' % pre.strip()) for j, pre, _ in RUN_IN if j == i), None) or \
                next(('the list numbered 1 to 6' for j, _, _ in NUMBERS if j == i), None)
            changed.append({'para': i, 'was': w, 'new': n, 'answers': ans, 'also': why})
    (V / 'CHANGED-PARAS.json').write_text(json.dumps(changed, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    fx = json.loads((H / 'fix-20261018' / 'rf-zg' / 'HG17.fixed.json').read_text(encoding='utf-8'))
    pub = {u['blocks'][0]: u for u in fx['units'] if u['kind'] == 'published'}
    assert sorted(pub) == PUBLISHED_HEADINGS
    units, si = [], 0
    for b in range(76):
        if b in pub:
            units.append(pub[b])
        elif si < len(STRETCHES) and STRETCHES[si][0][0] == b:
            blocks, idx, links = STRETCHES[si]
            ps = [paras[i] for i in idx if paras[i] is not None and i not in HEADINGS]
            units.append({'kind': 'emulate', 'blocks': blocks, 'paras': ps, 'run': 'HG17-fx1',
                          'file': str(BF.relative_to(REPO)), 'links': [{'published': k, 'new': v} for k, v in links.items()]})
            si += 1
    assert si == len(STRETCHES)
    out = {'key': 'HG17', 'from': 'fix-20261018/emu-bf/HG17-fx1.out.txt (sample bf), with make_hg17_bf_fixed.py',
           'choices': {'base': 'rf-zg/HG17.fixed.json (its published headings and block map)', 'sample': 'emu-bf'},
           'units': units,
           'note': 'the points a reader would act on put back in bf\'s own sentences (FIXDRAFT-partN.json, read one by one), '
                   'Joel\'s 11 b word for word, the published headings, three links'}
    (V / 'HG17.bf-fixed.json').write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    (V / 'FIXES.json').write_text(json.dumps(fixes, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    sec = IF.section_md(V / 'HG17.bf-fixed.json')
    (V / 'SECTION.md').write_text(sec + '\n', encoding='utf-8')
    md = (H / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
    a = md.index('# Induction: gathering attention without disappearing\n')
    b = md.index('\n# ', a + 5)
    cand = md[:a] + sec + '\n' + md[b:]   # the section's span ends with the newline before the blank line and the next h1
    (V / 'CANDIDATE.md').write_text(cand, encoding='utf-8')
    r = subprocess.run([sys.executable, '-c', 'import sys; sys.path.insert(0, %r); import apply_edits41 as E; '
                        'md = open(%r, encoding="utf-8").read(); out, ap, done = E.apply(md, E.load()); '
                        'print("4.1 edits: applied", ap, "; in", len(done))' % (str(H / 'fix-20261020'), str(V / 'CANDIDATE.md'))],
                       capture_output=True, text=True, cwd=REPO)
    print(r.stdout.strip() or r.stderr.strip()[-800:])
    print('fixes applied %d of %d; section %d words (was %d); units %d'
          % (sum(f['applied'] for f in fixes), len(fixes), len(sec.split()), len(md[a:b].split()), len(units)))


if __name__ == '__main__':
    main()
