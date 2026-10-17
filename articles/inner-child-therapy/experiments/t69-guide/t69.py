"""Turn 69 (2026-10-17, Joel's 18:56 UTC answers): the batches and installs (a copy of turn 68's t68.py).

  python3 t69.py candidate               # CANDIDATE.md (scratch, not in the repo): the article with this turn's installs
  python3 t69.py batch ROUND SPEC.json   # one Pangram batch: alone screens of my drafts and section checks

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
T = A / 'experiments/t69-guide'
ART = A / 'HUMANIZED-ARTICLE-SO-FAR.md'
CAND = pathlib.Path('/tmp/claude-0/-home-claude/d17e637c-ae79-5296-a30e-05fa0a73af9d/scratchpad/t69/CANDIDATE.md')   # not kept in the repo: `t67.py candidate` rebuilds it
RUNS = A / 'tools/pangram-runs'
DATE = '2026-10-17 (turn 69)'


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


SAID = 'experiments/t69-answers/JOEL-20261017-1856.md'


RW = os.environ.get('RW', 'rw-b1')   # the Remember When draft to install

RESULTS = {}   # @@NAME@@ in a comment -> the checks' results, filled in once they're in (install)


def find(pattern):
    """The article's passage that PATTERN matches, or None once it has been replaced (installed)."""
    m = re.search(pattern, ART.read_text(encoding='utf-8'), re.S)
    return m.group(0) if m else None


