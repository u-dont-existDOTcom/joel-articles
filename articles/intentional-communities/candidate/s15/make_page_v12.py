"""Section 15's side-by-side page for Joel: v12, now in the article, beside the published section (2026-10-17), each paragraph
with the Pangram check that read its exact text alone (or with its neighbor when it is under 50 words), the whole section's
check (338g), and the notes he needs: question 40 (H1-P4) and the published words put back after the meaning checks.
Run from the repo root: python3 articles/intentional-communities/candidate/s15/make_page_v12.py"""
import json, pathlib, re, subprocess, sys

REPO = pathlib.Path(__file__).resolve().parents[4]
C = REPO / 'articles' / 'intentional-communities' / 'candidate'
S15 = C / 's15'
sys.path.insert(0, str(C / 'tools'))
import page_checks  # noqa: E402

v12 = (S15 / 'v12.md').read_text(encoding='utf-8')
assert v12.strip() in (C / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8'), 'install v12 first (s15/install/install_s15_v12.py)'
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


P, R = sections((S15 / 'v0.md').read_text(encoding='utf-8')), sections(v12)
assert [len(x[1]) for x in P] == [len(x[1]) for x in R] == [5, 7, 8], ([len(x[1]) for x in P], [len(x[1]) for x in R])
IDS = [['H1-P%d' % i for i in range(1, 6)], ['H2-P%d' % i for i in range(1, 8)], ['H3-P%d' % i for i in range(1, 9)]]
BATCHES = sorted(p for p in S15.glob('b3*') if (p / 'drafts.json').exists())
CHECK = {p: g for p, g in page_checks.alone(v12, BATCHES)}
r338 = json.loads((S15 / 'b338' / 'b338-results.json').read_text(encoding='utf-8'))['S15v12']
NOTE = {
 'H1-P4': ('Question 40 on the questions page. This is the only shape of eleven that reads Human alone; it says the family and the '
           'local memory take care of "so much", where you published that these things "often pass through" them, and a meaning '
           'check called that a shift. The ten shapes that keep "often" read AI alone, among them "things often go through" '
           '(330g, https://www.pangram.com/history/450082a7-13ba-4d19-8e9b-e00aedad18a2). The whole section reads Human with any '
           'of them.'),
 'H2-P1': 'Your "either" is back ("No, not that either!"): a meaning check found the rewrite had dropped it.',
 'H3-P2': ('Your "may" and your "any independence or long-term stability" are back: meaning checks found the rewrite had made the '
           'expectation certain and dropped "any" and "long-term".'),
}
start = lambda t: ' '.join(re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', t).split()[:6])
blocks = []
for hi, ((h, pps), (_, rps)) in enumerate(zip(P, R)):
    rows = []
    for j, text in enumerate(rps):
        pid = IDS[hi][j]
        g = CHECK.get(text) or []
        notes = [page_checks.note(g[0])] if g else ['no check of this text alone yet']
        if pid in NOTE:
            notes.append(NOTE[pid])
        rows.append({'label': '', 'article': start(text), 'source': [start(pps[j])[:60]], 'notes': notes})
    blocks.append({'headings': [h], 'rows': rows})
out = {'title': 'What This Looks Like From Sénégal · section 15 (v12, in the article) beside the published one',
       'meta': 'Community article · section 15 · v12, 2026-10-17 · in the article, not accepted until you say so',
       'intro': ['Your published section is on the left; v12, now in the article, is on the right. Each row shows the check that read '
                 'that paragraph alone (your rule: every paragraph passes alone).',
                 'The whole section reads %s (338g, %s words, AI likelihood %.2f): https://www.pangram.com/history%s'
                 % (r338[0].replace(' Written', ''), r338[2], r338[1], r338[5]),
                 'How it was made: Emulate rewrote the section (five rounds, the last ones on single paragraphs), and your meaning '
                 'went back inside its sentences; meaning checks then compared every paragraph with yours and caught where a '
                 'point had slipped, each fixed before the Pangram checks. Nothing was cut as a repeat: each place that says '
                 'something another section says carries its own point here.',
                 'One paragraph needs you: the extended family and the local memory (question 40).'],
       'blocks': blocks}
(S15 / 'page').mkdir(exist_ok=True)
mp = S15 / 'page' / 'ic15-v12.json'
mp.write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'render_in_context.py'), str(mp),
                    str(C / 'community-section15-side-by-side.html'), '--article', str(C / 'HUMANIZED-SO-FAR.md'),
                    '--source', str(C.parent / 'original.md'), '--against-source'], capture_output=True, text=True)
print(r.returncode, (r.stdout + r.stderr)[-800:])
