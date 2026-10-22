"""Batch 470g, round 3 (2026-10-22): the stance check's conflicts, fixed in the paragraphs the batch changes.

Round 1's stance check (r1/STANCE.md) read the changed paragraphs whole against the published guide and Joel's positions
since, and found six conflicts, all in words the batch didn't change (the installed Human versions'), and fifteen places
where the published text itself pulls against his positions, most of which the batch fixes. Five of the six are in
paragraphs the batch changes, so they're fixed there in as few words as possible, as batch 469g fixed its stance
conflicts (make_b470.py's list, round 3):
  1  three-jobs-named, parent-script  "what you need to develop in yourself in order to be able to reparent" and "that you
                       will eventually build up" made reparenting wait; the published: "They’re three ways the present-day
                       person reparents the inner child", "the Nurturer, Protector, and Leader/Guru you deliberately build"
  2  script-humiliating  "something that has no value on its own" made the activity worthless; the published: "a small
                       experiment with no résumé value"
  4  guide-proportion  "preclude all loving relationships" and "consequences to others" narrowed the limits; the
                       published: "the Protector cannot exclude all love; the Nurturer cannot erase consequences"
  5  synchronicity     "where I can objectively and clearly see" claimed a peak state; the published: "I return to the
                       highest perspective I can access", "I make room for whatever is genuinely available"
Conflict 3 (Appendix B's "Put 3 good adults in") is Joel's question 12 c, with the published text's other three adults
(the invocation's "inner adult(s)", Appendix K's "three-adult arrangement"). Conflict 6 (Appendix G's one sentence for the
published three claims) is answered in gate-answers.json: the sentence names the scary image, the lighting and the bad
feeling, and says none of them necessarily means what you think, the same claims said once.

Writes r3/VERIFY-r3-PROMPT.txt (Opus: each conflict against the fixed paragraph in its place, -> r3/VERIFY-r3.md) and
r3/march/ (Sonnet, -> r3/march/march-labels.txt), after rebuilding the batch with make_b470.py --edits-only.

  python3 articles/inner-signal/humanize/fix-20261022/b470/make_b470_r3.py   (from the repo root)
"""
import json, pathlib, re, subprocess, sys

B = pathlib.Path(__file__).resolve().parent
REPO = B.parents[4]
sys.path.insert(0, str(REPO / 'tools' / 'humanization' / 'reviewer'))
sys.path.insert(0, str(B.parents[1] / 'tools'))
import reviewer as R   # noqa: E402
import sections as S   # noqa: E402

R1 = B / 'r1'
R3 = B / 'r3'
CHANGED = {'three-jobs-named': 1, 'parent-script': 1, 'script-humiliating': 2, 'guide-proportion': 4, 'synchronicity': 5}


def conflict(stance, n):
    m = re.search(r'(?ms)^\*\*%d\.\*\*(.*?)(?=^\*\*\d+\.\*\*|^## )' % n, stance)
    return m.group(1).strip()


def main():
    r = subprocess.run([sys.executable, str(B / 'make_b470.py'), '--edits-only'], capture_output=True, text=True, cwd=REPO)
    assert r.returncode == 0, r.stderr[-2000:]
    print(r.stdout.strip().splitlines()[-1])
    stance = (R1 / 'STANCE.md').read_text(encoding='utf-8')
    prompt = (B / 'REVIEW-PROMPT.txt').read_text(encoding='utf-8')
    items = {}
    for m in re.finditer(r'(?ms)^## Item (\d+) \(([^,)]+)[^)]*\)\n(.*?)(?=^## Item |\Z)', prompt):
        items[m.group(2)] = m.group(3).strip()
    R3.mkdir(exist_ok=True)
    out = []
    for n, (key, c) in enumerate(CHANGED.items(), 1):
        out.append('## Item %d (%s)\n\nTHE STANCE CHECK FOUND:\n%s\n\nTHE PARAGRAPH NOW, IN ITS PLACE:\n%s\n'
                   % (n, key, conflict(stance, c), items[key]))
    head = (
        "You check %d fixed paragraphs of a long self-hypnosis guide by Joel. A stance check read each against his published "
        "guide (\"Essay\") and found that the paragraph, as it was installed, pulls away from the published position quoted. "
        "Each paragraph also carries renames that Joel asked for (the guards as childhood protector parts; the inner adult's "
        "three jobs, Nurturer, Protector and Guide; the inherited parent script); those are settled. For each item you get "
        "THE STANCE CHECK FOUND (its finding, with the published words), and THE PARAGRAPH NOW: Joel's answers, BEFORE and "
        "AFTER (what comes just before and after it in the guide), WAS (the paragraph as installed) and NOW (with every "
        "change, the fix for the finding included).\n\nFor each item, say in a few words each:\n1. FIXED: does NOW agree "
        "with the published position the finding quotes? YES, or what still pulls away.\n2. MEANING: apart from that fix and "
        "the renames, does NOW keep every point of WAS? KEPT, or what changed, was lost or was added.\n3. SENSE: would a "
        "reader who has read the guide up to here understand every sentence of NOW in its place?\nEnd each item with one "
        "line, `VERDICT: OK` or `VERDICT: CHANGED`. Judge meaning and sense only, not style, and suggest a rewrite only for "
        "a problem you report.\n\nWrite your report with a single Write call to `%s`, one \"## Item N\" part per item, then "
        "reply with only the verdicts, one line per item. Don't read any other file, don't run commands, and don't use the "
        "web.\n\n" % (len(out), R3 / 'VERIFY-r3.md'))
    (R3 / 'VERIFY-r3-PROMPT.txt').write_text(head + '\n'.join(out), encoding='utf-8')

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
    M = R3 / 'march'
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
    if (B / 'march').exists():   # make_b470.py --edits-only writes the whole batch's march draft; this round's is r3/march/
        for f in (B / 'march').iterdir():
            f.unlink()
        (B / 'march').rmdir()
    print('r3: %d items to verify; %d march paragraphs' % (len(out), len(paras)))


if __name__ == '__main__':
    main()
