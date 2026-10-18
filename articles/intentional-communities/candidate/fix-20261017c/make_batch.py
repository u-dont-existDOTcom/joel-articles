"""Batch 420g (2026-10-17, after Joel's message of 19:14 UTC, "i agree with your excl 13 14 ideas"): section 13 v35
(make_s13_v35.py). Every changed paragraph alone (50 words or more) and with each neighbor under its heading when one of the two
is under 50, and the whole section as 317g read it (fix-20261014/ptext.py's section()). Section 14 doesn't change.
The gate records need the march reads (march-r1/MARCH-labels-a.txt and -b.txt) and the cold read (SENSE-s13.md); without them
this prints the drafts only, for the predictions.
Run from candidate/: python3 fix-20261017c/make_batch.py"""
import hashlib, json, pathlib, re, subprocess, sys, tempfile

HERE = pathlib.Path(__file__).resolve().parent
C = HERE.parent
REPO = C.parents[2]
sys.path.insert(0, str(C / 'fix-20261014'))
sys.path.insert(0, str(HERE))
from ptext import plain, section  # noqa: E402
from make_s13_v35 import CHANGES  # noqa: E402

JOEL = 'Joel, 2026-10-17 19:14 UTC (joel-20261017/joel-20261017-1914-message.txt): '
H13 = '# Your Little Forming Group Already Is the Community'
_art = (C / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
_a = _art.index(H13)
_m = re.search(r'\n(<!-- CANDIDATE|<!-- ACCEPTED|<!-- Section|# )', _art[_a + 3:])
_b = _a + 3 + _m.start()
if (C / 's13' / 'v35.md').read_text(encoding='utf-8').strip() in _art:   # after the install, the article is the text
    NEW = _art
else:
    NEW = _art[:_a] + (C / 's13' / 'v35.md').read_text(encoding='utf-8').strip() + '\n' + _art[_b:]
(HERE / 'article-with-s13v35.md').write_text(NEW, encoding='utf-8')
SKIP = re.compile(r'^(\[image \d+\]|<!--)')
SHORT = {'Please Choose the Values Before Falling in Love With the View': 'Values', 'Resources, Land, and Exit Terms': 'Resources',
         'From Visitor to Member—Slowly': 'Visitor to Member', 'When Somebody Has to Go': 'When Somebody Has to Go'}


def block(md, h1):
    a = md.index(h1)
    m = re.search(r'\n(<!-- CANDIDATE|<!-- ACCEPTED|<!-- Section|# )', md[a + 3:])
    return md[a:(a + 3 + m.start()) if m else len(md)]


def paras(md):
    """(heading index, subsection name, number under it, plain text, Markdown) for every paragraph."""
    out, h, name, n = [], 0, 'Opening', 0
    for b in [b.strip() for b in re.split(r'\n\s*\n', re.sub(r'<!--.*?-->', '', md, flags=re.S)) if b.strip()]:
        if b.startswith('#'):
            h += 1
            if b.startswith('## '):
                name, n = SHORT[b[3:].strip()], 0
        elif not SKIP.match(b) and not b.startswith('[caption]'):
            n += 1
            out.append((h, name, n, plain(b), b))
    return out


def lint(md_text):
    with tempfile.NamedTemporaryFile('w', suffix='.md', delete=False, encoding='utf-8') as f:
        f.write(md_text + '\n')
    # with the installed article: its sentences passed already and get no flags; only what the edit makes new is judged, the
    # way pangram_gate.py --lint-article runs it (E179)
    r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'tells_lint.py'), f.name, '--style',
                        str(C.parent / 'STYLE.json'), '--installed', str(C / 'HUMANIZED-SO-FAR.md')], capture_output=True, text=True)
    return re.search(r'verdict: (\w+)', r.stdout).group(1)


def labels(folder):
    if not (folder / 'MARCH-labels-a.txt').exists():
        return None
    ids = json.loads((folder / 'march-ids.json').read_text())
    L = [dict(re.findall(r'^\s*T(\d+):\s*([SB ]+?)\s*$', (folder / ('MARCH-labels-%s.txt' % x)).read_text(), re.M)) for x in 'ab']
    return {k: [m[str(i + 1)] for m in L] for i, k in enumerate(ids)}


