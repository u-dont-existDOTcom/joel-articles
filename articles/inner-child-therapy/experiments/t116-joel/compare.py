#!/usr/bin/env python3
"""Turn 116: what Joel's edits and reorganization did, sentence by sentence, against the last guide I gave him.

The base is the article as installed in turn 114 (HUMANIZED-ARTICLE-SO-FAR.md at commit 8c7068d4, unchanged since; turn
115 installed nothing), with turn 115's pass applied where he may have taken it (experiments/t115-pass/FIXES.json), so a
sentence of the pass that he kept counts as kept, not as his. His version is JOEL-GUIDE-20261103.md (to_markdown.py).

Each block of both is read as the reader sees it (headings without their #s, links as their text, no emphasis marks), and
split into sentences. Then:
  - a sentence of his is KEPT when its words are a base sentence's (case, quote marks and spacing before punctuation
    aside), EDITED when a base sentence shares most of its words (difflib ratio 0.6 or more over words), NEW otherwise;
  - a base sentence nothing of his keeps or edits is CUT;
  - each of his paragraphs is placed against the base paragraph most of its kept or edited sentences come from, and a
    paragraph whose base home was under another heading path has MOVED.
Writes EDITS.json (every sentence and paragraph with its fate) and EDITS.md (the reorganization, then each section's
edited, new and cut sentences, the material for the lessons).

  python3 compare.py"""
import difflib
import json
import pathlib
import re
import subprocess
import sys
from collections import Counter, defaultdict

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
from paragraphs_alone import reader_blocks, plain  # noqa: E402

BASE_SHA = '8c7068d4c572590c93145deee3bafee72d55f608'
base_md = subprocess.run(['git', 'show', BASE_SHA + ':articles/inner-child-therapy/HUMANIZED-ARTICLE-SO-FAR.md'], cwd=ROOT,
                         capture_output=True, text=True, check=True).stdout
FIXES = json.loads((HERE.parent / 't115-pass' / 'FIXES.json').read_text(encoding='utf-8'))
pass_md = base_md
for f in FIXES['fixes']:
    if pass_md.count(f['old']) == 1:
        pass_md = pass_md.replace(f['old'], f['new'])
joel_md = (HERE / 'JOEL-GUIDE-20261103.md').read_text(encoding='utf-8')
STRAIGHT = str.maketrans({'“': '"', '”': '"', '‘': "'", '’': "'", '«': '"', '»': '"', ' ': ' ', ' ': ' '})


def norm(s):
    s = s.translate(STRAIGHT).lower()
    s = re.sub(r'\s+([?!:;.,])', r'\1', s)
    s = re.sub(r'"\s+|\s+"', '"', s)
    return re.sub(r'\s+', ' ', s).strip()


def blocks(md):
    out, path = [], []
    for k, b in reader_blocks(re.sub(r'<!--.*?-->', '', md, flags=re.S)):
        if k == 'h':
            lvl = len(re.match(r'^#+', b).group(0))
            t = plain(b.lstrip('#').strip())
            path = [p for p in path if p[0] < lvl] + [(lvl, t)]
            out.append({'kind': 'h', 'level': lvl, 'text': t, 'md': b, 'path': [x for _, x in path]})
        else:
            out.append({'kind': 'p', 'text': plain(b), 'md': b, 'path': [x for _, x in path]})
    return out


def sentences(t):
    t = re.sub(r'\s+', ' ', t).strip()
    parts = re.split(r'(?<=[.!?…])["”’)]*\s+(?=[A-Z“"(‘\'0-9])', t)
    return [p for p in parts if p.strip()]


def words(s):
    return re.findall(r"[a-z0-9']+", norm(s))


