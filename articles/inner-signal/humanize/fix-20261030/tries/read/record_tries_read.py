"""READ.md and READ-RECORD.json for the tries of 30 October (../TRIES.json): each one read by me (the lead session,
Claude Opus 5.5, never a cheaper reader: E294) beside his published version and the words it replaces, sentence by
sentence, before the recheck. The verdicts below are that read; this script only lays them out with the texts.

  python3 articles/inner-signal/humanize/fix-20261030/tries/read/record_tries_read.py
"""
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
T = HERE.parent
H = T.parents[1]
ROOT = H.parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import compare_read as cr  # noqa: E402
import suggestion_review as sr  # noqa: E402

FINDINGS = json.loads((H / 'fix-20261030' / 'fullread' / 'FINDINGS.json').read_text(encoding='utf-8'))['findings']
PUB = {f['id']: f['published'] for f in FINDINGS}
PUB['A#63'] = ('(his inner child guide, the same words) How much of the grown-up you is actually here right now? Try '
               'looking around the room, pausing before you act, making a choice and following through on it. If you '
               'can\'t do that because you\'re basically the frightened kid, leave the deeper conversation until later.')
PUB['A#168'] = ('Start smaller: / “Show me one body sensation.” “Show me one word.” “Show me whether today is for listening '
                'or resting.”')

READ = {
    'T-35': 'The list of forces is gone, as he decided on 25 October (RP-1.4): the marketers paragraph, his TikTok '
            'example and the Silva line say just above that your mind is being trained anyway. "train your own mind from '
            'the inside" is "practice from inside it"; befriending and listening are there; "a whole new area of choice '
            'for you as an adult" is "making adult choice more available". Clear; nothing lost that he kept.',
    'T-337': '"investigate further" carries "ask what happened", and the response check just above says a tightness is a '
             'notice to find out about, not a meaning; the script just below asks whether the invitation fits. An '
             'explicit no needs no reason ("You don\'t need any other reason"), you change it, and you don\'t repeat it '
             'more persuasively: all there. The published contrast between a body sensation and a judgment of the '
             'wording is the one point not in the guide, as on 28 October, when I judged the guide\'s grouping clear '
             'guidance in its own words (AUDIT.md, F6a.1). Clear.',
    'T-339': 'Sentence 1: "the invitation just isn\'t right" is "the sentence was simply wrong"; "it\'s brought up '
             'something you hadn\'t thought of, with a feeling that\'s worth meeting" is "an unfamiliar possibility '
             'brings a feeling worth meeting"; "give it a little room and find out which" is "you don\'t have to decide '
             'which before making space to find out" (you make room first, and learn which after). Sentence 2: doubt '
             'isn\'t automatically a guard (published: skepticism, a protector), and silence doesn\'t mean a hidden '
             'process is working (published: not proof). Every point, both referents named. Clear.',
    'T-374': 'Flooding makes the adult capacities harder to reach, and regulation and support come first: both there. '
             'That silence may be protection is in the section\'s first paragraph ("If knowing what your subconscious '
             'knows would destabilize you, it is not meant for you to know directly at this time!") and its next one '
             '("your subconscious knows something that your conscious self is not prepared to know"). Clear.',
    'T-495': '"notice that too" is "notice what actually happens"; "don\'t talk yourself into believing it worked in '
             'some way you can\'t see" is "no change doesn\'t mean secret success", as an instruction. Clear.',
    'T-249': 'Same anchor wherever the script mentions it; don\'t read the directions out loud; pause between paragraphs. '
             'All three of the published points; the comma before "just" is the guide\'s spoken register (his own "stand '
             'down, any revelations can wait"). Clear.',
    'T-503': 'All six forms are there: an image, a word, a pressure, warmth, a silence, and a next action ("a sense of '
             'what to do next"). "Notice how the answer comes to you… maybe as" is "Notice whether the answer comes '
             'as". Silence stays one of the forms, so it doesn\'t promise an answer. Spoken with pauses, the way the '
             'guide\'s scripts are. Clear.',
    'T-505': 'What a presupposition is (published sentence 1) is there, as an aside, with why it\'s powerful: the person '
             'hearing it usually takes the assumption on board ("that power", published). The uses he allows (choice, '
             'timing, capacity, safety, love, adult leadership) are in the sentence he approved, unchanged. "Don\'t '
             'smuggle in obedience" is "Don\'t ever presume obedience", with what that sounds like (new words: a quoted '
             'misuse, the way his reframing paragraph quotes the dishonest reframe). His example is the next paragraph, '
             'unchanged. Clear.',
    'T-508': 'The published "Better:" version is there: "As I breathe, my adult self may become present enough to hear a '
             'little of what the wound needs" ("one small piece" became "a little of": the same small claim, without his '
             '"one" tell). "So an honest bridge might sound more like" leads into it from the line before ("it doesn\'t '
             'mean that it\'s true if it isn\'t"). Clear.',
    'S-162': 'His words, all kept. New: "To find out," ties the test to his question, and "since those are all things '
             'your adult self can do" says why the test works, which his next sentence implies ("because you\'re '
             'basically the frightened kid"). Clear; a suggestion for him.',
    'S-382': 'His three asks, word for word. New: "Ask for something small, like" says what "a smaller scale" means, and '
             '"If even that gets you nothing, try" makes the third ask the one after the first two get nothing; in his '
             'version the three stand side by side. That order is mine, so the card says so. Clear; a suggestion for '
             'him.',
}


def main():
    tries = json.loads((T / 'TRIES.json').read_text(encoding='utf-8'))
    master = (T / 'CANDIDATE-MASTER.md').read_text(encoding='utf-8')
    assert cr.hashlib.sha256(master.encode('utf-8')).hexdigest() == tries['master_sha256']
    now = {cr.phash(b['text']) for b in sr.blocks(master) if not b['level']}
    assert set(READ) == {t['id'] for t in tries['tries']}, set(READ) ^ {t['id'] for t in tries['tries']}
    cov = []
    lines = ['# My read of the tries of 30 October, beside his published version', '',
             'Each try was read by me (the lead session, never a cheaper reader: E294) beside Joel\'s published version '
             'and the words it replaces, sentence by sentence, before the recheck. "Take back" means a sentence my full '
             'read had restored comes out again; "suggestion" means his own words, which go to him as a card.', '']
    for t in tries['tries']:
        h = cr.phash(t['after'])
        assert h in now, t['id']
        cov.append(h)
        pub = ' / '.join(PUB.get(f, '') for f in t['findings'] if PUB.get(f))
        lines += ['## %s (%s; %s)' % (t['id'], t['kind'], t['where']), '',
                  '- **His published version:** %s' % (pub or '(none)'),
                  '- **Before (the guide now):** %s' % t['before'],
                  '- **The try:** %s' % t['after'],
                  '- **What it read:** %s' % t['read'],
                  '- **My read:** %s' % READ[t['id']], '']
    cr.record(HERE, findings=[], coverage=cov, dispositions={},
              article='fix-20261030/tries/CANDIDATE-MASTER.md: the tries of 2026-10-30, read by the lead session (E294)')
    (HERE / 'READ.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print(len(cov), 'tries recorded')


if __name__ == '__main__':
    main()
