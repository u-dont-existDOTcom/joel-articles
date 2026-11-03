"""Batch 481: the windows that read Human at less than High confidence in batch 480's recheck (Joel, 2026-10-26 12:43 UTC:
"i also want you to fix any segments that are not high confidence human if you can, and always we should be marking down
the confidence if we have it"; gate E278). The windows are ../b480/recheck/read/CONFIDENCE.json; the items Emulate rewrote
are BUNDLE.json (make_bundle.py: every Low window and every Medium one of 10 words or more, in its paragraphs), three
samples each (cm, cn, co on the laptop; SIDE-BY-SIDE.md puts them beside the text).

Only the flagged sentences come back from a sample, and only where a sample keeps their meaning and form; the fixes to a
sample's words are named with their reasons. Where no sample does, the window is left and LEFT says why. A spot marked
"his" replaces his own words (his published guide or his inner child guide): its card shows his words first, and Reject
keeps them (E214).

  python3 articles/inner-signal/humanize/fix-20261026/b481/make_b481.py   (from the repo root)
Writes CANDIDATES.json and CANDIDATE-MASTER.md (batch 480's candidate master with these in).
"""
import hashlib
import json
import pathlib
import re
import sys

B = pathlib.Path(__file__).resolve().parent
ROOT = B.parents[4]
H = ROOT / 'articles/inner-signal/humanize'
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
sys.path.insert(0, str(H / 'fix-20261025' / 'review'))
import suggestion_review as sr  # noqa: E402
import apply_answers as AA  # noqa: E402

BASE = B.parent / 'b480' / 'CANDIDATE-MASTER.md'
CONF = B.parent / 'b480' / 'recheck' / 'read' / 'CONFIDENCE.json'
K = {  # the bundle keys
    'how': 'HG-How-to-use-this-very-large-g-4', 'toc': 'HG-The-table-of-contents-is-hid-6',
    'prot': 'HG-Protecting-Yourself-from-Hyp-30', 'brain': 'HG-Forget-the-left-brain-right-62',
    'why': 'HG-Why-doing-it-myself-worked-b-65', 'voice': 'HG-When-your-voice-is-everybody-186',
    'six': 'HG-Please-don-t-put-six-metapho-238', 'begin': 'HG-Before-you-begin-242',
    'cap': 'HG-Capacity-before-content-377', 'nothing': 'HG-Nothing-happens-378', 'fake': 'HG-It-feels-fake-384',
    'p6': 'HG-Pattern-6-Ethical-double-bin-514', 'anx': 'HG-Anxiety-script-632',
    'forg1': 'HG-Forgiveness-without-bypass-661', 'forg5': 'HG-Forgiveness-without-bypass-665',
}


def sample(run, key):
    return (B / run / (key + '.out.txt')).read_text(encoding='utf-8')


def cut(text, first, last):
    assert text.count(first) == 1, first
    a = text.index(first)
    z = text.index(last, a) + len(last)
    return re.sub(r'\s+', ' ', text[a:z])


