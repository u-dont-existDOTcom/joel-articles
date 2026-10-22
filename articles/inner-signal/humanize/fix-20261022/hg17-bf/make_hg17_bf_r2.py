"""The induction section from sample bf, round 2 (2026-10-22): the reviews' findings fixed, and their re-reads.

Round 1's reviews (FIX-CHECK.md, SENSE-HG17.md, STANCE-HG17.md, march/) found what make_hg17_bf_fixed.py's ROUND2 list
fixes, each inside bf's own sentence, and two drafted fixes were reworded because they brought linter rules bf's
paragraph didn't have (its REWORD list; lint-compare.json). This builds, from the section as it is now:

  r2/VERIFY-r2-PROMPT.txt   for Opus: each paragraph round 2 changed, in its place, against the finding it answers
                            (-> r2/VERIFY-r2.md)
  r2/march/                 for Sonnet: bf's paragraph and the round 2 one (-> r2/march/march-labels.txt)

  python3 articles/inner-signal/humanize/fix-20261022/hg17-bf/make_hg17_bf_r2.py [--round 3]   (from the repo root, after make_hg17_bf_fixed.py)
Round 3 is the same for make_hg17_bf_fixed.py's ROUND3 (the stance check's findings) and the REWORD entries of round 3.
"""
import json, pathlib, re, sys

V = pathlib.Path(__file__).resolve().parent
H = V.parents[1]
REPO = H.parents[2]
sys.path.insert(0, str(V))
sys.path.insert(0, str(REPO / 'tools' / 'humanization' / 'reviewer'))
import make_hg17_bf_fixed as F  # noqa: E402
import reviewer as R  # noqa: E402

ABOUT = ('a long self-help guide to self-hypnosis ("the inner child", "the Nurturer", "the Protector", "the Guide" and '
         '"childhood protector parts" are the guide\'s terms; much of this part is a script the reader records or says to '
         'themselves)')


def main():
    changed = {c['para']: c for c in json.loads((V / 'CHANGED-PARAS.json').read_text(encoding='utf-8'))}
    section = (V / 'SECTION.md').read_text(encoding='utf-8')
    plain = [re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', re.sub(r'^#+\s*', '', b)) for b in section.split('\n\n') if b.strip()]
    items, paras = [], set()
    rnd = int(sys.argv[sys.argv.index('--round') + 1]) if '--round' in sys.argv else 2
    rounds = [(i, old, new, why) for i, old, new, why in (F.ROUND2 if rnd == 2 else F.ROUND3)]
    for (part, old), new in F.REWORD.items():
        if F.REWORD_ROUND.get((part, old), 2) != rnd:
            continue
        i = next(k for k, c in changed.items() if c['new'] and new in c['new'])
        fx = next((f for f in json.loads((V / 'FIXES.json').read_text(encoding='utf-8')) if f.get('old') == old), {})
        rounds.append((i, old, new, 'the meaning check found: %s. The drafted fix ("%s") brought a linter rule bf\'s paragraph '
                                    'didn\'t have (lint-compare.json), so it is reworded with the same meaning'
                                    % (fx.get('answers', '?'), fx.get('drafted', '?'))))
    R_ = 'r%d' % rnd
    for n, (i, old, new, why) in enumerate(rounds, 1):
        c = changed[i]
        k = next(j for j, b in enumerate(plain) if b.strip() == c['new'].strip())
        items.append(('## Item %d (bf paragraph %d)\n\nTHE FINDING:\n%s\n\nTHE ROUND ' + str(rnd) + ' CHANGE:\n"%s" -> "%s"\n\nBEFORE:\n%s\n\n'
                      'NOW:\n%s\n\nAFTER:\n%s\n') % (n, i, why, old, new, plain[k - 1], c['new'],
                                                    plain[k + 1] if k + 1 < len(plain) else ''))
        paras.add(i)
    head = (
        "You check %d fixes in one section of Joel's long self-hypnosis guide: the induction (preparation, a spoken "
        "listening script, the already-open and stay-awake practices, the two-hand and sleep inductions, fractionation, "
        "deepening, a trance depth check and a shortcut back into hypnosis). The section is a paraphrasing tool's rewrite "
        "of Joel's published section with its meaning put back in small edits; reviewers then found the problems below, "
        "and round ROUNDNUM fixed each inside the rewrite's own sentence. The guide is self-guided: the reader leads themselves, "
        "reading it or using a recording they made. For each item you get THE FINDING, THE ROUND CHANGE, and the "
        "paragraph NOW with BEFORE and AFTER around it.\n\nFor each item, say in a few words each:\n1. FIXED: is the "
        "finding answered in NOW? YES, or what is left.\n2. MEANING: does the change keep everything else the paragraph "
        "said? KEPT, or what changed.\n3. SENSE: would a reader who has read the guide up to here understand NOW in its "
        "place? OK, or the words that stop them and why.\nEnd each item with one line, `VERDICT: OK` or `VERDICT: CHANGED`. "
        "Judge meaning and sense only, not style, and suggest a rewrite only for a problem you report.\n\nWrite your report "
        "with a single Write call to `%s`, one \"## Item N\" part per item, then reply with only the verdicts, one line per "
        "item. Don't read any other file, don't run commands, and don't use the web.\n\n" % (len(items), V / R_ / ('VERIFY-%s.md' % R_)))
    head = head.replace('ROUNDNUM', str(rnd))
    (V / R_).mkdir(exist_ok=True)
    (V / R_ / ('VERIFY-%s-PROMPT.txt' % R_)).write_text(head + '\n'.join(items), encoding='utf-8')
    texts, mp = [], []
    for i in sorted(paras):
        for ver, q in (('was', changed[i]['was']), ('new', changed[i]['new'])):
            k = len(R.march_paragraphs(q))
            if k:
                texts.append(q)
                mp.append({'para': i, 'ver': ver, 'n': k, 'start': sum(m['n'] for m in mp)})
    M = V / R_ / 'march'
    M.mkdir(exist_ok=True)
    draft = '\n\n'.join(texts)
    (M / 'march-draft.txt').write_text(draft + '\n', encoding='utf-8')
    (M / 'march-map.json').write_text(json.dumps(mp, indent=1) + '\n', encoding='utf-8')
    prompt = R.build_march(draft, ABOUT)
    prompt += ('\n\nWrite exactly those lines, one per paragraph from T1 to T%d, with a single Write call to `%s`, then reply '
               'with only "done". Don\'t read any other file, don\'t run commands, and don\'t use the web.\n'
               % (sum(m['n'] for m in mp), M / 'march-labels.txt'))
    (M / 'march-prompt.txt').write_text(prompt, encoding='utf-8')
    print('%s: %d items; %d march paragraphs' % (R_, len(items), len(texts)))


if __name__ == '__main__':
    main()
