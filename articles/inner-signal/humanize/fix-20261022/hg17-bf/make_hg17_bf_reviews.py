"""The gate's reviews of the induction section from sample bf (make_hg17_bf_fixed.py), 2026-10-22.

Writes, in this folder:
  check/prompt.txt     the fix check, for Opus: every paragraph the fixes or the headings changed (bf's version and now,
                       in its place, with the items of the meaning check it answers), and an audit of the items let stand:
                       the published section and the fixed one are both in the prompt, so the reader can say where a let
                       stand would leave a reader doing or believing something Joel didn't publish (-> FIX-CHECK.md)
  march/march-prompt.txt  the march read of every changed paragraph, bf's and now, for Sonnet (-> march/march-labels.txt)
  sense/prompt.txt     the cold read of the whole section in the article (reviewer.py sense-section), for Opus
                       (-> SENSE-HG17.md)
  stance/prompt.txt    the whole-guide stance check (stance_check_prompt.py, with Joel's positions since publication,
                       question 12 included: b471/POSITIONS.txt), for Opus (-> STANCE-HG17.md)

  python3 articles/inner-signal/humanize/fix-20261022/hg17-bf/make_hg17_bf_reviews.py   (from the repo root)
"""
import json, pathlib, re, subprocess, sys

V = pathlib.Path(__file__).resolve().parent
H = V.parents[1]
REPO = H.parents[2]
sys.path.insert(0, str(REPO / 'tools' / 'humanization' / 'reviewer'))
import reviewer as R  # noqa: E402

TITLE = 'Induction: gathering attention without disappearing'
ABOUT = ('a long self-help guide to self-hypnosis ("the inner child", "the Nurturer", "the Protector", "the Guide" and '
         '"childhood protector parts" are the guide\'s terms; much of this part is a script the reader records or says to '
         'themselves)')


def rel(p):
    return str(pathlib.Path(p).resolve().relative_to(REPO))


def published():
    parts = []
    for n in (1, 2, 3):
        t = (V / ('VERIFY-part%d-PROMPT.txt' % n)).read_text(encoding='utf-8')
        parts.append(t.split('THE PUBLISHED SECTION:\n\n', 1)[1].split('\n\nTHE REWRITE:', 1)[0])
    return '\n\n'.join(parts)


