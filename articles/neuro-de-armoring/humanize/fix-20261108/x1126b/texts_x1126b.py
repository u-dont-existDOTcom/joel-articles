#!/usr/bin/env python3
"""His message of 2026-11-26 15:26 UTC (fix-20261108/joel-20261126-1526-message.txt): "70 a 71 ok but i don't want to
say never take 5-HTP with shrooms, that's up to them, and i don't think it shoul dbe a problem in this microdose protocol
either".

70a: both 5-HTP lines around iboga stay as they are. 71: everything I added last turn stays. The rest:

- 'ss', the 5-HTP section's interaction paragraph: "never take 5-HTP on the same day as either one" followed "If you're
  doing psychedelics", so it could be read as every psychedelic; it now names ayahuasca and iboga, and says mushrooms are
  up to the reader, with his view on this protocol's mushroom microdoses, in his words.
- 'who', the 5-HTP section's "Who this is for": "watch out for serotonin syndrome risk if you're ... using serotonergic
  psychedelics/entactogens" would now contradict that (his post had it as "not a casual experiment"; his comment on card
  W-HTPTOP, 2026-11-26 00:50 UTC: "we should change the 5-HTP warning with psychedelics, it's not likely to be dangerous
  with them"), so it keeps the entactogens, which his own list at the top names (MDMA), and leaves the psychedelics to the
  5-HTP section's line.
"""
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parents[1]
ARTICLE = H / 'HUMANIZED-SO-FAR.md'


def plain(s):
    s = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', s)
    s = re.sub(r'(?<![\w*])\*(?=\S)([^*\n]+?)(?<=\S)\*(?![\w*])', r'\1', s)
    return s.replace('**', '')


def _before():
    f = HERE / 'APPLIED-X1126B.json'
    if f.exists():
        import json
        return '\n\n'.join(a['old'] for a in json.loads(f.read_text(encoding='utf-8'))['runs'][0]['applied'])
    return ARTICLE.read_text(encoding='utf-8')


def para(start):
    hits = [p for p in _before().split('\n\n') if p.startswith(start)]
    assert len(hits) == 1, (start, len(hits))
    return hits[0]


OLD = {'ss': para('[Serotonin syndrome](https://medlineplus.gov/ency/article/007272.htm) usually comes from mixing'),
       'who': para('Who this is for: 5-HTP is not for every depressed person either.')}
NEW = {
    'ss': OLD['ss'].replace(
        'never take 5-HTP on the same day as either one, though it\'s fine the day before, or the day after ayahuasca.',
        'never take 5-HTP on the same day as ayahuasca or iboga, though it\'s fine the day before, or the day after '
        'ayahuasca.').replace(
        'While you\'re microdosing iboga, leave 5-HTP out altogether.',
        'While you\'re microdosing iboga, leave 5-HTP out altogether. With mushrooms, it\'s up to you whether to take '
        '5-HTP, and I don\'t think it should be a problem with this protocol\'s mushroom microdoses.'),
    'who': OLD['who'].replace(
        'And watch out for serotonin syndrome risk if you\'re on serotonergic meds, or using serotonergic '
        'psychedelics/entactogens.',
        'And watch out for serotonin syndrome risk if you\'re on serotonergic meds, or using entactogens like MDMA.'),
}
# the double space before "I'd avoid" was a typo
NEW['who'] = NEW['who'].replace(').  I\'d avoid', '). I\'d avoid')
# the version the three fresh readers read (v1/needed, v1/his-fixes, v1/fit: Fable, 2026-11-26)
READ = {'who': NEW['who']}
# what they found in its last sentence, which is the one this turn changes: "watch out for" doesn't say what to do (all
# three), "risk" stands for the thing, "serotonergic meds", "serotonin syndrome" and "entactogens" go unexplained, and the
# fit reader, who takes MDMA and mushrooms, read it as "combine them, just keep an eye out"; so it says what to do, names
# the drugs a reader knows, says what serotonin syndrome is, and points to the list at the top
NEW['who'] = NEW['who'].replace(
    'And watch out for serotonin syndrome risk if you\'re on serotonergic meds, or using entactogens like MDMA.',
    'And don\'t take it with anything else that raises serotonin, like most antidepressants or MDMA, since together they '
    'can cause serotonin syndrome, a dangerous overload of serotonin (the warnings at the top list those drugs).')
