#!/usr/bin/env python3
"""Turn 110: Joel's review page, only the changes GPT's review and mine both recommend (AGREED.md), each in place in the
whole guide, built with tools/humanization/suggestion_review.py (REVIEW.json, REVIEW.html).

Joel, 2026-10-25 17:26 UTC (../t110-answers/JOEL-20261025-1726.md): "i'm attaching gpt's review of your proposal to
consider. i have not really read yours or GPT's yet because it's a lot of reading and prob no point until you can agree".
The cards: S1 and S3 (the two sections in the agreed order, experiments/t110-installs/reshape_t110.py, checked in Pangram
as they'd read, experiments/t110-api/), the ten cuts both reviews approve (C3 to C12), three small wording changes (P2,
P5, P6) and three questions (Q1 to Q3). Everything both would leave as it is is named in the intro, with the agreement.
The ids are the turn-109 sheet's, so his answers line up with both reviews.

  python3 articles/inner-child-therapy/experiments/t110-review/build_review.py     # REVIEW.json and REVIEW.html"""
import datetime
import hashlib
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
sys.path.insert(0, str(HERE.parent / 't110-installs'))
import suggestion_review as sr  # noqa: E402
import reshape_t110 as RS  # noqa: E402

ARTICLE = 'articles/inner-child-therapy/HUMANIZED-ARTICLE-SO-FAR.md'
BLOB = 'https://github.com/u-dont-existDOTcom/joel-articles/blob/handoff/claude-dangerous-adult-20260924-1631/'
EXP = BLOB + 'articles/inner-child-therapy/experiments/'
MD = (ROOT / ARTICLE).read_text(encoding='utf-8')
BL = sr.blocks(MD)
PANGRAM = {'guard': 'https://www.pangram.com/history/8d811715-68ec-4c68-8641-79c098f8fb5b',
           'hardest': 'https://www.pangram.com/history/65b8f598-3077-440a-a12f-349143dc2f5a'}

TYPES = {
    'structure': {'label': 'Order', 'about': 'A section in a new order, every sentence kept but a few words, named on its card.'},
    'cut': {'label': 'Cuts', 'about': 'A line the text around it already says.'},
    'reread': {'label': 'Wording', 'about': 'A few words changed, or a line of yours added.'},
    'ask': {'label': 'Questions', 'about': 'What a line is based on: a few words from you, no story needed.'},
}
S = []


def section_blocks(heading):
    """The paragraph blocks under HEADING, up to the next heading."""
    hits = [b['i'] for b in BL if b['level'] and b['text'] == heading]
    assert len(hits) == 1, heading
    out = []
    for b in BL[hits[0] + 1:]:
        if b['level']:
            break
        out.append(b['i'])
    return out


def q(quote, near=None):
    return sr.find_quote(BL, quote, near)


def arrangement(sid, key, heading, title, reads_notes, new_words, what, why, stays, warning=None):
    blocks = section_blocks(heading)
    old, new = RS.candidate(MD, key)
    assert [BL[i]['text'] for i in blocks] == [sr.blocks(p)[0]['text'] for p in old], key
    assert len(old) == len(new) == len(reads_notes)
    shown = [sr.blocks(p)[0]['text'] for p in new]   # as a reader reads it (no Markdown)
    reads = [{'text': t, 'note': n} | ({'new': new_words[k]} if new_words.get(k) else {}) for k, (t, n) in enumerate(zip(shown, reads_notes))]
    edits = [{'block': i, 'before': BL[i]['text'], 'after': t} for i, t in zip(blocks, shown) if BL[i]['text'] != t]
    s = {'id': sid, 'type': 'structure', 'title': title, 'advice': 'approve',
         'spans': [{'block': i, 'start': 0, 'end': len(BL[i]['text'])} for i in blocks], 'card_after': blocks[-1],
         'edits': edits, 'inserts': [], 'moves': [], 'reads': reads, 'reads_label': 'How %s would read' % heading,
         'what': what, 'why': why, 'stays': stays,
         'deciding': 'Approve puts this order in, word for word. Reject keeps the section as it is now, above.',
         'advice_note': 'Both reviews recommend it, and it read Human in Pangram as a section: %s' % PANGRAM[key],
         'found_by': 'GPT\'s review of the turn-109 sheet, and mine', 'approve_label': 'use this order'}
    if warning:
        s['warning'] = warning
    S.append(s)


