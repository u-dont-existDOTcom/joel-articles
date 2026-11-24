#!/usr/bin/env python3
"""Put his answers of 2026-11-24 into HUMANIZED-SO-FAR.md: his versions on cards W-LMA and W-AGM (exported 18:40 UTC,
../x1123c/ANSWERS-X1123C-20261124-1840.json; he checked both himself, each Human Written, one window, High) and his
answers 57 to 61 (his message of 18:47 UTC: ../joel-20261124-1847-message.txt; the questions: ../../OWNER-QUESTIONS.md).

- W-LMA: his lion's mane and ashwagandha item, a paragraph of its own between the Cognitive Warning and the Agmatine
  Warning, as he checked it.
- W-AGM: his version replaces the agmatine stop-signs paragraph at the top (the one the cycle rule and Weeks 1-2 point
  to), as he checked it; only the trailing space goes.
- 57: "right", and the article does say it extrapolates D-serine from DCS (section B: the drug tested with exposure
  therapy is DCS, which works on the same spot, and "DCS (and maybe D-serine) helps that stick"). So the D-Serine
  section's sentence names DCS, the drug those studies tested, with section B's own "(and maybe d-serine)" for the
  extrapolation, and DCS links to section B, where the reader meets it.
- 58: his amounts and notes, fitted as a note right after the daily list that names zinc and L-serine (every point of
  his answer has its place: POINTS below). Two sources for what he says the studies show, in the article's citation form.
- 59a, 60a, 61a: as the options said.

  python3 articles/neuro-de-armoring/humanize/fix-20261108/x1124a/apply_x1124a.py [--write]
"""
import hashlib
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parents[1]
ARTICLE = H / 'HUMANIZED-SO-FAR.md'
ANSWERS = HERE.parent / 'x1123c' / 'ANSWERS-X1123C-20261124-1840.json'
U = 'https://ibogaqueen.substack.com/i/181671197/'
B, C = U + 'b-the-overheating-cpu-glutamate-excitotoxicity', U + 'c-the-hardened-circuit-dynorphin-and-deltafosb'

CARDS = {i['id']: i for i in json.loads(ANSWERS.read_text(encoding='utf-8'))['items']}
W_LMA = CARDS['W-LMA']['your_version']
W_AGM = CARDS['W-AGM']['your_version'].rstrip()  # the trailing space goes (an obvious correction)
assert hashlib.sha256(CARDS['W-LMA']['your_version'].encode()).hexdigest().startswith('fc9503e7')  # = his check 37022ca4
assert hashlib.sha256(CARDS['W-AGM']['your_version'].encode()).hexdigest().startswith('9ee2f6e3')  # = his check 2406fb09

OLD_AGM = ('Stop immediately if it causes flatness, anhedonia, apathy, emotional blunting, new depression, agitation, '
           'irritability, insomnia, dizziness, palpitations, nausea, loose stools, diarrhea, or increased craving. Only '
           'the stomach problems showed up in the human trials, but the flatness happens in practice, so do not "push '
           'through" numbness. If agmatine makes the world more gray, it is the wrong tool for that phase.')

NOTE_58 = ("For the zinc, I'd use zinc carnosine, up to 75 mg daily (16 mg elemental zinc), which is a standard dose. "
           "This form also helps repair leaky gut ([Mahmood, et al, 2007](https://pmc.ncbi.nlm.nih.gov/articles/PMC1856764)), "
           "and it's better tolerated than other forms of zinc, but if it causes nausea, take less at a time. Zinc should "
           "be taken with copper (1–2 mg elemental; avoid cupric oxide, and use copper gluconate or citrate). For "
           "L-serine, I'd do 5–15 g, depending how it feels. Up to 30 g has been used in trials for neurodegenerative "
           "conditions ([Levine, et al, 2017](https://doi.org/10.1080/21678421.2016.1221971)), but with more GI distress "
           "at higher doses.")

# every point of his 58, with where it went (lesson bad-trips-2026-11-23o)
POINTS_58 = [
    ("I'd use zinc carnosine", 'the note: "For the zinc, I\'d use zinc carnosine"'),
    ('up to 75mg daily (16mg elemental zinc) which is a standard dose', 'the note, as he said it'),
    ('this form also helps repair leaky gut', 'the note, with Mahmood 2007 (37.5 mg twice daily kept healthy volunteers\' '
                                              'gut permeability from rising on indomethacin)'),
    ('zinc should be taken with copper (1-2mg elemental, avoid cupric oxide, use copper gluconate or citrate)',
     'the note, as he said it'),
    ('zinc carnosine is better trolerated than other forms of zinc, but if it causes nausea take less at a time',
     'the note, joined to the zinc carnosine sentences before copper ("trolerated" spelled right)'),
    ("L-serine I'd do 5-15g depending how it feels", 'the note: "For L-serine, I\'d do 5–15 g, depending how it feels."'),
    ('Up to 30g has been used in trials for neurodegenerative conditions, but more GI distress at higher doses',
     'the note, with Levine 2017 (the ALS phase I trial: up to 15 g twice daily; two of 20 left with stomach problems) '
     'for the trials, and "with" for the grammar'),
]

