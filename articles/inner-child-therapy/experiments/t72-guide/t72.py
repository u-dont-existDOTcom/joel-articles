"""Turn 72 (2026-10-18, from Joel's 19:06 UTC answers to questions 45 and 47 to 54): the batches and installs (a copy of turn 71's t71.py).

  python3 t71.py candidate               # CANDIDATE.md (scratch, not in the repo): the article with this turn's installs
  python3 t71.py batch ROUND SPEC.json   # one Pangram batch: alone screens of my drafts and section checks

SPEC.json is a list of items:
  {"key": "ks4a", "draft": "ks4-a", "label": "..."}                    a draft in drafts/, alone; its march from MARCH.json
  {"key": "secba", "section": "# Borrowed Adulthood in Relationship", "label": "...", "march": "...", "article": "candidate"}
A section is cut from CANDIDATE.md (or from the article as it stands), from its heading to the next heading of the same
or a higher level, with the comments taken out. Sections are linted with CANDIDATE.md as the installed text, since every
paragraph in them has read Human alone already (or is Joel's); drafts are linted against the article as it stands.
"""
import json
import os
import pathlib
import re
import subprocess
import sys

REPO = pathlib.Path('/home/claude/joel-articles')
A = REPO / 'articles/inner-child-therapy'
G65 = A / 'experiments/t65-guide'
T = A / 'experiments/t72-guide'
T71 = A / 'experiments/t71-guide'
ART = A / 'HUMANIZED-ARTICLE-SO-FAR.md'
CAND = pathlib.Path('/tmp/claude-0/-home-claude/d17e637c-ae79-5296-a30e-05fa0a73af9d/scratchpad/t72/CANDIDATE.md')   # not kept in the repo: `t67.py candidate` rebuilds it
RUNS = A / 'tools/pangram-runs'
DATE = '2026-10-18 (turn 72)'


def g65(stem):
    return (G65 / (stem + '.txt')).read_text(encoding='utf-8').strip()


def joel(stem):
    return (T / (stem + '.txt')).read_text(encoding='utf-8').strip()


def draft(stem):
    return (T / 'drafts' / (stem + '.txt')).read_text(encoding='utf-8').strip()


def photos():
    """His section as he sent it, with the one obvious typo fixed under his rule (2026-10-06): "glean" for "gleam"."""
    t = joel('joel-photos-h2')
    assert t.count('gleam') == 1
    return t.replace('might even gleam from', 'might even glean from')


SAID = 'experiments/t72-answers/JOEL-20261018-1906.md'


RW = os.environ.get('RW', 'rw-b1')   # the Remember When draft to install
RW2 = os.environ.get('RW2', 'rw-b4')   # its cold-read fix
KS2 = os.environ.get('KS2', 'ks1-t')   # the safety paragraph's cold-read fix

RESULTS = {}   # @@NAME@@ in a comment -> the checks' results, filled in once they're in (install)


def find(pattern):
    """The article's passage that PATTERN matches, or None once it has been replaced (installed)."""
    m = re.search(pattern, ART.read_text(encoding='utf-8'), re.S)
    return m.group(0) if m else None


G69 = A / 'experiments/t69-guide'


def d69(stem):
    return (G69 / 'drafts' / (stem + '.txt')).read_text(encoding='utf-8').strip()


def para(start):
    """The article's paragraph (one line) that starts with START, or None once it has been replaced."""
    for l in ART.read_text(encoding='utf-8').split('\n'):
        if l.startswith(start):
            return l
    return None


FG2 = os.environ.get('FG2', 'fg2-a')


INSTALLS = []   # (name, old, new) built by the functions below as the run goes; see register()


def installs(names=None):
    """(old, new): each replaces one exact passage of the article; NAMES picks some of them."""
    out = [(n, (o() if callable(o) else o), (w() if callable(w) else w)) for n, o, w in INSTALLS]
    return [(o, n) for name, o, n in out if (names is None or name in names) and o is not None]


