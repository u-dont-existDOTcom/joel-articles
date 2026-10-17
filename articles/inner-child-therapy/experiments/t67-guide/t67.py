"""Turn 67 (2026-10-17, Joel's 14:01 UTC answers): the candidate article with his texts installed, and the batches.

  python3 t67.py candidate               # CANDIDATE.md (scratch, not in the repo): the article with this turn's installs
  python3 t67.py batch ROUND SPEC.json   # one Pangram batch: alone screens of my drafts and section checks

SPEC.json is a list of items:
  {"key": "ks4a", "draft": "ks4-a", "label": "..."}                    a draft in drafts/, alone; its march from MARCH.json
  {"key": "secba", "section": "# Borrowed Adulthood in Relationship", "label": "...", "march": "...", "article": "candidate"}
A section is cut from CANDIDATE.md (or from the article as it stands), from its heading to the next heading of the same
or a higher level, with the comments taken out. Sections are linted with CANDIDATE.md as the installed text, since every
paragraph in them has read Human alone already (or is Joel's); drafts are linted against the article as it stands.
"""
import json
import pathlib
import re
import subprocess
import sys

REPO = pathlib.Path('/home/claude/joel-articles')
A = REPO / 'articles/inner-child-therapy'
G65 = A / 'experiments/t65-guide'
T = A / 'experiments/t67-guide'
ART = A / 'HUMANIZED-ARTICLE-SO-FAR.md'
CAND = pathlib.Path('/tmp/claude-0/-home-claude/d17e637c-ae79-5296-a30e-05fa0a73af9d/scratchpad/t67/CANDIDATE.md')   # not kept in the repo: `t67.py candidate` rebuilds it
RUNS = A / 'tools/pangram-runs'
DATE = '2026-10-17 (turn 67)'


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


SAID = 'experiments/t67-answers/JOEL-20261017-1401.md'


RESULTS = {}   # @@NAME@@ in a comment -> the checks' results, filled in once they're in (install)


def find(pattern):
    """The article's passage that PATTERN matches, or None once it has been replaced (installed)."""
    m = re.search(pattern, ART.read_text(encoding='utf-8'), re.S)
    return m.group(0) if m else None


