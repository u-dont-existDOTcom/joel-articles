"""CHANGED-A.json and CHANGED-B.json for the recheck of 30 October (part_forecast.py make), written before the paste.

The last check is batch 483's recheck (../../fix-20261029/b483/recheck/read/RESULT-A.json and RESULT-B.json, of
b483/CANDIDATE-MASTER.md). What changed since, paragraph by paragraph (the two masters diffed): Joel's answers of 14:35
UTC (his own versions, and the cards he approved), the fixes from my full read, and my four suggestions for his words. My
chance that each reads red, by one stated rule:
- his own version: 0.25 where he said it passes on its own ("passes pangram alone", "100% high conf human"), 0.3 for the
  audit (he made the whole of it pass), 0.45 for the rest (nobody has checked them in place);
- an approved card or one of my fixes: by how its words read last time and how much changed. A small fix (three words or
  fewer: a comma, a word): AI 0.55, Human Low 0.1, Medium 0.05, High 0.03 (an unchanged Low window turned red 4 times
  in 75, part_forecast.py). A bigger one: AI 0.6, Low 0.3, Medium 0.2, High 0.15; plus 0.15 where the fix brings back
  words (a lost point restored), and 0.5 for Appendix C's rewritten list;
- a suggestion for his words: 0.35.
A window that read AI last time and whose words are unchanged: 0.6. part_forecast.py adds the neighbours and the windows
that read Human at Low or Medium last time.

  python3 articles/inner-signal/humanize/fix-20261030/recheck/make_changed.py
"""
import difflib
import json
import pathlib
import sys

X = pathlib.Path(__file__).resolve().parent
H = X.parents[1]
ROOT = H.parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import compare_read as cr  # noqa: E402
import suggestion_review as sr  # noqa: E402

LAST = H / 'fix-20261029' / 'b483' / 'recheck' / 'read'
OLD_MASTER = H / 'fix-20261029' / 'b483' / 'CANDIDATE-MASTER.md'
FLAT = str.maketrans({'“': '"', '”': '"', '‘': "'", '’': "'"})
PASSES_ALONE = ('R-237', 'R-238', 'N-243', 'N-276', 'R-289', 'R-509', 'R-755')
RESTORED = {11, 35, 80, 99, 172, 337, 339, 345, 353, 362, 365, 505, 507, 588}   # read/record_fixes_read.py's NOTES
P601 = 'check how it’s trying to get you there'


def find(text, s):
    """Where S (its words, quotes flattened) is in TEXT, once; else where its first 100 characters are."""
    ft = text.translate(FLAT)
    for probe in (s, s[:100]):
        fs = probe.translate(FLAT).strip()
        if fs and ft.count(fs) == 1:
            k = ft.find(fs)
            return k, k + (len(fs) if probe is s else len(s.translate(FLAT).strip()))
    return None


def last_reading(result, old):
    """How the words OLD read in the last check: 'AI' if any window over them read AI, else the lowest confidence."""
    loc = find(result['text'], old) if old else None
    if not loc:
        return None
    a, b = loc
    ws = [w for w in result['windows'] if w['start_index'] < b and w['end_index'] > a]
    if any(str(w['label']).startswith('AI') for w in ws):
        return 'AI'
    order = {'Low': 0, 'Medium': 1, 'High': 2}
    return min((w.get('confidence') for w in ws), key=lambda c: order.get(c, 0), default=None)


def main():
    old = [b['text'] for b in sr.blocks(OLD_MASTER.read_text(encoding='utf-8')) if not b['level']]
    new_bl = [b for b in sr.blocks((X / 'CANDIDATE-MASTER.md').read_text(encoding='utf-8')) if not b['level']]
    new = [b['text'] for b in new_bl]
    answers = json.loads((H / 'fix-20261029' / 'b483' / 'review' / 'ANSWERS-20261030-1435.json').read_text(encoding='utf-8'))
    his = {x['id']: cr.loose(x.get('your_version') or '') for x in answers['items'] if x.get('status') == 'revise'}
    sugg = {s['suggestion'] for s in json.loads((X / 'SUGGESTIONS.json').read_text(encoding='utf-8'))['suggestions']
            if s['in_recheck']}
    fixed = json.loads((H / 'fix-20261030' / 'fullread' / 'APPLIED-FULLREAD.json').read_text(encoding='utf-8'))
    fix_after = {}
    for c in fixed['changed']:
        for p in c['after'].split('\n\n'):
            fix_after[cr.loose(sr.blocks(p)[0]['text'] if p.strip() else '')] = c['block']
    changed = []
    sm = difflib.SequenceMatcher(a=old, b=new, autojunk=False)
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == 'equal':
            continue
        for j in range(j1, j2):
            o = old[i1 + (j - j1)] if i1 + (j - j1) < i2 else ''
            changed.append((new[j], o))
    for part in ('A', 'B'):
        text = (X / ('TEXT-%s.txt' % part)).read_text(encoding='utf-8')
        result = json.loads((LAST / ('RESULT-%s.json' % part)).read_text(encoding='utf-8'))
        out, taken = [], []
        for t, o in changed:
            loc = find(text, t)
            if not loc or len(t.split()) < 3:
                continue
            seg = text[loc[0]:loc[1]]
            lt = cr.loose(t)
            reading = last_reading(result, o)
            hid = next((k for k, v in his.items() if lt in v), None)
            if hid:
                red = 0.25 if hid in PASSES_ALONE else (0.3 if hid == 'R-audit' else 0.45)
                why = 'his own version (%s)%s' % (hid, ', which he said passes on its own' if hid in PASSES_ALONE else '')
            elif t in sugg:
                red, why = 0.35, 'my suggestion for his words'
            else:
                ow, nw = o.split(), t.split()
                same = sum(m.size for m in difflib.SequenceMatcher(a=ow, b=nw, autojunk=False).get_matching_blocks())
                small = o and max(len(ow), len(nw)) - same <= 3
                red = ({'AI': 0.55, 'Low': 0.1, 'Medium': 0.05, 'High': 0.03} if small else
                       {'AI': 0.6, 'Low': 0.3, 'Medium': 0.2, 'High': 0.15}).get(reading, 0.3)
                blk = fix_after.get(lt)
                if P601 in t:
                    red = 0.5
                elif blk in RESTORED:
                    red = min(0.75, red + 0.15)
                why = ('my fix (block %s)' % blk) if blk is not None else 'a card he approved'
            out.append({'name': t[:60].rstrip() + '...', 'text': seg, 'chance_red': round(red, 2), 'chance_high': 0.2,
                        'why': '%s; its words read %s last time' % (why, reading or 'nowhere (new)'), 'kind': 'changed'})
            taken.append(loc)
        # what read AI last time, unchanged
        for w in result['windows']:
            if not str(w['label']).startswith('AI'):
                continue
            seg = result['text'][w['start_index']:w['end_index']].strip()
            loc = find(text, seg)
            if not loc or any(a < loc[1] and b > loc[0] for a, b in taken):
                continue
            taken.append(loc)
            out.append({'name': 'kept red: ' + seg[:44].rstrip() + '...', 'text': text[loc[0]:loc[1]], 'chance_red': 0.6,
                        'chance_high': 0.1, 'why': 'unchanged; read %s (%s) last time' % (w['label'], w.get('confidence')),
                        'kind': 'changed'})
        (X / ('CHANGED-%s.json' % part)).write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
        print(part, len(out), 'parts', round(sum(c['chance_red'] for c in out), 1), 'expected red among them')


if __name__ == '__main__':
    main()
