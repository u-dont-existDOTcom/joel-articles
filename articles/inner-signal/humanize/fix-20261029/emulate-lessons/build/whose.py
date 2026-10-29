"""whose.py 'sentence' ... : is the sentence in the published guide, in which Emulate outputs (exact, quotes flattened), else best fuzzy match."""
import sys, glob, pathlib, re, difflib
H = pathlib.Path(__file__).resolve().parents[3]  # build -> emulate-lessons -> fix-20261029 -> humanize
FLAT = str.maketrans({'“': '"', '”': '"', '‘': "'", '’': "'", '–': '-', '—': '-'})
def norm(s): return re.sub(r'\s+', ' ', s.translate(FLAT)).strip()
PUB = norm((H / 'source/published-20260928.md').read_text())
OUTS = {}
for f in glob.glob(str(H / 'fix-2026*/**/*.out.txt'), recursive=True):
    OUTS[f.replace(str(H) + '/', '')] = norm(pathlib.Path(f).read_text())
def whose(s):
    n = norm(s)
    res = []
    if n in PUB: res.append('PUBLISHED')
    for f, t in OUTS.items():
        if n in t: res.append(f)
    return res
if __name__ == '__main__':
    for s in sys.argv[1:]:
        r = whose(s)
        print(s[:80], '->', r if r else 'NOT FOUND (exact)')
