"""Cut the overcompletion the whole-guide read found in our words (Joel, 2026-11-03 00:39 UTC, card E-61: "cut all this.
you didn't notice the massive overcompletion here? prob this whole guide is full of it then."; and on card W-685,
2 November: "let's see what other redundancy remains in this article and cut that also").

DECISIONS.json is the lead session's judgment of each reader's candidate (CANDIDATES.json): "cut" (ours: cut here),
"card" (his words: a card on his page, his call), or "keep" (with the reason). This script applies the cuts only, each one
found exactly in its block; a cut of a whole paragraph removes the block, a cut inside one removes the text (or puts in the
"join" the decision gives, when a word has to change), and set_block_text keeps the block's links and italics. It refuses
a cut that would drop a link.

  python3 articles/inner-signal/humanize/fix-20261103/overcompletion/apply_cuts.py [--check]
Writes HUMANIZED-SO-FAR.md, APPLIED-CUTS.json, CUTS.md (every cut, quoted, with what already says it) and read/READ-RECORD.json.
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
SHA = '090588f72475fbddf5528b9db50193bf50572fc5f99542a52fab02e36db15de0'


def tidy(s):
    s = re.sub(r'\s+', ' ', s).strip()
    s = re.sub(r'\s+([,.;:!?)])', r'\1', s)
    return s


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--check', action='store_true')
    a = ap.parse_args()
    md = GUIDE.read_text(encoding='utf-8')
    assert hashlib.sha256(md.encode('utf-8')).hexdigest() == SHA, 'the guide changed since the read'
    bl = sr.blocks(md)
    raw = re.split(r'\n\s*\n', md.rstrip('\n'))
    assert len(raw) == len(bl)
    dec = json.loads((HERE / 'DECISIONS.json').read_text(encoding='utf-8'))
    assert dec['guide_sha256'] == SHA
    cuts = [d for d in dec['decisions'] if d['decision'] == 'cut']
    by_block = {}
    for d in cuts:
        by_block.setdefault(d['block'], []).append(d)
    new_raw, lost, done = {}, [], []
    for i, ds in sorted(by_block.items()):
        text = bl[i]['text']
        whole = False
        for d in ds:
            assert d['cut'] in text, (d['id'], 'not in block %d' % i)
            if d.get('join'):
                assert len(ds) == 1, (d['id'], 'a join and another cut in one block')
                text = d['join']
            elif d['cut'].strip() == text.strip():
                whole = True
                text = ''
            else:
                text = tidy(text.replace(d['cut'], ' ', 1))
            done.append(d['id'])
        if whole or not tidy(text):
            # one cut of the whole paragraph, or cuts that together take all of it (P2a-06 and P2a-07)
            assert len(ds) == 1 or not tidy(text), (i, 'a whole-paragraph cut and another cut in one block')
            new_raw[i] = []
        else:
            before = len(lost)
            new_raw[i] = [set_block_text(raw[i], text, lost)]
            assert len(lost) == before, (i, 'a cut would drop a link', lost[before:])
    out = []
    for j, r in enumerate(raw):
        out += new_raw.get(j, [r])
    new = '\n\n'.join(out) + '\n'
    after = hashlib.sha256(new.encode('utf-8')).hexdigest()
    nb = sr.blocks(new)
    counts = {}
    for d in dec['decisions']:
        counts[d['decision']] = counts.get(d['decision'], 0) + 1
    words_cut = sum(len(bl[i]['text'].split()) for i in new_raw) - sum(
        len(sr.blocks(x)[0]['text'].split()) for i in new_raw for x in new_raw[i])
    rec = {'before_sha256': SHA, 'after_sha256': after, 'blocks': [len(bl), len(nb)], 'cuts_applied': done,
           'changed_blocks_before': sorted(new_raw), 'decisions': counts, 'words_cut': words_cut}
    print(json.dumps(rec, indent=1))
    if a.check:
        return
    GUIDE.write_text(new, encoding='utf-8')
    (HERE / 'APPLIED-CUTS.json').write_text(json.dumps(rec, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    lines = ['# What the overcompletion read cut from the guide (3 November)', '',
             'Joel, on card E-61 (2026-11-03 00:39 UTC): "cut all this. you didn\'t notice the massive overcompletion here? '
             'prob this whole guide is full of it then." Six fresh readers read the guide in six parts (BRIEF.md); the lead '
             'session judged every candidate (DECISIONS.json). These are the cuts in our words, each with what already said '
             'it. The guide went from %s to %s (%d blocks to %d, about %d words fewer). Block numbers are the guide\'s '
             'before the cuts.' % (SHA[:8], after[:8], len(bl), len(nb), words_cut), '']
    for d in cuts:
        lines += ['- **[%d] %s** (%s): ~~%s~~' % (d['block'], sr.where(bl, d['block']), d['kind'], d['cut'])]
        if d.get('join'):
            lines += ['  - now reads: %s' % d['join']]
        lines += ['  - already said: %s' % d['already_said']]
    others = [d for d in dec['decisions'] if d['decision'] != 'cut']
    if others:
        lines += ['', '## Not cut here', '']
        for d in others:
            lines += ['- **[%d] %s** (%s; %s): %s' % (d['block'], sr.where(bl, d['block']), d['decision'], d.get('whose', ''),
                                                     d['cut']), '  - why: %s' % d['why']]
    (HERE / 'CUTS.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')
    olds = {b['text'] for b in bl}
    changed = [b['text'] for b in nb if b['text'] not in olds]
    rd = HERE / 'read'
    rd.mkdir(parents=True, exist_ok=True)
    cr.record(rd, findings=[], coverage=sorted({cr.phash(t) for t in changed}), dispositions={},
              article='HUMANIZED-SO-FAR.md at %s: the %d paragraphs the overcompletion cuts changed, each read in place with '
                      'the paragraphs around it by the lead session (E284, E294, E328)' % (after[:8], len(changed)))


if __name__ == '__main__':
    main()