arrangement(
    'S1', 'guard', 'Hear the Guard First', 'Hear the Guard First: your exchange in one piece',
    ['Your first two sentences.',
     'Your own order from before turn 109, with "It might say" as you wrote it.',
     '"The Nurturer voice" for "it the same" (P8): right after "a harder voice", "the same" and "that voice" could point at the harder one.',
     'The roommate, as it is.',
     'Its long sentence in two, and "call it all off": a fresh reader took "it" for the guard.',
     'As it is.',
     '"A protective job" for "a job like that": a fresh reader couldn\'t tell which job, and GPT asked to make it plain.'],
    {1: ['It might say'], 2: ['the Nurturer voice'], 4: [['call it ', 'all']], 6: ['protective']},
    'Your question, then what the part might say, your reply "Tell me what you remember, I\'m listening." and your reason '
    'for it, all in one paragraph as you had them. Then the harder voice, the roommate, moving out, hopes and self-blame, one a paragraph.',
    'In turn 109\'s order your reply sat two paragraphs below the question it answers. GPT: "the opening now jumps from '
    'asking to the outcome of listening, while the actual listening is deferred."',
    'Every sentence, and the order of the last four paragraphs but one: the harder voice comes up from second to third '
    'place. Why the roommate isn\'t straight after the exchange is in the agreement, linked above.')
arrangement(
    'S3', 'hardest', 'Before You Tell the Hardest Stuff', 'Before You Tell the Hardest Stuff: the danger lines back with the dream line',
    ['Your topic and your "I\'d assume", without the danger lines.',
     'As it is.', 'As it is.', 'As it is.',
     'Your dream line with your two danger lines after it, where you had them on 2026-10-19.'],
    {},
    'Your two lines "Just don\'t hold back a danger that\'s happening now…" and "Sometimes telling on yourself…" go back after '
    'the dream line they limit, so the section ends on the danger.',
    'They limit the dream advice. Turn 109 moved them up front, so the section ended on the dream line by itself. GPT: '
    '"preserving words does not preserve their working relationship."',
    'Every sentence, word for word. The topic still opens the section, and the DM, reporting and your question to ask '
    'stay in their own paragraphs.',
    warning='A fresh reader read "them" in "So I\'d ask them" as the cops, the last people named before it. That\'s the same '
            'in your original, so it stays as it is unless you name them in your words (Revise).')


def cut(sid, quote, title, why, stays, note, found, near=None):
    i, a, z = q(quote, near)
    line = BL[i]['text']
    S.append({'id': sid, 'type': 'cut', 'title': title, 'advice': 'approve',
              'spans': [{'block': i, 'start': a, 'end': z}],
              'edits': [{'block': i, 'before': line, 'after': sr.cut_text(line, a, z)}], 'inserts': [], 'moves': [],
              'what': 'Takes out "%s"' % quote.rstrip('.') + '.', 'why': why, 'stays': stays,
              'deciding': 'Approve cuts it. Reject keeps it.', 'advice_note': note,
              'found_by': found + '; GPT\'s review: approve the cut', 'approve_label': 'cut it'})


cut('C3', "So it's worth noticing what it's doing to you.", 'Ill Will and Loving-Kindness: the line before the question',
    'The question right after it ("Has it ever left anybody at ease, with nothing to regret afterward?") already asks the reader to look.',
    'The Buddha\'s account, the Human Torch and the question.', '', 'the point-of-view read, 2.3')
cut('C4', "The quest for self-knowledge is a life's journey, but you don't have to wait for your life to finish to figure out your best next move.",
    'Borrow Love: the life\'s-journey line',
    'It does make a point of its own (you can act before you know yourself fully), but here it interrupts the exercise before '
    'Solomon\'s paradox, and the exercise already gives you your next move.',
    'The exercise, "a cheap trick for becoming the outsider to your own mess", and Solomon\'s paradox.', '',
    'the point-of-view read, 2.7')
cut('C5', "Like the two truths at bedtime, a true complaint and real love don't cancel each other out, so you can take the true part without giving up your love or defending yourself.",
    'Love Doesn\'t Have to Wait for Trust: the moral after Mr. Rogers',
    'The scene already shows it, and "You can see the same move" ties it back to your bedtime story; his "Thank you for that perspective." is the stronger last line.',
    'The whole Mr. Rogers scene.', '', 'the point-of-view read, 3.1')
