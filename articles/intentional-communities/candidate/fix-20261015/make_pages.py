"""The side-by-side page after Joel's answers of 2026-10-15 09:33 UTC: section 10 (28 b).

New map versions from the last ones (fix-20261014/make_pages.py's): the same rows and source starts, the starts
that changed fixed, last turn's notes and proposal rows dropped (questions 22 to 26 are answered), today's notes on
the rows that changed, and the one new proposal (section 10). Highlights are against main at b8a061ec, the version
Joel last saw (this morning's pages, merged at the start of this turn).

Run from the candidate folder: python3 fix-20261014b/make_pages.py
"""
import json, pathlib, subprocess, sys

CAND = pathlib.Path(__file__).resolve().parent.parent
REPO = CAND.parents[2]
sys.path.insert(0, str(REPO / 'tools' / 'humanization'))
import render_in_context as R  # noqa: E402

SINCE = "934d64c9"
CUR = R.paragraphs((CAND / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8'))
DROP = (' · changed today', ' · changed this turn', ' · changed for your answer', ' (PROPOSAL)', ', a proposal')
FIRST = ('Your published section is on the left. On the right is the version now in the article so far. '
         'Highlighted words are new since the version you merged last night (pull request 175), and struck words are ones that went.')
NOT_YET = 'Not checked in Pangram yet: I\'ll check it once you pick.'


def para(start):
    return R.plain(R.find(CUR, start, start))[0]


def swap(start, old, new):
    text = para(start)
    assert text.count(old) == 1, (start, old)
    return text.replace(old, new)


def build(name, old, meta, intro, fixes=None, changed=None, proposals=None):
    fixes, changed, proposals = fixes or {}, changed or {}, proposals or []
    m = json.loads((CAND / 'in-context' / old).read_text(encoding='utf-8'))
    out = {'title': m['title'], 'meta': meta, 'intro': intro, 'blocks': []}
    used = set()
    for blk in m['blocks']:
        rows = []
        for r in blk['rows']:
            if 'text' in r:          # last turn's proposals: answered
                continue
            r2 = {k: v for k, v in r.items() if k not in ('notes', 'note', 'flag', 'repeats')}
            lab = r2.get('label', '')
            for d in DROP:
                lab = lab.replace(d, '')
            r2['label'] = lab
            if 'article' in r2:
                r2['article'] = next((new for old_, new in fixes.items() if r2['article'].startswith(old_)), r2['article'])
                for k, (suffix, notes) in changed.items():
                    if r2['article'].startswith(k):
                        r2['label'] = (lab + ' · ' + suffix) if lab else suffix
                        r2['notes'] = notes
                        used.add(k)
            rows.append(r2)
            for p in proposals:
                if 'article' in r2 and r2['article'].startswith(p['after']):
                    rows.append({'label': p['label'], 'text': p['text'], 'proposal_of': r2['article'],
                                 'source': r2.get('source', []), 'notes': p['notes']})
                    used.add('P:' + p['label'])
        out['blocks'].append({'headings': blk.get('headings', []), 'rows': rows})
    missing = [k for k in changed if k not in used] + [p['label'] for p in proposals if 'P:' + p['label'] not in used]
    assert not missing, (name, missing)
    path = CAND / 'in-context' / name
    path.write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    return path


PAGES = []
S10 = 'Whenever a community or a federation creates or applies a rule'
PAGES.append((build('ic10-v5.json', 'ic10-v4.json',
    'Community article · section 10 · v4, 2026-10-15 09:33 · in the article so far as a candidate',
    [FIRST,
     'What changed: your 28 b, "Whenever a community or a federation creates or applies a rule" for "Whenever you create or apply a rule".',
     'Both cold reads of the section now read every paragraph OK. Pangram\'s web app: the paragraph reads Human alone (97 words, 09:37:56 UTC, https://www.pangram.com/history/e81a57be-e16a-48a5-8c53-ddef100c1cd4), and the whole section 100% Human (740 words, 09:38:10 UTC, https://www.pangram.com/history/b035c409-6832-4ef7-a005-de067e109a43).'],
    fixes={'Whenever you create or apply a rule': S10},
    changed={S10: ('changed today', ['Your 28 b.'])}),
    'community-section10-side-by-side.html'))

if __name__ == '__main__':
    for mp, out in PAGES:
        r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'render_in_context.py'), str(mp),
                            str(CAND / out), '--article', str(CAND / 'HUMANIZED-SO-FAR.md'),
                            '--source', str(CAND.parent / 'original.md'), '--since', SINCE],
                           capture_output=True, text=True)
        print(mp.name, '->', out, 'exit', r.returncode)
        print('  ' + '\n  '.join(l for l in (r.stdout + r.stderr).strip().split('\n') if 'label number was dropped' not in l))
