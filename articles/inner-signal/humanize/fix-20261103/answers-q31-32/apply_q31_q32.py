"""Put Joel's answers to questions 31 and 32 into the hypnosis guide (his message of 2026-11-03 11:19 UTC, word for word in
joel-20261103-1119-message.txt here: "31a 32a recheck b ... recheck a ...").

- 31a: his two-hand practice line, "and you breathe out" becomes "as you breathe out".
- 32a: the four lines of his own that explained again what the sentences before them said (the overcompletion read's
  "ask" decisions, ../overcompletion/DECISIONS.json: P6-05, P5a-02, P5a-03, P5b-02) are cut.

Each change is found by its exact text in the guide as it stands (7e77327d), and set_block_text keeps each block's links
and italics.

  python3 articles/inner-signal/humanize/fix-20261103/answers-q31-32/apply_q31_q32.py [--check]
Writes HUMANIZED-SO-FAR.md, APPLIED-Q31-Q32.json and read/READ-RECORD.json.
"""
import argparse
import hashlib
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parents[1]
ROOT = H.parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
sys.path.insert(0, str(H / 'fix-20261025' / 'review'))
import compare_read as cr  # noqa: E402
import suggestion_review as sr  # noqa: E402
from apply_answers import set_block_text  # noqa: E402

GUIDE = H / 'HUMANIZED-SO-FAR.md'
BEFORE = '7e77327df4ead54e8d233219387ee59a3506e9fb0a0f2a45c26d0d60d2b1883f'


def tidy(s):
    s = re.sub(r'\s+', ' ', s).strip()
    return re.sub(r'\s+([,.;:!?)])', r'\1', s)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--check', action='store_true')
    a = ap.parse_args()
    md = GUIDE.read_text(encoding='utf-8')
    sha = hashlib.sha256(md.encode('utf-8')).hexdigest()
    assert sha == BEFORE, 'the guide changed'
    bl = sr.blocks(md)
    raw = re.split(r'\n\s*\n', md.rstrip('\n'))
    dec = json.loads((H / 'fix-20261103' / 'overcompletion' / 'DECISIONS.json').read_text(encoding='utf-8'))
    asks = [x for x in dec['decisions'] if x['decision'] == 'ask']
    assert sorted(x['id'] for x in asks) == ['P5a-02', 'P5a-03', 'P5b-02', 'P6-05']
    edits = [('31a', 'and you breathe out', 'as you breathe out')] + [('32a ' + x['id'], x['cut'], ' ') for x in asks]
    new_raw, lost, fates = {}, [], {}
    for name, old, new in edits:
        hits = [b['i'] for b in bl if old in b['text']]
        assert len(hits) == 1, (name, hits)
        i = hits[0]
        cur = bl[i]['text'] if i not in new_raw else sr.blocks(new_raw[i][0])[0]['text']
        assert cur.count(old) == 1, name
        text = tidy(cur.replace(old, new, 1))
        new_raw[i] = [set_block_text(raw[i], text, lost)]
        fates[name] = {'block': i, 'where': sr.where(bl, i), 'before': cur, 'after': text}
    assert not lost, lost
    out = []
    for j, r in enumerate(raw):
        out += new_raw.get(j, [r])
    new = '\n\n'.join(out) + '\n'
    after = hashlib.sha256(new.encode('utf-8')).hexdigest()
    rec = {'message': 'joel-20261103-1119-message.txt', 'before_sha256': sha, 'after_sha256': after,
           'changed_blocks': sorted(new_raw), 'fates': fates}
    print(json.dumps({k: v for k, v in rec.items() if k != 'fates'}, indent=1))
    for k, v in fates.items():
        print(k, v['block'], v['where'], '\n   ', v['after'][-200:])
    if a.check:
        return
    GUIDE.write_text(new, encoding='utf-8')
    (HERE / 'APPLIED-Q31-Q32.json').write_text(json.dumps(rec, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    olds = {b['text'] for b in bl}
    changed = [b['text'] for b in sr.blocks(new) if b['text'] not in olds]
    d = HERE / 'read'
    d.mkdir(parents=True, exist_ok=True)
    cr.record(d, findings=[], coverage=sorted({cr.phash(t) for t in changed}), dispositions={},
              article='HUMANIZED-SO-FAR.md at %s: the %d paragraphs his answers 31a and 32a changed, read by the lead '
                      'session in place (E284, E294)' % (after[:8], len(changed)))


if __name__ == '__main__':
    main()
