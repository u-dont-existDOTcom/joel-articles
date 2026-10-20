"""The edits Joel and GPT made to the community article after Pangram 4.1 came out (Joel, 2026-10-20 22:01 UTC: "all the edits
you see between the final full html i'm attaching and the substack paste are because those sections became AI from 4.0 to
4.1"): the approved r04 HTML against his final Substack paste, block by block, each changed run with its words struck and
added. Writes PANGRAM41-EDITS.md. Run from this folder: python3 make_edits_summary.py"""
import difflib, pathlib
from blocks import blocks

HERE = pathlib.Path(__file__).resolve().parent
a = blocks(str(HERE / 'community-r04-approved.html'))
b = blocks(str(HERE / 'community-final-substack-20261020.html'))
ta, tb = [x['text'] for x in a], [x['text'] for x in b]
sm = difflib.SequenceMatcher(None, ta, tb, autojunk=False)
runs = [(op, i1, i2, j1, j2) for op, i1, i2, j1, j2 in sm.get_opcodes() if op != 'equal']
words_a = sum(len(t.split()) for t in ta)
changed = sum(len(' '.join(ta[i1:i2]).split()) for _, i1, i2, _, _ in runs)
out = ['# The community article\'s Pangram 4.1 edits (2026-10-20)', '',
       'Built by `make_edits_summary.py` from `community-r04-approved.html` (the approved r04, read in Pangram 4.0) and '
       '`community-final-substack-20261020.html` (Joel\'s final Substack paste after his and GPT\'s edits for Pangram 4.1). '
       '%d changed runs; %d of the r04\'s %d words are in changed blocks (%.0f%%). Struck words are [-like this-], added '
       'words {+like this+}.' % (len(runs), changed, words_a, 100 * changed / words_a), '']
for n, (op, i1, i2, j1, j2) in enumerate(runs, start=1):
    head = a[i1]['head'] if i1 < len(a) else b[j1]['head']
    wa, wb = ' ¶ '.join(ta[i1:i2]).split(), ' ¶ '.join(tb[j1:j2]).split()
    s = difflib.SequenceMatcher(None, wa, wb, autojunk=False)
    parts = []
    for o, x1, x2, y1, y2 in s.get_opcodes():
        if o == 'equal':
            seg = wa[x1:x2]
            parts.append(' '.join(seg) if len(seg) <= 24 else ' '.join(seg[:10]) + ' … ' + ' '.join(seg[-10:]))
        else:
            if x2 > x1:
                parts.append('[-' + ' '.join(wa[x1:x2]) + '-]')
            if y2 > y1:
                parts.append('{+' + ' '.join(wb[y1:y2]) + '+}')
    out += ['## %d. %s (%d to %d words)' % (n, head, len(wa), len(wb)), '', ' '.join(parts), '']
(HERE / 'PANGRAM41-EDITS.md').write_text('\n'.join(out), encoding='utf-8')
print(len(runs), 'runs;', changed, 'of', words_a, 'words')