cut('C6', 'Sometimes human beings need to be being, not always doing. 🙃', 'Catch the Hook: the being, not doing line',
    'Your "Take a breath or three" already says to pause, and "Maybe then you\'ll find…" follows from the breath.',
    'The breath and what it makes room for.', 'The emoji goes with it. If it\'s your own joke, reject and it stays.',
    'the point-of-view read, 3.8')
cut('C7', "Going back to your life is part of the healing, too.", 'Close the Session: the last line',
    'The heading and your line to the little one ("We\'re going back to the life we\'re building.") already say it.',
    'The section ends on "whatever you\'re still feeling can come along."', '', 'the point-of-view read, 4.4')
cut('C8', ", which is ordinary", 'Untangling the Belonging Bargains: ", which is ordinary"',
    '"Most groups" already makes it normal, and the next sentence says when it turns into the bargain.',
    '"Most groups expect some conformity."', '', 'the point-of-view read, 6.3')
cut('C9', "Either way, that's pl/ork in its most literal form: play becomes part of forming your identity.",
    'Let the Child Be Bad at Things: the closing summary',
    'The two outcomes are already there (you may quit, or find a part of you that never had permission to exist), and the section says earlier that trying things on is how people grow into who they are.',
    'Your permission to quit, and the paragraph ends on that part of you.', '', 'the point-of-view read, 6.7')
cut('C10', "Having someone like that while you're struggling can be an enormous blessing.",
    'Borrowed Adulthood in Relationship: the blessing line',
    '"Maybe you\'re picturing them right now" already brings that person to mind, and the next paragraph says what they\'ve been doing for you. GPT calls this one a preference.',
    'The person who drives you to your appointments, and the paragraph ends on "Maybe you\'re picturing them right now."',
    '', 'the point-of-view read, 7.5')
cut('C11', "(nobody gets a gold star for forgiving fastest)", 'How to Forgive Without Forgetting: the gold-star aside',
    '"It can\'t be put on a schedule" says it, and it\'s the same kind of aside as "(nobody\'s taking attendance)", which you cut.',
    'Every permission: you don\'t have to forgive first to get safe, set boundaries, hold someone accountable, get justice or get better.',
    '', 'the point-of-view read, 8.2')
cut('C12', "(nobody's checking their inbox)", 'Missing Someone: the inbox aside',
    '"It doesn\'t matter whether they get any of it" says it, and it\'s the same kind of aside.',
    'What to do if it gets compulsive, and "I miss you, and I care."', '', 'the point-of-view read, 8.4')


def wording(sid, quote, new, title, what, why, stays, note, found, near=None):
    i, a, z = q(quote, near)
    line = BL[i]['text']
    S.append({'id': sid, 'type': 'reread', 'title': title, 'advice': 'approve',
              'spans': [{'block': i, 'start': a, 'end': z}],
              'edits': [{'block': i, 'before': line, 'after': line[:a] + new + line[z:]}], 'inserts': [], 'moves': [],
              'what': what, 'why': why, 'stays': stays, 'deciding': 'Approve puts it in. Reject keeps it as it is.',
              'advice_note': note, 'found_by': found, 'approve_label': 'use this wording'})


wording('P2', "I'd keep whatever you feel around them, and look at their track record.",
        'Keep what you feel around them in mind, and look at their track record too.',
        'Don\'t Give the Inner Adult Away: what "keep whatever you feel" means',
        'GPT\'s wording, so it says what to do with the feeling.',
        '"Keep whatever you feel" can mean keep feeling it, remember it or trust it. GPT: "Removing \'I\'d\' leaves that ambiguity intact."',
        'The questions after it: whether they respect a no, what happens when you disagree, and what backs them up.',
        'The line is mine (turn 72), from the guide\'s.', 'the point-of-view read, 1.4; GPT\'s review: revise for meaning')
wording('P5', 'A real-life child of yours, or a calm pet, can also act as a companion that brings out the relationship with your own inner child.',
        'A real-life child of yours, or a calm pet, can also act as a companion that brings out the relationship with your own inner child. '
        'My son did that for me, and I think that\'s very common for parents.',
        'Remind Yourself: your son', 'Adds your line about your son after the first sentence.',
        'Your answer of 2026-10-02 has it: "I actually used my son (i shouldn\'t say "used") to reconnect with my inner child, and '
        'I think that\'s very common for parents." This is that answer as an article sentence, without "used".',
        'The reminder that a child or a pet has their own needs.',
        'Unless you left it out on purpose: that day you added only "A real-life child of yours" to the paragraph.',
        'the point-of-view read, 3.3; GPT\'s review: approve')