# 'from': pieces joined with a space: (run, bundle key, first words, last words) from a sample, or ('keep', words) for
# words of the paragraph that stay as they are between the spliced ones.
SPOTS = {
    'S11': {'part': 'A', 'where': 'How to use this very large guide, P1', 'his': False,
            'old': 'You can also look at the daily and weekly sections to make the practice your own.',
            'from': [('co', K['how'], 'You can also read some of the stuff in the daily and weekly sections', 'daily and weekly sections')],
            'fixes': [('in the daily and weekly sections', 'in the daily and weekly sections, to make the practice your own.',
                       'the sample went on "and take a look at some of the lots of appendices", which the next sentence says; the '
                       'sentence\'s point, his published "The daily and weekly sections help you make the practice your own", stays'),
                      ('You can also read', 'Also read',
                       'the gate\'s linter: "You can" is a coach phrase (E41), and one in a sentence this short is over the limit '
                       'of 2 per 100 words, a FAIL that can\'t be waived for model words; the old sentence had it too')],
            'published': ('His published guide: "The daily and weekly sections help you make the practice your own." (The working '
                          'copy\'s sentence, which he approved: "You can also look at the daily and weekly sections to make the '
                          'practice your own.")'),
            'red': 'Human, Medium (0.989), 16 words: this sentence', 'windows': ['A2']},
    'S12': {'part': 'A', 'where': 'The table of contents is hiding on the left, P1', 'his': True,
            'old': 'On a guide this long, that little hidden menu is your friend.',
            'from': [('cm', K['toc'], 'It\'ll be really helpful', 'as it\'s a long one.')],
            'fixes': [],
            'published': 'His published guide, his own words: "On a guide this long, that little hidden menu is your friend."',
            'red': 'Human, Low (0.649), 12 words: this sentence, his own', 'windows': ['A4']},
    'S14': {'part': 'A', 'where': 'Protecting Yourself from Hypnotists, P2', 'his': False,
            'old': ('Even when not actively engaging the conscious mind, there are many ways to influence people. Marketers and '
                    'interface designers know this perfectly well. In the Federal Trade Commission’s report on “dark patterns,” '
                    'they describe designs that trick or manipulate consumers.'),
            'from': [('co', K['prot'], 'There are a lot of ways to influence people', 'engaging their conscious mind.'),
                     ('keep', 'Marketers and interface designers know this perfectly well.'),
                     ('co', K['prot'], 'The Federal Trade Commission has a report', 'manipulate consumers.')],
            'fixes': [('a report on their “dark patterns” - designs used to trick and manipulate consumers.',
                       'a report on “dark patterns” - designs that trick or manipulate consumers.',
                       'the gate\'s preservation reviewer (G-S14, first draft): Emulate\'s "their" and "used to" made the dark '
                       'patterns the marketers\' own, used on purpose, and "trick and manipulate" said both where his line says '
                       'either; his "designs that trick or manipulate consumers" put back')],
            'published': ('His published guide: "Influence doesn’t wait for the conscious mind to sign a form. Marketers and '
                          'interface designers know this perfectly well. The FTC’s report on dark patterns describes designs that '
                          'trick or manipulate consumers, while the OECD describes commercial patterns that steer, deceive, coerce, '
                          'or manipulate people toward choices that may work against their interests." (His second sentence stays '
                          'as it is.)'),
            'red': 'Human, Medium (0.982), 77 words: the paragraph before and these three sentences', 'windows': ['A13']},
    'S15': {'part': 'A', 'where': 'Protecting Yourself from Hypnotists, P3', 'his': False,
            'old': ('Conscious agreement, unconscious receptivity, emotional compliance, legal and ethical consent. Can people have '
                    'their minds influenced without conscious agreement of their adult self?'),
            'from': [('co', K['prot'], 'Conscious agreement, unconscious receptivity', 'of their adult self?')],
            'fixes': [],
            'published': ('His published guide: "Conscious agreement is one thing. Unconscious receptivity is another. Emotional '
                          'compliance is another. Legal and ethical consent is another. A mind can be influenced without the adult '
                          'self having clearly chosen the influence."'),
            'red': 'Human, Low (0.848), 10 words: its first sentence, the four kinds of agreement', 'windows': ['A15']},
    'S16': {'part': 'A', 'where': 'Forget the left-brain/right-brain cartoon, P4', 'his': False,
            'old': 'So these modes can correct each other.',
            'from': [('cm', K['brain'], 'So each can correct the other.', 'correct the other.')],
            'fixes': [],
            'published': 'His published guide: "Let the modes correct each other."',
            'red': 'Human, Medium (0.989), 14 words: this sentence and the next paragraph', 'windows': ['A25']},
    'S17': {'part': 'A', 'where': 'Forget the left-brain/right-brain cartoon, P5', 'his': False,
            'old': 'And it’s got to lead somewhere!',
            'from': [('cm', K['brain'], 'It’s got to lead somewhere!', 'lead somewhere!')],
            'fixes': [],
            'published': ('The working copy\'s line, which he approved: "And it’s got to lead somewhere!" (his published guide: "A '
                          'powerful state matters only if something survives it: kinder behavior, more humility, better judgment, '
                          'real service, or a more workable ordinary life.")'),
            'red': 'Human, Medium (0.989), 14 words: this line and the sentence before it', 'windows': ['A25']},
    'S18': {'part': 'A', 'where': 'Why doing it myself worked better for me, P1', 'his': False,
            'old': ('I was sober at the session and didn\'t feel especially suggestible, but I suspect that\'s not even the main '
                    'reason the pro didn\'t work very well for me. The bigger issue was trust and precision.'),
            'from': [('cm', K['why'], 'One reason was that I was sober', 'susceptible to hypnosis.'),
                     ('cm', K['why'], 'But I think a bigger reason is', 'bigger reason is'),
                     ('keep', 'trust and precision.')],
            'fixes': [('One reason was that', 'One reason might have been that',
                       'his published "Maybe part of that was state-dependent" and the working copy\'s "I suspect that\'s not even '
                       'the main reason": a possible reason, not a sure one'),
                      ('wasn\'t that susceptible', 'didn\'t feel that susceptible',
                       'his published "didn’t feel especially suggestible" is how he felt, not a fact about how susceptible he is')],
            'published': ('His published guide: "The session with the hypnotist did very little. Maybe part of that was '
                          'state-dependent: I was sober and didn’t feel especially suggestible. The larger issue was trust and '
                          'precision." The sample\'s "But I think a bigger reason is" runs on into the next paragraph; its end here '
                          'is his "trust and precision."'),
            'red': 'Human, Medium (0.944), 31 words, and Human, Low (0.531), 7 words: these two sentences', 'windows': ['A27', 'A28']},
    'S19': {'part': 'A', 'where': 'Why doing it myself worked better for me, P2', 'his': False,
            'old': 'And I can notice my body saying no before my conscious mind talks me into a yes.',
            'from': [('co', K['why'], 'I can tell when my body is saying no', 'around to a yes.')],
            'fixes': [],
            'published': ('His published guide: "I can catch the body’s no before the conscious mind writes a persuasive little essay '
                          'called yes."'),
            'red': 'Human, Low (0.829), 17 words: this sentence', 'windows': ['A30']},
    'S20': {'part': 'A', 'where': 'When “your voice” is everybody else’s voice, P11', 'his': False,
            'old': 'You want to let your quieter preferences bubble up to the surface so you can be sure you’re not just echoing your social group.',
            'from': [('cm', K['voice'], 'You want to be able to let the quiet little preferences', 'would want you to do.')],
            'fixes': [('your “social” group', 'your social group',
                       'Emulate\'s quote marks around "social" taken off (the habit Joel caught on 2026-10-25, quote marks around '
                       'inner child)')],
            'published': ('His published guide: "Sometimes a temporary, intentional period of distance from the people or group '
                          'supplying the answers helps quieter preferences surface. Use that distance only long enough to tell your '
                          'own signal from the social echo." (The two sentences before it are his inner child guide\'s and stay.)'),
            'red': 'Human, Low (0.722), 64 words: this sentence and the two before it, which are his inner child guide\'s',
            'windows': ['A77']},
    'S21': {'part': 'A', 'where': 'Please don’t put six metaphors in one trance, P2', 'his': False,
            'old': 'And when you\'re done, come back the other way.',
            'from': [('cm', K['six'], 'When you\'re done, make sure to come back the other way.', 'the other way.')],
            'fixes': [],
            'published': ('His published guide: "Keep the language in the world you chose: let a count mark something meaningful '
                          'there, and reverse the journey when you finish."'),
            'red': 'Human, Medium (0.987), 21 words: this sentence and the bracket after it', 'windows': ['A87']},
    'S22': {'part': 'A', 'where': 'Please don’t put six metaphors in one trance, P3', 'his': False,
            'old': 'Read it out loud as you\'re writing it. Long, elegant sentences don\'t read well when you\'re being induced. It\'s all just soup.',
            'from': [('cn', K['six'], 'And then read it out loud as you write it.', 'soup to you at that point.')],
            'fixes': [],
            'published': ('His published guide: "Pick one central verb, one sensory quality, one short refrain, and one transition '
                          'phrase, then read the script aloud; long elegant sentences become soup during an induction."'),
            'red': 'Human, Medium (0.974), 26 words: these three sentences', 'windows': ['A89']},
    'S23': {'part': 'A', 'where': 'Before you begin, P2', 'his': False,
            'old': 'Get clear on what it is you want to do during the induction. What do you want not to do today?',
            'from': [('cn', K['begin'], 'Think about what you want to do.', 'what you want to do.'),
                     ('cn', K['begin'], 'Are there things you don’t want to do today?', 'want to do today?')],
            'fixes': [],
            'published': ('His published guide: "Choose the question or quality you want to explore, what you’re leaving alone today, '
                          'and how much time you have."'),
            'red': 'Human, Medium (0.982), 58 words: these two sentences and the rest of the paragraph to its last sentence',
            'windows': ['A91']},
    'S24': {'part': 'A', 'where': 'Before you begin, P3', 'his': False,
            'old': 'Put yourself in a place where you can safely do this.',
            'from': [('cm', K['begin'], 'Make sure you\'re in a safe place to do this.', 'place to do this.')],
            'fixes': [],
            'published': ('His published guide: "Choose a physically secure place without driving, water, machinery, or anyone needing '
                          'your supervision." (Two of the three samples gave this sentence word for word.)'),
            'red': 'Human, Medium (0.986), 11 words: this sentence', 'windows': ['A93']},
    'S25': {'part': 'A', 'where': 'Before you begin, P4', 'his': False,
            'old': ('Deciding to do it. How will you coax yourself to do this? Make it spacious? Make it warm and held? Something '
                    'else? Preview what you are going to do: will you close your eyes? Will you come out and go back in again? '
                    'What will you do at the end?'),
            'from': [('cn', K['begin'], 'Decide to do it.', 'What will you do at the end?')],
            'fixes': [('coax yourself to do it?', 'coax yourself to do this?',
                       'the gate\'s linter (R1, an action "it" near a paragraph start; Joel 2026-09-30: "the first it is unclear '
                       'referent"): the old sentence\'s "this" put back')],
            'published': ('His published guide: "Decide what kind of encouragement is welcome: spacious listening, warm company, or a '
                          'firmer invitation to stay with a feeling. Preview eye closure, any repeated exit and re-entry, and the '
                          'return." (The rest of the paragraph stays, with the stop lines of card S3b.)'),
            'red': ('Human, Medium (0.949), 20 words; Low (0.879), 2 words ("Something else?"); Medium (0.957), 28 words: these '
                    'sentences'), 'windows': ['A95', 'A96', 'A97']},
    'S26': {'part': 'A', 'where': 'Capacity before content, P8', 'his': False,
            'old': 'Give me one next action!',
            'from': [('co', K['cap'], 'What is one next thing I can do?', 'thing I can do?')],
            'fixes': [],
            'published': ('The working copy\'s request, which he approved (batch 470): "Prepare me BEFORE you break it open! Ground me '
                          'BEFORE you show me the memory! Support me BEFORE you make it intense! Give me one next action!" (his '
                          'published guide: "If the full truth would overwhelm me, please do not reveal it all. Show me the capacity '
                          'before the content.")'),
            'red': 'Human, Low (0.727), 6 words: this request', 'windows': ['A138']},
    'S27': {'part': 'A', 'where': 'Capacity before content, P9', 'his': False,
            'old': ('especially if it relates to trauma and memory. The mind makes it symbolic, squashes things together, distorts, '
                    'dramatizes, pulls from cultural influences, fears etc. So, treat it like an image and get some help outside of '
                    'yourself!'),
            'from': [('co', K['nothing'], 'especially if it has to do with trauma or memories.', 'trauma or memories.'),
                     ('keep', 'The mind makes it symbolic, squashes things together, distorts, dramatizes, pulls from cultural '
                              'influences, fears etc.'),
                     ('co', K['cap'], 'So take it as an image and get some outside help!', 'some outside help!')],
            'fixes': [],
            'published': ('The working copy\'s paragraph, which he approved (batch 470): "REMEMBER: Not everything in hypnotic imagery '
                          'is literal, especially if it relates to trauma and memory. ... So, treat it like an image and get some help '
                          'outside of yourself!" (his published guide: "The result is symbolic information or a hypothesis, never '
                          'proof of history.")'),
            'red': 'Human, Medium (0.989), 16 words, and Human, Medium (0.982), 13 words: the end of its first sentence and its last',
            'windows': ['A139', 'A141']},
    'S28': {'part': 'A', 'where': 'Nothing happens, P1', 'his': False,
            'old': 'Is there a way you could try this on a smaller scale?',
            'from': [('co', K['nothing'], 'Could you try it on a smaller scale?', 'a smaller scale?')],
            'fixes': [('try it on', 'try this on', 'the gate\'s linter (R1, an action "it" at a paragraph\'s start; Joel 2026-09-30: '
                       '"the first it is unclear referent"): the old sentence\'s "this" put back')],
            'published': 'His published guide: "Start smaller:"',
            'red': 'Human, Low (0.618), 12 words: this sentence', 'windows': ['A142']},
    'S29': {'part': 'A', 'where': 'Nothing happens, P2', 'his': True,
            'old': 'Ask: “Show me one body sensation.” “Show me one word.” “Show me whether today is for listening or resting.”',
            'from': [('co', K['nothing'], 'Maybe ask to', 'or even just whether'), ('keep', 'today is for listening or resting.')],
            'fixes': [('just one word, or even', 'just one word. Or even',
                       'the gate\'s linter: three asks joined with "or" in one sentence are a list of three (E125, a FAIL in model '
                       'words), so the third is its own sentence, the way he split his own')],
            'published': ('His published guide, his own words: "“Show me one body sensation.” “Show me one word.” “Show me whether '
                          'today is for listening or resting.”" The sample\'s last words ("whether it is more for listening to '
                          'something or resting today") make it listening to something outside you; his "today is for listening or '
                          'resting" ends it instead.'),
            'red': 'Human, Low (0.575), 31 words: these three requests and the next section\'s first sentence', 'windows': ['A143']},
    'S30': {'part': 'A', 'where': 'It feels fake, P1', 'his': False,
            'old': 'Do you have a sense of what it is that feels fake?',
            'from': [('co', K['fake'], 'Have you got any sense of what it is', 'feel fake?')],
            'fixes': [],
            'published': ('His published guide: "First ask what feels fake: the wording, the image, the expectation, or the role '
                          'you’re trying to perform."'),
            'red': 'Human, Low (0.575), 31 words: this sentence and the three requests before the heading', 'windows': ['A143']},
    'S31': {'part': 'A', 'where': 'It feels fake, P2', 'his': True,
            'old': 'Maybe you\'ve fooled yourself before, and that part remembers.',
            'from': [('co', K['fake'], 'You may have fooled yourself in the past', 'this part knows it.')],
            'fixes': [(' and this part knows it.', ', and that part remembers.',
                       'the gate\'s preservation reviewer (G-S31, first draft): "this part knows it" lost his "remembers", which '
                       'his next line picks up ("Tell me what you remember"), so his words end the sentence; and Emulate\'s "Try" for '
                       'his "works well here" made his claim a suggestion, so his next sentence stays as it is')],
            'published': ('His inner child guide, his own words: "Maybe you\'ve fooled yourself before, and that part remembers. '
                          '"Tell me what you remember, I\'m listening." works well here."'),
            'red': ('Human, Low (0.531), 10 words: this sentence, his own (his next line, "Tell me what you remember, I\'m '
                    'listening." works well here., Low (0.851), stays)'), 'windows': ['A146']},
    'S32': {'part': 'B', 'where': 'Pattern 6: Ethical double binds, P2', 'his': True,
            'old': 'An ethical one offers two genuinely safe routes.',
            'from': [('cn', K['p6'], 'An Ethical Double Bind Question gives someone', 'two safe things to do.')],
            'fixes': [('two safe things', 'two genuinely safe things',
                       'the gate\'s preservation reviewer (G-S32, first draft): Emulate dropped his "genuinely", the word that '
                       'says the safety is real, which is what separates the ethical double bind from the manipulative one')],
            'published': ('His published guide, his own words: "A manipulative double bind traps every answer inside the speaker’s '
                          'agenda. An ethical one offers two genuinely safe routes."'),
            'red': 'Human, Low (0.640), 8 words: this sentence, his own', 'windows': ['B5']},
    'S33': {'part': 'B', 'where': 'Anxiety script, P1', 'his': False,
            'old': 'A script you could use for anxiety is:',
            'from': [('cm', K['anx'], 'Here is a little script you could use:', 'you could use:')],
            'fixes': [],
            'published': ('The working copy\'s line, which he approved: "A script you could use for anxiety is:" (his published '
                          'guide: "For anxiety:"; the heading says "Anxiety script")'),
            'red': 'Human, Medium (0.984), 18 words: this line and the script\'s first two questions', 'windows': ['B33']},
    'S34': {'part': 'B', 'where': 'Anxiety script, P2', 'his': False,
            'old': 'Where are my body parts?',
            'from': [('cn', K['anx'], 'Lets see if I can find my body parts.', 'my body parts.')],
            'fixes': [('Lets see', 'Let’s see', 'Emulate\'s typo, "Lets" for "Let’s" (Joel, 2026-10-25: "i didn\' tmake these typos, '
                       'did you?"), with the curly apostrophe the section\'s other words have (the gate\'s three reviewers failed '
                       'the first draft\'s straight one)')],
            'published': 'The working copy\'s script, which he approved: "Where are my body parts? What are my feet doing? ..."',
            'red': 'Human, Medium (0.984), 18 words: the line before and these first two questions', 'windows': ['B33']},
    'S36': {'part': 'B', 'where': 'Forgiveness without bypass, P5', 'his': False,
            'old': 'What is theirs? What is mine?',
            'from': [('cm', K['forg5'], 'What’s theirs and what’s mine?', 'what’s mine?')],
            'fixes': [],
            'published': ('His published guide: "“What belongs to them?” “What belongs to me?”" (the working copy\'s "What '
                          'boundaries need to be set?", which he approved, stays: Emulate\'s "What boundaries do I need to set as a '
                          'result?" dropped his "still" ("What boundaries are still needed?") and added a cause, and the gate\'s '
                          'preservation reviewer failed it)'),
            'red': 'Human, Medium (0.963), 10 words: these two questions with his "What does accountability require?"',
            'windows': ['B41']},
}

