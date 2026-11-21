#!/usr/bin/env python3
"""collect_new.py - his fixes since the 2026-11-12 collection (humanize/h46-20261112/his-fixes/collect.py, same rules):
every item of a review page's answers whose "your_version" differs from the text the card showed, from answers files
saved after 2026-11-12 14:45 UTC, for the reading quiz he suggested on 2026-11-21 15:57 UTC ("we should do some quizes
for you without pangram first maybe").

Writes NEW-PAIRS.json beside it.   python3 collect_new.py
"""
import difflib, glob, json, pathlib, re
HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[4]


def words(t):
    return re.findall(r"[A-Za-z0-9'’]+", t.lower())


def stamp(f):
    m = re.search(r'(\d{8})-(\d{4})', pathlib.Path(f).name)
    return m.group(1) + m.group(2) if m else ''


pairs = []
for f in sorted(glob.glob(str(REPO / 'articles/**/ANSWERS*.json'), recursive=True)):
    if stamp(f) <= '202611121445':
        continue
    try:
        d = json.loads(pathlib.Path(f).read_text(encoding='utf-8'))
    except Exception:
        continue
    for it in (d.get('items') or []) if isinstance(d, dict) else []:
        his = (it.get('your_version') or '').strip()
        before = (it.get('my_version') or it.get('before') or '').strip()
        if not his or not before or his == before:
            continue
        a, b = words(before), words(his)
        sim = difflib.SequenceMatcher(None, a, b, autojunk=False).ratio() if a and b else 0.0
        pairs.append({'lane': str(pathlib.Path(f).relative_to(REPO)).split('/')[1], 'file': str(pathlib.Path(f).relative_to(REPO)),
                      'id': it.get('id'), 'type': it.get('type'), 'whose': it.get('whose'), 'title': it.get('title'),
                      'before': before, 'his': his, 'comment': (it.get('comment') or '').strip(),
                      'words_before': len(a), 'words_his': len(b), 'shared': round(sim, 2)})
(HERE / 'NEW-PAIRS.json').write_text(json.dumps(pairs, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print(len(pairs), 'pairs')
for p in pairs:
    print(p['file'].split('/')[-1][:32], p['id'], p['type'], p['whose'], p['words_before'], p['words_his'], p['shared'])
