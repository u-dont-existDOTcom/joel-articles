"""My check of every reader's item in the hypnosis guide's four-part clarity read (2026-10-25), against the whole guide,
Joel's earlier answers (his 3 a of 2026-10-21, his community 64 and 65, lessons E257 and E260) and the InnerSignal
protocol's rules (version 0.2.1, protocol_sha256 1da3ddf06a27aa8409fe953f21e8d9053d943bf383c04d5c561e2e93bb067a27).

Each entry is KEY: (status, pick, note). status "keep" offers the item on its page with my pick; "dup" lists it at the
end because another reader flagged the same words or it is offered on another list; "drop" lists it as not offered,
with the reason. In a note, {Q:KEY} becomes the item's number on question Q's page ("17.4"): 15 is the reread list,
16 the reader's edit, 17 the caveats, 18 the repeats.

Run: python3 articles/inner-signal/humanize/fix-20261025/my_checks.py   (after clarity_read.py collect on each folder)
"""
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[3] / 'tools' / 'humanization'))
import clarity_read  # noqa: E402

QUESTIONS = {15: 'clarity', 16: 'edit', 17: 'caveats', 18: 'repeats'}

EDIT = {
    '1.1': ('keep', 'A', "A reader who skips the V. story, as some will, still finds the rule in the contents. Title case, like its neighbours."),
    '1.2': ('keep', 'A', "The DO and DO NOT lists are the guide's first statement of what it's for and what it isn't; the heading puts them in the contents."),
    '1.3': ('keep', 'B', "The five paragraphs are one argument: the cartoon is wrong, and this is what's true instead, which is what the heading promises."),
    '2.1': ('keep', 'B', "The paragraph under it would open \"I found that especially amplified\", its \"that\" pointing back across the heading."),
    '2.2': ('keep', 'B', "Its first sentence already says who it's for, and it's the same borrowing, used one more way."),
    '2.3': ('dup', '', "On the repeats page as {18:2.4}."),
    '2.4': ('keep', 'A', "The two blame paragraphs are a second subject, and this is the heading you took for the same paragraphs in your inner child guide (91.2 A). The two changes go together."),
    '3.1': ('keep', 'A', "Each label repeats the heading right above it."),
    '3.2': ('keep', 'A', "The guard thread then runs without a break, and the script gets a heading of its own; every later mention of the script still comes after it."),
    '3.3': ('keep', 'A', "In sentence case, like the headings around it: \"Belonging without betraying yourself\"."),
    '4.1': ('keep', 'A', "Your \"First of all\" and \"Secondly\" then open the part that says what to do."),
    '4.2': ('keep', 'A', "Your setup says not to read the directions aloud; the label shows where the words to read start."),
    '4.3': ('keep', 'A', "It's a second technique with its own script; the heading lets a reader find it again."),
    '5.1': ('keep', 'A', "The example then follows the cue it illustrates."),
    '5.2': ('keep', 'A', "Turning the cue off is what a reader with a problem looks for."),
    '5.3': ('keep', 'A', "A shorter heading from your own words would work too: \"Notice or meaning?\"."),
    '6.1': ('keep', 'A', "The urge to move is its own instruction, with its own stop rule."),
    '6.2': ('keep', 'A', "The ending steps then run together, and the note about the whole exercise, with its memory caution, gets a place of its own."),
    '6.3': ('keep', 'A', "The sentence before already gives the permission."),
    '6.4': ('keep', 'A', "The fuller version, with its examples, comes two sentences later."),
    '7.1': ('keep', 'A', "A reader with recurring panic attacks then meets the list that applies to them before the reassurance."),
    '7.2': ('keep', 'A', "It's a rule for the whole practice, not only for work with a clinician."),
    '7.3': ('keep', 'A', "How to enter the app is the one step every app user needs."),
    '7.4': ('keep', 'A', "The survey and the consultation are about the guide as a whole; a reader who skips the app part still finds them."),
    '8.1': ('keep', 'A', "The two examples were left out on purpose: your 3 a of 21 October took the version that read Human, because every wording with them read AI. This cut ends the two references to examples that aren't there."),
    '8.2': ('keep', 'A', "The six steps come first, and the long paragraph becomes their detail."),
    '8.3': ('keep', 'A', "In sentence case, like its neighbours: \"False positives, and turning the cue off\"."),
    '9.1': ('keep', 'A', "The lead-in then sits under its own heading, as the other lead-ins in that appendix do."),
    '9.2': ('keep', 'A', "The appendix then follows its own order, body first and then the inner child, as its script at the end does; the InnerSignal rules put the body and orientation first too. It changes your published order, so it's yours to decide."),
    '9.3': ('dup', '', "On the repeats page as {18:9.3}."),
    '9.4': ('keep', 'A', "The lead-in then sits with the script it introduces."),
    '10.1': ('keep', 'A', "Forgiving yourself is a second subject the contents should show."),
    '10.2': ('dup', '', "On the repeats page as {18:9.7}."),
    '10.3': ('dup', '', "On the repeats page as {18:9.12}."),
    '11.1': ('keep', 'A', "The rule is for the whole practice, not only for suspected psychosis; with the heading, the contents show it."),
    '11.2': ('keep', 'A', "A paragraph break only."),
    '11.3': ('keep', 'A', "It repeats the heading above it."),
}

