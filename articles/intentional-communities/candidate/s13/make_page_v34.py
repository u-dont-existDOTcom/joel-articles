"""Section 13's side-by-side page for Joel: v34, now in the article, beside the published section (2026-10-17), each
paragraph with the Pangram check that read its exact text alone (Joel's rule of 2026-10-01; batches 312g to 317g) and, where
this turn changed it since v31, what changed and why (v32-fixes.json, v33-fixes.json, v34-fixes.json). Run from the repo root:
  python3 articles/intentional-communities/candidate/s13/make_page_v34.py
"""
import json, pathlib, re, subprocess, sys

REPO = pathlib.Path(__file__).resolve().parents[4]
C = REPO / 'articles' / 'intentional-communities' / 'candidate'
S13 = C / 's13'
sys.path.insert(0, str(C / 'tools'))
import page_checks  # noqa: E402

H = '# Your Little Forming Group Already Is the Community'
art = (C / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
v34 = (S13 / 'v34.md').read_text(encoding='utf-8').strip() + '\n'
assert v34.strip() in art, 'install v34 first (s13/install/install_s13_v34.py)'
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


P = paras(orig[oa:ob]); R = paras(v34)
MAP = [
    [([1], [1]), ([2, 3], [2]), ([4, 5], [3]), ([6], [4])],
    [([1, 2], [1]), ([3], [2]), ([4], [3]), ([5], [4]), ([6], [5])],
    [([1, 2], [1]), ([3], [2]), ([4, 5, 6], [3, 4]), ([7], [5])],
    [([1, 2], [1]), ([3], [2]), ([4], [3]), ([5], [4]), ([6, 7], [5]), ([8], [6, 7]), ([9], [8]), ([10], [9])],
    [([1], [1]), ([2], [2]), ([3], [3]), ([4], [4])],
]
checks = page_checks.alone(v34, [S13 / 'b317', S13 / 'b316', S13 / 'b314', S13 / 'b312'])
CHECK = {p: g for p, g in checks}
fixes = [f for v in ('v32', 'v33', 'v34') for f in json.loads((S13 / (v + '-fixes.json')).read_text(encoding='utf-8'))]
v31 = [x.strip() for x in re.split(r'\n\s*\n', (S13 / 'v31.md').read_text(encoding='utf-8')) if x.strip()]
WHY = {}
for f in fixes:
    WHY.setdefault(f['id'], []).append(f['why'])
# what changed since v31, in plain words for Joel's page (the fixes files hold the working reasons)
EMU = ('From Emulate now, with your points put back inside its sentences. In 316g the whole section read AI over this paragraph '
       'and its neighbours, though each read Human alone: your "borderline" point.')
PLAIN = {
    'H1-P3': '"a land surveyor" says what the surveyor is for (two readers stopped at "a surveyor"). Cut: "find out how much '
             'conflict the group can handle"; the paragraph before says it ("until you\'ve been through at least one real '
             'conflict together").',
    'H1-P4': 'Your "if the community uses them" is back. Cut: the failing well; section 12 says it ("The water well doesn\'t care '
             'how beautiful the new member\'s heart is.").',
    'H2-P2': EMU,
    'H2-P3': EMU + ' "if" a child comes out, as you published; a meaning check caught "when".',
    'H2-P3b': EMU,
    'H2-P4': EMU + ' Meaning checks put three of your points back: "don\'t just listen to what the group says" keeps your "not '
                   'only its public language" (for "look past"), "Does that match your values?" keeps your "compare your values" '
                   '(for "Is that how you want to live?"), and the conversation is "uncomfortable", not "a little uncomfortable".',
    'H3-P3': 'Cut: the scarcity without money; section 4 says it ("Even in a moneyless community, someone can control what\'s '
             'scarce."). The bottlenecks stay. The exit resources moved to the next paragraph.',
    'H3-P4': 'The exit resources are here now, after "That\'s coercive", so the right that\'s only on paper and the coercion are '
             'said once, side by side, as you published. Plainer: "lose everything they\'ve put in", "it only works when the '
             'community happens to have spare money" (readers stopped at both), "once anybody\'s furious" (your "before anybody '
             'is furious"). "while leaving is still only theoretical": a meaning check found "when it\'s only theoretical" could '
             'read as "hollow" right after "only on paper".',
    'H3-P5': 'The book is recommended for the nuts and bolts, not for its order, as you asked.',
    'H4-P1': 'Cut: "It\'s no good for anyone to join a group that can\'t deliver what it promised."; sections 5 and 12 say it.',
    'H4-P3': 'A new punchline: "congratulations! You\'ve established that they can be charming for two weeks" read AI alone '
             '(312g), so the point stays in other words.',
    'H4-P4': 'Cut: "time gets you more evidence, not certainty"; two paragraphs later, "there\'s still no "good person" detector" '
             'says it.',
    'H4-P6': 'Plainer: "think someone\'s safe just because they\'re going along with everyone else" and "Six months with someone" '
             '(readers stopped at both).',
    'H4-P8': '"sells their house to move in" (readers stopped at "sells a house"). Cut: "It won\'t show you anyone\'s soul"; the '
             '"good person" detector says it. "It can show you", not "It\'ll show you": a meaning check found your "can reveal" '
             'turned into a guarantee.',
    'H5-P4': '"ombudsperson", the plainer word (six readers stopped at "ombud").',
}
IDS = [['H1-P1', 'H1-P2', 'H1-P3', 'H1-P4'], ['H2-P1', 'H2-P2', 'H2-P3', 'H2-P3b', 'H2-P4'],
       ['H3-P1', 'H3-P2', 'H3-P3', 'H3-P4', 'H3-P5'], ['H4-P%d' % i for i in range(1, 10)], ['H5-P1', 'H5-P2', 'H5-P3', 'H5-P4']]
r317 = json.loads((S13 / 'b317' / 'b317-results.json').read_text(encoding='utf-8'))
whole = r317['S13v34']
WHOLE = 'https://www.pangram.com/history' + whole[5]
changed = [pid for hi, (_, rps) in enumerate(R) for j, pid in enumerate(IDS[hi]) if rps[j] not in v31]
assert set(changed) == set(PLAIN), (sorted(set(changed) - set(PLAIN)), sorted(set(PLAIN) - set(changed)))
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
            if text not in v31:
                notes += ['Changed this turn: ' + PLAIN[pid]]
            row = {'label': '', 'article': start(text), 'notes': notes}
            if j == 0:
                row['source'] = [start(pps[k - 1])[:60] for k in pp]
            rows.append(row)
    blocks.append({'headings': [h], 'rows': rows})
out = {'title': 'Your Little Forming Group Already Is the Community · section 13 (v34, in the article) beside the published one',
       'meta': 'Community article · section 13 · v34, 2026-10-17 · in the article, not accepted until you say so',
       'intro': ['Your published section is on the left; v34, now in the article, is on the right. Each row shows the check that read '
                 'that paragraph alone (your rule: every paragraph passes alone), and what changed this turn.',
                 'The whole section reads %s (317g, %s words, AI likelihood %.2f): %s' % (whole[0].replace(' Written', ''),
                                                                                                  whole[2], whole[1], WHOLE),
                 'What changed since your 23:38 message: your "if the community uses them" is back in the budget questions (with your '
                 'words the section read Human; my own rewording had been the trouble); the short visit lost its "congratulations" '
                 'punchline, the one paragraph that read AI alone; the book is recommended for the nuts and bolts, not for its order; '
                 'the repeats are cut where another place says the point better; and seven phrases readers kept stopping at are plainer.',
                 'And your point that it was all borderline: with all that in, the whole section read AI over the values paragraphs '
                 'after the opening story (316g, https://www.pangram.com/history/2be7c617-a4ed-4ea2-a9f5-14b303c84775), though each '
                 'read Human alone and the subsection read Human with its story. So those four paragraphs are Emulate\'s now, with '
                 'your points put back inside its sentences, and the meaning checks asked for five small fixes on the way.'],
       'blocks': blocks}
mp = S13 / 'page' / 'ic13-v34.json'
mp.write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'render_in_context.py'), str(mp),
                    str(C / 'community-section13-side-by-side.html'), '--article', str(C / 'HUMANIZED-SO-FAR.md'),
                    '--source', str(C.parent / 'original.md'), '--against-source'], capture_output=True, text=True)
print(r.returncode, (r.stdout + r.stderr)[-800:])
