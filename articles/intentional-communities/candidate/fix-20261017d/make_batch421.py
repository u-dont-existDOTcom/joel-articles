"""Batch 421g (2026-10-17, after Joel's message of 21:37 UTC): his texts and his line decisions (make_2137.py), each changed
paragraph alone (50 words or more) and with each neighbor under its heading when one of the two is under 50, each heading whose
first paragraph changed with that paragraph, and every changed section whole, in the text format its last check used (sections
2, 8 and 12: fix-20261014/ptext.py's section(); sections 15 and 16: their own batches' format, images and embeds out, captions
in, headings without their marks). Everything here is his words or his decision, so each part is an owner record with his words
from the message; the sections need their repeats checks (REPEATS-sN.md). Run from candidate/: python3 fix-20261017d/make_batch421.py"""
import hashlib, json, pathlib, re, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
C = HERE.parent
REPO = C.parents[2]
sys.path.insert(0, str(C / 'fix-20261014'))
from ptext import plain, section  # noqa: E402

JOEL = 'Joel, 2026-10-17 21:37 UTC (joel-20261017/joel-20261017-2137-message.txt): '
NEW = (HERE / 'article-with-drafts.md').read_text(encoding='utf-8')
SKIP = re.compile(r'^(\[image \d+\]|\[Professor Baby Sheep|Double click to interact with video|<!--)')
H2 = '# Communes Are Hot Again'
H8 = '# The Grown Children Get the Final Review'
H12 = '# The Math of Absorption, and Who This Isn’t For'
H15 = '# What This Looks Like From Sénégal'
H16 = '# Practice Comes Before Property'


def own_whole(md):
    out = []
    for b in [b.strip() for b in re.split(r'\n\s*\n', re.sub(r'<!--.*?-->', '', md, flags=re.S)) if b.strip()]:
        if SKIP.match(b):
            continue
        if b.startswith('[caption]'):
            b = re.sub(r'^\[caption\]\s*', '', b)
        out.append(plain(b.lstrip('#').strip()))
    return '\n\n'.join(out)


assert own_whole((C / 's15' / 'v14.md').read_text(encoding='utf-8')) == json.loads(
    (C / 'fix-20261017b' / 'b417' / 'drafts.json').read_text())['S15v14b']
assert own_whole((C / 's16' / 'v29.md').read_text(encoding='utf-8')) == json.loads(
    (C / 'fix-20261017b' / 'b419' / 'drafts.json').read_text())['S16-e']


def block(md, h1):
    a = md.index(h1)
    m = re.search(r'\n(<!-- CANDIDATE|<!-- ACCEPTED|<!-- Section|# )', md[a + 3:])
    return md[a:(a + 3 + m.start()) if m else len(md)]


def paras(md):
    out, h = [], 0
    for b in [b.strip() for b in re.split(r'\n\s*\n', re.sub(r'<!--.*?-->', '', md, flags=re.S)) if b.strip()]:
        if b.startswith('#'):
            h += 1
            out.append((h, None, b))
        elif not SKIP.match(b) and not b.startswith('[caption]'):
            out.append((h, plain(b), b))
    return out


drafts, gate = {}, {}


def checks(name, sec_md, starts, joel):
    hp = [x for x in paras(sec_md)]
    i = next(k for k, (_, p, _) in enumerate(hp) if p and p.startswith(starts))
    rec = {'kind': 'owner', 'joel': JOEL + joel}
    ps = [p for _, p, _ in hp]
    if len(ps[i].split()) >= 50:
        drafts[name] = ps[i]; gate[name] = dict(rec)
    for j in (i - 1, i + 1):
        if not (0 <= j < len(hp)) or hp[j][0] != hp[i][0]:
            continue
        if ps[j] is None:   # the heading over it, when the two reach Pangram's 50 words
            t = plain(hp[j][2].lstrip('#').strip()) + '\n\n' + ps[i]
            if len(t.split()) >= 50:
                drafts[name + '+head'] = t; gate[name + '+head'] = dict(rec)
        elif min(len(ps[i].split()), len(ps[j].split())) < 50:
            a, b = sorted((i, j))
            k = '%s+%s' % (name, 'prev' if j < i else 'next')
            drafts[k] = ps[a] + '\n\n' + ps[b]; gate[k] = dict(rec)


