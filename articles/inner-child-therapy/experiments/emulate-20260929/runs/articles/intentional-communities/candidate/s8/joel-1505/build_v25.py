"""Section 8 v25: v24 with P14's last sentence keeping the possibility (the gate's d7 trace: v24's "doesn't actually
prevent abuse" was a flat claim where v23 and the published sentence put a "can" over both halves).
"Fear like that can destroy that gift, and it doesn't actually prevent abuse." ->
"Fear like that can destroy that gift, and it might not even prevent abuse." (144g, 15:53:16 UTC: the whole section
reads 100% Human, 1,720 words scanned). P13 keeps "keeping secrets" ("secrecy" brought the P13-P14 window back in
every 143g variant). Writes cand-v25.json and section-d8.md."""
import json, pathlib
HERE = pathlib.Path(__file__).resolve().parent; S8 = HERE.parent
N = json.load(open(S8 / 'cand-v24.json', encoding='utf-8')); md = (S8 / 'section-d7.md').read_text(encoding='utf-8')
a = "Fear like that can destroy that gift, and it doesn't actually prevent abuse."
b = "Fear like that can destroy that gift, and it might not even prevent abuse."
assert N['P14'].count(a) == 1 and md.count(a) == 1
N['P14'] = N['P14'].replace(a, b); md = md.replace(a, b)
json.dump(N, open(S8 / 'cand-v25.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
(S8 / 'section-d8.md').write_text(md, encoding='utf-8')
