#!/usr/bin/env python3
"""Put his answers of 2026-11-24 21:43 UTC into HUMANIZED-SO-FAR.md (../joel-20261124-2143-message.txt: "62 a 63 a 64 a
65  a"; the questions: OWNER-QUESTIONS.md at d78fdee7). Each change is the words of the option he picked, fitted where it
goes.

- 62a: the red line's heart-rate test reads the same in the three places that use it (the Cognitive Warning, Scenario
  A's Step 2, Scenario C): back down to your usual resting rate, and under 90 BPM. Section A's "once your resting heart
  rate goes up" is the same test from the other side.
- 63a: the agmatine warning's "anything that works on the brain" leaves out what the protocol itself pairs agmatine with.
- 64a: the lines that forbid 5-HTP or UMP on a psychedelic day say they mean a trip (the five the question named, and
  the Shield's 5-HTP line, which has the 5-HTP trial's same words); his Weeks 3-7 line covers microdoses.
- 65a: in his Weeks 3-7 line, his last sentence (mushrooms act on serotonin too, so stop the 5-HTP at its stop signs)
  moves up to right after "see how it feels", and the numbness test ends the line. With the caution between them, "too
  numb to tell" no longer sits next to what it is about, so it says it: "too numb to tell how a combo feels" (the
  follow-on fix the move needs; named to him in the turn's report).

  python3 articles/neuro-de-armoring/humanize/fix-20261108/x1124b/apply_x1124b.py [--write]
"""
import hashlib
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
ARTICLE = HERE.parents[1] / 'HUMANIZED-SO-FAR.md'
HTP = 'https://ibogaqueen.substack.com/i/181671197/serotonin-bottleneck-pattern-5-htp-low-dose-p5p'
TEST = 'back down to your usual resting rate, and under 90 BPM'
S5 = ('Mushrooms act on serotonin too, just not the way iboga does, so stop the 5-HTP if you get any of the stop signs '
      '[the 5-HTP section](' + HTP + ') lists.')

EDITS = [
    ('62a', 'Assume you are misreading every room until your heart rate is below 90 BPM.',
     'Assume you are misreading every room until your heart rate is ' + TEST + '.'),
    ('62a', 'Once your heart rate is within normal range, your cerebral cortex is receptive.',
     'Once your heart rate is ' + TEST + ', your cerebral cortex is receptive.'),
    ('62a', 'Stick to lukewarm-to-cold until your baseline heart rate is below 90 BPM.',
     'Stick to lukewarm-to-cold until your heart rate is ' + TEST + '.'),
    ('63a', 'or other complex psychoactive stacks (anything that works on the brain) without',
     'or other complex psychoactive stacks (anything that works on the brain, beyond what this protocol pairs it with) '
     'without'),
    ('64a', 'Rule: do not take 5-HTP on the same day as psychedelics,',
     'Rule: do not take 5-HTP on the same day as a psychedelic trip,'),
    ('64a', 'Do not take UMP on the same day as psychedelics;', 'Do not take UMP on the same day as a psychedelic trip;'),
    ('64a', 'avoid 5-HTP on your psychedelic days,', 'avoid 5-HTP on the same day as a trip,'),
    ('64a', 'DHA/EPA in place. Do not take it on psychedelic days.',
     'DHA/EPA in place. Do not take it on the same day as a psychedelic trip.'),
    ('64a', 'Do not take UMP on psychedelic days, and assume',
     'Do not take UMP on the same day as a psychedelic trip, and assume'),
    ('64a', 'Do not combine with serotonergic medications, ayahuasca/harmalas, iboga, MDMA, DXM, tramadol, or same-day '
            'psychedelics.',
     'Do not combine with serotonergic medications, ayahuasca/harmalas, iboga, MDMA, DXM, tramadol, or a same-day '
     'psychedelic trip.'),
    ('64a', 'Do not use with serotonergic medications/supplements, ayahuasca/harmalas, iboga, MDMA, DXM, tramadol, or '
            'same-day psychedelics.',
     'Do not use with serotonergic medications/supplements, ayahuasca/harmalas, iboga, MDMA, DXM, tramadol, or a '
     'same-day psychedelic trip.'),
    ('65a', "see how it feels. If you're too numb to tell, compare your sleep and dreams on the nights after a microdose "
            "day and a day without. " + S5,
     "see how it feels. " + S5 + " If you're too numb to tell how a combo feels, compare your sleep and dreams on the "
     "nights after a microdose day and a day without."),
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
    for gone in ('psychedelic days', 'same day as psychedelics', 'same-day psychedelics', 'within normal range'):
        assert gone not in text, gone
    rec = {'about': 'his answers 62a, 63a, 64a and 65a (his message of 2026-11-24 21:43 UTC)',
           'message': '../joel-20261124-2143-message.txt',
           'whose': 'the words of the options he picked, fitted where they go; in his Weeks 3-7 line, his own sentences '
                    'in the order 65a gives, with "how a combo feels" added for the referent the move took away',
           'applied': applied,
           'before_sha256': before, 'after_sha256': hashlib.sha256(text.encode('utf-8')).hexdigest()}
    print('before', before[:8], 'after', rec['after_sha256'][:8], len(applied))
    if write:
        ARTICLE.write_text(text, encoding='utf-8')
        (HERE / 'APPLIED-X1124B.json').write_text(json.dumps(rec, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')


if __name__ == '__main__':
    main('--write' in sys.argv)
