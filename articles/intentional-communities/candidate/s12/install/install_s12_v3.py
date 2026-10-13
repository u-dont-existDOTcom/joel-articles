"""Replace section 12 v10c (installed by install_s12_v2.py) in HUMANIZED-SO-FAR.md with v10f: v10c with two words of the
published text back, which the sweep of 2026-10-12 found narrowed (sweep-20261012/sweep-G8.md): P13's "fix whatever
breaks" (published "equipment repaired"; v10c "fix the cars") and P22's "or anyone else it can't take right now"
(published "every limit"; v10c only "people who fall into these categories"). Run from candidate/."""
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


v10c, v10f = with_chart('s12/section-v10c.md'), with_chart('s12/section-v10f.md')
start = art.index('<!-- CANDIDATE: section 12 v10c ')
k = art.index('# Your Little Forming Group Already Is the Community', start)
note_end = art.index('-->\n', start) + 4
assert art[note_end:k].strip() == v10c, 'the article does not hold section 12 v10c; stop'
note = ('<!-- CANDIDATE: section 12 v10f (2026-10-12), Joel\'s message of 05:33 UTC: 17b ("review by someone who wasn\'t part '
        'of the decision"), 18b ("the same need, or even more of it,"), P3, P7 and P16 back to the guide\'s words ("revert '
        'those to guide exactly"), his last sentence of P16 ("Even then, the power to veto membership applications based on '
        'capacity remains dangerous."), P22 out of its parentheses ("2 parentheticals in a row"); P13 names its subject '
        '("The ability to welcome somebody"), P14 has the guide\'s "available" back, and the sweep for the same kind of break '
        'put back the published generality in P13 ("fix whatever breaks") and P22 ("or anyone else it can\'t take right now"). '
        'Key-word check PASS (s12/preservation-keys.json). Pangram web app: Mixed, 30% AI (910 words, 07:44:50 UTC, batch '
        '265g), on the guide\'s P3 and P16 and the list run, as v10c; every paragraph that isn\'t his or the guide\'s reads 100% '
        'Human alone or with a neighbor (s12/PREDICTIONS-s12.md). Open for Joel: question 19 (P3 and P16 read AI in the '
        'guide\'s words). Not accepted until Joel says so. -->\n')
art = art[:start] + note + v10f + '\n\n' + art[k:]
(C / 'HUMANIZED-SO-FAR.md').write_text(art, encoding='utf-8')
print('installed section 12 v10f')