checks('S2v34-P2', block(NEW, H2), 'Whether you want to call that loneliness',
       '47.5 "here\'s my fixed version, reads human to apngram" (his P2, "Genevia" spelled "Geneva"), and 46 a (the anomie paragraph '
       'after it: "This paragraph there, with your screenshot and caption after it")')
checks('S2v34-A46', block(NEW, H2), "What's starving them is anomie", '46 a (the anomie paragraph of question 46, his pick)')
checks('S8v31-rumspringa', block(NEW, H8), 'Amish young people', '49 "yes fix rumspringa age"')
checks('S8v31-skills', block(NEW, H8), 'Kids also need transferable skills', '49 "yes put punishing departure back"')
s15 = (C / 's15' / 'v15.md').read_text(encoding='utf-8')
checks('S15v15-H2P1', s15, 'But does this mean I think', '47.4 "i reworded the whole thing and it\'s better and human now" (his P1)')
checks('S15v15-H2P2', s15, 'Sénégal passed a law in March 2026', '47.4 (his P2; the published law link kept on "March 2026")')
s16 = (C / 's16' / 'v30.md').read_text(encoding='utf-8')
checks('S16v30-H3P2', s16, 'Find two or three other people', '47.1 "remove one is enough"')
REP = {}
for k in ('s2', 's8', 's15'):
    f = HERE / ('REPEATS-%s.md' % k)
    REP[k] = f.read_text(encoding='utf-8') if f.exists() else None
drafts['S2v34'] = section(NEW, H2)
drafts['S8v31'] = section(NEW, H8)
drafts['S12v16'] = section(NEW, H12)
drafts['S15v15'] = own_whole(s15)
drafts['S16v30'] = own_whole(s16)
NOTE = {'S2v34': 'fix-20261017d/DISPOSITIONS.md (REPEATS-s2.md)', 'S8v31': 'fix-20261017d/DISPOSITIONS.md (REPEATS-s8.md)',
        'S15v15': 'fix-20261017d/DISPOSITIONS.md (REPEATS-s15.md)', 'S12v16': 'nothing added: the screenshot and its caption moved out',
        'S16v30': 'nothing added: his cut of "One disagreement is enough!"'}
for key in ('S2v34', 'S8v31', 'S12v16', 'S15v15', 'S16v30'):
    gate[key] = {'kind': 'section', 'parts': ['installed'] + sorted(k for k in gate if k.startswith(key + '-')), 'repeats': 0,
                 'repeats_note': NOTE[key]}
for k in gate:
    gate[k]['words'] = len(drafts[k].split())
seen, aliases = {}, {}
for k in list(drafts):
    if drafts[k] in seen:
        aliases[k] = seen[drafts[k]]; del drafts[k]
    else:
        seen[drafts[k]] = k
for k in drafts:
    print(k, gate[k]['words'], gate[k]['kind'], '|', drafts[k][:70].replace('\n', ' / '))
print('aliases:', aliases)
print(len(drafts), 'items,', sum(gate[k]['words'] for k in drafts), 'words')
if all(REP.values()):
    out = HERE / 'b421'
    out.mkdir(exist_ok=True)
    (out / 'aliases.json').write_text(json.dumps(aliases, indent=1) + '\n', encoding='utf-8')
    (out / 'drafts.json').write_text(json.dumps(drafts, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    (out / 'GATE.json').write_text(json.dumps(gate, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'pangram_gate.py'), str(out / 'drafts.json'),
                        str(out / 'GATE.json'), str(out / 'b421.js'), '--name', 'B421'] + list(drafts), capture_output=True, text=True)
    print(r.stdout[-1800:], r.stderr[-1500:])
    items = [[k, t, hashlib.sha256(t.encode('utf-8')).hexdigest()] for k, t in drafts.items()]
    (out / 'b421-items.json').write_text(json.dumps(items, ensure_ascii=False), encoding='utf-8')
else:
    print('waiting for the repeats checks:', [k for k, v in REP.items() if not v])
