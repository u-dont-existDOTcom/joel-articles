"""Our fixes of batch w1102's windows that read Human in their checks (batch w1102f, RESULTS.md), put into the guide, and
every edit's fate recorded (APPLIED-W1102F.json).

In: F-20, F-42, F-140, F-255, F-265 (each read Human Written in its section, and none is flagged in the whole halves, but
F-20's window, which also holds his teleprompter sentence, reads AI (Low) in the whole as the one it replaced did).
Reverted: F-11, F-16, F-218, F-251, F-253, F-527, F-528 (each made its section read worse; the ledger explains each).
Not in yet: F-216 (Human in its section, its seatbelt sentence AI (High) in the whole).
Cards: C-141, C-384. Not cards: C-672 (the owner-delivery gate's preservation review failed it, gate/GATE.md) and C-626
(his own line read AI (High) here).

  python3 articles/inner-signal/humanize/fix-20261102/w1102fix/apply_w1102f.py [--check]
"""
import argparse
import hashlib
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parents[1]
ROOT = H.parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(H / 'fix-20261025' / 'review'))
import compare_read as cr  # noqa: E402
import fixes_w1102 as fx  # noqa: E402
import suggestion_review as sr  # noqa: E402

IN = ['F-20', 'F-42', 'F-140', 'F-255', 'F-265']
FATES = {
    'F-11': 'reverted: AI (Low, High, Medium) in its section (w1102f-02); the original read Human there',
    'F-16': 'reverted: AI (High) in its section and in the whole',
    'F-20': 'in: its section Human Written, 0% AI; in the whole its window (with his teleprompter sentence) AI (Low), as before',
    'F-42': 'in: its section Human Written, 0% AI; not flagged in the whole',
    'F-140': 'in: its section Human Written, 0% AI (with C-141); not flagged in the whole',
    'F-216': 'not in yet: its section Human Written, its seatbelt sentence AI (High) in the whole',
    'F-218': 'reverted: its section Mostly Human, the heading and next sentence Human (Low) once it was cut',
    'F-251': 'reverted: AI (Low) in its section, AI (High) in the whole',
    'F-253': 'reverted: AI (High) and three AI (Low) in its section',
    'F-255': 'in: not flagged in its section or in the whole',
    'F-265': 'in: not flagged in its section or in the whole',
    'F-527': 'reverted: AI (Medium) in its section and in the whole',
    'F-528': 'reverted: Human (Low) in its section, AI (High) in the whole',
    'C-141': 'card: his inner child guide\'s lines; its section Human Written, 0% AI; not flagged in the whole',
    'C-384': 'card: his inner child guide\'s lines; its section Human Written, 0% AI; Human (Low) in the whole, as before',
    'C-626': 'withdrawn: his inner child guide\'s line read AI (High) in its section and in the whole',
    'C-672': 'not a card: its section Human Written, 0% AI, and not flagged in the whole, but the owner-delivery gate\'s '
              'preservation review failed it ("whole life" dropped, his "I\'m" made "We\'re", his "But" lost; gate/GATE.md)',
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--check', action='store_true')
    a = ap.parse_args()
    guide = H / 'HUMANIZED-SO-FAR.md'
    md = guide.read_text(encoding='utf-8')
    new = fx.apply(md, kinds=('ours',), only=set(IN))
    assert set(FATES) == {e[0] for e in fx.EDITS}
    rec = {'before_sha256': hashlib.sha256(md.encode('utf-8')).hexdigest(),
           'after_sha256': hashlib.sha256(new.encode('utf-8')).hexdigest(), 'in': IN, 'fates': FATES,
           'blocks': [len(sr.blocks(md)), len(sr.blocks(new))], 'results': 'RESULTS.md (batch w1102f)'}
    print(json.dumps(rec, indent=1))
    if a.check:
        return
    guide.write_text(new, encoding='utf-8')
    (HERE / 'APPLIED-W1102F.json').write_text(json.dumps(rec, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    olds = {b['text'] for b in sr.blocks(md)}
    changed = [b['text'] for b in sr.blocks(new) if b['text'] not in olds]
    d = HERE / 'read'
    d.mkdir(exist_ok=True)
    cr.record(d, findings=[], coverage=sorted({cr.phash(t) for t in changed}), dispositions={},
              article='HUMANIZED-SO-FAR.md at %s: the %d paragraphs our w1102f fixes changed (F-20, F-42, F-140, F-255, F-265), '
                      'read by the lead session in place beside his published version and his inner child guide (E284, E294)'
                      % (rec['after_sha256'][:8], len(changed)))


if __name__ == '__main__':
    main()
