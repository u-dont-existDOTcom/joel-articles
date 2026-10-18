"""Section 15's side-by-side page for Joel: v17, now in the article, beside the published section (2026-10-17 night, after his 21:37
message), each paragraph with the Pangram check that read its exact text alone (or with its neighbor when it is under 50 words),
the whole section's check (423g), and the notes he needs: his rewrite of the two paragraphs under "All is not well in paradise"
(his 47.4), the two cuts of his 51 a, "So which is it? ..." (kept, 424g), and the earlier notes that still hold.
Run from the repo root: python3 articles/intentional-communities/candidate/s15/make_page_v17.py"""
import json, pathlib, re, subprocess, sys

REPO = pathlib.Path(__file__).resolve().parents[4]
C = REPO / 'articles' / 'intentional-communities' / 'candidate'
S15 = C / 's15'
D = C / 'fix-20261017d'
sys.path.insert(0, str(C / 'tools'))
import page_checks  # noqa: E402

v17 = (S15 / 'v17.md').read_text(encoding='utf-8')
art = (C / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
assert v17.strip() in art, 'install v17 first (fix-20261017d/install_423.py)'
# v18 (the cut of "So which is it? ...") was run as 424g and is not in the article: this page is v17's, and the note on that paragraph says why
assert not (S15 / 'v18.md').exists() or (S15 / 'v18.md').read_text(encoding='utf-8').strip() not in art, 'v18 is in the article: rebuild the page for v18'
SKIP = re.compile(r'^(\[image \d+\]|\[caption\]|\[Professor Baby Sheep|Double click to interact with video)')


def sections(md):
    """[(heading, [paragraphs])] in order"""
    out = []
    for b in [b.strip() for b in re.split(r'\n\s*\n', md) if b.strip()]:
        if b.startswith('#'):
            out.append((b, []))
        elif not SKIP.match(b):
            out[-1][1].append(b)
    return out


P, R = sections((S15 / 'v0.md').read_text(encoding='utf-8')), sections(v17)
assert [len(x[1]) for x in P] == [len(x[1]) for x in R] == [5, 7, 8], ([len(x[1]) for x in P], [len(x[1]) for x in R])
IDS = [['H1-P%d' % i for i in range(1, 6)], ['H2-P%d' % i for i in range(1, 8)], ['H3-P%d' % i for i in range(1, 9)]]
BATCHES = [D / 'b424', D / 'b423', D / 'b422', D / 'b421'] + sorted(p for p in S15.glob('b3*') if (p / 'drafts.json').exists()) + [
           C / 'fix-20261017' / 'b410', C / 'fix-20261017' / 'b412', C / 'fix-20261017b' / 'b415', C / 'fix-20261017b' / 'b417']
BATCHES = [b for b in BATCHES if (b / 'drafts.json').exists()]
CHECK = {p: g for p, g in page_checks.alone(v17, BATCHES)}
r423 = json.loads((D / 'b423' / 'b423-results.json').read_text(encoding='utf-8'))['S15v17']
r424 = json.loads((D / 'b424' / 'b424-results.json').read_text(encoding='utf-8'))
LINK = lambda k: 'https://www.pangram.com/history' + r424[k][5]
# the figures the "So which is it?" note quotes: the cut paragraph with the law paragraph before it, with the next one, and the cut section
assert r424['S15v18-p3+prev'][0].startswith('AI') and r424['S15v18-p3+prev'][1] == 0.95, r424['S15v18-p3+prev'][:2]
assert r424['S15v18-p3+next'][0].startswith('Human') and r424['S15v18'][0].startswith('Human'), (r424['S15v18-p3+next'][0], r424['S15v18'][0])
REWRITE = ('Your rewrite (your 47.4), as you wrote it: "No, not quite." with its period, "favort" spelled "favor", the law link kept '
           'after "March 2026". You were right that the "!" made it blunter, not softer.')
NOTE = {
 'H1-P2': ['Your 43: "I find them so soothing." with a period (a calm feeling; the published "I find them deeply soothing.").'],
 'H1-P3': ['"And the humor!" stays: a real reaction, and with a period it would read flat (your 43).'],
 'H1-P4': ['Your 40 a: "so much is taken care of by" stays.'],
 'H1-P5': ['Your 43: "Spiritual graffiti still surprises me." with a period, after the graffiti\'s five exclamations.'],
 'H2-P1': [REWRITE],
 'H2-P2': [REWRITE],
 'H2-P3': [('From the faithfulness pass: your published judgment back, "Being in community isn\'t automatically liberating. It all '
            'depends on who is allowed to belong without pretending.", for Emulate\'s "It\'s interesting to see that ... whether '
            'you\'re allowed" (a detached remark, and one person\'s luck where you named who the community lets belong).'),
           ('"So which is it? Well, in a way, it\'s both." stays, though your new first paragraph already answers it: cut, the '
            'paragraph read AI with your law paragraph before it (424g, 0.95 %s), though Human with the one after %s and the '
            'section 100%% Human; by your borderline rule (a paragraph that passes only beside a strong neighbor has to pass '
            'without it), it stays.' % (LINK('S15v18-p3+prev'), LINK('S15v18-p3+next')))],
 'H2-P5': ['"Every morning!" is yours (published).'],
 'H2-P6': ['Your 43: "Everybody here has sheep (even me), and they are super cute." Both marks out: two in one sentence, between '
           '"Every morning!" and the sheep video\'s title.'],
 'H3-P1': [('From the faithfulness pass: "whatever prosperity came through you later", your published phrase, for "whatever you '
            'made of yourself later", which is the self-made view the paragraph argues against ("nobody made it alone").')],
 'H3-P3': ['Your 13:11 correction stays: "This is also". Your 43: "someone has to handle it." with a period (logistics, not a reaction).'],
 'H3-P5': ['Your 13:11 sentence stays: "I understand the motivation to negotiate like that, but I think it\'s not a full solution either."'],
 'H3-P6': ['Your 51 a: the tag "isn\'t it?" out.'],
 'H3-P7': ['Your 43: "a spiritual service package." with a period (advice; the "!" made it scold).'],
 'H3-P8': ['"they won\'t let me pay rent!" stays: a real reaction to the hospitality.',
           'Your 51 a: "Can you believe it?" out; your "they won\'t let me pay rent!" carries the surprise.'],
}
# what changed since v14 (the page Joel last saw): his rewrite of the first two paragraphs under "All is not well in paradise"
# and the two 51 a cuts; each of these paragraphs has a note above
v14p = [x.strip() for x in re.split(r'\n\s*\n', (S15 / 'v14.md').read_text(encoding='utf-8')) if x.strip()]
changed = [IDS[hi][j] for hi, (_, rps) in enumerate(R) for j, t in enumerate(rps) if t not in v14p]
assert sorted(changed) == ['H2-P1', 'H2-P2', 'H3-P6', 'H3-P8'], changed
# each note belongs to the paragraph it talks about
for pid, words in (('H2-P1', 'No, not quite.'), ('H2-P2', 'in their favor'), ('H2-P3', "So which is it? Well, in a way, it's both."),
                   ('H3-P6', 'Kind of the opposite problem.'), ('H3-P8', "they won't let me pay rent!")):
    hi, n = int(pid[1]) - 1, int(pid.split('-P')[1])
    assert words in R[hi][1][n - 1], (pid, words)
start = lambda t: ' '.join(re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', t).split()[:6])
blocks = []
for hi, ((h, pps), (_, rps)) in enumerate(zip(P, R)):
    rows = []
    for j, text in enumerate(rps):
        pid = IDS[hi][j]
        g = CHECK.get(text) or []
        # a paragraph under 50 words passes with either neighbor (Joel's rule; paragraphs_alone.py): the row shows the newest check that
        # read Human, and any newer check that read otherwise is said too
        main = next((r for r in g if r[2].startswith('Human')), g[0] if g else None)
        notes = [page_checks.note(main)] if main else ['no check of this text alone yet']
        for r in g:
            if main and r[0] > main[0] and not r[2].startswith('Human'):
                notes.append('Also checked, and read AI: %s. It passes %s, which your rule allows for a paragraph under 50 words.'
                             % (page_checks.note(r), main[5] or 'alone'))
        notes += NOTE.get(pid, [])
        rows.append({'label': '', 'article': start(text), 'source': [start(pps[j])[:60]], 'notes': notes})
    blocks.append({'headings': [h], 'rows': rows})
out = {'title': 'What This Looks Like From Sénégal · section 15 (v17, in the article) beside the published one',
       'meta': 'Community article · section 15 · v17, 2026-10-17 night · in the article, not accepted until you say so',
       'intro': ['Your published section is on the left; v17, now in the article, is on the right. Each row shows the check that read '
                 'that paragraph alone (your rule: every paragraph passes alone).',
                 'The whole section reads %s (423g, %s words, AI likelihood %.2f): https://www.pangram.com/history%s'
                 % (r423[0].replace(' Written', ''), r423[2], r423[1], r423[5]),
                 'How it was made: Emulate rewrote the section (five rounds, the last ones on single paragraphs), and your meaning '
                 'went back inside its sentences; meaning checks then compared every paragraph with yours and caught where a '
                 'point had slipped, each fixed before the Pangram checks. Nothing was cut as a repeat: each place that says '
                 'something another section says carries its own point here.',
                 'What changed since v14: your rewrite of the first two paragraphs under "All is not well in paradise" (your 47.4), '
                 'as you wrote it, and two small cuts from your 51 a: the tag "isn\'t it?" after "Kind of the opposite problem." and '
                 '"Can you believe it?" in the paragraph on your residency. "So which is it? Well, in a way, it\'s both." stays '
                 '(its row says why). Each changed paragraph has its new check in its row.'],
       'blocks': blocks}
(S15 / 'page').mkdir(exist_ok=True)
mp = S15 / 'page' / 'ic15-v17.json'
mp.write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'render_in_context.py'), str(mp),
                    str(C / 'community-section15-side-by-side.html'), '--article', str(C / 'HUMANIZED-SO-FAR.md'),
                    '--source', str(C.parent / 'original.md'), '--against-source'], capture_output=True, text=True)
print(r.returncode, (r.stdout + r.stderr)[-800:])
