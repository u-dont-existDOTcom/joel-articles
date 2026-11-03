"""Joel's answer to question 30 of the hypnosis questions page: "30a" (his message of 2026-11-02 21:57 UTC,
../free-whole/joel-20261102-2157-message.txt). The question: his new line in Nothing happens says "only like 50% of people
are very suggestible", and Stanford Medicine's report on its 2024 hypnosis study says about 15% of people are highly
hypnotizable and about two-thirds of adults at least somewhat
(https://med.stanford.edu/news/all-news/2024/01/brain-stimulation-hypnosis.html). a) was "only like 15%", with the rest
of his sentence as it is. Only the number changes.

  python3 articles/inner-signal/humanize/fix-20261102/q30/apply_q30.py [--check]
Writes HUMANIZED-SO-FAR.md, APPLIED-Q30.json and read/READ-RECORD.json (the comparison gate's record of the changed
paragraph, read in place by the lead session).
"""
import argparse
import hashlib
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
F = HERE.parent
H = F.parent
ROOT = H.parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import compare_read as cr  # noqa: E402
import suggestion_review as sr  # noqa: E402

GUIDE = H / 'HUMANIZED-SO-FAR.md'
BEFORE = '28c84e9e1d54da1227a1ea2985a75a2954714b8491436c36f8cfe19241499a4d'
OLD = 'After all, only like 50% of people are very suggestible.'
NEW = 'After all, only like 15% of people are very suggestible.'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--check', action='store_true')
    a = ap.parse_args()
    md = GUIDE.read_text(encoding='utf-8')
    assert hashlib.sha256(md.encode('utf-8')).hexdigest() == BEFORE, 'the guide changed since question 30 was asked'
    assert md.count(OLD) == 1
    new = md.replace(OLD, NEW)
    bl_old, bl_new = sr.blocks(md), sr.blocks(new)
    assert len(bl_old) == len(bl_new)
    changed = [b['i'] for b, c in zip(bl_old, bl_new) if b['text'] != c['text']]
    assert len(changed) == 1
    after = hashlib.sha256(new.encode('utf-8')).hexdigest()
    rec = {'question': 30, 'answer': '30a', 'message': '../free-whole/joel-20261102-2157-message.txt',
           'before_sha256': BEFORE, 'after_sha256': after, 'changed_blocks': changed,
           'where': sr.where(bl_new, changed[0]), 'before': OLD, 'after': NEW,
           'source': 'https://med.stanford.edu/news/all-news/2024/01/brain-stimulation-hypnosis.html'}
    print(json.dumps(rec, indent=1))
    if a.check:
        return
    GUIDE.write_text(new, encoding='utf-8')
    (HERE / 'APPLIED-Q30.json').write_text(json.dumps(rec, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    d = HERE / 'read'
    d.mkdir(parents=True, exist_ok=True)
    cr.record(d, findings=[], coverage=[cr.phash(bl_new[changed[0]]['text'])], dispositions={},
              article='HUMANIZED-SO-FAR.md at %s: the paragraph his answer 30a changed (his "50%%" made "15%%"), read by '
                      'the lead session in place beside his version (E284, E294)' % after[:8])


if __name__ == '__main__':
    main()
