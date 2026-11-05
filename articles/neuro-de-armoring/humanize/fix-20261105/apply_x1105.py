"""Neuro de-armoring, 2026-11-05 (his answers of 15:55 UTC on Neuro De-Armoring Cards, 5 November,
../fix-20261104/cards/ANSWERS-20261105-1555.json, and this turn's checks in his account):

- ATP-2, his version of the ATP section's first paragraph, in as he wrote it: "reduced hippocampal ATP signaling" becomes
  "reduced hippocampal astrocyte ATP release" (what the mouse study measured). It read Human Written, 0%, one window,
  High (https://www.pangram.com/history/d0bbc185-3142-4ad9-9468-718e2263a9ee). His version keeps ATP-1's Calabrese
  sentence as I had changed it, so ATP-1's "rejected" changes nothing in the text. Y-93b: rejected with "already said keep
  this fix in last turn?": the fix stays.
- The ketone decision and Strategy A (the post's blocks 95 and 96, one paragraph) and Strategy B with its fat, protein and
  guide lines (blocks 98 to 100, one paragraph), try 3: clearer than the post's labels (why the choice touches the
  electrolytes, what each strategy is for, the keto flu named), and still AI after three tries each and the tell panel
  (../fix-20261104/checks/x1105a to x1105c; panel ../fix-20261104/panel/x1105-ketone/PANEL.md). In the article meanwhile
  (gate E291: the clear version stays); his to rewrite on Neuro De-Armoring Cards, 5 November (2).

  python3 articles/neuro-de-armoring/humanize/fix-20261105/apply_x1105.py [--check]
"""
import argparse
import copy
import hashlib
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parent
ROOT = H.parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import fidelity_keys as fk  # noqa: E402

ARTICLE = H / 'HUMANIZED-SO-FAR.md'
ANS = H / 'fix-20261104' / 'cards' / 'ANSWERS-20261105-1555.json'


def plain(t):
    return re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', t)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--check', action='store_true')
    a = ap.parse_args()
    md = ARTICLE.read_text(encoding='utf-8')
    sha = hashlib.sha256(md.encode('utf-8')).hexdigest()
    answers = json.loads(ANS.read_text(encoding='utf-8'))
    assert answers['article']['sha256'] == sha, 'the article changed since his page'
    A = {x['id']: x for x in answers['items']}
    raw = re.split(r'\n\s*\n', md.rstrip('\n'))
    (i,) = [k for k, b in enumerate(raw) if b.startswith('If your cortisol is normal or low')]
    his = A['ATP-2']['your_version'].strip()
    assert plain(raw[i]) == A['ATP-2']['before'] and his.count('astrocyte ATP release') == 1
    new = raw[i].replace('reduced hippocampal ATP signaling', 'reduced hippocampal astrocyte ATP release')
    assert plain(new) == his
    raw[i] = new
    (j,) = [k for k, b in enumerate(raw) if b.startswith('KETONE DECISION:')]
    assert raw[j + 1].startswith('Strategy A:')
    raw[j:j + 2] = [(HERE / 'blocks' / '095-096.md').read_text(encoding='utf-8').strip()]
    (k,) = [n for n, b in enumerate(raw) if b.startswith('Strategy B:')]
    assert raw[k + 1].startswith('Fat:EAT FAT') and raw[k + 2].startswith('To avoid side effects')
    raw[k:k + 3] = [(HERE / 'blocks' / '098-100.md').read_text(encoding='utf-8').strip()]
    out = '\n\n'.join(raw) + '\n'
    r = fk.check(json.loads((H / 'FIDELITY-KEYS.json').read_text(encoding='utf-8')), out)
    after = hashlib.sha256(out.encode('utf-8')).hexdigest()
    rec = {'before_sha256': sha, 'after_sha256': after, 'fidelity_pass': r['pass'],
           'atp2': 'his version, Human High: https://www.pangram.com/history/d0bbc185-3142-4ad9-9468-718e2263a9ee',
           'ketone': {'p095-096': 'try 3, AI: https://www.pangram.com/history/2d2d6dc2-2232-4460-8b86-751f044f80a3',
                      'p098-100': 'try 3, AI 71%: https://www.pangram.com/history/2c76e3b4-deac-493c-9aab-a5affbedfb1e'}}
    print(json.dumps(rec, indent=1))
    assert r['pass'], r
    if a.check:
        return
    ARTICLE.write_text(out, encoding='utf-8')
    (HERE / 'APPLIED-X1105.json').write_text(json.dumps(rec, indent=1) + '\n', encoding='utf-8')


if __name__ == '__main__':
    main()
