"""The comparative read of block 48 at its words after SC-48c (approved 2026-11-12 19:32 UTC), beside his post's paragraph
(gates E284, E294), as read_x1111c.py did for his version.

The two phrases SC-48c changed now say what the review he cites says ("BHB injections work for rats with trauma";
"although in humans it's still an open question whether the salts work as well as the keto diet"), so read_x1111c's F1
and F2 are fixed: their words are gone. Each sentence reads on its own and in order; the post's point, that the protocol
works on the brain's structure where mood drugs don't, is kept with what has been seen in people and rats.

- F3 (1, unclear): the last sentence still runs long with two "although" clauses; his shape, and he kept it when the
  card offered the split.

  python3 articles/neuro-de-armoring/humanize/fix-20261108/keto/read_x1112a.py
Writes read-x1112a/READ-RECORD.json here.
"""
import hashlib
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parents[1]
ROOT = H.parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import compare_read as cr  # noqa: E402
import suggestion_review as sr  # noqa: E402

START = 'Why don\'t these drugs work on calcified PTSD?'
NOW = ('although we can see some astounding BHB salt reviews on forums, like for brain injury repair, and BHB injections '
       'work for rats with trauma, although in humans it\'s still an open question whether the salts work as well as the '
       'keto diet')


def main():
    md = (H / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
    (blk,) = [b for b in sr.blocks(md) if b['text'].startswith(START)]
    assert NOW in blk['text']
    h = cr.phash(blk['text'])
    d = HERE / 'read-x1112a'
    d.mkdir(exist_ok=True)
    cr.record(d, findings=[{'id': 'F3', 'severity': 1, 'kind': 'unclear', 'block_hashes': [h], 'now': NOW}],
              coverage=[h],
              dispositions={'F3': ['his', 'his own shape; he kept it when SC-48c offered the split (severity 1)']},
              article='HUMANIZED-SO-FAR.md at %s: block 48 after SC-48c, read beside his post\'s by the lead session '
                      '(E284, E294)' % hashlib.sha256(md.encode('utf-8')).hexdigest()[:8])
    print('recorded')


if __name__ == '__main__':
    main()
