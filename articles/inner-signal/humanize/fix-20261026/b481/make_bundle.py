"""Batch 481: Emulate first (E235, E237) on every paragraph where batch 480's recheck read Human at less than High confidence
(Joel, 2026-10-26 12:43 UTC: "fix any segments that are not high confidence human if you can"; gate E278). The windows are
../b480/recheck/read/CONFIDENCE.json (tools/humanization/window_confidence.py): every Low one, and every Medium one of 10
words or more. Shorter Medium windows (a list letter, "Yes.", a line of a script) go to Joel as a question instead, and so
does the one AI window, the hypnosis audit he kept as a list (2c).

Each item is the target paragraphs of one section as they stood in that recheck (../b480/CANDIDATE-MASTER.md), with the
paragraph before a target where the item would be under 40 words (Emulate refuses less), adjacent targets in one item.
Only the flagged sentences come back from a sample.

  python3 articles/inner-signal/humanize/fix-20261026/b481/make_bundle.py   (from the repo root)
"""
import hashlib, json, pathlib, re, sys

B = pathlib.Path(__file__).resolve().parent
ROOT = B.parents[4]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import suggestion_review as sr  # noqa: E402
import window_confidence as wc  # noqa: E402

MASTER = B.parent / 'b480' / 'CANDIDATE-MASTER.md'
CONF = B.parent / 'b480' / 'recheck' / 'read' / 'CONFIDENCE.json'


def targets(bl, conf):
    """{block index: [the window rows with a flagged sentence in it]} for the Low windows and the Medium ones of 10+ words."""
    paras = [(b['i'], wc.norm(b['text'])) for b in bl if not b['level']]
    out = {}
    for name in ('RESULT-A.json', 'RESULT-B.json'):
        for x in conf[name]['rows']:
            if x['label'] == 'AI' or not (x['confidence'] == 'Low' or x['words'] >= 10):
                continue
            for s in x['sentences']:
                ns = wc.norm(s['text'])
                i = next((i for i, pt in paras if ns and ns in pt), None)
                if i is not None:
                    out.setdefault(i, [])
                    if x not in out[i]:
                        out[i].append(x)
    return out


def main():
    md = MASTER.read_text(encoding='utf-8')
    bl = sr.blocks(md)
    conf = json.loads(CONF.read_text(encoding='utf-8'))
    tg = targets(bl, conf)
    head = {}
    for b in bl:   # each block's section: the nearest heading above it
        head[b['i']] = b['i'] if b['level'] else head.get(b['i'] - 1)
    ranges = []
    for i in sorted(tg):
        a = i
        words = len(bl[i]['text'].split())
        while words < 40 and a - 1 >= 0 and not bl[a - 1]['level']:
            a -= 1
            words += len(bl[a]['text'].split())
        z = i
        while words < 40 and z + 1 < len(bl) and not bl[z + 1]['level']:
            z += 1
            words += len(bl[z]['text'].split())
        while words < 40 and a - 1 >= 0:   # a one-paragraph section: the heading and the paragraph before it too
            a -= 1
            words += len(bl[a]['text'].split())
        if ranges and a <= ranges[-1][1] + 1 and head[i] == head[ranges[-1][1]]:
            ranges[-1][1] = max(ranges[-1][1], z)
        else:
            ranges.append([a, z])
    bundle, rec = {}, {'master_sha256': hashlib.sha256(md.encode('utf-8')).hexdigest(), 'items': {}}
    for a, z in ranges:
        sec = bl[head[z]]['text'] if head[z] is not None else 'the opening'
        key = 'HG-' + re.sub(r'[^A-Za-z0-9]+', '-', sec)[:28].strip('-') + '-%d' % a
        text = '\n\n'.join(bl[j]['text'] for j in range(a, z + 1))
        n = len(text.split())
        assert 40 <= n <= 3000, (key, n)
        bundle[key] = text
        rec['items'][key] = {'paragraphs': [sr.where(bl, j) for j in range(a, z + 1)], 'blocks': list(range(a, z + 1)),
                             'targets': [sr.where(bl, j) for j in range(a, z + 1) if j in tg], 'words': n,
                             'windows': sorted({'%s %s %d words' % (x['confidence'], x['window'], x['words'])
                                                for j in range(a, z + 1) for x in tg.get(j, [])})}
    out = json.dumps(bundle, ensure_ascii=False, indent=1) + '\n'
    (B / 'BUNDLE.json').write_text(out, encoding='utf-8')
    rec['bundle_sha256'] = hashlib.sha256(out.encode('utf-8')).hexdigest()
    rec['words'] = sum(v['words'] for v in rec['items'].values())
    (B / 'BUNDLE-RECORD.json').write_text(json.dumps(rec, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    for k, v in rec['items'].items():
        print('%-36s %4d words  %s' % (k, v['words'], v['targets']))
    print(len(bundle), 'items,', rec['words'], 'words a sample;', rec['bundle_sha256'])


if __name__ == '__main__':
    main()
