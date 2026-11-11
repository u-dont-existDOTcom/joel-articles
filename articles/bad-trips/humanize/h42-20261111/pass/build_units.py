#!/usr/bin/env python3
"""build_units.py - the guide as it stands after round 33, section by section, as Pangram's web app reads it, for the
humanize pass that resumes now the guide makes sense (his rule of 2026-11-08 17:22 UTC: humanize only after that).

Each unit is a "##" section with its "###" subsections; a part's opening ("#" heading and the words before its first
"##") goes with that first section when it is short (under 40 words), and is a unit of its own otherwise. Text as the
lane's earlier section checks had it: headings as plain lines, links as their words, bold and italics marks out, list
items one per line, pictures, videos and dividers out, blocks joined by a blank line (`humanize/pangram-ledger.jsonl`,
e.g. "Appendix as the guide has it#317").

  python3 build_units.py      writes UNITS.json ([[key, text, sha256], ...], the page helpers' form) and units/*.txt
"""
import hashlib, json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parents[2]
BLOCKS = json.loads((ART / 'GUIDE-SO-FAR-blocks.json').read_text(encoding='utf-8'))
HIS = set(json.loads((ART / 'humanize/h41-20261109/boilerplate/HIS-OWN.json').read_text(encoding='utf-8')))
HIS |= {'R31-ALONE', 'R33-SMELL-L'} | {b['id'] for b in BLOCKS if b['id'].startswith(('N-', 'R27-', 'R30-OILS', 'R30-RUE'))}


def plain(md):
    t = re.sub(r'!\[[^\]]*\]\([^)]*\)', '', md)
    t = re.sub(r'\[([^\]]*)\]\(((?:[^()\s]|\([^()\s]*\))+)\)', r'\1', t)
    t = re.sub(r'<sub>(.*?)</sub>', r'\1', t)
    t = t.replace('**', '').replace('__', '')
    t = re.sub(r'(?<![\w*])\*(?!\s)([^*\n]+?)\*(?!\w)', r'\1', t)
    lines = []
    for l in t.split('\n'):
        l = re.sub(r'^\s*(?:[-*]|\d+\.)\s+', '', l)
        l = re.sub(r'^\s*>\s?', '', l)
        l = re.sub(r'^#+\s*', '', l)
        lines.append(l.rstrip())
    return '\n'.join(lines).strip()


units, cur, part_intro = [], None, None
for b in BLOCKS:
    k, md = b['kind'], b['md']
    if k in ('image', 'youtube', 'hr'):
        continue
    if k == 'h1':
        if part_intro is not None and len(part_intro['blocks']) > 1:   # a part with no "##" of its own is a unit
            units.append(part_intro)
        part_intro = {'title': plain(md), 'blocks': [b]}
        cur = None
        continue
    if k == 'h2':
        cur = {'title': plain(md), 'blocks': []}
        if part_intro is not None:
            words = sum(len(plain(x['md']).split()) for x in part_intro['blocks'][1:])
            if words >= 40:
                units.append(part_intro)
            else:
                cur['blocks'] += part_intro['blocks']
                cur['title'] = part_intro['title'] + ' / ' + cur['title']
            part_intro = None
        cur['blocks'].append(b)
        units.append(cur)
        continue
    if cur is None:
        if part_intro is None:
            part_intro = {'title': '(top)', 'blocks': []}
        part_intro['blocks'].append(b)
    else:
        cur['blocks'].append(b)
if part_intro is not None and len(part_intro['blocks']) > 1:
    units.append(part_intro)

# his rule for the web app (preferences): "a section check of about 5-6 paragraphs in the GUI is fine", so a longer unit
# is split, at its "###" headings first, then into runs of at most six paragraphs (a list counts one per three items)
def weight(b):
    if b['kind'] in ('ul', 'ol'):
        return max(1, -(-len([l for l in b['md'].split('\n') if l.strip()]) // 3))
    return 0 if b['kind'].startswith('h') else 1


def split(u):
    """Runs of at most about six paragraphs and at least 150 words: a new run starts at a "###" heading or after six
    paragraphs, once the run has 150 words; a last run under 100 words joins the one before."""
    nw = lambda bl: sum(len(plain(b['md']).split()) for b in bl if not b['kind'].startswith('h'))
    out, cur, w = [], [], 0
    for b in u['blocks']:
        if cur and nw(cur) >= 150 and ((b['kind'] == 'h3') or (weight(b) and w + weight(b) > 6)):
            out.append(cur); cur, w = [], 0
        cur.append(b); w += weight(b)
    if out and nw(cur) < 100:
        out[-1] += cur
    else:
        out.append(cur)
    if len(out) == 1:
        return [u]
    title = u['title']
    return [{'title': title + ' (%d of %d)' % (i + 1, len(out)), 'blocks': bl, 'parent': title} for i, bl in enumerate(out)]


units = [v for u in units for v in (split(u) if sum(weight(b) for b in u['blocks']) > 6 else [u])]
out, n = [], 0
(HERE / 'units').mkdir(exist_ok=True)
for u in units:
    text = '\n\n'.join(p for p in (plain(x['md']) for x in u['blocks']) if p)
    words = len(text.split())
    if words < 25:
        continue
    n += 1
    key = 'h42-%02d' % n
    his = sum(len(plain(x['md']).split()) for x in u['blocks'] if x['id'] in HIS)
    (HERE / 'units' / (key + '.txt')).write_text(text + '\n', encoding='utf-8')
    out.append({'key': key, 'title': u['title'], 'parent': u.get('parent', u['title']), 'words': words, 'his_share': round(his / words, 2),
                'blocks': [x['id'] for x in u['blocks']], 'sha256': hashlib.sha256(text.encode('utf-8')).hexdigest()})
(HERE / 'UNITS.json').write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
for u in out:
    print(u['key'], u['words'], u['his_share'], u['title'][:70])
print(len(out), 'units,', sum(u['words'] for u in out), 'words')
