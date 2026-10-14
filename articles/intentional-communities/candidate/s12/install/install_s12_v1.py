"""Replace section 12 ("The Math of Absorption, and Who This Isn't For"), still as published in HUMANIZED-SO-FAR.md,
with section 12 v9 (a candidate). Run from candidate/. The chart stays as the article writes its images
("[image 17](url)"); section-v9.md carries it as an IMAGE note for the reviewers."""
import pathlib, re
C = pathlib.Path(__file__).resolve().parents[2]
art = (C / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
pub = (C / 's12/pub-section.md').read_text(encoding='utf-8').strip()
v9 = (C / 's12/section-v9.md').read_text(encoding='utf-8').strip()
img = [b for b in pub.split('\n\n') if b.startswith('[image 17](')]
assert len(img) == 1, 'the published section has no image 17 line; stop'
blocks = v9.split('\n\n')
notes = [i for i, b in enumerate(blocks) if b.startswith('<!-- IMAGE ')]
assert len(notes) == 1, 'section-v9.md should hold one IMAGE note; stop'
blocks[notes[0]] = img[0]
v9 = '\n\n'.join(blocks)
i = art.index('# The Math of Absorption, and Who This Isn’t For')
k = art.index('# Your Little Forming Group Already Is the Community', i)
assert art[i:k].strip() == pub, 'the article does not hold the published section 12; stop'
assert '<!-- CANDIDATE: section 12' not in art, 'a section 12 candidate is already installed; stop'
note = ('<!-- CANDIDATE: section 12 v9 (2026-10-12), "continue" (Joel, 01:02 UTC): Emulate\'s passing shapes with the meaning '
        'put back one change at a time, then the fixes from gate rounds r2 to r5 (s12/DISPOSITIONS-r2.md). Pangram web app: '
        'the section 100% Human ("Human Written", 907 words, 03:32:03 UTC, batch 259g); every paragraph 100% Human alone or '
        'in a run with a neighbor that passes alone (s12/PREDICTIONS-s12.md, 237g to 260g). Records: s12/section-v9.md, '
        's12/candidate-v9-keys.json, s12/fix-v1-parts.json to fix-v4-parts.json, s12/STANCE-LEDGER-s12.md, s12/review-r1 to '
        'review-r5. Open for Joel: questions 17 ("outside review", published) and 18 (the chart and "the same need"), where '
        'the published words stay until he answers. Not accepted until Joel says so. -->\n')
art = art[:i] + note + v9 + '\n\n' + art[k:]
(C / 'HUMANIZED-SO-FAR.md').write_text(art, encoding='utf-8')
print('installed section 12 v9')
