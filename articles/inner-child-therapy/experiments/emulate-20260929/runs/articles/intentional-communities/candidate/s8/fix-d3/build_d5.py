"""drafts-v5.json: drafts-v3 with the d3 gate's fixes as they stand in cand-v22.json (the variants that passed in
127g-135g; fix-d3/choice-v22.json names them), links and italics restored on the same words as in v3."""
import json, pathlib, re
HERE = pathlib.Path(__file__).resolve().parent
S8 = HERE.parent
P = json.load(open(S8 / 'cand-v22.json', encoding='utf-8'))  # the plain candidate after 127g-131g (fix-d3/compose.py)
D3 = json.load(open(S8 / 'drafts-v3.json', encoding='utf-8'))
C = json.load(open(S8 / 'cand-current.json', encoding='utf-8'))
CHOICE = [k for k in P if P[k] != C[k]]
MARK = {  # plain words -> markdown, each must occur exactly once in the chosen plain text
    'P8': [("The Continuum Concept", "[*The Continuum Concept*](https://www.arvindguptatoys.com/arvindgupta/conconcept.pdf)")],
    'P9': [("the practice of kids sleeping communally eventually ended for a mix of reasons: developmental findings, parents' preferences and social change",
            "[the practice of kids sleeping communally eventually ended for a mix of reasons: developmental findings, parents' preferences and social change](https://pubmed.ncbi.nlm.nih.gov/12395568/)")],
    'P12': [("Kinderhaus", "*Kinderhaus*")],
    'P20': [("seized 112 kids in the Island Pond raid",
             "[seized 112 kids in the Island Pond raid](https://vtdigger.org/2024/06/21/40-years-later-island-pond-has-little-interest-in-revisiting-its-historic-raid/)")],
    'P21': [("the research corpus", "[the research corpus](https://innerself.185-233-106-15.sslip.io/blog/commune-article-research/)")],
    'P22': [("roughly 85 percent or more of them end up joining",
             "[roughly 85 percent or more of them end up joining](https://groups.etown.edu/amishstudies/social-organization/population-growth/)"),
            ("Rumspringa", "*Rumspringa*")],
    'P27': [("schooling", "[schooling](https://www.instagram.com/p/DcDGotaFCeZ/?utm_source=ig_web_copy_link&igsh=MzRlODBiNWFlZA==)")],
}
D4 = dict(D3)
for k in CHOICE:
    t = P[k]; md = t
    for a, b in MARK.get(k, []):
        assert md.count(a) == 1, (k, a); md = md.replace(a, b)
    if k in ('P25a', 'P25b'):
        continue
    D4[k] = md
D4['P25'] = P['P25a'] + '\n\n' + P['P25b']
# every URL in v3 is still there exactly once
urls = lambda d: sorted(re.findall(r'\]\((https?://[^)]+)\)', '\n'.join(d.values())))
assert urls(D3) == urls(D4), (urls(D3), urls(D4))
json.dump(D4, open(S8 / 'drafts-v5.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('drafts-v5.json:', len(D4), 'blocks;', len(urls(D4)), 'links; changed vs v3:', ' '.join(k for k in D4 if D4[k] != D3.get(k)))