# The windows of BUNDLE.json that get no candidate, and why (each is in CONFIDENCE.json under its part).
LEFT = {
    'A13 (Protecting Yourself from Hypnotists, P1)': 'the window also holds P2\'s first three sentences, which S14 changes; '
        'Emulate\'s versions of P1 are the same list with an "It" that has nothing to refer to',
    'A39 (Instead of blame, P2)': 'his inner child guide\'s three questions (Medium, 0.987): Emulate\'s version turns "it" into '
        '"they" in a paragraph that says "it" throughout and drops "stand to" from "Could it stand to take any of them?"',
    'A53 (Working with your guards, P4)': 'his inner child guide\'s "I\'m not going to force my way past you." (Medium, 0.987): '
        'Emulate kept it or changed it to "I don\'t want to go past you"',
    'A75 (When "your voice" is everybody else\'s voice, P11)': '"Temporary Separation." (Low, 0.851, 2 words), the label the '
        'paragraph starts with; a two-word window can\'t read High, and Emulate\'s versions drop the label or turn it into a question',
    'A79 (When "your voice" is everybody else\'s voice, P12)': 'every sample drops "a kind of bargain for belonging", his '
        'published "belonging bargains", which the section\'s question "Where am I buying my sense of belonging" picks up',
    'A111 (Sober induction, P13 and P14)': 'every sample keeps "Just let it be there for now." word for word and drops "You '
        'don\'t need to tell the whole story yet."',
    'A119 (Already open? Contain before you deepen, P4)': 'Emulate\'s versions make "My body may stay safe" a promise, "My body '
        'will be safe" (his published "The body may stay safe."); the only other change was a comma',
    'A135 (Finish without forcing a revelation, P1)': 'his inner child guide\'s line, which all three samples kept word for word',
    'B9 (Reframing, P1)': 'its questions are his published ones ("What else might be true?" "What is this part trying to do for '
        'me?"); the samples changed them',
    'B19 (Appendix C, P1)': '"I don\'t have to obey it. I don\'t even have to attack it.": the samples kept it word for word, or '
        'dropped "even"',
    'B37 (Forgiveness without bypass, P3)': 'his published three sentences to the inner child; every sample changes who speaks '
        '("We don\'t have to ...") or what is promised',
    'A137 (Capacity before content, P8)': 'the three BEFORE requests: Emulate\'s version puts "Please" in front of each, and '
        'three new exclamations in a row fail the linter\'s exclamation rate (S1, S2), which can\'t be waived for model words; '
        'the Low request after them is S26',
    'B35 (Forgiveness without bypass, P1)': 'the only change a sample offered, "We remember that it can all be true at once." '
        '(no "just"), is a coach phrase in model words ("remember that", E41), a FAIL',
    'B39 (Forgiveness without bypass, P5)': '"What boundaries need to be set?" with his "What was the impact?" (Medium, 0.981): '
        'Emulate\'s "What boundaries do I need to set as a result?" dropped his published "still" and added a cause, and the '
        'gate\'s preservation reviewer failed it',
    'B23 (Hypnosis-specific audit, the one AI window)': 'his list (2c); Emulate\'s three versions change what three of its seven '
        'questions ask: question 23 on his questions page',
}


