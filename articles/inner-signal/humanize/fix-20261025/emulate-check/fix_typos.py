"""The typos and slips the strict Emulate check found in the guide, fixed (his message of 2026-10-25 19:42 UTC: "i didn'
tmake these typos, did you?").

  python3 articles/inner-signal/humanize/fix-20261025/emulate-check/fix_typos.py

Each one was found by the paragraph readers (READ-<part>.json, the id after each fix) or the check itself and is in none of
his texts: his published post has the word or the mark right at that spot. Only clear errors: a word split or run
together, a missing hyphen or apostrophe, "a ecology", "yo", "breath" for "breathe", "council" for "counsel", a full stop
for a question mark, a bracket never closed, a comma between a subject and its verb. His casual style stays ("de hypno",
"etc etc", "According to who?", "un-undoable", self hypnosis without a hyphen as in his own sentences). Quote marks and
changes of meaning are on the marking page instead.
"""
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
GUIDE = HERE.parents[1] / 'HUMANIZED-SO-FAR.md'
FIXES = [  # (old, new, finding)
    ('cravings, day dreams and weird', 'cravings, daydreams and weird', '1.21'),
    ('as if it were a ecology', 'as if it were an ecology', '1.23'),
    ('49 meta analyses', '49 meta-analyses', '1.48'),
    ('pain, child birth, pediatric', 'pain, childbirth, pediatric', '1.49'),
    ('resting state fmri scans', 'resting-state fMRI scans', '1.54'),
    ('part etc etc then:', 'part etc etc) then:', '1.75'),
    ('What do you want not to do today.', 'What do you want not to do today?', '4.18'),
    ("Where are you. What's the date or day. How", "Where are you? What's the date or day? How", '4.50'),
    ('to your fore finger. And as you press your finger together', 'to your forefinger. And as you press your fingers together', '4.56, 4.57'),
    ('Start to breath gently', 'Start to breathe gently', '4.60'),
    ('a tendency to day dream,', 'a tendency to daydream,', '5.19'),
    ('use the ‘ Come all the way back ‘ procedure', 'use the ‘Come all the way back’ procedure', '5.71'),
    ('psychosis like symptoms', 'psychosis-like symptoms', '6.2'),
    ('without actually telling me what it is”?', 'without actually telling me what it is?”', '6.12'),
    ('your other on your solar plexus', 'your other hand on your solar plexus', '6.40'),
    ('ongoing help if: You are experiencing', 'ongoing help if you are experiencing', '6.71'),
    ('even wanting to feel difficult feelings, are not necessarily', 'even wanting to feel difficult feelings are not necessarily', '6.75'),
    ('this can be very useful to use it to help you', 'this can be very useful to help you', '7.12'),
    ('is NOT a large language model of AI', 'is NOT an AI large language model', '7.13'),
    ('make your prompt “safe” otherwise, the analytical', 'make your prompt “safe”, otherwise the analytical', '7.16'),
    ('vague, absolutes, manipulative or grandiose', 'vague, absolute, manipulative or grandiose', '7.42'),
    ("Nominalizations are words like, '", "Nominalizations are words like '", '8.2'),
    ('What do yo mean by that?', 'What do you mean by that?', '8.4'),
    ('easily, dont go for a peak', 'easily, don’t go for a peak', '8.21'),
    ("satisfies both parts needs", "satisfies both parts' needs", '8.61'),
    ('Buteyko’ breathing', 'Buteyko breathing', '9.23'),
    ('there are first line therapies', 'there are first-line therapies', '9.31'),
    ('neither one of those products are necessary', 'neither one of those products is necessary', '9.41'),
    ('you didn’t have to scream I got your message', 'you didn’t have to scream, I got your message', '9.49'),
    ('if there is nothing to do help my body stand down', 'if there is nothing to do, help my body stand down', '9.52'),
    ("after you've tried to get council", "after you've tried to get counsel", '9.73'),
    ('A helpful understanding to come to, is that', 'A helpful understanding to come to is that', '9.78'),
    ('in tune with love and helping you better your life', 'in tune with love and to better your life', '9.83'),
    ('The problem is, that some people', 'The problem is that some people', '2.0'),
    ('the benefits of being young; curiosity', 'the benefits of being young: curiosity', '2.29'),
    ('You agree with people at the moment but', 'You agree with people in the moment but', '3.29'),
    ('any of the following; urgency, you are special, FOMO (fear of missing out), not be included,',
     'any of the following: urgency, you are special, FOMO (fear of missing out), not being included,', '3.59'),
    ('ready for you to go in to.', 'ready for you to go into.', '4.68'),
    ('like an "Ok" sign', 'like an "OK" sign', '5.4'),
    ('"if it would be useful for you to do so" type language it\'s just not safe',
     '"if it would be useful for you to do so" type language, it\'s just not safe', '5.10'),
    ('it is under control of your adult mind', 'it is under the control of your adult mind', '5.13'),
    ('(or act or taking more time etc)', '(or action or taking more time etc)', '5.26'),
    ('not only how impressive the session felt\n', 'not only how impressive the session felt.\n', '5.80'),
    # the last part's readers (READ-10a.json, READ-10b.json) and a comma the merge left
    ("when you're loveyhuasca, meditati", "when you're on loveyhuasca, meditati", '10a.5'),
    ('FASTER than you are able to put it into context', 'FASTER than you are able to put them into context', '10a.6'),
    ('and it does n’t just feel', 'and it doesn’t just feel', '10a.9'),
    ('more Paranoid, sleepless, Grandiose, isolated', 'more paranoid, sleepless, grandiose, isolated', '10a.13'),
    ('to become interested in demons or jinns or', 'to become interested in demons or jinn or', '10b.6'),
    ('take care of my body by resting and eating etc. I don’t need it.', 'take care of my body by resting and eating etc, I don’t need it.”', '10b.4'),
    ('combining body orientated work', 'combining body-oriented work', '10b.13'),
    ("as well as [nimja's tutorial", "as well as [Nimja's tutorial", '10b.14'),
    ('(nimja did not write or endorse this guide)', '(Nimja did not write or endorse this guide)', '10b.14'),
    ('Remember that whatever you find out, is likely', 'Remember that whatever you find out is likely', '5.61'),
]
if __name__ == '__main__':
    text = GUIDE.read_text(encoding='utf-8')
    done = 0
    for old, new, _f in FIXES:
        if text.count(old) == 0 and text.count(new) >= 1:
            continue   # made on an earlier run
        assert text.count(old) == 1, old
        text = text.replace(old, new)
        done += 1
    GUIDE.write_text(text, encoding='utf-8')
    print(done, 'fixes made now,', len(FIXES), 'in all')
