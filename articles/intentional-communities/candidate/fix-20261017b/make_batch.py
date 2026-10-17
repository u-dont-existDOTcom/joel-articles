"""Batch 415g (2026-10-17, after Joel's message of 17:16 UTC): every paragraph this turn changes, alone (50 words or more) or
with each neighbor under its heading, and every changed section whole; the appendix goes in 416g (appendix/apx_batch.py).
- Section 12 v15: his P2 as written with his caption after it (owner), and the section.
- Section 2 v3.3 (P2's "starving") and section 9 v17 (the published "I'm not claiming the Zapatistas already proved my whole
  model."): edits, and the sections.
- Sections 15 v14 and 16 v29: the exclamations his way (make_excl.py) and the faithfulness fixes (make_faithful.py): edits,
  and the sections.
- Screens, never installed: the anomie paragraph (question 46) alone, with the next paragraph, and in its section.
Each whole section is the text Pangram read for it before: sections 15 and 16 as their own batches built them (images and
embeds out, captions in, headings without their marks), the others as fix-20261014/ptext.py builds them.
Run from candidate/: python3 fix-20261017b/make_batch.py"""
import hashlib, json, pathlib, re, subprocess, sys, tempfile

HERE = pathlib.Path(__file__).resolve().parent
C = HERE.parent
REPO = C.parents[2]
sys.path.insert(0, str(C / 'fix-20261014'))
from ptext import plain, section  # noqa: E402

JOEL = 'Joel, 2026-10-17 17:16 UTC (joel-20261017/joel-20261017-1716-message.txt): '
SKIP = re.compile(r'^(\[image \d+\]|\[Professor Baby Sheep|Double click to interact with video|<!--)')
NOW = (C / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
NEW = (HERE / 'article-with-drafts.md').read_text(encoding='utf-8')
ANOM = (HERE / 'anomie' / 'article-with-anomie.md').read_text(encoding='utf-8')


def own_whole(md):
    out = []
    for b in [b.strip() for b in re.split(r'\n\s*\n', re.sub(r'<!--.*?-->', '', md, flags=re.S)) if b.strip()]:
        if SKIP.match(b):
            continue
        if b.startswith('[caption]'):
            b = re.sub(r'^\[caption\]\s*', '', b)
        out.append(plain(b.lstrip('#').strip()))
    return '\n\n'.join(out)


assert own_whole((C / 's15' / 'v13.md').read_text(encoding='utf-8')) == json.loads(
    (C / 'fix-20261017' / 'b412' / 'drafts.json').read_text())['S15v13']
assert own_whole((C / 's16' / 'v28.md').read_text(encoding='utf-8')) == json.loads(
    (C / 'fix-20261017' / 'b413' / 'drafts.json').read_text())['S16v28']


def paras(md):
    out, h = [], 0
    for b in [b.strip() for b in re.split(r'\n\s*\n', re.sub(r'<!--.*?-->', '', md, flags=re.S)) if b.strip()]:
        if b.startswith('#'):
            h += 1
        elif not SKIP.match(b) and not b.startswith('[caption]'):
            out.append((h, plain(b), b))
    return out


def lint(md_text):
    with tempfile.NamedTemporaryFile('w', suffix='.md', delete=False, encoding='utf-8') as f:
        f.write(md_text + '\n')
    r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'tells_lint.py'), f.name, '--style',
                        str(C.parent / 'STYLE.json')], capture_output=True, text=True)
    return re.search(r'verdict: (\w+)', r.stdout).group(1)


def labels(folder, name='MARCH-labels-%s.txt'):
    ids = json.loads((folder / 'march-ids.json').read_text())
    L = [dict(re.findall(r'^\s*T(\d+):\s*([SB ]+?)\s*$', (folder / (name % x)).read_text(), re.M)) for x in 'ab']
    return {k: [m[str(i + 1)] for m in L] for i, k in enumerate(ids)}


