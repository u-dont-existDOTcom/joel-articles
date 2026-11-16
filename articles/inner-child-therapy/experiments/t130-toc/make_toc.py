"""Build reader contents files from the live post's sections (or from a proposal).
make_toc.py sections.json OUTDIR            -> TOC-NOW.json, TOC-NOW-FULL.md, TOC-NOW-SIDEBAR.md
Each entry: id, level, heading, words (own words, with any unlisted h5+ below it folded in)."""
import json, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..', 'tools', 'humanization'))
import toc_sidebar as ts

def entries_from_sections(path):
    S = json.load(open(path))
    out = []
    for s in S:
        if s['level'] == 0: continue
        if s['level'] > 4:
            out[-1]['words'] += s['own_words']; out[-1]['folded'] = out[-1].get('folded', []) + [f"S{s['idx']:03d}"]; continue
        if not s['heading'].strip():
            continue  # an empty heading shows only as a blank line in the sidebar
        out.append({'id': f"S{s['idx']:03d}", 'level': s['level'], 'heading': s['heading'].strip(), 'words': s['own_words']})
    return out

def render(entries, title, sidebar, note=''):
    lines = [f"# {title}", '']
    if note: lines += [note, '']
    for e in entries:
        h = ts.shown(e['heading'], e['level'])[1] if sidebar else e['heading']
        lines.append('    ' * (e['level'] - 1) + '#' * e['level'] + ' ' + h + f"  ({e['words']} words)")
    return '\n'.join(lines) + '\n'

if __name__ == '__main__':
    src, outdir = sys.argv[1], sys.argv[2]
    E = entries_from_sections(src)
    os.makedirs(outdir, exist_ok=True)
    json.dump(E, open(os.path.join(outdir, 'TOC-NOW.json'), 'w'), ensure_ascii=False, indent=1)
    print(len(E), 'listed headings;', sum(e['words'] for e in E), 'words')
