"""Section 13's side-by-side page for Joel: v35, in the article (accepted), beside the published section (2026-10-17
evening), each paragraph with the Pangram check that read its exact text alone (Joel's rule of 2026-10-01; batches 312g to 318g
and 420g) and, where his 19:14 decision on the exclamations changed it since v34, what changed (fix-20261017c/excl-changes-13.json).
Run from the repo root:
  python3 articles/intentional-communities/candidate/s13/make_page_v35.py
"""
import json, pathlib, re, subprocess, sys

REPO = pathlib.Path(__file__).resolve().parents[4]
C = REPO / 'articles' / 'intentional-communities' / 'candidate'
S13 = C / 's13'
sys.path.insert(0, str(C / 'tools'))
import page_checks  # noqa: E402

H = '# Your Little Forming Group Already Is the Community'
art = (C / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
v35 = (S13 / 'v35.md').read_text(encoding='utf-8').strip() + '\n'
assert v35.strip() in art, 'install v35 first (fix-20261017c/install_1914.py)'
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


P = paras(orig[oa:ob]); R = paras(v35)
MAP = [
    [([1], [1]), ([2, 3], [2]), ([4, 5], [3]), ([6], [4])],
    [([1, 2], [1]), ([3], [2]), ([4], [3]), ([5], [4]), ([6], [5])],
    [([1, 2], [1]), ([3], [2]), ([4, 5, 6], [3, 4]), ([7], [5])],
    [([1, 2], [1]), ([3], [2]), ([4], [3]), ([5], [4]), ([6, 7], [5]), ([8], [6, 7]), ([9], [8]), ([10], [9])],
    [([1], [1]), ([2], [2]), ([3], [3]), ([4], [4])],
]
checks = page_checks.alone(v35, [C / 'fix-20261017c' / 'b420', S13 / 'b318', S13 / 'b317', S13 / 'b316', S13 / 'b314', S13 / 'b312'])
CHECK = {p: g for p, g in checks}
v34p = [x.strip() for x in re.split(r'\n\s*\n', (S13 / 'v34.md').read_text(encoding='utf-8')) if x.strip()]
IDS = [['H1-P1', 'H1-P2', 'H1-P3', 'H1-P4'], ['H2-P1', 'H2-P2', 'H2-P3', 'H2-P3b', 'H2-P4'],
       ['H3-P1', 'H3-P2', 'H3-P3', 'H3-P4', 'H3-P5'], ['H4-P%d' % i for i in range(1, 10)], ['H5-P1', 'H5-P2', 'H5-P3', 'H5-P4']]
SUB = {'Opening': 0, 'Values': 1, 'Resources': 2, 'Visitor to Member': 3, 'When Somebody Has to Go': 4}
CH = json.loads((C / 'fix-20261017c' / 'excl-changes-13.json').read_text(encoding='utf-8'))
PLAIN = {}
for where, kind, old, new, why in CH:
    sub, n = where.rsplit(' P', 1)
    pid = IDS[SUB[sub]][int(n) - 1]
    if kind == 'cut':
        gone = old.replace(new, '').strip() if new in old else old
        what = 'out: "%s"' % gone
    else:
        what = '"%s" for "%s"' % (new.strip(), old.strip())
    if 'missed by the list' in why:
        what += ' (the list missed this one; the same treatment)'
    PLAIN.setdefault(pid, []).append(what)
r420 = json.loads((C / 'fix-20261017c' / 'b420' / 'b420-results.json').read_text(encoding='utf-8'))
whole = r420['S13v35']
WHOLE = 'https://www.pangram.com/history' + whole[5]
changed = [pid for hi, (_, rps) in enumerate(R) for j, pid in enumerate(IDS[hi]) if rps[j] not in v34p]
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
            if text not in v34p:
                notes += ['Changed this evening (your 48, the exclamations): ' + '; '.join(PLAIN[pid]) + '.']
            row = {'label': '', 'article': start(text), 'notes': notes}
            if j == 0:
                row['source'] = [start(pps[k - 1])[:60] for k in pp]
            rows.append(row)
    blocks.append({'headings': [h], 'rows': rows})
out = {'title': 'Your Little Forming Group Already Is the Community · section 13 (v35, in the article) beside the published one',
       'meta': 'Community article · section 13 · v35, 2026-10-17 evening · in the article, accepted',
       'intro': ['Your published section is on the left; v35, in the article, is on the right. Each row shows the check that read '
                 'that paragraph alone (your rule: every paragraph passes alone), and what your decision on the exclamations changed.',
                 'The whole section reads %s (420g, %s words, AI likelihood %.2f): %s' % (whole[0].replace(' Written', ''),
                                                                                                  whole[2], whole[1], WHOLE),
                 'What changed since v34: the exclamations list you agreed with at 19:14 ("i agree with your excl 13 14 ideas"), and two '
                 'more the list missed because each had an emoji after its mark ("Not exactly a high bar! 😅" and "(Hint: not the person '
                 'who recruited them! 😜)"), which got the same treatment, the emoji staying. Kept: "That\'s okay!", "(And who owns the '
                 'land!)", "Being open to everybody felt so spiritual!", "(Hopefully not all at once!)" and the quoted visitor\'s own. '
                 'Section 14 keeps all of its own, as the list said.'],
       'blocks': blocks}
mp = S13 / 'page' / 'ic13-v35.json'
mp.write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'render_in_context.py'), str(mp),
                    str(C / 'community-section13-side-by-side.html'), '--article', str(C / 'HUMANIZED-SO-FAR.md'),
                    '--source', str(C.parent / 'original.md'), '--against-source'], capture_output=True, text=True)
print(r.returncode, (r.stdout + r.stderr)[-800:])
