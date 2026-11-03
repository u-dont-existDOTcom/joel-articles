"""Fix what my own read of the whole guide found (FINDINGS.json, 122 findings), and record each finding's fate.

Joel, 2026-10-30 14:35 UTC, on his cards: ""in waking life" was an error ... make sure we dont' ahve other errors like
that", "looks like you need to read everything again yourself (not sonnet)", "we should be ADDING clarity, not losing it",
"you're not using commas in many places they belong", "Let's make sure we aren't giving people exercises over and over".
So the lead model read all 21 parts beside his published version (READER-1..21.md), and this script puts in the fixes:

- Our words (Emulate's, the writers', mine, and the stretch he passed through on 25 October when he fixed Emulate's
  quote marks, card EM-Q1: there he changed only quote marks, one capital, one sentence and "protectors"): fixed here,
  each fix the smallest that makes the sentence say what his published version says, in the voice around it.
- His own versions (a card he rewrote, word for word): never changed here. They go on his next cards page with my
  suggestion beside them (CARDS below), or are his call and left (FATES).
- A finding that isn't a problem once checked against the whole guide and his history (FATES, with the reason).
- The two-hand exercise, taught four times (E297): taught once, in "The two-hand practice"; the induction and the
  troubleshooting line name it instead of teaching it again; Appendix D's (his version) goes on his cards page.
- Appendix C's "any of the following" list, which his audit comment asked me to try with his fix (uncompress the list,
  explain, and a bridge that sounds different): rewritten here, in our words, for the recheck to test.
- Tells he named on 30 October (O42 "quietly", O43 "proof", O46 "one small", O47 "silently", O48 passive voice),
  where they were in our words (the linter's whole-guide run; uses that say how a sound is made, or where proving
  is the subject, stay).

  python3 articles/inner-signal/humanize/fix-20261030/fullread/apply_fullread.py [--check]

It runs on the guide as it was before the fixes (BEFORE_SHA, commit d24bd21a's HUMANIZED-SO-FAR.md; to run it again:
git show d24bd21a:articles/inner-signal/humanize/HUMANIZED-SO-FAR.md > articles/inner-signal/humanize/HUMANIZED-SO-FAR.md),
and makes the guide at 975fdb3c.

Writes HUMANIZED-SO-FAR.md, APPLIED-FULLREAD.json (every changed paragraph before and after, with its findings) and
DISPOSITIONS.json (every finding's fate, for compare_read.py record).
"""
import argparse
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
import suggestion_review as sr  # noqa: E402
from apply_answers import set_block_text  # noqa: E402

GUIDE = H / 'HUMANIZED-SO-FAR.md'
BEFORE_SHA = 'd97ac3ad820e4f4caa8e591595ee50d4a87a349a96a607ecc782a71d6786ae05'

