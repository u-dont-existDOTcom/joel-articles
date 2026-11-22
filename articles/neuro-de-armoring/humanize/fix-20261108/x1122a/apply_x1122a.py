"""Put his answers of 2026-11-22 17:39 UTC into HUMANIZED-SO-FAR.md (his message: ../joel-20261122-1739-message.txt;
the questions: ../../OWNER-QUESTIONS.md, 24 to 33). Each change is his line with the words the option he picked gave,
or his own words from the message; none is a paragraph of mine.

- 32b: the iboga list (female for emotional numbness, male for brain fog, helplessness and relapse, and his Tabernanthe
  elliptica line, its potency and feel said as his experience, without "closest to what is mainly studied"), and Weeks
  3-5's two iboga lines to match, with "(if heart is ok: an ECG is how to know)".
- 33b: his agmatine paragraph after agmatine's timing rule, with "People's reports differ ...".
- 24a: Weeks 3-5 says "Reduce or stop phosphatidylserine here" once, in its Protocol line.
- 25: the strains line gives his range, and that some strains are much more potent.
- 26a: Weeks 1-2's agmatine line starts as the agmatine section does.
- 27a: the order of PQQ and ketones, D-serine and the session, said once.
- 28a: the D-serine cap wins for lighter people.
- 29a: the 5-HTP trial's second step lasts as long as it benefits you, in the section and in Weeks 3-5.
- 30a: the potassium plan gets you close, and the rest comes from other food.
- 31a: Weeks 1-2's showers line in his words (cold for anxiety, hot may help too, hot baths with Epsom salt), and his
  breathwork page.

His new warnings (lion's mane and ashwagandha, agmatine, 5-HTP) are new text: checked against sources first, then
written and checked like any text of mine. The article advises neither lion's mane nor ashwagandha anywhere.

  python3 articles/neuro-de-armoring/humanize/fix-20261108/x1122a/apply_x1122a.py [--write]
"""
import hashlib
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parents[1]
ARTICLE = H / 'HUMANIZED-SO-FAR.md'
ELLIPTICA = ('Tabernanthe elliptica ("bisexual" or "healer" iboga): an iboga cousin with many iboga alkaloids. In my '
             'experience it\'s the best of both worlds, but lower potency than regular iboga, and it doesn\'t feel as '
             'trancey. Try elliptica first for microdosing: in my experience it\'s more functional, more clear-headed, '
             'and often better for mood.')
AGMATINE = ('Agmatine with psychedelics is more complicated, and I can\'t say to take it with them or not. People\'s reports '
            'differ: some say it makes a trip or roll stronger while capping the euphoria, others that it weakens it. A '
            'friend of mine finds it gives a lot of the introspective benefits he gets from iboga, and that the two go well '
            'together, although I haven\'t heard of that from others. I don\'t notice much from it myself, aside from, I '
            'think, a lower ceiling on euphoria. I wouldn\'t use it unless a trip gets too stormy, but you can try the '
            'combination to see if it\'s worthwhile for you. Everyone\'s different.')
