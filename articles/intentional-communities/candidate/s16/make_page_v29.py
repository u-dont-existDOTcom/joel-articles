"""Section 16's side-by-side page for Joel (v29 and later; s16/make_page.py made the earlier ones): the draft now in the article beside the published section (2026-10-17), each
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
ONLY = '--draft-only' in sys.argv   # the draft is not in the article yet (question 42): shown in a copy of the article
md = (S16 / DRAFT).read_text(encoding='utf-8')
ARTICLE = C / 'HUMANIZED-SO-FAR.md'
if ONLY:
    art = ARTICLE.read_text(encoding='utf-8')
    a = art.index('# Practice Comes Before Property')
    b = art.index('<!-- CANDIDATE: the appendix', a)
    assert art[a:b].strip() == (S16 / 'v0.md').read_text(encoding='utf-8').strip(), 'the article holds a section 16 already'
    ARTICLE = S16 / 'page' / 'article-with-draft.md'
    ARTICLE.parent.mkdir(exist_ok=True)
    ARTICLE.write_text(art[:a] + md.strip() + '\n\n' + art[b:], encoding='utf-8')
else:
    assert md.strip() in ARTICLE.read_text(encoding='utf-8'), 'install the draft first (s16/install/install_s16.py)'
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
BATCHES = sorted(p for p in S16.glob('b[34]*') if (p / 'drafts.json').exists()) + [C / 'fix-20261017' / 'b410', C / 'fix-20261017' / 'b412',
           C / 'fix-20261017' / 'b413', C / 'fix-20261017b' / 'b415', C / 'fix-20261017b' / 'b417',
           C / 'fix-20261017b' / 'b418', C / 'fix-20261017b' / 'b419']
BATCHES = [b for b in BATCHES if (b / 'drafts.json').exists()]
CHECK = {p: g for p, g in page_checks.alone(md, BATCHES)}
BDIR = next(d / BATCH for d in (S16, C / 'fix-20261017', C / 'fix-20261017b') if (d / BATCH).exists())
whole = json.loads((BDIR / ('%s-results.json' % BATCH)).read_text(encoding='utf-8'))[KEY]
NOTE = {
 'H1-P1': 'Your quoted founders ("First let\'s get land!" ...) keep their exclamations: they\'re voices being imitated.',
 'H1-P2': ('Your order of 2026-10-16 23:38, every step of it: practice, a real conflict, values, membership, ownership and exit, '
           'then land. Your 43: "Less cinematic, I know." with a period (a wry concession; the joke is in the brackets).'),
 'H1-P3': ('Your 43: "in one go." with a period (advice). From the faithfulness pass: "rather than by declaring "money is impure!"", '
           'the published "declaring": the rewrite had mocked the belief itself, which section 4 gives as yours ("money is '
           'antagonistic to the spirit of community"). Your 13:11 "quietly" stays out. The first money stage isn\'t repeated here '
           '(section 4 says it in your words).'),
 'H2-P1': '"That\'s fine!" stays: with a period it read curt to a fresh reader, your "That\'s it!" shape.',
 'H2-P3': ('Your 43, your own example: "That\'s it!" is out (the phrase, not just the mark). Pangram read the paragraph Human '
           'with both neighbors (415g, 418g).'),
 'H2-P4': ('"It can still make a difference when people are going through ..." stays: the faithfulness pass put your published '
           '"change how people survive" in, and it read AI with the paragraph before it (415g 0.88, 417g 0.87) and brought AI '
           'windows into the section (question 47). "already contains a real piece of community" stays out: section 13 opens '
           'with it (the overnight dedup).'),
 'H2-P5': 'Your 43: "Or a sauna." with a period (deadpan; the sauna is the joke).',
 'H2-P6': '"Trust me on this one." vouches from your own experience where the published didn\'t (question 47 c).',
 'H3-P1': 'Your 43: "And practice before you have an audience." with a period (your published sentence had one).',
 'H3-P2': '"One disagreement is enough!" stays for now: it\'s the paragraph\'s only turn (question 47).',
 'H3-P4': '"Really, go!" stays for now: it\'s the paragraph\'s only turn (question 47).',
 'H3-P5': 'Your 42 lines, with your two exclamations.',
 'H3-P6': 'Your 42, as you wrote it: "Look before you leap. It will really save you some time & money."',
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
WHERE = 'a draft, not in the article yet' if ONLY else 'now in the article'
win = [w for w in whole[3].split('; ') if w.startswith('AI')]
out = {'title': 'Practice Comes Before Property · section 16 (%s, %s) beside the published one'
                % (DRAFT[:-3], 'a draft' if ONLY else 'in the article'),
       'meta': 'Community article · section 16 · %s, 2026-10-17 · %s' % (DRAFT[:-3], 'a draft: your published section is still in the '
               'article (question 42)' if ONLY else 'in the article, not accepted until you say so'),
       'intro': ['Your published section is on the left; %s, %s, is on the right. Each row shows the check that read '
                 'that paragraph alone, or with its neighbor when it is short (your rule: every paragraph passes alone).'
                 % (DRAFT[:-3], WHERE),
                 'The whole section reads %s (%s, %s words, AI likelihood %.2f%s): https://www.pangram.com/history%s'
                 % (whole[0].replace(' Written', ''), BATCH[1:] + 'g', whole[2], whole[1],
                    '; one AI window of %s words, from the showers sentence into the land line, question 42' % win[0].split(', ')[-1]
                    if win else '', whole[5]),
                 'What changed this evening: the exclamations your way (your 43: the mark becomes a period only where the '
                 'sentence reads right with one; real reactions and your own lines stay; "That\'s it!" is out), and one fix from '
                 'the whole-article faithfulness pass ("rather than by declaring", your published word). Pangram checked the '
                 'section one change at a time (418g, 419g). What it or the march showed was holding a paragraph is question 47.'],
       'blocks': blocks}
(S16 / 'page').mkdir(exist_ok=True)
mp = S16 / 'page' / ('ic16-%s.json' % DRAFT[:-3])
mp.write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'render_in_context.py'), str(mp),
                    str(C / 'community-section16-side-by-side.html'), '--article', str(ARTICLE),
                    '--source', str(C.parent / 'original.md'), '--against-source'], capture_output=True, text=True)
print(r.returncode, (r.stdout + r.stderr)[-800:])