# (findings, block, old words or None for the whole paragraph, new words)
EDITS = [
    (['F1.1'], 11, None,
     'Yet no one taught those layers to talk to each other. Instead you were taught (or you figured out) that the way to '
     'grow up and be an adult is to push through, repress, suppress, pretend you’re confident, follow authority, go '
     'against authority, etc etc etc. And mind you, the deeper mind is still running all of the programs it’s running: '
     'the child mind wanting to feel safe, the guard mind bracing for danger (childhood protector parts, the protective '
     'reactions learned as a child), the body mind remembering what your intellect explained away, the intuitive mind '
     'speaking up before you have the words, and the fantasy mind trying to become guidance mind, etc etc.'),
    (['F1.2'], 12, 'until they can all be heard.',
     'until they can all be heard, without any of them grabbing the microphone.'),
    (['O47'], 23, 'can you make yourself think in words, silently?', 'can you make yourself think in words?'),
    (['F1.8'], 31, 'Even when not actively engaging the conscious mind, there are many ways to influence people.',
     'There are many ways to influence people that never go through their conscious mind.'),
    (['F1.10'], 35, 'With self-hypnosis you can train your own mind from the inside,',
     'Ads, screens, fear and cravings are already training your mind, and so are your tribe, the people in authority, '
     'loneliness and plain old repetition. With self-hypnosis you can train your own mind from the inside,'),
    (['F2.1'], 51, 'In 2024 there has been an overview', 'In 2024, there was an overview'),
    (['F2.2'], 52, 'pain, childbirth, pediatric, stress, anxiety etc.', 'pain, childbirth, children, stress, anxiety etc.'),
    (['F2.3'], 55, 'may invoke strong emotions', 'may bring up strong emotions'),
    (['F2.5'], 61, 'The imagination can have opened up the field and then the adult can choose what to do next in the real '
     'world….', 'The imagination can open up the field, and then the adult can choose what to do next in the real world.'),
    (['F2.4'], 62, 'Without the mind of love the mind of analysis can be sterile. Without the mind of analysis the mind of '
     'love can lead to fantasy. Without testing intuitive signals they can become delusions. Without intuitive signals '
     'the testing can be dead.',
     'Without the mind of love, the mind of analysis can be sterile. Without the mind of analysis, the mind of love can '
     'lead to fantasy. Without testing, intuitive signals can become delusions. Without intuitive signals, the testing '
     'can be dead.'),
    (['F2.6'], 73, 'and it feels like if I needed to I could have continued',
     'and it felt like, if I needed to, I could have continued'),
    (['F2.7'], 73, "I'm not recommending that anyone prolong an altered state forever, because it's better to integrate, etc.",
     "I'm not recommending that anyone prolong an altered state forever, though. It's better to integrate it into your "
     "life than to try to live inside it."),
    (['F3.1'], 77, None, 'Working with parts gives you precision, and working with the Higher Self gives you coherence. '
     'Communion is going back and forth between the two.'),
    (['F3.2'], 80, None,
     'If you need to work with the ecology in the subconscious, notice what each part wants: the child parts usually want '
     'love, the guards want you safe, the critic wants you to meet some standard, the fantasy making parts are after '
     'possibility, body memories want to be recognized, the social part wants to belong, the spiritual part wants God or '
     'source or what’s best for all beings, and the wiser part just wants what’s true. Then:'),
    (['F3.3'], 82, 'Which part wants to avoid it?', 'Which part wants to avoid the whole thing?'),
    (['F3.4'], 98, 'If you have a safe adult in your life you can borrow from them, if not borrow from a mentor, older '
     'brother/sister, imagine your future self,',
     'If you have a safe adult in your life, you can borrow from them. If not, borrow from a mentor, an older '
     'brother/sister, your imagined future self,'),
    (['F3.6'], 99, None, 'Next, put on your adult hat as if you are an apprentice adult, and pick the words or the action '
     'yourself. Then do at least part of it.'),
    (['F3.7'], 103, 'and not knowing what a decent adult would do', 'and don’t know what a decent adult would do'),
    (['F3.8'], 103, 'You may still feel young when you do it, it’s okay, feeling like an adult can come after you act like '
     'one.', 'You may still feel young when you do it. Feeling like an adult can come after you act like one.'),
    (['F3.9'], 105, ' without handing over the adult part of you to the caretaker in another person or without actually going '
     'back in age.', '. That doesn’t mean handing your adult judgment over to someone else to take care of you, or '
     'actually going back in age.'),
    (['O43'], 113, 'take the blaming as proof your love really is conditional', 'take the blaming to mean your love '
     'really is conditional'),
    (['F4.1'], 117, 'in the center of your chest which is physically connecting you to your love and then place',
     'in the center of your chest, which physically connects you to your love, and then place'),
    (['F4.2'], 120, "You don't have to move their feelings, just sit back and enjoy their company.",
     "You don't have to try to make their feelings go away. Just sit back and enjoy their company."),
    (['F4.3'], 129, 'all the fluffy stuff but then they go', 'all the fluffy stuff, but then they go'),
    (['F4.3'], 129, "whatever it is they're supposed to be doing.",
     "whatever it is they're supposed to be doing. Your inner child starts to trust you when you start taking care of "
     "those things."),
    (['F5.1'], 151, 'make it relative to the danger', 'keep it in proportion to the danger'),
    (['F5.2'], 152, 'verify if it is safe enough', "verify if it is safe enough (you don't need perfect certainty, just "
     "enough real-world evidence to take the next step)"),
    (['F5.3'], 156, 'It doesn’t even have to be a child, if there is no child there,',
     'It doesn’t even have to be a child. If there is no child there,'),
    (['F5.4'], 160, 'It can be anything. What does the child need? warmth,', 'What does the child need? It can be anything: '
     'warmth,'),
    (['F5.5'], 164, 'If you feel like you already know what they need,', 'Even if you feel like you already know what they '
     'need,'),
    (['F5.6'], 165, None, "D. Give them what you can: pick a need and do the smallest thing that would help. Don't feel "
     "like you have to fix it all."),
    (['F5.7'], 168, None, 'G. Stop and rest before the caring turns into another performance, and reconnect with them '
     'later to see what was helpful.'),
    (['F5.8'], 169, "you can substitute whatever part you're working with for a signal or a feeling, or an imaginary "
     "younger you", 'you can work with a signal or a feeling instead of a part, or with an imaginary younger you'),
    (['F5.9'], 172, None,
     'Resting doesn’t mean you have to become helpless. It’s okay to limit the number of decisions you are going to be '
     'making for a certain amount of time, it’s okay to put the things you might not get to on a list, and it’s okay to '
     'let your inner adult keep watch for a while. You can still move, stop and come back whenever you need to.'),
    (['F6.1'], 176, 'For others, it is very easy to work with the inner child, they can feel it easily.',
     'For others, it is very easy to work with the inner child because they can feel it right away.'),
    (['F6.2'], 185, 'in your childhood you didn’t spend enough attention in finding out what you like and what you want to '
     'try out and who you are', 'your childhood didn’t leave you much room for finding out what you like, what you want to '
     'try out and who you are'),
    (['F6.4'], 198, 'That is why you are reading a self hypnosis guide!',
     'That is why belonging gets a section in a self hypnosis guide!'),
    (['F6.5'], 206, 'And then look what your body tells you.', 'And then notice what your body tells you.'),
    (['F6.6'], 209, 'urgency, you are special, FOMO (fear of missing out), not being included, sexual charge, shame, '
     'confused, someone will rescue you, destiny, you should obey,',
     'urgency, feeling special, FOMO (fear of missing out), the threat of not being included, sexual charge, shame, '
     'confusion, the promise that someone will rescue you, destiny, pressure to obey,'),
    (['F6.7', 'O48'], 212, None, 'Secondly, here are some of the ways people use hypnotic language to manipulate: you '
     'consent to something without realizing it, you only get one choice, or someone slips something you never agreed '
     'to into a sentence. For example:'),
    (['F6.7'], 214, 'the following questions;', 'the following questions:'),
    (['F6.7'], 216, 'The more powerful the state the stronger', 'The more powerful the state, the stronger'),
    (['O48'], 215, None, 'What are they asking me to agree to? What choice are they giving me? What are they assuming '
     'that I may not agree with? Who benefits if I comply? What is the emotionally charged part of what they’re saying? '
     'What are they leaving out? If I say no, what will the consequences be? (Will they punish me, shame me, laugh at '
     'me, leave me out, tell me I’m not ‘awake’ etc?)'),
    (['F7.1'], 218, ' Be aware of;', ''),
    (['F7.2'], 226, 'or making a subject think that something (dream, amnesia, imagery, body experiences etc) has happened',
     'or using dreams, gaps in memory, imagery, body experiences etc as evidence to make a subject think that something '
     'has happened'),
    (['F7.3'], 228, 'whilst in a hypnosis, there MUST', 'whilst in hypnosis, there MUST'),
    (['F7.3'], 228, 'being in full awareness whilst in a hypnosis,', 'being in full awareness whilst in hypnosis,'),
    (['F7.4'], 229, 'of the de hypno)', 'of the de-hypnosis checklist)'),
    (['F7.5'], 231, 'If on the other hand, you', 'If, on the other hand, you'),
    (['F7.6'], 241, "Read this page, and the Come all the way back page, when you're awake.",
     "Read through the induction, and the Come all the way back section, when you're awake."),
    (['F7.8'], 245, "coming out part first, don't bring in", "coming out part first. Don't bring in"),
    (['F7.7'], 246, 'Learn how to notice if there is no change, and that no change is not a secret success.',
     "If nothing changes, notice that too: no change doesn't mean it worked in some way you can't see."),
    (['F8.1'], 248, 'into your recorder, you can read it out loud', 'into your recorder, or you can read it out loud'),
    (['E297'], 248, 'or the two hands thing (above)', 'or the two-hand practice (above)'),
    (['F8.1'], 248, "Use the same anchor for everywhere that anchor is mentioned. Don't read the directions, just pause "
     "between paragraphs.", "Use the same anchor wherever the script mentions it. Don't read the directions out loud. "
     "Just pause between paragraphs."),
    (['F8.2'], 250, "for a bit, and let what's already there come into view.",
     "for a bit. Notice the difference between looking for something and letting what's already there come into view."),
    (['F8.3'], 268, "If there's too much it can wait.", "If there's too much, it can wait."),
    (['F8.3'], 268, "I'll be here as an adult, this won't just be my inner child.",
     "I'll be here as an adult, so my inner child doesn't have to carry this alone."),
    (['F8.4', 'E297'], 279, None, 'Start with the two-hand practice: one hand on your heart for your Nurturer, the other '
     'on your solar plexus for your vulnerable child.'),
    (['F8.4'], 281, 'Start to breathe gently….', 'Breathe gently.'),
    (['F8.7'], 287, 'to go to sleep listening to hypnosis', 'to go to sleep listening to hypnosis.'),
    (['F8.5'], 297, None, 'It might be useful for your wise subconscious to let you know that your inner meeting space is '
     'ready for you to go into by making a finger twitch, pulse, lift up by itself, heat up or tingle in a way you '
     'notice.'),
    (['F8.6'], 299, 'Even if something happens, it doesn’t mean it is true, it just might mean that something is listening.',
     'Even if something happens, it doesn’t mean that what comes next will be true. It just might mean that something is '
     'listening.'),
    (['F9.1'], 301, 'how to come back down at the end, you can do the following….',
     'how to come all the way back up at the end, you can do the following:'),
    (['F9.2'], 316, 'If you are going to sleep to a recording then it is fine to go to sleep or just remain resting quietly '
     'at the end of it.', 'If you are going to sleep to a recording, then it is fine to go to sleep or just keep resting '
     'at the end of it.'),
    (['F9.2'], 316, 'However, if you are coming out of a recording then you should not',
     "However, if it's a recording that's meant to bring you back awake, then you should not"),
    (['F9.3'], 321, 'Ask your conscious mind to listen.', "Ask your conscious mind to listen, and don't force an answer."),
    (['F10.7'], 331, '(if you can help it) but some days', '(if you can help it), but some days'),
    (['F10.1'], 337, None,
     "Your shoulders tightening, or 'hmm, that feels kind of wrong', is a signal to investigate further. A tightening "
     "won't tell you what it's about by itself, so ask what happened and whether the invitation fits. But 'No! That is "
     "Not Right!' is a signal to stop what you're doing and change it. If you don't feel like it fits, don't keep doing "
     "it, and don't try saying it again more persuasively. Just change it. You don't need any other reason."),
    (['F10.2'], 339, None,
     "Sometimes the invitation just isn't right. Sometimes it brings up a possibility you hadn't thought of, and the "
     "feeling that comes with it is worth meeting. You don't have to know which it is before you make room to find out. "
     "Either way, your doubt isn't automatically a guard, and silence doesn't mean a hidden process is working."),
    (['F10.3'], 341, 'Are they able to communicate in a mature fashion?',
     "Can they hear you disagree, take responsibility, and make room for what you're going through?"),
    (['F10.4'], 345, None, 'You can say, "I can let this much be here, and notice what\'s supporting me right now." And '
     'when you\'ve had enough, "Ok, I think that is enough for now."'),
    (['F10.6'], 353, 'it is processing the upset of not getting what it wanted before.',
     'it is processing the upset of not getting what it wanted before. That doesn’t mean your love isn’t working.'),
    (['F10.6'], 353, '(ie remain in the process).', '(ie remain in the process), but don’t push for more tears, since '
     'crying more doesn’t mean you’re healing more.'),
    (['F10.5'], 354, 'It may be a good hypothesis for what you need to do but it is not a proven fact.',
     'It may be a good hypothesis for what you need to do, but it isn’t a record of what actually happened.'),
    (['F11.2'], 362, 'and come out again (that takes a few minutes too).',
     'and come out again (that takes a few minutes too). Fifteen minutes is just a handy appointment with yourself, '
     'though, and your feelings don\'t have to keep to it.'),
    (['F11.8'], 363, "Choose one way to induce yourself, you don't need to try all of them!",
     "Choose one way to induce yourself. You don't need to try all of them!"),
    (['F11.1'], 365, 'As you come out of the process ask yourself', 'As you come out of the process, ask yourself'),
    (['F11.1'], 365, 'And most importantly, what can you carry with you as you move forward from this?',
     'And most importantly, what can you now carry yourself that you used to have to borrow?'),
    (['O46'], 365, '(fill in one small action that will begin', '(fill in a small action that will begin'),
    (['F11.8'], 367, 'very intense but it is good', 'very intense, but it is good'),
    (['F11.3'], 368, 'Otherwise, the dishes won’t get done.',
     'Otherwise you just get another beautiful inner meeting, and the dishes are still sitting in the sink.'),
    (['F11.4'], 370, 'If it takes you destabilizing to know what your subconscious knows, it is not meant',
     'If knowing what your subconscious knows would destabilize you, it is not meant'),
    (['F11.5'], 374, 'it is much harder to access your adult capacities so focus on being able to regulate and getting '
     'support!', 'it is much harder to access your adult capacities, so focus on being able to regulate and getting '
     'support! If your subconscious won’t answer, it may be protecting you until your adult is steady enough to take in '
     'what it has.'),
    (['F11.6'], 376, 'Instead, say to yourself something like this:',
     'Or, instead of demanding answers, say to yourself something like this:'),
    (['F11.7'], 378, 'So, treat it like an image and get some help outside of yourself!',
     'So, treat it like an image, and get some help outside of yourself when you need it!'),
    (['F12.1'], 384, "to do this, it isn't necessarily", "to do this. It isn't necessarily"),
    (['F12.1'], 384, "you don't want to do then correct the invitation.", "you don't want to do, then correct the "
     "invitation."),
    (['F12.2'], 389, 'might be “I need to know you will set boundaries” “I need to know you will do what you said you will '
     'do” “I need to know you won’t keep leaving” “I need to know you won’t think that knowing something means that you '
     'don’t need to do anything about it” etc.',
     'might be “I need to know you will set boundaries,” “I need to know you will do what you said you will do,” “I need '
     'to know you won’t keep leaving,” or “I need to know you won’t think that knowing something means that you don’t '
     'need to do anything about it.”'),
    (['E297'], 403, 'Put your hand on your heart, your other hand on your solar plexus, and say,',
     'Do the two-hand practice and say,'),
    (['F12.3'], 405, '“What’s the smallest, most specific thing you can do to demonstrate the love you’re feeling?”',
     '“What’s the smallest, most specific thing your love is asking you to do next? A task, a boundary, a meal, some '
     'rest, a repair, a conversation?”'),
    (['F12.4'], 416, 'You may have a real wound that needs to be dealt with, but it’s possible you’re caught in a checking '
     'loop.', 'You may have a real wound that you need to deal with and be caught in a checking loop at the same time.'),
    (['F13.1'], 423, ', until you have stabilized your life. Get help to do so, if you are not reality testing well,',
     '. Stabilize your life first, and get help to do so if you are not reality testing well,'),
    (['F13.3'], 446, "Start from the basis that the subconscious, the body, the sharp mind, and the guard who's tensed up "
     "and ready for the other shoe to drop for a long time are all not your enemies.",
     "Start from the basis that none of these are your enemies: the subconscious, the body, the sharp mind, and the guard "
     "who's been tensed up and waiting for the other shoe to drop for a long time."),
    (['F13.4'], 450, 'You can download Inner Signal App for voice hypnosis,', 'You can use the Inner Signal app for voice '
     'hypnosis,'),
    (['F14.1'], 465, 'Constraint: What do you need to do to make sure your asking is safe, true, kind etc.',
     'Constraint: What do you need to do to make sure your asking is safe, true, kind etc.? That means no forcing, no '
     'false certainty, and making sure you can handle the answer before you ask for it.'),
    (['F14.2'], 483, None, 'NLP stands for Neuro-Linguistic Programming.'),
    (['F14.3'], 490, 'presuming you can do something safe; linking cause and effect;',
     'presuming only that you can do something safe; linking cause and effect carefully;'),
    (['F14.6'], 503, 'Example: ‘Notice how you find out the answer.’', 'Example: ‘Notice how the answer comes to you: as an '
     'image, a word, a pressure, some warmth, silence, or something to do next.’'),
    (['F14.4'], 505, None, 'A presupposition is an assumption hidden inside a sentence. Presumption is a powerful thing, '
     'so please don’t use it except to presume that we will have the choice of when it will happen, that we will be able '
     'to do it, that we are safe, that we are loved and that our adult can lead us. Never use it to sneak in obedience.'),
    (['F14.5'], 507, 'It’s not very likely that just by breathing in and out that your trauma is going to go away!',
     'It’s not very likely that just by breathing in and out your trauma is going to go away! A better bridge claims a '
     'lot less: ‘As I breathe, my adult self may become present enough to hear a small piece of what the wound needs.’'),
    (['F15.1'], 532, "If someone's fear, craving,", 'If your fear, craving,'),
    (['O43'], 543, "remembering that what I'm noticing is not proof for what I'm interpreting from the coincidences",
     "remembering that what I'm noticing doesn't confirm what I'm reading into the coincidences"),
    (['O48'], 543, '(What is really going on, what is just my interpretation? What needs to be warmed? What needs to be '
     'protected? What action needs to be taken?)', '(What is really going on, what is just my interpretation? What '
     'needs warmth? What needs protecting? What do I need to do?)'),
    (['O48'], 543, '(if there is a problem with my body that needs to be taken care of) or if there is something that '
     'needs to be done about the situation', '(if there is a problem with my body that I need to take care of) or if I '
     'need to do something about the situation'),
    (['F15.2'], 550, 'it is just a bell that rings to wake you up, it is not proof for what you are interpreting from it.',
     'it is just a bell that rings to wake you up. It doesn’t confirm what you are reading into it.'),
    (['F15.4'], 557, 'Research has shown that people that score high on apophenia tests also score high for detecting '
     'patterns that were not really there, as well as scoring high on psychosis spectrum traits (see Blain and '
     'colleagues, and Grant and colleagues) (this is not saying that noticing patterns is bad; in fact, it\'s not a '
     'pathology).',
     'Research has linked apophenia, the tendency to see patterns that aren\'t really there, with psychosis spectrum '
     'traits (see Blain and colleagues, and Grant and colleagues). That isn\'t saying that noticing patterns is bad. In '
     'fact, it\'s not a pathology.'),
    (['F15.5'], 564, 'Perceptual Positions: 1) seeing from Self', 'I go through four positions: 1) seeing from Self'),
    (['F15.5'], 567, 'Future Pacing: 1) Once I have seen', 'Once I have seen'),
    (['F15.5'], 570, 'Swish Variation: 2) I use an NLP technique', 'I use an NLP technique'),
    (['F15.5'], 572, 'Parts Integration: I use this technique to ask', 'I use parts integration to ask'),
    (['F16.1'], 579, 'I do not remove pain,', 'I do not use NLP to remove pain,'),
    (['F16.2'], 588, None, 'Induce or contain yourself (gather your attention, or stabilize yourself first if you are '
     'already wide open).'),
    (['F16.2'], 589, None, 'Ask yourself for permission: is it useful to work with this image, feeling or pattern today?'),
    (['F16.2'], 590, 'Get a representation of their pattern', 'Get a representation of your pattern'),
    (['F16.2'], 591, 'is protecting for them.', 'is protecting for you.'),
    (['F16.2'], 592, 'Gently change some aspect of their pattern', 'Gently change some aspect of your pattern'),
    (['F16.2'], 593, 'Put 3 good adults in with the person (Nurturer', 'Bring in your 3 good adults (Nurturer'),
    (['F16.2'], 594, "Anchor the person's good state", 'Anchor your good state'),
    (['F16.2'], 595, None, 'Future pace a scenario where your old pattern would have triggered, and do a small new '
     'behavior (If...then... statement).'),
    (['F16.2'], 596, 'Have them check in with their body for changes, ask whether the new behavior is kind and doable, and '
     'ask what supports their new interpretation', 'Check in with your body for changes, ask whether the new behavior is '
     'kind and doable, and ask what supports your new interpretation'),
    (['F16.2'], 597, None, 'Get yourself out of the altered state (come back to the room and do something normal).'),
    (['F16.4'], 618, 'Therefore, instead of interrogating that part, start with yourself:',
     'Therefore, don’t start by interrogating that part. Help your body first.'),
    (['F17.1'], 623, 'EFT tapping: One of the easiest ways', 'One of the easiest ways'),
    (['F17.1'], 625, 'Somatic experiencing: If you would like', 'If you would like'),
    (['F17.1'], 627, 'Gendlin Focusing: Focusing is another approach', 'Focusing is another approach'),
    (['F17.3'], 636, None, 'If you’re there, little one, I’m here. Thank you, guard, for letting me know you’re here. You '
     'didn’t have to scream. I got your message.'),
    (['F17.3'], 637, None, 'If there is something we need to do, let me know what the first thing is that we need to do '
     'at this moment. If there is nothing to do, help my body stand down. I’m not going to abandon you, but I’m not going '
     'to worship you either. I will listen to what you have to say and reality test it and then take some action.'),
    (['F17.4'], 639, 'to help you digest grief', 'to help you work through grief'),
    (['F17.4'], 640, 'rather than the real life.', 'rather than real life.'),
    (['F17.6'], 662, 'if things go unexpected during', 'if something unexpected happens during'),
    (['F17.7'], 666, 'if the person was certified in them or not, though.',
     'whether the person was certified in those methods, though.'),
    (['O42'], 673, 'Seeking counsel can quietly turn into abdicating to an authority figure.',
     'Seeking counsel can slide into abdicating to an authority figure without you noticing.'),
    (['F18.1'], 676, 'We can not force forgiveness on ourselves, it has to come from a place of understanding otherwise it '
     'can be bypassing.', 'We cannot force forgiveness on ourselves. It has to come from a place of understanding, '
     'otherwise it can be bypassing.'),
    (['F18.2'], 693, '(i.e. when you', '(e.g. when you'),
    (['F18.3'], 694, 'regardless of the lighting that came with the "download",',
     'regardless of how amazing the lighting was on the "download",'),
    (['F19.1'], 717, 'But if you’re fighting it out of fear…', 'But if you’re fighting it out of fear, it can backfire:'),
    (['F19.2'], 721, 'Second, feel free to tell the presence', 'You can also tell the presence'),
    (['F19.2'], 730, 'Finally, presences, shadow forces, or grandiose parts don’t always attack through fear.',
     'Presences, shadow forces, or grandiose parts don’t always attack through fear, either.'),
    (['F20.1'], 741, 'Stretch and Release: Work out what will be supporting you, focus on the feeling of support.',
     'Work out what will be supporting you, and focus on the feeling of support.'),
    (['F20.2'], 741, 'See if there is any difference, even if there isn’t.',
     'See if there is any difference (it’s fine if there isn’t).'),
    (['F20.4'], 743, 'Supported Floating: Work out what is supporting you and where your weight is, imagine that',
     'Work out what is supporting you and where your weight is. Imagine that'),
    (['F20.4'], 743, 'See what happens, you can fractionate this', 'See what happens. You can fractionate this'),
    (['F20.3'], 745, 'Rhythmic: Use your breathing or slightly hum in your throat to make a natural rhythm, or tap your '
     'finger or listen to sounds outside to make an artificial one.',
     'Use your breathing or a slight hum in your throat for a natural rhythm. You could also tap your finger, or follow '
     'a sound outside.'),
    (['F20.3'], 745, 'Tell yourself you are going to say “here, and here again” over and over, and notice what you pay '
     'attention to in between the phrases, then stop saying it.',
     'Say “here, and here again” over and over, and notice what you pay attention to in between the phrases. Then stop '
     'saying it.'),
    (['F20.1'], 747, 'Unwinding Object: Good for when', 'Unwinding an object is good for when'),
    (['F20.4'], 747, 'give yourself a minute to look at them all, you don’t have to change anything,',
     'give yourself a minute to look at them all. You don’t have to change anything,'),
    (['F20.4'], 747, 'Which one do you need to work on, what does it need', 'Which one do you need to work on, and what '
     'does it need'),
    (['F20.1'], 749, 'Sensory Journey: Pay attention to', 'Pay attention to'),
    (['F20.4'], 749, 'as you walk, what do objects feel like if you touch them, what landmarks do you see?',
     'as you walk. What do objects feel like if you touch them? What landmarks do you see?'),
    (['F20.1'], 751, 'Gradual wave: start with', 'Start with'),
    (['F20.1'], 753, 'Care workshop: prepare the workshop', 'Prepare the workshop'),
    (['F20.1'], 753, 'Goal is to make it', 'The goal is to make it'),
    (['F20.1'], 755, 'Resource: pick a resource quality', 'Pick a resource quality'),
    (['O46'], 755, 'keeping the quality and one positive action that you would do with it',
     'keeping the quality and a positive action that you would do with it'),
    (['F21.1'], 774, 'see Inner Child Self-Love Reparenting Guide.', 'see my Inner Child Self-Love Reparenting Guide.'),
    (['O48'], 775, 'Some of the information in this post is taken from', 'Some of the information in this post comes '
     'from'),
    (['F21.3'], 779, 'This US Veterans Administration website', 'This US Department of Veterans Affairs website'),
]