def register(name, old, new):
    INSTALLS.append((name, old, new))


def candidate(names=None):
    t = ART.read_text(encoding='utf-8')
    for old, new in installs(names):
        assert t.count(old) == 1, old[:80]
        t = t.replace(old, new)
    CAND.write_text(t, encoding='utf-8')
    return t


def install(names, results_file):
    """Put NAMES into the article itself, with each @@NAME@@ in their comments replaced from RESULTS_FILE (JSON)."""
    res = json.loads(pathlib.Path(results_file).read_text(encoding='utf-8'))
    t = ART.read_text(encoding='utf-8')
    for old, new in installs(names):
        assert t.count(old) == 1, old[:80]
        for k, v in res.items():
            new = new.replace('@@%s@@' % k, v)
        assert '@@' not in new, new[:200]
        t = t.replace(old, new)
    ART.write_text(t, encoding='utf-8')


def section(md, heading):
    """The section under HEADING (its first line), to the next heading of the same or a higher level; no comments."""
    lines = md.split('\n')
    i = lines.index(heading)
    lvl = len(heading) - len(heading.lstrip('#'))
    j = next((k for k in range(i + 1, len(lines)) if re.match(r'#{1,%d} ' % lvl, lines[k])), len(lines))
    body = re.sub(r'<!--.*?-->', '', '\n'.join(lines[i:j]), flags=re.S)
    return '\n\n'.join(b.strip() for b in re.split(r'\n\s*\n', body) if b.strip())


def block(b):
    if b.startswith('#'):
        return b
    d, stem = b.split(':', 1)
    if d == 'S':   # a section of the article as it stands, comments out
        return section(ART.read_text(encoding='utf-8'), stem)
    if d == 'G':
        return g65(stem)
    if d == 'D0':   # turn 70's drafts
        return (A / 'experiments/t70-guide/drafts' / (stem + '.txt')).read_text(encoding='utf-8').strip()
    if d == 'D9':   # turn 69's drafts
        return (A / 'experiments/t69-guide/drafts' / (stem + '.txt')).read_text(encoding='utf-8').strip()
    if d == 'D7':   # turn 67's drafts
        return (A / 'experiments/t67-guide/drafts' / (stem + '.txt')).read_text(encoding='utf-8').strip()
    if d == 'J7':   # his turn-67 texts
        return (A / 'experiments/t67-guide' / (stem + '.txt')).read_text(encoding='utf-8').strip()
    if d == 'J':
        return photos().split('\n', 1)[1].strip() if stem == 'joel-photos-h2' else joel(stem)
    return (T / 'drafts' / (stem + '.txt')).read_text(encoding='utf-8').strip()


