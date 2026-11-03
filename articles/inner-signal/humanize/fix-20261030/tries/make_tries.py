"""The next round for the hypnosis guide (2026-10-30, after Joel's recheck results of 20:15 UTC): new tries for the 14
windows that read AI in the recheck of 30 October (feeds fc1d8dae and 48eed31c) and for two Low ones, put into the guide
as it stands with the recheck's four suggestions still in, so the next recheck reads them in place.

What the recheck showed (../recheck/read/SPOTS.md): 8 of the 14 AI windows sit on points my full read restored, and the
red ran on into words nobody changed (the double binds, the weekend line, the "Show me" asks, which read High or Medium on
29 October with the same words). So the tries are of three kinds:
- take-backs: a restored point he had cut himself (RP-1.4, 25 October) or that my own check of 28 October had found said
  already (AUDIT.md: F6a.1, F6b.12); the restored sentence comes out again;
- new tries in our words, written the way his versions of 30 October are (his-study: the why and an example where a
  definition or a colon list stood, a run broken, the steps chained, no "you don't have to" line);
- suggestions for his own words (S-162, S-382), on his cards page with how they read; in the recheck so they're read in
  place.
Every new sentence was read by the lead model beside his published version (READ.md beside this file).

  python3 articles/inner-signal/humanize/fix-20261030/tries/make_tries.py   (from anywhere)
Writes CANDIDATE-MASTER.md and TRIES.json here.
"""
import hashlib
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parents[1]
ROOT = H.parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
sys.path.insert(0, str(H / 'fix-20261025' / 'review'))
sys.path.insert(0, str(H / 'fix-20261030' / 'recheck'))
import suggestion_review as sr  # noqa: E402
from apply_answers import set_block_text  # noqa: E402
import make_candidates as last  # noqa: E402  the recheck of 30 October: its four suggestions stay in

GUIDE_SHA = last.GUIDE_SHA

# (id, kind, findings, a unique piece of the block, [(old, new)], whose, what it read, why)
TRIES = [
    ('T-35', 'take back', ['F1.10'], 'With self-hypnosis you can train your own mind from the inside',
     [('Ads, screens, fear and cravings are already training your mind, and so are your tribe, the people in authority, '
       'loneliness and plain old repetition. ', '')],
     'my fix of 30 October (F1.10)', 'AI (Low), part A window 14',
     'You cut this point as a repeat on 25 October (card RP-1.4: "says again that other forces are already shaping your '
     'mind, after the marketers paragraph and the Silva line have said it"). My full read brought it back as a list, '
     'and it read AI. It comes out again.'),
    ('T-337', 'take back', ['F10.1'], "Your shoulders tightening, or 'hmm, that feels kind of wrong'",
     [("is a signal to investigate further. A tightening won't tell you what it's about by itself, so ask what happened "
       "and whether the invitation fits. But 'No!", "is a signal to investigate further, but 'No!")],
     'my fix of 30 October (F10.1)', 'AI (Low), part A window 150',
     'On 28 October I found this point said already (AUDIT.md, F6a.1): the response check just above calls a tightness '
     'a notice, not a meaning, and says to find out what happened, and the script just below asks whether the '
     'invitation fits. My restored sentence said it again and read AI. The sentence goes back to one, as it read High '
     'on 29 October; "don\'t try saying it again more persuasively" stays.'),
    ('T-339', 'new try', ['F10.2'], "Sometimes the invitation just isn't right",
     [("Sometimes the invitation just isn't right. Sometimes it brings up a possibility you hadn't thought of, and the "
       "feeling that comes with it is worth meeting. You don't have to know which it is before you make room to find "
       "out.", "Sometimes the invitation just isn't right, and other times it's brought up something you hadn't thought "
       "of, with a feeling that's worth meeting, so give it a little room and find out which.")],
     'my fix of 30 October (F10.2)', 'AI (High), part A windows 155 and 156',
     'My clear version read AI (High): two "Sometimes" sentences in a row, a "you don\'t have to" line and a tidy pair. '
     'This keeps every point in two sentences, the shape of the unclear version that read High on 29 October.'),
    ('T-374', 'take back', ['F11.5'], 'This can lead to flooding, panic, false certainty',
     [(" If your subconscious won’t answer, it may be protecting you until your adult is steady enough to take in what it "
       "has.", '')],
     'my fix of 30 October (F11.5)', 'AI (Low), part A window 162',
     'On 28 October I found this point said already (AUDIT.md, F6b.12): the section\'s first paragraph says "If knowing '
     'what your subconscious knows would destabilize you, it is not meant for you to know directly at this time!" My '
     'full read brought it back anyway, and it read AI. It comes out again; the comma before "so" stays.'),
    ('T-495', 'new try', ['F7.7'], 'Let your response guide you as to what to do next',
     [("If nothing changes, notice that too: no change doesn't mean it worked in some way you can't see.",
       "If nothing changes, notice that too, and don't talk yourself into believing it worked in some way you can't "
       "see.")],
     'my fix of 30 October (F7.7)', 'Human (Low), part A window 108',
     'Read Human (Low): a colon, then a "doesn\'t mean" line. This says the same thing as one plain instruction.'),
    ('T-249', 'new try', ['F8.1'], 'You can read this slowly into your recorder',
     [("Don't read the directions out loud. Just pause between paragraphs.",
       "Don't read the directions out loud, just pause between paragraphs.")],
     'my fix of 30 October (F8.1)', 'Human (Low), part A window 112',
     'Read Human (Low): three short commands in a row. The sentence before my fix was "Don\'t read the directions, just '
     'pause between paragraphs"; this keeps its shape, with "out loud" so it can\'t be read as "don\'t read them at all".'),
    ('T-503', 'new try', ['F14.6'], 'Notice how the answer comes to you',
     [('Example: ‘Notice how the answer comes to you: as an image, a word, a pressure, some warmth, silence, or something '
       'to do next.’', 'Example: ‘Notice how the answer comes to you… maybe as an image, or a word… maybe as a pressure, '
       'or some warmth… or a silence, or a sense of what to do next.’')],
     'my fix of 30 October (F14.6)', 'AI (Medium), part B window 9',
     'Read AI: a colon, then six things in one breath. Said the way a script is spoken, with its pauses, every one of '
     'them is still there.'),
    ('T-505', 'new try', ['F14.4'], 'Presumption is a powerful thing',
     [('A presupposition is an assumption hidden inside a sentence. Presumption is a powerful thing, so please don’t use '
       'it except', 'Presumption is a powerful thing (a presupposition hides an assumption inside a sentence, and the '
       'person hearing it usually takes that assumption on board), so please don’t use it except'),
      ('Never use it to sneak in obedience.', 'Don’t ever presume obedience, the way a hypnotist does when they say '
       'something like, ‘As you go deeper, it gets easier and easier to just do what I say.’')],
     'my fix of 30 October (F14.4)', 'AI (Medium and Low), part B windows 9 and 11',
     'Read AI: a textbook definition on its own and a short command. This puts the definition inside the sentence you '
     'approved, as an aside that says why presumption is powerful, and shows what presuming obedience sounds like, the '
     'way your reframing paragraph shows the dishonest reframe before the honest one.'),
    ('T-508', 'new try', ['F14.5'], 'Bridge words are words like',
     [('A better bridge claims a lot less: ‘As I breathe, my adult self may become present enough to hear a small piece '
       'of what the wound needs.’', 'So an honest bridge might sound more like, ‘As I breathe, my adult self may become '
       'present enough to hear a little of what the wound needs.’')],
     'my fix of 30 October (F14.5)', 'AI (High), part B window 15 (it ran on into your embedded-invitations paragraph)',
     '"A better bridge claims a lot less:" was a colon reveal, and the red ran on into your paragraph after it. This '
     'leads into the better version the way your reframing paragraph does ("So we might arrive at, ...").'),
]
# suggestions for his own words: on his cards page; in the recheck so they're read in place
SUGGEST = [
    ('S-162', 'suggestion', ['A#63'], 'A. Prepare yourself to tend to them',
     [('Try looking around the room, pausing before you act, making a choice and following through on it.',
       'To find out, try looking around the room, pausing before you act, making a choice and following through on it, '
       'since those are all things your adult self can do.')],
     'your inner child guide\'s words', 'AI (Low, 0.53), part A window 63; High on 29 October with the same words',
     'Nothing in it changed, but the windows around it got smaller and it read AI at a coin toss. Your fix strategy, say '
     'why: the test works because those are things the adult in you can do, and the frightened kid can\'t.'),
    ('S-382', 'suggestion', ['A#168'], 'Show me one body sensation',
     [('Ask: “Show me one body sensation.” “Show me one word.” “Show me whether today is for listening or resting.”',
       'Ask for something small, like “Show me one body sensation,” or “Show me one word.” If even that gets you '
       'nothing, try “Show me whether today is for listening or resting.”')],
     'your published version', 'AI (High), part A window 168; Human (Medium) on 29 October with the same words',
     'Three "Show me" lines in a row read AI (High). This keeps your three asks, and the last one becomes what you ask '
     'when the small ones get nothing.'),
]


