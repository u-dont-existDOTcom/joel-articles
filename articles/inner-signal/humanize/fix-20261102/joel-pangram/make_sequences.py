"""SEQUENCES.md: Joel's Pangram tries on the cards of 1 November (2), in his order, each with its link, its result and what
changed from the try before (his note on E-315, 2 November: "these are my attempts in order. i'm thinking you could
maybe learn more this way than just looking at the perfect final one?").

The results were read from each link's page on 2 November (the in-page reader, by SHA-256 for the five texts kept in
texts-raw.json); the notes on what changed are the lead session's, from the word-level differences between tries.

  python3 articles/inner-signal/humanize/fix-20261102/joel-pangram/make_sequences.py
"""
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
COMMENTS = (HERE.parent / 'joel-20261102-1643-comments.txt').read_text(encoding='utf-8')
LINKS = {u[:8]: 'https://www.pangram.com/history/' + u for u in re.findall(r'history/([0-9a-f-]{36})', COMMENTS)}

# card: [(uuid prefix, result, what changed and what it showed)]
SEQ = {
    'W-164 (Don\'t rush the repair)': [
        ('1fc537a3', 'AI Detected, 55%', 'my card\'s version'),
        ('02ffb895', 'AI Detected, 43%', '"spend some quality time with them before taking off the kid gloves, so to speak"; "They might like to hear"'),
        ('e2fd260f', 'AI Detected, 28%', '"You don\'t have to work to explain anything. I\'m not asking you to impress me with how fast you can get better."'),
        ('be6be4f7', 'AI Detected, 29%', '"Can I help you feel less alone?"'),
        ('85a2e717', 'AI Detected, 37%', 'the colon-question split: "first. Can you take a moment before you react? When you decide something, do you follow through? If you answered \\"No,\\""'),
        ('8852d677', 'Human Written', '"do whatever helps you come back to yourself a bit" became "do whatever makes you feel adult": the portable phrase was the trigger'),
        ('6a013fb0', 'AI Detected, 22%', 'minimal pair: the packed colon-question back, the rest kept: AI again'),
        ('14c44cec', 'Human Written, High', 'both fixes, and "the frightened little boo", "Do what makes you feel adult"'),
    ],
    'E-315 (Come all the way back, the recording that cuts out)': [
        ('36ec99b2', 'AI Detected, 88%', 'the stuck version (ours)'), ('b5d71590', 'AI Generated, 99.7%', ''),
        ('94cbf52b', 'AI Generated, 100%', ''), ('92cc0afc', 'AI Detected, 92%', ''), ('13234f89', 'AI Detected, 58%', ''),
        ('eb780122', 'AI Detected, 73%', ''), ('71102ea3', 'AI Detected, 37%', ''),
        ('4dea2bac', 'Human Written, High', 'his voice throughout ("woops...", "dazed & confused", "you don\'t have to be a vegetable forever", "touch grass"), and in his words "the only version with a real useful ending"'),
    ],
    'E-406 (You become too blissful or diffuse)': [
        ('41905cb6', 'AI Generated, 100%', '"one next step" and "the next small thing" undoubled'),
        ('6f4ca408', 'AI Generated, 100%', 'the first "next step" out too'),
        ('ff307b0a', 'Human Written, High', 'the list "A task, a boundary, a meal, some rest, a repair, a conversation?" said as four questions, and "down to Earth", "this lofty love"'),
        ('f418aed4', 'Human Written, High', 'minimal pair: only the list expanded, "one next step" and "the next small thing" kept: the list was what Pangram read; "it still reads ai to me without the other fixes"'),
    ],
    'W-509 (Patterns 3 to 7)': [
        ('6387a3ed', 'AI Generated, 100%', 'the approved cards\' version'),
        ('7b6141ee', 'AI Detected, 41%', 'his first rewrite'), ('597d8b09', 'AI Detected, 14%', ''), ('f6ad1c0c', 'AI Detected, 13%', ''),
        ('daa67474', 'AI Detected, 11%', ''),
        ('6c87cdc9', 'Human Written', '"Welcome to McHappyness ... And would you like fries with that?": an unusual joke of his own turned the whole text Human'),
        ('06769981', 'AI Detected, 16%', 'minimal pair: the joke out, AI again'),
        ('7ee02c7d', 'Mostly Human, 5%', 'no joke; the communication pattern broken up'),
        ('b25dea80', 'Human Written', 'no joke; one Human (Low) stretch left'),
        ('54ec1675', 'Human Written, High', 'the Low sentence uncompressed: "a sneaky little yes or no question that\'s actually a way to ask for something indirectly"; "I dare you now to practice this ethical postulate!"'),
    ],
    'W-589 (Running the whole NLP sequence)': [
        ('a1824eb6', 'AI Detected, 26%', 'with my round-2 paragraph on the three adults: "that wasn\'t the part marked ai"'),
        ('115adaff', 'AI Detected, 68%', ''),
        ('222e4bec', 'Human Written, High', '"The Nurturer brings love in. Next, the Protector puts your helmet on, and then the Guide points the way out of the mess ... (like Captain Planet if you saw that cartoon)": a sequence, not a list of three'),
        ('4a5eca9f', 'Human Written, High', 'without Captain Planet, also Human'),
    ],
    'W-605 (Hypnosis-specific audit)': [
        ('ca9568e9', 'AI Generated, 100%', 'my card\'s version ("quietly", lists): "you didn\'t check if your changes passed.. they didn\'t"'),
        ('1f7c2ed9', 'AI Generated, 100%', 'his first rewrite'),
        ('dc29f59e', 'AI Detected, 43%', '"a lot of it was unclear": clearer, and "Like oh your hand dropped real fast, so you ARE gay."'),
        ('50fe8c5b', 'AI Detected, 16%', 'another listicle broken up'),
        ('c341e75a', 'Human Written, High', '"turning what you feel in your body into evidence for something they\'d already decided" became "using your body signals to prove their theories"'),
        ('38d09be5', 'Human Written, High', 'without the body-signal example, also Human; he\'d keep the example'),
    ],
    'W-685 (Forgiveness without bypass, Forgiving yourself)': [
        ('e971282c', 'AI Detected, 37%', 'as it was: "there was a whole lot there that was redundant"'),
        ('530840d1', 'AI Detected, 60%', 'the repeats cut: "less human, altho reads a lot better to me"; "still matters" is a tell'),
        ('8fdd1272', 'AI Detected, 24%', 'an AI part clarified: "is crucial to maintain, especially after forgiveness which can tend to weaken it", "just like Jesus did on the Cross"'),
        ('21e4379b', 'Human Written', '"spiritual talk" became "spiritual mumbo jumbo" (an intensifier AI doesn\'t use); "did" to "regret doing" didn\'t change the score'),
        ('0ace8ab7', 'Human Written, High', '"shut your pain up" became "shush your cries"'),
    ],
    'W-762 (No-trance inner contact)': [
        ('83fb69fc', 'AI Detected, 21%', 'as it was: "it looks like you chose the wrong parts to fix"'),
        ('14f6e8d7', 'AI Detected, 78%', 'my card\'s version'),
        ('2a567edc', 'Human Written, High', 'his: "We don\'t need to go into trance to get a lot of the benefits ... Hopefully your name didn\'t suddenly change to Larry."'),
    ],
    'W-274 (When you\'re already trancey)': [
        ('afe7f6a6', 'AI Detected, 36%', 'the passage: "the real problem was below, you didn\'t see" (the wish and Stay awake)'),
        ('5aa7a3fd', 'AI Generated, 100%', 'the part below by itself'),
    ],
    'E-107, W-579, W-596 (one check each)': [
        ('3cd6c871', 'Human Written, High', 'E-107, his Let the child speak'),
        ('a25e487f', 'Human Written, High', 'W-579, his What I will not use NLP for'),
        ('8fb8b276', 'Human Written', 'W-596, Appendix C as it was: "it didn\'t show me that when i checked it"'),
    ],
}


def main():
    out = ['# Joel\'s Pangram tries, 2 November', '', __doc__.split('\n\n')[0].replace('\n', ' '), '']
    n = 0
    for card, tries in SEQ.items():
        out += ['## %s' % card, '']
        for k, (p, res, note) in enumerate(tries, 1):
            n += 1
            out.append('%d. [%s](%s)%s' % (k, res, LINKS[p], (': ' + note) if note else ''))
        out.append('')
    assert n == len(LINKS), (n, len(LINKS))
    (HERE / 'SEQUENCES.md').write_text('\n'.join(out), encoding='utf-8')
    print(n, 'tries')


if __name__ == '__main__':
    main()
