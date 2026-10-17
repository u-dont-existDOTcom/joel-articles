"""Install what batch 422g read Human, for Joel's 48 a and 51 a of 2026-10-17 21:37 UTC (the tightening and question-answer pass,
make_tighten.py): section 13 v36 and section 15 v16, each in place of the section now there, with a new note in front of the old
one. A section goes in only if 422g read it whole Human with no AI window and every check of its changed paragraphs (alone, and
with each neighbor when one of the two is under 50 words) Human. Section 16 v31 ("can" for "CAN") read AI whole, one 96-word
window around the "So what?" paragraph (S16v31), so section 16 stays v30; section 2's two variants read AI in their first window,
installed text (S2v34a, S2v34b), so section 2 stays v3.2 and section 12 v15. Idempotent. Run from candidate/:
python3 fix-20261017d/install_422.py"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent
C = HERE.parent
ART = C / 'HUMANIZED-SO-FAR.md'
R = json.loads((HERE / 'b422' / 'b422-results.json').read_text(encoding='utf-8'))
G = json.loads((HERE / 'b422' / 'GATE.json').read_text(encoding='utf-8'))
ok = lambda k: k in R and R[k][0].startswith('Human') and R[k][3].startswith('Human') and '; AI' not in R[k][3]
link = lambda k: 'https://www.pangram.com/history' + R[k][5]
J = 'Joel\'s message of 21:37 UTC (joel-20261017/joel-20261017-2137-message.txt'
SECT = [
    ('S13v36', '# Your Little Forming Group Already Is the Community', C / 's13' / 'v36.md', '<!-- ACCEPTED: section 13 v35', 'ACCEPTED',
     'section 13 v36 (2026-10-17, after %s, 48 a and 51 a): the tightening, in the four paragraphs where the march let it through: '
     'the conflict paragraph with one "dealt with it" fewer and no capitals ("Dealing with it for real" is the tone reader\'s '
     'wording), "visibility" in lower case with the published anchor back ("A money-free community still has scarce things and '
     'bottlenecks, sorry."), the provisional-membership questions folded into fewer (the last in the tone reader\'s wording), and '
     'the repeat of section 9 out ("But when power had crept up in their own system over the years, it took them a long review to '
     'push it back down."). His "Very important!" and "Lots of decisions to make!" stay ("leave those in actually, they are ok"), '
     'and so do the question-answer lines that the march found were their paragraph\'s only turn (make_tighten.py, HELD)' % J),
    ('S15v16', '# What This Looks Like From Sénégal', C / 's15' / 'v16.md', '<!-- CANDIDATE: section 15 v15', 'CANDIDATE',
     'section 15 v16 (2026-10-17, after %s, 51 a): "Kind of the opposite problem." for "Kind of the opposite problem, isn\'t it?"; '
     'the other question-answer lines stay, each its paragraph\'s only turn (make_tighten.py, HELD)' % J),
]
md = ART.read_text(encoding='utf-8')
for key, h1, path, old_note, word, what in SECT:
    parts = [p for p in G[key]['parts'] if p != 'installed']
    bad = [p for p in [key] + parts if not ok(p)]
    if bad:
        print(key, 'not installed:', bad)
        continue
    new = path.read_text(encoding='utf-8').strip()
    if new in md:
        print(key, 'already in'); continue
    a = md.index(h1)
    m = re.search(r'\n(<!-- CANDIDATE|<!-- ACCEPTED|<!-- Section|# )', md[a + 3:])
    md = md[:a] + new + '\n' + md[a + 3 + m.start():]
    i = md.index(old_note)
    note = ('<!-- %s: %s. Pangram web app (422g): every changed paragraph Human alone and with its short neighbors, the whole section '
            '%s (%s). Records: fix-20261017d/. Before: -->\n' % (word, what, R[key][0].replace(' Written', ''), link(key)))
    md = md[:i] + note + md[i:]
    print(key, 'installed')
ART.write_text(md, encoding='utf-8')
for k in ('S16v31', 'S2v34a', 'S2v34b'):
    print(k, 'stays out:', R[k][0], R[k][1], R[k][3], link(k))
