"""Section 15's side-by-side page for Joel: v14, now in the article, beside the published section (2026-10-17, after his 17:16
message), each paragraph with the Pangram check that read its exact text alone (or with its neighbor when it is under 50 words),
the whole section's check (415g), and the notes he needs: the exclamations his way (his 43), and the faithfulness pass's fixes.
Run from the repo root: python3 articles/intentional-communities/candidate/s15/make_page_v14.py"""
import json, pathlib, re, subprocess, sys

REPO = pathlib.Path(__file__).resolve().parents[4]
C = REPO / 'articles' / 'intentional-communities' / 'candidate'
S15 = C / 's15'
sys.path.insert(0, str(C / 'tools'))
import page_checks  # noqa: E402

v12 = (S15 / 'v14.md').read_text(encoding='utf-8')
assert v12.strip() in (C / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8'), 'install v14 first (fix-20261017b/install_1716.py)'
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
BATCHES = sorted(p for p in S15.glob('b3*') if (p / 'drafts.json').exists()) + [C / 'fix-20261017' / 'b410', C / 'fix-20261017' / 'b412',
           C / 'fix-20261017b' / 'b415']
CHECK = {p: g for p, g in page_checks.alone(v12, BATCHES)}
r338 = json.loads((C / 'fix-20261017b' / 'b415' / 'b415-results.json').read_text(encoding='utf-8'))['S15v14']
NOTE = {
 'H1-P2': 'Your 43: "I find them so soothing." with a period (a calm feeling; the published "I find them deeply soothing.").',
 'H1-P3': '"And the humor!" stays: a real reaction, and with a period it would read flat (your 43).',
 'H1-P4': 'Your 40 a: "so much is taken care of by" stays.',
 'H1-P5': 'Your 43: "Spiritual graffiti still surprises me." with a period, after the graffiti\'s five exclamations.',
 'H2-P1': ('Your 43: "No, not that either." with a period. It opens the passage on the anti-gay law, prison and mob violence, and '
           'the whole-article reader found the "!" softened the article\'s bluntness at its gravest point (published: "I don\'t want '
           'to turn this into Sénégal as a surviving communal paradise either.").'),
 'H2-P3': ('From the faithfulness pass: your published judgment back, "Being in community isn\'t automatically liberating. It all '
           'depends on who is allowed to belong without pretending.", for Emulate\'s "It\'s interesting to see that ... whether '
           'you\'re allowed" (a detached remark, and one person\'s luck where you named who the community lets belong).'),
 'H2-P5': '"Every morning!" is yours (published).',
 'H2-P6': 'Your 43: "Everybody here has sheep (even me), and they are super cute." Both marks out: two in one sentence, between "Every morning!" and the sheep video\'s title.',
 'H3-P1': ('From the faithfulness pass: "whatever prosperity came through you later", your published phrase, for "whatever you '
           'made of yourself later", which is the self-made view the paragraph argues against ("nobody made it alone").'),
 'H3-P3': 'Your 13:11 correction stays: "This is also". Your 43: "someone has to handle it." with a period (logistics, not a reaction).',
 'H3-P5': 'Your 13:11 sentence stays: "I understand the motivation to negotiate like that, but I think it\'s not a full solution either."',
 'H3-P7': 'Your 43: "a spiritual service package." with a period (advice; the "!" made it scold).',
 'H3-P8': '"they won\'t let me pay rent!" stays: a real reaction to the hospitality.',
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
out = {'title': 'What This Looks Like From Sénégal · section 15 (v14, in the article) beside the published one',
       'meta': 'Community article · section 15 · v14, 2026-10-17 evening · in the article, not accepted until you say so',
       'intro': ['Your published section is on the left; v14, now in the article, is on the right. Each row shows the check that read '
                 'that paragraph alone (your rule: every paragraph passes alone).',
                 'The whole section reads %s (415g, %s words, AI likelihood %.2f): https://www.pangram.com/history%s'
                 % (r338[0].replace(' Written', ''), r338[2], r338[1], r338[5]),
                 'How it was made: Emulate rewrote the section (five rounds, the last ones on single paragraphs), and your meaning '
                 'went back inside its sentences; meaning checks then compared every paragraph with yours and caught where a '
                 'point had slipped, each fixed before the Pangram checks. Nothing was cut as a repeat: each place that says '
                 'something another section says carries its own point here.',
                 'What changed this evening: the exclamations your way (your 43: the mark becomes a period only where the sentence '
                 'reads right with one; the real reactions stay), and two fixes from the whole-article faithfulness pass (your '
                 'published words back). Each changed paragraph has its new check in its row.'],
       'blocks': blocks}
(S15 / 'page').mkdir(exist_ok=True)
mp = S15 / 'page' / 'ic15-v14.json'
mp.write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'render_in_context.py'), str(mp),
                    str(C / 'community-section15-side-by-side.html'), '--article', str(C / 'HUMANIZED-SO-FAR.md'),
                    '--source', str(C.parent / 'original.md'), '--against-source'], capture_output=True, text=True)
print(r.returncode, (r.stdout + r.stderr)[-800:])
