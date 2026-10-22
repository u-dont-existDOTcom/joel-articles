"""Batch 470g, round 2 (2026-10-22): the fixes for round 1's findings, and their re-reads.

Round 1 (now in r1/): the item review (REVIEW.md) marked items 1, 10, 11, 21 and 24 CHANGED; the cold read of the h1
(SENSE-HG14.md) asked the same as item 11; the stance check is STANCE.md. Round 2 changes four of them in make_b470.py's
list, with the reviewer's own wording:
  1  guard-first-read  the new name was given but not explained at its first read: "guard mind (your childhood protector
                       parts, the protective reactions you learned as a child)"
  10 parent-script     "it may jump in" put "it" right after "your child", and the guide calls the inner child "it": "the
                       script may jump in"
  11 to-the-part       right after the script "may jump in", "the protector part" could be the script; the published line
                       was said to the protector (b469's sweep, finding 1): "(To the guard, the childhood protector part:"
  21 synchronicity     without its second "my", "a childhood protector part" could describe the Inner Child: "from a
                       childhood protector part"
Item 24 (Appendix B's "Put 3 good adults in with the person") goes to Joel as question 12 c: the reviewer's own reading was
that it's his call whether the NLP step needs three figures.

Writes r2/VERIFY-r2-PROMPT.txt (Opus: each round 1 finding against the fixed paragraph in its place, -> r2/VERIFY-r2.md) and
r2/march/ (Sonnet: the installed paragraph and the round 2 one, -> r2/march/march-labels.txt), after rebuilding the batch
with make_b470.py --edits-only.

  python3 articles/inner-signal/humanize/fix-20261022/b470/make_b470_r2.py   (from the repo root)
"""
import json, pathlib, re, shutil, subprocess, sys

B = pathlib.Path(__file__).resolve().parent
REPO = B.parents[4]
sys.path.insert(0, str(B))
sys.path.insert(0, str(REPO / 'tools' / 'humanization' / 'reviewer'))
sys.path.insert(0, str(B.parents[1] / 'tools'))
import reviewer as R   # noqa: E402
import sections as S   # noqa: E402

R1 = B / 'r1'
R2 = B / 'r2'
CHANGED = {'guard-first-read': 1, 'parent-script': 10, 'to-the-part': 11, 'synchronicity': 21}
COLD = {'to-the-part': 'P45 "To the protector part": the guard of P43, or the parent script P44 says "may jump in"?'}


def finding(review, n):
    part = re.split(r'(?m)^## Item ', review)
    p = next(x for x in part[1:] if x.split()[0] == str(n))
    return '## Item ' + p.strip()


