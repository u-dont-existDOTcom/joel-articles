"""Map the windows of a Pangram 4.1 result (RESULT-41a.json, the Substack check of 2026-10-20) onto the guide's blocks.

The checked text is the post's paragraphs without its headings, so each block of the working copy (HUMANIZED-SO-FAR.md,
with its h1 and h2 headings) is found in it by its words, in order, and each window is given the blocks it overlaps.

  python3 articles/inner-signal/humanize/fix-20261020/result41/map_windows.py RESULT.json OUT.json   (from the repo root)

Prints the red (AI-Generated) and light-green (Human, Low or Medium) windows with their sections.
"""
import json, re, sys, pathlib

REPO = pathlib.Path(__file__).resolve().parents[5]
sys.path.insert(0, str(REPO / 'tools' / 'humanization'))
import substack_merge as SM   # md_blocks, plain_md, body_md

H = REPO / 'articles' / 'inner-signal' / 'humanize'


def norm_map(t):
    """t with its whitespace runs collapsed to one space and quotes straightened, and a map from each output index to t."""
    out, idx, prev_space = [], [], False
    tr = {'’': "'", '‘': "'", '“': '"', '”': '"', ' ': ' '}
    for i, ch in enumerate(t):
        ch = tr.get(ch, ch)
        if ch.isspace():
            if prev_space:
                continue
            ch, prev_space = ' ', True
        else:
            prev_space = False
        out.append(ch); idx.append(i)
    return ''.join(out), idx


def main(result_path, out_path):
    d = json.loads(pathlib.Path(result_path).read_text(encoding='utf-8'))
    text = d['text']
    nt, nidx = norm_map(text)
    blocks = SM.md_blocks((H / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8'))
    h1 = h2 = None
    placed, cursor = [], 0
    for k, b in enumerate(blocks):
        if b['kind'] == 'heading':
            lv = len(re.match(r'^(#+)', b['md']).group(1))
            title = SM.plain_md(b['md'].lstrip('#'))
            if lv == 1:
                h1, h2 = title, None
            else:
                h2 = title
            continue
        if b['kind'] != 'para':
            continue
        plain, _ = norm_map(SM.plain_md(SM.body_md(b)))
        key = plain[:60]
        j = nt.find(key, cursor)
        if j < 0 or j - cursor > 4000:
            continue
        end = j + len(plain)
        placed.append({'block': k, 'h1': h1, 'h2': h2, 'start': nidx[j], 'end': nidx[min(end, len(nidx)) - 1] + 1,
                       'md': b['md']})
        cursor = j + max(1, len(key))
    wins = []
    for i, w in enumerate(d['windows']):
        over = [p for p in placed if p['start'] < w['end_index'] and p['end'] > w['start_index']]
        wins.append({'window': i, 'label': w['label'], 'confidence': w['confidence'], 'ai_likelihood': w['ai_likelihood'],
                     'words': w['word_count'], 'start': w['start_index'], 'end': w['end_index'],
                     'is_humanized': w.get('is_humanized'), 'text': text[w['start_index']:w['end_index']],
                     'blocks': [p['block'] for p in over],
                     'sections': sorted({(p['h1'] or '-') + (' > ' + p['h2'] if p['h2'] else '') for p in over})})
    pathlib.Path(out_path).write_text(json.dumps({'placed_blocks': len(placed), 'para_blocks': sum(b['kind'] == 'para' for b in blocks),
                                                  'last_block_placed': placed[-1]['block'] if placed else None,
                                                  'windows': wins}, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print('blocks placed', len(placed), 'of', sum(b['kind'] == 'para' for b in blocks), '; last placed:', placed[-1]['h1'],
          '>', placed[-1]['h2'])
    for w in wins:
        light = w['label'] == 'Human' and (w['confidence'] == 'Low' or (w['confidence'] == 'Medium' and w['words'] >= 15))
        if w['label'] != 'Human' or light:
            print('%2d %-12s %-6s %4dw ai=%.2f %s| %s\n     %s' % (
                w['window'], w['label'], w['confidence'], w['words'], w['ai_likelihood'] or 0,
                'humanized ' if w['is_humanized'] else '', ' ; '.join(w['sections']) or '?',
                w['text'].strip().replace('\n', ' / ')[:240]))


if __name__ == '__main__':
    main(*sys.argv[1:3])
