"""Section 15's side-by-side page for Joel: v13, now in the article, beside the published section (2026-10-17, after his 13:11
message), each paragraph with the Pangram check that read its exact text alone (or with its neighbor when it is under 50 words),
the whole section's check (412g), and the notes he needs: his three corrections, the sweep's "This", his 40 a.
Run from the repo root: python3 articles/intentional-communities/candidate/s15/make_page_v13.py"""
import json, pathlib, re, subprocess, sys

REPO = pathlib.Path(__file__).resolve().parents[4]
C = REPO / 'articles' / 'intentional-communities' / 'candidate'
S15 = C / 's15'
sys.path.insert(0, str(C / 'tools'))
import page_checks  # noqa: E402

v12 = (S15 / 'v13.md').read_text(encoding='utf-8')
assert v12.strip() in (C / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8'), 'install v13 first (fix-20261017/install_20261017.py)'
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
BATCHES = sorted(p for p in S15.glob('b3*') if (p / 'drafts.json').exists()) + [C / 'fix-20261017' / 'b410', C / 'fix-20261017' / 'b412']
CHECK = {p: g for p, g in page_checks.alone(v12, BATCHES)}
r338 = json.loads((C / 'fix-20261017' / 'b412' / 'b412-results.json').read_text(encoding='utf-8'))['S15v13']
NOTE = {
 'H1-P3': ('"This is the most joking culture" again, your published "This": the sweep of your 13:11 rule ("this" is not the same as '
           '"it") found "It\'s the most joking culture" here.'),
 'H1-P4': ('Your 40 a: "so much is taken care of by" stays. The ten shapes that keep "often" read AI alone; the probe for your '
           'question is on the questions page.'),
 'H2-P1': 'Your "either" is back ("No, not that either!"): a meaning check found the rewrite had dropped it.',
 'H2-P2': ('Your 13:11 correction: "public advocacy for homosexuality", without quotes (the law\'s French "apologie" is advocacy, '
           'not "apology"), and the financing clause you called redundant is out.'),
 'H3-P2': ('Your "may" and your "any independence or long-term stability" are back: meaning checks found the rewrite had made the '
           'expectation certain and dropped "any" and "long-term".'),
 'H3-P3': 'Your 13:11 correction: "This is also", your published "This", for my "It\'s also".',
 'H3-P5': ('Your 13:11 sentence, "I understand the motivation to negotiate like that, but I think it\'s not a full solution '
           'either.", in place of the "I like that." I had added (with capital I\'s and a comma before "but").'),
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
out = {'title': 'What This Looks Like From Sénégal · section 15 (v13, in the article) beside the published one',
       'meta': 'Community article · section 15 · v13, 2026-10-17 · in the article, not accepted until you say so',
       'intro': ['Your published section is on the left; v13, now in the article, is on the right. Each row shows the check that read '
                 'that paragraph alone (your rule: every paragraph passes alone).',
                 'The whole section reads %s (412g, %s words, AI likelihood %.2f): https://www.pangram.com/history%s'
                 % (r338[0].replace(' Written', ''), r338[2], r338[1], r338[5]),
                 'How it was made: Emulate rewrote the section (five rounds, the last ones on single paragraphs), and your meaning '
                 'went back inside its sentences; meaning checks then compared every paragraph with yours and caught where a '
                 'point had slipped, each fixed before the Pangram checks. Nothing was cut as a repeat: each place that says '
                 'something another section says carries its own point here.',
                 'What changed today: your three corrections of 13:11 ("advocacy", "This is also", and your sentence for the '
                 '"I like that." I had added), and "This is the most joking culture" from the sweep of your "this" rule.'],
       'blocks': blocks}
(S15 / 'page').mkdir(exist_ok=True)
mp = S15 / 'page' / 'ic15-v13.json'
mp.write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'render_in_context.py'), str(mp),
                    str(C / 'community-section15-side-by-side.html'), '--article', str(C / 'HUMANIZED-SO-FAR.md'),
                    '--source', str(C.parent / 'original.md'), '--against-source'], capture_output=True, text=True)
print(r.returncode, (r.stdout + r.stderr)[-800:])
