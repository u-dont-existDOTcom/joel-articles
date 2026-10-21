"""The gate's reviews of the fixed induction section (HG17: Emulate sample ba with every lost point put back,
make_hg17_fixed.py), 2026-10-21.

Writes, in this folder:
  HG17-section.md                the section as it will be installed (tools/install_fixed.py section_md: the published
                                 headings, the fixed paragraphs, the three links on their words)
  CANDIDATE.md                   the working copy with HG17.fixed.json installed, for the readers that need the article
                                 around the section; the 4.1 edits (fix-20261020/EDITS41.json) are checked against it
  HG17.fixed.verify.prompt.txt   the meaning check: every point of the published section against the fixed one (the
                                 prompt of HG17.ba.verify.prompt.txt with the fixed section as the rewrite), for Sonnet
  march/march-prompt.txt         the march read of every paragraph the fixes changed, ba's version ("was") and the fixed
                                 one ("new"), with march-draft.txt and march-map.json to decode the labels, for Sonnet
  sense/prompt.txt               the cold read of the whole section in the article (reviewer.py sense-section), for Opus
  stance/prompt.txt              the whole-guide stance check (stance_check_prompt.py, with Joel's positions since
                                 publication from fix-20261021/b469/POSITIONS.txt), for Opus
Each prompt names the file its reader writes: HG17.fixed.verify.out.md, march/march-labels.txt, SENSE-HG17.md,
STANCE-HG17.md.

  python3 articles/inner-signal/humanize/fix-20261018/rf-zg/make_hg17_reviews.py   (from the repo root)
"""
import json, pathlib, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parents[1]
REPO = H.parents[2]
sys.path.insert(0, str(H / 'tools'))
sys.path.insert(0, str(H / 'fix-20261020'))
sys.path.insert(0, str(REPO / 'tools' / 'humanization'))
sys.path.insert(0, str(REPO / 'tools' / 'humanization' / 'reviewer'))
import install_fixed as I     # noqa: E402
import apply_edits41 as E41   # noqa: E402
import reviewer as R          # noqa: E402

FIXED = HERE / 'HG17.fixed.json'
TITLE = 'Induction: gathering attention without disappearing'
ABOUT = ('a long self-help guide to self-hypnosis ("the inner child", "the Nurturer", "the Adult" and "protectors" are '
         'the guide\'s terms; much of this part is a script the reader records or says to themselves)')


def rel(p):
    return str(pathlib.Path(p).resolve().relative_to(REPO))


def main():
    md = I.section_md(FIXED)
    (HERE / 'HG17-section.md').write_text(md + '\n', encoding='utf-8')
    art = (H / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
    cand, notes = I.install(art, [FIXED])
    (HERE / 'CANDIDATE.md').write_text(cand, encoding='utf-8')
    edits = E41.load()
    broken = [e['key'] for i, e in enumerate(edits) if not (E41.is_in(cand, e) or E41.superseded(e, edits[i + 1:], cand))]
    print('install notes:', notes or 'none', '| 4.1 edits not in the candidate:', broken or 'none')

    # the meaning check: the same prompt as sample ba's, with the fixed section as the rewrite
    ba = (HERE / 'HG17.ba.verify.prompt.txt').read_text(encoding='utf-8')
    head = ba.split('THE REWRITE:')[0]
    head = head.replace(str(HERE / 'HG17.ba.verify.out.md'), str(HERE / 'HG17.fixed.verify.out.md'))
    head = head.replace('The rewrite was made by a paraphrasing tool that writes in a plainer, more personal voice; its '
                        'looser wording is fine.',
                        'The rewrite was made by a paraphrasing tool that writes in a plainer, more personal voice, and '
                        'then edited; its looser wording is fine.')
    assert 'HG17.fixed.verify.out.md' in head and 'then edited' in head
    (HERE / 'HG17.fixed.verify.prompt.txt').write_text(head + 'THE REWRITE:\n\n' + md + '\n', encoding='utf-8')

    # the march: ba's paragraph and the fixed one, for every paragraph a fix changed
    fixes = json.loads((HERE / 'FIXES.json').read_text(encoding='utf-8'))
    paras, mp = [], []
    for n, x in enumerate(fixes):
        for ver in ('was', 'new'):
            q = x.get(ver)
            if not q:
                continue
            k = len(R.march_paragraphs(q))
            if k:
                paras.append(q)
                mp.append({'fix': n, 'unit': x['unit'], 'para': x['para'], 'ver': ver, 'n': k,
                           'start': sum(m['n'] for m in mp)})
    M = HERE / 'march'
    M.mkdir(exist_ok=True)
    draft = '\n\n'.join(paras)
    (M / 'march-draft.txt').write_text(draft + '\n', encoding='utf-8')
    (M / 'march-map.json').write_text(json.dumps(mp, indent=1) + '\n', encoding='utf-8')
    prompt = R.build_march(draft, ABOUT)
    prompt += ('\n\nWrite exactly those lines, one per paragraph from T1 to T%d, with a single Write call to `%s`, then reply '
               'with only "done". Don\'t read any other file, don\'t run commands, and don\'t use the web.\n'
               % (sum(m['n'] for m in mp), M / 'march-labels.txt'))
    (M / 'march-prompt.txt').write_text(prompt, encoding='utf-8')

    # the cold read of the section in the article
    (HERE / 'sense').mkdir(exist_ok=True)
    r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'reviewer' / 'reviewer.py'), '--article',
                        rel(HERE / 'CANDIDATE.md'), 'sense-section', rel(HERE / 'sense' / 'prompt.txt'), '--section', TITLE,
                        '--report', str(HERE / 'SENSE-HG17.md')], capture_output=True, text=True, cwd=REPO)
    assert r.returncode == 0, r.stderr[-2000:]

    # the stance check against the whole published guide and Joel's positions since
    (HERE / 'stance').mkdir(exist_ok=True)
    r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'stance_check_prompt.py'),
                        '--essay', rel(H / 'source' / 'published-20260928.md'), '--rewrite', rel(HERE / 'HG17-section.md'),
                        '--out', rel(HERE / 'stance' / 'prompt.txt'),
                        '--scope', 'the induction section (its preparation, a spoken listening script, the already-open and '
                                   'stay-awake practices, the two-hand and sleep inductions, fractionation, deepening, a '
                                   'trance depth check and a shortcut back into hypnosis)',
                        '--topic', 'self-hypnosis and listening to the subconscious',
                        '--positions', rel(H / 'fix-20261021' / 'b469' / 'POSITIONS.txt'),
                        '--report', str(HERE / 'STANCE-HG17.md')], capture_output=True, text=True, cwd=REPO)
    assert r.returncode == 0, r.stderr[-2000:]
    for f in ('HG17-section.md', 'HG17.fixed.verify.prompt.txt', 'march/march-prompt.txt', 'sense/prompt.txt',
              'stance/prompt.txt'):
        print(f, len((HERE / f).read_text(encoding='utf-8').split()), 'words')
    print(len(mp), 'march paragraphs from', len(fixes), 'fixes;', sum(m['n'] for m in mp), 'march lines')


if __name__ == '__main__':
    main()
