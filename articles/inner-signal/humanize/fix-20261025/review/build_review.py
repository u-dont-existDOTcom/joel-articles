"""The hypnosis guide's review page: every suggestion of 2026-10-25, marked in the whole guide (REVIEW.json, REVIEW.html).

Joel, 2026-10-25 14:40 UTC (../joel-20261025-1440-message.txt): "why don't you give me the full HTML guide with
highlighting where you notice x,y,z type of problems (color-coded) and your suggestion for that and then my comment box on
your suggestion with approve reject reivse buttons etc". It replaces the four lists of his 01:01 request (questions 15 to
18: the reread, the reader's edit, the caveats, the repeats), with the reread run again on the fixed brief (his 15.1:
"your reader is not a good reader"), the inner child alignment ("make sure we line up all the inner child work with the
latest inner child guide") and the typos my check found.

Every suggestion is my check of a reader's item against the whole guide, his rules (the clarity brief's; "never take out
something important"), his earlier answers and the InnerSignal protocol (version 0.2.1, protocol_sha256
1da3ddf06a27aa8409fe953f21e8d9053d943bf383c04d5c561e2e93bb067a27, loaded this turn), or one of mine. The tables say for each
reader's item whether I offer it (advice "approve"), show it as one a reader flagged that I'd leave as it is ("leave"), or
fold it into another suggestion ("dup"). An edit is (anchor, old, new): in the paragraph holding ANCHOR, OLD becomes NEW
("" cuts it, tidied like clarity_read.cut_text; None removes the paragraph), so the page shows exactly what changes.

  python3 articles/inner-signal/humanize/fix-20261025/review/build_review.py      # writes REVIEW.json and REVIEW.html
"""
import datetime
import hashlib
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
FIX = HERE.parent
ROOT = HERE.parents[4]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
sys.path.insert(0, str(FIX))
import clarity_read as cr  # noqa: E402
import suggestion_review as sr  # noqa: E402
import my_checks  # noqa: E402

ARTICLE = 'articles/inner-signal/humanize/HUMANIZED-SO-FAR.md'
GIT_FILE = 'articles/inner-signal/humanize/fix-20261025/review/REVIEW.html'
BLOB = 'https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/community-joel-1018/'
MD = (ROOT / ARTICLE).read_text(encoding='utf-8')
BL = sr.blocks(MD)

TYPES = {
    'reread': {'label': 'A reader would stop', 'about': 'A passage a first-time reader would have to read twice: the reread on the fixed brief, and the first reread where it still holds.'},
    'structure': {'label': 'Headings and order', 'about': 'A new heading, a move, a line that repeats its heading, a paragraph break: the reader\'s edit.'},
    'caveat': {'label': 'Caveats', 'about': 'A safety line, disclaimer, reassurance or takeback a reader doesn\'t need where it is.'},
    'repeat': {'label': 'Said already', 'about': 'Something the guide has already said.'},
    'innerchild': {'label': 'Inner child guide', 'about': 'Where the guide differs from your latest inner child guide, lined up with its decided words.'},
    'typo': {'label': 'Typos', 'about': 'A typo, a missing word, a space before a full stop.'},
}

S = []


def where_q(quote):
    """The block holding QUOTE; "#Text" is the heading whose text is exactly Text."""
    if quote.startswith('#'):
        hits = [b['i'] for b in BL if b['level'] and b['text'] == quote[1:]]
        if len(hits) != 1:
            raise ValueError('heading %r is in the guide %d times' % (quote[1:], len(hits)))
        return hits[0], 0, len(BL[hits[0]]['text'])
    return sr.find_quote(BL, quote)


def changed(old, new):
    """(start, end) in OLD of the words that change into NEW; a pure addition gives the sentence it follows."""
    a = 0
    while a < min(len(old), len(new)) and old[a] == new[a]:
        a += 1
    z = 0
    while z < min(len(old), len(new)) - a and old[len(old) - 1 - z] == new[len(new) - 1 - z]:
        z += 1
    s, e = a, len(old) - z
    while s > 0 and old[s - 1].isalnum():
        s -= 1
    while e < len(old) and old[e].isalnum():
        e += 1
    if e <= s:
        cut = max(old.rfind('. ', 0, s), old.rfind('? ', 0, s), old.rfind('! ', 0, s))
        s, e = (cut + 2 if cut >= 0 else 0), len(old.rstrip())
        if s >= e:
            s, e = 0, len(old)
    return s, e


def add(sid, typ, title, advice, edits=(), inserts=(), moves=(), why='', stays='', what=None, deciding=None, note='',
        found_by='', approve_label=None, decided=None, warning=None, spans=None):
    by_block, out_spans, first = {}, [], {}
    for anchor, old, new in edits:
        i = anchor if isinstance(anchor, int) else where_q(anchor)[0]
        orig = BL[i]['text']
        cur = by_block.get(i, orig)
        if new is None:
            by_block[i] = ''
            out_spans.append({'block': i, 'start': 0, 'end': len(orig)})
            continue
        old = locate(sid, cur, old)
        new = match_style(new, orig) if new else new
        k = cur.index(old)
        by_block[i] = sr.cut_text(cur, k, k + len(old)) if new == '' else cur[:k] + new + cur[k + len(old):]
        o = orig.find(old)
        if o >= 0 and orig.count(old) == 1:
            if new == '':
                out_spans.append({'block': i, 'start': o, 'end': o + len(old)})
            else:
                cs, ce = changed(old, new)
                out_spans.append({'block': i, 'start': o + cs, 'end': o + ce})
    out_edits = [{'block': i, 'before': BL[i]['text'], 'after': after} for i, after in by_block.items()]
    out_ins = [{'before': len(BL) if a is None else where_q(a)[0], 'kind': kind, 'text': text, 'seq': seq}
               for a, kind, text, seq in inserts]
    out_mv = [{'blocks': [where_q(a)[0] for a in anchors], 'before': len(BL) if b is None else where_q(b)[0], 'seq': seq}
              for anchors, b, seq in moves]
    s = {'id': sid, 'type': typ, 'title': title, 'advice': advice, 'spans': spans if spans is not None else out_spans,
         'edits': out_edits, 'inserts': out_ins, 'moves': out_mv, 'why': clean(why),
         'stays': clean(stays) or 'Everything else in the paragraph, word for word.', 'advice_note': clean(note),
         'found_by': found_by}
    s['what'] = what or describe(edits, out_ins, out_mv)
    s['deciding'] = deciding or default_deciding(s)
    if approve_label:
        s['approve_label'] = approve_label
    if decided:
        s['decided'] = decided
    links = sorted({t for sp in s['spans'] for t in sr.links_in(BL, sp['block'], sp['start'], sp['end'])})
    if warning:
        s['warning'] = warning
    elif links and any(new in ('', None) for _, _, new in edits):
        s['warning'] = 'The words it cuts carry a link (%s): say where the link should go if you approve.' % ', '.join(links)
    S.append(s)
    return s


