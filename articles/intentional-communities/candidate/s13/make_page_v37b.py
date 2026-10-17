"""Section 13's side-by-side page for Joel: v37b, in the article (accepted), beside the published section (2026-10-17
night), each paragraph with the Pangram check that read its exact text alone (Joel's rule of 2026-10-01; batches 312g to 318g,
420g, 422g and 423g) and, where his 21:37 answers (48 a and 51 a) changed it since v35, what changed (the tightening pass in
fix-20261017d, then batch 423g).
Run from the repo root:
  python3 articles/intentional-communities/candidate/s13/make_page_v37b.py
"""
import json, pathlib, re, subprocess, sys

REPO = pathlib.Path(__file__).resolve().parents[4]
C = REPO / 'articles' / 'intentional-communities' / 'candidate'
S13 = C / 's13'
D = C / 'fix-20261017d'
sys.path.insert(0, str(C / 'tools'))
import page_checks  # noqa: E402

H = '# Your Little Forming Group Already Is the Community'
art = (C / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
v37b = (S13 / 'v37b.md').read_text(encoding='utf-8').strip() + '\n'
assert v37b.strip() in art, 'v37b is not in the article (fix-20261017d/install_423.py)'
orig = (C.parent / 'original.md').read_text(encoding='utf-8')
oa = orig.index(H); ob = orig.index('\n# ', oa + 5)


def paras(md):
    out = []
    for x in [p.strip() for p in re.split(r'\n\s*\n', md) if p.strip()]:
        if x.startswith('#'):
            out.append((x, []))
        else:
            out[-1][1].append(x)
    return out


P = paras(orig[oa:ob]); R = paras(v37b)
MAP = [
    [([1], [1]), ([2, 3], [2]), ([4, 5], [3]), ([6], [4])],
    [([1, 2], [1]), ([3], [2]), ([4], [3]), ([5], [4]), ([6], [5])],
    [([1, 2], [1]), ([3], [2]), ([4, 5, 6], [3, 4]), ([7], [5])],
    [([1, 2], [1]), ([3], [2]), ([4], [3]), ([5], [4]), ([6, 7], [5]), ([8], [6, 7]), ([9], [8]), ([10], [9])],
    [([1], [1]), ([2], [2]), ([3], [3]), ([4], [4])],
]
IDS = [['H1-P1', 'H1-P2', 'H1-P3', 'H1-P4'], ['H2-P1', 'H2-P2', 'H2-P3', 'H2-P3b', 'H2-P4'],
       ['H3-P1', 'H3-P2', 'H3-P3', 'H3-P4', 'H3-P5'], ['H4-P%d' % i for i in range(1, 10)], ['H5-P1', 'H5-P2', 'H5-P3', 'H5-P4']]
# the paragraph MAP and IDS are v35's: the counts must still fit (the article's v37b has v35's 4, 5, 5, 9 and 4 paragraphs)
assert [len(r) for _, r in R] == [len(i) for i in IDS] == [4, 5, 5, 9, 4], ([len(r) for _, r in R], [len(i) for i in IDS])
assert len(P) == len(R) == len(MAP) == 5, (len(P), len(R), len(MAP))
for (_, pps), (_, rps), m in zip(P, R, MAP):
    assert sorted(x for _, rr in m for x in rr) == list(range(1, len(rps) + 1)), 'MAP does not cover the rows of v37b'
    assert max(k for pp, _ in m for k in pp) <= len(pps), 'MAP names a published paragraph that is not there'
checks = page_checks.alone(v37b, [D / 'b423', D / 'b422', C / 'fix-20261017c' / 'b420', S13 / 'b318', S13 / 'b317', S13 / 'b316',
                                  S13 / 'b314', S13 / 'b312'])
CHECK = {p: g for p, g in checks}
v35p = [x.strip() for x in re.split(r'\n\s*\n', (S13 / 'v35.md').read_text(encoding='utf-8')) if x.strip()]
# What changed since v35, by paragraph (Joel's 21:37 answers 48 a and 51 a; the tightening pass and Emulate's lines, batches 422g and 423g)
NOTE = {
 'H1-P2': ('Your 48 a (the tightening): one "dealt with it" fewer and no capitals ("and really dealt with it. Not by writing out ...", '
           '"Dealing with it for real includes ..."). "Until then, what\'s it worth?" stays: with it and the cheesy line above out as '
           'well, Pangram read three windows of the section AI (423g).'),
 'H3-P3': ('"visibility" in lower case, and your published anchor back: "A money-free community still has scarce things and '
           'bottlenecks, sorry." (a cold reader had asked "Bottlenecks in what?").'),
 'H3-P5': '"Honestly?" out before the book line (padding).',
 'H4-P5': 'The provisional-membership questions folded together (your 48 a), the last one in a fresh reader\'s wording.',
 'H4-P9': '"Why wouldn\'t they be?" out (padding: the sentence before already answers it).',
 'H5-P1': '"Yeah, it\'s tough. It\'s also true." out (padding).',
 'H5-P3': ('The repeat of your section 9 out: "But when power had crept up in their own system over the years, it took them a long '
           'review to push it back down." (section 9 says it: "it had crept up and consolidated itself at higher levels over time").'),
}
STAYS = 'Stays, as you said ("leave those in actually, they are ok").'
STAY_WORDS = ('Very important!', 'Lots of decisions to make!')
r423 = json.loads((D / 'b423' / 'b423-results.json').read_text(encoding='utf-8'))
whole = r423['S13v37b']
LINK = lambda k: 'https://www.pangram.com/history' + r423[k][5]
WHOLE = LINK('S13v37b')
changed = [pid for hi, (_, rps) in enumerate(R) for j, pid in enumerate(IDS[hi]) if rps[j] not in v35p]
assert set(changed) == set(NOTE), (sorted(set(changed) - set(NOTE)), sorted(set(NOTE) - set(changed)))
stays = [pid for hi, (_, rps) in enumerate(R) for j, pid in enumerate(IDS[hi]) if rps[j] in v35p and any(w in rps[j] for w in STAY_WORDS)]
assert all(any(w in rps[j] for hi, (_, rps) in enumerate(R) for j in range(len(rps))) for w in STAY_WORDS) and len(stays) == 2, stays
start = lambda t: ' '.join(re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', t).split()[:6])
blocks = []
for hi, ((h, pps), (_, rps), m) in enumerate(zip(P, R, MAP)):
    rows = []
    for pp, rr in m:
        for j, r in enumerate(rr):
            text = rps[r - 1]
            pid = IDS[hi][r - 1]
            g = CHECK.get(text) or []
            notes = [page_checks.note(g[0])] if g else ['no check of this text alone yet']
            if pid in NOTE:
                notes.append(NOTE[pid])
            if pid in stays:
                notes.append(STAYS)
            row = {'label': '', 'article': start(text), 'notes': notes}
            if j == 0:
                row['source'] = [start(pps[k - 1])[:60] for k in pp]
            rows.append(row)
    blocks.append({'headings': [h], 'rows': rows})
out = {'title': 'Your Little Forming Group Already Is the Community · section 13 (v37b, in the article) beside the published one',
       'meta': 'Community article · section 13 · v37b, 2026-10-17 night · in the article, accepted',
       'intro': ['Your published section is on the left; v37b, in the article, is on the right. Each row shows the check that read '
                 'that paragraph alone (your rule: every paragraph passes alone), and what changed since v35.',
                 'The whole section reads %s (423g, %s words, AI likelihood %.2f): %s' % (whole[0].replace(' Written', ''),
                                                                                                  whole[2], whole[1], WHOLE),
                 'What changed since v35: your 48 a and 51 a, the tightening pass and Emulate\'s question-answer lines and capitals. '
                 'Each change was checked alone and in the section. Your "Very important!" and "Lots of decisions to make!" stay. '
                 '"It may sound cheesy, but it\'s true all the same." and "Until then, what\'s it worth?" stay too: with those two '
                 'out as well, the section read AI windows (423g, S13v37 %s and S13v37a %s).' % (LINK('S13v37'), LINK('S13v37a'))],
       'blocks': blocks}
mp = S13 / 'page' / 'ic13-v37b.json'
mp.write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'render_in_context.py'), str(mp),
                    str(C / 'community-section13-side-by-side.html'), '--article', str(C / 'HUMANIZED-SO-FAR.md'),
                    '--source', str(C.parent / 'original.md'), '--against-source'], capture_output=True, text=True)
print(r.returncode, (r.stdout + r.stderr)[-800:])
