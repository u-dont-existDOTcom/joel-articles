"""Batches 410g and 411g (2026-10-17, after Joel's 13:11 message): every paragraph this turn changes, alone (50 words or more)
or with each neighbor under its heading, every changed section whole, and the two probes of his question 40. 410g holds
sections 1, 4, 8, 15 and 16 and the probes; 411g holds section 12, whose new paragraph of mine waits for its meaning reviews.
Each whole section is the text Pangram read for that section before: sections 15 and 16 as their own batches built them (images
and embeds out, captions in, headings without their marks), the others as fix-20261014/ptext.py builds them.
Run from candidate/: python3 fix-20261017/make_batch.py 410|411"""
import json, pathlib, re, subprocess, sys, tempfile

HERE = pathlib.Path(__file__).resolve().parent
C = HERE.parent
REPO = C.parents[2]
sys.path.insert(0, str(C / 'fix-20261014'))
from ptext import plain, section  # noqa: E402

WHICH = sys.argv[1]
JOEL = 'Joel, 2026-10-17 13:11 UTC (joel-20261017/joel-20261017-1311-message.txt): '
SKIP = re.compile(r'^(\[image \d+\]|\[Professor Baby Sheep|Double click to interact with video|<!--)')


def own_whole(md):
    """Sections 15 and 16 as their batches read them (s15/b338 S15v12, s16/b399 S16v26kni)."""
    out = []
    for b in [b.strip() for b in re.split(r'\n\s*\n', re.sub(r'<!--.*?-->', '', md, flags=re.S)) if b.strip()]:
        if SKIP.match(b):
            continue
        if b.startswith('[caption]'):
            b = re.sub(r'^\[caption\]\s*', '', b)
        out.append(plain(b.lstrip('#').strip()))
    return '\n\n'.join(out)


# the method reproduces the whole-section texts Pangram read before
assert own_whole((C / 's15' / 'v12.md').read_text(encoding='utf-8')) == json.loads((C / 's15' / 'b338' / 'drafts.json').read_text())['S15v12']
subprocess.run([sys.executable, str(C / 's16' / 'make_v26.py'), 'kni'], check=True, capture_output=True)
assert own_whole((C / 's16' / 'v26.md').read_text(encoding='utf-8')) == json.loads((C / 's16' / 'b399' / 'drafts.json').read_text())['S16v26kni']
subprocess.run([sys.executable, str(C / 's16' / 'make_v28.py')], check=True, capture_output=True)
subprocess.run([sys.executable, str(C / 's15' / 'make_v13.py')], check=True, capture_output=True)
subprocess.run([sys.executable, str(HERE / 'make_edits.py')], check=True, capture_output=True)


def paras(md):
    """[(heading number, paragraph)] for the reader's paragraphs; a pair is read only under one heading (paragraphs_alone.py)."""
    out, h = [], 0
    for b in [b.strip() for b in re.split(r'\n\s*\n', re.sub(r'<!--.*?-->', '', md, flags=re.S)) if b.strip()]:
        if b.startswith('#'):
            h += 1
        elif not SKIP.match(b) and not b.startswith('[caption]'):
            out.append((h, plain(b)))
    return out


def lint(md_text):
    with tempfile.NamedTemporaryFile('w', suffix='.md', delete=False, encoding='utf-8') as f:
        f.write(md_text + '\n')
    r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'tells_lint.py'), f.name, '--style',
                        str(C.parent / 'STYLE.json')], capture_output=True, text=True)
    return re.search(r'verdict: (\w+)', r.stdout).group(1)


drafts, gate = {}, {}


