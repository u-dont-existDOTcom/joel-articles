"""Put SC-48c into HUMANIZED-SO-FAR.md, as he approved it (his answers on x1112a, pasted in chat 2026-11-12 19:32 UTC:
ANSWERS-X1112A-20261112-1932.json, SC-48c approved, no comment).

Two phrases of his clause in block 48's last sentence change to what the review he cites says (texts_x1111d.SWAPS):
"the salts work for rats with trauma" to "BHB injections work for rats with trauma", and "although not nearly as proven
for humans as the keto diet is" to "although in humans it's still an open question whether the salts work as well as
the keto diet". The split the card's advice offered wasn't taken, so the sentence keeps his shape.

  python3 articles/neuro-de-armoring/humanize/fix-20261108/keto/apply_x1112a.py [--write]
"""
import hashlib
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parents[1]
sys.path.insert(0, str(HERE))
import texts_x1111d as T  # noqa: E402

ARTICLE = H / 'HUMANIZED-SO-FAR.md'
ANSWERS = HERE / 'ANSWERS-X1112A-20261112-1932.json'


def main(write=False):
    md = ARTICLE.read_text(encoding='utf-8')
    a = json.loads(ANSWERS.read_text(encoding='utf-8'))
    (item,) = [x for x in a['items'] if x['id'] == 'SC-48c']
    assert item['status'] == 'approved'
    assert a['article']['sha256'] == hashlib.sha256(md.encode('utf-8')).hexdigest(), 'the article changed since the card'
    lines = md.split('\n')
    (i,) = [k for k, l in enumerate(lines) if l.startswith(T.START)]
    new = lines[i]
    for old, rep in T.SWAPS:
        assert new.count(old) == 1, old
        new = new.replace(old, rep)
    built = (HERE / 'SP48C.md').read_text(encoding='utf-8').strip()
    assert new == built, 'not the paragraph the card showed'
    out = '\n'.join(lines[:i] + [new] + lines[i + 1:])
    rec = {'about': 'SC-48c, approved (his answers on x1112a, pasted in chat 2026-11-12 19:32 UTC)',
           'answers': ANSWERS.name, 'card': 'SC-48c', 'status': 'approved', 'line': i + 1,
           'swaps': [{'old': o, 'new': n} for o, n in T.SWAPS], 'old': lines[i], 'new': new,
           'before_sha256': hashlib.sha256(md.encode('utf-8')).hexdigest(),
           'after_sha256': hashlib.sha256(out.encode('utf-8')).hexdigest()}
    print('after', rec['after_sha256'][:8])
    if write:
        ARTICLE.write_text(out, encoding='utf-8')
        (HERE / 'APPLIED-X1112A.json').write_text(json.dumps(rec, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')


if __name__ == '__main__':
    main('--write' in sys.argv)
