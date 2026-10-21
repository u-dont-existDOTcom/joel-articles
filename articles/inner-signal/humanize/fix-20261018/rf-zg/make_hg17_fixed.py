"""The induction section (HG17) from Emulate sample ba, with every lost point put back (2026-10-21, after Joel's answers of
17:56 UTC: question 4, "i am fine with all the humanized replacements as long as we don't lose anything").

Base: rf-zg/HG17.ba.json (emu-ba composed over rf-j/HG17.fixed.json). Its second reader (HG17.ba.verify.out.md: kept 156,
changed 57, lost 30, invented 14) lists each point. Here each changed paragraph is ba's paragraph with the lost points put
back inside its own sentences, the inventions taken out, and the changes that alter what a reader does or believes put
right (the triage brief's rule, rf-a/TRIAGE-BRIEF.md); tone and looser wording are let stand. Three lines of the published
script come back close to how Joel wrote them, because they are lines the reader says ("What am I noticing now?" and the
two-hand induction's two lines, the second joined with "and"); the rest is in ba's register. The three published links go
back on their words ("links").

The first pass put the published phrasings back as Joel wrote them, and the linter found tells in eleven of my sentences
that ba's text didn't have: four "without ...ing" and one "can ... without" (E186: "without finishing the thought
first", "without preparing an answer", "without going over its whole story", "without trying to disappear inward",
"You can stay nearby, listening, without finishing their sentence"), three "not Y" tails (O9: "for orienting yourself,
not for making an unstable state any deeper", "guided by your response, not by the response the script expected", "a
clear state, not a sleepier one"), two ideas doing what a person does (O6: silence giving a narrator permission; a sound
drawing attention "without you having to arrange it") and a double "and" (O14). Each point is now said plainly in its
own words ("and leave the thought unfinished", "Don’t get an answer ready", "all on its own"), with the same meaning.

  python3 articles/inner-signal/humanize/fix-20261018/rf-zg/make_hg17_fixed.py   (from the repo root)
Writes rf-zg/HG17.fixed.json and rf-zg/FIXES.json (each paragraph's before and after, with the points it answers).
"""
import json, pathlib

HERE = pathlib.Path(__file__).resolve().parent