CAVEATS = {
    '1.1': ('keep', 'B', "This is the line that keeps the stop rule from covering every hard feeling: staying with a feeling while you're present is a choice, and stopping is for losing presence. The InnerSignal rules make the same distinction."),
    '1.2': ('keep', 'B', "How you usually think and what you notice in a given moment are two different things; the InnerSignal rules keep them apart, and this is where the guide does."),
    '1.3': ('keep', 'B', "It stops a reader from taking feelings-first as a rule; the InnerSignal rules say the first thing you notice isn't truer."),
    '1.4': ('keep', 'B', "The InnerSignal rules say the inner-speech question is never a diagnosis, and this line says so where the reader answers it."),
    '1.5': ('keep', 'B', "It's the hinge between your phrase and the study: without it, the study reads as contradicting you."),
    '1.6': ('keep', 'B', "It's the other side of your case for doing it yourself (what a guide adds), and a reader deciding whether to get one needs it."),
    '1.7': ('keep', 'B', "Without it, the extended chrunga trip reads as a recommendation."),
    '1.8': ('keep', 'B', "It's the one place the guide says the Higher Self frame is optional; the InnerSignal rules never make spirituality a requirement."),
    '2.1': ('keep', 'A', "\"Three aspects\" and \"It's you that needs to develop these qualities\" already say they're one person."),
    '2.2': ('keep', 'B', "It says where borrowed adulthood stands, untested: a limit on relying on it, the kind you kept in your community article (64.3)."),
    '2.3': ('keep', 'B', "It makes a point of its own (the positions you're telling apart may not be ages), which \"It can be any age\" doesn't."),
    '2.4': ('keep', 'A', "The heading right above says it."),
    '2.5': ('keep', 'A', "The one change that matters, a signal or a feeling instead of part work, stays."),
    '3.1': ('keep', 'A', "\"One way of explaining this\" already says it's a way of looking."),
    '3.2': ('keep', 'A', "The next paragraph says \"Using metaphors and imagery is entirely optional.\""),
    '3.3': ('keep', 'B', "It's the rule that the containment step is for getting your bearings, not for going deeper when you're unstable. Your published guide said it (\"not permission to intensify an unstable state\"), and the InnerSignal rules hold it."),
    '3.4': ('keep', 'B', "It's the consent rule just before the reader starts: your no holds, and saying nothing isn't a yes. Your published guide had it here."),
    '3.5': ('keep', 'B', "It's a writing instruction: keep the stop and exit words plain even when the rest of your script uses the language of Appendix B."),
    '3.6': ('keep', 'B', "It's part of the script: the built-in way out that your own de-hypnosis section says every script needs."),
    '4.1': ('keep', 'B', "It's the other side of your dad's story, which has him doing it while driving."),
    '4.2': ('keep', 'B', "It's the permission at the moment of use; \"Be able to change directions\" later is a test of the cue."),
    '4.3': ('keep', 'B', "Readers who know hypnosis expect a trigger to need repetition and depth; this tells them it doesn't."),
    '4.4': ('keep', 'B', "It's the branch the rest of the paragraph turns from (\"For now, though\"), and the heading on the reader's-edit page names it."),
    '4.5': ('keep', 'A', "The reader has just done the induction and the meeting, and the next sentence is the instruction."),
    '4.6': ('keep', 'A', "The next sentence gives the same permission, with its condition."),
    '4.7': ('keep', 'B', "It tells a reader not to put themselves at risk to test another person; the InnerSignal rules count that kind of protection as part of the work."),
    '4.8': ('keep', 'A', "The sentence before says it."),
    '4.9': ('keep', 'A', "\"Find out if there is anything that you need to do\" already allows for nothing."),
    '4.10': ('keep', 'B', "It's the guide's plainest line that an image isn't a memory; with hypnosis and false memories, the InnerSignal rules keep this wherever images come up."),
    '4.11': ('keep', 'A', "\"Fifteen minutes or so\" already makes it loose."),
    '4.12': ('dup', '', "The reader's-edit page's {16:6.3} cuts only the second line, which I pick."),
    '5.1': ('keep', 'A', "The NOTE at the top of the section says it."),
    '5.2': ('keep', 'B', "It's the crisis list where an anxious reader is: chest pain and fainting can be medical, and \"wanting to hurt yourself or somebody else\" is only here and in Appendix H."),
    '5.3': ('keep', 'A', "The first line of the list says to reality-test every inner experience."),
    '5.4': ('drop', '', "not offered: the guide teaches NLP in Appendix B, and this is the main guide's one warning about it"),
    '5.5': ('keep', 'A', "The heading says it, and the next paragraph gives the instruction."),
    '5.6': ('keep', 'A', "The two sentences before already say to get help now, or promptly."),
    '5.7': ('keep', 'A', "The aside could read as a go-ahead for regression on your own when it isn't about trauma, which the guide doesn't teach."),
    '5.8': ('keep', 'B', "It's the app's promise about the reader's medium, and the InnerSignal rules make it a rule: a drawing or a song counts without being turned into prose."),
    '5.9': ('keep', 'B', "It says what the app is and isn't; the InnerSignal rules keep that role plain."),
    '6.1': ('keep', 'A', "\"You can skip this section and just use the main path\" already says it."),
    '6.2': ('keep', 'A', "It comments on the prompt; the reader can see it's longer."),
    '6.3': ('keep', 'B', "It separates how you ask from whether the answer is true, as the appendix's last word on prompts."),
    '6.4': ('keep', 'A', "The warning that follows is the caution."),
    '6.5': ('keep', 'A', "If {17:6.5} to {17:6.8}, {17:6.10} and {17:6.12} all go, the paragraph reads: \"Synchronicity cues do not authorize you to make a decision. They do not stop you from hearing the message of your intuition if it is warning you about something.\" The first \"They\" becomes \"Synchronicity cues\", the one change the cuts make necessary."),
    '6.6': ('keep', 'A', "\"What not to do\" already says not to put hidden commands in yourself, and to know exactly what you're doing."),
    '6.7': ('keep', 'A', "Said below, with how."),
    '6.8': ('keep', 'A', "The step above gives the cue's job."),
    '6.9': ('keep', 'B', "A limit said nowhere else: the cue is no reason to decide."),
    '6.10': ('keep', 'A', "Said twice just above, and \"isn't proof\" is the phrase you flagged as an AI pattern (64.23)."),
    '6.11': ('keep', 'B', "It says where the not-proof rule stops: a cue doesn't silence a real warning."),
    '6.12': ('keep', 'A', "\"What not to do\" already says not to let anyone activate a cue in you."),
    '7.1': ('keep', 'A', "The NOTE gives the exact limits."),
    '7.2': ('keep', 'B', "It tells a reader with an anxiety disorder that better-tested treatments exist, the full picture (your 64.28). If you'd rather, only \"So use the evidence with caution, and\" could go."),
    '7.3': ('keep', 'B', "Physical safety: the front of the neck, varicose veins and injuries are places where massage can harm, and \"get a massage\" doesn't say where."),
    '7.4': ('keep', 'A', "\"But neither one of those products are necessary\" is already the other side, and \"neither proves\" is the \"isn't proof\" pattern you flagged."),
    '7.5': ('keep', 'A', "The sentence before lays out the choices."),
    '7.6': ('keep', 'B', "It's the hardening half of the line before (\"we aren't expecting something from someone that they can't give\"), like your 64.8."),
    '7.7': ('keep', 'B', "Without it, the paragraph about using substances reads as a recommendation."),
    '7.8': ('keep', 'B', "In altered states, using trance to skip sleep or medical care is a real risk, and this list is where that reader is."),
    '7.9': ('keep', 'B', "It's the test by outcome (are you more loving, grounded, able to sleep?) and the step to integrate instead of going deeper; the line before only says what not to use it for."),
    '8.1': ('keep', 'A', "The heading says it, and the appendix opens with it."),
    '8.2': ('dup', '', "The repeats page's {18:9.12} cuts only the first two sentences and keeps the last, which says the heading's point; I pick that."),
    '8.3': ('keep', 'A', "\"What not to do\" already says nothing is healed in the body because it's healed in your imagination."),
    '8.4': ('keep', 'B', "It's the guide's one plain statement of where the method stands, not a validated treatment: a limit a reader needs."),
    '8.5': ('keep', 'A', "Nobody consults a reading list mid-practice."),
    '8.6': ('keep', 'B', "Your published guide said what it means: the 1995 book's case procedures and historical claims shouldn't be brought wholesale into solo practice."),
    '8.7': ('keep', 'B', "It says nimja didn't write or endorse the guide, which a reader of your sources should know; the reread list splits the same sentence in three."),
    '8.8': ('keep', 'A', "\"What not to do\" says it for the whole guide."),
    '8.9': ('keep', 'A', "\"This isn't a diagnosis\", in the section itself ({17:1.4}, which I keep), says it where the questions are."),
    '8.10': ('keep', 'B', "It's the sourcing limit: the links back their own claims, not every use of hypnosis."),
}

