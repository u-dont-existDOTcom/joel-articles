"""compose_v.py - a section's text from the samples the second reader chose, window by window (2026-10-18, rf-v/).

  rf-v/choices.json: {KEY: {"base": FIXED_OR_SPLIT.json, "windows": [{"blocks": [b, ...], "folder": "emu-X"}, ...],
                            "pruns": [{"run": "HG15-pw3", "folder": "emu-X", "paras": [a, b]}, ...]}}
  windows: Emulate segments of those published blocks from that folder replace the base's units (tools/refix_runs._merge,
  which takes every segment of a stretch); pruns: a run of paragraphs of one long stretch (paras a..b of the unit that has
  them, as pruns.json recorded) is replaced by the run's output paragraphs, by position, checked against the base text.
  Writes rf-v/KEY.units.json (the chosen stretches marked "refix", for the second reader's records and the triage).
Run from fix-20261018/: python3 compose_v.py KEY [KEY ...]
"""
import json, pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / 'tools'))
import assemble as A  # noqa: E402
import refix_runs as R  # noqa: E402


def compose(key, spec):
    base = HERE / spec['base']
    d = json.loads(base.read_text(encoding='utf-8'))
    segs = {}
    for w in spec.get('windows', []):
        got = A.run_segments([HERE / w['folder']])
        for (k, b0), v in got.items():
            if k == key and set(v[0]) <= set(w['blocks']):
                segs[(k, b0)] = v
        cover = sorted(b for (k, b0), v in segs.items() if set(v[0]) <= set(w['blocks']) for b in v[0])
        assert cover == sorted(w['blocks']), (key, w, cover)
    units = []
    for kind, u in R._merge(d, segs):
        if kind == 'seg':
            units.append({'kind': 'emulate', 'blocks': u[0], 'paras': u[1], 'run': u[2], 'file': u[3], 'refix': True})
        else:
            units.append({k: v for k, v in u.items() if k not in ('fixes', 'verdict', 'redo', 'paras_was', 'refix')})
    for pr in sorted(spec.get('pruns', []), key=lambda x: -x['paras'][0]):  # from the end, so earlier positions stay put
        out = (HERE / pr['folder'] / (pr['run'] + '.out.txt')).read_text(encoding='utf-8').strip()
        new = [p.strip() for p in out.split('\n\n') if p.strip()]
        src = (HERE / pr['folder'] / (pr['run'] + '.txt')).read_text(encoding='utf-8').strip()
        old = [p.strip() for p in src.split('\n\n') if p.strip()]
        u = next(x for x in units if x['kind'] == 'emulate' and len(x['paras']) > pr['paras'][1]
                 and x['paras'][pr['paras'][0]:pr['paras'][1] + 1] == old)
        a, b = pr['paras']
        u['paras'] = u['paras'][:a] + new + u['paras'][b + 1:]
        u.setdefault('pruns', []).append({'run': pr['run'], 'folder': pr['folder'], 'replaced': [a, b], 'new_count': len(new)})
        u['refix'] = True
    kb = A.kb()[key]
    assert sorted(b for x in units for b in x['blocks']) == list(range(len(kb))), (key, 'blocks')
    out = {'key': key, 'from': str(base), 'choices': spec, 'units': units}
    (HERE / 'rf-v' / ('%s.units.json' % key)).write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    return out


if __name__ == '__main__':
    ch = json.loads((HERE / 'rf-v' / 'choices.json').read_text(encoding='utf-8'))
    for key in sys.argv[1:]:
        o = compose(key, ch[key])
        print(key, len(o['units']), 'units;', sum(bool(x.get('refix')) for x in o['units']), 'from the chosen samples')