# (unit, paragraph): (points answered, new paragraph)
FIX = {
    (1, 0): ('P1: "guarded"; begin with orientation and containment instead of adding depth (a directive)',
             "Inductions serve to gather up attention in order to access quiet stuff. They are not about surrendering, playing "
             "asleep, or obeying someone. You may want to do an actual induction if you are sober, distracted, analytical, "
             "guarded, or otherwise not very trancey. If you are already trancey, due to meditation, loveyhuasca, lucid "
             "dreaming, grief, music, prayer, or tiredness, or if for any other reason you feel in touch with deeper stuff, "
             "skip the induction and go straight to orientation and containment instead of going deeper."),
    (1, 1): ('P2: the amount of trance that suits the practice, and its qualities (focused, warm, receptive, embodied, still '
             'able to stop); out: "You can control and decide how trancey you want to get" (invented)',
             "Get as trancey as the practice needs: focused, warm, receptive, embodied, and still able to stop. Deeper "
             "trance is optional."),
    (3, 0): ('P4: deepen only when that helps; let what you notice shape the words and the next response',
             "It gets you ready to do whatever you are doing. It does this by gathering up your attention, deepening the "
             "state only when that helps, and then letting what you notice shape the words and what happens next. There are "
             "all sorts of ways to do this. The method here involves counting, but there are many others. You might just "
             "talk with someone, tell a story, move, play with sound, or make use of curiosity. However you do it, say so. "
             "Don’t pretend it’s some other thing in the name of elegance."),
    (3, 1): ('P5: build from the response that is already happening; a receptive way of listening (not "what you want to '
             'hear"); no ceremony to finish before you may respond; out: "always"',
             "You can test a simple target suggestion before deepening, to see if you are already getting your target "
             "response, and then build from that. The induction is just there to help you find a receptive way of "
             "listening. It doesn’t have to be some sort of ceremony you finish before you’re allowed to respond."),
    (5, 0): ('P7: neutral witnessing; the metaphors needn\'t all report for duty at once (not "you don\'t need" them); '
             'switch when the metaphor stops helping',
             "You need to keep it simple. One purpose, one anchor or image to start, one way back, and a decided on feeling "
             "(warm, bounded, directed, or neutral witnessing). You don’t need floating, stairs, gardens, inner rooms, color, "
             "and a dialogue with a child all at once. If you do metaphors at all, use one, and only switch to another "
             "consciously, when the first one stops helping."),
    (5, 1): ('P8: a signal arrives (the reader doesn\'t send one)',
             "Metaphors and imagery are optional. A signal might come to you through sensation, rhythm, movement, words, "
             "spatial sense, simple knowing, or the lack of a signal. If you are using words, keep them related to the world "
             "you have created. If you are counting, do it in a way that makes sense in that world. When you’re done with "
             "your induction, come back the other way. You can borrow qualities from your induction (warmth or steadiness) "
             "but don’t change who you are."),
    (7, 1): ('P11: you don\'t have to find a problem; several minutes for returning and reflecting',
             "2. Decide what you want to do during the induction. You might be asking a question, building a quality, or "
             "exploring a state. You might also want to pick what you are NOT going to do. Consider your time. Remember that "
             "this doesn’t have to be about a problem, and you can use it for good stuff too, like love, play, confidence, "
             "creativity, or communion with things. Make sure to leave a few minutes at the end for coming back and for "
             "reflection."),
    (7, 2): ('P12: get immediate support instead of exploratory hypnosis; Already open? is for orientation, not for '
             'intensifying an unstable state',
             "3. Make sure you are in a safe place. Don’t do this if you are driving, in water, operating machinery, or "
             "otherwise in a place where you need to attend to yourself or others. If you are intoxicated, acutely confused, "
             "or otherwise not capable of protecting yourself, then get some immediate support instead of doing exploratory "
             "hypnosis. The later part of this (the already open? section) is for orienting yourself. Don’t use it to make "
             "an unstable state any deeper."),
    (7, 3): ('P13: a firmer invitation to stay with a feeling; out: "a gentle suggestion" (added)',
             "4. Decide how you want to be coaxed into it. Do you want to feel like you have a lot of room, or do you want "
             "to feel held and warm? Or do you need a firmer invitation to stay with a feeling? Preview to yourself what you "
             "are going to do. This might involve closing your eyes, or even coming out of it and going back in. It will "
             "include coming back at the end. If you are recording your induction, read the script to yourself first (if "
             "you can). Know that you can end the induction any time you want by saying “stop” or by opening your eyes. You "
             "can also say “less” to make it ask less of you, or “quiet” to make it stop talking. You do not need permission "
             "from any inner part to stop, even if you feel like a part is telling you that you need permission."),
    (7, 4): ('P14: let a useful response become easier and less effortful (an invitation); silence doesn\'t authorize a '
             'narrator to add what you haven\'t agreed to (a consent rule)',
             "5. If you have not done hypnosis before, or if you haven’t done it in a while, practice the coming in and out "
             "part first before trying to do it for anything else. You don’t have to watch yourself the whole time, but it "
             "is good to make sure you can do the state change at first. Let a useful response get easier and take less "
             "effort. The answer no will stay no. And if you say nothing, that isn’t a yes, so a narrator can’t add things "
             "you haven’t agreed to."),
    (7, 5): ('P15: not the response the script expected; the Utilization link; a thought, sound, movement or objection may '
             'change where the practice goes; keep safety and exit instructions plain; "after the induction"',
             "6. Let the response you got guide what happens next, whatever the script expected. Utilization is "
             "the act of letting your current response guide where you go next: a thought, a sound, a movement, or an "
             "objection may change where the practice goes. Learn to notice what does happen when you do these things. Also "
             "learn that if nothing happens, that doesn’t mean there was a positive, hidden change. Keep the safety and exit "
             "instructions plain. If you need more tools on utilization, see Appendix B, or read on to Let the next response "
             "guide you, which shows how to use them after the induction."),
    (9, 0): ('P17: read it slowly; learn its movement; an opening phrase (the one P24 says); keep using the anchor where the '
             'words refer to it; out: "(see link above)" (there is no link above; the two-hand practice comes later)',
             "Read this slowly to yourself on a recorder, or read it aloud, or learn how it moves and say it silently if you "
             "are good at that. Pick a sound, a contact on your body, or the two hands thing (below) to be your anchor for "
             "this, and pick an opening phrase. Keep using the same anchor wherever the words mention it. Don’t read the "
             "instructions, just pause between paragraphs."),
    (9, 1): ('P18: the difference between looking for something and letting what is already there come into view',
             "Allow your eyes to rest on something in the room for a little while. Notice the difference between looking "
             "for something and just letting what’s already there come into view."),
    (9, 2): ('P19: the pause; the contact and the pressure; a sound or a breath without your arranging either one',
             "As you rest, allow yourself to notice something you can feel, perhaps the sensation of something beneath you … "
             "the contact, the pressure. A sound may draw your attention, or a breath, or something else, all on its own."),
    (9, 4): ('P21: a thought about whether you\'re doing this properly; return without finishing the thought first',
             "You may notice a thought arising, about the day, or about whether you’re doing this properly. Whenever you "
             "notice a thought, simply allow yourself to re-engage with whatever you've chosen to anchor yourself, and leave "
             "the thought unfinished."),
    (9, 5): ('P22: the pauses; let attention stay long enough to become curious',
             "You may focus your attention on one aspect of what you're doing … perhaps a particular detail of a sound, or a "
             "sensation, or the act of listening itself … and let your attention stay with it long enough to get curious."),
    (9, 6): ('P23: someone who has begun to speak and hasn\'t found the words; stay nearby, listening, without finishing '
             'their sentence',
             "Allow yourself some time to do this, the time you would give someone you care about who has started to speak "
             "and hasn’t found the words yet. You’d stay nearby and listen while they finish their own sentence."),
    (9, 7): ('P24: say it as an invitation; how it is received; out: "in your mind\'s eye"',
             "Now say to yourself the phrase you have chosen. Say it as an invitation, and allow yourself to notice how it "
             "is received."),
    (9, 10): ('P27: "Five."; four, gather around what you find; three, leave a little space after the words; two, listen '
              'into that space without preparing an answer; one, stay here for a moment',
              "5... focus your attention once more on your chosen anchor. 4... allow more of your attention to gather around "
              "what you find. 3... leave a little space after the words. 2... listen into that space. Don’t get an answer "
              "ready. 1... stay here for a moment, allowing yourself some time to settle in."),
    (9, 11): ('P28: your chosen concern, lightly, or your wish for contact; let it be present without rehearsing its whole '
              'story',
              "Bring your chosen concern lightly to mind, if you wish, or just stay with your wish for contact. Let it be "
              "there. Its whole story can wait."),
    (9, 12): ('P30: give the response time to take its own form; there may be nothing clear yet (out: "in response to your '
              'question", which ba never gave; the question is back as its own line before this one)',
              "Allow yourself to notice what comes to you, if anything, and give it time to take its own form. Notice how it "
              "comes to you, if it does - sensation, words, pictures, feelings, movements, etc."),
    (11, 0): ('P33: stabilize before making it stronger; out: "rather than risking deepening an experience you won\'t be '
              'able to integrate" (an added claim)',
              "Use this when you're already open (from loveyhuasca, meditation, lucid dreaming, grief, beautiful music, "
              "prayer, erotic energy, exhaustion, seeing something incredibly beautiful, etc), and you just need to aim and "
              "stabilise what's already there before making it any stronger."),
    (11, 1): ('P34: keep it kind (no need to intensify it stays as ba had it, "All you need to do")',
              "Recognise to yourself that your state is already open. All you need to do is aim it, stabilise it, and keep "
              "it kind."),
    (11, 2): ('P35: press gently but firmly',
              "Orient yourself: look around and say out loud where you are, what date (or day) it is, feel your body, ground "
              "yourself, feel your feet, hands, spine, etc. Make some physical contact with yourself (press your thumbs to "
              "the tip of your index fingers, gently but firmly, so you can feel the friction). Focus on the physical "
              "sensation."),
    (11, 3): ('P36: only what can be integrated is welcome (a welcome, not a vow of control); anything too much can wait; '
              'the body may stay safe (a wish, not an assertion)',
              "Say to yourself, 'Only what I can integrate is welcome now. Anything that’s too much can wait. My body can "
              "stay safe. I am here, in my adult body, with my adult experience. My inner child does not need to face this "
              "on her/his/their own.'"),
    (11, 5): ('P38: the next useful truth, symbol, feeling, question or action (not only "a step I need to take")',
              "Say to yourself, 'I ask that you show me the next useful truth/symbol/feeling/question/action, and that you "
              "show me only what I am able to integrate.'"),
    (13, 0): ('P40: feel the feet; let the breath be natural',
              "Sit up, open your eyes, feel your feet, let your breath be natural, and say to yourself, 'I recognise that I am "
              "not going anywhere. I am only coming closer to what is here.'"),
    (13, 2): ('P44: bring me gently into the present',
              "Then say to yourself, 'I ask that if I am receiving guidance, you show me the action I need to take; and if I "
              "am avoiding what is here, please bring me gently back into the present, and show me what I am avoiding.'"),
    (13, 3): ('P45: the source link (hypnosis can be more alert rather than more relaxed); notice what remains, without '
              'trying to disappear inward',
              "If your state of being still is one where you tend to become sleepy, diffuse or mentally escaping, try making "
              "your hypnosis more active, since hypnosis can be more alert rather than more relaxed. For example, keeping your "
              "eyes open, and making a deliberate movement with one hand as you bring yourself into a clearer state, and then "
              "ceasing the deliberate movement and noticing what remains. Don’t try to disappear inward. For example, you "
              "could say to yourself:"),
    (13, 4): ('P46: press gently; clearer, not sleepier; the echo in the fingers, the breath, the attention, or nowhere at '
              'all',
              "'As I keep my eyes open, I press my thumb and forefinger together gently, then release. As I do this, I bring "
              "myself into a clearer, more awake state. Again, I press my fingers together, and again I release them, as "
              "I bring myself into an even clearer state. One more time... and now I stop pressing my fingers deliberately, and "
              "I notice in the first second after I cease my deliberate movement whether there is an echo in my fingers, my "
              "breath, my attention, or nowhere at all. I notice, I keep myself upright, and I work at this level.'"),
    (15, 0): ('P48: (the heading\'s words taken off the line, under the published heading; "plexus" spelled right)',
              "Put one hand on your heart, and the other on your solar plexus."),
    (15, 1): ('P49: out: "or feel free to make different associations if you like" (added)',
              "Label the hand on the heart as your Nurturer and the hand on the solar plexus as your vulnerable child."),
    (15, 2): ('P50: breathe gently', "Breathe gently..."),
    (15, 3): ('P51: the spoken refrain, as Joel wrote it (a line to say)',
              "As you breathe, say to yourself, “Love above. Child below. Adult present.”"),
    (15, 4): ('P52: the second spoken line: I send love, I receive the child\'s signal, I send love again, I listen again '
              '(the reader receives and listens)',
              "Then say, “I send love down to the child, and I receive the child’s signal. I send love again, and I listen "
              "again.”"),
    (17, 0): ('P54: out: "For sleep you can cut the last part out" (a new step); the task is rest',
              "Sleep induction has a different goal than inner work, where the Adult ultimately needs to come back in to write "
              "things down and take actions. When you are going to sleep you want your analytical mind to stand down until the "
              "next day, when you have time for revelations. The task is rest."),
    (19, 0): ('P57: what fractionation is (back toward ordinary awareness, then deciding whether to go back in); used '
              'openly, a door in both directions; name it before using it (not "I always announce", an invented fact); no '
              'answer secretly means "deeper"',
              "There is an optional fractionation you can add to this at some point: you come back toward ordinary awareness, "
              "then decide whether to go back in. Used openly, it teaches you that trance has a door in both directions. Say "
              "that you're doing it before you do it, so an answer never secretly means \"go deeper\"."),
    (19, 1): ('P58: open your eyes and come back toward ordinary awareness (a step); feel the room; notice what changes as '
              'attention gathers again; you may stop at either point',
              "Open your eyes and come back up toward ordinary awareness. Feel the room and decide whether to stop here. If "
              "you want to go on, close or soften your eyes again and notice what changes as your attention gathers. Either "
              "way is ok, you can stop at either point."),
    (21, 0): ('P60: if it is useful, attention may become more gathered',
              "If it will be useful, your attention may gather more. But if it won't, you can stay just as awake as you need "
              "to be."),
    (21, 1): ('P61: a chair where the adult waits (not a chair across from the Adult)',
              "Pick an inner scene to go into when you get there. It can be a room in your heart, a garden, a temple, sitting "
              "by a fire with the Protector nearby, at a lake with clear water where you can see the bottom, or a chair where "
              "the Adult waits, whatever feels right to you. Just pick one."),
    (21, 2): ('P62: who or what needs to speak first', "Who or what needs to talk first?"),
    (23, 1): ('P64: give up the responsibility of making anything happen',
              "As I wait, I let go of the responsibility of making anything happen..."),
    (23, 2): ('P65: when the inner meeting space is ready (not permission); out: "which knows what is best for me in the '
              'long term" (added)',
              "If it would be useful, my wise subconscious might let a finger in one of my hands twitch, pulse, come up by "
              "itself, heat up, tingle, or in some way become noticeable to me when the inner meeting space is ready."),
    (23, 3): ('P66: wait with love and notice (not "for what is true")',
              "I will not try to make it happen, I will not pretend it is happening, I will just wait with love and notice..."),
    (25, 2): ('P69: his dad brought two fingers together, including while driving (past; out: "uses", "when he drives", and '
              '"great for calming down and being more alert"); his experience, not a recommendation; keep alert calming and '
              'inward hypnosis on different cues',
              "My dad used a mudra ( putting two fingers together like the \"Ok\" sign ) to help him relax, including when he "
              "drove. That's his experience, not a recommendation to go into a trance while driving. Don't do that. Keep the "
              "cue you use to calm down and stay alert separate from the one you use for inward hypnosis."),
    (25, 3): ('P70: a distinctive cue; pair it with that receptive way of listening; not a peak of emotion, a child state or '
              'a traumatic scene (three exclusions, no causal claim); out: "to instantly go into hypnosis"',
              "Pick a distinctive word, phrase or motion ( optional ) that you will use to go back into hypnosis. Practice "
              "saying the word or phrase while doing the motion ( if you picked one ) when you are in a good, familiar "
              "hypnotic state, pairing it with that receptive way of listening, and not with a peak of emotion, a child state "
              "or a traumatic scene. You are picking the state here, it means whatever you say it means."),
    (25, 4): ('P71: set aside time, an appropriate place, a deliberate cue; return to this familiar way of listening; '
              'change direction or finish; out: "From now on" and "just as easily" (a promise)',
              "When I deliberately pick a time and an appropriate place to use this word or phrase to begin, I can return to "
              "this familiar way of listening. I can change direction or finish."),
    (25, 5): ('P72: gradually shorten the longer induction',
              "Now come back up and at some point when it is appropriate for you to begin a practice, start using this. You "
              "can gradually shorten the longer induction as you find this useful, or just do the longer induction when this "
              "doesn't seem to be enough for what you are working on. You don't have to do it any particular number of "
              "times, you don't have to go a certain depth instantly, and you don't need to have any particular sensation "
              "when you do this."),
    (25, 6): ('P73: it stays away when not chosen; it mustn\'t become obedience to a narrator, a notification or an '
              'overheard word (a check on conditioning)',
              "Check to make sure it is useful, that you can turn it on and off at will, and that it stays away when you "
              "haven't chosen it. It must never turn into obeying a narrator, a notification, or anything you might overhear; "
              "it is a tool for you to use when you pick to use it. Going into hypnosis faster doesn't mean you should be "
              "working on things you aren't ready for."),
    (25, 7): ('P74: never train, test or use it while driving or doing anything requiring active attention',
              "Never practice or use this when driving or doing anything where you need to be actively paying attention. It "
              "isn't safe to go into a trance where you are listening inwardly when you need to be listening outwardly, even if "
              "you have your eyes open and even if you use the \" if it would be useful \" type language."),
    (25, 8): ('P75: state your decision while awake; a cancellation sentence doesn\'t prove the association vanished '
              'instantly; persistent unwanted responses or disorientation need qualified help; a retained cue is only for a '
              'future, separately chosen session; today\'s state ends with the return; out: "something like the below" '
              '(twice, with nothing below) and "a good start"',
              "To turn it off, just stop rehearsing it, remove it from any recordings you may have, stop having it as an "
              "active part of any apps you may use, and go back to the regular induction. Say that you're done using it while "
              "you're awake, but keep in mind that saying so doesn't mean the association is gone right away. If you still "
              "have the response when you don't want it, or you feel disoriented after the state, please get qualified help. "
              "If you want to keep it for future use, it's only for beginning a session you choose at a future time, and the "
              "state you are in now ends when you come back."),
}
# new paragraphs: (unit, insert before paragraph index): (points, text)
INSERT = {
    (9, 12): ('P29: the question "What am I noticing now?", Joel\'s line to ask', "What am I noticing now?"),
}
APPEND = {
    17: ('P55: Nimja\'s sleep playlist (the link)', "For sleep hypnosis, see Nimja’s sleep playlist."),
}
DROP = {(7, 6): 'Emulate\'s own heading line ("Induction for when you are sober (3-5 min)") above the published heading'}
# Round 2 (2026-10-21, after the first reviews: SENSE-HG17.md, STANCE-HG17.md, march/march-labels.txt and
# HG17.fixed.verify.out.md): exact replacements in the paragraph as round 1 left it (ba's own paragraph where round 1 didn't
# change it), each with the finding it answers.
REVIEWS = {
    (7, 1): [(2, 'stance 1: choosing what you leave alone is part of every session\'s setup (Quick start: "Choose one purpose '
              'and what you are leaving alone today"; published P11), not an option',
              'You might also want to pick what you are NOT going to do.', 'Also pick what you are NOT going to do today.'),
             (2, 'stance 2: communion is the essay\'s word for the inner meeting of the conscious mind, the subconscious, the '
              'body and the parts (Introduction), not "communion with things"',
              'or communion with things.', 'or communion.')],
    (7, 2): [(2, 'stance, the published text\'s own contradiction: "otherwise" made every intoxicated reader one who can\'t '
              'keep safe; the published lists three conditions ("When intoxicated, acutely confused, or unable to keep '
              'yourself safe"). Whether exploratory hypnosis on loveyhuasca is ruled out goes to Joel (question 11)',
              'or otherwise not capable of protecting yourself,', 'or not able to keep yourself safe,')],
    (7, 3): [(2, 'cold read P11: "make it ask less of you": who is "it"', 'to make it ask less of you',
              'to make the induction ask less of you')],
    (7, 4): [(2, 'stance 3: the published asks for the first rehearsals "without a difficult subject", not entry and exit '
              'drills before any other use',
              'practice the coming in and out part first before trying to do it for anything else.',
              'practice the coming in and out part first, and leave difficult subjects for later.')],
    (7, 5): [(2, 'cold read P13: "these things" could be the steps or the thought, sound, movement or objection just listed',
              'Learn to notice what does happen when you do these things.', 'Learn to notice what does happen as you go.'),
             (3, 'meaning, part 1, P15: Appendix B holds "richer language tools" (the published), not "more tools on '
                 'utilization"', 'If you need more tools on utilization, see Appendix B,',
              'If you need richer language tools, see Appendix B,')],
    (9, 5): [(3, 'meaning, part 1, P22: "focus your attention on one aspect" made the step willed; the published lets a '
                 'detail "hold your interest", the script\'s receptive way',
              "You may focus your attention on one aspect of what you're doing",
              "You may find one aspect of what you're doing holding your interest")],
    (9, 8): [(3, 'meaning, part 1, P25: the published keeps "a sound from the room" available in the background (a link to '
                 'the room); "something you\'re hearing" lost the room',
              "something you're hearing.", 'a sound from the room.')],
    (9, 12): [(3, 'meaning, part 1, P30: "There may be nothing clear yet" was lost, and "Notice how it comes to you" read as a '
                  'new step; the published lists the forms ("It might be a sensation, a few words, ...")',
               'Notice how it comes to you, if it does - sensation, words, pictures, feelings, movements, etc.',
               'It might come as sensation, words, pictures, feelings, movements, etc. It may not be clear yet.')],
    (9, 0): [(2, 'cold read P14: "the instructions" could be this paragraph or the script\'s own lines; the published: "don\'t '
              'read the delivery directions aloud"',
              'Don’t read the instructions, just pause between paragraphs.',
              'Don’t read the stage directions out loud, just pause between paragraphs.')],
    (9, 7): [(2, 'march: round 1 took its one break away ("Allow yourself to notice how it resonates with you" had been its own '
              'sentence); the noticing is its own sentence again',
              'Now say to yourself the phrase you have chosen. Say it as an invitation, and allow yourself to notice how it '
              'is received.',
              'Now say to yourself the phrase you have chosen, as an invitation. Allow yourself to notice how it is '
              'received.')],
    (9, 11): [(2, 'cold read P25: "contact" had been physical in this script ("a contact on your body", "the contact, the '
               'pressure"); the wish is for contact inside', 'your wish for contact.', 'your wish for inner contact.')],
    (11, 3): [(2, 'stance 4: "in my adult body, with my adult experience" ties the adult self to age; the essay keeps adult '
               'capacity apart from chronological age ("Don\'t decide from the person\'s chronological age"; "Those adult '
               'functions still grow through practice"), the inner-adult conflation Joel asked to check for; the published: '
               '"The adult self remains present"',
               'I am here, in my adult body, with my adult experience.', 'I am here, and my adult self stays present.')],
    (11, 2): [(3, 'meaning, part 2, P35: "say out loud where you are" is a new instruction; the published: "Name where you are"',
               'look around and say out loud where you are', 'look around and name where you are')],
    (11, 4): [(2, 'cold read P33: "choose one thing you want to do" and one thing follows; the published: "Once oriented, '
               'choose one intention"', 'choose one thing you want to do:', 'set one intention:')],
    (17, 0): [(3, 'meaning, part 3, and the inner-figure rule of 2026-10-21: "the Adult" with a capital reads as a named part; '
                  'the published: "In inner work, the adult returns, writes, and acts"',
               'where the Adult ultimately needs', 'where the adult ultimately needs')],
    (21, 1): [(3, 'meaning, part 3, P61: the scene is "simple" in the published ("Choose one simple scene"), and "a chair '
                  'where the adult waits" has a lowercase adult (a capital reads as a named part)',
               'Pick an inner scene', 'Pick a simple inner scene'),
              (3, 'the same', 'a chair where the Adult waits', 'a chair where the adult waits')],
    (25, 3): [(3, 'meaning, part 3, P70: the published leads into the statement to say ("Give it the meaning you choose:"); '
                  'the colon makes the next line the thing you say',
               'it means whatever you say it means.', 'it means whatever you say it means:')],
    (25, 5): [(3, 'meaning, part 3, P72: "Return fully" (the published) had become "come back up"',
               'Now come back up and at some point', 'Now come all the way back up and at some point'),
              (3, 'meaning, part 3, P72: "Give it time" was lost', 'You can gradually shorten the longer induction',
               'Give it time: you can gradually shorten the longer induction')],
    (25, 6): [(3, 'meaning, part 3, P73: the check that changing direction stays workable was lost ("turn it on and off" '
                  'covers returning only)',
               'and that it stays away when you haven\'t chosen it.', 'and that it stays away when you haven\'t chosen it. '
               'Can you still change direction while you\'re in it?')],
    (23, 4): [(2, 'cold read P56: "it is \\"True\\"" and "it just might be listening": true about what, and which "it" listens; '
               'the published: "None proves truth. At most, something may be listening"',
               'that doesn\'t mean it is "True" in any way, it just might be listening.',
               'that doesn\'t prove anything is "True", it just means something might be listening.')],
    (25, 8): [(2, 'stance 5: qualified help is for what persists (the published: "Persistent unwanted responses or '
               'disorientation need qualified help"); brief unreality gets grounding in the essay\'s troubleshooting',
               'If you still have the response when you don\'t want it, or you feel disoriented after the state,',
               'If the response keeps coming when you don\'t want it, or you stay disoriented after the state,'),
              (2, 'march: taking out "it is a good start" (an invention) took the paragraph\'s one break; a permission brings '
               'one back, and the published allows a kept cue ("Any retained cue is for a future, separately chosen '
               'session")',
               'If you want to keep it for future use, it\'s only for beginning',
               'If you want to keep it for future use, that\'s fine, but it\'s only for beginning')],
}
LINKS = {7: [{'published': 'Utilization', 'new': 'Utilization'}],
         13: [{'published': 'hypnosis can become more alert rather than more relaxed',
               'new': 'hypnosis can be more alert rather than more relaxed'}],
         17: [{'published': 'Nimja’s sleep playlist', 'new': 'Nimja’s sleep playlist'}]}