def batch(rnd, spec_file):
    spec = json.loads(pathlib.Path(spec_file).read_text(encoding='utf-8'))
    march = json.loads((T / 'MARCH.json').read_text(encoding='utf-8'))
    md = {'candidate': CAND.read_text(encoding='utf-8'), 'article': ART.read_text(encoding='utf-8')}
    drafts, gate, rows = {}, {}, []
    for it in spec:
        k = 't72%s_%s' % (rnd, it['key'])
        if 'draft' in it:
            text = (T / 'drafts' / (it['draft'] + '.txt')).read_text(encoding='utf-8').strip()
            la = ART
            if it.get('his'):   # his published sentences in the draft (2026-10-17 16:58: "yes they are [my words]") count as his
                la = CAND.with_name('lint-%s.md' % k)
                la.write_text(ART.read_text(encoding='utf-8') + '\n\n' + '\n\n'.join(it['his']), encoding='utf-8')
            gate[k] = {'kind': 'screen', 'march': [march[it['draft']]], 'lint': 'REVIEW', 'lint_article': str(la),
                       'note': 't72%s: %s, alone.' % (rnd, it['draft'])}
        elif 'blocks' in it:   # a section put together: a heading, G:stem (t65-guide), J:stem (his, here), D:stem (drafts/)
            text = '\n\n'.join(block(b) for b in it['blocks'])
            # the settled parts (G: read Human alone, J: his) count as installed for the linter; only my new drafts (D:) are
            # linted as mine
            la = CAND.with_name('lint-%s.md' % k)
            la.write_text(md['candidate'] + '\n\n' + '\n\n'.join(block(b) for b in it['blocks'] if b.split(':')[0] in ('G', 'J', 'S', 'J7', 'D7', 'D9', 'D0')) + '\n\n' + '\n\n'.join(it.get('his', [])),
                          encoding='utf-8')   # his published lines in my drafts count as his (E188, E189)
            gate[k] = {'kind': 'screen', 'march': [it['march']], 'lint': 'REVIEW', 'lint_article': str(la),
                       'note': 't72%s: %s, put together: %s.' % (rnd, it['blocks'][0], ', '.join(it['blocks'][1:]))}
        elif 'para' in it:     # one paragraph of a section as it would be installed (his, with a typo fixed)
            text = section(md['candidate'], it['para'][0]).split('\n\n')[it['para'][1]]
            gate[k] = {'kind': 'screen', 'march': [it['march']], 'lint': 'REVIEW', 'lint_article': str(CAND),
                       'note': 't72%s: paragraph %d under %s as it would be installed.' % (rnd, it['para'][1], it['para'][0])}
        else:
            src = it.get('article', 'candidate')
            if src not in md:   # a path: another candidate article (two placements in one batch, round t71uu)
                md[src] = pathlib.Path(src).read_text(encoding='utf-8')
            text = section(md[src], it['section'])
            gate[k] = {'kind': 'screen', 'march': [it['march']], 'lint': 'REVIEW',
                       'lint_article': str(CAND if src == 'candidate' else ART if src == 'article' else src),
                       'note': 't72%s: %s as it would be installed; every paragraph has read Human alone or is Joel\'s.'
                               % (rnd, it['section'])}
        drafts[k] = text
        rows.append('| %s | %s (%d words) [%s], a screen | Human, low (my call) | (pending) | |'
                    % (DATE, it['label'], len(text.split()), k))
    out = RUNS / ('2026-10-18-turn72-%s' % rnd)
    (out.parent / (out.name + '-drafts.json')).write_text(json.dumps(drafts, indent=1, ensure_ascii=False), encoding='utf-8')
    (out.parent / (out.name + '-gate.json')).write_text(json.dumps(gate, indent=1, ensure_ascii=False), encoding='utf-8')
    cmd = [sys.executable, str(REPO / 'tools/humanization/pangram_gate.py'), str(out.parent / (out.name + '-drafts.json')),
           str(out.parent / (out.name + '-gate.json')), str(out.parent / (out.name + '.js')), '--name', 't72' + rnd,
           '--lint-article', str(ART)] + list(drafts)
    rc = subprocess.run(cmd, cwd=REPO).returncode
    if rc == 0:
        p = A / 'tools/PREDICTIONS.md'
        p.write_text(p.read_text(encoding='utf-8').rstrip('\n') + '\n' + '\n'.join(rows) + '\n', encoding='utf-8')
        print('%d checks, %d words' % (len(drafts), sum(len(t.split()) for t in drafts.values())))
    return rc


exec(open(pathlib.Path(__file__).with_name('installs72.py')).read()) if pathlib.Path(__file__).with_name('installs72.py').exists() else None


if __name__ == '__main__':
    if sys.argv[1] == 'candidate':
        candidate(sys.argv[2].split(',') if len(sys.argv) > 2 else []); print('wrote', CAND)   # names not installed yet
    elif sys.argv[1] == 'install':
        install(sys.argv[2].split(','), sys.argv[3]); print('installed', sys.argv[2])
    else:
        sys.exit(batch(sys.argv[2], sys.argv[3]))
