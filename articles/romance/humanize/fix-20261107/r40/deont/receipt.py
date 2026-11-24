#!/usr/bin/env python3
"""The receipt for "De-ontologizing Twin Flames FTW", his live words with one correction of mine: the pointer back to
"Seeing idealization right" took the heading's name (it said "doing Idealization right"; the contradictions read, item 5)."""
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[5]
FILL = [
    ('it warns that what follows sounds unromantic but leads to deeper love', 'the section heading', None),
    ('he has reconciled the pragmatists and the fairy-tale idealists', 'it says what the unromantic part does', 'I’ve basically synthesized the'),
    ('a joke about how rare that view is in a partner', 'it follows his claim with a wry aside', 'If only I could find'),
    ('the twin flame isn’t two unique people destined to meet', 'it starts the synthesis he promised', 'Basically, the Twin Flame experience'),
    ('he grants they are matched in some ways', 'it concedes part of what he just denied', 'Well, they are uniquely'),
    ('what is unique is reaching each other’s most vulnerable heart', 'it says what the uniqueness really is', 'But what’s really unique'),
    ('Key’s example: feeling safe, she slipped into that archetype', 'an example of reaching that corner', 'When Key felt understood'),
    ('Bee’s example: the same, often', 'a second example of the same', 'Bee did the same'),
    ('what that state was like for them', 'it describes the state both examples reached', 'In that state I'),
    ('what the safety brought out in them', 'it says what the state brought out', 'The safety brought out'),
    ('what it did to him, as a joke', 'the effect on him of what it brought out', 'It made me like'),
    ('the mistake: taking the flaws for the deepest self, as Ann did with the song', 'it returns from the examples to the point', 'Anyway, if we don’t'),
    ('he isn’t bashing the song', 'it softens the jab at the song just played', 'Ok, I’m not trying'),
    ('he grants its beauty', 'it says why he isn’t bashing it', 'It’s one of the'),
    ('the part of it that is right: a partner needs to feel accepted', 'it says what in the song applies', 'And there’s a part'),
    ('the toxic part: accepting everything makes you a doormat', 'the other side of the song', 'But there’s a toxic'),
    ('love means being a good influence, as the earlier section said', 'it points back to where he said it', 'This goes back to'),
    ('what that influence looks like', 'it says what being a good influence means', 'That means showing them'),
    ('saying that this deeper self is why you love them', 'a further part of the same influence', 'none: it continues the list the sentence before began, in his clipped style'),
    ('not their flaws and not desperation', 'it says what the love is not for', 'Not because they are'),
    ('the summary: accept the person and help them toward their chosen self, as the Faker song says', 'it sums up the section', 'You accept the imperfect'),
]
text = HERE.parent / 'checks' / 'CHECK-r40-66-de-ontologizing-twin-flames-ftw.txt'
out = HERE / 'R-66.json'
subprocess.run([sys.executable, str(ROOT / 'tools/humanization/sense_receipt.py'), 'make', str(text), '--section',
                'De-ontologizing Twin Flames FTW 💗', '--reader', 'Someone wondering whether twin flames are real, and what '
                'to do with the idea if they\'ve felt it', '--out', str(out)], check=True, capture_output=True)
R = json.loads(out.read_text(encoding='utf-8'))
assert len(R['sentences']) == len(FILL)
for s, (pay, fol, link) in zip(R['sentences'], FILL):
    s['payoff'], s['follows'] = pay, fol
    if link is not None:
        s['link'] = link
R['placement'] = 'The whole subsection "De-ontologizing Twin Flames FTW", his live words with the pointer corrected'
R['opens']['why_reading'] = 'It says what the twin flame experience really is, so the idea leads to deeper love.'
R['same_point'] = ('none: read the section from its heading to the next for the twin flame as an energy, the song and '
                   'being a good influence; each is made once, here')
R['needed'] = {'reader': 'his own live words; my one change is the pointer\'s name, which now matches the heading',
               'unneeded': [], 'kept': {}}
R['his_fixes'] = {'reader': 'N/A: his own words; my change is a section name in a pointer', 'marked': [], 'kept': {}}
R['fit'] = {'reader': 'N/A: his own words; my change is a section name in a pointer', 'marked': [], 'kept': {}}
R['questions'] = {q: 'PASS: his live words; the one change is the pointer\'s section name, which now matches the heading it '
                     'points to' for q in R['questions']}
out.write_text(json.dumps(R, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
r = subprocess.run([sys.executable, str(ROOT / 'tools/humanization/sense_receipt.py'), 'check', str(text), str(out)],
                   capture_output=True, text=True)
print((r.stdout + r.stderr).strip().replace('\n', ' | ')[:700])