wording('P6', "I'd leave out forgiving them and picturing their childhood.",
        "I'd leave out forgiving them and picturing their childhood here.",
        'Just Like Me: "here"', 'Adds "here" at the end.',
        'So it reads as this exercise\'s limit and can\'t be taken as advice against forgiving or understanding them at all. The pointer to the forgiveness section is dropped (GPT: optional).',
        'Your "I\'d", and the rest of the paragraph.', '', 'the point-of-view read, 4.2; GPT\'s review: add only "here"')


def ask(sid, quote, title, question, why, note, found):
    i, a, z = q(quote)
    S.append({'id': sid, 'type': 'ask', 'title': title, 'advice': 'ask', 'spans': [{'block': i, 'start': a, 'end': z}],
              'question': question, 'why': why, 'stays': 'The line stays as it is until you answer.', 'advice_note': note,
              'found_by': found})


ask('Q1', 'What people most often say helped is letting their defenses down.',
    'If the Love Isn\'t Coming Yet: "most often"',
    'What is "most often" based on: what people have told you, something you read, what you\'ve seen, or something else? A few words is enough.',
    '"Most often" compares how often people say things, so a reader may wonder whose words they are.',
    'If it\'s what people have told you, it stays as it is. If you\'re not sure, I\'d make it "What people often say helped", which claims only what you\'ve seen.',
    'the point-of-view read, 2.4; GPT\'s review: ask what it is based on')
ask('Q2', 'A lot of people find that a mantra they feel some heart connection to',
    'Gentle Meditation and Mantra: "A lot of people find"',
    'What is "A lot of people find" based on? If the mantra does something for you that a reader should know, one line of it is welcome too, and it\'s optional.',
    'It says how many people find it, and your "I personally love…" right after it is about the mantra you like.',
    'If it\'s what you\'ve seen or been told, it stays as it is.',
    'the point-of-view read, 5.8; GPT\'s review: ask its basis, a personal line optional')
ask('Q3', 'Some people find that deep grieving gives way to warmth, or to feeling connected.',
    'Somatic Heart Opening: "Some people find"',
    'Where do "Some people find" and "Some feel held, in the body" come from: your own experience, people you\'ve worked with, a source, or something else? An example is optional.',
    'They\'re the reason to stay with grief at all, so a reader may wonder whose experience they are.',
    'If it\'s yours or people you know, it stays as it is.',
    'the point-of-view read, 7.4; GPT\'s review: ask its basis')

sha = hashlib.sha256(MD.encode('utf-8')).hexdigest()
review = {
    'format': sr.FORMAT, 'review_id': 'inner-child-t110-agreed', 'title': 'Inner Child Review Sheet',
    'intro': [
        'Only the changes GPT\'s review and mine both recommend, each in place in the whole guide: two sections in a new '
        'order, ten cuts, three small wording changes and three questions. The agreement card by card, with GPT\'s advice, is '
        '<a href="%st110-review/AGREED.md" target="_blank" rel="noopener noreferrer">here</a>. Everything else on the turn-109 '
        'sheet, both of us would leave as it is.' % EXP,
        'Approve, Reject or Revise each change, and answer the questions in their boxes. Your answers save in this browser as '
        'you click. When you\'re done, press "Save / send", then "Copy my answers", and paste them into the chat from either account.',
        'Nothing in the guide changes until you approve. The two sections read Human in Pangram as they\'d read, and the cuts '
        'and wording changes get their checks once you approve them.',
    ],
    'git_file': 'articles/inner-child-therapy/experiments/t110-review/REVIEW.html',
    'article': {'file': ARTICLE, 'sha256': sha},
    'built': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M UTC'),
    'links': {'guide': BLOB + ARTICLE, 'review': EXP + 't110-review/REVIEW.json'},
    'types': TYPES, 'suggestions': S,
}
probs = sr.check(review, BL)
assert not probs, probs
(HERE / 'REVIEW.json').write_text(json.dumps(review, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
html = sr.page(review, MD, BL)
(HERE / 'REVIEW.html').write_text(html, encoding='utf-8')
(HERE / 'REVIEW-artifact.html').write_text(sr.artifact_view(html), encoding='utf-8')
print('REVIEW.json, REVIEW.html and REVIEW-artifact.html:', len(S), 'cards,', len(html), 'bytes')
