"""The hypnosis guide's marking page for the strict Emulate check (REVIEW-EMULATE.json, REVIEW-EMULATE.html).

Joel, 2026-10-25 19:42 UTC, on the last page: "i didn' tmake these typos, did you?", "why was inner child in quotes? ...
looks like more crap from emulate you forgot to check. make those emulate checks more strict pls for future also" and
"make sure all the citations and stuff are not messed up in the emulate-infused articles"; and "that was a good marking
page save that so it's how we work in future editing work".

The check (run_audit.sh; tools/humanization/emulate_artifacts.py) compared the guide with his own texts: his published post
of 2026-09-28, his editor HTML and drafts, his inner child texts, his messages, and the new sentences he approved today.
Ten fresh Sonnet readers then read every paragraph that isn't his word for word beside his own paragraph (PAIRS-<n>.txt,
BRIEF.txt) and listed what it adds, loses or gets wrong (READ-<n>.json, 808 findings). What was mechanical is fixed already
(fix_citations.py, fix_typos.py and the spaces, listed on the page). Of the rest, I checked each one that a reader marked
"matters" against his texts and records: a change he made or approved himself, a point the guide makes nearby, or a
rewording that keeps his meaning stays as it is; what's left is here, each with his own version beside it. Quote marks
Emulate put around words are one card, the same way his last page had the spaces.

  python3 articles/inner-signal/humanize/fix-20261025/emulate-check/build_emulate_review.py
"""
import datetime
import hashlib
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / 'review'))
import build_review as br  # noqa: E402  (its helpers, and the guide as it is now)

sr = br.sr
GIT_FILE = 'articles/inner-signal/humanize/fix-20261025/emulate-check/REVIEW-EMULATE.html'
TYPES = {
    'quotes': {'label': 'Quote marks', 'about': 'Quote marks Emulate put around words your guide has plain.'},
    'meaning': {'label': 'Emulate changed your meaning', 'about': 'A condition, limit or point of yours that Emulate dropped or turned around; the suggestion puts it back in the paragraph\'s own words.'},
    'source': {'label': 'Sources', 'about': 'A reference Emulate changed: who wrote it, what it found, what it\'s about.'},
}
FOUND = 'The strict Emulate check: a fresh reader comparing this paragraph with your published one (%s)'

# blocks and the quoted words that lose their quote marks; "x" -> new text when it changes more than the marks
QUOTES = [(11, '‘grow up’'), (11, '‘adult’'), (12, '‘subconscious mind’'), (14, '‘trance experience’'), (15, '‘communion’'),
          (62, '‘modes’'), (76, '‘subconscious’'), (76, '‘mind’'), (76, '‘ecology’'), (76, '‘right’'), (76, '‘wrong’'),
          (78, '‘whole’'), (79, '‘Invoke’'), (80, '‘ecology’'), (80, '‘critic’'), (80, '‘wiser’'), (81, '‘invoke’'),
          (216, '‘adult’'), (216, '‘state’'), (218, '‘permissive’'), (219, '‘skeptical guard’'), (352, '‘inner part’'),
          (352, '‘should’'), (353, '‘stay there’'), (353, '‘take’'), (354, '‘do something’'), (354, '‘doing that’'),
          (357, '‘great revelation’'), (357, '‘in real life’'), (358, '‘protector’'), (358, '‘repairs’'), (360, '‘analytical’'),
          (502, '‘awareness’'), (661, '‘force’'), (722, '‘families’'), (724, '‘knowing’'), (726, '‘releasing’'),
          (328, "'thing'"), (387, "'grown up'"), (387, "'good enough'"), (521, "'tag'"), (521, "'oily'"),
          (33, '“Mind Control”'), (57, '“prove”'), (147, '“embody”'), (154, '“mature”'), (154, '“do”'), (156, '“child”'),
          (159, '“healed”'), (299, '“True”'), (346, '“coming back”'), (346, '“induction”'), (348, '“act out”'),
          (350, 'If any “younger” parts'), (350, 'literally “younger”'), (350, '“meeting”'), (351, '“Nurturer”'), (351, '“Protector”'), (351, '“Guide”'), (351, '“tone”'),
          (351, '“Witness”'), (426, '“Force”'), (428, '“Inner Child”'), (428, '“Protector”'), (428, '“Nurturer”'),
          (428, '“Guide”'), (428, '“Child”'), (429, '“force”'), (429, '“protectors,”'), (429, '“heal”'), (431, '“safety”'),
          (431, '“your unconscious mind”'), (431, '“get out”'), (434, '“hidden ‘commands’”'), (434, '“commands”'),
          (447, '"get hypnotized"'), (469, '“safe”'), (469, '“make up”'), (580, '"psychosis-like state"'), (642, '“real”'),
          (649, '"fit"'), (651, '"bad,"'), (651, '"certified"'), (679, '"bad"'), (695, '“real world”')]