def locate(sid, text, old):
    """OLD as it is in TEXT: exactly, or with only quote marks, dashes and spaces differing (my tables are typed)."""
    if text.count(old) == 1:
        return old
    if text.count(old) > 1:
        raise ValueError('%s: %r is in its paragraph %d times' % (sid, old, text.count(old)))
    nt, idx = sr.norm_map(text)
    no = sr.norm_map(old)[0]
    if nt.count(no) != 1:
        raise ValueError('%s: %r is not in its paragraph once' % (sid, old))
    k = nt.index(no)
    return text[idx[k]:idx[k + len(no) - 1] + 1]


def match_style(new, para):
    """NEW with the paragraph's own apostrophes and quote marks."""
    if '’' in para and "'" not in para:
        new = re.sub(r"(?<=\w)'(?=\w)", '’', new)
    if ('“' in para or '”' in para) and '"' not in para:
        out, opened = [], False
        for ch in new:
            if ch == '"':
                out.append('”' if opened else '“')
                opened = not opened
            else:
                out.append(ch)
        new = ''.join(out)
    return new


def clean(t):
    return re.sub(r'\s+', ' ', (t or '')).strip()


def short(t, n=16):
    w = t.split()
    return ' '.join(w[:n]) + (' …' if len(w) > n else '')


def describe(edits, inserts, moves):
    out = []
    for anchor, old, new in edits:
        if new is None:
            out.append('Cuts the paragraph "%s".' % short(BL[anchor if isinstance(anchor, int) else where_q(anchor)[0]]['text'], 12))
        elif new == '':
            out.append('Cuts "%s".' % short(old, 30))
        elif new.startswith(old):
            out.append('Adds, after "%s": "%s"' % (short(old.split('. ')[-1], 10), short(new[len(old):].strip(), 30)))
        elif len(old) <= 150 and len(new) <= 170:
            out.append('"%s" becomes "%s".' % (old, new))
        else:
            out.append('Rewrites "%s", as shown below.' % short(old, 12))
    for ins in inserts:
        to = ('above ' + sr.where(BL, ins['before'])) if ins['before'] < len(BL) else 'at the end'
        out.append('Adds the %s "%s" %s.' % (sr.KIND_NAMES[ins['kind']], ins['text'], to))
    for mv in moves:
        to = mv['before']
        out.append('Moves %s to just before %s.' % (sr.where(BL, mv['blocks'][0]),
                                                    sr.where(BL, to) if to < len(BL) else 'the end'))
    return ' '.join(out)


def default_deciding(s):
    if s['type'] == 'structure':
        return 'Approve makes this change; Reject leaves it as it is.'
    if s['moves'] and not s['edits']:
        return 'Approve moves it there; Reject leaves it where it is.'
    if s['inserts'] and not s['edits'] and not s['moves']:
        return 'Approve adds it; Reject leaves the section as it is.'
    if s['type'] in ('caveat', 'repeat'):
        return 'Approve cuts it; Reject keeps it as it is.'
    return 'Approve uses the new wording; Reject keeps yours as it is; Revise lets you write your own.'


