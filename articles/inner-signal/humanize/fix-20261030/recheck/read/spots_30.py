"""SPOTS.json and SPOTS.md for the recheck of 30 October: how each thing that changed since batch 483's recheck read in
place, and the red on words nobody changed; and HIS-30.md (every paragraph of the master that is his own words, for
window_confidence.py --his).

What changed (the two masters diffed paragraph by paragraph, as ../make_changed.py does): his versions of 30 October
(and the cards he approved), my fixes from the full read (../../fullread/APPLIED-FULLREAD.json), my four suggestions for
his words (../SUGGESTIONS.json), and Appendix C's rewritten list. A spot's reading is its worst window: any AI window
over its words makes it AI (with that window's confidence); otherwise the lowest confidence of the Human windows over it.

  python3 articles/inner-signal/humanize/fix-20261030/recheck/read/spots_30.py
"""
import difflib
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
X = HERE.parent
H = X.parents[1]
ROOT = H.parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import compare_read as cr  # noqa: E402
import suggestion_review as sr  # noqa: E402

FLAT = str.maketrans({'“': '"', '”': '"', '‘': "'", '’': "'"})
OLD_MASTER = H / 'fix-20261029' / 'b483' / 'CANDIDATE-MASTER.md'
ORDER = {'Low': 0, 'Medium': 1, 'High': 2}


def find(text, s):
    ft, fs = text.translate(FLAT), s.translate(FLAT).strip()
    if fs and ft.count(fs) == 1:
        k = ft.find(fs)
        return k, k + len(fs)
    return None


def reading(result, a, b):
    ws = [(i, w) for i, w in enumerate(result['windows']) if w['start_index'] < b and w['end_index'] > a]
    ai = [(i, w) for i, w in ws if w['label'].startswith('AI')]
    if ai:
        worst = max(ai, key=lambda iw: ORDER.get(iw[1]['confidence'], 0))
        return 'AI (%s)' % worst[1]['confidence'], [i + 1 for i, _ in ai]
    low = min(ws, key=lambda iw: ORDER.get(iw[1]['confidence'], 0))[1]['confidence'] if ws else None
    return ('Human (%s)' % low) if low else 'not read', []