# whole paragraphs given as Markdown (a list item that becomes a paragraph, a new list item, a new paragraph)
RAW = {
    100: ['Last, return the adult hat, noticing what you borrowed and what you were able to do on your own (even if '
          'it’s only 5%).'],
    735: ['For sleep, try using [this playlist by '
          'Nimja](https://www.youtube.com/watch?v=IqyqE8V2CJg&list=PLZhjR9_8QJZsWUmSS5KpiueoQuq0k-poT).'],
    654: ["- What they will do if things don't fit",
          "- If they are treating trauma, whether they have specific training in trauma and dissociation (having "
          "hypnosis certifications matters, but doesn't mean they are trained in trauma care)"],
    # Appendix C's list (his audit comment: "see if you can apply the fix strategy I used above on the below"): his
    # strategy from the audit, uncompress the list, explain, and break it with a bridge that sounds different (his was a
    # point about the last question, then "Continuing with the job interview:"; this one follows his police line above)
    601: ['Before you do what it wants you to do, check how it’s trying to get you there. Is it rushing you, or telling '
          'you to keep things secret? Is it shaming you, or threatening to leave you out if you don’t do what it says? '
          'Maybe it makes you feel special, or there’s a sexual charge to it, or a sense that you’re spiritually above '
          'everyone else.',
          'Then look at what it wants from you. Is it money, or sex? Your loyalty? Is it asking you to keep quiet, or to '
          'obey it?',
          'Keep in mind though, people who mean well can ask for some of these too. A teacher charges for their time, and '
          'your partner probably wants your loyalty. If you can say no to them and they’re fine with it, that’s a good '
          'sign.',
          'Back to the interrogation:',
          'Is it trying to narrow down your choices? Does questioning it feel like you’re doing something wrong, or does '
          'it act like not obeying is a problem you need to fix? Does normal life start to seem boring, stupid or '
          'irrelevant when it’s around? Is it trying to seduce, scare or rescue your inner child? And does it try to stop '
          'your adult self from saying no?'],
}
INSERT_AFTER = {
    219: (['F7.1'], 'Here are some of the ways that happens:'),
    505: (['F14.4'], 'Example: ‘Before any part has to change, it can first become more understood.’'),
}
DELETE = {
    280: ['F8.4', 'E297'],   # "Let the hand on your heart be your Nurturer ..." is in the first line now
    563: ['F15.5'],          # "Here is a rough outline of the NLP tools and techniques I use:" under the first tool's heading
}
RAW_FINDINGS = {100: ['F3.5'], 735: ['F20.5'], 654: ['F17.5'], 601: ['C-601']}

