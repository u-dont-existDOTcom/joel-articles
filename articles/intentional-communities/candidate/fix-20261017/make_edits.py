"""Sections 4 and 12 (2026-10-17 13:11 UTC): Joel's answer to question 39 and the PsyPost study he sent
(joel-20261017/joel-20261017-1311-message.txt). Writes s4-v11.4.md and s12-v14.md here, each the section as it stands in
HUMANIZED-SO-FAR.md (from its heading to the next CANDIDATE note or the next section) with the change in.
- Section 4, "4. The container": "39. i'd say it's the practical logistical foundation that gets built once the architects can
  work well together, does that work?" His answer fitted to its place, after "The first three parts are the inside of the
  container, and this container is what gives those a stable place to manifest.": "I'd say" dropped (a definition of his own
  model's fourth part, which section 4's opening names "the practical logistical foundation"), "It's" capitalized.
- Section 12, after P2 ("... Instead we optimize to fit the career market with all the little energy we've got."): "i also want
  to add this link and screenshot somewhere in the article where it belongs (altho it's kind of a "no, duh" study)". The study
  (Elnakouri, Finkel and Scholer, Social Psychological and Personality Science, written up by PsyPost on 2026-10-15) found that
  where relationships are easy to form and end, people share reality more selectively with whoever helps them reach their goals
  (the experiment used career contacts), partly by feeling less in sync with whoever doesn't. It fits P2's career market. A new
  paragraph of mine with his link and his "no, duh", then the screenshot as an image note (tools/humanization/article_images.py),
  which keeps the page's paragraph numbers.
And the sweep of the checks made from his corrections (fix-20261017/SWEEP-20261017.md), in sections not yet accepted:
- Section 1 (no version name; the first section humanized): "It's the sort of thing that doesn't make it into the history books."
  stood for the published "These are the questions history books neglect." (R2, his "this is not the same as it"): "That's".
- Section 8 v29 -> v30: "Older kids can't be allowed to quietly boss the younger ones around there." (O42, his "remove "quietly"
  that's an ai tell"): "quietly" out; the sentence before ("The adults still have to pay attention to what goes on in a children's
  territory.") carries the published "quietly dominate", the dominating adults don't see.
Writes s1-swept.md and s8-v30.md too.
Run from candidate/: python3 fix-20261017/make_edits.py"""
import pathlib, re

HERE = pathlib.Path(__file__).resolve().parent
C = HERE.parent
art = (C / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')


def section(h1):
    a = art.index(h1)
    m = re.search(r'\n(<!-- CANDIDATE|<!-- Section|# )', art[a + 3:])
    return art[a:a + 3 + m.start()].strip()


S4 = section('# The Four Parts That Have to Pl/ork Together')
OLD4 = 'The first three parts are the inside of the container, and this container is what gives those a stable place to manifest.'
NEW4 = OLD4 + " It's the practical logistical foundation that gets built once the architects can work well together."
assert S4.count(OLD4) == 1
(HERE / 's4-v11.4.md').write_text(S4.replace(OLD4, NEW4) + '\n', encoding='utf-8')

S12 = section('# The Math of Absorption, and Who This Isn’t For')
OLD12 = "Instead we optimize to fit the career market with all the little energy we've got."
URL = 'https://www.psypost.org/social-freedom-shapes-whose-version-of-reality-you-adopt-new-research-suggests/'
IMG = ('https://raw.githubusercontent.com/u-dont-existDOTcom/joel-articles/d8252275008b83064aa2ed7d89b183898097c262/'
       'articles/intentional-communities/candidate/images/psypost-relational-mobility.png')
# The first wording ("A new study found the same goes for how we see the world. Where relationships are easy to make and break,
# people line up their view of reality with whoever helps them reach their goals, and feel less on the same page with whoever
# doesn't. ...") passed the source check (SOURCE-s12.md: OK), but the cold read (SENSE-s12.md) couldn't tell what "the same"
# was or why the study was there, and found the image repeating it. The source check also found the "closer to helpers" half
# the weaker one ("Shared reality with helpful contacts did not differ between conditions"). So the paragraph keeps the strong
# half, ties it to the career market with "even", and leaves the rest to the screenshot.
NEWP = ('A [new study](%s) found that where relationships are easy to make and break, people even feel less on the same page '
        'with whoever doesn\'t help them reach their goals. Kind of a "no, duh" study, but still.' % URL)
NOTE = ('<!-- IMAGE %s : a screenshot of the opening of PsyPost\'s write-up of the study: new research suggests that the culture '
        'or social setting we live in shapes whose version of the world we adopt, and that where relationships are easily formed '
        'and broken, people line up their worldviews more selectively with the people who help them reach their goals; published '
        'in Social Psychological and Personality Science. -->\n<!-- The screenshot is Joel\'s, sent 2026-10-17 13:11 '
        '(candidate/images/psypost-relational-mobility.png); the Substack image goes in when he uploads it. -->' % IMG)
assert S12.count(OLD12) == 1
(HERE / 's12-v14.md').write_text(S12.replace(OLD12, OLD12 + '\n\n' + NEWP + '\n\n' + NOTE) + '\n', encoding='utf-8')
A1 = art.index('# The New Age May Dawn Suddenly')
S1 = art[:art.index('<!-- CANDIDATE: section 2')].strip()
OLD1, NEW1 = ("It's the sort of thing that doesn't make it into the history books.",
              "That's the sort of thing that doesn't make it into the history books.")
assert S1.count(OLD1) == 1
(HERE / 's1-swept.md').write_text(S1.replace(OLD1, NEW1) + '\n', encoding='utf-8')
S8 = section('# The Grown Children Get the Final Review')
OLD8, NEW8 = ("Older kids can't be allowed to quietly boss the younger ones around there.",
              "Older kids can't be allowed to boss the younger ones around there.")
assert S8.count(OLD8) == 1
(HERE / 's8-v30.md').write_text(S8.replace(OLD8, NEW8) + '\n', encoding='utf-8')
print('wrote s4-v11.4.md, s12-v14.md, s1-swept.md and s8-v30.md')