REPEATS = {
    '1.1': ('keep', 'B', "It's the introduction's statement of the method, the thesis up front, which your 65 kept."),
    '1.2': ('keep', 'B', "It's the line that sends Quick start readers to the induction and the return before their first session."),
    '1.3': ('keep', 'A', "Before you begin, which the reader reads with the induction, has it as step 2."),
    '1.4': ('keep', 'A', "The marketers paragraph and the Silva line say it just above."),
    '1.5': ('keep', 'B', "With the DO line above it, it's the guide's first statement of what it's for and what it isn't (the reader's edit gives the pair a heading, {16:1.2})."),
    '1.6': ('keep', 'B', "The four consequences (sterile, fantasy, delusions, dead) are new here."),
    '1.7': ('keep', 'B', "It adds your example (the breast implants) and the link between religious fear and shame."),
    '1.8': ('keep', 'A', "The return is told step by step in Come all the way back, and at the end of every induction."),
    '1.9': ('keep', 'B', "It's the longer version the earlier section points to (\"see appendix C for a longer version\"), with your police joke."),
    '1.10': ('keep', 'B', "It's Appendix F's own premise, which \"That said\" in the next paragraph answers."),
    '2.1': ('dup', '', "Same cut as {18:1.1}."),
    '2.2': ('dup', '', "On the caveats page as {17:1.8}."),
    '2.3': ('keep', 'A', "It sums up the three steps the section before gives in full."),
    '2.4': ('keep', 'B', "Its list pairs with the list of what you leave behind, and three of its items (curiosity, spontaneity, feeling easily) are new."),
    '2.5': ('keep', 'A', "The two paragraphs above give the hands, and the induction's script says \"Love above, Child below, Adult present\"."),
    '2.6': ('keep', 'A', "The part opens with it: \"What's going to help your inner child to trust you is you, the person you are right now, becoming reliable.\""),
    '2.7': ('keep', 'B', "It's the rule not to redo a step you can already do, where the reader is doing the practice; the InnerSignal rules say the same."),
    '2.8': ('keep', 'B', "In troubleshooting the reader is in the middle of the problem: who to borrow from and what to borrow make the step usable without going back."),
    '2.9': ('keep', 'B', "It's for working with someone else, where splitting the three and bringing them back together is the step."),
    '3.1': ('keep', 'B', "It lets a reader drop parts language when it makes them feel more divided; the InnerSignal rules use parts only while they help."),
    '3.2': ('keep', 'B', "It's the checklist's main symptom, and the checklist is how a reader tells whether they're \"in this camp\"."),
    '3.3': ('keep', 'A', "The line above asks it, and the second list asks it again."),
    '3.4': ('keep', 'B', "It gives the reason (a child needs the family to survive) and the list of groups; the reader's edit also puts a heading above this paragraph ({16:3.3})."),
    '3.5': ('keep', 'B', "Readers who skip the appendices need a list here, and it has signs Appendix C lacks (FOMO, destiny, confusion, certainty too quickly, one good question)."),
    '3.6': ('keep', 'B', "Here it's a sign of manipulation in someone else's recording; in Come all the way back it's your own rule."),
    '3.7': ('dup', '', "On the caveats page as {17:3.4}."),
    '3.8': ('keep', 'A', "It's the resistance prompt's two questions, a few lines up."),
    '3.9': ('keep', 'B', "It's the script you say to yourself, and not obeying and not attacking are its core."),
    '3.10': ('keep', 'B', "It's the definition a reader who goes straight to the anxiety appendix needs."),
    '3.11': ('keep', 'B', "Each induction in the library stands on its own; the reread list glosses \"good as you\" here."),
    '4.1': ('dup', '', "Same as {18:1.2} and {18:1.3}."),
    '4.2': ('keep', 'A', "The Already open section, where the reader goes next, gives the list in full."),
    '4.3': ('keep', 'B', "It's the only place the target state is described (focused, warm, receptive, embodied, able to stop)."),
    '4.4': ('dup', '', "On the caveats page as {17:3.4}."),
    '4.5': ('keep', 'B', "It's the principle a reader needs before their first induction, which comes before \"Let the next response guide you\"."),
    '4.6': ('keep', 'B', "It adds \"keep it kind\", and it's the line the reader tells themselves."),
    '4.7': ('dup', '', "On the caveats page as {17:4.2}."),
    '4.8': ('keep', 'B', "This is the cue a reader uses in daily life (your dad used his while driving), and the paragraph adds that open eyes and permissive wording don't make it safe."),
    '4.9': ('keep', 'A', "Appendix E, the daydream appendix, and Stay awake both give it."),
    '4.10': ('dup', '', "Covered by {18:8.5} and {18:8.6}."),
    '4.11': ('keep', 'B', "It's the daydream appendix's own script, where the topic lives."),
    '5.1': ('dup', '', "The same place as {18:3.6}."),
    '5.2': ('dup', '', "Same as {18:4.5}."),
    '5.3': ('keep', 'A', "The bring-back script says it right below."),
    '5.4': ('keep', 'B', "\"Only what actually came up\" is part of the return, which readers use with every practice."),
    '5.5': ('keep', 'B', "It gives the three-part frame (the notice, the meaning, your thoughts on the meaning) and the next paragraph gives the example; the InnerSignal rules keep the notice and the meaning apart."),
    '5.6': ('dup', '', "Same as {18:2.7}."),
    '5.7': ('dup', '', "On the caveats page as {17:4.10}."),
    '5.8': ('keep', 'B', "It's the follow-up step for the if-then plan."),
    '5.9': ('dup', '', "Same as {18:1.8}."),
    '6.1': ('dup', '', "Same as {18:1.5}."),
    '6.2': ('dup', '', "Same as {18:4.8}."),
    '6.3': ('dup', '', "On the caveats page as {17:4.10}."),
    '6.4': ('dup', '', "Same as {18:2.8}."),
    '6.5': ('keep', 'B', "It's the main guide's instruction; the script is in an appendix many readers won't reach."),
    '6.6': ('dup', '', "On the caveats page as {17:5.2}."),
    '6.7': ('keep', 'A', "The prompt just before calls silence a successful answer, and \"The subconscious will not answer\" has it."),
    '6.8': ('keep', 'A', "The clarity prompt above ends on the same sentence."),
    '6.9': ('keep', 'B', "It's for altered states, where making yourself more afraid, skipping sleep and becoming less communicative are risks the main list doesn't name."),
    '6.10': ('dup', '', "On the caveats page as {17:7.9}."),
    '6.11': ('keep', 'B', "It names the warning signs (paranoid, sleepless, grandiose, isolated, scared, unreal) and says GET HELP; the reader's edit gives it a heading ({16:11.1})."),
    '7.1': ('keep', 'B', "It's the closing: the guide's argument in one line, where the reader ends."),
    '7.2': ('dup', '', "Same as {18:6.7}."),
    '7.3': ('dup', '', "Same as {18:4.9}."),
    '7.4': ('dup', '', "Same as {18:3.8}."),
    '7.5': ('dup', '', "Same as {18:6.8}."),
    '7.6': ('keep', 'B', "It's the bridge from the prompts to the NLP appendix, with the limit that keeps it honest."),
    '7.7': ('keep', 'B', "It shows which words of the example make each move; the reread list points each label at its words."),
    '7.8': ('dup', '', "Same as {18:6.11}."),
    '8.1': ('dup', '', "Same as {18:3.5}."),
    '8.2': ('keep', 'B', "It adds \"not a peak state\", the opposite of the usual NLP advice."),
    '8.3': ('dup', '', "The reader's edit moves it to the top instead ({16:8.2})."),
    '8.4': ('dup', '', "On the caveats page as {17:6.10}."),
    '8.5': ('keep', 'A', "\"By not rehearsing them anymore\" says it two sentences later."),
    '8.6': ('keep', 'B', "It's the limit on this cue's own off-switch: deciding doesn't make the association go at once."),
    '8.7': ('keep', 'B', "It's your own vow, in the first person; Appendix C describes what a bad guide does."),
    '8.8': ('dup', '', "Same as {18:2.9}."),
    '8.9': ('keep', 'B', "The audit is the checklist to use before accepting a recording, and Appendix C is where it belongs."),
    '8.10': ('keep', 'B', "As {18:8.9}."),
    '8.11': ('keep', 'B', "As {18:8.9}."),
    '8.12': ('dup', '', "Same as {18:3.10}."),
    '9.1': ('dup', '', "Same as {18:6.5}."),
    '9.2': ('dup', '', "Same as {18:4.9}."),
    '9.3': ('keep', 'A', "It lists again what the paragraph before lists; only \"a favorite object\" and \"technology you use to relax\" are new."),
    '9.4': ('keep', 'B', "It's the appendix's own step for when the daydream is taking you away."),
    '9.5': ('dup', '', "Same as {18:1.10}."),
    '9.6': ('dup', '', "On the caveats page as {17:7.6}."),
    '9.7': ('keep', 'A', "The next sentence gives the same steps in full."),
    '9.8': ('dup', '', "Same as {18:6.9}."),
    '9.9': ('dup', '', "On the caveats page as {17:7.9}."),
    '9.10': ('keep', 'B', "It's the words a reader needs at the moment a hostile presence shows up."),
    '9.11': ('dup', '', "On the caveats page as {17:8.1}."),
    '9.12': ('keep', 'A', "The paragraph two above says both. The last sentence stays, with the heading's point that how it responds doesn't prove what it is."),
    '10.1': ('keep', 'B', "It's the main guide's one practical pointer for sleep."),
    '10.2': ('keep', 'B', "\"What not to do\" is for readers who don't reach the appendices; the reread list glosses the term here."),
    '10.3': ('dup', '', "On the caveats page as {17:8.1}."),
    '10.4': ('dup', '', "Same as {18:9.12}."),
    '10.5': ('keep', 'A', "\"The door is closed\" says it just before."),
    '10.6': ('keep', 'B', "It's the other side of \"not sentimental love\": love that keeps the boundary, the section's point."),
    '10.7': ('dup', '', "Same as {18:6.11}."),
    '10.8': ('keep', 'B', "It's the only line with \"humble\", the test's name."),
    '10.9': ('keep', 'B', "The induction library's own instruction; the reader's edit splits this paragraph ({16:11.2})."),
    '10.10': ('dup', '', "Same as {18:3.11}."),
    '10.11': ('dup', '', "On the caveats page as {17:8.5}."),
}