def installs(names=None):
    """(old, new): each replaces one exact passage of the article; NAMES picks some of them (rw, ks)."""
    out = []
    # 39: Remember When P1, his own opening (his published father line was a paraphrase), then my humanized rest of the guide's
    old = find(r"<!-- Turn 68 \(E188\): his published words back at the start, \"My father often suggested remembering.*?"
               r"\(No example\? Try another way in\.\)")
    out.append(('rw', old,
                '<!-- Turn 69 (E189): Joel\'s opening, word for word (2026-10-17 18:56 UTC, his answer to question 39: "i see i got '
                'paraphrased about my father... change that para to say"; ' + SAID + '), with one obvious fix: his link had a '
                'space between ] and (. His published line, "My father often suggested remembering a time when I met a difficulty '
                'in a way I respected.", was a paraphrase of him, so it is out. Then my humanized version of the rest of the '
                'guide\'s passage (experiments/t69-guide/drafts/' + RW + '.txt): what helped then, one piece of it within reach, a '
                'small real example is enough (not a dramatic one; his "similar-level (or even harder)" carries the guide\'s "The '
                'earlier situation need not have been harder"), past capacity no proof that exhaustion or present limits should '
                'go (the stick), another doorway. @@RW@@ -->\n\n' + draft(RW)))
    # 39: If You Want to Kill Yourself, his own fuller opening as its own paragraph, as in his guide; then turn 65's P1 again
    old = find(r"<!-- Turn 68 \(E188\): his published first line of the section back at its start.*?"
               r"It just keeps the question open long enough to look at\.")
    out.append(('ks', old,
                '<!-- Turn 69 (E189): Joel\'s opening, word for word (2026-10-17 18:56 UTC, his answer to question 39: "i was '
                'paraphrased for if you want to kill yourself as well. the first sentence should be expanded to"; ' + SAID + '), '
                'with one obvious typo fixed under his rule: "proselytize" for his "prosletyze". It is its own paragraph, as the '
                'first sentence is in his guide; his published line, "When somebody tells me they want to kill themselves, I get '
                'stricter about spirituality, not looser.", was a paraphrase of him, so it is out. @@KS0@@ -->\n\n'
                + joel('joel-ks-p1') + '\n\n'
                '<!-- Turn 65 (E177), my own draft again as it was (writers/ks12-w8-p1), now that his opening is its own paragraph. '
                'Alone Human Written (0.2, low), https://www.pangram.com/history/981ab947-596f-4de7-8c7f-adbe370c04fe. @@KS1@@ -->'
                '\n\n' + g65('writers/ks12-w8-p1')))
    return [(o, n) for name, o, n in out if (names is None or name in names) and o is not None]


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
        k = 't69%s_%s' % (rnd, it['key'])
        if 'draft' in it:
            text = (T / 'drafts' / (it['draft'] + '.txt')).read_text(encoding='utf-8').strip()
            la = ART
            if it.get('his'):   # his published sentences in the draft (2026-10-17 16:58: "yes they are [my words]") count as his
                la = CAND.with_name('lint-%s.md' % k)
                la.write_text(ART.read_text(encoding='utf-8') + '\n\n' + '\n\n'.join(it['his']), encoding='utf-8')
            gate[k] = {'kind': 'screen', 'march': [march[it['draft']]], 'lint': 'REVIEW', 'lint_article': str(la),
                       'note': 't69%s: %s, alone.' % (rnd, it['draft'])}
        elif 'blocks' in it:   # a section put together: a heading, G:stem (t65-guide), J:stem (his, here), D:stem (drafts/)
            text = '\n\n'.join(block(b) for b in it['blocks'])
            # the settled parts (G: read Human alone, J: his) count as installed for the linter; only my new drafts (D:) are
            # linted as mine
            la = CAND.with_name('lint-%s.md' % k)
            la.write_text(md['candidate'] + '\n\n' + '\n\n'.join(block(b) for b in it['blocks'] if b.split(':')[0] in ('G', 'J', 'S', 'J7', 'D7')) + '\n\n' + '\n\n'.join(it.get('his', [])),
                          encoding='utf-8')   # his published lines in my drafts count as his (E188, E189)
            gate[k] = {'kind': 'screen', 'march': [it['march']], 'lint': 'REVIEW', 'lint_article': str(la),
                       'note': 't69%s: %s, put together: %s.' % (rnd, it['blocks'][0], ', '.join(it['blocks'][1:]))}
        elif 'para' in it:     # one paragraph of a section as it would be installed (his, with a typo fixed)
            text = section(md['candidate'], it['para'][0]).split('\n\n')[it['para'][1]]
            gate[k] = {'kind': 'screen', 'march': [it['march']], 'lint': 'REVIEW', 'lint_article': str(CAND),
                       'note': 't69%s: paragraph %d under %s as it would be installed.' % (rnd, it['para'][1], it['para'][0])}
        else:
            text = section(md[it.get('article', 'candidate')], it['section'])
            gate[k] = {'kind': 'screen', 'march': [it['march']], 'lint': 'REVIEW',
                       'lint_article': str(CAND if it.get('article', 'candidate') == 'candidate' else ART),
                       'note': 't69%s: %s as it would be installed; every paragraph has read Human alone or is Joel\'s.'
                               % (rnd, it['section'])}
        drafts[k] = text
        rows.append('| %s | %s (%d words) [%s], a screen | Human, low (my call) | (pending) | |'
                    % (DATE, it['label'], len(text.split()), k))
    out = RUNS / ('2026-10-17-turn69-%s' % rnd)
    (out.parent / (out.name + '-drafts.json')).write_text(json.dumps(drafts, indent=1, ensure_ascii=False), encoding='utf-8')
    (out.parent / (out.name + '-gate.json')).write_text(json.dumps(gate, indent=1, ensure_ascii=False), encoding='utf-8')
    cmd = [sys.executable, str(REPO / 'tools/humanization/pangram_gate.py'), str(out.parent / (out.name + '-drafts.json')),
           str(out.parent / (out.name + '-gate.json')), str(out.parent / (out.name + '.js')), '--name', 't69' + rnd,
           '--lint-article', str(ART)] + list(drafts)
    rc = subprocess.run(cmd, cwd=REPO).returncode
    if rc == 0:
        p = A / 'tools/PREDICTIONS.md'
        p.write_text(p.read_text(encoding='utf-8').rstrip('\n') + '\n' + '\n'.join(rows) + '\n', encoding='utf-8')
        print('%d checks, %d words' % (len(drafts), sum(len(t.split()) for t in drafts.values())))
    return rc


if __name__ == '__main__':
    if sys.argv[1] == 'candidate':
        candidate(sys.argv[2].split(',') if len(sys.argv) > 2 else []); print('wrote', CAND)   # names not installed yet
    elif sys.argv[1] == 'install':
        install(sys.argv[2].split(','), sys.argv[3]); print('installed', sys.argv[2])
    else:
        sys.exit(batch(sys.argv[2], sys.argv[3]))
