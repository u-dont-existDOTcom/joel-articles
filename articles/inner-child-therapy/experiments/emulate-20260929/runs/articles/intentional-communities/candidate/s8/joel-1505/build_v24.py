"""Section 8 v24: v23 plus the three changes that made the whole section read 100% Human in Pangram's web app
(batches 140g and 142g, 15:26 and 15:28 UTC on 2026-10-07).

1. P28 loses its first sentence, "Once a kid is already living inside the disagreement, goodwill doesn't answer those
   questions." This is a PROPOSAL (asked at 03:35 and again at 15:24 UTC): it needs Joel's yes. With the sentence, the
   top window (P27's last sentence to P1's second) read AI in every wording tried (about 25).
2. P13's last sentence splits in two: "... boss the younger ones around there. And keeping secrets can't be treated as
   independence." ("secrecy" -> "keeping secrets"). With the cut alone, P13's end and P14's start read AI (42 words).
3. P14's last sentence drops the "X and still not Y" shape Joel named at 15:05 ("may be X and still Y"):
   "can destroy that gift and still not prevent abuse" -> "can destroy that gift, and it doesn't actually prevent
   abuse" (the published sentence had "without actually preventing abuse", which read AI beside the split in 141g).

Writes cand-v24.json (plain blocks) and section-d7.md (markdown), and checks that the markdown says the same words."""
import json, pathlib, re
HERE = pathlib.Path(__file__).resolve().parent
S8 = HERE.parent
N = json.load(open(S8 / 'cand-v23.json', encoding='utf-8'))
md = (S8 / 'section-d6.md').read_text(encoding='utf-8')
CH = [
    ('P28', "Once a kid is already living inside the disagreement, goodwill doesn't answer those questions. ", '',
     'proposal: cut (needs Joel)'),
    ('P13', "Older kids can't be allowed to quietly boss the younger ones around there, and secrecy can't be treated as independence.",
     "Older kids can't be allowed to quietly boss the younger ones around there. And keeping secrets can't be treated as independence.",
     'split, "keeping secrets" for "secrecy"'),
    ('P14', "Fear like that can destroy that gift and still not prevent abuse.",
     "Fear like that can destroy that gift, and it doesn't actually prevent abuse.",
     'the "and still not" tell'),
]
for k, a, b, why in CH:
    assert N[k].count(a) == 1 and md.count(a) == 1, (k, a)
    N[k] = N[k].replace(a, b); md = md.replace(a, b)
json.dump(N, open(S8 / 'cand-v24.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
(S8 / 'section-d7.md').write_text(md, encoding='utf-8')
# the markdown, stripped of its markup and its image/caption/video lines, must give the same paragraphs as the plain blocks
def plain(p):
    p = re.sub(r'^#+ ', '', p); p = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', p); return p.replace('*', '')
blocks = [plain(p) for p in re.split(r'\n\s*\n', md.strip())]
blocks = [b for b in blocks if not b.startswith('[image') and not b.startswith('[video')]
mine = [v if not k.startswith('CAP') else v for k, v in N.items()]
missing = [k for k, v in N.items() if not any(v == b or ('[caption] ' + v) == b or v == b.replace('[caption] ', '') for b in blocks)]
print('blocks', len(N), 'markdown paragraphs', len(blocks), 'not matched:', missing)
print('words', len('\n\n'.join(N.values()).split()))