SWAPS = [
    ('32b', 'Female Iboga: For "Numbness/Fog" (Anima).', 'Female Iboga: For "Emotional Numbness" (Anima).'),
    ('32b', 'Male Iboga: For "Helplessness/Relapse" (Animus).', 'Male Iboga: For "Brain Fog/Helplessness/Relapse" (Animus).'),
    ('32b', 'Micro-dose Male Iboga (if heart is ok).',
     'Micro-dose Tabernanthe elliptica or Male Iboga (if heart is ok: an ECG is how to know).'),
    ('32b', '*If Numb:* Micro-dose Male Iboga and/or Hillybilly/Mazatapec shrooms.',
     '*If Numb:* Micro-dose Tabernanthe elliptica or Female Iboga, and/or Hillybilly/Mazatapec shrooms.'),
    ('24a', ' Reduce or stop phosphatidylserine here--you don\'t want to suppress an already-flattened system.', ''),
    ('25', 'strains are some of the best (0.1g - 0.2g).',
     'strains are some of the best (100-300mg, though some strains are much more potent).'),
    ('26a', 'Agmatine Sulfate 250–500 mg AM, increasing to', 'Agmatine Sulfate 250–500 mg in the morning or early afternoon '
     'for 3 days, then increasing to'),
    ('27a', 'on an empty stomach 45 minutes before a de-armoring session acts as', 'on an empty stomach before a '
     'de-armoring session acts as'),
    ('27a', 'You should take it 45 minutes or so after taking PQQ & Ketones so that your brain is fueled when the D-serine '
     'starts working.', 'Take PQQ & Ketones first, the D-serine about 45 minutes later, and start the session about 45 '
     'minutes after that, so that your brain is fueled when the D-serine starts working.'),
    ('28a', 'Do not exceed 30mg/kg and ensure high water intake.', 'Do not exceed 30mg/kg, even when that\'s less than the '
     'dose above, as it is for anyone under about 47 kg (104 lb), and ensure high water intake.'),
    ('29a', 'then go up to 100mg if 50mg was clearly helpful and not causing side effects.', 'then go up to 100mg if 50mg '
     'was clearly helpful and not causing side effects, and stay on it as long as it benefits you.'),
    ('29a', 'looks serotonergic: 50–100 mg at night for 2–3 nights, with optional', 'looks serotonergic: 50 mg at night for '
     '2–3 nights, then 100 mg if that clearly helped without side effects, for as long as it benefits you, with optional'),
    ('30a', 'The Strategy: Eat 2 large potatoes and 2 cups of greens every single day.', 'The Strategy: Eat 2 large '
     'potatoes and 2 cups of greens every single day. That gets you close to the target, and the rest comes from your '
     'other food.'),
    ('31a', 'Self-care: Hot & cold showers, alternating, ending on cold. *No hot showers if heart rate elevated or '
     'heart-rate-variability reduced.*', 'Self-care: Cold showers for anxiety, though hot showers might also help, so you '
     'can experiment, and many people find hot baths especially good for anxiety (especially with Epsom salt). *No hot '
     'showers if heart rate elevated or heart-rate-variability reduced.* My [breathwork page]'
     '(http://breathwork.u-dont-exist.com/) can help a lot with anxiety and mood too.'),
]


def main(write=False):
    md = ARTICLE.read_text(encoding='utf-8')
    before = hashlib.sha256(md.encode('utf-8')).hexdigest()
    lines = md.split('\n')
    applied = []
    for answer, old, new in SWAPS:
        if new and any(new in l for l in lines):
            continue
        hits = [k for k, l in enumerate(lines) if old in l]
        if not hits and not new:
            continue
        (i,) = hits
        assert lines[i].count(old) == 1, (answer, old[:40])
        applied.append({'answer': answer, 'line': i + 1, 'old': lines[i], 'new': lines[i].replace(old, new)})
        lines[i] = lines[i].replace(old, new)
    if ELLIPTICA not in lines:
        (j,) = [k for k, l in enumerate(lines) if l.startswith('Male Iboga: For "Brain Fog/Helplessness/Relapse"')]
        assert lines[j + 1] == ''
        lines[j + 1:j + 1] = ['', ELLIPTICA]
        applied.append({'answer': '32b', 'line': j + 3, 'inserted': ELLIPTICA})
    if AGMATINE not in lines:
        (j,) = [k for k, l in enumerate(lines) if l.startswith('Timing rule: avoid agmatine on D-Serine/DCS-style')]
        assert lines[j + 1] == ''
        lines[j + 1:j + 1] = ['', AGMATINE]
        applied.append({'answer': '33b', 'line': j + 3, 'inserted': AGMATINE})
    out = '\n'.join(lines)
    rec = {'about': 'his answers of 2026-11-22 17:39 UTC: 32b, 33b, 24a, 25, 26a, 27a, 28a, 29a, 30a, 31a',
           'message': '../joel-20261122-1739-message.txt', 'whose': 'his lines and his words, with the words of the '
           'option he picked', 'applied': applied,
           'held': ['his new warnings (lion\'s mane and ashwagandha, agmatine, 5-HTP): sources first, then text of mine '
                    'through the reads and a Pangram check'],
           'before_sha256': before, 'after_sha256': hashlib.sha256(out.encode('utf-8')).hexdigest()}
    print('before', before[:8], 'after', rec['after_sha256'][:8], len(applied), [x['answer'] for x in applied])
    if write and applied:
        ARTICLE.write_text(out, encoding='utf-8')
        (HERE / 'APPLIED-X1122A.json').write_text(json.dumps(rec, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')


if __name__ == '__main__':
    main('--write' in sys.argv)