def installs(names=None):
    """(old, new): each replaces one exact passage of the article; NAMES picks some of them (timing, photos, lm4, ba)."""
    out = []
    # 35: his P14, first under the guide's own subheading
    out.append(('timing', '## Timing Is Individual\n\n<!-- Turn 65 (E181), my own draft, groups 15 and 16',
                '## Timing Is Individual\n\n<!-- Turn 67: Joel\'s P14, word for word (2026-10-17 14:01 UTC, his answer to question 35: '
                '"added a marching order break that sounds a bit human, now it passes"; ' + SAID + '). His check counts for it '
                'alone. @@TIMING@@ -->\n\n' + joel('joel-guide-p14') + '\n\n<!-- Turn 65 (E181), my own draft, groups 15 and 16'))
    # 36: his Photos section, in the Simple Practices order (after the four still parked before it, Close the Session after)
    old = find(r"<!-- Parked from Simple Practices \(experiments/t65-guide/PARKED\.md, with what each needs from Joel\): "
               r"Journal With Each Hand;.*?They go here, in that order\. -->")
    ph = photos()
    head, body = ph.split('\n', 1)
    assert head == '## Use Childhood Photographs Gently'
    out.append(('photos', old,
                '<!-- Parked from Simple Practices (experiments/t65-guide/PARKED.md, with what each needs from Joel): Journal With '
                'Each Hand; And So That\'s the Way It Happened!; One Intention in the Morning, One Review at Night; Just Like Me. '
                'They go here, in that order. -->\n\n' + head + '\n\n<!-- Turn 67: Joel\'s section, word for word under his heading '
                '(2026-10-17 14:01 UTC, his answer to question 36: "here learn some lessons this passes"; ' + SAID + '; his '
                'paste is experiments/t67-guide/joel-photos-h2.txt). One obvious typo fixed under his rule (2026-10-06): '
                '"glean" for "gleam" in P2. His check counts for the section as he sent it. @@PHOTOS@@ -->\n\n' + body.strip() +
                '\n\n<!-- Parked from Simple Practices (experiments/t65-guide/PARKED.md): Close the Session and Return to Life. '
                'It goes here. -->'))
    # 34: How Much Happiness, with his P4, and new P1 to P3 of mine (rounds t67b to t67e: with the turn-65 ones the h2 read AI)
    old = find(r"<!-- Parked: How Much Happiness Do You Know Is Possible\?.*?It goes here\. -->")
    out.append(('lm4', old,
                '## How Much Happiness Do You Know Is Possible?\n\n'
                '<!-- Turn 67 (E186), my own draft (experiments/t67-guide/drafts/lm4-p1-j6.txt; GROUNDING-lm4.md): what you picture '
                'when you wish someone well, practical love (babies get it), and how far the wish reaches depending on the happiness '
                'you know is possible. The turn-65 P1 read Human alone, but the h2 read AI over it with every P2 and P3 (its first '
                'sentence echoed the heading); without any P1 the h2 read Human (round t67c). Alone Human Written (0.37, low), '
                'https://www.pangram.com/history/2cb5b084-39b3-425a-af1f-218bfa1b0052. -->\n\n' + draft('lm4-p1-j6') + '\n\n'
                '<!-- Turn 67 (E186), my own draft (lm4-p2-j3): a big spiritual experience can show a peace or a love you didn\'t '
                'know existed; why loving-kindness can sound simple or powerful; repeating the phrase isn\'t automatically profound '
                'love (the grounding\'s [7]), and it\'s one way to find and grow it. Alone Human Written (0.011, low), '
                'https://www.pangram.com/history/21264e66-a92b-4a1d-bc64-416a8e0f6d13. -->\n\n' + draft('lm4-p2-j3') + '\n\n'
                '<!-- Turn 67 (E186), my own draft (lm4-p3-j2): follow the curiosity without pretending to believe; read and meet '
                'people across traditions; judge a path by its fruits, not by how certain it makes people (the guide\'s G4.11, '
                'which the turn-65 writer\'s version had lost). Alone Human Written (0.03, low), '
                'https://www.pangram.com/history/76179f60-f36c-4f03-9011-f7462be1df33. -->\n\n' + draft('lm4-p3-j2') + '\n\n'
                '<!-- Turn 67: Joel\'s P4, word for word (2026-10-17 14:01 UTC, his answer to question 34: "this one is human"; '
                + SAID + '). His check counts for it alone. @@LM4@@ -->\n\n' + joel('joel-lm4-p4') + '\n\n'
                '<!-- Turn 65, my own draft (lm4-p5-c): curiosity can be enough, and the limits of what you\'ve felt aren\'t the '
                'limits of what\'s possible. Alone Human Written (0.002, low), '
                'https://www.pangram.com/history/c690f23b-fdb2-4e14-a2ed-663e50460455. -->\n\n' + g65('lm4-p5-c')))
    # 32: If You Want to Kill Yourself, with his P2; the Buddhist view (P4) and the edits of P4b and P5 are this turn's
    old = find(r"<!-- Parked between the love section and this one \(experiments/t65-guide/PARKED\.md, with what each needs "
               r"from Joel\): If You Want to Kill Yourself.*?They go here, in that order\. -->")
    out.append(('ks', old,
                '# If You Want to Kill Yourself\n\n'
                '<!-- Turn 65 (E177), my own draft (writers/ks12-w8-p1; GROUNDING-ks01.md\'s MUSTs: a crisis line or emergency number '
                'counts as another human being, and if you can\'t tell whether it\'s you, treat it like it is). Alone Human Written '
                '(0.2, low), https://www.pangram.com/history/981ab947-596f-4de7-8c7f-adbe370c04fe. -->\n\n' + g65('writers/ks12-w8-p1') +
                '\n\n<!-- Turn 67: Joel\'s P2, word for word (2026-10-17 14:01 UTC, his answer to question 32: "i removed most of the '
                'AI tells, this is now human and it makes more sense"; ' + SAID + '). His check counts for it alone. -->\n\n'
                + joel('joel-ks-p2') + '\n\n'
                '<!-- Turn 65, my own draft (ks1-p3-a): what is the self you want to kill, and what makes you sure destroying the '
                'body ends a state of mind. Alone Human Written (0.002, low), '
                'https://www.pangram.com/history/a691708e-29fa-4c24-802d-4f27c341a066. -->\n\n' + g65('ks1-p3-a') + '\n\n'
                '<!-- Turn 67 (E186, E187), my own draft (experiments/t67-guide/drafts/ks4-o.txt): the Buddhist view in plain words, '
                'close to the guide. The turn-65 record said an earlier version read Human alone; that result was another file\'s '
                '(E187), and fourteen versions had read AI (0.36 to 0.98) before this one. Alone Human Written (0.099, low), '
                'https://www.pangram.com/history/6c232c89-9116-4d0c-accb-c662f29f9ac7. -->\n\n' + draft('ks4-o') + '\n\n'
                '<!-- Turn 65\'s ks1-p4c (the grounding\'s [16]: for someone weighing it, and anyone at the edge does the first step '
                'first; alone Human 0.39) with its last sentence changed in turn 67 (drafts/ks4b-e1.txt), since the h1 had an AI '
                'window from it into P5. Alone Human Written (0.19, low), '
                'https://www.pangram.com/history/1c284efa-a488-49ea-9829-a18c8cd5cdab. -->\n\n' + draft('ks4b-e1') + '\n\n'
                '<!-- Turn 65\'s ks1-p5-b (alone Human 0.086) changed in turn 67 (drafts/ks5-e2.txt): its first sentence (its "that '
                'momentum" had nothing to point to after P4b), its three short claims (two kept, isolation an aside) and its '
                '"without taking away" ending (E186). Alone Human Written (0.2, low), '
                'https://www.pangram.com/history/22b9a51c-c3c4-46dd-8ede-a73ad8a59a8e. "The accumulating scientific evidence" is '
                'the guide\'s claim, still Joel\'s to call (OWNER-QUESTIONS). -->\n\n' + draft('ks5-e2') + '\n\n'
                '<!-- Turn 65, my own draft (ks1-p6-d): the change you still can\'t make; smaller than dying but not free, and it can '
                'wait until you\'re calmer and have help (the grounding\'s [28]). Alone Human Written (0.022, low), '
                'https://www.pangram.com/history/04587d39-7d40-4cd2-b6b1-96173fe546ae. The h1 with every paragraph read Human '
                'Written (0.24, high, 601 words), https://www.pangram.com/history/71cbf2e1-e6dd-4d34-a1b7-96cd6b4a192f (round t67e). -->'
                '\n\n' + g65('ks1-p6-d') + '\n\n'
                '<!-- Parked between this section and When the Practice Feels Real but Stays Shallow (experiments/t65-guide/PARKED.md, '
                'with what each needs from Joel): This human life is the most precious opportunity (the guide\'s first person about '
                'his own life); Altered States Can Deepen the Therapy, Altered States Can Require Reparenting and Non-altered states '
                'can feel like this too (his own stories, guides and images). They go here, in that order. -->'))
    # 33: Borrowed Adulthood, P1 (w8; with w9 the h1 read AI in round a) and his P2
    old = find(r"<!-- Parked between this section and the closing \(experiments/t65-guide/PARKED\.md, with what each "
               r"needs from Joel\): When One Life Has Ended.*?They go here, in that order\. -->")
    out.append(('ba', old,
                '<!-- Parked between this section and Borrowed Adulthood (experiments/t65-guide/PARKED.md, with what it needs): '
                'When One Life Has Ended and the Next Hasn\'t Begun (its P1 reads Human alone; P2 and P3 are this turn\'s work). '
                'It goes here. -->\n\n# Borrowed Adulthood in Relationship\n\n'
                '<!-- Turn 65 (E177), my own draft (writers/ba1p1-w8-p1; GROUNDING-ba01.md): reparenting is usually talked about as '
                'something done alone or with a therapist, but a relational hurt heals only so far alone; one person may be doing a '
                'lot of the borrowed grown-up jobs at once, which can be an enormous blessing while you struggle. Alone Human Written '
                '(0.21, medium), https://www.pangram.com/history/847b3962-516a-440b-887c-2166e1523f9e. @@BA1@@ -->\n\n' + g65('writers/ba1p1-w8-p1') +
                '\n\n<!-- Turn 67: Joel\'s P2, word for word (2026-10-17 14:01 UTC, his answer to question 33: "this version passes"; '
                + SAID + '). His check counts for it alone. @@BA2@@ -->\n\n' + joel('joel-ba-p2') + '\n\n'
                '<!-- Parked between this section and the closing (experiments/t65-guide/PARKED.md, with what it needs from Joel): '
                'Speak Toward What You Are Building (P3 and P4 read Human alone and together; P1, P2, P5 and P6 never did; the '
                'guide\'s Hearthwork naming needs him). It goes here. -->'))
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
    if d == 'J':
        return photos().split('\n', 1)[1].strip() if stem == 'joel-photos-h2' else joel(stem)
    return (T / 'drafts' / (stem + '.txt')).read_text(encoding='utf-8').strip()