# The reread list: KEY -> dict of the fields my check sets ("status": keep, minor, drop or dup; "my_score"; "note";
# "check" where a plainer version guesses at his reasoning; "plain" where mine replaces the reader's). Part 1 was read in
# two halves, READER-7 and READER-8, after its first reader ran out of output (E255 again).
CLARITY = {
    '2.1': {'my_score': 3, 'note': 'Your published guide had the words in quotes ("“Stop” ends the exercise; “less” reduces the demand; “quiet” stops the words.").'},
    '2.2': {},
    '2.3': {'note': 'The line stays on the caveats page ({17:3.4}); this only glosses the narrator.'},
    '2.4': {'check': 'The second gloss guesses at your joke ("That is why you are reading a self hypnosis guide!"); if it is a joke, leave it and use only the first gloss.'},
    '2.5': {'status': 'minor', 'note': 'the Protector is introduced in "The inner child, the guards, and the inner adult’s three jobs"; only "installed parental" might stop a reader'},
    '2.6': {}, '2.7': {},
    '2.8': {'plain': 'skip straight to the orientation/containment part (the section "Already open? Contain before you deepen", below) rather than going deeper.', 'plain_by': 'mine'},
    '2.9': {}, '2.10': {},
    '2.11': {'status': 'dup', 'note': 'cut on the caveats page ({17:3.1}), my pick'},
    '2.12': {},
    '3.1': {'plain': 'Sometimes the invitation just isn’t right - sometimes the reaction is about something you hadn’t thought of. Neither case is automatically a protector, and just being silent doesn’t mean there’s a process (that something hidden is working).', 'plain_by': 'mine',
            'note': 'From your published version: "Skepticism is not automatically a protector, and silence is not proof that a hidden process is working."'},
    '3.2': {'plain': 'You don’t have to talk to them, just use the one whose job you need, and if you can’t do it yet, borrow it. You only need to use the “Witness” (just noticing what’s there, as in "When the adult role is not available yet") if you need help getting started with a step.', 'plain_by': 'mine'},
    '3.3': {'my_score': 2}, '3.4': {}, '3.5': {},
    '3.6': {'plain': 'however if you are coming out of a recording (rather than going to sleep to it) then you should not leave yourself in an altered state. This includes leaving yourself in a role, with lowered judgment, with lowered ability to move, blank, with a non-specific reset word (a cue left in place without saying exactly what it does) or for an indefinite length of time.', 'plain_by': 'mine',
            'check': 'The gloss reads "non-specific reset word" as a cue left in place without saying what it does (your published guide says "an undefined reset word"); check it is what you mean.'},
    '3.7': {},
    '3.8': {'plain': 'Choose a sound, or a contact, or the two hands thing (below) or something to anchor yourself (something to come back to when your mind wanders), and the thing you will say to open it up (your opening phrase). Use the same anchor for everywhere that anchor is mentioned (each time the script says "your anchor").', 'plain_by': 'mine',
            'note': 'Your published guide: "Choose one anchor ... and an opening phrase."'},
    '3.9': {},
    '3.10': {'status': 'minor', 'note': 'if the reader’s-edit move goes in ({16:5.1}), the cue is introduced before this line and the snag goes'},
    '3.11': {}, '3.12': {},
    '4.1': {'status': 'drop', 'note': 'each term is explained in its own pattern right after it (Patterns 1 to 10)'},
    '4.2': {'my_score': 2},
    '4.3': {'plain': 'Listen to the kid for as long as it takes until it’s comfortable enough to move closer to you.', 'plain_by': 'mine',
            'note': 'Your published closing: "Listen until the kid is willing to come closer."'},
    '4.4': {},
    '4.5': {'plain': 'DO NOT: Engage in seeking "downloads" of information (messages that seem to arrive from beyond you) or make a hobby of demons/jinn/Unattached Burdens (see Appendix H) or the like, until you have stabilized your life.', 'plain_by': 'mine'},
    '4.6': {}, '4.7': {}, '4.8': {},
    '4.9': {'status': 'minor', 'note': 'the guard is introduced in "Working with childhood protector parts", and "You don’t have to let me in" two sentences later says which one'},
    '4.10': {},
    '4.11': {'check': 'The gloss says what the "ordinary evidence" is evidence of; your published guide says "what ordinary evidence would make the new adult voice more believable", so check the gloss fits.'},
    '4.12': {},
    '5.1': {'my_score': 2, 'plain_by': 'mine', 'plain': 'There are many ways to make an anchor (a touch, word or movement you pair with a good state, so that doing it later brings the state back). ... Feel something that you have got to in reality (a good state you are actually in right now) that you want to be able to get to easily when you need to. Do your anchor thing and say to yourself that this state is available to you. Do make sure you do it when you have clearly got the state. To get yourself back into a good hypnosis state easily, dont go for a peak state (the most intense one) but for a good hypnotic state. ... Do make sure this is different from both your alert and calm cue (the relaxation/stay alert cue in "A shortcut back into hypnosis") and your synchronicity wake up cue.'},
    '5.2': {'status': 'dup', 'note': 'the reader’s edit ends the two references instead ({16:8.1}), since your 3 a of 21 October left the examples out'},
    '5.3': {'my_score': 2, 'plain_by': 'mine', 'plain': 'You might even be able to use the Inner Signal app or ask around to see if someone can tell you what the things they did meant. Whoever you ask probably won’t be able to tell you if the person was "certified" in them or not, though.'},
    '5.4': {},
    '5.5': {'note': 'Your published guide defined it ("These are questions whose ordinary conversational form also acts as an invitation."); the version you installed on 21 October (3 a) doesn’t, and a definition here may read AI, as the embedded-invitation one did then.'},
    '5.6': {'note': 'Your 3 a of 21 October took the version without the definition ("An embedded invitation places a small direction inside a larger sentence. ..."), because with it the stretch read AI; a shorter gloss may too.'},
    '5.7': {},
    '5.8': {'status': 'minor', 'note': 'the three are introduced in "The inner child, the guards, and the inner adult’s three jobs"; only a reader who starts in Appendix B misses them'},
    '5.9': {'status': 'minor', 'note': 'the guard is introduced in the main guide ("Working with childhood protector parts")'},
    '5.10': {}, '5.11': {},
    '5.12': {'plain_by': 'mine', 'plain': 'Here is a rough outline of the NLP (Neuro-Linguistic Programming) tools and techniques I use: Perceptual Positions : 1) seeing from Self (my own eyes), 2) then seeing from Other (the other person’s eyes), 3) then seeing from Witness (an onlooker with no stake), and 4) then seeing from Universal Heart (the Higher Self you start from).'},
    '6.1': {'my_score': 2},
    '6.2': {'note': 'Your published guide says the reader’s guess: "Having experienced love once, being able to access it only in a particular state, and contacting it reliably in daily life are different things."'},
    '6.3': {'plain_by': 'mine', 'plain': 'Come back, keeping the quality and one positive action that you would do with it, but leaving the "person" behind (the role you took on to feel the quality), saying "I am me".', 'note': 'Your published guide: "release the role".'},
    '6.4': {'plain_by': 'mine', 'plain': 'Try to avoid any language that makes you not one person (that makes you feel split up). ... Goal is to make it "good as you" (more supported and connected to yourself), not to erase history.',
            'note': 'From your published "choose language that doesn’t make you feel fragmented", and your own gloss of "good as you" in "Don’t rush the repair".'},
    '6.5': {},
    '6.6': {'plain_by': 'mine', 'plain': 'In Hearthwork (my peer counseling method), the concept is that you give each other equal time, warmth, confidentiality, and acceptance of “no” as an answer, and you act for each other as Nurturer and Protector, but not as Guide.', 'note': 'The three roles are introduced in the main guide; only Hearthwork needs a word.'},
    '6.7': {'status': 'minor', 'note': 'in your post the link below it is the card for your Trip-Sitting guide (medical triage, shadow work, therapy), which is how the question gets answered'},
    '6.8': {'status': 'minor', 'note': 'glossed at its first use, in "What not to do", on this list'},
    '6.9': {},
    '6.10': {'plain_by': 'mine', 'plain': 'Any of these ‘families’ of induction can be done as light inductions, with eyes open, or instead of trance you can just do them as a contact (inner contact without trance, as in number 9).'},
    '6.11': {},
    '6.12': {'status': 'minor', 'note': 'loveyhuasca is a link to your page at its first use; the snag is the tail "etc, etc, etc around plant medicine" (your published guide: "or other plant-medicine-adjacent states")'},
    '7.1': {}, '7.2': {'my_score': 2}, '7.3': {},
    '7.4': {'status': 'minor', 'note': 'only a missing comma and "the" ("and mind you, the deeper mind is still running"); the gloss of fantasy mind would be a guess'},
    '7.5': {}, '7.6': {}, '7.7': {},
    '7.8': {'note': 'The line stays on the caveats page ({17:1.2}); this only untangles the double negative.'},
    '7.9': {},
    '7.10': {'check': 'The gloss would add a claim of your own (that V. is one of the elites); only you can say whether to spell it out.'},
    '7.11': {},
    '8.1': {'my_score': 2, 'note': 'Your published guide: "handing adult judgment to an outside caretaker".'},
    '8.2': {'status': 'minor', 'note': 'the a), b) and c) steps right after it show what each means'},
    '8.3': {'plain_by': 'mine', 'plain': 'Or are you blending them? It might not be chronological age (which position is which isn’t decided by your age).', 'note': 'From your published "Don’t decide from the person’s chronological age."'},
    '8.4': {'my_score': 2, 'plain_by': 'mine', 'plain': 'I found that (the trust and precision of doing it myself) especially amplified with loveyhuasca.', 'note': 'loveyhuasca is a link to your page, so only the "that" needs anchoring.'},
    '8.5': {},
    '8.6': {'status': 'drop', 'note': 'chrunga is a link to your chrunga page'},
    '8.7': {'check': 'Why it matters is yours to say; your published guide had only "I find that phenomenologically important."'},
    '8.8': {'status': 'minor', 'note': 'your Introduction’s "warm up to what’s there, protect it, clarify what it is" is the same three'},
    '8.9': {}, '8.10': {'status': 'minor', 'note': 'the guide says how they correct each other in "Forget the left-brain/right-brain cartoon"'},
    '8.11': {'plain_by': 'mine', 'plain': 'This is a borrowed figure, so you’re still making the choice (it stays beside your judgment instead of replacing it).', 'note': 'From your published "The borrowed figure stays beside your judgment rather than replacing it."'},
    '8.12': {'status': 'minor', 'note': '"positions" comes earlier in the same part ("different internal positions", "your witnessing position")'},
}