# ======================================================================= the reread on the fixed brief (clarity2)
# key: (status, edits or None for the reader's own quote -> plain, title, my note). A "leave" or "dup" note says why.
RR = {
    '1.1': ('decided', [('because without the rupture in your thought stream,', 'because without the rupture in your thought stream,',
                         'because without redirecting the thought stream with your conscious, higher intention,')],
            'Your wording for the rupture sentence',
            'Your fix of 14:40, word for word. You said "do that" is clear from the words right before it, so it stays; the reader\'s two brackets are gone.'),
    '1.2': ('approve', [('you may not notice feelings before words', 'you may not notice feelings before words', 'you won\'t notice feelings before words')],
            'End a double negative', 'The smallest change that ends "doesn\'t mean ... may not notice"; the reader rewrote the whole sentence.'),
    '1.3': ('leave', None, '', 'You guide yourself through the practice, so the invitations are yours to vary; I\'d leave your wording.'),
    '1.4': ('leave', None, '', 'Your phrase, and it reads on a first pass.'),
    '1.5': ('leave', None, '', 'Your word, and the sentence is clear without unpacking it.'),
    '2.1': ('approve', [('It might not be chronological age.', 'It might not be chronological age.', 'Their age might not be your chronological age.')],
            'Say whose age', 'Names what "It" is and keeps your sentence. Your published guide put it as "Don\'t decide from the person\'s chronological age"; the inner child guide dropped the sentence. If you meant something else, Revise.'),
    '2.2': ('approve', [('to the caretaker in the other person', 'to the caretaker in the other person', 'to the caretaker in another person')],
            'Another person, not "the other person"', 'No other person has come up yet, so "the other person" makes a reader look back for one; "another person" is the smallest change.'),
    '2.3': ('approve', [('how valuable is it to consider how valuable it might have been for them to do what they did at the time',
                         'how valuable is it to consider how valuable it might have been for them to do what they did at the time',
                         'how valuable is it to consider what their actions did for them at the time')],
            'One "how valuable", not two', '"Their actions" is the words the paragraph uses two questions later. IC-A9 (the inner child guide\'s six questions) would replace this whole paragraph; if you approve that, this one falls away.'),
    '2.4': ('leave', None, '', 'A short formula in your style; the next lines explain each one.'),
    '2.5': ('approve', [('often warming up and protecting yourself', 'often warming up and protecting yourself', 'often being warm to yourself, protecting yourself')],
            '"Warming up" reads as getting ready', 'Warmth is the Nurturer\'s job in your inner child guide; "warming up" reads as preparing. I left the "So" that follows.'),
    '2.6': ('leave', None, '', 'Trust that can question your promises is your image, from your published guide ("Trust can question your promises"). Only the "it\'s" is a typo (TY-2).'),
    '2.7': ('approve', [('Don\'t make it so that doing it successfully is having to feel good about it, or being able to check it off a list.',
                         'Don\'t make it so that doing it successfully is having to feel good about it, or being able to check it off a list.',
                         'Don\'t make it so that doing it successfully means you have to feel good about it, or be able to check it off a list.')],
            'Untangle "is having to feel good"', 'Keeps your "Don\'t make it so that"; the reader rewrote it as "Don\'t make your success depend on".'),
    '3.1': ('leave', None, '', '"This" points to "One way of explaining this", two sentences before, so a reader gets it.'),
    '3.2': ('leave', None, '', 'You write your own scripts in this guide, so "you" fits both the hypnotist and the reader; the reader\'s version made it only a hypnotist.'),
    '3.3': ('approve', [('whatever the subject says, shows that', 'whatever the subject says, shows that', 'whatever the subject says shows that')],
            'One comma', 'The comma splits the subject from its verb; taking it out is enough.'),
    '3.4': ('approve', None, 'The last sign in the list', 'The list ends as a list: "an excessive sense of certainty ..., and a sense that one good question will break the spell."'),
    '3.5': ('leave', None, '', 'The contrast is the point (specific aim, vague wording), and the next sentence says it.'),
    '3.6': ('leave', None, '', 'Long, but each part is needed; the reader\'s version cut "what it means to have".'),
    '3.7': ('approve', [('are where you have consented to something you didn’t realize, or you being given only one choice, or something not yet agreed upon is embedded in a sentence.',
                         'are where you have consented to something you didn’t realize, or you being given only one choice, or something not yet agreed upon is embedded in a sentence.',
                         'are where you have consented to something without realizing it, where you are given only one choice, or where something not yet agreed upon is embedded in a sentence.')],
            'Three tricks, said the same way', 'Keeps your "where" and gives each trick the same shape; "consented to something you didn\'t realize" becomes "without realizing it".'),
    '3.8': ('leave', None, '', 'A method without trance; "No-trance inner contact" later says the same.'),
    '3.9': ('approve', [('You are in this camp if:', 'You are in this camp if:', 'You are in the first camp if:')],
            'Which camp', 'Right after "For others, it is very easy", "this camp" reads as the easy group, though the list describes the other one.'),
    '4.1': ('approve', None, 'Quote marks on the words to say', 'Your published guide had the three words in quote marks; "or say "quiet"" adds the missing verb.'),
    '4.2': ('approve', [('is not the same as your go inward to hypnosis one.', 'is not the same as your go inward to hypnosis one.', 'is not the same as your cue to go inward to hypnosis.')],
            '"Your go inward to hypnosis one"', 'The smallest change; ST-5.1 moves this paragraph after the one that sets up the cue.'),
    '4.3': ('leave', None, '', '"What you\'ve got" is whatever you\'re left with once you stop moving; the script right after shows it.'),
    '4.4': ('approve', [('No will stay no.', 'No will stay no.', 'A no will stay a no.')],
            '"No will stay no"', '"No will" first reads as one noun. The reader also explained "the narrator" in brackets; you\'re reading the script yourself here, so I left that out.'),
    '4.5': ('approve', [('or something to anchor yourself and the thing you will say to open it up.', 'or something to anchor yourself and the thing you will say to open it up.',
                         'or something to anchor yourself, and choose the thing you will say to open it up.')],
            'Two choices, not one list', 'The phrase you\'ll say is a second choice; ", and choose" says so and keeps your order.'),
    '4.6': ('approve', [('(The later part of this can be used', '(The later part of this can be used', '(The part below called "Already open? Contain before you deepen" can be used'),
                        ('skip straight to the orientation/containment part rather than going deeper', 'skip straight to the orientation/containment part rather than going deeper',
                         'skip straight to "Already open? Contain before you deepen" rather than going deeper')],
            'Name the section the two safety notes point to', 'Both safety notes send a reader to a part they can\'t find yet; the first reread flagged the second one (its 2.8).'),
    '4.7': ('leave', None, '', 'The section is about writing your own induction, so "writing this" is clear.'),
    '5.1': ('leave', None, '', 'Compressed, but the heading carries it; guessing the referents would risk changing what you mean.'),
    '5.2': ('leave', None, '', 'This is the section about thinking in words, so "in your head" means in words.'),
    '5.3': ('leave', None, '', '"It" is the job named right before ("the one whose job you need").'),
    '5.4': ('approve', [('at the end of it, however if you are coming out of a recording then you should not leave yourself in an altered state, this includes',
                         'at the end of it, however if you are coming out of a recording then you should not leave yourself in an altered state, this includes',
                         'at the end of it. However, if you are coming out of a recording then you should not leave yourself in an altered state. This includes')],
            'A safety note in three sentences', 'Full stops only, no words changed.'),
    '5.5': ('approve', [('are now finished, the only intention I will take with me into my everyday life or the only cue I will use to take me into this state at a later date will be the one I consciously choose to and neither',
                         'are now finished, the only intention I will take with me into my everyday life or the only cue I will use to take me into this state at a later date will be the one I consciously choose to and neither',
                         'are now finished. The only intention I will take with me into my everyday life, and the only cue I will use to take me into this state at a later date, will be the ones I consciously choose, and neither')],
            'The return line, read aloud', 'It\'s read aloud at the end of a session, so it has to parse first time; the dangling "choose to" goes.'),
    '5.6': ('approve', None, 'The three steps first', 'The steps (induce, practice, come out) come together, and the five-minutes sentence follows; no words cut.'),
    '5.7': ('approve', [('Read through these, and then', 'Read through these, and then', 'Read through these sections, and then')],
            '"These" what', 'One word, under a heading with six sections below it.'),
    '5.8': ('approve', [('When you start to contact it, if it feels too much', 'When you start to contact it, if it feels too much', 'When you start to contact the difficult thing, if it feels too much')],
            'The first "it" under the heading', 'Nothing before it says what "it" is; the next sentence calls it "the difficult thing".'),
    '5.9': ('leave', None, '', 'The paragraph before is about the image and the voice; "the metaphor" reads as that.'),
    '6.1': ('approve', [('You probably don\'t need any more support than this: If you keep the practice shorter',
                         'You probably don\'t need any more support than this: If you keep the practice shorter',
                         'You probably don\'t need any more support than this if you keep the practice shorter'),
                        ('for a week or two, and if you notice', 'for a week or two, and if you notice', 'for a week or two. If you notice')],
            'A 100-word sentence in two', 'The conditions then belong to the first sentence, and the warning gets its own; the reader\'s version added "guide gives you".'),
    '6.2': ('approve', [('that you’re there for your Little parts and that you recognize that your protector parts are trying to protect you and that you don’t need',
                         'that you’re there for your Little parts and that you recognize that your protector parts are trying to protect you and that you don’t need',
                         'that you’re there for your Little parts, that you recognize that your protector parts are trying to protect you, and that you don’t need')],
            'Three things to say, with commas', 'Commas only. IC-B7 changes the names in the same sentence.'),
    '6.3': ('leave', None, '', 'Under the heading "It feels fake", "it" is the fake feeling.'),
    '6.4': ('approve', None, 'A reason, not a rule', '"Skip ... just because" stops "because you can force them down" reading as a reason to skip medical attention.'),
    '6.5': ('approve', None, '"Observing ego"', 'A clinical term most readers don\'t know; "observe yourself" says it.'),
    '6.6': ('leave', None, '', 'A clipped instruction in your style; it reads.'),
    '6.7': ('leave', None, '', 'What your subconscious isn\'t saying yet, from the section\'s heading.'),
    '7.1': ('dup', 'ST-8.1', '', 'ST-8.1 cuts these two sentences instead: your 3 a of 21 October dropped the examples they refer to.'),
    '7.2': ('leave', None, '', 'The example right before shows each move; the reader\'s version added a gloss to each.'),
    '7.3': ('approve', [('Listen to it for as long as it takes', 'Listen to it for as long as it takes', 'Listen to the kid for as long as it takes')],
            'Who "it" is in the Closing', 'Nothing before it says who "it" is; the next sentence calls them "the kid". IC alignment didn\'t touch this.'),
    '7.4': ('approve', None, 'What a conversational postulate is', 'One bracket for a term a reader can\'t know, as your rule allows; Reject if the example says enough.'),
    '7.5': ('approve', None, '"The sub"', '"The sub" reads as submissive or submarine; it opens the Closing.'),
    '7.6': ('leave', None, '', '"Container" is your word ("Contain before you deepen").'),
    '7.7': ('approve', [('how wide and narrow a range', 'how wide and narrow a range', 'how wide or narrow a range')],
            '"Wide and narrow"', 'One word; the reader also added "of feelings", which the sentence before already implies.'),
    '7.8': ('approve', [('The NLP can help you', 'The NLP can help you', 'The NLP in Appendix B can help you')],
            '"The NLP"', 'After a paragraph about prompts, "NLP" reads as natural language processing; NLP is spelled out at the start of Appendix B.'),
    '7.9': ('leave', None, '', '"It" is the change the pattern invites.'),
    '8.1': ('leave', None, '', 'A checklist line from your published guide; the answer is yours during a session.'),
    '8.2': ('approve', [('We do this on purpose when we rehearse what to do when we notice a synchronicity (we create an association in our head)',
                         'We do this on purpose when we rehearse what to do when we notice a synchronicity (we create an association in our head)',
                         'We create an association in our head on purpose when we rehearse what to do when we notice a synchronicity')],
            '"We do this on purpose"', 'Right after "false positives", "We do this on purpose" reads as making false positives on purpose; the bracket says what "this" is, so it goes in its place.'),
    '8.3': ('approve', None, 'A reason, not an admission', '"(I create urgency for them)" reads as if you do.'),
    '8.4': ('approve', [('You must be the one authoring these.', 'You must be the one authoring these.', 'You must be the one authoring these cues.')],
            '"These" after "caveats"', 'Right after "Mind the caveats!", "these" reads as the caveats.'),
    '8.5': ('approve', [('Feel something that you have got to in reality', 'Feel something that you have got to in reality', 'Feel a state that you have got to in reality')],
            'Feel what', 'One word; the reader rewrote the paragraph.'),
    '8.6': ('approve', [('a "Swish Pattern", but I will', 'a "Swish Pattern", but I will', 'a "Swish Pattern" (it swaps a picture of an old reaction for a picture of a new one), but I will')],
            'What a Swish Pattern is', 'One bracket for a term a reader can\'t know; it also shows what your variation changes.'),
    '8.7': ('leave', None, '', 'A checklist line from your published guide.'),
    '8.8': ('approve', [('Stop-orient-go wider-reality check-listen-do at least one thing from a loving place.',
                         'Stop-orient-go wider-reality check-listen-do at least one thing from a loving place.',
                         'Stop, orient, go wider, reality check, listen, do at least one thing from a loving place.')],
            'Six steps, with commas', 'The hyphens also sit inside "go wider" and "reality check". ST-8.2 moves this line up; the commas go with it.'),
    '8.9': ('leave', None, '', '"What would this felt sense like me to know?" is grammatical (what would it like me to know), and it\'s your published wording.'),
    '8.10': ('leave', None, '', 'It\'s a link to Gollwitzer\'s paper, and the If-then sections explain it later.'),
    '8.11': ('leave', None, '', 'The sentence explains the term itself ("patterns that were not really there").'),
    '9.1': ('approve', [('there is a difference between you having experienced it at one point, and only being able to access it in a certain state, compared to being able to get to it at any point in your life.',
                         'there is a difference between you having experienced it at one point, and only being able to access it in a certain state, compared to being able to get to it at any point in your life.',
                         'there is a difference between having experienced it at one point, or only being able to access it in a certain state, and being able to get to it at any point in your life.')],
            '"Between ... and ... compared to"', 'Only this sentence; "give it to the child" stays, since "that experience" is right before it.'),
    '9.2': ('approve', [('what the things they did meant', 'what the things they did meant', 'what the things the person did meant')],
            'Who "they" are', 'With "the person", "They" in the next sentence is clearly whoever you ask.'),
    '9.3': ('approve', None, '"Do it" before it\'s named', 'Under the heading, "do it" reads as self-hypnosis; IC-B19 adds to the same paragraph.'),
    '9.4': ('approve', [('This doesn’t negate that harm was caused, holding someone accountable', 'This doesn’t negate that harm was caused, holding someone accountable',
                         'This doesn’t negate that harm was caused, and it doesn’t stop you from holding someone accountable')],
            'What it doesn\'t negate', 'Only the second sentence; "accumulated nature" is your published wording.'),
    '9.5': ('approve', None, 'Three "may"s', 'The state and what you experience in it stop blurring; nothing cut.'),
    '9.6': ('approve', [('if they told you in advance.', 'if they told you in advance.', 'and whether they told you in advance.')],
            'A question, not a condition', '"If they told you" reads as a condition on asking.'),
    '10.1': ('leave', None, '', '"The autonomous" is the "Autonomous" step two lines before.'),
    '10.2': ('approve', [('Goal is to make it "good as you", not to erase history.', 'Goal is to make it "good as you", not to erase history.',
                          'Goal is to make it "good as you" rather than "good as new", not to erase history.')],
             'The pun on "good as new"', 'Your published guide spelled it out: "The goal isn’t “good as new,” as though history should disappear. Aim for good as you."'),
    '10.3': ('approve', [('leaving the "person" behind', 'leaving the "person" behind', 'leaving the imagined "person" behind')],
             'Which "person"', 'The only person in the exercise is the you you imagine with 1% more of the quality.'),
    '10.4': ('leave', None, '', 'The first sentence gives the strands ("a few different strands to one thing").'),
    '10.5': ('approve', [('Try to avoid any language that makes you not one person.', 'Try to avoid any language that makes you not one person.',
                          'Try to avoid any language that makes you feel you\'re not one person.')],
             'Language that divides you', 'Your published guide: "If parts language makes you feel more divided"; the reader\'s version said "more than one person".'),
    '10.6': ('approve', [('or just keep it at the same level, just enough weight/pressure.', 'or just keep it at the same level, just enough weight/pressure.',
                          'or you can just keep it at the same level, with just enough weight/pressure.')],
             'The second half of the floating sentence', '"It" is the contact named right before, so only the grammar changes.'),
    '10.7': ('leave', None, '', '"The first beat" follows "then stop saying it".'),
    '10.8': ('leave', None, '', 'A contact like "No-trance inner contact" at the end of the library; ST-11.2 also splits this paragraph.'),
    '10.9': ('approve', [('not because they are necessarily validating the validity of some aspects of NLP', 'not because they are necessarily validating the validity of some aspects of NLP',
                          'not because they necessarily validate some aspects of NLP')],
             '"Validating the validity"', 'The smallest change; the reader split the sentence in three.'),
    '10.10': ('leave', None, '', 'It reads: whichever helps, that doesn\'t say what it is.'),
}