def batch(rnd, spec_file):
    spec = json.loads(pathlib.Path(spec_file).read_text(encoding='utf-8'))
    march = json.loads((T / 'MARCH.json').read_text(encoding='utf-8'))
    md = {'candidate': CAND.read_text(encoding='utf-8'), 'article': ART.read_text(encoding='utf-8')}
    drafts, gate, rows = {}, {}, []
    for it in spec:
        k = 't67%s_%s' % (rnd, it['key'])
        if 'draft' in it:
            text = (T / 'drafts' / (it['draft'] + '.txt')).read_text(encoding='utf-8').strip()
            gate[k] = {'kind': 'screen', 'march': [march[it['draft']]], 'lint': 'REVIEW', 'lint_article': str(ART),
                       'note': 't67%s: my own draft %s (E186: Joel\'s 14:01 lessons), alone.' % (rnd, it['draft'])}
        elif 'blocks' in it:   # a section put together: a heading, G:stem (t65-guide), J:stem (his, here), D:stem (drafts/)
            text = '\n\n'.join(block(b) for b in it['blocks'])
            # the settled parts (G: read Human alone, J: his) count as installed for the linter; only my new drafts (D:) are
            # linted as mine
            la = CAND.with_name('lint-%s.md' % k)
            la.write_text(md['candidate'] + '\n\n' + '\n\n'.join(block(b) for b in it['blocks'] if b[:2] in ('G:', 'J:', 'S:')),
                          encoding='utf-8')
            gate[k] = {'kind': 'screen', 'march': [it['march']], 'lint': 'REVIEW', 'lint_article': str(la),
                       'note': 't67%s: %s, put together: %s.' % (rnd, it['blocks'][0], ', '.join(it['blocks'][1:]))}
        elif 'para' in it:     # one paragraph of a section as it would be installed (his, with a typo fixed)
            text = section(md['candidate'], it['para'][0]).split('\n\n')[it['para'][1]]
            gate[k] = {'kind': 'screen', 'march': [it['march']], 'lint': 'REVIEW', 'lint_article': str(CAND),
                       'note': 't67%s: paragraph %d under %s as it would be installed.' % (rnd, it['para'][1], it['para'][0])}
        else:
            text = section(md[it.get('article', 'candidate')], it['section'])
            gate[k] = {'kind': 'screen', 'march': [it['march']], 'lint': 'REVIEW',
                       'lint_article': str(CAND if it.get('article', 'candidate') == 'candidate' else ART),
                       'note': 't67%s: %s as it would be installed; every paragraph has read Human alone or is Joel\'s.'
                               % (rnd, it['section'])}
        drafts[k] = text
        rows.append('| %s | %s (%d words) [%s], a screen | Human, low (my call) | (pending) | |'
                    % (DATE, it['label'], len(text.split()), k))
    out = RUNS / ('2026-10-17-turn67-%s' % rnd)
    (out.parent / (out.name + '-drafts.json')).write_text(json.dumps(drafts, indent=1, ensure_ascii=False), encoding='utf-8')
    (out.parent / (out.name + '-gate.json')).write_text(json.dumps(gate, indent=1, ensure_ascii=False), encoding='utf-8')
    cmd = [sys.executable, str(REPO / 'tools/humanization/pangram_gate.py'), str(out.parent / (out.name + '-drafts.json')),
           str(out.parent / (out.name + '-gate.json')), str(out.parent / (out.name + '.js')), '--name', 't67' + rnd,
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