def main():
    d = json.loads((HERE / 'HG17.ba.json').read_text(encoding='utf-8'))
    log = []
    for ui, u in enumerate(d['units']):
        if u['kind'] != 'emulate':
            continue
        new = []
        for pi, p in enumerate(u['paras']):
            if (ui, pi) in INSERT:
                why, text = INSERT[(ui, pi)]
                new.append(text)
                log.append({'unit': ui, 'para': pi, 'kind': 'insert', 'points': why, 'new': text})
            if (ui, pi) in DROP:
                log.append({'unit': ui, 'para': pi, 'kind': 'drop', 'points': DROP[(ui, pi)], 'was': p})
                continue
            if (ui, pi) in FIX:
                why, text = FIX[(ui, pi)]
                entry = {'unit': ui, 'para': pi, 'kind': 'fix', 'points': why, 'was': p, 'new': text}
            else:
                text, entry = p, None
            for rnd, finding, old, rep in REVIEWS.get((ui, pi), []):
                assert text.count(old) == 1, ((ui, pi), old)
                round1 = text
                text = text.replace(old, rep)
                if entry is None:
                    entry = {'unit': ui, 'para': pi, 'kind': 'review', 'points': '', 'was': p, 'new': text}
                entry.setdefault('round1', round1)
                entry['new'] = text
                entry.setdefault('reviews', []).append(finding)
                entry.setdefault('rounds', []).append(rnd)
            if entry:
                log.append(entry)
            new.append(text)
        if ui in APPEND:
            why, text = APPEND[ui]
            new.append(text)
            log.append({'unit': ui, 'para': len(u['paras']), 'kind': 'insert', 'points': why, 'new': text})
        u['paras'] = new
        if ui in LINKS:
            u['links'] = LINKS[ui]
        u['fixes'] = ['; '.join([x['points']] * bool(x['points']) + x.get('reviews', [])) for x in log if x['unit'] == ui]
    used = {(x['unit'], x['para']) for x in log if x['kind'] == 'fix'} | set(DROP)
    missing = set(FIX) - used
    assert not missing, missing
    rmissing = set(REVIEWS) - {(x['unit'], x['para']) for x in log if x.get('reviews')}
    assert not rmissing, rmissing
    d['from'] = 'rf-zg/HG17.ba.json (emu-ba over rf-j/HG17.fixed.json), with make_hg17_fixed.py'
    d['note'] = ('every point the second reader found lost put back in ba\'s sentences, its inventions taken out, and the '
                 'changes that alter what a reader does or believes put right (rf-zg/HG17.ba.verify.out.md)')
    (HERE / 'HG17.fixed.json').write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    (HERE / 'FIXES.json').write_text(json.dumps(log, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    old_w = sum(len(p.split()) for u in json.loads((HERE / 'HG17.ba.json').read_text(encoding='utf-8'))['units']
                if u['kind'] == 'emulate' for p in u['paras'])
    new_w = sum(len(p.split()) for u in d['units'] if u['kind'] == 'emulate' for p in u['paras'])
    print(len(log), 'changes;', old_w, '->', new_w, 'words in the Emulate stretches')


if __name__ == '__main__':
    main()