def alone_or_pairs(name, md, starts, joel, kind='owner'):
    """The paragraph that starts with STARTS, alone when 50 words or more, and with each neighbor."""
    hp = paras(md)
    ps = [p for _, p in hp]
    i = next(k for k, p in enumerate(ps) if p.startswith(starts))
    rec = {'kind': kind, 'joel': joel} if kind == 'owner' else None
    if len(ps[i].split()) >= 50:
        drafts[name] = ps[i]; gate[name] = dict(rec, words=len(ps[i].split()))
    for j in (i - 1, i + 1):
        # a pair under the same heading, when one of the two is too short to be read alone
        if 0 <= j < len(ps) and hp[j][0] == hp[i][0] and min(len(ps[i].split()), len(ps[j].split())) < 50:
            a, b = sorted((i, j))
            k = '%s+%s' % (name, 'prev' if j < i else 'next')
            drafts[k] = ps[a] + '\n\n' + ps[b]; gate[k] = dict(rec, words=len(drafts[k].split()))
    return ps[i]


if WHICH in ('410', '412'):   # 410: the paragraphs and the probes; 412: the whole sections, once their repeats checks are in
    v28 = (C / 's16' / 'v28.md').read_text(encoding='utf-8')
    alone_or_pairs('S16v28-H1P3', v28, 'Same with money', JOEL + '"practice comes before property p3: remove "quietly" that\'s an ai '
                   'tell at the end"')
    alone_or_pairs('S16v28-H3P7', v28, 'Look before you leap', JOEL + 'question 42, his lines for the stretch that read AI: "And '
                   'whether communal showers feel liberating, or make you start looking at studio apartments! No manifesto is going to '
                   'tell you any of that! Look before you leap. It will really save you some time & money."')
    drafts['S16v28'] = own_whole(v28)
    gate['S16v28'] = {'kind': 'section', 'parts': ['installed'] + [k for k in gate if k.startswith('S16v28-')], 'repeats': 0,
                      'repeats_note': 'fix-20261017/REPEATS-s16.md, with the dispositions in fix-20261017/DISPOSITIONS-20261017.md'}
    v13 = (C / 's15' / 'v13.md').read_text(encoding='utf-8')
    alone_or_pairs('S15v13-H1P3', v13, 'And the humor!', JOEL + '""this" is not the same as "it"... you can\'t use those '
                   'interchangeably all the time." His rule, applied by the sweep to the published "This is the most intensely joking '
                   'culture I\'ve encountered" (fix-20261017/SWEEP-20261017.md, R2): "This" back, no other change')
    alone_or_pairs('S15v13-H2P2', v13, 'Sénégal passed a law', JOEL + '"the french word apology should have been translated as '
                   '"advocacy" and it doesn\'t need to be in quotes. and then we can remove the ", along with certain financing or '
                   'support meant to promote it." as that sounds redundant."')
    alone_or_pairs('S15v13-H3P3', v13, 'This is also the thorny', JOEL + '"you replaced "this is " with "it\'s"... "this" is not '
                   'the same as "it"..."')
    alone_or_pairs('S15v13-H3P5', v13, 'Some Zapatista communities', JOEL + '"I\'d rather say that... i understand the motivation to '
                   'negotiate like that but i think it\'s not a full solution either." in place of the "I like that." I had added')
    drafts['S15v13'] = own_whole(v13)
    gate['S15v13'] = {'kind': 'section', 'parts': ['installed'] + [k for k in gate if k.startswith('S15v13-')], 'repeats': 0,
                      'repeats_note': 'fix-20261017/REPEATS-s15.md, with the dispositions in fix-20261017/DISPOSITIONS-20261017.md'}
    art = (HERE / 'article-with-drafts-b.md').read_text(encoding='utf-8')
    s4 = (HERE / 's4-v11.4.md').read_text(encoding='utf-8')
    alone_or_pairs('S4v114-container', s4, 'The first three parts are the inside', JOEL + 'question 39: "i\'d say it\'s the practical '
                   'logistical foundation that gets built once the architects can work well together, does that work?" (his answer '
                   'fitted to its place: "I\'d say" dropped)')
    drafts['S4v114'] = section(art, '# The Four Parts That Have to Pl/ork Together')
    gate['S4v114'] = {'kind': 'section', 'parts': ['installed'] + [k for k in gate if k.startswith('S4v114-')], 'repeats': 0,
                      'repeats_note': 'fix-20261017/REPEATS-s4.md, with the dispositions in fix-20261017/DISPOSITIONS-20261017.md'}
    s1 = (HERE / 's1-swept.md').read_text(encoding='utf-8')
    alone_or_pairs('S1sw-EastWind', s1, 'The East Wind commune', JOEL + '""this" is not the same as "it"...", applied by the sweep '
                   '(R2) to the published "These are the questions history books neglect.": "That\'s" for "It\'s", no other change')
    drafts['S1sw'] = section(art, '# The New Age May Dawn Suddenly')
    gate['S1sw'] = {'kind': 'section', 'parts': ['installed'] + [k for k in gate if k.startswith('S1sw-')], 'repeats': 0,
                    'repeats_note': 'one word changed ("It\'s" to "That\'s"); nothing said twice that was said once'}
    s8 = (HERE / 's8-v30.md').read_text(encoding='utf-8')
    alone_or_pairs('S8v30-safeguards', s8, 'This could be badly misunderstood', JOEL + '"remove "quietly" that\'s an ai tell", '
                   'applied by the sweep (O42) to "Older kids can\'t be allowed to quietly boss the younger ones around there."')
    drafts['S8v30'] = section(art, '# The Grown Children Get the Final Review')
    gate['S8v30'] = {'kind': 'section', 'parts': ['installed'] + [k for k in gate if k.startswith('S8v30-')], 'repeats': 0,
                     'repeats_note': 'one word taken out ("quietly"); nothing said twice that was said once'}
    probes = json.loads((HERE / 'probes-q40.json').read_text(encoding='utf-8'))
    M = [dict(re.findall(r'^\s*T(\d+):\s*([SB ]+?)\s*$', (HERE / 'march-r1' / ('MARCH-labels-%s.txt' % x)).read_text(), re.M))
         for x in 'ab']
    for n, key in ((2, 'q40-c-plus-often'), (3, 'q40-g-minus-often')):
        drafts['Q40-' + key[4:]] = plain(probes[key])
        gate['Q40-' + key[4:]] = {'kind': 'screen', 'march': [m[str(n)] for m in M], 'march_note': 'fix-20261017/march-r1',
                                  'lint': lint(probes[key]), 'probe': 'Joel\'s question 40: "so "often" is an ai tell?"',
                                  'words': len(plain(probes[key]).split())}