# his own versions: on his next cards page, with my suggestion (build_cards_fullread.py makes the cards)
CARDS = {
    'F1.3': 14, 'F1.4': 14, 'F1.5': 20, 'F1.6': 20, 'F1.7': 24, 'F21.2': 777,
}
# the fate of every finding not fixed above: (fate, why, my severity when lower)
FATES = {
    'F1.3': ('his', 'His own sentence (ED-A1, 28 October): the comma before "but" is on his cards page.'),
    'F1.4': ('his', 'His edit of the paragraph (ED-A1): the suggestion ("see the results in your day-to-day life") is on '
             'his cards page.'),
    'F1.5': ('his', 'His edit of the paragraph (ED-A3, 28 October), which kept "as you\'re invited": the suggestion is on '
             'his cards page.'),
    'F1.6': ('his', 'His edit of the paragraph (ED-A3): "any real-world actions it calls for" is on his cards page.'),
    'F1.7': ('his', 'His own paragraph (ED-A5, 28 October: "couldn\'t even understand what the original was talking '
             'about"): the "Not sure" point, said plainly, is on his cards page.'),
    'F1.9': ('his', 'His own version (J5, 30 October) replaces the paragraph with his example; the four kinds of consent '
             'are his call, and the example makes the point that the mind can be influenced without the adult choosing.'),
    'F3.10': ('his', 'His own version (R-96, 30 October); Appendix K keeps the disclaimer that the sequence isn\'t '
              'validated as one treatment.'),
    'F6.3': ('not', 'He approved this change on 25 October (card IC-A21, lined up with his inner child guide\'s '
             '"Differentiation": "sometimes the break has to be long-term"); the published caution is what he replaced.'),
    'F13.2': ('not', 'The last rule\'s point (end every session back in your ordinary self, saying it\'s over) is made '
              'where it belongs, in Come all the way back ("the session is now over"); saying it again here is the '
              'repeated safety language he asked us to cut (O45, 23 October).'),
    'F15.3': ('not', 'The cue\'s limits that are gone here are in its own sections: it is yours and you can take it out '
              '("False positives, and turning the cue off"), and nobody may activate what you put in yourself ("What not '
              'to do", the hidden commands rule).'),
    'F16.3': ('his', 'His own text (his message of 23 October 01:10 UTC, window 13 "human high conf"); the published '
              'caution would bring back "proves", a tell he named; the next paragraph already tests the signal ("it\'ll '
              'still be there tomorrow").'),
    'F17.2': ('not', 'The caution (a product says nothing about whether an inner signal is true) is the guide\'s point '
              'everywhere; saying it again after a product is the repeated safety language he asked us to cut (O45), in '
              'the "doesn\'t prove" form he named a tell on 30 October.'),
    'F21.2': ('his', 'His edit (CV-8.9, 25 October): marking the title ("The study ...") is on his cards page.'),
}


