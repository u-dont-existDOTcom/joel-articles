"""Batch 470g, round 4 (2026-10-22): three rewordings for linter rules the batch's own words brought in.

The gate compares the linter's rules on each installed paragraph and on its edit (lint-compare.json, from
make_gate_b470.py's run). Every paragraph the batch changes was installed from Emulate's text, whose paragraphs FAIL the
linter more often than not, so a FAIL holds an edit only when the installed paragraph wasn't FAIL; but a rule the
installed paragraph didn't trip is one my words brought, and it gets reworded before any reader sees it (the gate doc,
"A lost point goes back in the sample's words"). Round 3's text had four such rules:
  guard-first-read  E36 heavy second person, from the gloss's "your" and "you": now "guard mind (childhood protector parts,
                    the protective reactions learned as a child)"
  synchronicity     E125 list of three (and the packed-sentence rule B4 on that sentence), from round 2's "from ..., from
                    ..., or if": now "a message from my Inner Child or from a childhood protector part, or if I just need
                    to grieve" (one "or from" keeps the two sources apart, as round 2 wanted, without a list of three)
  anxiety-part      E36 heavy second person, from Joel's reason in my words: now "the same as in childhood. It's trying to
                    help, but it believes you are in danger"
  script-fake       E36 heavy second person: an artifact of a two-word change in a sentence addressed to the reader
                    ("It could also be your inherited parent script that you are picking up"); its "your" and "you" are the
                    installed sentence's, so it stays, answered in gate-answers.json
Writes r4/VERIFY-r4-PROMPT.txt (Opus, -> r4/VERIFY-r4.md) and r4/march/ (Sonnet), after rebuilding the batch with
make_b470.py --edits-only.

  python3 articles/inner-signal/humanize/fix-20261022/b470/make_b470_r4.py   (from the repo root)
"""
import json, pathlib, re, subprocess, sys

B = pathlib.Path(__file__).resolve().parent
REPO = B.parents[4]
sys.path.insert(0, str(REPO / 'tools' / 'humanization' / 'reviewer'))
sys.path.insert(0, str(B.parents[1] / 'tools'))
import reviewer as R   # noqa: E402
import sections as S   # noqa: E402

R4 = B / 'r4'
WHY = {
    'guard-first-read': ('round 2 put in the gloss "(your childhood protector parts, the protective reactions you learned as a '
                         'child)", and round 2\'s reader passed it; the linter then found the gloss made the paragraph\'s '
                         'second person heavier, so it is now said without "your" and "you"'),
    'synchronicity': ('round 2 made it "a message from my Inner Child, from a childhood protector part, or if I just need to '
                      'grieve", so the protector part could not be read as describing the Inner Child, and round 2\'s reader '
                      'passed it; the linter then found a list of three in that shape, so it is now "from my Inner Child or '
                      'from a childhood protector part, or if I just need to grieve"'),
    'anxiety-part': ('round 1 added Joel\'s reason ("It\'s what protects you when your consciously installed parental Protector '
                     'isn\'t functioning, the same as when you were a child. It\'s trying to help you, but it believes ..."), '
                     'and round 1\'s reader passed it; the linter then found the added words too heavy in "you", so it is now '
                     '"the same as in childhood. It\'s trying to help, but it believes you are in danger"'),
}


def main():
    r = subprocess.run([sys.executable, str(B / 'make_b470.py'), '--edits-only'], capture_output=True, text=True, cwd=REPO)
    assert r.returncode == 0, r.stderr[-2000:]
    print(r.stdout.strip().splitlines()[-1])
    prompt = (B / 'REVIEW-PROMPT.txt').read_text(encoding='utf-8')
    items = {}
    for m in re.finditer(r'(?ms)^## Item (\d+) \(([^,)]+)[^)]*\)\n(.*?)(?=^## Item |\Z)', prompt):
        items[m.group(2)] = m.group(3).strip()
    R4.mkdir(exist_ok=True)
    out = ['## Item %d (%s)\n\nWHAT CHANGED SINCE THE LAST READ:\n%s\n\nTHE PARAGRAPH NOW, IN ITS PLACE:\n%s\n'
           % (n, key, why, items[key]) for n, (key, why) in enumerate(WHY.items(), 1)]
    head = (
        "You check %d paragraphs of a long self-hypnosis guide by Joel, each reworded slightly after an earlier reader passed "
        "it. They carry renames Joel asked for (the guards as childhood protector parts, with his reason: \"that's what we "
        "have to protect us when the consciously installed parental Protector is not functioning, same as when we were "
        "children\"; the inner adult's three jobs, Nurturer, Protector and Guide; the inherited parent script). For each "
        "item you get WHAT CHANGED SINCE THE LAST READ, and THE PARAGRAPH NOW: Joel's answers, BEFORE and AFTER (what comes "
        "just before and after it in the guide), WAS (the paragraph as installed before any change) and NOW (with every "
        "change).\n\nFor each item, say in a few words each:\n1. ANSWER: does NOW still do what Joel's answer asks?\n2. "
        "MEANING: apart from the renames, does NOW keep every point of WAS? KEPT, or what changed, was lost or was added.\n3. "
        "NAMES: are the figures kept apart (a protective reaction is not the Protector; the Inner Child is not a protector "
        "part)?\n4. SENSE: would a reader who has read the guide up to here understand every sentence of NOW in its place?\n"
        "End each item with one line, `VERDICT: OK` or `VERDICT: CHANGED`. Judge meaning, names and sense only, not style, "
        "and suggest a rewrite only for a problem you report.\n\nWrite your report with a single Write call to `%s`, one "
        "\"## Item N\" part per item, then reply with only the verdicts, one line per item. Don't read any other file, don't "
        "run commands, and don't use the web.\n\n" % (len(out), R4 / 'VERIFY-r4.md'))
    (R4 / 'VERIFY-r4-PROMPT.txt').write_text(head + '\n'.join(out), encoding='utf-8')

    meta = json.loads((B / 'meta.json').read_text(encoding='utf-8'))
    hsf = (B.parents[1] / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8').split('\n\n')
    cand = (B / 'CANDIDATE.md').read_text(encoding='utf-8').split('\n\n')
    paras, mp = [], []
    for key in WHY:
        t = meta['texts']['b470-' + key]
        for ver, p in (('was', hsf[t['block']]), ('new', cand[t['block']])):
            q = S.plain(p)
            k = len(R.march_paragraphs(q))
            if k:
                paras.append(q)
                mp.append({'key': 'b470-' + key, 'ver': ver, 'n': k, 'start': sum(m['n'] for m in mp)})
    M = R4 / 'march'
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
    if (B / 'march').exists():
        for f in (B / 'march').iterdir():
            f.unlink()
        (B / 'march').rmdir()
    print('r4: %d items to verify; %d march paragraphs' % (len(out), len(paras)))


if __name__ == '__main__':
    main()
