"""emu-ah, emu-ai (2026-10-18): two samples each of the paragraphs that read AI alone in 454g, from my meaning-right text.

  HG14 B6-B7, B8-B9, B43-B44, B77   (454g: p5+next, p7+next, p42+next and p43, p72; rf-k/HG14.fixed.json)
  HG37 B26                          (454g p20, Emulate's own words, AI 0.81 alone; rf-e/HG37.fixed.json split by paragraph)
  HG15 p10, p11                     (452g; the two samples of their window B9-B11 in emu-ac/emu-ad each lost or bent six to
                                     nine points, so each paragraph goes alone now: pruns.json, put back by text)
Run from fix-20261018/: python3 make_emu_ah.py
"""
import json, pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import make_emu_ac as E  # noqa: E402  (never import make_emu_ab: its module code rebuilds emu-ab and rf-h)


def split(path, out):
    d = json.loads(pathlib.Path(path).read_text(encoding='utf-8'))
    us = []
    for u in d['units']:
        if u['kind'] == 'emulate' and len(u['blocks']) > 1 and len(u['paras']) == len(u['blocks']) and not u.get('links'):
            for b, p in zip(u['blocks'], u['paras']):
                us.append(dict({k: v for k, v in u.items() if k not in ('blocks', 'paras', 'links', 'fixes')}, blocks=[b], paras=[p]))
        else:
            us.append(u)
    assert '\n\n'.join(p for u in us for p in u['paras']) == '\n\n'.join(p for u in d['units'] for p in u['paras'])
    pathlib.Path(out).write_text(json.dumps(dict(d, units=us, split_from=str(path)), ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    return pathlib.Path(out)


if __name__ == '__main__':
    (HERE / 'rf-q').mkdir(exist_ok=True)
    h37 = split(HERE / 'rf-e' / 'HG37.fixed.json', HERE / 'rf-q' / 'HG37.split.json')
    runs = []
    for n, w in enumerate((range(6, 8), range(8, 10), range(43, 45), range(77, 78)), 1):
        text, rec = E.window('HG14', HERE / 'rf-k' / 'HG14.fixed.json', w)
        runs.append(('HG14-pw%d' % n, text, rec))
    text, rec = E.window('HG37', h37, range(26, 27))
    runs.append(('HG37-pw1', text, rec))
    # HG15 p10 and p11 alone (the paragraph texts 452g checked), from rf-a/HG15.fixed.json's one long stretch
    dr = json.loads((HERE / 'b452' / 'drafts.json').read_text(encoding='utf-8'))
    d = json.loads((HERE / 'rf-a' / 'HG15.fixed.json').read_text(encoding='utf-8'))
    u = next(x for x in d['units'] if x['kind'] == 'emulate' and len(x['paras']) > 20)
    pr = []
    for n, nm in enumerate(('HG15-f-p10', 'HG15-f-p11'), 3):
        i = u['paras'].index(dr[nm])
        pr.append(('HG15-pw%d' % n, dr[nm], {'key': 'HG15', 'unit_first_block': u['blocks'][0], 'paras': [i, i], 'words': len(dr[nm].split()),
                                             'input': 'meaning-fixed text (the triaged refix)', 'from': str(HERE / 'rf-a' / 'HG15.fixed.json')}))
    for r in runs + pr:
        print(r[0], r[2].get('sent', r[2].get('paras')), r[2]['words'])
    E.write('emu-ah', runs, pr)
    E.write('emu-ai', runs, pr)
