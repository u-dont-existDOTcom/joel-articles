"""The second reader for several Emulate samples of the same windows (2026-10-18, emu-ac, emu-ad, emu-ae): one folder per
sample set (rf-l, rf-m, rf-n), each with the section's units where only that sample's stretches are new ("refix"), so the
reader compares just those with the published blocks, and I can pick the sample that keeps the meaning best.

  HG17, HG31, HG06, HG26, HG24: units_fixed(base, folders) of the base text the window was cut from (HG24: its refix text
  with emu-s, emu-u and emu-aa), only the sample folder's units marked new.
  HG15: paragraph runs (pruns.json) of its one long stretch; the reader gets the published blocks they replace (B9-B11,
  B16-B17, matched by text) and the new paragraphs, in a units file of their own (KEY.p.json, never a section's units).
Run from fix-20261018/: python3 make_verify_samples.py
"""
import json, pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / 'tools'))
import faithful as F  # noqa: E402
import refix_runs as R  # noqa: E402

g441 = json.loads((HERE / 'b441' / 'GATE.json').read_text(encoding='utf-8'))
BASES = {'HG17': (HERE / 'rf-j' / 'HG17.fixed.json', []), 'HG31': (HERE / 'rf-j' / 'HG31.fixed.json', []),
         'HG06': (HERE / 'rf-f' / 'HG06.fixed.json', []), 'HG26': (HERE / 'rf-h' / 'HG26.fixed.json', []),
         'HG24': (HERE / g441['HG24-fix']['reviews'], [HERE / 'emu-s', HERE / 'emu-u', HERE / 'emu-aa'])}
HG15_BLOCKS = {'HG15-pw1': [9, 10, 11], 'HG15-pw2': [16, 17]}
MAX = 900


def compose(base, before, emu):
    """units_fixed(base, before + [emu]), except that a base unit whose blocks the sample folder's segments cover entirely
    (HG17: the old refix stretch B17-B31 is one unit; the new sample's segments are one per block) becomes those segments."""
    import assemble as A
    u = R.units_fixed(base, before + [emu])
    segs = {k: v for k, v in A.run_segments([emu]).items()}
    d = json.loads(pathlib.Path(base).read_text(encoding='utf-8'))
    out, done = [], set()
    for bu in d['units']:
        mine = sorted([v for (k, b0), v in segs.items() if k == d['key'] and b0 in bu['blocks']], key=lambda v: v[0][0])
        cover = [b for v in mine for b in v[0]]
        if len(bu['blocks']) > 1 and mine and cover == bu['blocks'] and len(mine) > 1:
            done |= set(bu['blocks'])
    if not done:
        return u
    for x in u['units']:
        if set(x['blocks']) & done:
            continue
        out.append(x)
    new = [{'kind': 'emulate', 'blocks': v[0], 'paras': v[1], 'run': v[2], 'file': v[3], 'refix': True}
           for (k, b0), v in segs.items() if k == d['key'] and set(v[0]) <= done]
    out = sorted(out + new, key=lambda x: x['blocks'][0])
    return dict(u, units=out)


def prompts(folder, key, units, tag=''):
    pub = F.pub_blocks(key)
    rf = [u for u in units if u.get('refix')]
    groups, cur, w = [], [], 0
    for u in rf:
        uw = len(' '.join(u['paras']).split())
        if cur and w + uw > MAX:
            groups.append(cur); cur, w = [], 0
        cur.append(u); w += uw
    if cur:
        groups.append(cur)
    out = []
    for n, g in enumerate(groups, 1):
        blocks = sorted({b for u in g for b in u['blocks']})
        published = '\n\n'.join('[B%d] %s' % (b, pub[b]) for b in blocks)
        rewrite = '\n\n'.join('[CHANGED, replaces %s]\n%s' % ('B%d' % u['blocks'][0] + ('-B%d' % u['blocks'][-1] if len(u['blocks']) > 1 else ''),
                                                              '\n\n'.join(u['paras'])) for u in g)
        text = F.VERIFY.format(about=F.ABOUT, published=published, rewrite=rewrite)
        if len(groups) > 1:
            text += F.VERIFY_NOTE.format(n=n, m=len(groups))
        p = folder / ('%s%s.verify.part%d.txt' % (key, tag, n))
        p.write_text(text, encoding='utf-8')
        out.append(str(p))
    return out


def main():
    jobs = []
    for emu, rf in (('emu-ac', 'rf-l'), ('emu-ad', 'rf-m'), ('emu-ae', 'rf-n')):
        E, D = HERE / emu, HERE / rf
        D.mkdir(exist_ok=True)
        runs = json.loads((E / 'runs.json').read_text(encoding='utf-8'))
        parts = []
        for key in sorted({r['key'] for r in runs}):
            base, before = BASES[key]
            u = compose(base, before, E)
            for x in u['units']:
                if x.get('refix') and ('/%s/' % emu) not in (x.get('file') or ''):
                    x['refix_was'] = True
                    del x['refix']
            (D / ('%s.units.json' % key)).write_text(json.dumps(u, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
            parts += prompts(D, key, u['units'])
        pr = E / 'pruns.json'
        if pr.exists():
            us = []
            for r in json.loads(pr.read_text(encoding='utf-8')):
                out = (E / (r['run'] + '.out.txt')).read_text(encoding='utf-8').strip()
                us.append({'kind': 'emulate', 'blocks': HG15_BLOCKS[r['run']], 'paras': [p.strip() for p in out.split('\n\n') if p.strip()],
                           'refix': True, 'run': r['run'], 'file': str(E / (r['run'] + '.out.txt')), 'replaces_paras': r['paras']})
            (D / 'HG15.p.json').write_text(json.dumps({'key': 'HG15', 'from': r['from'], 'units': us}, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
            parts += prompts(D, 'HG15', us)
        jobs.append(parts)
        print(rf, len(parts), 'parts:', ' '.join(pathlib.Path(p).name for p in parts))
    (HERE / 'rf-l' / 'jobs-samples.json').write_text(json.dumps(jobs, indent=1) + '\n', encoding='utf-8')


if __name__ == '__main__':
    main()
