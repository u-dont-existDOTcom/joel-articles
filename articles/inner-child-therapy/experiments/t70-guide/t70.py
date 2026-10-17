"""Turn 70 (2026-10-17, Joel's 22:59 UTC answers): the batches and installs (a copy of turn 69's t69.py).

  python3 t70.py candidate               # CANDIDATE.md (scratch, not in the repo): the article with this turn's installs
  python3 t70.py batch ROUND SPEC.json   # one Pangram batch: alone screens of my drafts and section checks

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
T = A / 'experiments/t70-guide'
ART = A / 'HUMANIZED-ARTICLE-SO-FAR.md'
CAND = pathlib.Path('/tmp/claude-0/-home-claude/d17e637c-ae79-5296-a30e-05fa0a73af9d/scratchpad/t70/CANDIDATE.md')   # not kept in the repo: `t67.py candidate` rebuilds it
RUNS = A / 'tools/pangram-runs'
DATE = '2026-10-17 (turn 70)'


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


SAID = 'experiments/t70-answers/JOEL-20261017-2259.md'


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


def installs(names=None):
    """(old, new): each replaces one exact passage of the article; NAMES picks some of them (st, bh, lm, sh, fg2, fg3)."""
    out = []
    # 44: Speak Toward What You Are Building, with his P1, P2 and P5
    old = find(r"<!-- Parked between this section and the closing \(experiments/t65-guide/PARKED\.md, with what it needs from Joel\): "
               r"Speak Toward What You Are Building.*?It goes here\. -->")
    out.append(('st', old,
        '# Speak Toward What You Are Building\n\n'
        '<!-- Turn 70: Joel\'s P1, word for word (2026-10-17 22:59 UTC, his answer to question 44: "I made changes to the end, then '
        'the beginning, and then the middle. Each part required changes as each part was being shown by itself as AI ... now human '
        'high conf on pangram"; ' + SAID + '), with one obvious typo fixed under his rule: "lilies" for his "lillies". His check '
        'counts for it alone. -->\n\n' + joel('joel-st-p1') + '\n\n'
        '<!-- Turn 70: Joel\'s P2, word for word (his answer to question 44: "the ai para was not very clear, and it also had that '
        'pollished ai quip pattern where it\'s like "that\'s X, not Y". it\'s better this way and human med conf"; ' + SAID + '). His '
        'check counts for it alone. -->\n\n' + joel('joel-st-p2') + '\n\n'
        '<!-- Turn 65 (E177), a writer\'s draft (experiments/t65-guide/writers/st1p3-w1-p1): find out what kind of company someone '
        'wants; not a ritual; follow an obvious mode. Alone Human Written (0.057, low), '
        'https://www.pangram.com/history/eddb9b08-8bf3-444b-bdeb-d3c349b9ba45. -->\n\n' + g65('writers/st1p3-w1-p1') + '\n\n'
        '<!-- Turn 69 (E188, E189), my own draft (experiments/t69-guide/drafts/hw-d.txt): his framework\'s basic premise in his '
        'own words (his guide\'s "Hearthwork, my peer-counseling framework, begins:" with his Hearthwork article\'s "The basic premise '
        'is:"; question 43, 3: "my words"), then a third kind of relationship next to friendship and therapy, one your little one may '
        'need. Alone Human Written (0.32, low), https://www.pangram.com/history/d8e227db-b7b3-44d2-9114-8ff9afebd93f. -->\n\n'
        + d69('hw-d') + '\n\n'
        '<!-- Turn 65, my join of a writer\'s Human half (experiments/t65-guide/writers/st1p4-w8-p1): what a good peer lends you '
        '(Nurturer, Protector) and what they don\'t (your Guide, the meaning); a question at the right moment; then you trade '
        'places. Alone Human Written (0.22, medium), https://www.pangram.com/history/863d3a02-3e38-41d8-9c68-c6abe0c41f20. -->\n\n'
        + g65('writers/st1p4-w8-p1') + '\n\n'
        '<!-- Turn 70: Joel\'s P5, word for word (his answer to question 44: "Just a little loosening of the march is what it needed. '
        'this is human"; ' + SAID + '). His check counts for it alone. -->\n\n' + joel('joel-st-p5') + '\n\n'
        '<!-- Turn 69, my own draft (experiments/t69-guide/drafts/st6a-c.txt): community works both ways (the people first, or the '
        'opening first and then who you "manifest"); community makes it practical, real, down to earth, embodied. Alone Human '
        'Written (0.010, low), https://www.pangram.com/history/2028fb7f-c78b-41de-aa3d-a49591f5fb67. -->\n\n' + d69('st6a-c') + '\n\n'
        '<!-- Turn 69 (E188, E189), my own draft (experiments/t69-guide/drafts/st6b-a.txt): his published "This is part of why I '
        'connect inner-child pl/ork with Hearthwork and with building community." (question 43, 4: "my words"), then the loop. Alone '
        'Human Written (0.0098, low), https://www.pangram.com/history/613b1e94-cc35-46dd-80e8-4b0cd3dd20b6. @@STH1@@ -->\n\n'
        + d69('st6b-a')))
    # 43, items 9 to 12: his first person back ("9. a 10 a 11 a 12 a")
    for name, start, stem, what in (
            ('bh', 'A question to borrow from your future self', 'bh-a', 'his guide\'s "I sometimes ask:" back at the start (question 43, 9: A), with "It\'s a question borrowed from your future self." so "that person" still has something to point to'),
            ('lm', 'What do you picture when you wish someone well', 'lm-a', 'his guide\'s "The horizon of what I can wish for someone is partly shaped by the happiness, peace, and freedom I know are possible." for my last sentence (question 43, 10: A)'),
            ('sh', 'Some people have the opposite problem', os.environ.get('SH', 'sh-a'), 'his guide\'s "What showed me that the daytime pl/ork had stayed shallow was the difference at night." for my "So say the dream that night ..." (question 43, 11: A), and the sign put as a condition after it'),
            ('fg2', 'What can help is seeing how they got there', FG2, 'his guide\'s "The understanding that helps me is seeing how a person\'s conditioning, history, pain, and capacity shaped the harmful move they made." for my first two sentences (question 43, 12: A), with my list of what made them who they were cut, since his line has it'),
            ('fg3', 'They still have to answer for what they did', 'fg3-a', 'his guide\'s "Understanding somebody\'s limitations should make my expectations more realistic, not make those limitations less consequential." back before the two quotes (question 43, 12: A)')):
        old = para(start)
        out.append((name, old, '<!-- Turn 70 (E189): ' + what + '; experiments/t70-guide/drafts/' + stem + '.txt. Joel, 2026-10-17 22:59 UTC: "43 my '
                    'words" and "9. a 10 a 11 a 12 a" (' + SAID + '). @@' + name.upper() + '@@ -->\n\n' + draft(stem)))
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
        k = 't70%s_%s' % (rnd, it['key'])
        if 'draft' in it:
            text = (T / 'drafts' / (it['draft'] + '.txt')).read_text(encoding='utf-8').strip()
            la = ART
            if it.get('his'):   # his published sentences in the draft (2026-10-17 16:58: "yes they are [my words]") count as his
                la = CAND.with_name('lint-%s.md' % k)
                la.write_text(ART.read_text(encoding='utf-8') + '\n\n' + '\n\n'.join(it['his']), encoding='utf-8')
            gate[k] = {'kind': 'screen', 'march': [march[it['draft']]], 'lint': 'REVIEW', 'lint_article': str(la),
                       'note': 't70%s: %s, alone.' % (rnd, it['draft'])}
        elif 'blocks' in it:   # a section put together: a heading, G:stem (t65-guide), J:stem (his, here), D:stem (drafts/)
            text = '\n\n'.join(block(b) for b in it['blocks'])
            # the settled parts (G: read Human alone, J: his) count as installed for the linter; only my new drafts (D:) are
            # linted as mine
            la = CAND.with_name('lint-%s.md' % k)
            la.write_text(md['candidate'] + '\n\n' + '\n\n'.join(block(b) for b in it['blocks'] if b.split(':')[0] in ('G', 'J', 'S', 'J7', 'D7')) + '\n\n' + '\n\n'.join(it.get('his', [])),
                          encoding='utf-8')   # his published lines in my drafts count as his (E188, E189)
            gate[k] = {'kind': 'screen', 'march': [it['march']], 'lint': 'REVIEW', 'lint_article': str(la),
                       'note': 't70%s: %s, put together: %s.' % (rnd, it['blocks'][0], ', '.join(it['blocks'][1:]))}
        elif 'para' in it:     # one paragraph of a section as it would be installed (his, with a typo fixed)
            text = section(md['candidate'], it['para'][0]).split('\n\n')[it['para'][1]]
            gate[k] = {'kind': 'screen', 'march': [it['march']], 'lint': 'REVIEW', 'lint_article': str(CAND),
                       'note': 't70%s: paragraph %d under %s as it would be installed.' % (rnd, it['para'][1], it['para'][0])}
        else:
            text = section(md[it.get('article', 'candidate')], it['section'])
            gate[k] = {'kind': 'screen', 'march': [it['march']], 'lint': 'REVIEW',
                       'lint_article': str(CAND if it.get('article', 'candidate') == 'candidate' else ART),
                       'note': 't70%s: %s as it would be installed; every paragraph has read Human alone or is Joel\'s.'
                               % (rnd, it['section'])}
        drafts[k] = text
        rows.append('| %s | %s (%d words) [%s], a screen | Human, low (my call) | (pending) | |'
                    % (DATE, it['label'], len(text.split()), k))
    out = RUNS / ('2026-10-17-turn70-%s' % rnd)
    (out.parent / (out.name + '-drafts.json')).write_text(json.dumps(drafts, indent=1, ensure_ascii=False), encoding='utf-8')
    (out.parent / (out.name + '-gate.json')).write_text(json.dumps(gate, indent=1, ensure_ascii=False), encoding='utf-8')
    cmd = [sys.executable, str(REPO / 'tools/humanization/pangram_gate.py'), str(out.parent / (out.name + '-drafts.json')),
           str(out.parent / (out.name + '-gate.json')), str(out.parent / (out.name + '.js')), '--name', 't70' + rnd,
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