M1, M2, M3 = labels(HERE / 'march-r1'), labels(HERE / 'march-r2'), labels(HERE / 'march-r3')
MA = [dict(re.findall(r'^\s*T(\d+):\s*([SB ]+?)\s*$', (HERE / 'anomie' / ('MARCH-v2-labels-%s.txt' % x)).read_text(), re.M)) for x in 'ab']
MALT = [dict(re.findall(r'^\s*T(\d+):\s*([SB ]+?)\s*$', (HERE / ('MARCH-alt-labels-%s.txt' % x)).read_text(), re.M)) for x in 'ab']
drafts, gate = {}, {}


def sect_text(md, h1, own=False):
    if not own:
        return section(md, h1)
    a = md.index(h1)
    m = re.search(r'\n(<!-- CANDIDATE|<!-- ACCEPTED|<!-- Section|# )', md[a + 3:])
    return own_whole(md[a:a + 3 + m.start()])


def checks(name, sec_md, starts, rec):
    """The paragraph that starts with STARTS, alone when 50 words or more, and with each neighbor under its heading when one
    of the two is under 50."""
    hp = paras(sec_md)
    i = next(k for k, (_, p, _) in enumerate(hp) if p.startswith(starts))
    ps = [p for _, p, _ in hp]
    if len(ps[i].split()) >= 50:
        drafts[name] = ps[i]; gate[name] = dict(rec, lint=lint(hp[i][2]), words=len(ps[i].split()))
    for j in (i - 1, i + 1):
        if 0 <= j < len(ps) and hp[j][0] == hp[i][0] and min(len(ps[i].split()), len(ps[j].split())) < 50:
            a, b = sorted((i, j))
            k = '%s+%s' % (name, 'prev' if j < i else 'next')
            drafts[k] = ps[a] + '\n\n' + ps[b]
            gate[k] = dict(rec, lint=lint(hp[i][2]), words=len(drafts[k].split()))
    return [k for k in drafts if k == name or k.startswith(name + '+')]


def block(md, h1):
    a = md.index(h1)
    m = re.search(r'\n(<!-- CANDIDATE|<!-- ACCEPTED|<!-- Section|# )', md[a + 3:])
    return md[a:(a + 3 + m.start()) if m else len(md)]


COLD = {s: json.loads((HERE / 'cold.json').read_text())[s] for s in ('s2', 's9', 's15', 's16')}
# 1. Section 12 v15 (installed): his P2 as written, his caption after it.
H12 = '# The Math of Absorption, and Who This Isn’t For'
s12 = block(NOW, H12)
P2 = next(p for _, p, _ in paras(s12) if p.startswith("This doesn't surprise me"))
CAP = next(plain(b.strip()) for b in re.split(r'\n\s*\n|\n', s12) if b.strip().startswith('[caption] It\'s kind of'))
drafts['S12v15-P2cap'] = P2 + '\n\n' + CAP
gate['S12v15-P2cap'] = {'kind': 'owner', 'joel': JOEL + '44c "i was not saying to put the prose in, i wanted the actual screenshot '
                        'with the link and my caption as that quote aside to you." His P2 as he wrote it (2026-10-14), and his aside '
                        '("altho it\'s kind of a "no, duh" study") as the caption, "altho" dropped'}
drafts['S12v15'] = section(NOW, H12)
gate['S12v15'] = {'kind': 'section', 'parts': ['installed', 'S12v15-P2cap'], 'repeats': 0,
                  'repeats_note': 'my two sentences about the study out; the only new words are his seven-word caption, which says '
                                  'nothing the section says elsewhere'}