TABLES = {16: EDIT, 17: CAVEATS, 18: REPEATS}


def load(q):
    return json.loads((HERE / QUESTIONS[q] / 'ITEMS.json').read_text(encoding='utf-8'))


def apply(tables):
    items = {q: load(q) for q in tables}
    for q, table in tables.items():
        keys = {x['key'] for x in items[q] if x.get('by') != 'mine'}
        missing, extra = keys - set(table), set(table) - keys
        assert not missing and not extra, (q, sorted(missing), sorted(extra))
        for x in items[q]:
            if x['key'] not in table:
                continue
            if isinstance(table[x['key']], dict):   # the reread list
                for k, v in table[x['key']].items():
                    x[k] = v
                continue
            status, pick, note = table[x['key']]
            x['status'] = status
            if pick:
                x['my_pick'] = pick
            else:
                x.pop('my_pick', None)
            x['note'] = note
    nums = {q: clarity_read.numbers(items[q]) for q in items}
    def resolve(m):
        q, key = int(m.group(1)), m.group(2)
        if q not in nums or key not in nums[q]:
            raise KeyError('%s:%s is not offered on its page' % (q, key))
        return '%d.%d' % (q, nums[q][key])
    for q in items:
        for x in items[q]:
            if x.get('note'):
                x['note'] = re.sub(r'\{(\d+):(\d+\.\d+)\}', resolve, x['note'])
        (HERE / QUESTIONS[q] / 'ITEMS.json').write_text(json.dumps(items[q], ensure_ascii=False, indent=1) + '\n',
                                                        encoding='utf-8')
    return items, nums


if __name__ == '__main__':
    tables = dict(TABLES)
    if CLARITY:
        tables[15] = CLARITY
    items, nums = apply(tables)
    for q in sorted(items):
        it = items[q]
        live = [x for x in it if x.get('status', 'keep') == 'keep']
        print(q, QUESTIONS[q], len(it), 'items:', len(live), 'offered,',
              sum(1 for x in live if x.get('my_pick') == 'A'), 'A,', sum(1 for x in live if x.get('my_pick') == 'B'), 'B;',
              sum(1 for x in it if x.get('status') == 'dup'), 'dup,', sum(1 for x in it if x.get('status') == 'drop'), 'drop')