def main():
    cfg = json.loads((H / 'COMPARE-GATE.json').read_text(encoding='utf-8'))
    mine_texts = cr.owner_paragraphs(cfg['owner'], str(ROOT))
    old = [b['text'] for b in sr.blocks(OLD_MASTER.read_text(encoding='utf-8')) if not b['level']]
    new_bl = [b for b in sr.blocks((X / 'CANDIDATE-MASTER.md').read_text(encoding='utf-8')) if not b['level']]
    new = [b['text'] for b in new_bl]
    answers = json.loads((H / 'fix-20261029' / 'b483' / 'review' / 'ANSWERS-20261030-1435.json').read_text(encoding='utf-8'))
    his30 = {x['id']: cr.loose(x.get('your_version') or '') for x in answers['items'] if x.get('status') == 'revise'}
    approved = {x['id'] for x in answers['items'] if x.get('status') == 'approved'}
    sugg = {s['suggestion']: s['id'] for s in json.loads((X / 'SUGGESTIONS.json').read_text(encoding='utf-8'))['suggestions']
            if s['in_recheck']}
    fixed = json.loads((H / 'fix-20261030' / 'fullread' / 'APPLIED-FULLREAD.json').read_text(encoding='utf-8'))
    fix_of = {}
    for c in fixed['changed']:
        for p in c['after'].split('\n\n'):
            if p.strip():
                fix_of[cr.loose(sr.blocks(p)[0]['text'])] = (c['block'], c['findings'])
    texts = {'A': (X / 'TEXT-A.txt').read_text(encoding='utf-8'), 'B': (X / 'RENDERED-B.txt').read_text(encoding='utf-8')}
    results = {p: json.loads((HERE / ('RESULT-%s.json' % p)).read_text(encoding='utf-8')) for p in 'AB'}
    sm = difflib.SequenceMatcher(a=old, b=new, autojunk=False)
    spots, covered = [], {'A': [], 'B': []}
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == 'equal':
            continue
        for j in range(j1, j2):
            t = new[j]
            if len(t.split()) < 3:
                continue
            lt = cr.loose(t)
            hid = next((k for k, v in his30.items() if lt in v or cr.is_his(lt, [v])), None)
            if hid:
                kind, who = 'his version (%s)' % hid, 'his'
            elif t in sugg:
                kind, who = 'my suggestion for his words (%s)' % sugg[t], 'suggestion'
            elif lt in fix_of:
                blk, fids = fix_of[lt]
                kind, who = 'my fix (%s)' % ', '.join(fids), 'fix'
            else:
                kind, who = 'a card he approved, or his words moved', 'other'
            for part in 'AB':
                loc = find(texts[part], t)
                if not loc:
                    continue
                r, ai = reading(results[part], *loc)
                covered[part].append(loc)
                spots.append({'part': part, 'kind': kind, 'who': who, 'where': sr.where(new_bl, j) if False else
                              new_bl[j]['section'], 'reading': r, 'ai_windows': ai, 'text': t})
    elsewhere = []
    for part in 'AB':
        res = results[part]
        for i, w in enumerate(res['windows']):
            if not w['label'].startswith('AI'):
                continue
            a, b = w['start_index'], w['end_index']
            if any(x < b and y > a for x, y in covered[part]):
                continue
            seg = res['text'][a:b].strip()
            his = cr.is_his(cr.loose(seg), mine_texts) or any(cr.loose(seg) in m for m in mine_texts)
            elsewhere.append({'part': part, 'window': i + 1, 'reading': '%s (%s)' % (w['label'], w['confidence']),
                              'words': w['word_count'], 'his': his, 'text': seg})
    out = {'spots': spots, 'red_elsewhere': elsewhere}
    (HERE / 'SPOTS.json').write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    lines = ['# The recheck of 30 October: what changed, and how it read in place', '']
    for who, title in (('his', 'His versions of 30 October'), ('suggestion', 'My suggestions for his words'),
                       ('fix', 'My fixes from the full read'), ('other', 'Other changes')):
        group = [s for s in spots if s['who'] == who]
        if not group:
            continue
        ok = sum(s['reading'] == 'Human (High)' for s in group)
        lines += ['## %s: %d of %d read Human (High)' % (title, ok, len(group)), '']
        for s in group:
            if s['reading'] == 'Human (High)' and who == 'fix':
                continue
            lines.append('- **%s** (part %s, %s; %s): %s' % (s['reading'], s['part'], s['where'], s['kind'],
                                                              s['text'][:220] + ('...' if len(s['text']) > 220 else '')))
        lines.append('')
    lines += ['## Red on words nobody changed since the last check', '']
    for e in elsewhere:
        lines.append('- **%s**, part %s window %d, %d words%s: %s' % (e['reading'], e['part'], e['window'], e['words'],
                                                                    ' (his words)' if e['his'] else '',
                                                                    e['text'][:260].replace('\n', ' / ')))
    (HERE / 'SPOTS.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')
    his_paras = [b['text'] for b in new_bl if cr.is_his(cr.loose(b['text']), mine_texts)]
    (HERE / 'HIS-30.md').write_text('# His own words in the master of 30 October (every paragraph the comparison gate '
                                    'counts as his), for window_confidence.py --his\n\n' + '\n\n'.join(his_paras) + '\n',
                                    encoding='utf-8')
    for who in ('his', 'suggestion', 'fix', 'other'):
        g = [s for s in spots if s['who'] == who]
        print(who, len(g), {r: sum(s['reading'] == r for s in g) for r in sorted({s['reading'] for s in g})})
    print('red elsewhere', len(elsewhere))


if __name__ == '__main__':
    main()