def main():
    md = (H / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
    assert hashlib.sha256(md.encode('utf-8')).hexdigest() == GUIDE_SHA, 'the guide changed'
    bl = sr.blocks(md)
    raw = re.split(r'\n\s*\n', md.rstrip('\n'))
    assert len(raw) == len(bl)
    text = {b['i']: b['text'] for b in bl}
    lost = []
    # the recheck's four suggestions, as they were
    for sid, fids, start, edits, whose, why in last.SUGGESTIONS:
        hits = [b for b in bl if b['text'].startswith(start)]
        assert len(hits) == 1, sid
        t = text[hits[0]['i']]
        for old, new in edits:
            assert t.count(old) == 1, (sid, old)
            t = t.replace(old, new)
        text[hits[0]['i']] = t
    out = list(raw)
    for i, t in text.items():
        if t != next(b['text'] for b in bl if b['i'] == i):
            out[i] = set_block_text(raw[i], t, lost)
    rec = []
    for tid, kind, fids, piece, edits, whose, read, why in TRIES + SUGGEST:
        hits = [b for b in bl if piece in text[b['i']] and not b['level']]
        assert len(hits) == 1, (tid, len(hits))
        i = hits[0]['i']
        before = text[i]
        t = before
        for old, new in edits:
            assert t.count(old) == 1, (tid, old)
            t = t.replace(old, new)
        t = re.sub(r'  +', ' ', t).strip()
        text[i] = t
        out[i] = set_block_text(raw[i], t, lost)
        rec.append({'id': tid, 'kind': kind, 'findings': fids, 'block': i, 'where': sr.where(bl, i), 'whose': whose,
                    'read': read, 'before': before, 'after': t, 'why': why})
    assert not lost, lost
    master = '\n\n'.join(out) + '\n'
    (HERE / 'CANDIDATE-MASTER.md').write_text(master, encoding='utf-8')
    (HERE / 'TRIES.json').write_text(json.dumps({'guide_sha256': GUIDE_SHA, 'master_sha256': hashlib.sha256(
        master.encode('utf-8')).hexdigest(), 'kept_from_last_recheck': [s[0] for s in last.SUGGESTIONS],
        'tries': rec}, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print(len(rec), 'changes;', hashlib.sha256(master.encode('utf-8')).hexdigest())


if __name__ == '__main__':
    main()
