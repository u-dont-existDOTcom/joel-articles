"""Section 8 v27: Joel's message of 2026-10-07 20:21 UTC (joel-20261007-2021.json) on v26.
- P28's cut stays ("p28 looks better now yes"); the H4 heading stays out ("ok").
- P23 is his new first paragraph for the subsection: his P23 plus the point of the published P26, which he had
  left out by accident ("And kids coming back isn't necessarily the best thing for the communal movement either...").
- P10 is his new version ("Here's a better version tho"). Its double space after "underpinnings." is whitespace only.
- P18: "it requires them to help also" -> "it requires children to help also" ("yes fix that").
- P22: "a commitment they choose on their own" -> "a commitment they make as adults" ("yes that's better").
- P25's last line keeps only its second half ("i agree with your suggestion to shorten the last line"):
  "No upbringing can provide perfect freedom, because path dependence is a reality, but belonging and freedom should
  go hand in hand." -> "Belonging and freedom should go hand in hand."
Writes cand-v27.json and section-d10.md, and checks the markdown says the same words."""
import json, pathlib, re
HERE = pathlib.Path(__file__).resolve().parent; S8 = HERE.parent
J = json.load(open(HERE / 'joel-20261007-2021.json', encoding='utf-8'))
N = json.load(open(S8 / 'cand-v26.json', encoding='utf-8')); md = (S8 / 'section-d9.md').read_text(encoding='utf-8')
ws = lambda t: re.sub(r' {2,}', ' ', t).strip()
def whole(k, new):
    global md
    assert md.count(N[k]) == 1, k
    md = md.replace(N[k], new); N[k] = new
def part(k, a, b):
    global md
    assert N[k].count(a) == 1 and md.count(a) == 1, (k, a)
    N[k] = N[k].replace(a, b); md = md.replace(a, b)
whole('P23', ws(J['P23']))
whole('P10', ws(J['P10']))
part('P18', 'it requires them to help also', 'it requires children to help also')
part('P22', 'a commitment they choose on their own', 'a commitment they make as adults')
whole('P25c', 'Belonging and freedom should go hand in hand.')
json.dump(N, open(S8 / 'cand-v27.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
(S8 / 'section-d10.md').write_text(md, encoding='utf-8')
def plain(p):
    p = re.sub(r'^#+ ', '', p); p = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', p); return p.replace('*', '')
blocks = [plain(p) for p in re.split(r'\n\s*\n', md.strip())]
missing = [k for k, v in N.items() if not any(v == b or v == b.replace('[caption] ', '') for b in blocks)]
print('not matched in the markdown:', missing, '| words', len('\n\n'.join(N.values()).split()))