# The first reread (01:01) items the second missed and that still hold, with the smallest change; the rest of the first
# reread's 64 were glosses, his own words or already elsewhere on this page.
RO = [
    ('RO-2.7', 'and that that is not a positive change', 'and that no change is not a positive change', '"That that"',
     'The second "that" is the "no change"; the first reread flagged it.',
     'The double "that" makes a reader go back to see what isn\'t a positive change.'),
    ('RO-3.12', 'Don\'t use it in a way that you are going to follow instructions', 'Don\'t use it in a way that makes you follow instructions',
     '"In a way that you are going to follow"', 'The smallest change; the first reread flagged it.',
     '"In a way that you are going to follow instructions" is knotted: a reader has to rebuild it as "in a way that makes you follow".'),
    ('RO-6.12', 'haven\'t slept, etc, etc, etc around plant medicine)', 'haven\'t slept, are around plant medicine, etc, etc, etc)',
     '"Around plant medicine" hangs', 'Your published guide had "or other plant-medicine-adjacent states"; this keeps your words in the list.',
     'After "etc, etc, etc", "around plant medicine" has nothing to attach to.'),
]

TYPOS = [
    ('TY-1', [('led astray but your random wrong thoughts', 'led astray but your random wrong thoughts', 'led astray by your random wrong thoughts')],
     '"Led astray but"', 'In the paragraph of your 15.1.'),
    ('TY-2', [('and take it\'s time.', 'and take it\'s time.', 'and take its time.')], '"Take it\'s time"', 'Your published guide had "its".'),
    ('TY-3', [('and mind you deeper mind is still running', 'and mind you deeper mind is still running', 'and mind you, the deeper mind is still running')],
     '"Mind you deeper mind"', 'A missing comma and "the"; the first reread flagged it.'),
    ('TY-4', [('so you’re more familiar with it.', 'so you’re more familiar with it.', 'so you’re more familiar with them.')],
     'Two things, "them"', 'The induction and the full return.'),
    ('TY-5', [('As long as you\'re reality testing is good', 'As long as you\'re reality testing is good', 'As long as your reality testing is good')],
     '"You\'re reality testing"', ''),
]


