"""My meaning reviews of the three sections that read Human in 437g with emu-h's whole-window runs: the quick start (HG04),
influence literacy (HG16) and troubleshooting (HG24). Each fix is the smallest change that gives back the published
point, keeping Emulate's words around it; each (old, new) is checked against the stretch's exact text."""
import json
def build(key, fixes, links=None):
    d = json.load(open('rev-f/%s.units.json' % key, encoding='utf-8'))
    body = {u['blocks'][0]: '\n\n'.join(u['paras']) for u in d['units'] if u['kind'] == 'emulate'}
    rv = []
    straight = lambda t: t.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')
    fixed = []
    for f in fixes:  # Emulate's text keeps straight quotes in some runs: match its style, both in the old and the new words
        b, t, w, o, n = f
        if b in body and body[b].count(o) != 1 and body[b].count(straight(o)) == 1:
            o, n = straight(o), straight(n)
        fixed.append((b, t, w, o, n))
    fixes = fixed
    for b in body:
        fs = [f for f in fixes if f[0] == b]
        for f in fs:
            assert body[b].count(f[3]) == 1, (key, b, f[3])
        r = {'block': b, 'verdict': 'FIX' if fs else 'OK'}
        if fs:
            r['problems'] = [{'type': t, 'what': w, 'replace': o, 'with': n} for _, t, w, o, n in fs]
        if links and b in links:
            r['links'] = links[b]
        rv.append(r)
    assert not [f for f in fixes if f[0] not in body], [f[0] for f in fixes if f[0] not in body]
    json.dump(rv, open('rev-f/%s.review.json' % key, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(key, len(fixes), 'fixes in', sum(r['verdict'] == 'FIX' for r in rv), 'of', len(rv), 'stretches')

build('HG04', [
 (1, 'WRONG', "'conjure' for gathering attention; come all the way back", 'Conjure, notice, respond, wait, return.', 'Gather attention, notice, respond, wait, come all the way back.'),
 (2, 'LOST', 'the practice is something you learn to conduct, not a checklist to keep reading (and the sentence broke off into the next paragraph)',
  'After putting this on the shelf,', 'Then put the screen on the shelf: the practice is something you learn to conduct, not a checklist to keep reading.'),
 (3, 'UNCLEAR', 'the paragraph began mid-sentence', 'you’ll follow whatever you notice', 'You’ll follow whatever you notice'),
 (3, 'LOST', 'direction or more time', 'to create a boundary, to proceed, etc.', 'to create a boundary, to give direction or more time, etc.'),
 (4, 'LOST', 'stop deepening', 'Return to the room & be appropriately supported.', 'Stop deepening, return to the room & get appropriate support.'),
 (6, 'INVENTED', "'when you're by yourself'; LOST: before choosing a script", 'When you’re by yourself, do you talk', 'Before choosing a script, notice: do you talk'),
 (7, 'LOST', "neither question asks you to decide that feelings always come first; not a diagnosis", 'You may not know.', 'You don’t have to decide that feelings always come first, and you may not know.'),
 (7, 'SHIFT', 'a way to choose workable instructions, not a diagnosis', 'This isn’t about being right, just finding what’s useful.', 'This isn’t a diagnosis, just a way of finding what’s useful.'),
])

build('HG16', [
 (1, 'SHIFT', "influence literacy: noticing when somebody is shaping your attention (not 'all the ways you're being manipulated', which the paragraph then calls benign)",
  'is an increased awareness of all the ways you’re being manipulated in your day-to-day life.', 'is influence literacy: an increased awareness of all the ways your attention is being shaped in your day-to-day life.'),
 (1, 'SHIFT', 'religious fear (not a religion)', 'By a religion?', 'By religious fear?'),
 (2, 'LOST', 'one honest question would break the spell', 'about something pretty quickly.', 'about something pretty quickly. You may also feel that one honest question would break the spell.'),
 (3, 'SHIFT', "don't obey right away (not 'don't listen')", 'Don’t listen.', 'Don’t obey right away.'),
 (4, 'LOST', 'the three ways: it smuggles in your consent, makes one choice seem inevitable, hides a disputed claim inside the sentence',
  'Some common ways hypnotic language becomes manipulative includes:', 'Some common ways hypnotic language becomes manipulative: it smuggles in your consent, makes one choice seem inevitable, or hides a disputed claim inside the sentence, like'),
 (5, 'SHIFT', "the examples' patterns: 'the only reason you resist is', 'part of you already knows', 'everyone who is truly awake'",
  '“the reason you’re not feeling it yet is…”', '“the only reason you resist is…”'),
 (5, 'SHIFT', 'part of you already knows', '“even if part of you doesn’t feel that’s true…”', '“part of you already knows…”'),
 (5, 'LOST', 'truly awake', '“everyone knows…”', '“everyone who’s truly awake knows…”'),
 (6, 'LOST', "the grammar assumes the conclusion, turns resistance into proof and makes obedience feel like awakening ('other language patterns' led into the questions)",
  'Other language patterns to watch out for include:', 'The grammar takes the conclusion for granted, turns your resistance into proof, and makes obeying feel like waking up. Ask:'),
 (8, 'SHIFT', "a useful guide leaves the adult more present; powerful states need stronger boundaries (not 'the above is a rough guide')",
  'The above is a rough guide to help bring more of the ‘adult’ into the conversation. Use more of the above when the state is more powerful.',
  'A useful guide leaves more of the ‘adult’ in the conversation. When the state is more powerful, you need stronger boundaries.'),
 (10, 'UNCLEAR', "'these words' had nothing to point to: permissive words", 'These words in and of themselves', 'Permissive words in and of themselves'),
 (11, 'SHIFT', "can slip past (not 'are generally used to')", 'Indirect suggestions are generally used to by-pass', 'Indirect suggestions can by-pass'),
 (12, 'UNCLEAR', 'the bracket never closed', 'using the same mechanics of induction.', 'can use the same mechanics of induction).'),
 (14, 'LOST', "uncertainty turned into invisible success that can't be checked", 'Using phrases like "whether or not you notice", etc.', 'Using phrases like "whether or not you notice", etc., which turn uncertainty into invisible success that can’t be checked.'),
 (15, 'SHIFT', "belonging to someone else (not 'being part of something')", 'or being part of something, etc.', 'or belonging to someone else, etc.'),
 (16, 'SHIFT', "without telling you that repeated re-entry is part of the method (not 'the benefits')",
  'without informing the subject of the benefits of going in and out of absorption several times.', 'without informing the subject that going in and out of absorption several times is part of the method.'),
 (20, 'INVENTED', "'then it can not be a covert hypnosis'; the published: a real choice includes at least one branch that doesn't continue the induction",
  'If at any point during a hypnosis you have a REAL choice to NOT carry on, turn it into a lighter hypnosis, use a different method, stay in full awareness, pause or stop the hypnosis then it can not be a covert hypnosis.',
  'A REAL choice during a hypnosis includes at least one way to NOT carry on: turn it into a lighter hypnosis, use a different method, stay in full awareness, pause or stop the hypnosis.'),
 (20, 'INVENTED', "'if you are unsure you probably can't'; the published: silence and uncertainty don't become consent",
  'If you are unsure that you can or can’t then you probably can’t. Simply not knowing your options isn’t a choice.', 'And silence, or simply not knowing your options, isn’t consent.'),
])

build('HG24', [
 (5, 'LOST', "isn't, by itself, resistance", 'is not a resistance', 'is not, by itself, resistance'),
 (8, 'LOST', 'the particular warmth, boundary or direction you lack; a caring figure; one believable sentence',
  'borrow the capacity you need from someone (real or imagined) who has it. Try out a sentence or action etc and see how it goes.',
  'borrow the warmth, boundary or direction you need from a caring someone (real or imagined) who has it. Try out one believable sentence or action etc and see how it goes.'),
 (12, 'WRONG', "the fourth question: will you stop substituting insight for action", '“I need to know you’ll stop telling me that what I’m asking for isn’t actually what I need.”', '“I need to know you’ll stop putting insight in place of action.”'),
 (14, 'SHIFT', "stay with the feeling or preference that is actually present (not 'talk in terms of')", 'then simply talk in terms of your feelings or preferences.', 'then simply stay with the feeling or preference that’s actually there.'),
 (15, 'SHIFT', "the script: 'You do not have to let me in. Just tell me what would make the doorway safer.'", '“Even if you don’t let me in, there are things I can do to help you feel safer.”', '“You don’t have to let me in. Just tell me what would make the doorway safer.”'),
 (16, 'LOST', 'a beginner experiment, instead of forcing an image', 'by working with whatever you are aware of–preferences, curiosity, or even a statement that you’re new to this and would like to try something and see how it goes.',
  'by working with whatever you are aware of (a preference, curiosity, or a beginner’s experiment to try and see how it goes) instead of forcing an image.'),
 (18, 'SHIFT', "less contact (not 'do something to reduce it')", 'or whether you need to do something to reduce it.', 'or whether you need less contact with it.'),
 (18, 'SHIFT', 'stop searching for content', 'stop whatever you’re doing to help your body first.', 'stop searching for content and help your body first.'),
 (20, 'LOST', "'You do not have to scream for me to listen'; show me one step; stand down gently", 'Thank you for letting me know.', 'Thank you for letting me know. You don’t have to scream for me to listen.'),
 (20, 'LOST', 'show me one step', 'If so, what?', 'If so, show me one step.'),
 (20, 'LOST', 'gently', 'can you let my body know it can stand down?', 'can you help my body stand down gently?'),
 (20, 'UNCLEAR', "'Little'", 'Talk to your Little and Protector parts:', 'Talk to your Little one and Protector parts:'),
 (21, 'SHIFT', "when anxiety includes these (not 'is causing'); psychosis-like or mania-like symptoms",
  'If your anxiety is causing you to have chest pain, faint, have suicidal thoughts, become psychotic or manic, severely dissociate, not sleep, or makes you want to hurt yourself or someone else, get help from a professional.',
  'If your anxiety comes with chest pain, fainting, suicidal thoughts, psychosis-like or mania-like symptoms, severe dissociation or not being able to sleep, or makes you want to hurt yourself or someone else, get help from a professional.'),
 (23, 'INVENTED', "'out loud'", 'name five objects out loud.', 'name five objects.'),
 (25, 'SHIFT', "somebody who will disagree with you (not 'feedback')", 'get some feedback.', 'find somebody who will disagree with you.'),
 (25, 'SHIFT', "the script: if this insight is real, it will survive...; 'silently' is new", 'Silently say, “I need to know that these insights can survive sleep, food, time, humility, and feedback.”',
  'Say, “If this insight is real, it will survive sleep, food, time, humility, and feedback.”'),
 (28, 'SHIFT', "the script: not here to do this perfectly (not 'not supposed to be doing this well')", '“I’m not supposed to be doing this well.', '“I’m not here to do this perfectly.'),
 (28, 'UNCLEAR', 'the script lost its closing quotation mark', 'deeper than my surface mind.', 'deeper than my surface mind.”'),
 (28, 'LOST', 'one honest action', 'to do something.', 'to do one honest thing.'),
 (33, 'LOST', "the script's list: what task, boundary, meal, rest, repair or conversation", '“What would love do right now?”', '“What task, boundary, meal, rest, repair, or conversation does love need from me right now?”'),
 (42, 'LOST', "let that matter without demanding the child receive it on command", 'how much more love and freedom are possible.', 'how much more love and freedom are possible. Let that matter, without demanding that the child receive it on command.'),
 (42, 'INVENTED', "'as a child, you prayed'; the published: prayer can evoke abandonment or condemnation, or a teacher's betrayal can damage something sacred",
  'It’s also possible that, as a child, you prayed and then felt abandoned or condemned; that you went to a teacher and were betrayed.',
  'It’s also possible that prayer left you feeling abandoned or condemned, or that a teacher’s betrayal damaged something sacred.'),
 (42, 'LOST', 'what was lost and what needs questioning', 'It’s worth asking some questions about what happened.', 'It’s worth asking what was lost and what needs questioning.'),
 (42, 'WRONG', "'while pretending there isn't a larger horizon, but pretending you're curious'; the published: practical care while the horizon still feels too small, and curiosity about deeper happiness without pretending to believe an explanation",
  'Sometimes the best thing is to do something practical in your life, while pretending that there isn’t a larger horizon, but pretending that you’re curious about what it would be like to step into it.',
  'Sometimes the best thing is to do something practical in your life while the horizon still feels too small, and to follow your curiosity about deeper happiness without pretending to believe an explanation.'),
 (42, 'SHIFT', "some people already have enough love and meaning for the life they want ('seem to', and 'you don't have to do anything about it' is new)",
  'Other people seem to have enough love and meaning. You don’t have to do anything about it.', 'Some people already have enough love and meaning for the life they want.'),
 (46, 'SHIFT', "does this round help you feel, understand, decide or respond differently, or are you checking for reassurance",
  '“Am I looking for something new here, or am I checking again to see if it’s gone yet?”', '“Does this round help me feel, understand, decide or respond differently, or am I checking again for reassurance?”'),
 (46, 'SHIFT', "can revisit familiar ground; novelty isn't required (not 'supposed to')", 'you’re supposed to cover the same ground over and over again.', 'it’s fine to cover the same ground again; it doesn’t have to be new every time.'),
 (46, 'LOST', 'or chasing it away', 'but don’t argue with it.', 'but don’t argue with it or chase it away.'),
 (50, 'UNCLEAR', "'my child' could be a real child: the inner child", '“What would show my child that I’m for real?”', '“What would show my inner child that I’m for real?”'),
])
