"""emu-ac, emu-ad, emu-ae (2026-10-18): several new samples of each window at once, so the second reader can pick the one
that keeps the meaning instead of one sample, one screen and one reading at a time.

Windows (each from my meaning-right text, never the published text):
  HG17 B17-B31  the listening script; the triage (rf-j/HG17.triage.json) sent it to a new sample (about 30% would change)
  HG31 B79-B80  the reframing questions; rf-j/HG31.triage.json resample
  HG06 B6       the forces paragraph: my fix (rf-f/HG06.fixed.json) read AI alone in 453g; three earlier samples bent it
  HG26 B1-B2    the get-help paragraphs (rf-h/HG26.fixed.json): AI 0.60 together in 453g
  HG24 B36-B40  B36 (rf-c/HG24.triage.json resample) is 21 words, under Emulate's 40, so it goes with the next stretch
  HG15 p9-p11, p23-p24  paragraphs of its one long stretch that read AI alone in 452g (rf-a/HG15.fixed.json); its 31
                paragraphs don't line up with its 20 published blocks, so these go as paragraph runs (pruns.json), put back
                by text, not by emu_runs.py back
Samples: emu-ac and emu-ad get every window; emu-ae a third sample of HG06 and HG26 (they failed most often).
Run from fix-20261018/: python3 make_emu_ac.py
"""
import hashlib, json, pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / 'tools'))
import assemble as A  # noqa: E402

g444 = json.loads((HERE / 'b444' / 'GATE.json').read_text(encoding='utf-8'))
g441 = json.loads((HERE / 'b441' / 'GATE.json').read_text(encoding='utf-8'))
WINDOWS = [('HG17', HERE / g444['HG17-fix']['reviews'], range(17, 32)),
           ('HG31', HERE / g444['HG31-fix']['reviews'], range(79, 81)),
           ('HG06', HERE / 'rf-f' / 'HG06.fixed.json', range(6, 7)),
           ('HG26', HERE / 'rf-h' / 'HG26.fixed.json', range(1, 3)),
           ('HG24', HERE / g441['HG24-fix']['reviews'], range(36, 41))]


def window(key, path, blocks):
    d = json.loads(pathlib.Path(path).read_text(encoding='utf-8'))
    us = d['units']
    ix = [i for i, u in enumerate(us) if set(u['blocks']) & set(blocks)]
    assert ix == list(range(ix[0], ix[-1] + 1)), (key, ix)
    while ix[0] > 0 and us[ix[0] - 1].get('heading'):
        ix.insert(0, ix[0] - 1)
    keep = A.KEEP.get(key, set())
    assert not any(set(us[i]['blocks']) & keep for i in ix), (key, 'a kept line of Joel\'s is in the window')
    text = '\n\n'.join(p for i in ix for p in us[i]['paras'])
    return text, {'key': key, 'sent': [b for i in ix for b in us[i]['blocks']],
                  'flagged': [b for i in ix if not us[i].get('heading') for b in us[i]['blocks']],
                  'headings': [b for i in ix if us[i].get('heading') for b in us[i]['blocks']],
                  'words': len(text.split()), 'input': 'meaning-fixed text', 'from': str(path)}


def hg15_runs():
    """The two paragraph windows of HG15's stretch that read AI alone in 452g, by their text in the checked drafts."""
    dr = json.loads((HERE / 'b452' / 'drafts.json').read_text(encoding='utf-8'))
    d = json.loads((HERE / 'rf-a' / 'HG15.fixed.json').read_text(encoding='utf-8'))
    u = next(x for x in d['units'] if x['kind'] == 'emulate' and len(x['paras']) > 20)
    paras = u['paras']
    p10, p11, p23 = dr['HG15-f-p10'], dr['HG15-f-p11'], dr['HG15-f-p23']
    i10, i11, i23 = paras.index(p10), paras.index(p11), paras.index(p23)
    p9 = dr['HG15-f-p9+next'][:-len(p10)].rstrip()
    p24 = dr['HG15-f-p24+prev'][len(p23):].lstrip()
    assert paras[i10 - 1] == p9 and i11 == i10 + 1 and paras[i23 + 1] == p24
    out = []
    for n, (a, b) in enumerate(((i10 - 1, i11), (i23, i23 + 1)), 1):
        text = '\n\n'.join(paras[a:b + 1])
        out.append(('HG15-pw%d' % n, text, {'key': 'HG15', 'unit_first_block': u['blocks'][0], 'paras': [a, b], 'words': len(text.split()),
                                             'input': 'meaning-fixed text (the triaged refix)', 'from': str(HERE / 'rf-a' / 'HG15.fixed.json')}))
    return out


def write(folder, runs, pruns):
    out = HERE / folder
    out.mkdir(exist_ok=True)
    manifest, bundle = [], {}
    for name, text, rec in runs:
        (out / (name + '.txt')).write_text(text, encoding='utf-8')
        bundle[name] = text
        manifest.append(dict(rec, run=name))
    pm = []
    for name, text, rec in pruns:
        (out / (name + '.txt')).write_text(text, encoding='utf-8')
        bundle[name] = text
        pm.append(dict(rec, run=name))
    (out / 'runs.json').write_text(json.dumps(manifest, indent=1) + '\n', encoding='utf-8')
    if pm:
        (out / 'pruns.json').write_text(json.dumps(pm, indent=1) + '\n', encoding='utf-8')
    s = json.dumps(bundle, ensure_ascii=False)
    (out / 'BUNDLE.json').write_text(s, encoding='utf-8')
    print(folder, len(bundle), 'runs,', sum(len(t.split()) for t in bundle.values()), 'words:', ' '.join(bundle),
          'sha256', hashlib.sha256(s.encode('utf-8')).hexdigest()[:16])


if __name__ == '__main__':
    runs = []
    for key, path, blocks in WINDOWS:
        text, rec = window(key, path, blocks)
        runs.append(('%s-fxw1' % key, text, rec))
    pr = hg15_runs()
    write('emu-ac', runs, pr)
    write('emu-ad', runs, pr)
    write('emu-ae', [r for r in runs if r[0].startswith(('HG06', 'HG26'))], [])