SPECIAL = {'“True”': 'true', '“hidden ‘commands’”': 'hidden commands', 'If any “younger” parts': 'If any younger parts',
           'literally “younger”': 'literally younger'}

# (id, type, block, [(old, new)], title, why (his version), note)
CARDS = [
    ('EM-1', 'meaning', 86, [('the part of me that knows it belongs to life, not any wound, or role, or family, or group, or identity, or ideology, or story',
                              'the part of me that knows it belongs to life before it belongs to any wound, or role, or family, or group, or identity, or ideology, or story')],
     'Belongs to life before anything else',
     'Your published line: "the part of me that belongs to life before it belongs to any wound, role, family, group, identity, ideology, or story". Emulate made it "not any wound ...", which denies those belong to you at all.',
     'Puts back your "before it belongs to"; the rest of Emulate\'s sentence stays.', '1.82'),
    ('EM-2', 'meaning', 96, [('It is important to note here that I’m not suggesting that all of the steps in this process have been formally tested and proven.',
                              'It’s built from familiar practices like modeling and supported action, but I’m not suggesting that the whole sequence has been formally tested and proven as one treatment.')],
     'Borrowed adulthood: which part is untested',
     'Your published line: "It combines familiar practices—witnessing, modeling, supported action, and gradual transfer of responsibility—without claiming that the complete sequence has been validated as one treatment." Emulate dropped the familiar practices and made it "not all of the steps ... have been tested", which says some steps are untested; yours says each step is familiar and only the whole sequence is untested.',
     'Your two points in plainer words, with two of your four practices (a list of four reads as AI, and the gate refuses one I write).', '2.7, 2.8'),
    ('EM-3', 'meaning', 176, [('for example when your family, religion, or community ‘takes over’ very early in your life',
                               'for example when a controlling family, a rigid religion or an enmeshed community takes over very early in your life')],
     'Which families and religions',
     'Your published line: "In controlling families, rigid religions, enmeshed communities, or high-pressure achievement systems". Without "controlling", "rigid" and "enmeshed" it reads as if any family, religion or community does this.',
     'Your three words back; the quote marks Emulate put around "takes over" go too.', '3.24, 3.25'),
    ('EM-4', 'meaning', 184, [('You can rebel, but you can’t choose', 'You can rebel, but you can’t choose yet')],
     'Not choosing yet',
     'Your published line: "You can rebel, but you cannot yet choose." Without "yet" it says you never will.', 'One word.', '3.32'),
    ('EM-5', 'meaning', 185, [('You were too occupied in not being in pain, reading out what was dangerous',
                               'You were too busy avoiding pain, reading what was dangerous')],
     'Garbled: "occupied in", "reading out"',
     'Your published line: "when childhood is organized around avoiding pain and preserving attachment, attention goes into reading danger, meeting expectations, and keeping the bond". Emulate\'s "too occupied in not being in pain, reading out what was dangerous" stops a reader twice.',
     'Your "avoiding pain", and "reading" for "reading out", in the sentence Emulate made.', '3.35'),
    ('EM-6', 'meaning', 239, [('what the short refrains are', 'what the short refrain is')],
     'One refrain, as the heading says',
     'Your published line: "Pick one central verb, one sensory quality, one short refrain, and one transition phrase". The section is "Please don\'t put six metaphors in one trance"; Emulate made the refrain plural.',
     'One word.', '4.15'),
    ('EM-7', 'meaning', 243, [('If you are overwhelmed by chemicals,', 'If you are intoxicated,')],
     'Not when intoxicated',
     'Your published line: "When intoxicated, acutely confused, or unable to keep yourself safe, deal with immediate support rather than exploratory hypnosis." Emulate\'s "overwhelmed by chemicals" lets someone who is merely drunk or high go ahead.',
     'Your word; it changes who should stop.', '4.20'),
    ('EM-8', 'meaning', 311, [('If you have done anything to alter your state when coming out of a trance, make sure to reverse those things.',
                               'If you have done anything to alter your state when entering the trance, make sure to reverse those things.')],
     'Reverse what you did going in',
     'Your published line: "Reverse whatever you used to enter." Emulate wrote "when coming out of a trance", the opposite end; the examples after it (floating, shrinking) are all things done going in.',
     'Your word, "enter".', '5.11'),
    ('EM-9', 'meaning', 320, [('to help me know what I need to know in a form and at a level that will be useful',
                               'to help me know what I need to know, only in a form and at a time that will be useful')],
     '"Only", and the timing',
     'Your published line: "please help me understand what I need to know, only in the form and timing that is useful, kind, stabilizing, and real." Emulate dropped "only" and the timing, so the request no longer limits when an answer comes.',
     'Your "only" and your timing; Emulate\'s "at a level" goes, as yours had form and timing only.', '5.20'),
    ('EM-10', 'meaning', 382, [('Show yourself one body sensation, one word, ask yourself if you want to listen today or if you need to rest.',
                                'Ask: “Show me one body sensation.” “Show me one word.” “Show me whether today is for listening or resting.”')],
     'Ask to be shown, not show yourself',
     'Your published lines: "“Show me one body sensation.” “Show me one word.” “Show me whether today is for listening or resting.”" When nothing happens, you ask your deeper mind to show you something small; Emulate made it "Show yourself", so the reader does it all.',
     'Your three requests, word for word.', '6.16'),
    ('EM-11', 'meaning', 425, [('DO NOT: Attempt to “force” memories, to use trance to “prove” something happened to you, or to skip medical attention for symptoms just because you can “force” them down using hypnosis.',
                                'DO NOT: Attempt to force memories, to use trance to prove something happened to you, or to suppress medical symptoms.')],
     'Don\'t suppress medical symptoms',
     'Your published line: "Do not force memory recovery, use trance to prove what happened, or suppress medical symptoms." Emulate\'s version only forbids skipping medical attention, so pushing symptoms down with hypnosis reads as fine if you also see a doctor.',
     'Your rule, in your words; the quote marks go too. (The owner-delivery gate\'s reviewers refused my first wording, "instead of getting them looked at", as a condition yours doesn\'t have.)', '6.57'),
    ('EM-12', 'meaning', 474, [('How can you trust me 1% more?', 'What would help you trust me 1% more?')],
     'What would help the part trust you',
     'Your published line: "What are you protecting me from, and what would help you trust me 1% more?" Emulate\'s "How can you trust me 1% more?" asks the part to do the work; yours asks what you can do.',
     'Your question, word for word.', '7.25'),
    ('EM-13', 'meaning', 515, [('Ethical Double Bind Questions might be:', 'An ethical one offers two genuinely safe routes. Ethical Double Bind Questions might be:')],
     'What makes a double bind ethical',
     'Your published line: "An ethical one offers two genuinely safe routes." The paragraph before says what a manipulative one does; Emulate dropped what makes the ethical one different.',
     'Your sentence, word for word, before the examples; "one" is the double bind question of the paragraph before.', '7.61'),
    ('EM-14', 'meaning', 524, [("Nominalizations are words like 'healing',", "Nominalizations are words that turn a process into a noun, like 'healing',")],
     'What a nominalization is',
     'Your published line: "Nominalizations turn processes into nouns: healing, safety, trust ..." Emulate kept only the examples.',
     'Your definition, in front of the examples.', '8.1'),
    ('EM-15', 'meaning', 576, [('I do not tell people to override their fear.', 'I do not tell people to override their fear before asking what it’s protecting.')],
     'Override fear before asking',
     'Your published line, in the list of what you won\'t use NLP for: "To override fear before asking what the fear protects." Emulate made it a flat rule against overriding fear at all.',
     'Your condition back.', '8.65'),
    ('EM-16', 'meaning', 700, [('You don’t have to find out if it’s a protector immediately, and you may not be able to comfort it quickly, but whether warmth or distance helps, that doesn’t prove what it is.',
                                'You don’t have to find out if it’s a protector immediately, and you may not be able to comfort it quickly. The useful question is whether this way of responding helps you become clearer, steadier, and less hooked.')],
     'The test for a response',
     'Your published lines: "Neither response establishes its origin. ... The useful question is whether this way of responding helps you become clearer, steadier, and less hooked." Emulate\'s sentence breaks in the middle ("but whether warmth or distance helps, that doesn\'t prove") and drops your test.',
     'Your test, word for word, in place of Emulate\'s broken sentence (its "doesn\'t prove" is the pattern you flagged on 2026-10-24); the heading still says a response isn\'t a verdict on what it is.', '10a.2, 10a.11'),
    ('EM-S1', 'source', 621, [('noted that EFT was more effective than no intervention in a few studies', 'noted that EFT was more effective than no intervention in several of them')],
     'EFT: several trials, not a few',
     'Your published line: "A 2025 systematic review found seven randomized controlled trials involving EFT for anxiety disorders; EFT beat no intervention in several of them". Emulate\'s "in a few studies" weakens what the review found. ("Randomized control trials" is already back to "controlled".)',
     'Your "several of them".', '9.28'),
    ('EM-S2', 'source', 746, [("Also, Adam Eason's work with Benjamin Parris in the International Society of Hypnosis, specifically his article about self hypnosis, should be a useful thing to read",
                               "Also, Adam Eason and Benjamin Parris's article about self hypnosis for the International Society of Hypnosis should be a useful thing to read")],
     'Who wrote the ISH article',
     'Your published line: "Adam Eason and Benjamin Parris’s ISH article on self-hypnosis discusses self-directed learning and its relationship to another hypnotist and recordings." Emulate gave the article to Eason alone and made the two of them "work in" the society.',
     'Both authors, and the link stays on "article about self hypnosis". (The book titles here are back in italics, and "(1995) pp" is fixed.)', '10b.1'),
    ('EM-S3', 'source', 757, [('contains useful information on this.', 'is useful on the difference between compelling experience and historical verification.'),
                              ('but they point to their particular claims, not every use of hypnosis.', 'but they point to their particular claims rather than validating every use of hypnosis.')],
     'What chapter 7 is about, and what the links back up',
     'Your published lines: "Levine’s Trauma and Memory (2015), chapter 7, is useful on the difference between compelling experience and historical verification." and "The existing links in the evidence and specialist sections point to their particular claims rather than validating every use of hypnosis." Emulate\'s "useful information on this" doesn\'t say on what, and "they point to their particular claims, not every use of hypnosis" lost what the links do and don\'t back up.',
     'Your words for the chapter\'s topic and for what the links do. (The commas between "website" and "contains" are already gone.)', 'the check\'s citation list'),
]


