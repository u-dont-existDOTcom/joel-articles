"""Collect the pairs, check every quote against its file, write PAIRS.json, print the tallies."""
import json, pathlib, collections, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from ex import check
import data1, data2, data3, data4, data5

OUT = pathlib.Path(__file__).resolve().parents[1]  # the emulate-lessons folder
MAIN = set(data1.L.values())


LOOSE = {  # Emulate's version is looser and wordier than the text it replaced (filler, repetition), judged pair by pair
    'b479-S2', 'b479-S3a', 'b479-S4', 'b479-S5', 'b480-S7', 'b480-S8', 'b480-S9', 'b480-S10',
    'b474-drive', 'b474-shortcut-steps', 'b474-shortcut-help', 'b474-trouble-fake', 'b474-stand',
    'b475-count', 'b475-reorient', 'b475-note', 'seam-bj-keep', 'seam-bk-reverse',
    'screen-S2-metaphors', 'screen-S2-imagery', 'screen-S4-active',
    'b481-S12', 'b481-S18', 'b481-S20', 'b481-S21', 'b481-S22', 'b481-S30', 'b481-S32', 'b481-S11', 'b481-S14',
    '40-HG06-form', '40-HG06-training', '40-HG22-dishes', '40-HG27-enemy', '40-HG27-kid', '40-HG12-sober',
    '40-HG12-essay', '40-HG18-orient', '40-HG19-response', '40-HG23-rule', '40-HG26-feedback', '40-HG36-lighting',
    '40-HG01-nav', '40-HG12-outside',
    'fail-41-screen-S6-guide', 'fail-41-emu-ax-if', 'fail-41-emu-ba-ways',
    'fail-40-HG04-a', 'fail-40-HG16-a', 'fail-40-HG29-a', 'fail-41-br-fix',
}


def collect():
    P = []
    for m in (data1, data2, data3, data4, data5):
        P += m.pairs()
    for p in P:
        if p['id'] in LOOSE and data1.O['loose'] not in p['labels']:
            p['labels'] = p['labels'] + [data1.O['loose']]
    missing = LOOSE - {p['id'] for p in P}
    assert not missing, missing
    return P


def verify(P):
    bad = []
    ids = collections.Counter(p['id'] for p in P)
    for k, n in ids.items():
        if n > 1:
            bad.append('duplicate id ' + k)
    for p in P:
        for fld in ('input', 'emulate', 'emulate_raw'):
            q = p.get(fld)
            if q and not check(q['file'], q['text']):
                bad.append('%s %s not exact in %s' % (p['id'], fld, q['file']))
        for lab in p['labels']:
            if lab not in MAIN and not lab.startswith('other: '):
                bad.append('%s bad label %r' % (p['id'], lab))
    return bad


def flatten(p):
    d = {
        'id': p['id'],
        'batch': p['batch'],
        'source_file': p['input']['file'],
        'input': p['input']['text'],
        'input_reading': p['input_reading'],
        'emulate': p['emulate']['text'],
        'emulate_reading': p['emulate_reading'],
        'labels': p['labels'],
        'meaning_error': p['meaning_error'],
        'detector': p['detector'],
        'kind': p['kind'],
        'emulate_file': p['emulate']['file'],
    }
    if 'key' in p['input']:
        d['source_key'] = p['input']['key']
    if 'key' in p['emulate']:
        d['emulate_key'] = p['emulate']['key']
    if p.get('emulate_raw'):
        d['emulate_raw'] = p['emulate_raw']['text']
        d['emulate_raw_file'] = p['emulate_raw']['file']
    if p.get('kept_or_made'):
        d['kept_or_made'] = p['kept_or_made']
    d['note'] = p.get('note', '')
    return d


GROUPS = [
    ('pass-4.1', lambda p: p['detector'].startswith('Pangram 4.1') and p['kind'] in ('pass', 'pass-low', 'pass-alone-ai-in-place')),
    ('weak-to-high-4.1', lambda p: p['kind'] in ('weak-to-high',)),
    ('pass-4.0', lambda p: p['detector'] == 'Pangram 4.0' and p['kind'] == 'pass'),
    ('fail', lambda p: p['kind'].startswith('fail') or p['kind'] == 'weak-stays-weak'),
    ('reverse', lambda p: p['kind'] == 'reverse'),
]


def tally(P):
    out = {}
    for name, sel in GROUPS:
        ps = [p for p in P if sel(p)]
        c = collections.Counter(l for p in ps for l in p['labels'])
        out[name] = (len(ps), c)
    return out


if __name__ == '__main__':
    P = collect()
    bad = verify(P)
    for b in bad:
        print('BAD', b)
    if bad:
        sys.exit(1)
    rows = [flatten(p) for p in P]
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / 'PAIRS.json').write_text(json.dumps(rows, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print(len(rows), 'rows written;', collections.Counter(r['kind'] for r in rows))
    print('batches:', len(set(r['batch'] for r in rows)))
    for name, (n, c) in tally(P).items():
        print('=====', name, n)
        for lab, k in c.most_common():
            print('  %3d  %s' % (k, lab))