# 2. Edits in sections 2, 9, 15 and 16.
EDITS = [
    ('S2v33-P2', '# Communes Are Hot Again', 'Whether you want to call that loneliness', 's2-P2', 's2', False,
     'batch 268g: section 2 v3.2 100% Human, P2 Human with its neighbors', 'the published "starving" for Emulate\'s "starvin\'"'),
    ('S9v17-evid', '# The Best Model I’ve Seen: Zapatistas', 'As part of my research I have also looked', 's9-evidence', 's9', False,
     'batch 276g: section 9 v15, this paragraph (E-S9P18f) Human alone and the section 100% Human', 'the published limit back'),
    ('S15v14-H2P3', '# What This Looks Like From Sénégal', 'So which is it?', 's15-H2P3', 's15', True,
     'batch 410g: section 15 v13 100% Human', 'the published judgment back'),
    ('S15v14-H3P1', '# What This Looks Like From Sénégal', 'Then there\'s the so-called', 's15-H3P1', 's15', True,
     'batch 410g: section 15 v13 100% Human', 'the published "prosperity came through you"'),
    ('S16v29-H2P4', '# Practice Comes Before Property', 'A group that practices together weekly', 's16-H2P4', 's16', True,
     'batch 413g: section 16 v28 100% Human', 'the published "change how people survive"'),
    ('S15v14-H2P1', '# What This Looks Like From Sénégal', 'But does this mean I think', 's15-H2P1', 's15', True,
     'batch 410g: section 15 v13 100% Human', 'his 43, the mark only: the answer opens the passage on the anti-gay law'),
]
EXCL = json.loads((HERE / 'excl-changes.json').read_text())
STARTS = {'s15': {'H1P2': 'Sénégal is unlike anywhere', 'H1P5': 'Even in Dakar', 'H2P6': 'Everybody here has sheep',
                  'H3P4': 'This is also the thorny', 'H3P8': 'So this is a global issue'},
          's16': {'H1P2': 'It would be better to get together', 'H1P3': 'Same with money', 'H2P3': 'So your inner pl/ork',
                  'H2P5': "Here's an idea if you're remote", 'H3P1': 'So what do you actually do this month'}}
for s, ch in EXCL.items():
    h1 = '# What This Looks Like From Sénégal' if s == 's15' else '# Practice Comes Before Property'
    was = 'batch 410g: section 15 v13 100% Human' if s == 's15' else 'batch 413g: section 16 v28 100% Human'
    for where, kind, old, new, why in ch:
        EDITS.append(('%s-%s' % ('S15v14' if s == 's15' else 'S16v29', where), h1, STARTS[s][where], '%s-%s' % (s, where), s, True,
                      was, 'his 43, %s: %s' % ('the mark only' if kind == 'period' else 'the phrase out', why)))
for key, h1, starts, mid, s, own, was, what in EDITS:
    # the latest reading of the paragraph's final text: march-r3 (the last fixes), then r2 (the faithfulness fixes), then r1
    m1, rnd = next((m, r) for m, r in ((M3, 'march-r3'), (M2, 'march-r2'), (M1, 'march-r1')) if mid + '-new' in m)
    if key == 'S16v29-H1P3':
        what += '; and "by declaring" for "because" (the published "declaring", REPORT-FOREST.md [2])'
    rec = {'kind': 'edit', 'was': was, 'march_was': m1[mid + '-was'], 'march': m1[mid + '-new'],
           'march_note': 'fix-20261017b/%s (%s-was and %s-new)' % (rnd, mid, mid),
           'cold': COLD[s][0], 'cold_note': COLD[s][1], 'grounding': 'OK',
           'grounding_note': 'no claim of mine: ' + what + ' (fix-20261017b/faithful/TRIAGE.md, excl-changes.json)',
           'stance': 0, 'stance_note': 'the published words or a mark; no position added', 'missing': [],
           'joel_note': JOEL + ('his 43 ("either take out the exclamation phrases themselves, replace the exclamation marks alone only '
                                'if it makes sense to")' if 'his 43' in what else 'his 45 ("a final pass to make sure it\'s faithful to the original")')}
    checks(key, block(NEW, h1), starts, rec)
