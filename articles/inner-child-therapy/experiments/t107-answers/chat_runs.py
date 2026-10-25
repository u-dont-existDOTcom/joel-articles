#!/usr/bin/env python3
"""Turn 107: where the article repeats a long run of one of Joel's messages (E261 (Inner Child)). For each article paragraph
(notes left out, links as their words), the longest run of 12 or more words it shares with any message saved in
experiments/*/JOEL-*.md (turns 55 to 107; earlier turns' messages weren't saved whole). "chat" marks a run whose source
has his chat lowercase "i" or differs from the article only by capitals, the sign of an answer typed to me rather than a
line for the article. Run from articles/inner-child-therapy/; writes CHAT-RUNS.json beside it. Which runs are answers
and which are lines he gave for the article is a reading, recorded in LESSONS.md beside this file."""
import re, glob, json, sys
art = open('HUMANIZED-ARTICLE-SO-FAR.md', encoding='utf-8').read()
TR = str.maketrans({'’': "'", '‘': "'", '“': '"', '”': '"'})
def clean(s):
    s = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', s).replace('*', '')
    return s.translate(TR)
def toks(s):
    return [(m.group(0), m.start()) for m in re.finditer(r"[A-Za-z0-9']+", s)]
# article paragraphs with their heading
paras = []
head = ''
for block in re.split(r'\n\s*\n', re.sub(r'<!--.*?-->', '', art, flags=re.S)):
    b = block.strip()
    if not b: continue
    if b.startswith('#'):
        head = b.split('\n')[0]; continue
    paras.append((head, clean(b)))
srcs = []
for f in sorted(glob.glob('experiments/*/JOEL-*.md')):
    t = open(f, encoding='utf-8').read()
    t = t.split('\n---\n', 1)[-1]
    srcs.append((f, clean(t)))
def runs(pw, sw):
    # longest common contiguous run, case-insensitive; returns (len, i_end, j_end)
    best = (0, 0, 0)
    pl = [w.lower() for w, _ in pw]; sl = [w.lower() for w, _ in sw]
    idx = {}
    for j, w in enumerate(sl): idx.setdefault(w, []).append(j)
    prev = {}
    for i, w in enumerate(pl):
        cur = {}
        for j in idx.get(w, []):
            v = prev.get(j - 1, 0) + 1
            cur[j] = v
            if v > best[0]: best = (v, i, j)
        prev = cur
    return best
out = []
for head, p in paras:
    pw = toks(p)
    if len(pw) < 12: continue
    for f, s in srcs:
        sw = toks(s)
        n, i, j = runs(pw, sw)
        if n >= 12:
            src_span = s[sw[j - n + 1][1]: sw[j][1] + len(sw[j][0])]
            art_span = p[pw[i - n + 1][1]: pw[i][1] + len(pw[i][0])]
            # chat register: lowercase pronoun i, or the span differs from the article only by case
            lower_i = bool(re.search(r"(?<![A-Za-z'])i(?![A-Za-z])|(?<![A-Za-z'])i'(?:m|d|ve|ll)", src_span))
            case_diff = src_span != art_span
            out.append(dict(head=head, file=f, n=n, plen=len(pw), share=round(n / len(pw), 2), chat=lower_i or case_diff, art=art_span[:160], src=src_span[:160]))
# keep best source per paragraph-span
seen = {}
for o in sorted(out, key=lambda o: -o['n']):
    k = (o['head'], o['art'][:60])
    if k not in seen: seen[k] = o
res = sorted(seen.values(), key=lambda o: (not o['chat'], -o['share']))
json.dump(res, open('experiments/t107-answers/CHAT-RUNS.json', 'w'), ensure_ascii=False, indent=1)
print(len(res), 'candidates;', sum(1 for o in res if o['chat']), 'chat-register')
for o in res:
    if o['chat']:
        print(o['share'], o['n'], o['head'][:40], '|', o['file'].split('/')[1], '|', o['art'][:100])
