"""Section 16's side-by-side page for Joel: the draft now in the article beside the published section (2026-10-17), each
paragraph with the Pangram check that read its exact text alone (or with its neighbor when it is under 50 words), the whole
section's check, and the notes he needs (what the dedup cut and where it is said, the published words the meaning checks put
back). Run from the repo root: python3 articles/intentional-communities/candidate/s16/make_page.py DRAFT BATCH KEY"""
import json, pathlib, re, subprocess, sys

REPO = pathlib.Path(__file__).resolve().parents[4]
C = REPO / 'articles' / 'intentional-communities' / 'candidate'
S16 = C / 's16'
sys.path.insert(0, str(C / 'tools'))
import page_checks  # noqa: E402

DRAFT, BATCH, KEY = sys.argv[1], sys.argv[2], sys.argv[3]
md = (S16 / DRAFT).read_text(encoding='utf-8')
assert md.strip() in (C / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8'), 'install the draft first (s16/install/install_s16.py)'
SKIP = re.compile(r'^(\[image \d+\]|\[caption\])')


def sections(text):
    out = []
    for b in [b.strip() for b in re.split(r'\n\s*\n', text) if b.strip()]:
        if b.startswith('#'):
            out.append((b, []))
        elif not SKIP.match(b):
            out[-1][1].append(b)
    return out


P, R = sections((S16 / 'v0.md').read_text(encoding='utf-8')), sections(md)
assert [len(x[1]) for x in P] == [3, 6, 11] and [len(x[1]) for x in R] == [3, 6, 10], ([len(x[1]) for x in P], [len(x[1]) for x in R])
IDS = [['H1-P%d' % i for i in range(1, 4)], ['H2-P%d' % i for i in range(1, 7)], ['H3-P%d' % i for i in range(2, 12)]]
PUB = [P[0][1], P[1][1], P[2][1][1:]]          # the published H3-P1, the lead-in line, went in the dedup
BATCHES = sorted(p for p in S16.glob('b3*') if (p / 'drafts.json').exists())
CHECK = {p: g for p, g in page_checks.alone(md, BATCHES)}
whole = json.loads((S16 / BATCH / ('%s-results.json' % BATCH)).read_text(encoding='utf-8'))[KEY]
NOTE = {
 'H1-P2': 'Your order of 2026-10-16 23:38, every step of it: practice, a real conflict, values, membership, ownership and exit, then land.',
 'H1-P3': ('The first money stage (households that stop buying the basics among themselves while outside earners put in a share) '
           'is not repeated here: section 4, "The container", says it in your words.'),
 'H2-P4': '"already contains a real piece of community" is not repeated here: section 13 opens with it.',
 'H2-P5': ('"build the part of community you actually can": a meaning check found "the part of it" had no noun for "it" since the '
           'dedup, so your noun is back.'),
 'H3-P2': ('Your lead-in "Here is the first month without the heroic land purchase:" is cut: the section says land can wait four '
           'other times, and the heading says "This Month".'),
 'H3-P3': ('Your "Call it a practice group rather than a commune" and your four skills as the full list: a meaning check found '
           'that "not quite the same thing as forming a commune" and "skills ... like listening" had shifted them.'),
 'H3-P5': 'Your "current visitor requirements" is back: a meaning check found "their requirements" had lost it.',
 'H3-P6': 'A meaning check found "right after the first communal shower you take" added a timing; it is your "make you start looking at studio apartments" now.',
 'H3-P7': 'A meaning check found "the land is the exciting part" added a claim; just "I know!" now.',
 'H3-P8': ('Your "real" care is back (a meaning check found it lost). "I\'m in Sénégal and expect to buy land, but I\'m not '
           'announcing a commune." is not repeated here: section 2 says it.'),
 'H3-P9': ('"He made a film, founded a research organization, and carried me through communal experiments." is not repeated '
           'here: sections 1 and 14 say it.'),
}
start = lambda t: ' '.join(re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', t).split()[:6])
blocks = []
for hi, ((h, _), (_, rps)) in enumerate(zip(P, R)):
    rows = []
    for j, text in enumerate(rps):
        pid = IDS[hi][j]
        g = CHECK.get(text) or []
        notes = [page_checks.note(g[0])] if g else ['no check of this text alone yet']
        if pid in NOTE:
            notes.append(NOTE[pid])
        rows.append({'label': '', 'article': start(text), 'source': [start(PUB[hi][j])[:60]], 'notes': notes})
    blocks.append({'headings': [h], 'rows': rows})
out = {'title': 'Practice Comes Before Property · section 16 (%s, in the article) beside the published one' % DRAFT[:-3],
       'meta': 'Community article · section 16 · %s, 2026-10-17 · in the article, not accepted until you say so' % DRAFT[:-3],
       'intro': ['Your published section is on the left; %s, now in the article, is on the right. Each row shows the check that read '
                 'that paragraph alone, or with its neighbor when it is short (your rule: every paragraph passes alone).' % DRAFT[:-3],
                 'The whole section reads %s (%s, %s words, AI likelihood %.2f): https://www.pangram.com/history%s'
                 % (whole[0].replace(' Written', ''), BATCH[1:] + 'g', whole[2], whole[1], whole[5]),
                 'How it was made: Emulate rewrote the opening and each subsection from your published text, and your meaning went '
                 'back inside its sentences; every hand-written version of "What to Do This Month" read AI. Meaning checks then '
                 'compared every paragraph with yours, and each point that had slipped got your words back before the last Pangram '
                 'checks. Five things are cut as repeats of other sections, each noted where it was.'],
       'blocks': blocks}
(S16 / 'page').mkdir(exist_ok=True)
mp = S16 / 'page' / ('ic16-%s.json' % DRAFT[:-3])
mp.write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'render_in_context.py'), str(mp),
                    str(C / 'community-section16-side-by-side.html'), '--article', str(C / 'HUMANIZED-SO-FAR.md'),
                    '--source', str(C.parent / 'original.md'), '--against-source'], capture_output=True, text=True)
print(r.returncode, (r.stdout + r.stderr)[-800:])