def main():
    changed = json.loads((V / 'CHANGED-PARAS.json').read_text(encoding='utf-8'))
    fixes = json.loads((V / 'FIXES.json').read_text(encoding='utf-8'))
    section = (V / 'SECTION.md').read_text(encoding='utf-8')
    blocks = [b for b in section.split('\n\n') if b.strip()]
    plain = [re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', re.sub(r'^#+\s*', '', b)) for b in blocks]

    def place(new):
        k = next((i for i, b in enumerate(plain) if new and new.strip() == b.strip()), None)
        if k is None:
            return '(the paragraph is gone: its words were a run-in heading, and the published heading above carries them)', ''
        return plain[k - 1] if k else '', plain[k + 1] if k + 1 < len(plain) else ''

    items = []
    for n, c in enumerate(changed, 1):
        before, after = place(c['new'])
        answers = [f for f in fixes if f['applied'] and ((f['new'] and c['new'] and f['new'] in c['new'])
                                                          or (f['old'] in c['was'] and (c['new'] is None or f['old'] not in c['new'])))]
        why = '\n'.join('- the meaning check found: %s\n  fix: "%s" -> "%s"' % (f['answers'], f['old'], f['new']) for f in answers)
        if c.get('also'):
            why += ('\n' if why else '') + '- also: %s' % c['also']
        items.append('## Item %d (bf paragraph %d)\n\nWHY IT CHANGED:\n%s\n\nBEFORE:\n%s\n\nWAS (bf):\n%s\n\nNOW:\n%s\n\nAFTER:\n%s\n'
                     % (n, c['para'], why or '- (no fix of its own: see WAS and NOW)', before, c['was'],
                        c['new'] if c['new'] is not None else '(dropped)', after))
    stand = []
    for n in (1, 2, 3):
        d = json.loads((V / ('FIXDRAFT-part%d.json' % n)).read_text(encoding='utf-8'))
        stand += ['- part %d, %s: %s (let stand because: %s)' % (n, x['p'], x['item'], x['why']) for x in d['let_stand']]
    stand += ['- part 2, P35: ADDED-CLAIM: "How does your body feel? Where are you grounded?" Two new orientation checks '
              '(let stand because: two harmless orientation questions; the drafted cut was left out)']
    head = (
        "You check the meaning fixes in one section of Joel's long self-hypnosis guide: the induction (what an induction "
        "does, how to prepare, a spoken listening script, the already-open and stay-awake practices, the two-hand and "
        "sleep inductions, fractionation, deepening, a trance depth check and a shortcut back into hypnosis). A "
        "paraphrasing tool rewrote Joel's published section in a looser, more personal voice (\"bf\"), and a detector read "
        "bf as human-written. A reader then compared bf with the published section point by point. The points that change "
        "what a reader of the guide does or believes were put back in the smallest edits inside bf's own sentences, and "
        "the rest was let stand on purpose: every edit risks making the text read as machine-written again. The guide is "
        "self-guided: the reader leads themselves, reading it or using a recording they made.\n\n"
        "PART 1, THE FIXES. For each item below you get WHY IT CHANGED (the meaning check's finding and the edit), BEFORE "
        "and AFTER (the paragraphs around it in the fixed section), WAS (bf) and NOW. For each item, say in a few words "
        "each:\n1. FIXED: does NOW say what the published section says on that point (THE PUBLISHED SECTION is below)? "
        "YES, or what is still off.\n2. MEANING: apart from that, does NOW keep everything WAS said? KEPT, or what changed.\n"
        "3. SENSE: would a reader who has read the guide up to here understand NOW in its place? OK, or the words that stop "
        "them and why.\nEnd each item with one line, `VERDICT: OK` or `VERDICT: CHANGED`.\n\n"
        "PART 2, WHAT WAS LET STAND. Below the items is the list of the meaning check's findings that were left as bf has "
        "them, each with the reason. Read THE PUBLISHED SECTION and THE FIXED SECTION, and name only the ones where you "
        "disagree: where the fixed section would still have a reader do or believe something the published section "
        "doesn't say (a step missing, a safety or exit point lost, a condition dropped, a permission made a duty or the "
        "other way round, a claim the published doesn't make). For each, quote the words and say what a reader would do or "
        "believe, and suggest the smallest edit inside the fixed section's own sentence. Agree silently with the rest.\n\n"
        "Judge meaning and sense only, not style. Write your report with a single Write call to `%s`: \"## Item N\" parts "
        "for part 1, then \"## Let stand\" with your disagreements, or \"none\". Then reply with only the verdicts, one "
        "line per item, and a last line `let stand: N disagreements`. Don't read any other file, don't run commands, and "
        "don't use the web.\n\n" % (V / 'FIX-CHECK.md'))
    body = ('\n'.join(items) + '\n# WHAT WAS LET STAND\n\n' + '\n'.join(stand) + '\n\n# THE PUBLISHED SECTION\n\n'
            + published() + '\n\n# THE FIXED SECTION\n\n' + section)
    (V / 'check').mkdir(exist_ok=True)
    (V / 'check' / 'prompt.txt').write_text(head + body + '\n', encoding='utf-8')

    paras, mp = [], []
    for c in changed:
        for ver, q in (('was', c['was']), ('new', c['new'])):
            if not q:
                continue
            k = len(R.march_paragraphs(q))
            if k:
                paras.append(q)
                mp.append({'para': c['para'], 'ver': ver, 'n': k, 'start': sum(m['n'] for m in mp)})
    M = V / 'march'
    M.mkdir(exist_ok=True)
    draft = '\n\n'.join(paras)
    (M / 'march-draft.txt').write_text(draft + '\n', encoding='utf-8')
    (M / 'march-map.json').write_text(json.dumps(mp, indent=1) + '\n', encoding='utf-8')
    prompt = R.build_march(draft, ABOUT)
    prompt += ('\n\nWrite exactly those lines, one per paragraph from T1 to T%d, with a single Write call to `%s`, then reply '
               'with only "done". Don\'t read any other file, don\'t run commands, and don\'t use the web.\n'
               % (sum(m['n'] for m in mp), M / 'march-labels.txt'))
    (M / 'march-prompt.txt').write_text(prompt, encoding='utf-8')

    (V / 'sense').mkdir(exist_ok=True)
    r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'reviewer' / 'reviewer.py'), '--article',
                        rel(V / 'CANDIDATE.md'), 'sense-section', rel(V / 'sense' / 'prompt.txt'), '--section', TITLE,
                        '--report', str(V / 'SENSE-HG17.md')], capture_output=True, text=True, cwd=REPO)
    assert r.returncode == 0, r.stderr[-2000:]
    (V / 'stance').mkdir(exist_ok=True)
    r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'stance_check_prompt.py'),
                        '--essay', rel(H / 'source' / 'published-20260928.md'), '--rewrite', rel(V / 'SECTION.md'),
                        '--out', rel(V / 'stance' / 'prompt.txt'),
                        '--scope', 'the induction section (its preparation, a spoken listening script, the already-open and '
                                   'stay-awake practices, the two-hand and sleep inductions, fractionation, deepening, a '
                                   'trance depth check and a shortcut back into hypnosis)',
                        '--topic', 'self-hypnosis and listening to the subconscious',
                        '--positions', rel(H / 'fix-20261022' / 'b471' / 'POSITIONS.txt'),
                        '--report', str(V / 'STANCE-HG17.md')], capture_output=True, text=True, cwd=REPO)
    assert r.returncode == 0, r.stderr[-2000:]
    for f in ('check/prompt.txt', 'march/march-prompt.txt', 'sense/prompt.txt', 'stance/prompt.txt'):
        print(f, len((V / f).read_text(encoding='utf-8').split()), 'words')
    print(len(items), 'items;', len(stand), 'let stand;', sum(m['n'] for m in mp), 'march lines')


if __name__ == '__main__':
    main()
