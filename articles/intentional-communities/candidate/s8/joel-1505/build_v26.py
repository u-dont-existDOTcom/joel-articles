"""Section 8 v26: v25 with P19's "Keep everyone safe first" narrowed to "Keep everyone at risk safe first".
The d5 logic checks (A and B) both found "everyone" AMBIGUOUS: it can take in the accused, where the published
"Immediate safety comes first" meant the child and anyone else at risk. 145g (16:05:58 UTC): the whole section reads
100% Human, 1,722 words scanned. Writes cand-v26.json and section-d9.md."""
import json, pathlib
HERE = pathlib.Path(__file__).resolve().parent; S8 = HERE.parent
N = json.load(open(S8 / 'cand-v25.json', encoding='utf-8')); md = (S8 / 'section-d8.md').read_text(encoding='utf-8')
a, b = "Keep everyone safe first, right away,", "Keep everyone at risk safe first, right away,"
assert N['P19'].count(a) == 1 and md.count(a) == 1
N['P19'] = N['P19'].replace(a, b); md = md.replace(a, b)
json.dump(N, open(S8 / 'cand-v26.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
(S8 / 'section-d9.md').write_text(md, encoding='utf-8')
