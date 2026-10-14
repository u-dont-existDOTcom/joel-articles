"""Replace section 12 v10f (install_s12_v3.py) in HUMANIZED-SO-FAR.md with v11: Joel's P3 and P16 of 2026-10-12 17:23 UTC
as written, P14 and P15 with their lists broken his way, and P14's "absorb disruption" and "the new member's heart" back
(trace r6). Run from candidate/."""
import pathlib
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


old, new = with_chart('s12/section-v10f.md'), with_chart('s12/section-v11.md')
start = art.index('<!-- CANDIDATE: section 12 v10f ')
k = art.index('# Your Little Forming Group Already Is the Community', start)
note_end = art.index('-->\n', start) + 4
assert art[note_end:k].strip() == old, 'the article does not hold section 12 v10f; stop'
note = ('<!-- CANDIDATE: section 12 v11 (2026-10-12). Joel\'s message of 17:23 UTC: his P3 ("human, best") and P16 ("let\'s keep '
        'this one, best one"), as written; before that, 05:33: 17b, 18b, P7 in the guide\'s words, P22 out of parentheses. Mine: P14\'s '
        'five-item list as two pairs and a sentence and P15\'s third item in its own sentence (his list rule), P14\'s "absorb '
        'disruption" and "the new member\'s heart" back (trace r6), P13 names its subject, P22 keeps "every limit". Key-word check '
        'PASS. Pangram web app: the section 100% Human ("Human Written", 944 words, 17:43:06 UTC, batch 273g); each paragraph of '
        'mine alone or in a run that passes (s12/PREDICTIONS-s12.md). Not accepted until Joel says so. -->\n')
art = art[:start] + note + new + '\n\n' + art[k:]
(C / 'HUMANIZED-SO-FAR.md').write_text(art, encoding='utf-8')
print('installed section 12 v11')
