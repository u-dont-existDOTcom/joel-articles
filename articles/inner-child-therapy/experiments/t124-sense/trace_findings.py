#!/usr/bin/env python3
"""Turn 124: every finding of the word-for-sense read (FINDINGS-RAW.json, from tools/humanization/sense_read.py score) traced to
whose words it is, as SKILL.md's step 5 asks ("read every finding in place and trace whose words it is"):
  - his guide: the words are in his reorganized guide (experiments/t116-joel/JOEL-GUIDE-20261103.md, his ODT of 2026-11-03);
  - his version: in one of his marking-page versions (experiments/t122-answers/ANSWERS-20261104-1344.json);
  - his edit: in an OWNER-EDITS.json entry of his (an id starting "joel-");
  - not in his texts: ours, or his words changed since (read it in place before deciding).
Quote marks, dashes and spaces are compared the same way in all of them, and link addresses and emphasis marks are left out.
Writes TRACE.json (each finding with its block's text and whose words) and prints one line a finding.
  python3 articles/inner-child-therapy/experiments/t124-sense/trace_findings.py [--raw FINDINGS-RAW.json] [--out TRACE.json]"""
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
ART_DIR = HERE.parents[1]
ROOT = HERE.parents[3]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import suggestion_review as sr  # noqa: E402

SAME = str.maketrans({'’': "'", '‘': "'", '“': '"', '”': '"', '\xa0': ' ', '–': '-', '—': '-'})


def norm(s):
    s = re.sub(r'<!--.*?-->', ' ', s, flags=re.S)
    s = re.sub(r'\[([^\]]*)\]\(((?:[^()\s]|\([^()\s]*\))+)\)', r'\1', s)
    s = s.replace('**', '').replace('*', '').replace('  \n', ' ')
    s = re.sub(r'^#+\s*', '', s, flags=re.M)
    return re.sub(r'\s+', ' ', s.translate(SAME)).strip().lower()


def main():
    arg = lambda k, d: pathlib.Path(sys.argv[sys.argv.index(k) + 1]) if k in sys.argv else d
    raw = json.loads(arg('--raw', HERE / 'FINDINGS-RAW.json').read_text(encoding='utf-8'))
    blocks = sr.blocks((ART_DIR / 'HUMANIZED-ARTICLE-SO-FAR.md').read_text(encoding='utf-8'))
    guide = norm((HERE.parent / 't116-joel' / 'JOEL-GUIDE-20261103.md').read_text(encoding='utf-8'))
    ans = json.loads((HERE.parent / 't122-answers' / 'ANSWERS-20261104-1344.json').read_text(encoding='utf-8'))
    versions = {it['id']: norm(it.get('your_version') or '') for it in ans['items']}
    led = json.loads((ART_DIR / 'OWNER-EDITS.json').read_text(encoding='utf-8'))
    edits = {e['id']: norm(' '.join(e.get('must_contain', []))) for e in led['entries']
             if e['id'].startswith('joel-') and e.get('status') == 'applied'}
    out = []
    for f in raw:
        t = norm(f['text'])
        b = blocks[f['block']]
        whose = 'not in his texts'
        if t and t in guide:
            whose = 'his guide'
        else:
            v = [k for k, s in versions.items() if t and t in s]
            e = [k for k, s in edits.items() if t and t in s]
            if v:
                whose = 'his version (%s)' % ', '.join(v)
            elif e:
                whose = 'his edit (%s)' % ', '.join(e)
        out.append(dict(f, whose=whose, section=b.get('section'), block_text=b['text']))
        print('[%d] %s | %s | readers %s | %s: %s -> %s' % (f['block'], whose, b.get('section'), f['readers'], f.get('kind'),
                                                            f['text'][:90], (f.get('fix') or '')[:90]))
    arg('--out', HERE / 'TRACE.json').write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print(len(out), 'findings traced:', {w: sum(1 for o in out if o['whose'] == w) for w in sorted({o['whose'] for o in out})})
    return 0


if __name__ == '__main__':
    sys.exit(main())
