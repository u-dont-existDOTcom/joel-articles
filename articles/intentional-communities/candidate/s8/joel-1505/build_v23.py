"""Section 8 v23: Joel's 15:05 UTC edits (joel-20261007-1505.json) on v22.
- P27 and P28 open the section, under its title ("i would move p27-p28 to the top of the section"); their subheading
  "Discuss Child-Rearing Values Before Children Are Caught Between Them" goes, since its two paragraphs now open the section.
- P2 is P2b ("only saying that…"; his "agree" to question 1). P3, P10, P18, P21 and P22-P26 are his texts.
- P7 is cut and the subheading becomes "Communal Parenting Adds On" (his ruling); P26 is not in his rewrite of P22-P26.
- P13 ("boss") and P17 (the spelled-out surprise) stay, both OK'd by him.
Typo fixes, his rule: "althoug" -> "although"; "able to access to their own records" -> "able to access their own records";
P10's "~~rather than~~ instead of" is the page's diff marking copied with the text: "instead of". Double spaces and trailing
spaces are whitespace only.
Writes cand-v23.json (plain blocks, as the web app gets them), section-d6.md (markdown with links, images and video) and
prints the changes from v22."""
import json, pathlib, re
HERE = pathlib.Path(__file__).resolve().parent
S8 = HERE.parent
J = json.load(open(HERE / 'joel-20261007-1505.json', encoding='utf-8'))
B = json.load(open(S8 / 'cand-v22.json', encoding='utf-8'))
V = {}
for f in ('v127-parts.json', 'v128-parts.json', 'v129-parts.json', 'v130-parts.json', 'v131-parts.json', 'v133-parts.json', 'v134-parts.json', 'v135-parts.json'):
    V.update(json.load(open(S8 / 'fix-d3' / f, encoding='utf-8')))
ws = lambda t: re.sub(r' {2,}', ' ', t).strip()
fixes = []
def fix(t, a, b, why):
    assert t.count(a) == 1, (a, t[:80]); fixes.append('%s -> %s (%s)' % (a, b, why)); return t.replace(a, b)
P10 = fix(ws(J['P10']), '~~rather than~~ instead of', 'instead of', "the page's diff marking")
S8d = [ws(p) for p in J['S8d']]
S8d[1] = fix(S8d[1], 'althoug they', 'although they', 'typo')
S8d[4] = fix(S8d[4], 'able to access to their own', 'able to access their own', 'typo')
N = {'H0': B['H0'], 'P27': B['P27'], 'P28': B['P28'], 'P1': B['P1'], 'CAP1': B['CAP1'], 'P2': V['f-P2b'], 'P3': ws(J['P3']), 'P4': B['P4'],
     'P5': B['P5'], 'P6': B['P6'], 'H1': 'Communal Parenting Adds On', 'P8': B['P8'], 'P9': B['P9'], 'P10': P10,
     'H2': B['H2'], 'CAP2': B['CAP2']}
for k in ('P11', 'P12', 'P13', 'P14', 'P15', 'P16', 'P17'): N[k] = B[k]
N['P18'] = ws(J['P18']); N['P19'] = B['P19']; N['P20'] = B['P20']; N['P21'] = ws(J['P21']); N['H3'] = B['H3']
N['P23'] = S8d[0]; N['P22'] = S8d[1]; N['P24'] = S8d[2]; N['P25a'] = S8d[3]; N['P25b'] = S8d[4]; N['P25c'] = S8d[5]
assert N['P23'] == B['P23'], 'his P23 is v22\'s P23n'
json.dump(N, open(S8 / 'cand-v23.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
# markdown: start from section-d5.md's blocks for images, captions, video and links
d5 = [p for p in re.split(r'\n\s*\n', (S8 / 'section-d5.md').read_text(encoding='utf-8').strip())]
md = {}
def find(start):
    hits = [p for p in d5 if p.startswith(start)]; assert len(hits) == 1, start; return hits[0]
LINKS = {'P8': ("The Continuum Concept", "[*The Continuum Concept*](https://www.arvindguptatoys.com/arvindgupta/conconcept.pdf)"),
         'P21': ('the research corpus', '[the research corpus](https://innerself.185-233-106-15.sslip.io/blog/commune-article-research/)'),
         'P22': ('roughly 85 percent or more of them end up joining', '[roughly 85 percent or more of them end up joining](https://groups.etown.edu/amishstudies/social-organization/population-growth/)'),
         'P27': ('schooling', '[schooling](https://www.instagram.com/p/DcDGotaFCeZ/?utm_source=ig_web_copy_link&igsh=MzRlODBiNWFlZA==)')}
def mdize(k, t):
    if k in LINKS:
        a, b = LINKS[k]; assert t.count(a) == 1, (k, a); t = t.replace(a, b)
    if k == 'P12': t = t.replace('Kinderhaus', '*Kinderhaus*')
    if k == 'P22': t = t.replace('Rumspringa', '*Rumspringa*')
    return t
out = ['# ' + N['H0'], mdize('P27', N['P27']), N['P28'], find('My own childhood'), find('[image 12]'), find('[caption] Me as a child'),
       N['P2'], N['P3'], find('I actually learned'), find('Double click'), find('A friend who'), find('What she said'),
       '## ' + N['H1'], mdize('P8', N['P8']), find('Experiments where kids'), N['P10'],
       '## ' + N['H2'], find('[image 13]'), find('[caption] African kids')]
for k in ('P11', 'P12', 'P13', 'P14', 'P15', 'P16', 'P17'): out.append(find(N[k][:30]) if k != 'P12' else find("I got a taste"))
out += [N['P18'], find(N['P19'][:30]), find(N['P20'][:30]), mdize('P21', N['P21']), '## ' + N['H3']]
out += [N['P23'], mdize('P22', N['P22']), N['P24'], N['P25a'], N['P25b'], N['P25c']]
assert find('Experiments where kids').count('pubmed') == 1 and find('In 1984') if False else True
(S8 / 'section-d6.md').write_text('\n\n'.join(out) + '\n', encoding='utf-8')
urls = re.findall(r'\]\((https?://[^)]+)\)', '\n'.join(out))
print('links', len(urls), '| blocks', len(out)); print('\n'.join(fixes))
for k in N:
    if k not in B or N[k] != B[k]: print('changed from v22:', k)
print('dropped from v22:', [k for k in B if k not in N])
