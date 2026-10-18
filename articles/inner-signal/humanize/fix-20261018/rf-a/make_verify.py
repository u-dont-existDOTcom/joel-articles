"""The second reader for the refix screens that read Human in 443g (2026-10-18): each refix stretch (Emulate's rewrite of
my meaning-fixed text, emu-r) against the published blocks it replaces, in parts of at most MAX words of new text, with
faithful.py's VERIFY template. The section's other stretches were checked before (rev-*, verify-*). Writes
rf-a/<key>.verify.partN.txt and rf-a/jobs.json (parts grouped for one reader each). Run from fix-20261018/:
python3 rf-a/make_verify.py [FOLDER] (default rf-a; rf-b holds 445g's)."""
import json, pathlib, sys
HERE = pathlib.Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1] / 'tools'))
import faithful as F  # noqa: E402
MAX = 900
parts = []
for f in sorted(HERE.glob('*.units.json')):
    d = json.loads(f.read_text(encoding='utf-8'))
    key, pub = d['key'], F.pub_blocks(d['key'])
    rf = [u for u in d['units'] if u.get('refix')]
    groups, cur, w = [], [], 0
    for u in rf:
        uw = len(' '.join(u['paras']).split())
        if cur and w + uw > MAX:
            groups.append(cur); cur, w = [], 0
        cur.append(u); w += uw
    if cur:
        groups.append(cur)
    for n, g in enumerate(groups, 1):
        blocks = sorted({b for u in g for b in u['blocks']})
        published = '\n\n'.join('[B%d] %s' % (b, pub[b]) for b in blocks)
        rewrite = '\n\n'.join('[CHANGED, replaces %s]\n%s' % ('B%d' % u['blocks'][0] + ('-B%d' % u['blocks'][-1] if len(u['blocks']) > 1 else ''),
                                                              '\n\n'.join(u['paras'])) for u in g)
        text = F.VERIFY.format(about=F.ABOUT, published=published, rewrite=rewrite)
        if len(groups) > 1:
            text += F.VERIFY_NOTE.format(n=n, m=len(groups))
        out = HERE / ('%s.verify.part%d.txt' % (key, n))
        out.write_text(text, encoding='utf-8')
        parts.append((str(out), len(text.split())))
jobs, cur, w = [], [], 0
for p, pw in parts:
    if cur and (w + pw > 3200 or len(cur) >= 4):
        jobs.append(cur); cur, w = [], 0
    cur.append(p); w += pw
if cur:
    jobs.append(cur)
(HERE / 'jobs.json').write_text(json.dumps(jobs, indent=1) + '\n', encoding='utf-8')
print(len(parts), 'parts in', len(jobs), 'jobs:', [len(j) for j in jobs])