elif WHICH == '411':
    sys.exit('411 is built after the meaning reviews of the new section 12 paragraph')
for k in gate:
    gate[k].setdefault('words', len(drafts[k].split()))
KEYS = [k for k in drafts if (gate[k]['kind'] == 'section') == (WHICH == '412')] if WHICH in ('410', '412') else list(drafts)
drafts = {k: drafts[k] for k in KEYS}
out = HERE / ('b' + WHICH)
out.mkdir(exist_ok=True)
(out / 'drafts.json').write_text(json.dumps(drafts, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
(out / 'GATE.json').write_text(json.dumps(gate, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'pangram_gate.py'), str(out / 'drafts.json'),
                    str(out / 'GATE.json'), str(out / ('b%s.js' % WHICH)), '--name', 'B' + WHICH] + KEYS, capture_output=True,
                   text=True)
print(r.stdout[-600:], r.stderr[-1500:])
import hashlib  # noqa: E402
items = [[k, t, hashlib.sha256(t.encode('utf-8')).hexdigest()] for k, t in drafts.items()]
(out / ('b%s-items.json' % WHICH)).write_text(json.dumps(items, ensure_ascii=False), encoding='utf-8')
for k in drafts:
    print(k, gate[k]['words'], gate[k]['kind'], drafts[k][:70].replace('\n', ' / '))
print(len(items), 'items,', sum(gate[k]['words'] for k in drafts), 'words')
