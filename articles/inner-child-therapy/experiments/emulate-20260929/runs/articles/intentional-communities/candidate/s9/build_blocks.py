"""Section 9 ("The Best Model I've Seen: Zapatistas"): the published section as labeled blocks (original-blocks.json,
markdown as published) and as the plain text the Pangram web app gets (plain-blocks.json: headings without '#',
captions without '[caption]', link targets and emphasis marks dropped, images left out)."""
import json, pathlib, re
HERE = pathlib.Path(__file__).resolve().parent
src = (HERE.parent.parent / 'sections/010-original.md').read_text(encoding='utf-8').strip()
paras = [p.strip() for p in re.split(r'\n\s*\n', src) if p.strip()]
O, P = {}, {}
n = img = cap = 0
for p in paras:
    if p.startswith('#'):
        k = 'H0'; O[k] = p; P[k] = p.lstrip('#').strip(); continue
    if p.startswith('[image'):
        img += 1; O['IMG%d' % img] = p; continue
    if p.startswith('[caption]'):
        cap += 1; k = 'CAP%d' % cap
    else:
        n += 1; k = 'P%d' % n
    O[k] = p
    t = re.sub(r'^\[caption\]\s*', '', p)
    t = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', t).replace('*', '')
    P[k] = t
json.dump(O, open(HERE / 'original-blocks.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump(P, open(HERE / 'plain-blocks.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(list(P.keys())); print({k: len(v.split()) for k, v in P.items()})