# the comparison read of this turn (read-1126f): F1.7, "the day before" could be read as ayahuasca's only; F1.6 and F1.9,
# with the general same-day rule gone, LSD got no word, "up to you" didn't say it meant the same day or a full trip, and
# it sat oddly after "don't take it with anything else that raises serotonin" in the paragraph before; classic
# psychedelics work by acting on serotonin 5-HT2A receptors, not by raising serotonin (Nichols 2016, Pharmacological
# Reviews, https://pmc.ncbi.nlm.nih.gov/articles/PMC4813425/), which is why they aren't in that line
NEW['ss'] = NEW['ss'].replace(
    'though it\'s fine the day before, or the day after ayahuasca.',
    'though it\'s fine the day before either one, or the day after ayahuasca.').replace(
    'With mushrooms, it\'s up to you whether to take 5-HTP, and I don\'t think it should be a problem with this '
    'protocol\'s mushroom microdoses.',
    'Mushrooms and LSD [act on serotonin receptors](https://pmc.ncbi.nlm.nih.gov/articles/PMC4813425/) rather than '
    'raising serotonin, so whether you take 5-HTP on the same day as a trip with them is up to you, and I don\'t think '
    'it should be a problem with this protocol\'s mushroom microdoses.')
assert all(NEW[k] != OLD[k] for k in OLD), [k for k in OLD if NEW[k] == OLD[k]]
MINE = ['who']          # a humanized paragraph that read Human High (fix-20261104/checks/x1104o, b088m): checked again
OWNER_EDITS = ['ss']    # not yet humanized (LEFT.md: never checked as it stands): his answer, fitted


# The humanizing pass, "Psychology is the Software; Biology is the Hardware.": checked as they stand (x1126p), his
# first paragraph and the Gibson paragraph read Human High; "We are operating on about one-sixteenth" (his approved card
# SC-24), the Anti-Breakthrough paragraph and the one after it (his post) read AI, 100%. Each is fixed for sense from the
# three fresh reads of it as it stood (v1/needed, v1/his-fixes, v1/fit: Fable, 2026-11-26), keeping his numbers, his
# sources and his phrase "just to survive the cold". (The underpinnings paragraph, his card version of 2026-11-03, read
# with a Human window, so it goes by small steps next turn; so does the "Underpinning" Principle, Human with Medium
# windows.)
PERRY = 'https://issuu.com/familyjusticegroup/docs/20230629_journal_final/s/27001732'
# the paragraphs as this pass found them (OLD-SW.json, saved from the article at fce359ca before any of them changed)
import json as _json
_SW = _json.loads((HERE / 'OLD-SW.json').read_text(encoding='utf-8'))
OLD.update({k: _SW[k] for k in ('sw19', 'sw22', 'sw23')})
NEW.update({
    # the reads: "relational density" counts nothing a reader can picture; the "Void" arrives unexplained; "cannot simply
    # return" reads as a threat with no reason; "aggressively engineer a High-Density social environment" gives no act;
    # the paragraph after the Gibson one never said it follows from Perry's ratio
    'sw19': ('That works out to about one-sixteenth of the grown-ups per child that our brains evolved with ([Perry, '
             '2023](' + PERRY + ')). So the empty feeling you may carry, the "Void" this guide keeps coming back to, is '
             'real: it\'s what that missing company feels like. Once you\'ve de-armored, going back to a lonely life will '
             'feel worse than it did with the armor on. Gather a tribe around you, people you\'re close to and see '
             'most days, or your brain will eventually reach for the armor again just to survive the cold.'),
    # the reads: the label ran into the sentence; "Micro-Dosing" read as the drug doses; the source came before the
    # point and twice; "metabolize sixty minutes of trauma processing" and "a flood, not a fix" don't say what happens;
    # a reader with years of hour-long therapy heard that it harmed them; the act (doses of seconds) was never said
    'sw22': ('The Anti-Breakthrough (Micro-Dosing): A brain stuck in alarm can often take in healing work for only a few '
             'seconds at a time, Dr. Perry finds. So for now we have to give up on the hour-long breakthrough that '
             'therapy aims for, since an hour spent working on the trauma itself overwhelms an armored nervous system '
             'more than it heals it. Instead, this protocol works in doses of a few seconds, and those small doses are '
             'what I mean by micro-dosing here.'),
    # the reads: "Micro-Dosing Safety" read as how to microdose the drugs; "regulated breathing" said no pattern; the
    # marathon line said S3 again and pointed the wrong way; "Frequency beats intensity" ended on a slogan
    'sw23': ('Your goal is small doses of feeling safe in your body: 30 seconds of slow, steady breathing, twenty '
             'times a day. It works the way physical therapy rebuilds an injured knee, where many short sessions do '
             'more than a long one.'),
})
