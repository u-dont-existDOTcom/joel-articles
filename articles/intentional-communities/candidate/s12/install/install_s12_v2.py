"""Replace section 12 v9 (installed 2026-10-12 by install_s12_v1.py) in HUMANIZED-SO-FAR.md with section 12 v10c, which
carries Joel's message of 2026-10-12 05:33 UTC: 17b, 18b, P3, P7 and P16 back to the guide's words ("revert those to guide
exactly"), his last sentence of P16, and P22 out of parentheses. Run from candidate/. The chart stays as the article
writes its images ("[image 17](url)")."""
import pathlib, re
C = pathlib.Path(__file__).resolve().parents[2]
art = (C / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
pub = (C / 's12/pub-section.md').read_text(encoding='utf-8').strip()


def with_chart(path):
    blocks = (C / path).read_text(encoding='utf-8').strip().split('\n\n')
    img = [b for b in pub.split('\n\n') if b.startswith('[image 17](')]
    notes = [i for i, b in enumerate(blocks) if b.startswith('<!-- IMAGE ')]
    assert len(img) == 1 and len(notes) == 1, 'image 17 or its IMAGE note is missing; stop'
    blocks[notes[0]] = img[0]
    return '\n\n'.join(blocks)


v9, v10c = with_chart('s12/section-v9.md'), with_chart('s12/section-v10c.md')
start = art.index('<!-- CANDIDATE: section 12 v9 ')
k = art.index('# Your Little Forming Group Already Is the Community', start)
old_note_end = art.index('-->\n', start) + 4
assert art[old_note_end:k].strip() == v9, 'the article does not hold section 12 v9; stop'
note = ('<!-- CANDIDATE: section 12 v10c (2026-10-12), Joel\'s message of 05:33 UTC: 17b ("review by someone who wasn\'t part '
        'of the decision"), 18b ("the same need, or even more of it,"), P3, P7 and P16 back to the guide\'s words ("revert '
        'those to guide exactly"), his last sentence of P16 ("Even then, the power to veto membership applications based on '
        'capacity remains dangerous."), P22 out of its parentheses ("2 parentheticals in a row"); P13 names its subject '
        '("The ability to welcome somebody"), P14 has the guide\'s "available" back. Key-word check PASS '
        '(s12/preservation-keys.json). Pangram web app: Mixed, 30% AI (901 words, 06:41:44 UTC, batch 262g), on the guide\'s '
        'P3 and P16 and once on the list run; every paragraph that isn\'t his or the guide\'s reads 100% Human (s12/PREDICTIONS-s12.md). '
        'Open for Joel: question 19 (P3 and P16 read AI in the guide\'s words). Not accepted until Joel says so. -->\n')
art = art[:start] + note + v10c + '\n\n' + art[k:]
(C / 'HUMANIZED-SO-FAR.md').write_text(art, encoding='utf-8')
print('installed section 12 v10c')