MARCH = labels(HERE / 'march-r1')
COLD = json.loads((HERE / 'cold.json').read_text()) if (HERE / 'cold.json').exists() else None
sec = block(NEW, H13)
hp = paras(sec)
drafts, gate = {}, {}
WHY = {}
for where, kind, old, new, why in CHANGES:
    WHY.setdefault(where, []).append(('the mark only' if kind == 'period' else 'the phrase out') + ': ' + why)
for where, whys in WHY.items():
    i = next(k for k, (_, nm, n, _, _) in enumerate(hp) if '%s P%d' % (nm, n) == where)
    key = 'S13v35-' + where.replace(' ', '')
    mid = 's13-' + where.replace(' ', '')
    rec = {'kind': 'edit', 'was': 'batch 317g: section 13 v34 100% Human',
           'grounding': 'OK', 'grounding_note': 'no claim of mine: his 48, the exclamations list (fix-20261017b/excl-13-14.md): '
                                                 + '; '.join(whys) + ' (fix-20261017c/excl-changes-13.json)',
           'stance': 0, 'stance_note': 'a mark or a filler phrase out; no position added', 'missing': [],
           'joel_note': JOEL + '"i agree with your excl 13 14 ideas"'}
    if MARCH:
        rec.update(march_was=MARCH[mid + '-was'], march=MARCH[mid + '-new'],
                   march_note='fix-20261017c/march-r1 (%s-was and %s-new)' % (mid, mid))
    if COLD:
        rec.update(cold=COLD['s13'][0], cold_note=COLD['s13'][1])
    ps = [p for _, _, _, p, _ in hp]
    if len(ps[i].split()) >= 50:
        drafts[key] = ps[i]
        gate[key] = dict(rec, lint=lint(hp[i][4]), words=len(ps[i].split()))
    for j in (i - 1, i + 1):
        if 0 <= j < len(ps) and hp[j][0] == hp[i][0] and min(len(ps[i].split()), len(ps[j].split())) < 50:
            a, b = sorted((i, j))
            k = '%s+%s' % (key, 'prev' if j < i else 'next')
            drafts[k] = ps[a] + '\n\n' + ps[b]
            gate[k] = dict(rec, lint=lint(hp[i][4]), words=len(drafts[k].split()))
drafts['S13v35'] = section(NEW, H13)
gate['S13v35'] = {'kind': 'section', 'parts': ['installed'] + sorted(k for k in gate if k.startswith('S13v35-')), 'repeats': 0,
                  'repeats_note': 'fix-20261017c/DISPOSITIONS.md: exclamation marks and three filler phrases out; nothing added',
                  'words': len(drafts['S13v35'].split())}
seen, aliases = {}, {}
for k in list(drafts):
    if drafts[k] in seen:
        aliases[k] = seen[drafts[k]]
        del drafts[k]
    else:
        seen[drafts[k]] = k
for k in drafts:
    print(k, gate[k]['words'], gate[k].get('lint'), '|', drafts[k][:70].replace('\n', ' / '))
print('aliases:', aliases)
print(len(drafts), 'items,', sum(gate[k]['words'] for k in drafts), 'words')
if MARCH and COLD:
    out = HERE / 'b420'
    out.mkdir(exist_ok=True)
    (out / 'aliases.json').write_text(json.dumps(aliases, indent=1) + '\n', encoding='utf-8')
    (out / 'drafts.json').write_text(json.dumps(drafts, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    (out / 'GATE.json').write_text(json.dumps(gate, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'pangram_gate.py'), str(out / 'drafts.json'),
                        str(out / 'GATE.json'), str(out / 'b420.js'), '--name', 'B420', '--lint-article',
                        str(C / 'HUMANIZED-SO-FAR.md')] + list(drafts), capture_output=True, text=True)
    print(r.stdout[-2500:], r.stderr[-2500:])
    items = [[k, t, hashlib.sha256(t.encode('utf-8')).hexdigest()] for k, t in drafts.items()]
    (out / 'b420-items.json').write_text(json.dumps(items, ensure_ascii=False), encoding='utf-8')
