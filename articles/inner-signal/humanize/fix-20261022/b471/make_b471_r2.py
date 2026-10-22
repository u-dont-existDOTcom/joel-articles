"""Batch 471g, round 2 (2026-10-22): the stance check's findings, and their re-reads.

Round 1 (now in r1/): the item review (REVIEW.md) passed both items; the march (march/march-labels.txt) has no new break
in either; the stance check (STANCE.md) found four things in the changed paragraphs:
  1  the installed "like telling them to just be able to fly" (HG14) makes the adult out of reach for good, where the
     published line says the capacity is being built: fixed in make_b471.py's list ("like telling a baby bird to just
     fly");
  2  "what I call forced adulthood" has no source in the published guide: it is Joel's answer 12 a, his term from the
     Inner Child article (his words of 15:33 UTC), so it stays;
  3  the installed step lost each adult's job ("Nurturer warms, Protector makes it safe, Leader points a direction"):
     fixed, the jobs in the step's own parentheses;
  4  "an inherited inner critic" is another name for the inherited parent: batch 470g kept it on purpose and said so on the
     questions page (answer 10, point 4: "that's the script acting as a critic"), so it stays.

Writes r2/VERIFY-r2-PROMPT.txt (Opus: each fixed finding against the paragraph in its place, -> r2/VERIFY-r2.md) and
r2/march/ (Sonnet: the installed paragraph and the round 2 one, -> r2/march/march-labels.txt), after rebuilding the batch
with make_b471.py --edits-only.

  python3 articles/inner-signal/humanize/fix-20261022/b471/make_b471_r2.py   (from the repo root)
"""
import json, pathlib, re, shutil, subprocess, sys

B = pathlib.Path(__file__).resolve().parent
REPO = B.parents[4]
sys.path.insert(0, str(REPO / 'tools' / 'humanization' / 'reviewer'))
sys.path.insert(0, str(B.parents[1] / 'tools'))
import reviewer as R   # noqa: E402
import sections as S   # noqa: E402

R1, R2 = B / 'r1', B / 'r2'
FOUND = {'forced-adulthood': 1, 'three-roles': 3}


def finding(stance, n):
    m = re.search(r'(?ms)^\*\*%d\. (.*?)(?=^\*\*\d+\. |^## |\Z)' % n, stance)
    return '**%d. %s' % (n, m.group(1).strip())


def main():
    R1.mkdir(exist_ok=True)
    for f in ('REVIEW-PROMPT.txt', 'REVIEW.md', 'march', 'STANCE.md', 'stance'):
        if (B / f).exists() and not (R1 / f).exists():
            shutil.move(str(B / f), str(R1 / f))
    r = subprocess.run([sys.executable, str(B / 'make_b471.py'), '--edits-only'], capture_output=True, text=True, cwd=REPO)
    assert r.returncode == 0, r.stderr[-2000:]
    stance = (R1 / 'STANCE.md').read_text(encoding='utf-8').split('## Contradictions in the published text')[0]
    prompt = (B / 'REVIEW-PROMPT.txt').read_text(encoding='utf-8')
    items = {m.group(2): m.group(3).strip()
             for m in re.finditer(r'(?ms)^## Item (\d+) \(([^,)]+)[^)]*\)\n(.*?)(?=^## Item |\Z)', prompt)}
    R2.mkdir(exist_ok=True)
    out = []
    for n, (key, k) in enumerate(FOUND.items(), 1):
        out.append('## Item %d (%s)\n\nTHE STANCE CHECK FOUND:\n%s\n\nTHE PARAGRAPH NOW, IN ITS PLACE:\n%s\n'
                   % (n, key, finding(stance, k), items[key]))
    head = (
        "You check %d fixed paragraphs of a long self-hypnosis guide by Joel. Each carries out an answer Joel gave (shown "
        "below as THE ANSWER IT CARRIES OUT). A stance check then read the changed paragraphs against his whole published "
        "guide and found that each had drifted from it in words an earlier rewrite had put there; round 2 puts the published "
        "meaning back. For each item you get THE STANCE CHECK FOUND, and THE PARAGRAPH NOW: the answer, BEFORE and AFTER "
        "(what comes just before and after it in the guide), WAS (the paragraph as installed) and NOW (with the answer and "
        "the round 2 fix).\n\nFor each item, say in a few words each:\n1. FIXED: is the drift the stance check found gone in "
        "NOW? YES, or what is left.\n2. ANSWER: does NOW still do what the answer asks, no more and no less?\n3. MEANING: "
        "apart from those two, does NOW keep every point of WAS? KEPT, or what changed, was lost or was added.\n4. NAMES: "
        "are the figures kept apart (a protective reaction is not the Protector, the adult's jobs are not guards or parts, "
        "the inherited parent script is not the inner adult)?\n5. SENSE: would a reader who has read the guide up to here "
        "understand every sentence of NOW in its place?\nEnd each item with one line, `VERDICT: OK` or `VERDICT: CHANGED`. "
        "Judge meaning, names and sense only, not style, and suggest a rewrite only for a problem you report.\n\nWrite your "
        "report with a single Write call to `%s`, one \"## Item N\" part per item, then reply with only the verdicts, one "
        "line per item. Don't read any other file, don't run commands, and don't use the web.\n\n" % (len(out), R2 / 'VERIFY-r2.md'))
    (R2 / 'VERIFY-r2-PROMPT.txt').write_text(head + '\n'.join(out), encoding='utf-8')

    meta = json.loads((B / 'meta.json').read_text(encoding='utf-8'))
    hsf = (B.parents[1] / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8').split('\n\n')
    cand = (B / 'CANDIDATE.md').read_text(encoding='utf-8').split('\n\n')
    paras, mp = [], []
    for key in FOUND:
        t = meta['texts']['b471-' + key]
        for ver, p in (('was', hsf[t['block']]), ('new', cand[t['block']])):
            q = S.plain(p)
            k = len(R.march_paragraphs(q))
            if k:
                paras.append(q)
                mp.append({'key': 'b471-' + key, 'ver': ver, 'n': k, 'start': sum(m['n'] for m in mp)})
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
