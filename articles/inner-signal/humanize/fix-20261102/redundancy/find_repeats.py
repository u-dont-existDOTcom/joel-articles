"""Candidate repeats in the hypnosis guide, found by code for the lead session to judge (Joel, 2 November, on W-685:
"there was a whole lot there that was redundant, cut that. let's see what other redundancy remains in this article and
cut that also.").

Two finders over the guide's paragraphs (tools/humanization/suggestion_review.py's blocks, headings left out):
- pairs of paragraphs whose words overlap most (TF-IDF over words and two-word phrases, English stop words out, cosine
  similarity), nearest first;
- runs of six words or more said in two places (words compared without case or punctuation).
Neither decides anything: a repeat can be a cross-reference, a summary the reader needs, or a list the guide uses twice
on purpose. The lead session reads each candidate in place and says what it is (REPEATS.md).

  python3 articles/inner-signal/humanize/fix-20261102/redundancy/find_repeats.py [--top N]
Writes CANDIDATES.json here.
"""
import argparse
import collections
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parents[1]
ROOT = H.parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import suggestion_review as sr  # noqa: E402

FLAT = str.maketrans({'“': '"', '”': '"', '‘': "'", '’': "'"})


def words(t):
    return re.findall(r"[a-z0-9']+", t.translate(FLAT).lower())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--top', type=int, default=60)
    a = ap.parse_args()
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import cosine_similarity
    md = (H / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
    bl = sr.blocks(md)
    paras = [b for b in bl if not b['level'] and len(b['text'].split()) >= 10]
    texts = [b['text'] for b in paras]
    m = TfidfVectorizer(stop_words='english', ngram_range=(1, 2), min_df=1, sublinear_tf=True).fit_transform(texts)
    sim = cosine_similarity(m)
    pairs = []
    for i in range(len(paras)):
        for j in range(i + 1, len(paras)):
            if sim[i, j] >= 0.25:
                pairs.append((float(sim[i, j]), paras[i]['i'], paras[j]['i']))
    pairs.sort(reverse=True)
    # runs of 6+ words said twice
    grams = collections.defaultdict(list)
    for b in paras:
        w = words(b['text'])
        for k in range(len(w) - 5):
            grams[' '.join(w[k:k + 6])].append(b['i'])
    runs = collections.defaultdict(set)
    for g, where in grams.items():
        if len(set(where)) > 1:
            runs[tuple(sorted(set(where)))].add(g)
    sec = {b['i']: b['section'] for b in bl}
    out = {'guide_sha256': __import__('hashlib').sha256(md.encode('utf-8')).hexdigest(),
           'similar_pairs': [{'similarity': round(s, 3), 'a': i, 'b': j, 'a_section': sec[i], 'b_section': sec[j],
                              'a_text': bl[i]['text'], 'b_text': bl[j]['text']} for s, i, j in pairs[:a.top]],
           'repeated_runs': sorted(({'blocks': list(k), 'sections': [sec[x] for x in k], 'runs': len(v),
                                     'example': sorted(v)[0]} for k, v in runs.items()),
                                   key=lambda r: -r['runs'])[:a.top]}
    (HERE / 'CANDIDATES.json').write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print(len(paras), 'paragraphs;', len(pairs), 'pairs at 0.25 or more;', len(runs), 'block sets sharing a 6-word run')


if __name__ == '__main__':
    main()