def main():
    B, P, J = blocks(base_md), blocks(pass_md), blocks(joel_md)
    # base sentences (from the base, and the pass's versions of the same paragraphs, tagged)
    bs = []
    for i, b in enumerate(B):
        for s in sentences(b['text']) if b['kind'] == 'p' else [b['text']]:
            bs.append({'block': i, 'kind': b['kind'], 'text': s, 'path': b['path'], 'used': False, 'src': 'base'})
    pass_new = set()
    for f in FIXES['fixes']:
        for s in sentences(plain(f['new'])):
            pass_new.add(norm(s))
    for i, b in enumerate(P):
        if b['kind'] != 'p':
            continue
        for s in sentences(b['text']):
            if norm(s) in pass_new:
                bs.append({'block': None, 'kind': 'p', 'text': s, 'path': b['path'], 'used': False, 'src': 'pass'})
    exact = defaultdict(list)
    for n, s in enumerate(bs):
        exact[norm(s['text'])].append(n)
    index = defaultdict(set)
    for n, s in enumerate(bs):
        for w in set(words(s['text'])):
            if len(w) > 3:
                index[w].add(n)
    js = []
    for j, b in enumerate(J):
        units = sentences(b['text']) if b['kind'] == 'p' else [b['text']]
        for s in units:
            rec = {'block': j, 'kind': b['kind'], 'text': s, 'path': b['path'], 'fate': 'NEW', 'match': None, 'ratio': 0.0}
            hits = exact.get(norm(s))
            if hits:
                n = next((h for h in hits if not bs[h]['used']), hits[0])
                rec.update(fate='KEPT', match=n, ratio=1.0)
                bs[n]['used'] = True
            else:
                ws = words(s)
                cand = Counter()
                for w in set(ws):
                    for n in index.get(w, ()):
                        cand[n] += 1
                best, br = None, 0.0
                for n, _ in cand.most_common(40):
                    if bs[n]['kind'] != b['kind']:
                        continue
                    r = difflib.SequenceMatcher(None, words(bs[n]['text']), ws, autojunk=False).ratio()
                    if r > br:
                        best, br = n, r
                if best is not None and br >= 0.6:
                    rec.update(fate='EDITED', match=best, ratio=round(br, 3))
                    bs[best]['used'] = True
            js.append(rec)
    # paragraphs: home in the base, moved or not
    paras = []
    for j, b in enumerate(J):
        if b['kind'] != 'p':
            continue
        mine = [r for r in js if r['block'] == j]
        homes = Counter()
        for r in mine:
            if r['match'] is not None and bs[r['match']]['block'] is not None:
                homes[bs[r['match']]['block']] += len(r['text'])
        home = homes.most_common(1)[0][0] if homes else None
        fates = Counter(r['fate'] for r in mine)
        paras.append({'block': j, 'path': b['path'], 'home': home, 'home_path': B[home]['path'] if home is not None else None,
                      'moved': home is not None and B[home]['path'][-1:] != b['path'][-1:] and B[home]['path'] != b['path'],
                      'fates': dict(fates), 'text': b['text'], 'sources': [k for k, _ in homes.most_common()]})
    cut = [s for s in bs if not s['used'] and s['src'] == 'base']
    out = {'base_commit': BASE_SHA, 'joel_file': 'JOEL-GUIDE-20261103.md',
           'counts': {'joel_sentences': Counter(r['fate'] for r in js if r['kind'] == 'p'),
                      'joel_headings': Counter(r['fate'] for r in js if r['kind'] == 'h'),
                      'base_sentences': sum(1 for s in bs if s['src'] == 'base' and s['kind'] == 'p'),
                      'base_cut_sentences': sum(1 for s in cut if s['kind'] == 'p'),
                      'base_cut_headings': sum(1 for s in cut if s['kind'] == 'h'),
                      'pass_sentences_kept': sum(1 for s in bs if s['src'] == 'pass' and s['used']),
                      'pass_sentences': sum(1 for s in bs if s['src'] == 'pass'),
                      'paragraphs': len(paras), 'paragraphs_moved': sum(p['moved'] for p in paras)},
           'joel': js, 'base': bs, 'paragraphs': paras, 'base_blocks': [{'kind': b['kind'], 'path': b['path'], 'text': b['text']} for b in B],
           'joel_blocks': [{'kind': b['kind'], 'path': b['path'], 'text': b['text']} for b in J]}
    (HERE / 'EDITS.json').write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print(json.dumps(out['counts'], indent=1))


if __name__ == '__main__':
    main()
