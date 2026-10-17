"""The appendix's side-by-side page for Joel: v9, now in the article, beside the published appendix (2026-10-17), each entry with
the Pangram check that read its exact text (alone, with its neighbor under its heading, or in the shortest run Pangram can
read, for the one-line entries), the whole appendix's check (343g), and the notes he needs: question 41 (the breaks in the
list) and the changes the meaning checks asked for.
Run from the repo root: python3 articles/intentional-communities/candidate/appendix/make_page_v9.py"""
import json, pathlib, re, subprocess, sys

REPO = pathlib.Path(__file__).resolve().parents[4]
C = REPO / 'articles' / 'intentional-communities' / 'candidate'
APX = C / 'appendix'
sys.path.insert(0, str(C / 'tools'))
import page_checks  # noqa: E402

v9 = (APX / 'v9.md').read_text(encoding='utf-8')
assert v9.strip() in (C / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8'), 'install v9 first (appendix/install/install_apx_v9.py)'


def sections(md):
    """[([headings], [entries])] in order; headings with no entry of their own go with the next one"""
    out, heads = [], []
    for b in [b.strip() for b in re.split(r'\n\s*\n', md) if b.strip()]:
        if b.startswith('#'):
            if out and not out[-1][1]:
                out[-1][0].append(b)
            else:
                out.append(([b], []))
        elif not b.startswith(('[image', '[caption')):
            out[-1][1].append(b)
    return out


P, R = sections((APX / 'v0.md').read_text(encoding='utf-8')), sections(v9)
assert [len(x[1]) for x in P] == [len(x[1]) for x in R], ([len(x[1]) for x in P], [len(x[1]) for x in R])
assert sum(len(x[1]) for x in R) == 25
BATCHES = sorted(p for p in APX.glob('b3*') if (p / 'drafts.json').exists())
CHECK = {p: g for p, g in page_checks.alone(v9, BATCHES)}
r343 = json.loads((APX / 'b343' / 'b343-results.json').read_text(encoding='utf-8'))['APXv9']
NOTE = {
 3: ('Question 41 on the questions page: each run of short entries that Pangram reads together got one break, a question or an '
     'aside; this is the one for the films ("Why this one?").'),
 9: 'Your "My father lived there for 17 years." is cut as a repeat: sections 1 and 4 say it.',
 1: 'Your "and now online" is cut as a repeat: section 1 says the film is online, and the entry links it.',
 12: ('A meaning check asked for your three topics as three things the book is about (an earlier version made autonomy and the '
      'shared care results of the first); the list as one sentence read AI with Liedloff\'s entry, so it is two sentences.'),
 13: ('"Sequencing" is gone, by your answer of 10-16 23:38 (your order, in section 16, comes first); "start here" is now a '
      'question scoped to the nuts and bolts.'),
 25: ('The opening is your heading\'s words, "the research behind this": the first version, "If you\'re curious how I got to all '
      'this", made the research the route to your whole model, and a stance check flagged it. This paragraph read AI alone in '
      'seven shapes before this one.'),
}
start = lambda t: ' '.join(re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', t).replace('*', '').split()[:6])
blocks, n = [], 0
for (hs, pps), (_, rps) in zip(P, R):
    rows = []
    for j, text in enumerate(rps):
        n += 1
        g = CHECK.get(text) or []
        notes = [page_checks.note(g[0])] if g else ['no check of this text yet']
        if n in NOTE:
            notes.append(NOTE[n])
        rows.append({'label': '', 'article': start(text), 'source': [start(pps[j])[:60]], 'notes': notes})
    blocks.append({'headings': hs, 'rows': rows})
out = {'title': 'Watch These, Then Read These · the appendix (v9, in the article) beside the published one',
       'meta': 'Community article · the appendix · v9, 2026-10-17 · in the article, not accepted until you say so',
       'intro': ['Your published appendix is on the left; v9, now in the article, is on the right. Each row shows the check that '
                 'read that entry: alone when it has 50 words, with the entry next to it under its heading when the two reach 50, '
                 'or else in the shortest run of entries Pangram can read (most entries are one or two sentences).',
                 'The whole appendix reads %s (343g, %s words, AI likelihood %.2f): https://www.pangram.com/history%s'
                 % (r343[0].replace(' Written', ''), r343[2], r343[1], r343[5]),
                 'How it was made: Emulate rewrote the entries, your meaning went back inside its sentences, and meaning checks '
                 'compared every entry with yours (five rounds), a cold read and a stance check against the whole essay; each '
                 'finding is fixed or answered in the rounds\' notes. Every title, author, year and link is kept.',
                 'One thing needs you: the breaks in the list (question 41).'],
       'blocks': blocks}
(APX / 'page').mkdir(exist_ok=True)
mp = APX / 'page' / 'icapx-v9.json'
mp.write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'render_in_context.py'), str(mp),
                    str(C / 'community-appendix-side-by-side.html'), '--article', str(C / 'HUMANIZED-SO-FAR.md'),
                    '--source', str(C.parent / 'original.md'), '--against-source'], capture_output=True, text=True)
print(r.returncode, (r.stdout + r.stderr)[-800:])