def space_typos():
    """A space before a full stop or comma after a link or a label (the Substack paste leaves one): one edit each."""
    edits = []
    for b in BL:
        if b['level'] or b['native']:
            continue
        for m in re.finditer(r'(\w) ([.,])(?!\.)', b['text']):
            ctx = b['text'][max(0, m.start() - 25):m.end()]
            if b['text'].count(ctx) != 1:
                continue
            edits.append((b['i'], ctx, ctx[:-2] + ctx[-1]))
    return edits


# ======================================================================= the reader's edit (structure), exact operations
def heading(anchor, kind, text, seq=0):
    return (anchor, kind, text, seq)


ST_OPS = {
    '1.1': dict(inserts=[heading('Under no circumstances allow a strong state', 'h1', 'Keep the Adult Part of Yourself in Charge')]),
    '1.2': dict(inserts=[heading('The Mayo Clinic warns that using hypnosis', 'h1', 'What to Use Self-Hypnosis For, and What Not To')]),
    '1.3': dict(inserts=[heading('Let’s elicit a high level of co-operation', 'h1', 'Co-operation Between the Modes')]),
    '2.1': dict(inserts=[heading('I found that especially amplified with loveyhuasca.', 'h1', 'What amplified it, and what lasted')]),
    '2.2': dict(inserts=[heading('It can be helpful to use borrowing when you’re in the adult position', 'h3', 'Borrowing when you don’t know what a decent adult would do')]),
    '2.4': dict(inserts=[heading('Be aware of what you are teaching your other positions.', 'h2', 'Instead of blame'),
                         heading('#The two-hand practice', 'h1', 'Working with your inner child')],
                edits=[('WORKING WITH YOUR INNER CHILD:', 'WORKING WITH YOUR INNER CHILD:', None)]),
    '3.1': dict(edits=[('The Guide:', 'The Guide:', None), ('Working with childhood protector parts:', 'Working with childhood protector parts:', None)]),
    '3.2': dict(inserts=[heading('#Protection that knows when to stop scanning', 'h2', 'Your inherited parent script', 1)],
                moves=[(['One important thing to become aware of when approaching your inner child is your inherited parent script.'], '#Protection that knows when to stop scanning', 2)]),
    '3.3': dict(inserts=[heading('When you are a child you feel that you need to belong to the family in order to survive.', 'h2', 'Belonging without betraying yourself')]),
    '4.1': dict(inserts=[heading('First of all, if you sense you are being hypnotically influenced, stop.', 'h2', 'If you sense you are being influenced')]),
    '4.2': dict(inserts=[heading('You can allow your eyes to rest on something in the room for a bit', 'p', 'Script:')]),
    '4.3': dict(inserts=[heading('If being still tends to make you sleepy', 'h3', 'Make the hypnosis more active')]),
    '5.1': dict(moves=[(['Ex: My dad used to use a mudra'], 'When you pick the time and place (it needs to be an appropriate time and place)', 0)]),
    '5.2': dict(inserts=[heading('If you want to turn this one off, simply don\'t practice it anymore.', 'h3', 'Turning the shortcut off, or keeping it')]),
    '5.3': dict(inserts=[heading('It\'s worth trying to separate the notice, the meaning, and your thoughts on the meaning', 'h3', 'Notice, meaning, and your thoughts on the meaning')]),
    '6.1': dict(inserts=[heading('If you feel an urge to move, turn, reach, push', 'h3', 'If you feel an urge to move')]),
    '6.2': dict(moves=[(['When you have finished, even if you stopped part way through'], 'Note : throughout the exercise', 1)],
                inserts=[heading('Note : throughout the exercise', 'h3', 'Throughout the exercise', 2)]),
    '6.3': dict(edits=[('Being able to guide yourself does not mean you have to!', 'Being able to guide yourself does not mean you have to!', '')]),
    '6.4': dict(edits=[('If you can’t, just work with what you are aware of.', 'If you can’t, just work with what you are aware of.', '')]),
    '7.1': dict(moves=[(['You should seek suitable ongoing help if:'], 'You probably don\'t need any more support than this', 0)]),
    '7.2': dict(inserts=[heading('Always keep in mind that your functioning in ordinary life is the feedback.', 'h2', 'Your functioning in ordinary life is the feedback')]),
    '7.3': dict(moves=[(['Always enter this app via this page'], 'If you’re using the ChatGPT version of this app', 0)]),
    '7.4': dict(inserts=[heading('Please fill in this survey with what you’ve learned', 'h2', 'Survey and consultation')]),
    '8.1': dict(edits=[('Be very careful here. Bridge words are words like', 'it doesn’t mean that it’s true if it isn’t!',
                        'it doesn’t mean that it’s true if it isn’t! It’s not very likely that just by breathing in and out that your trauma is going to go away!'),
                       ('In general, the problem with the first example is that it’s too strong.', 'In general, the problem with the first example is that it’s too strong.', None)]),
    '8.2': dict(edits=[('It is my cue to:', 'It is my cue to:', 'It is my cue to: Stop-orient-go wider-reality check-listen-do at least one thing from a loving place.'),
                       ('In other words: Stop-orient-go wider', 'In other words: Stop-orient-go wider', None)]),
    '8.3': dict(inserts=[heading('A downside of synchronicity cues is that they can lead to false positives.', 'h4', 'False positives, and turning the cue off')]),
    '9.1': dict(moves=[(['Here is a rough outline of the entire NLP process :'], 'Induce/Contain the person (get their attention', 0)]),
    '9.2': dict(moves=[(['Inner child love', 'Here is some inner child love.'], 'A script you could use for anxiety is:', 0)],
                edits=[('Then work on your reduced breathing', 'Then work on your reduced breathing', 'Work on your reduced breathing')]),
    '9.4': dict(moves=[(['A script you could use for anxiety is:'], 'Where are my body parts? What are my feet doing?', 0)]),
    '10.1': dict(inserts=[heading('For self-forgiveness, name what you did, but don\'t take responsibility', 'h2', 'Forgiving yourself')]),
    '11.1': dict(inserts=[heading('The General Rule is: if you find that what you\'re doing is making you more loving', 'h3', 'The General Rule')]),
    '11.2': dict(edits=[('Once you start an induction, you will want to notice', ' Once you start an induction, you will want to notice', '\n\nOnce you start an induction, you will want to notice')]),
    '11.3': dict(edits=[('Learning to learn, how to get in and out', 'Learning to learn, how to get in and out', None)]),
}