def build():
    md = BASE.read_text(encoding='utf-8')
    bl = sr.blocks(md)
    raw = re.split(r'\n\s*\n', md.rstrip('\n'))
    assert len(raw) == len(bl)
    by = {sr.where(bl, b['i']): b['i'] for b in bl}
    flat = lambda x: x.translate(str.maketrans({'’': "'", '‘': "'", '“': '"', '”': '"'}))
    new_text, cands = {}, {}
    for k, s in SPOTS.items():
        i = by[s['where']]
        t = new_text.get(i, bl[i]['text'])
        old = s['old']
        if t.count(old) != 1:   # the working copy mixes straight and curly quotes; match either
            k0 = flat(t).find(flat(old))
            assert k0 >= 0 and flat(t).count(flat(old)) == 1, (k, old[:60])
            old = t[k0:k0 + len(old)]
        pieces = [p[1] if p[0] == 'keep' else cut(sample(p[0], p[1]), p[2], p[3]) for p in s['from']]
        for p in s['from']:
            if p[0] == 'keep':
                assert flat(p[1]) in flat(old), (k, 'kept words not in the old text', p[1][:40])
        raw_new = ' '.join(pieces)
        new = raw_new
        done = []
        for a, b, why in s['fixes']:
            assert new.count(a) == 1, (k, a)
            new = new.replace(a, b)
            done.append({'replace': a, 'with': b, 'why': why})
        assert new != old, k
        new_text[i] = t.replace(old, new)
        cands[k] = {'part': s['part'], 'where': s['where'], 'block': i, 'his': s['his'], 'red': s['red'],
                    'windows': s['windows'], 'samples': ['%s/%s' % (p[0], p[1]) for p in s['from'] if p[0] != 'keep'],
                    'old': old, 'sample_words': raw_new, 'new': new, 'fixes': done, 'published': s['published']}
    out, lost = list(raw), []
    for i, t in new_text.items():
        out[i] = AA.set_block_text(raw[i], t, lost)
    assert not lost, lost
    master = '\n\n'.join(out) + ('\n' if md.endswith('\n') else '')
    bl2 = sr.blocks(master)
    assert len(bl2) == len(bl)
    for k, c in cands.items():
        c['paragraph_before_change'] = bl[c['block']]['text']
        c['paragraph_after'] = bl2[c['block']]['text']
        assert c['new'] in c['paragraph_after'], k
    (B / 'CANDIDATE-MASTER.md').write_text(master, encoding='utf-8')
    rec = {'base': str(BASE.relative_to(ROOT)), 'base_sha256': hashlib.sha256(md.encode('utf-8')).hexdigest(),
           'candidate_master_sha256': hashlib.sha256(master.encode('utf-8')).hexdigest(), 'spots': cands, 'left': LEFT}
    (B / 'CANDIDATES.json').write_text(json.dumps(rec, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    return cands


if __name__ == '__main__':
    cands = build()
    for k, c in cands.items():
        print('%s%s | %s' % (k, ' (his)' if c['his'] else '', c['new']))