def main():
    by_block = {}
    for i, q in QUOTES:
        by_block.setdefault(i, []).append(q)
    edits = []
    for i, qs in sorted(by_block.items()):
        for q in qs:
            new = SPECIAL.get(q, q[1:-1] if not q.endswith(',”') else q[1:-2] + ',')
            edits.append((i, q, new))
    br.add('EM-Q1', 'quotes', 'Quote marks Emulate put around words (%d places)' % len(QUOTES), 'approve', edits=edits,
           what='Takes the quote marks off %d words and phrases in %d paragraphs: %s.' % (
               len(QUOTES), len(by_block), ', '.join(sorted({SPECIAL.get(q) and q.replace('If any ', '').replace('literally ', '').replace(' parts', '') or q for _i, q in QUOTES}, key=str.lower))),
           why='Your published guide has these words plain. Emulate is known for odd quote marks, and you asked about the ones around inner child ("why was inner child in quotes? ... check and remove quotes if you find it elsewhere"). The single curly ones are its habit, not yours: your inner child guide has two.',
           stays='Every quote that is speech or a prayer, a word talked about as a word ("when this guide says "say""), a section\'s name, a term you use in a special sense ("human doing", “downloads”, ‘see’ the images, “hostile presences”), and the skeptical ones that carry a point (“attachments,” “transformations”, “healed” in your imagination).',
           note='One card, like the spaces on your last page. Revise if one of them should keep its quote marks.',
           found_by='The strict Emulate check (quote marks his texts don\'t have at that spot) and its readers')
    for sid, typ, block, pairs, title, why, note, ids in CARDS:
        br.add(sid, typ, title, 'approve', edits=[(block, old, new) for old, new in pairs], why=why, note=note,
               found_by=FOUND % ('items ' + ids if ids[0].isdigit() else ids))
    br.S.sort(key=lambda s: (br.first_block(s), br.order_key(s['id'])))
    br.overlaps()
    review = {
        'format': sr.FORMAT, 'review_id': 'inner-signal-hypnosis-guide-emulate-check-20261025',
        'title': 'Hypnosis Guide Emulate Check',
        'intro': [
            'This is your hypnosis guide as it is in Git now, with your answers from the last page in, and the strict Emulate check you asked for: every paragraph that isn\'t yours word for word, compared with your own texts by the check and by fresh readers. Each card has your own version beside it.',
            'Already fixed, because they were plain errors in none of your texts: 31 spaces before a full stop, comma or colon (22 on your last page, 9 more), 53 typos and slips (split words like "day dreams" and "child birth", "a ecology", "yo", "breath" for "breathe", "council" for "counsel", missing question marks, a bracket never closed, "does n’t"), and the references: the book titles in italics again, "(1995) pp", "randomized controlled trials". The list is in fix_typos.py and fix_citations.py in Git.',
            'Click <b>Approve</b>, <b>Reject</b> or <b>Revise</b> on each card, and add a comment if you want. If you leave cards unmarked, tell me whether to take my advice on them as you did last time. Your answers save as you click.',
        ],
        'git_file': GIT_FILE, 'article': {'file': br.ARTICLE, 'sha256': hashlib.sha256(br.MD.encode('utf-8')).hexdigest()},
        'links': {'guide': br.BLOB + br.ARTICLE, 'review': br.BLOB + 'articles/inner-signal/humanize/fix-20261025/emulate-check/REVIEW-EMULATE.json'},
        'built': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M UTC'),
        'types': TYPES, 'suggestions': br.S,
    }
    probs = sr.check(review, br.BL)
    for p in probs:
        print('PROBLEM', p)
    (HERE / 'REVIEW-EMULATE.json').write_text(json.dumps(review, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    if probs:
        sys.exit(1)
    page = sr.page(review, br.MD, br.BL)
    (HERE / 'REVIEW-EMULATE.html').write_text(page, encoding='utf-8')
    print(len(br.S), 'cards;', HERE / 'REVIEW-EMULATE.html', len(page), 'bytes')


if __name__ == '__main__':
    main()