def q_or_ref(text):
    """A {Q:KEY} cross-reference in my 01:01 notes, as this page's suggestion id."""
    return re.sub(r'\{(\d+):(\d+\.\d+)\}', lambda m: {'15': 'RO', '16': 'ST', '17': 'CV', '18': 'RP'}[m.group(1)] + '-' + m.group(2), text)


def load_items(name):
    return json.loads((FIX / name / 'ITEMS.json').read_text(encoding='utf-8'))


def structure():
    items = {x['key']: x for x in load_items('edit')}
    for key, (status, pick, note) in my_checks.EDIT.items():
        if status != 'keep':
            continue
        it, ops = items[key], ST_OPS[key]
        edits = list(ops.get('edits', []))
        inserts = list(ops.get('inserts', []))
        add('ST-' + key, 'structure', {'HEADING': 'A new heading', 'MOVE': 'A move', 'CUT-REPEAT': 'A line that says it again',
                                       'LABEL': 'A label', 'CUT-LAST-LINE': 'Two sentences that point at nothing'}[it['move']]
            if key != '11.2' else 'A paragraph break',
            'approve' if pick == 'A' else 'leave', edits=edits, inserts=inserts, moves=ops.get('moves', []),
            what=it['change'], why=it['why'], stays=it['keeps'], note=q_or_ref(note),
            found_by='The reader\'s edit (Sonnet), 01:01 read, part %d' % it['part'])


# ======================================================================= the caveats and the repeats
def cuts(name, typ, table, prefix):
    for x in load_items(name):
        if x['key'] not in table:
            continue
        status, pick, note = table[x['key']]
        if status != 'keep':
            continue
        title = cr.KINDS.get(x['kind'], x['kind'].lower()).capitalize() if typ == 'caveat' else 'Said already'
        stays = ('A reader loses: ' + x['loses']) if x.get('loses') else ''
        if typ == 'repeat' and x.get('said_already'):
            stays = 'Said already: "%s". %s' % (x['said_already'], stays)
        add(prefix + x['key'], typ, title, 'approve' if pick == 'A' else 'leave',
            edits=[(x['quote'], x['quote'], '')], why=x['why'], stays=stays, note=q_or_ref(note),
            found_by='The %s read (Sonnet), 01:01, part %d' % ('caveats' if typ == 'caveat' else 'repeats', x['part']),
            approve_label='cut it')


