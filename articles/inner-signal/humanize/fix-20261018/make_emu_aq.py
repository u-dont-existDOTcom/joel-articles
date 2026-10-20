"""emu-aq, emu-ar, emu-as (2026-10-18, after 458g): more samples of what is still open, each from my meaning-right text.

  HG24 B1-B8            its opening ("Nothing happens", "It feels fake") read AI with or without its fixes (457g)
  HG36 B10-B11           the end of "Altered states" keeps a 52-56-word AI window (456g, 457g); one sample of the published
                         text, one of my fixed text per set
  HG17 B17-B21, B22-B26, B27-B31   the listening script in three medium windows: one window lost its steps (451g), seven
                         small ones read AI as a run (457g)
  HG18 B1-B3, B4-B6      the return steps in two medium windows
Three sample sets for HG24 and HG36 (they need the whole section to read Human), two for the scripts.
Run from fix-20261018/: python3 make_emu_aq.py
"""
import json, pathlib, sys
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE)); sys.path.insert(0, str(HERE.parent / 'tools'))
import make_emu_ac as E  # noqa: E402
import assemble as A  # noqa: E402

g444 = json.loads((HERE / 'b444' / 'GATE.json').read_text(encoding='utf-8'))


def win(key, path, blocks, name, keep_heading=True):
    text, rec = E.window(key, path, blocks)
    if not keep_heading:
        rec['sent'] = [b for b in rec['sent'] if b >= blocks[0]]
        rec['headings'] = [b for b in rec['headings'] if b >= blocks[0]]
        d = json.loads(pathlib.Path(path).read_text(encoding='utf-8'))
        text = '\n\n'.join(p for u in d['units'] if u['blocks'][0] in blocks for p in u['paras'])
        rec['words'] = len(text.split())
    return (name, text, rec)


kb = A.kb()
pub36 = kb['HG36'][10][1] + '\n\n' + kb['HG36'][11][1]
r36p = ('HG36-ew1', pub36, {'key': 'HG36', 'sent': [10, 11], 'flagged': [10, 11], 'headings': [], 'words': len(pub36.split()),
                            'input': 'published text', 'from': 'source/published-20260928.md B10-B11'})
f36 = json.loads((HERE / 'rf-p' / 'HG36.fixed.json').read_text(encoding='utf-8'))
t36 = '\n\n'.join(p for u in f36['units'] if u['blocks'][0] in (10, 11) for p in u['paras'])
r36f = ('HG36-ew2', t36, {'key': 'HG36', 'sent': [10, 11], 'flagged': [10, 11], 'headings': [], 'words': len(t36.split()),
                          'input': 'meaning-fixed text', 'from': str(HERE / 'rf-p' / 'HG36.fixed.json')})
H24 = HERE / 'rf-v' / 'HG24.fixed.json'
common = [win('HG24', H24, range(1, 9), 'HG24-ow1')]  # B1-B3 alone is 35 words, under Emulate's 40
scripts = [win('HG17', HERE / g444['HG17-fix']['reviews'], range(17, 22), 'HG17-mw1'),
           win('HG17', HERE / g444['HG17-fix']['reviews'], range(22, 27), 'HG17-mw2', keep_heading=False),
           win('HG17', HERE / g444['HG17-fix']['reviews'], range(27, 32), 'HG17-mw3', keep_heading=False),
           win('HG18', HERE / 'rev-b' / 'HG18.fixed.json', range(1, 4), 'HG18-mw1'),
           win('HG18', HERE / 'rev-b' / 'HG18.fixed.json', range(4, 7), 'HG18-mw2', keep_heading=False)]
for r in common + [r36p, r36f] + scripts:
    print(r[0], r[2]['sent'], r[2]['words'])
E.write('emu-aq', common + [r36p] + scripts, [])
E.write('emu-ar', common + [r36f] + scripts, [])
E.write('emu-as', common + [r36p], [])
