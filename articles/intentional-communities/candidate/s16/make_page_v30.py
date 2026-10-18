"""Section 16's side-by-side page for Joel (v30 and later; v29 and the earlier ones: s16/make_page_v29.py, s16/make_page.py): the
draft now in the article beside the published section (2026-10-17 night, after his 21:37 message), each paragraph with the
Pangram check that read its exact text alone (or with its neighbor when it is under 50 words), the whole section's check, and
the notes he needs (what the dedup cut and where it is said, the published words the meaning checks put back, his answers 47.1
to 47.3 and 51 a).
Run from the repo root: python3 articles/intentional-communities/candidate/s16/make_page_v30.py v30.md b421 S16v30"""
import json, pathlib, re, subprocess, sys

REPO = pathlib.Path(__file__).resolve().parents[4]
C = REPO / 'articles' / 'intentional-communities' / 'candidate'
S16 = C / 's16'
sys.path.insert(0, str(C / 'tools'))
import page_checks  # noqa: E402

DRAFT, BATCH, KEY = sys.argv[1], sys.argv[2], sys.argv[3]
md = (S16 / DRAFT).read_text(encoding='utf-8')
ARTICLE = C / 'HUMANIZED-SO-FAR.md'
assert md.strip() in ARTICLE.read_text(encoding='utf-8'), 'install the draft first (fix-20261017d/install_2137.py)'
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
# The notes are keyed by a paragraph's place in the draft, counting its paragraphs under the heading without the images and
# captions (H3-P1 is the "So what do you actually do this month?" paragraph). v29's script numbered the third heading's rows
# from 2, the published numbering, so its H3 notes (47, 42 and 43) sat one row too low on that page.
IDS = [['H1-P%d' % i for i in range(1, 4)], ['H2-P%d' % i for i in range(1, 7)], ['H3-P%d' % i for i in range(1, 11)]]
PUB = [P[0][1], P[1][1], P[2][1][1:]]          # the published H3-P1, the lead-in line, went in the dedup
BATCHES = sorted(p for p in S16.glob('b[34]*') if (p / 'drafts.json').exists()) + [C / 'fix-20261017' / 'b410', C / 'fix-20261017' / 'b412',
           C / 'fix-20261017' / 'b413', C / 'fix-20261017b' / 'b415', C / 'fix-20261017b' / 'b417',
           C / 'fix-20261017b' / 'b418', C / 'fix-20261017b' / 'b419', C / 'fix-20261017d' / 'b421', C / 'fix-20261017d' / 'b422']
BATCHES = [b for b in BATCHES if (b / 'drafts.json').exists()]
CHECK = {p: g for p, g in page_checks.alone(md, BATCHES)}
BDIR = next(d / BATCH for d in (S16, C / 'fix-20261017', C / 'fix-20261017b', C / 'fix-20261017d') if (d / BATCH).exists())
whole = json.loads((BDIR / ('%s-results.json' % BATCH)).read_text(encoding='utf-8'))[KEY]
win = [w for w in whole[3].split('; ') if w.startswith('AI')]
assert not win, ('the whole section has an AI window now; the intro must say so', win)
NOTE = {
 'H1-P1': 'Your quoted founders ("First let\'s get land!" ...) keep their exclamations: they\'re voices being imitated.',
 'H1-P2': ('Your order of 2026-10-16 23:38, every step of it: practice, a real conflict, values, membership, ownership and exit, '
           'then land. Your 43: "Less cinematic, I know." with a period (a wry concession; the joke is in the brackets).'),
 'H1-P3': ('Your 43: "in one go." with a period (advice). From the faithfulness pass: "rather than by declaring "money is impure!"", '
           'the published "declaring": the rewrite had mocked the belief itself, which section 4 gives as yours ("money is '
           'antagonistic to the spirit of community"). Your 13:11 "quietly" stays out. The first money stage isn\'t repeated here '
           '(section 4 says it in your words). Your 51 a: "CAN" stays: with "can", Pangram read a window further on AI (422g).'),
 'H2-P1': '"That\'s fine!" stays: with a period it read curt to a fresh reader, your "That\'s it!" shape.',
 'H2-P2': 'Your 51 a: "PLUS goats" stays.',
 'H2-P3': ('Your 43, your own example: "That\'s it!" is out (the phrase, not just the mark). Pangram read the paragraph Human '
           'with both neighbors (415g, 418g).'),
 'H2-P4': ('Stays as it passed (your 47.3: "use the version that passed"). "already contains a real piece of community" stays '
           'out: section 13 opens with it.'),
 'H2-P5': 'Your 43: "Or a sauna." with a period (deadpan; the sauna is the joke).',
 'H2-P6': '"Trust me on this one." stays (you said it\'s fine).',
 'H3-P1': 'Your 43: "And practice before you have an audience." with a period (your published sentence had one).',
 'H3-P2': ('Your 47.1: "One disagreement is enough!" is out ("saying "one is enough" actually undermines the prior sentence '
           '"at least one"").'),
 'H3-P4': '"Really, go!" stays (your 47.2: "fine").',
 'H3-P5': 'Your 42 lines, with your two exclamations.',
 'H3-P6': 'Your 42, as you wrote it: "Look before you leap. It will really save you some time & money."',
}
# each note belongs to the paragraph it talks about: check the quoted words against the draft's paragraph
for pid, words in (('H1-P3', '"CAN"'), ('H2-P2', 'PLUS goats'), ('H2-P4', 'So what?'), ('H2-P6', 'Trust me on this one.'),
                   ('H3-P1', 'And practice before you have an audience.'), ('H3-P4', 'Really, go!'),
                   ('H3-P5', 'No manifesto is going to tell you any of that!'), ('H3-P6', 'Look before you leap.')):
    hi, n = int(pid[1]) - 1, int(pid.split('-P')[1])
    assert words.strip('"') in R[hi][1][n - 1], (pid, words)