# ======================================================================= the inner child alignment
IC_FIELDS = ['SECTION', 'QUOTE', 'IC', 'DIFFERS', 'PROPOSED', 'KEEPS', 'PRIORITY']
# key: (advice, proposed override or None, my note)
IC_CHECK = {
    'A1': ('approve', None, 'Your inner child guide now says the Higher Self has no specific wisdom. Other parts of this guide ask your universal heart for guidance (the core prompts); if you approve this, I\'ll check each against it.'),
    'A2': ('approve', None, 'CV-2.1 suggested cutting "but I don’t mean them as if there were really three people in you"; with this, keep that clause and reject CV-2.1, or the reverse.'),
    'A3': ('approve', None, ''),
    'A4': ('dup', 'IC-T1', 'IC-T1 changes all of this section\'s "him/her" and quoted "child" at once.'),
    'A5': ('approve', None, 'Your decided answer from the inner child guide (without its emoji).'),
    'A6': ('approve', None, 'If you approve IC-T1 too, the added words get "they" like the rest.'),
    'A7': ('approve', None, 'Your inner child guide softened this: not hitting back is enough to start being the adult, and trust takes warmth.'),
    'A8': ('approve', None, 'RR-2.1 rewords the last sentence of the same passage; they go together.'),
    'A9': ('approve', None, 'Your six questions replace the four "how valuable" questions (RR-2.3 falls away if you approve this). ST-2.4 puts your heading "Instead of blame" above this part.'),
    'A10': ('approve', None, ''),
    'A11': ('approve', None, ''),
    'A12': ('approve', None, ''),
    'A13': ('approve', None, 'The same caution would also go in the core prompts (IC-B11); I\'d put it here, where the Guide is taught.'),
    'A14': ('approve', None, ''),
    'A15': ('approve', None, ''),
    'A16': ('approve', None, 'The guide\'s own consent rule ("No will stay no") says the same at the start.'),
    'A17': ('approve', None, 'This changes the guide\'s advice: learn the inner child work in your ordinary state before bringing it into hypnosis. IC-B19 adds the same lines in Appendix G, where they\'re about substances; if you approve both, I\'ll keep the full words in one place and point to them from the other.'),
    'A18': ('approve', None, ''),
    'A19': ('approve', None, 'TY-5 fixes "you\'re reality testing" in the same sentence.'),
    'A20': ('approve', None, ''),
    'A21': ('approve', None, 'Your inner child guide reversed this: a break sometimes has to be long-term. The paragraph keeps its "Temporary Separation" label.'),
    'A22': ('approve', None, ''),
    'B1': ('approve', None, ''),
    'B2': ('approve', None, ''),
    'B3': ('approve', None, 'A consent point: the guide\'s own rule ("No will stay no") already says a no holds.'),
    'B4': ('approve', None, ''),
    'B5': ('approve', 'It could also be your inherited parent script that you are picking up, and it is trying to enforce a rule about how you should be to belong to them. Find out what rule it is enforcing. Comfort your little one before you answer any of it. Your answers can be firm or funny, as long as they aren’t mean. Then work on finding some ordinary evidence to build a more believable \'grown up\' voice of your own.',
           'Your inner child guide answers the inherited parent instead of not arguing with it. I left out its "since mean is the Critic\'s department": this guide has no Critic.'),
    'B6': ('approve', None, 'RR-6.5 rewords "observing ego" in the same paragraph.'),
    'B7': ('approve', None, 'RR-6.2 adds commas to the same sentence.'),
    'B8': ('approve', None, ''),
    'B9': ('approve', None, ''),
    'B10': ('approve', None, 'In your inner child guide the Protector is a job of your one grown-up, not a separate part with needs. If you meant this prompt for a guard, Revise to keep the question and label it "When you want to ask a guard something:".'),
    'B11': ('leave', None, 'IC-A13 puts the same caution in "The Guide", where it\'s taught; here it would say it twice.'),
    'B12': ('approve', None, ''),
    'B13': ('approve', None, ''),
    'B14': ('approve', None, 'ST-9.2 moves this paragraph; the sentence goes with it.'),
    'B15': ('approve', None, ''),
    'B16': ('approve', None, ''),
    'B17': ('approve', None, ''),
    'B18': ('approve', None, 'ST-10.1 puts your heading "Forgiving yourself" above this part.'),
    'B19': ('approve', None, 'IC-A17 adds the same lines in "Inner child reparenting"; see its note.'),
    'B20': ('approve', None, ''),
    'B21': ('approve', None, ''),
}


def ic_items():
    for part in ('A', 'B'):
        items = cr.parse_reader((FIX / 'ic-align' / ('READER-%s.md' % part)).read_text(encoding='utf-8'), IC_FIELDS)
        for k, it in enumerate(items, 1):
            key = '%s%d' % (part, k)
            advice, override, note = IC_CHECK[key]
            if advice == 'dup':
                continue
            i, s, e = where_q(it['quote'])
            quote = BL[i]['text'][s:e]
            proposed = override or it['proposed']
            ic = re.sub(r'\s*\n\s*', ' ', it['ic'])
            add('IC-' + key, 'innerchild', 'Lined up with "%s"' % ic_head(ic), advice, edits=[(quote, quote, proposed)],
                why=you(it['differs']) + ' Your inner child guide: ' + ic, stays=you(it['keeps']),
                note=(note + (' ' if note else '') + ('Priority: %s.' % it['priority'] if it.get('priority') else '')).strip(),
                found_by='Inner child alignment %s (Opus), checked against your latest inner child guide' % part)


def you(t):
    """The readers wrote about Joel in the third person; the page talks to him."""
    for a, z in (('His decided', 'Your decided'), ('his decided', 'your decided'), ('the IC guide', 'your inner child guide'),
                 ('The IC guide', 'Your inner child guide'), ('IC guide', 'inner child guide')):
        t = t.replace(a, z)
    return t


def ic_head(ic):
    m = re.match(r'\[([^\]]+)\]', ic) or re.match(r'([^—]+?) —', ic)
    return m.group(1).strip() if m else 'your inner child guide'


def ic_terms():
    """IC-T1: the inner child guide's "your little one" and they/them in "Love doesn't have to wait for trust"."""
    reps = [('the "child"', 'your little one'), ('your "inner child"', 'your little one'), ('the "inner child"', 'your little one'),
            ('if he/she doesn\'t, it is', 'if they don\'t, it is'), ('he/she doesn\'t', 'they don\'t'), ('he/she is', 'they are'),
            ('he/she needs', 'they need'), ('him/her', 'them'), ('his/her', 'their'), ('he/she', 'they')]
    edits = []
    for b in BL:
        if b['section'] != 'Love doesn’t have to wait for trust' or b['level']:
            continue
        t = b['text']
        if not re.search(r'him/her|he/she|his/her|"inner child"|"child"', t):
            continue
        new = t
        for a, z in reps:
            new = new.replace(a, z)
        new = new.replace('You need to love your "inner child."', 'You need to love your little one.')
        edits.append((t, t, new))
    add('IC-T1', 'innerchild', 'Your little one, and they/them', 'approve', edits=edits,
        what='In "Love doesn’t have to wait for trust", "him/her" and "he/she" become "them" and "they", and the quoted "child" and "inner child" become "your little one", as in your inner child guide (24 places in 3 paragraphs).',
        why='Your inner child guide says "your little one" and they/them throughout; this section still has the older "him/her" and the quoted "inner child".',
        stays='Every sentence, word for word, apart from those words.',
        note='If you approve the other inner child suggestions in this section (IC-A5 to A9), their added words get the same change.',
        found_by='Inner child alignment A (Opus), its item 4, made for the whole section')


