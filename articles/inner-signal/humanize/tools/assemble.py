"""assemble.py - a key's text with Emulate's blocks put back in place of the flagged ones (2026-10-18).

  from assemble import assembled
  text, changed = assembled(key, emu_dirs, keep=KEEP)

Headings and unflagged blocks are the published text; a flagged block is replaced by its run's output block when the run
mapped cleanly (emu_runs.py back: the same number of paragraphs); KEEP names blocks that stay as published even inside
an AI window (Joel's own short lines: his greeting, his notes). Returns the text Pangram reads and {block: run} for what
changed.
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


def run_pairs(emu_dir):
    """{(key, block): (new text, run, out file)} from a folder's back.json."""
    d = pathlib.Path(emu_dir)
    out = {}
    for r in json.loads((d / 'back.json').read_text(encoding='utf-8')):
        if r.get('status') != 'ok':
            continue
        for p in r['pairs']:
            if 'new' in p:
                out[(r['key'], p['block'])] = (p['new'], r['run'], str(d / (r['run'] + '.out.txt')))
    return out


def assembled(key, emu_dirs, keep=None, only=None):
    """only: the blocks to replace (default: every block a run gives); keep: blocks never replaced."""
    keep = KEEP.get(key, set()) if keep is None else keep
    pairs = {}
    for d in emu_dirs:
        pairs.update(run_pairs(d))
    blocks = kb()[key]
    texts, changed, files = [], {}, set()
    for j, (md, plain, head) in enumerate(blocks):
        p = pairs.get((key, j))
        if p and j not in keep and not head and (only is None or j in only):
            texts.append(p[0]); changed[j] = p[1]; files.add(p[2])
        else:
            texts.append(plain)
    return '\n\n'.join(texts), changed, sorted(files)
