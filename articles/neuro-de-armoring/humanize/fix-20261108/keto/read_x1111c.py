"""The comparative read of block 48 as his version of SC-48b put it in (his answers exported 2026-11-12 18:23 UTC), beside
his post's paragraph (gates E284, E294): sentence by sentence, for anything garbled, unclear, lost or vaguer than his.

His post: "Why don't these drugs work on calcified PTSD? Because standard serotonin drugs treat the "software" (mood), but
they cannot penetrate the "hardware" (the structural changes in the amygdala caused by severe trauma). This protocol uses
Ketones and HDAC Inhibitors to remodel the physical structure of the brain that resists standard medication."

Now: his four sentences from his answer on SC-48; the HDAC sentence (BHB blocks HDACs; in mice an HDAC blocker made
extinction learning last); the Oslo study; the two case reports; and the limit, with his clause on forum reviews, rats
and the review he cites. The post's point, that the protocol works on the brain's structure where mood drugs don't, is
kept and now has what has been seen in people. Each sentence before the last reads on its own and in order.

- F1 (2, fact): "the salts work for rats with trauma": the rats in the studies the review covers were given BHB by
  injection (Yamanashi 2020; Jung 2025) or MCT oil by mouth (Yoshioka 2026), not the salts. His words: card SC-48c.
- F2 (2, fact): "not nearly as proven for humans as the keto diet is": the review he cites says neither has been shown
  to work against a control group in people, and calls whether supplements can match the diet an open question. His
  words: card SC-48c.
- F3 (1, unclear): the last sentence runs to about 75 words with two "although" clauses, so which claim each qualifies
  takes a second read. His words and his shape; it reads, with effort.

  python3 articles/neuro-de-armoring/humanize/fix-20261108/keto/read_x1111c.py
Writes read-x1111c/READ-RECORD.json here.
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
FINDINGS = [
    ('F1', 2, 'fact', 'the salts work for rats with trauma'),
    ('F2', 2, 'fact', 'although not nearly as proven for humans as the keto diet is'),
    ('F3', 1, 'unclear', 'although we can see some astounding BHB salt reviews on forums, like for brain injury repair, and '
                         'the salts work for rats with trauma, although not nearly as proven for humans as the keto diet is'),
]
DISPOSITIONS = {
    'F1': ['his', 'his own words; the review he cites has the rats given BHB by injection or MCT oil by mouth, and card '
                  'SC-48c puts that wording to him'],
    'F2': ['his', 'his own words; the review he cites calls it an open question whether supplements can match the diet, '
                  'and card SC-48c puts that wording to him'],
    'F3': ['his', 'his own words and his shape, a small snag (severity 1): it reads, with effort'],
}


def main():
    md = (H / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
    bl = sr.blocks(md)
    hits = [b for b in bl if b['text'].startswith(START)]
    assert len(hits) == 1
    text = hits[0]['text']
    h = cr.phash(text)
    findings = []
    for fid, sev, kind, now in FINDINGS:
        assert now in text, fid
        findings.append({'id': fid, 'severity': sev, 'kind': kind, 'block_hashes': [h], 'now': now})
    d = HERE / 'read-x1111c'
    d.mkdir(exist_ok=True)
    cr.record(d, findings=findings, coverage=[h], dispositions=DISPOSITIONS,
              article='HUMANIZED-SO-FAR.md at %s: block 48 as his version of SC-48b put it in, read beside his post\'s by '
                      'the lead session (E284, E294)' % hashlib.sha256(md.encode('utf-8')).hexdigest()[:8])
    print('recorded', len(findings))


if __name__ == '__main__':
    main()
