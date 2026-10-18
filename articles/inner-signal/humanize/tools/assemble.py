"""assemble.py - a key's text with Emulate's stretches put back in place of the flagged blocks (2026-10-18).

  from assemble import assembled, units
  text, changed, files = assembled(key, emu_dirs)          # the text Pangram reads, {first block: run}, run files used
  us = units(key, emu_dirs)                                # [{'kind', 'blocks', 'paras', 'run'}] in order

Headings and unflagged blocks are the published text. A run's output comes back as segments (emu_runs.py back): one
block for one paragraph when Emulate kept the count, else the stretch between two headings for Emulate's paragraphs
there. KEEP names blocks that stay as published even inside an AI window (Joel's own short lines); a segment that holds
one of them stays published whole. A later folder's segment for the same blocks wins over an earlier one's.
"""
import json, pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parent
sys.path.insert(0, str(HERE))
import emu_runs as E  # noqa: E402

# Joel's own lines inside an AI window, kept as published (2026-10-18): his opening line, his table-of-contents note, his
# greeting. They are his voice ("Working hard!", "kinda", "Lovey Bunny"), and the windows that read AI are the paragraphs
# around them.
KEEP = {'HG01': {0}, 'HG02+03': {1, 3}}
_KB = None


def kb():
    global _KB
    if _KB is None:
        _KB = E.key_blocks(H / 'HUMANIZED-SO-FAR.md', H / 'source' / 'substack-editor-20260928.html')
    return _KB


def run_segments(emu_dirs):
    """{(key, first block): (blocks, paragraphs, run, out file)} from the folders' back.json, later folders winning."""
    out = {}
    for d in emu_dirs:
        d = pathlib.Path(d)
        for r in json.loads((d / 'back.json').read_text(encoding='utf-8')):
            if not str(r.get('status', '')).startswith('ok'):
                continue
            for sg in r['segments']:
                out[(r['key'], sg['blocks'][0])] = (sg['blocks'], sg['new'], r['run'], str(d / (r['run'] + '.out.txt')))
    return out


def units(key, emu_dirs, keep=None, only=None):
    keep = KEEP.get(key, set()) if keep is None else keep
    segs = run_segments(emu_dirs)
    blocks = kb()[key]
    out, j = [], 0
    while j < len(blocks):
        sg = segs.get((key, j))
        if sg and not (set(sg[0]) & keep) and (only is None or set(sg[0]) <= set(only)) and not any(blocks[b][2] for b in sg[0]):
            out.append({'kind': 'emulate', 'blocks': sg[0], 'paras': sg[1], 'run': sg[2], 'file': sg[3]})
            j = sg[0][-1] + 1
        else:
            out.append({'kind': 'published', 'blocks': [j], 'paras': [blocks[j][1]], 'heading': blocks[j][2]})
            j += 1
    return out


def assembled(key, emu_dirs, keep=None, only=None):
    us = units(key, emu_dirs, keep, only)
    text = '\n\n'.join(p for u in us for p in u['paras'])
    changed = {u['blocks'][0]: u['run'] for u in us if u['kind'] == 'emulate'}
    files = sorted({u['file'] for u in us if u['kind'] == 'emulate'})
    return text, changed, files


if __name__ == '__main__':
    import argparse
    ap = argparse.ArgumentParser(description='write a key\'s units (published and Emulate stretches) as JSON')
    ap.add_argument('key'); ap.add_argument('emu_dirs', nargs='+'); ap.add_argument('--out', required=True)
    a = ap.parse_args()
    us = units(a.key, a.emu_dirs)
    pathlib.Path(a.out).write_text(json.dumps({'key': a.key, 'emu_dirs': a.emu_dirs, 'units': us}, ensure_ascii=False, indent=1) + '\n',
                                   encoding='utf-8')
    print(a.key, len(us), 'units,', sum(u['kind'] == 'emulate' for u in us), 'from Emulate ->', a.out)
