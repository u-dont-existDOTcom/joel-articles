"""Our fixes from batch r1102b that read Human before going in (gate E306, E315), put into the guide, with the read
record (E294).

Batch r1102 (../recheck/RESULTS.md) found one window of ours that read Human (Low) in a section that read Human Written:
"So before you decide where it's coming from, ask it what it's trying to stop, or what it wants." (Working with your
guards). Its fix, the two questions asked as questions, read Human Written with the paragraph after it, the changed
sentence Human (Medium) (r1102b-C1). Our other window, Pattern 10's (Human (Low) in its section), stays as it is: both
tries read AI in their stretch (r1102b-D2, D1), so neither goes in.

The lead session read the fixed paragraph beside his published version and the paragraphs around it: it asks the guard
the same two things the published guide has you ask ("what it's trying to stop, or what it wants"), and nothing else
changed. tells_lint.py on it names his own list of what you might feel (his inner child guide) and nothing of ours.

  python3 articles/inner-signal/humanize/fix-20261102/fixes/apply_fixes_r1102b.py
Writes HUMANIZED-SO-FAR.md, FIXES-R1102B.json and read/READ-RECORD.json.
"""
import hashlib
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parents[1]
ROOT = H.parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import compare_read as cr  # noqa: E402
import suggestion_review as sr  # noqa: E402

GUIDE = H / 'HUMANIZED-SO-FAR.md'
L = 'https://www.pangram.com/history/'
FIXES = [
    {'id': 'r1102b-C1', 'section': 'Working with your guards', 'block_start': 'Instead, you might feel numb',
     'old': 'So before you decide where it\'s coming from, ask it what it\'s trying to stop, or what it wants.',
     'new': 'So before you decide where it\'s coming from, ask it. What is it trying to stop? What does it want from you?',
     'window': 'Human (Low), 21 words, in section 23\'s check: ' + L + 'ea5ab290-9965-40a1-83c3-bae3634cf0d3',
     'tested': 'Human Written, the sentence Human (Medium), with the paragraph after it: ' + L +
               '65ac97c1-88c9-483a-bc30-2b8a427e3209'},
]


def main():
    md = GUIDE.read_text(encoding='utf-8')
    before = hashlib.sha256(md.encode('utf-8')).hexdigest()
    for f in FIXES:
        if f['new'] in md:
            continue
        assert md.count(f['old']) == 1, f['id']
        md = md.replace(f['old'], f['new'])
    GUIDE.write_text(md, encoding='utf-8')
    after = hashlib.sha256(md.encode('utf-8')).hexdigest()
    bl = sr.blocks(md)
    paras = []
    for f in FIXES:
        [b] = [b for b in bl if b['text'].startswith(f['block_start'])]
        assert f['new'] in b['text']
        paras.append(b['text'])
    (HERE / 'FIXES-R1102B.json').write_text(json.dumps({'before_sha256': before, 'after_sha256': after, 'fixes': FIXES},
                                                       ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    (HERE / 'read').mkdir(exist_ok=True)
    cr.record(HERE / 'read', findings=[], coverage=sorted({cr.phash(p) for p in paras}), dispositions={},
              article='HUMANIZED-SO-FAR.md at %s: the paragraph batch r1102b\'s fix changed (FIXES-R1102B.json), read by the '
                      'lead session beside his published version and the paragraphs around it, then linted (E294, E306)'
              % after[:8])
    print(len(FIXES), 'fix;', before[:12], '->', after[:12])


if __name__ == '__main__':
    main()
