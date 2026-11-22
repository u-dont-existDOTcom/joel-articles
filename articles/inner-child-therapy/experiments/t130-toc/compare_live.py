"""Compare the repository's article (round 11, as published 2026-11-04) with the live post, block by block.
Usage: python3 compare_live.py ARTICLE.md sections.json > LIVE-VS-ARTICLE.json"""
import json, re, sys, difflib

def norm(t):
    t = t.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"').replace(' ', ' ')
    t = re.sub(r'\s*--\s*|\s+[–—]\s+|[–—]', ' -- ', t)
    t = re.sub(r'\s+', ' ', t).strip()
    return t

def md_blocks(path):
    raw = open(path, encoding='utf-8').read()
    raw = re.sub(r'<!--.*?-->', '', raw, flags=re.S)
    out = []
    for b in re.split(r'\n\s*\n', raw):
        b = b.strip()
        if not b: continue
        m = re.match(r'^(#{1,6})\s+(.*)$', b, re.S)
        if m:
            kind, text = 'h%d' % len(m.group(1)), m.group(2)
        else:
            kind, text = 'p', b
        text = re.sub(r'!\[[^\]]*\]\([^)]*\)', '', text)
        text = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', text)
        text = re.sub(r'(\*\*|__|\*|_)(?=\S)(.+?)(?<=\S)\1', r'\2', text)
        text = re.sub(r'^\s*[-*]\s+', '', text, flags=re.M)
        text = re.sub(r'^\s*>\s?', '', text, flags=re.M)
        text = text.replace('\\', '')
        out.append((kind, norm(text)))
    return out

def live_blocks(path):
    S = json.load(open(path))
    out = []
    for s in S:
        if s['level']:
            out.append(('h%d' % s['level'], norm(s['heading'])))
        for b in s['blocks']:
            if b['kind'] in ('p', 'ul', 'ol', 'blockquote', 'pullquote') and b['text']:
                out.append(('p', norm(b['text'])))
    return out

A = md_blocks(sys.argv[1]); L = live_blocks(sys.argv[2])
sm = difflib.SequenceMatcher(a=[x[1] for x in A], b=[x[1] for x in L], autojunk=False)
ops = []
for tag, i1, i2, j1, j2 in sm.get_opcodes():
    if tag == 'equal': continue
    ops.append({'op': tag, 'article': [list(A[i]) for i in range(i1, i2)], 'live': [list(L[j]) for j in range(j1, j2)], 'article_at': i1, 'live_at': j1})
# pair deleted/inserted blocks that are near-identical (moves) and replaced pairs (edits)
dele = [(o['article_at'] + k, b) for o in ops for k, b in enumerate(o['article'])]
ins = [(o['live_at'] + k, b) for o in ops for k, b in enumerate(o['live'])]
pairs = []
used = set()
for ai, (ak, at) in dele:
    best, bj = 0, None
    for lj, (lk, lt) in ins:
        if lj in used or ak[0] != lk[0] and not (ak.startswith('h') and lk.startswith('h')): continue
        r = difflib.SequenceMatcher(a=at, b=lt, autojunk=False).quick_ratio()
        if r > best:
            r = difflib.SequenceMatcher(a=at, b=lt, autojunk=False).ratio()
            if r > best: best, bj = r, lj
    if bj is not None and best >= 0.6:
        used.add(bj); pairs.append({'article_i': ai, 'live_j': bj, 'ratio': round(best, 3), 'article': [ak, at], 'live': list(dict(ins)[bj])})
paired_a = {p['article_i'] for p in pairs}
gone = [{'article_i': ai, 'block': list(b)} for ai, b in dele if ai not in paired_a]
new = [{'live_j': lj, 'block': list(b)} for lj, b in ins if lj not in used]
res = {'article_blocks': len(A), 'live_blocks': len(L), 'equal_ratio': round(sm.ratio(), 4),
       'changed_or_moved': pairs, 'only_in_article': gone, 'only_in_live': new}
json.dump(res, sys.stdout, ensure_ascii=False, indent=1)
