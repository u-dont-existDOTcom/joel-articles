"""Round z (turn 65): fresh writers' outputs -> paragraph files, lint, then one screen batch.

  python3 rz.py split            # writers/{job}-w{n}.txt -> writers/{job}-w{n}-p{i}.txt, lint each (parallel)
  python3 rz.py build MARCH.json ROUND OUTPREFIX   # MARCH.json: {"job-wn-pi": "S B S", ...}; only those go in
Each paragraph is checked alone; each writer's set is also checked in its section (SECTIONS), with the settled
paragraphs around it, when every paragraph of the set is in MARCH.json.
"""
import concurrent.futures as cf
import json
import pathlib
import re
import subprocess
import sys

REPO = pathlib.Path('/home/claude/joel-articles')
A = REPO / 'articles/inner-child-therapy'
G = A / 'experiments/t65-guide'
W = G / 'writers'
ART = A / 'HUMANIZED-ARTICLE-SO-FAR.md'
txt = lambda n: (G / (n + '.txt')).read_text(encoding='utf-8').strip()

SECTIONS = {  # NEW = the writer's paragraphs, in order; None = alone checks only
    'sp4': ['## Journal With Each Hand', 'NEW'],
    'sp5': ['## “And So That’s the Way It Happened!”', 'sp5-p1-e2', 'NEW'],
    'sp6': ['## One Intention in the Morning, One Review at Night', 'NEW'],
    'sp7': ['## Just Like Me', 'sp7-p1-c', 'NEW'],
    'sp8p1': None, 'sp8p4b': None,
    'sp9': ['## Close the Session and Return to Life', 'NEW'],
    'lm1': ['# When Love Still Feels Missing', 'NEW'],
    'lm2': ['## Notice the Part That Came Here', 'NEW'],
    'lm3': ['## Somatic Heart Opening', 'NEW'],
    'lm4': ['## How Much Happiness Do You Know Is Possible?', 'lm4-p1-a', 'lm4-p2-a2', 'NEW', 'lm4-p5-c'],
    'ks12': None, 'ks4b': None,
    'sh1': ['# When the Practice Feels Real but Stays Shallow', 'NEW'],
    'fg1': ['# How to Forgive Without Forgetting', 'NEW'],
    'le1': ['# When One Life Has Ended and the Next Hasn’t Begun', 'le1-p1-c', 'NEW'],
    'ba1': ['# Borrowed Adulthood in Relationship', 'NEW'],
}


def paras(p):
    return [b.strip() for b in re.split(r'\n\s*\n', p.read_text(encoding='utf-8').strip()) if b.strip()]


def lint(f):
    r = subprocess.run([sys.executable, str(REPO / 'tools/humanization/tells_lint.py'), '--installed', str(ART), str(f)],
                       capture_output=True, text=True, cwd=REPO)
    out = r.stdout + r.stderr
    v = re.search(r'verdict: (\w+)', out)
    return f.stem, (v.group(1) if v else '?'), out


def split():
    files = []
    for f in sorted(W.glob('*-w[0-9].txt')):
        ps = paras(f)
        for i, p in enumerate(ps, 1):
            q = W / ('%s-p%d.txt' % (f.stem, i))
            q.write_text(p + '\n', encoding='utf-8')
            files.append(q)
    with cf.ThreadPoolExecutor(12) as ex:
        res = list(ex.map(lint, files))
    for stem, v, out in res:
        n = len((W / (stem + '.txt')).read_text().split())
        print('%-16s %3dw %s' % (stem, n, v))
        if v == 'FAIL':
            for ln in out.splitlines():
                if 'FAIL' in ln and 'verdict' not in ln:
                    print('      ' + ln.strip()[:200])


def build(march_file, rnd, out_prefix):
    m = json.loads(pathlib.Path(march_file).read_text())
    drafts, gate, rows = {}, {}, []
    date = '2026-10-17 (turn 65)'
    sets = {}
    for stem, march in m.items():  # stem: job-wN-pI
        job, w, p = stem.rsplit('-', 2)
        text = (W / (stem + '.txt')).read_text(encoding='utf-8').strip()
        k = '%s_%s%s%s' % (rnd, job, w, p)
        drafts[k] = text
        gate[k] = {'kind': 'screen', 'march': [march], 'lint': 'REVIEW', 'lint_article': str(ART),
                   'note': '%s: %s of %s, paragraph %s. March: my own reading.' % (rnd, 'my own draft (w9)' if w == 'w9' else 'fresh writer %s (E177)' % w, job, p[1:])}
        rows.append('| %s | %s %s %s alone, %s (%d words) [%s], a screen | Human, low (my call) | (pending) | |'
                    % (date, job, w, p, 'my own draft' if w == 'w9' else 'a fresh writer', len(text.split()), k))
        sets.setdefault((job, w), []).append((int(p[1:]), stem, march))
    for (job, w), items in sorted(sets.items()):
        sec = SECTIONS.get(job)
        n = len(paras(W / ('%s-%s.txt' % (job, w))))
        if not sec or len(items) != n:
            continue
        items.sort()
        new = [(W / (s + '.txt')).read_text(encoding='utf-8').strip() for _, s, _ in items]
        blocks, marches = [], []
        for b in sec:
            if b == 'NEW':
                blocks += new; marches += ['%s %s' % (w, mm) for _, _, mm in items]
            elif b.startswith('#'):
                blocks.append(b)
            else:
                blocks.append(txt(b)); marches.append(b + ' (read Human alone)')
        k = '%s_sec%s%s' % (rnd, job, w)
        drafts[k] = '\n\n'.join(blocks)
        gate[k] = {'kind': 'screen', 'march': [' | '.join(marches)], 'lint': 'REVIEW', 'lint_article': str(ART),
                   'note': '%s: %s with fresh writer %s\'s paragraphs.' % (rnd, sec[0], w)}
        rows.append('| %s | %s with %s\'s paragraphs (%d words) [%s], a screen | Human, low (my call) | (pending) | |'
                    % (date, sec[0].lstrip('# '), w, len(drafts[k].split()), k))
    order = [k for k in drafts if '_sec' not in k] + [k for k in drafts if '_sec' in k]
    drafts = {k: drafts[k] for k in order}
    gate = {k: gate[k] for k in order}
    out = pathlib.Path(out_prefix)
    (out.parent / (out.name + '-drafts.json')).write_text(json.dumps(drafts, indent=1, ensure_ascii=False), encoding='utf-8')
    (out.parent / (out.name + '-gate.json')).write_text(json.dumps(gate, indent=1, ensure_ascii=False), encoding='utf-8')
    cmd = [sys.executable, str(REPO / 'tools/humanization/pangram_gate.py'), str(out.parent / (out.name + '-drafts.json')),
           str(out.parent / (out.name + '-gate.json')), str(out.parent / (out.name + '.js')), '--name', rnd,
           '--lint-article', str(ART)] + order
    rc = subprocess.run(cmd, cwd=REPO).returncode
    if rc == 0:
        p = A / 'tools/PREDICTIONS.md'
        p.write_text(p.read_text(encoding='utf-8').rstrip('\n') + '\n' + '\n'.join(rows) + '\n', encoding='utf-8')
        print('%d checks, %d words' % (len(drafts), sum(len(t.split()) for t in drafts.values())))
    return rc


if __name__ == '__main__':
    if sys.argv[1] == 'split':
        split()
    else:
        sys.exit(build(*sys.argv[2:5]))