EDITS = [
    ('57', 'Some studies suggested that d-serine is more effective at this',
     'Some studies suggested that [DCS](' + B + ') (and maybe d-serine) is more effective at this'),
    ('59a', 'Mechanism: You feel "dead."',
     'Mechanism: DeltaFosB is still holding the armor (see [section C](' + C + ')). You feel "dead."'),
    ('60a', 'The Dynorphin Bridge (Apathy / DAWS-pattern Void):', 'The Void Bridge (Apathy / DAWS-pattern Void):'),
    ('61a', 'on the nights after each kind of day.', 'on the nights after a microdose day and a day without.'),
    ('W-AGM', OLD_AGM, W_AGM),
]


def main(write):
    text = ARTICLE.read_text(encoding='utf-8')
    before = hashlib.sha256(text.encode('utf-8')).hexdigest()
    applied = []
    for ans, old, new in EDITS:
        if text.count(old) != 1:
            sys.exit('%s: %d matches for %r' % (ans, text.count(old), old[:70]))
        text = text.replace(old, new, 1)
        applied.append({'answer': ans, 'old': old, 'new': new})
    lines = text.split('\n')
    # W-LMA: his item, a paragraph of its own right before the Agmatine Warning
    (j,) = [k for k, l in enumerate(lines) if l.startswith('Agmatine Warning (The Voltage Governor):')]
    assert lines[j - 1] == '' and lines[j - 2].startswith('The armored brain projects its own internal threat level')
    lines[j:j] = [W_LMA, '']
    applied.append({'answer': 'W-LMA', 'inserted': W_LMA, 'before': lines[j + 2][:60]})
    # 58: the note right after the daily list
    (d,) = [k for k, l in enumerate(lines) if l.endswith('+ Magnesium Glycinate 400 mg with zinc at night + L-Serine + '
                                                          'NAC 1.8–2.4 g divided.')]
    assert lines[d - 2] == 'Supplement daily:' and lines[d + 1] == '' and lines[d + 2].startswith('Optional add-on: Agmatine')
    lines[d + 1:d + 1] = ['', NOTE_58]
    applied.append({'answer': '58', 'inserted': NOTE_58, 'after': 'the Weeks 1-2 daily list'})
    out = '\n'.join(lines)
    rec = {'about': 'his cards W-LMA and W-AGM (his versions, exported 2026-11-24 18:40 UTC) and his answers 57 to 61 '
                    '(his message of 2026-11-24 18:47 UTC)',
           'message': '../joel-20261124-1847-message.txt', 'cards': '../x1123c/ANSWERS-X1123C-20261124-1840.json',
           'his_checks': {
               'W-LMA': ['https://www.pangram.com/history/e8bbd7a1-a04b-40f6-9bcd-54b789bad815 (AI Generated, 99.99% AI: '
                         'AI Low, AI Medium, AI High)',
                         'https://www.pangram.com/history/04bff64d-2281-41c4-8abe-2bd3e49407eb (AI Detected, 42% AI: '
                         'Human High, AI Low, AI Medium)',
                         'https://www.pangram.com/history/37022ca4-704b-48af-a7d3-150d3700c3c2 (Human Written, one window '
                         'of 68 words, High): the text that went in'],
               'W-AGM': ['https://www.pangram.com/history/2406fb09-5b1d-4236-b141-e1becf296cf9 (Human Written, one window '
                         'of 103 words, High): the text that went in, less its trailing space']},
           'whose': 'his versions as he checked them; his words for 58, fitted after the list; the words of the options he '
                    'picked for 59a to 61a; for 57, section B\'s own words',
           'answer_57': 'his "right ... i\'m extrapolating d-serine results mostly from DCS, didn\'t it say that?": it '
                        'does, in section B ("DCS (and maybe D-serine) helps that stick", Smits 2013), so the sentence '
                        'keeps the point and says what was tested, with the extrapolation as section B puts it',
           'points_58': [{'point': p, 'went': w} for p, w in POINTS_58],
           'w_agm_signs': 'his version names flat and numb, flatter or more depressed, wound up (more irritable, can\'t '
                          'sleep), dizziness, palpitations, nausea, loose stools and stronger cravings; the old list\'s '
                          '"anhedonia", "apathy" and "emotional blunting" are in his "flat and numb" and "flatter", '
                          '"diarrhea" in "loose stools" (his note: "you had some redundancy")',
           'applied': applied,
           'before_sha256': before, 'after_sha256': hashlib.sha256(out.encode('utf-8')).hexdigest()}
    print('before', before[:8], 'after', rec['after_sha256'][:8], len(applied), [a['answer'] for a in applied])
    if write:
        ARTICLE.write_text(out, encoding='utf-8')
        (HERE / 'APPLIED-X1124A.json').write_text(json.dumps(rec, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')


if __name__ == '__main__':
    main('--write' in sys.argv)