def main():
    R1.mkdir(exist_ok=True)
    # the stance check's prompt and report move to r1/ when its reader is done (it was still reading at round 2's start)
    for f in ('REVIEW-PROMPT.txt', 'REVIEW.md', 'SENSE-HG14.md', 'sense', 'march') + (('STANCE.md', 'stance') if (B / 'STANCE.md').exists() else ()):
        src = B / f
        if src.exists() and not (R1 / f).exists():
            shutil.move(str(src), str(R1 / f))
    r = subprocess.run([sys.executable, str(B / 'make_b470.py'), '--edits-only'], capture_output=True, text=True, cwd=REPO)
    assert r.returncode == 0, r.stderr[-2000:]
    print(r.stdout.strip().splitlines()[-1])
    review = (R1 / 'REVIEW.md').read_text(encoding='utf-8')
    prompt = (B / 'REVIEW-PROMPT.txt').read_text(encoding='utf-8')
    items = {}
    for m in re.finditer(r'(?ms)^## Item (\d+) \(([^,)]+)[^)]*\)\n(.*?)(?=^## Item |\Z)', prompt):
        items[m.group(2)] = m.group(3).strip()
    R2.mkdir(exist_ok=True)
    out = []
    for n, (key, old_n) in enumerate(CHANGED.items(), 1):
        body = items[key]
        prior = finding(review, old_n)
        if key in COLD:
            prior += '\n\nA cold reader of the whole section asked the same: ' + COLD[key]
        out.append('## Item %d (%s)\n\nROUND 1 FOUND:\n%s\n\nTHE PARAGRAPH NOW, IN ITS PLACE:\n%s\n' % (n, key, prior, body))
    head = (
        "You check %d fixed paragraphs of a long self-hypnosis guide by Joel. In round 1 a reader checked each change Joel's "
        "answers asked for (how the guide names the inner child, the guards he now calls childhood protector parts, the "
        "inner adult's three jobs, Nurturer, Protector and Guide, and the inherited parent script) and found a problem in "
        "each of these. For each item you get ROUND 1 FOUND (the reader's report, with the answer the change carries out), "
        "and THE PARAGRAPH NOW: the answer again, BEFORE and AFTER (what comes just before and after it in the guide), WAS "
        "(the paragraph as installed before any change) and NOW (with the round 2 fix).\n\nFor each item, say in a few "
        "words each:\n1. FIXED: is round 1's problem gone in NOW? YES, or what is left.\n2. ANSWER: does NOW still do what "
        "the answer asks, no more and no less?\n3. MEANING: apart from that, does NOW keep every point of WAS? KEPT, or "
        "what changed, was lost or was added.\n4. NAMES: are the figures kept apart (a protective reaction is not the "
        "Protector, the adult's jobs are not guards or parts, the inherited parent script is not the inner adult)?\n5. "
        "SENSE: would a reader who has read the guide up to here understand every sentence of NOW in its place?\nEnd each "
        "item with one line, `VERDICT: OK` or `VERDICT: CHANGED`. Judge meaning, names and sense only, not style, and suggest "
        "a rewrite only for a problem you report.\n\nWrite your report with a single Write call to `%s`, one \"## Item N\" "
        "part per item, then reply with only the verdicts, one line per item. Don't read any other file, don't run commands, "
        "and don't use the web.\n\n" % (len(out), R2 / 'VERIFY-r2.md'))
    (R2 / 'VERIFY-r2-PROMPT.txt').write_text(head + '\n'.join(out), encoding='utf-8')

    meta = json.loads((B / 'meta.json').read_text(encoding='utf-8'))
    hsf = (B.parents[1] / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8').split('\n\n')
    cand = (B / 'CANDIDATE.md').read_text(encoding='utf-8').split('\n\n')
    paras, mp = [], []
    for key in CHANGED:
        t = meta['texts']['b470-' + key]
        for ver, p in (('was', hsf[t['block']]), ('new', cand[t['block']])):
            q = S.plain(p)
            k = len(R.march_paragraphs(q))
            if k:
                paras.append(q)
                mp.append({'key': 'b470-' + key, 'ver': ver, 'n': k, 'start': sum(m['n'] for m in mp)})
    M = R2 / 'march'
    M.mkdir(exist_ok=True)
    draft = '\n\n'.join(paras)
    (M / 'march-draft.txt').write_text(draft + '\n', encoding='utf-8')
    (M / 'march-map.json').write_text(json.dumps(mp, indent=1) + '\n', encoding='utf-8')
    about = ('a long self-help guide to self-hypnosis ("the inner child", "little parts", "guards" or "childhood protector '
             'parts", and the inner adult\'s three jobs, "the Nurturer", "the Protector" and "the Guide", are the guide\'s terms)')
    mprompt = R.build_march(draft, about)
    mprompt += ('\n\nWrite exactly those lines, one per paragraph from T1 to T%d, with a single Write call to `%s`, then reply '
                'with only "done". Don\'t read any other file, don\'t run commands, and don\'t use the web.\n'
                % (len(paras), M / 'march-labels.txt'))
    (M / 'march-prompt.txt').write_text(mprompt, encoding='utf-8')
    print('r2: %d items to verify; %d march paragraphs' % (len(out), len(paras)))


if __name__ == '__main__':
    main()
