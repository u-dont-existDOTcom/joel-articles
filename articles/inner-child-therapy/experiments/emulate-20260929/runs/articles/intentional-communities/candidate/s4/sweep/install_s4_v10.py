"""Section 4 v10 (2026-10-12): Relational pl/ork P6 back to what the published sentence says. Joel, 17:23 UTC: "oops, yeah we
can't replace "dyads" with "romance" that's not the same concept." Pangram: 100% Human in its run and in the section (272g).
Run from candidate/."""
import pathlib
C = pathlib.Path(__file__).resolve().parents[2]
art = (C / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
link = '[Romance Guide](https://ibogaqueen.substack.com/p/romance-advice-i-wish-my-parents)'
old = ('Also, read my ' + link + ', because no matter how much your founding document says that you’re all beyond romance, '
       'you’re still gonna have dyads.')
new = ('Also, read my ' + link + '. It covers the dyads that will form whether your founding document acknowledges romance or '
       'pretends you’re all beyond it.')
assert art.count(old) == 1, 'section 4 P6 is not as v9 has it; stop'
art = art.replace(old, '<!-- 2026-10-12: section 4 v10, this sentence back to the published meaning (the guide covers the dyads; '
                  'the document is about romance; both cases). Joel 17:23: "we can\'t replace "dyads" with "romance" that\'s not the '
                  'same concept." 100% Human in its run and the section, 272g (s4/sweep/PREDICTIONS-272g.md). -->\n' + new)
(C / 'HUMANIZED-SO-FAR.md').write_text(art, encoding='utf-8')
print('installed section 4 v10')
