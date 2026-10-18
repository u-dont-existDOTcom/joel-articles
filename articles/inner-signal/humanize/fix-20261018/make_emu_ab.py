"""emu-ab (2026-10-18): new samples of the small AI windows left in triaged sections (451g: HG14's three windows of 73,
57 and 43 words, HG33's two of 191 and 128), each from its triaged text (rf-a/KEY.fixed.json, meaning right) split into
one unit per paragraph where a stretch has as many paragraphs as published blocks, so only the paragraphs in the window
are rewritten (tools/refix_runs.py window_runs). Run from fix-20261018/: python3 make_emu_ab.py"""
import json, pathlib, re, sys
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / 'tools'))
import refix_runs as R  # noqa: E402


def split(path, out):
    d = json.loads(pathlib.Path(path).read_text(encoding='utf-8'))
    us = []
    for u in d['units']:
        if u['kind'] == 'emulate' and len(u['blocks']) > 1 and len(u['paras']) == len(u['blocks']) and not u.get('links'):
            for b, p in zip(u['blocks'], u['paras']):
                us.append(dict({k: v for k, v in u.items() if k not in ('blocks', 'paras', 'links', 'fixes')}, blocks=[b], paras=[p]))
        else:
            us.append({k: v for k, v in u.items() if k != 'fixes'})
    assert '\n\n'.join(p for u in us for p in u['paras']) == '\n\n'.join(p for u in d['units'] for p in u['paras'])
    pathlib.Path(out).write_text(json.dumps(dict(d, units=us, split_from=str(path)), ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    return out


f451 = json.loads((HERE / 'b451' / 'flags.json').read_text(encoding='utf-8'))
cases = []
for key in ('HG14', 'HG33'):
    sp = split(HERE / 'rf-a' / ('%s.fixed.json' % key), HERE / 'rf-h' / ('%s.split.json' % key))
    cases.append((str(sp), f451[key + '-rfix']['flagged_blocks']))
    print(key, f451[key + '-rfix']['flagged_blocks'])
R.window_runs(HERE / 'emu-ab', cases)