def overlaps():
    touch = {}
    for s in S:
        blocks = {e['block'] for e in s['edits']} | {sp['block'] for sp in s['spans']} | {i for m in s['moves'] for i in m['blocks']}
        for b in blocks:
            touch.setdefault(b, []).append(s['id'])
    for s in S:
        blocks = {e['block'] for e in s['edits']} | {sp['block'] for sp in s['spans']} | {i for m in s['moves'] for i in m['blocks']}
        others = sorted({o for b in blocks for o in touch[b] if o != s['id']}, key=order_key)
        if others:
            s['overlaps'] = others


def order_key(sid):
    return [int(x) if x.isdigit() else x for x in re.split(r'(\d+)', sid)]


def build():
    for key, x in sorted(((x['key'], x) for x in load_items('clarity2')), key=lambda kv: order_key(kv[0])):
        status, edits, title, note = RR[key]
        if status == 'dup':
            continue
        hard = x['hard']
        if edits is None or status == 'leave':
            quote = reader_quote(x['quote'], x['plain'])
            edits = [(quote, quote, x['plain'])] if edits is None or status == 'leave' else edits
        if status == 'leave':
            add('RR-' + key, 'reread', 'A reader stopped here', 'leave', edits=edits, why=hard,
                note=note, found_by='The reread on the fixed brief (Sonnet), part %d' % x['part'],
                deciding='Approve uses the reader\'s version (shown); Reject keeps yours as it is, as I suggest.')
            continue
        decided = None
        if status == 'decided':
            decided = {'status': 'approved', 'by': 'Joel', 'at': '2026-10-25T14:40:00Z',
                       'comment': 'From your message of 14:40: "you coud improve the second issue by changing to "because without redirecting the thought stream with your conscious, higher intention,""'}
        add('RR-' + key, 'reread', title, 'approve', edits=edits, why=hard, note=note, decided=decided,
            found_by='The reread on the fixed brief (Sonnet), part %d' % x['part'])
    for sid, old, new, title, note, why in RO:
        add(sid, 'reread', title, 'approve', edits=[(old, old, new)], why=why, note=note,
            found_by='The first reread (Sonnet), 01:01; checked again', what='"%s" becomes "%s".' % (old, new))
    for sid, edits, title, note in TYPOS:
        add(sid, 'typo', title, 'approve', edits=edits, why='A typo.', note=note, found_by='My check')
    sp = space_typos()
    add('TY-6', 'typo', 'Spaces before a full stop or comma (%d places)' % len(sp), 'approve', edits=sp,
        why='The Substack paste left a space between a link or a label and the full stop or comma after it, so readers see "guide ." and "Self ,".',
        what='Takes out the space before a full stop or comma after a link or a label, in %d places.' % len(sp),
        note='The French spacing before a colon in Appendix B ("Note :", "Perceptual Positions :") is consistent there, so I left it.',
        found_by='My check')
    structure()
    cuts('caveats', 'caveat', my_checks.CAVEATS, 'CV-')
    cuts('repeats', 'repeat', my_checks.REPEATS, 'RP-')
    ic_items()
    ic_terms()
    S.sort(key=lambda s: (first_block(s), order_key(s['id'])))
    overlaps()


def reader_quote(quote, plain):
    """The reader's quote as it is in the guide, widened to the words their plain version also covers (a reader sometimes
    rewrote the rest of the paragraph too, which would otherwise show twice)."""
    i, s, e = where_q(quote)
    t = BL[i]['text']
    for n in (60, 40, 25):
        tail = plain.rstrip()[-n:]
        k = t.find(tail, e)
        if len(tail) == n and k >= 0 and t.count(tail) == 1:
            e = k + len(tail)
            break
    for n in (60, 40, 25):
        head = plain.lstrip()[:n]
        k = t.find(head)
        if len(head) == n and 0 <= k < s and t.count(head) == 1:
            s = k
            break
    return t[s:e]


def first_block(s):
    bs = [sp['block'] for sp in s['spans']] + [e['block'] for e in s['edits']] + [i for m in s['moves'] for i in m['blocks']] + \
         [ins['before'] for ins in s['inserts']]
    return min(bs) if bs else 0


def main():
    build()
    review = {
        'format': sr.FORMAT, 'review_id': 'inner-signal-hypnosis-guide-review-20261025',
        'title': 'Hypnosis Guide Review',
        'intro': [
            'This is your whole hypnosis guide, as it is in Git now, with every suggestion from today’s checks marked where it applies. Each colour is one kind of problem (the buttons above say which). Under each marked paragraph is my suggestion: the paragraph as it would read (struck words go, green words come in), why, what stays, and my advice.',
            'Click <b>Approve</b>, <b>Reject</b> or <b>Revise</b> on each card (Revise opens your own version of the paragraph, starting from mine), and add a comment if you want. Nothing counts as approved until you click Approve. Your answers save as you click. <b>Next undecided</b> takes you through them in order.',
            'Some readers’ suggestions I’d leave as they are; they’re hidden unless you tick “The ones a reader flagged and I’d leave” under Filters. Your fix for 15.1 is already in, marked as yours.',
        ],
        'git_file': GIT_FILE, 'article': {'file': ARTICLE, 'sha256': hashlib.sha256(MD.encode('utf-8')).hexdigest()},
        'links': {'guide': BLOB + ARTICLE, 'review': BLOB + 'articles/inner-signal/humanize/fix-20261025/review/REVIEW.json'},
        'built': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M UTC'),
        'types': TYPES, 'suggestions': S,
    }
    probs = sr.check(review, BL)
    for p in probs:
        print('PROBLEM', p)
    (HERE / 'REVIEW.json').write_text(json.dumps(review, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    if probs:
        sys.exit(1)
    page = sr.page(review, MD, BL)
    (HERE / 'REVIEW.html').write_text(page, encoding='utf-8')
    counts = {}
    for s in S:
        counts.setdefault((s['type'], s['advice']), 0)
        counts[(s['type'], s['advice'])] += 1
    print(len(S), 'suggestions;', ', '.join('%s %s %d' % (t, a, n) for (t, a), n in sorted(counts.items())))
    print(HERE / 'REVIEW.html', len(page), 'bytes')


if __name__ == '__main__':
    main()