for key, h1, own, prefix in (('S2v33', '# Communes Are Hot Again', False, 'S2v33-'), ('S9v17', '# The Best Model I’ve Seen: Zapatistas', False, 'S9v17-'),
                             ('S15v14', '# What This Looks Like From Sénégal', True, 'S15v14-'), ('S16v29', '# Practice Comes Before Property', True, 'S16v29-')):
    drafts[key] = sect_text(NEW, h1, own)
    parts = sorted(k for k in gate if k.startswith(prefix))   # a paragraph under 50 words has only its pair records
    gate[key] = {'kind': 'section', 'parts': ['installed'] + parts, 'repeats': 0,
                 'repeats_note': 'fix-20261017b/DISPOSITIONS.md: exclamation marks and filler phrases out, or published words back; '
                                 'nothing said twice that was said once'}
# 3. Screens: the anomie paragraph (question 46) and the alternative for "One disagreement is enough!" (question 47).
s2a = block(ANOM, '# Communes Are Hot Again')
A_ = next(p for _, p, _ in paras(s2a) if p.startswith("What's starving them is anomie"))
recA = {'kind': 'screen', 'march': [MA[0]['1'], MA[1]['1']], 'march_note': 'fix-20261017b/anomie/MARCH-v2-labels-a.txt and -b.txt (T1)'}
checks('A46', s2a, "What's starving them is anomie", recA)
drafts['S2-A46'] = section(ANOM, '# Communes Are Hot Again')
# the linter reads the new paragraph: run on the whole section it fails on the installed text this screen doesn't change (his
# published 🔥, off the emoji allowlist, and words its speller doesn't know), which no screen of a new paragraph can fix
gate['S2-A46'] = dict(recA, lint=gate['A46']['lint'], lint_note='the anomie paragraph alone (A46); the section as a whole fails '
                      'only on installed text: his published 🔥 off the allowlist, spellings', words=len(drafts['S2-A46'].split()))
# The alternative for "One disagreement is enough!" ("(One is plenty for now.)", alt-s16.md) isn't screened: the linter fails
# the paragraph for its coach rate (E41: "You can talk about a shared future later.", the published "before discussing a shared
# future", one phrase in 46 words), as it fails the installed paragraph, so the paragraph goes to Joel as it is (question 47).
for k in gate:
    gate[k].setdefault('words', len(drafts[k].split()))
# a pair can be the same text for two paragraphs (H2P4 with the next is H2P5 with the previous): read it once, and keep the
# other key as an alias of the one read (b415/aliases.json; the results file gets both)
seen, aliases = {}, {}
for k in list(drafts):
    if drafts[k] in seen:
        aliases[k] = seen[drafts[k]]
        del drafts[k]
    else:
        seen[drafts[k]] = k
out = HERE / 'b415'
out.mkdir(exist_ok=True)
(out / 'aliases.json').write_text(json.dumps(aliases, indent=1) + '\n', encoding='utf-8')
(out / 'drafts.json').write_text(json.dumps(drafts, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
(out / 'GATE.json').write_text(json.dumps(gate, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'pangram_gate.py'), str(out / 'drafts.json'),
                    str(out / 'GATE.json'), str(out / 'b415.js'), '--name', 'B415'] + list(drafts), capture_output=True, text=True)
print(r.stdout[-1500:], r.stderr[-2500:])
items = [[k, t, hashlib.sha256(t.encode('utf-8')).hexdigest()] for k, t in drafts.items()]
(out / 'b415-items.json').write_text(json.dumps(items, ensure_ascii=False), encoding='utf-8')
for k in drafts:
    print(k, gate[k]['words'], gate[k]['kind'], gate[k].get('lint'), drafts[k][:60].replace('\n', ' / '))
print('aliases:', aliases)
print(len(items), 'items,', sum(gate[k]['words'] for k in drafts), 'words')