assert 'One disagreement is enough!' not in md and 'Get through at least one disagreement too' in R[2][1][1]
start = lambda t: ' '.join(re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', t).split()[:6])
blocks = []
for hi, ((h, _), (_, rps)) in enumerate(zip(P, R)):
    rows = []
    for j, text in enumerate(rps):
        pid = IDS[hi][j]
        g = CHECK.get(text) or []
        # A paragraph under 50 words passes with either neighbor (Joel's rule; paragraphs_alone.py): the row shows the newest check
        # that read Human, and any newer check that read otherwise is said too, not hidden.
        main = next((r for r in g if r[2].startswith('Human')), g[0] if g else None)
        notes = [page_checks.note(main)] if main else ['no check of this text alone yet']
        for r in g:
            if main and r[0] > main[0] and not r[2].startswith('Human'):
                notes.append('Also checked, and read AI: %s. It passes %s, which your rule allows for a paragraph under 50 words.'
                             % (page_checks.note(r), main[5] or 'alone'))
        if pid in NOTE:
            notes.append(NOTE[pid])
        rows.append({'label': '', 'article': start(text), 'source': [start(PUB[hi][j])[:60]], 'notes': notes})
    blocks.append({'headings': [h], 'rows': rows})
out = {'title': 'Practice Comes Before Property · section 16 (%s, in the article) beside the published one' % DRAFT[:-3],
       'meta': 'Community article · section 16 · %s, 2026-10-17 night · in the article, not accepted until you say so' % DRAFT[:-3],
       'intro': ['Your published section is on the left; %s, now in the article, is on the right. Each row shows the check that read '
                 'that paragraph alone, or with its neighbor when it is short (your rule: every paragraph passes alone).'
                 % DRAFT[:-3],
                 'The whole section reads %s (%s, %s words, AI likelihood %.2f): https://www.pangram.com/history%s'
                 % (whole[0].replace(' Written', ''), BATCH[1:] + 'g', whole[2], whole[1], whole[5]),
                 'What changed tonight: your 47.1, "One disagreement is enough!" out. "Really, go!" and the "So what?" paragraph stay '
                 'as you said, and so does "CAN" (your 51 a), because with "can" the section read AI.'],
       'blocks': blocks}
(S16 / 'page').mkdir(exist_ok=True)
mp = S16 / 'page' / ('ic16-%s.json' % DRAFT[:-3])
mp.write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'render_in_context.py'), str(mp),
                    str(C / 'community-section16-side-by-side.html'), '--article', str(ARTICLE),
                    '--source', str(C.parent / 'original.md'), '--against-source'], capture_output=True, text=True)
print(r.returncode, (r.stdout + r.stderr)[-800:])