def main():
    ap = argparse.ArgumentParser(description=__doc__.split('\n\n')[0])
    ap.add_argument('--check', action='store_true')
    a = ap.parse_args()
    md = GUIDE.read_text(encoding='utf-8')
    assert hashlib.sha256(md.encode('utf-8')).hexdigest() == BEFORE_SHA, 'the guide changed since this was written'
    bl = sr.blocks(md)
    raw = re.split(r'\n\s*\n', md.rstrip('\n'))
    assert len(raw) == len(bl)
    texts, fids, problems = {}, {}, []
    for f, b, old, new in EDITS:
        t = texts.get(b, bl[b]['text'])
        if old is None:
            t = new
        elif t.count(old) != 1:
            problems.append('block %d: %r found %d times' % (b, old[:60], t.count(old)))
            continue
        else:
            t = t.replace(old, new)
        texts[b] = t
        fids.setdefault(b, []).extend(f)
    if problems:
        print('\n'.join(problems))
        return 1
    new_raw, lost, changed = {}, [], []
    for b, t in sorted(texts.items()):
        assert b not in RAW and b not in DELETE, b
        new_raw[b] = [set_block_text(raw[b], t, lost)]
        changed.append({'block': b, 'where': sr.where(bl, b), 'findings': sorted(set(fids[b])),
                        'before': bl[b]['text'], 'after': t})
    for b, paras in RAW.items():
        assert b not in new_raw
        new_raw[b] = list(paras)
        changed.append({'block': b, 'where': sr.where(bl, b), 'findings': RAW_FINDINGS[b], 'before': bl[b]['text'],
                        'after': '\n\n'.join(paras), 'markdown': True})
    for b, (f, p) in INSERT_AFTER.items():
        new_raw[b] = new_raw.get(b, [raw[b]]) + [p]
        changed.append({'block': b, 'where': sr.where(bl, b), 'findings': f, 'before': '', 'after': p, 'inserted_after': b})
    for b, f in DELETE.items():
        assert b not in new_raw
        new_raw[b] = []
        changed.append({'block': b, 'where': sr.where(bl, b), 'findings': f, 'before': bl[b]['text'], 'after': '',
                        'deleted': True})
    assert not lost, lost
    out = []
    for i, r in enumerate(raw):
        out += new_raw.get(i, [r])
    new_md = '\n\n'.join(out) + '\n'
    findings = json.loads((HERE / 'FINDINGS.json').read_text(encoding='utf-8'))['findings']
    done = {x for c in changed for x in c['findings']}
    disp = {}
    for x in findings:
        fid = x['id']
        if fid in FATES:
            disp[fid] = list(FATES[fid])
        elif fid in done:
            disp[fid] = ['fixed', 'Fixed in our words (apply_fullread.py; APPLIED-FULLREAD.json has the paragraph before '
                         'and after), and the paragraph read beside his published version (VERIFY.md).']
        else:
            problems.append('%s has no fate' % fid)
    if problems:
        print('\n'.join(problems))
        return 1
    rec = {'about': __doc__.split('\n\n')[0], 'before_sha256': BEFORE_SHA,
           'after_sha256': hashlib.sha256(new_md.encode('utf-8')).hexdigest(), 'changed': changed,
           'cards': CARDS, 'counts': {'paragraphs_changed': len({c['block'] for c in changed}),
                                      'findings_fixed': sum(1 for v in disp.values() if v[0] == 'fixed'),
                                      'findings_his': sum(1 for v in disp.values() if v[0] == 'his'),
                                      'findings_not': sum(1 for v in disp.values() if v[0] == 'not')}}
    print(json.dumps(rec['counts']), rec['after_sha256'])
    if a.check:
        return 0
    GUIDE.write_text(new_md, encoding='utf-8')
    (HERE / 'APPLIED-FULLREAD.json').write_text(json.dumps(rec, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    (HERE / 'DISPOSITIONS.json').write_text(json.dumps(disp, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    return 0


if __name__ == '__main__':
    sys.exit(main())
