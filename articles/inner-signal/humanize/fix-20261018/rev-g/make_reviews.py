"""My meaning reviews of the sections that read Human in 439g and 440g: Appendix A (HG29+30, mapped right), the hostile-presences
appendix (HG37) and the induction library (HG38+39). Each fix is the smallest change that gives back the published
point, keeping Emulate's words around it; each (old, new) is checked against the stretch's exact text."""
import json
def build(key, fixes, links=None):
    d = json.load(open('rev-g/%s.units.json' % key, encoding='utf-8'))
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
    json.dump(rv, open('rev-g/%s.review.json' % key, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(key, len(fixes), 'fixes in', sum(r['verdict'] == 'FIX' for r in rv), 'of', len(rv), 'stretches')

build('HG29+30', [
 (3, 'SHIFT', "to hear the next signal (not 'to get more information')", 'more loving and to get more information.', 'more loving and better able to hear the next signal.'),
 (3, 'LOST', 'the constraint: safety, truth, kindness, no forcing, no false certainty, capacity before content', 'Constraint (what is safe?)',
  'Constraint (what keeps it safe, true and kind: no forcing, no false certainty, capacity before content)'),
 (3, 'LOST', 'so the analytical mind doesn’t treat silence as failure', 'might fabricate answers to fit your prompt.', 'might treat silence as failure and fabricate an answer to fit your prompt.'),
 (3, 'UNCLEAR', "the fallback is a script the reader says (quotation marks, 'my body', today)",
  'If the system needs more time to process this, or if silence is the best and safest answer, then let the body go into a deeper state of comfortable rest. The prompt is considered successfully answered with peaceful silence.',
  '“If the system needs more time to process this, or if silence is the best and safest answer today, then let my body go into a deeper state of comfortable rest. Peaceful silence is a successful answer.”'),
 (16, 'LOST', 'only as a gentle symbol, a body signal, or a single next step', 'in a safe way that I can integrate.', 'only as a gentle symbol, a body signal, or a single next step.'),
 (16, 'LOST', "the inner child's prompt: little one, what can I do today so you are not alone with it", 'Inner child: What do you need me to know? What can I do for you?',
  'Inner child: Little one, what do you need me to know? What can I do today so you’re not alone with it?'),
 (16, 'SHIFT', "what action would make this system safer (not 'for you to feel safe')", 'for you to feel safe?', 'to make this system safer?'),
 (16, 'SHIFT', "the conditioning prompt: look at the impulse clearly; if part of it comes from conditioning, let that part be seen, and soften or step back only as much as is safe (not 'dissolve all the programming'); let my body feel the difference",
  'Wise subconscious mind, dissolve all the programming from my previous family, religion, marketing, erotic imprints, political tribe, trauma responses, and need for belonging as a child. Show me how these show up so I can see that they are just programming. Let them dissolve, or at least let them step back, so that I can receive the true guidance from the universal heart that will make my life better in simple, ordinary ways.',
  'Wise subconscious mind, help me look at this impulse clearly. If part of it comes from family programming, religious fear, marketing, erotic imprints, political tribe, trauma responses, or a childhood need for belonging, show me that part so I can see it as programming. Let it soften or step back only as much as is safe, so that I can receive the true guidance from the universal heart that will make my life better in simple, ordinary ways. Let my body feel the difference.'),
 (16, 'SHIFT', "the daydream prompt: if useful, reveal the guidance in it; if avoidance, bring me gently into the present",
  'Show me if this daydream is useful and guiding me, or if it is a way of not dealing with my life. If it is the latter, let me deal with my life.',
  'If this daydream is useful, show me the guidance in it. If it is a way of not dealing with my life, bring me gently into the present and help me deal with what I need to deal with.'),
 (16, 'SHIFT', "if the full truth would overwhelm me, don't reveal it all (not 'don't show it to me')", 'Please don’t show it to me.', 'If the full truth would overwhelm me, please don’t show me all of it.'),
 (16, 'SHIFT', "an action that would prove I heard correctly (not 'integrate this')", 'What can I do in ordinary life to integrate this?', 'What can I do in ordinary life that would prove I heard correctly?'),
 (16, 'LOST', "without pretending the answer is automatically true", 'Use both.', 'Use both, without pretending the answer is automatically true.'),
])

build('HG37', [
 (1, 'SHIFT', "from experience (not 'a bit more')", 'I’m going to come from a bit more experience here.', 'I’m going to come from experience here.'),
 (1, 'LOST', 'plant-medicine-adjacent practice; grief (not extreme grief)', 'extreme grief, prayer, or a variety', 'grief, prayer, plant-medicine-adjacent practice, or a variety'),
 (1, 'SHIFT', "it doesn't feel like an emotion or younger part (not 'it is not'); it feels intrusive, hateful, seductive, mocking or simply alien",
  'But it is not a simple emotion, and not merely a younger part.', 'It doesn’t feel like a simple emotion or a younger part, and it feels intrusive, hateful, seductive, mocking, or simply alien.'),
 (1, 'LOST', 'the possibilities: literal beings, symbolic mind-forms, trauma in a frightening costume, dissociated energy, ancestral and relational burdens',
  'whether they are literally demons or not.', 'whether they are literally demons or not. Maybe they are literal beings; maybe they are symbolic mind-forms, trauma in a frightening costume, dissociated energy, or ancestral and relational burdens.'),
 (1, 'LOST', "the practical question as a script, with 'less hooked'",
  'All that matters is what the best way of dealing with them is, in terms of what leaves you feeling the safest, clearest, most loving, most grounded, etc.',
  'All that matters is the practical question: “What response makes me safer, clearer, more loving, more grounded, and less hooked?”'),
 (6, 'LOST', "no instant certainty; the triage (medical danger, environment, body, overload, how open the mind is); the steps; don't deepen, hunt for hidden truth or debate what it is",
  'you check in with the room, your body, and safety in general.',
  'you check in with the room, your body, and safety in general, without rewarding it with instant certainty about what it is. Run the triage first: medical danger, environment, body, overload, and how open your mind has become. Open your eyes, feel your feet, name the room, lower the stimulation, leave hostile company, and stop adding prompts. Don’t go deeper, hunt for hidden truth, or debate what it is while you’re destabilized.'),
 (6, 'WRONG', "the script invited the presence forward and had the body bring it to safety; the published: only what can be integrated is welcome, too much can wait, the adult remains, the body may return to safety",
  '“If there is anything that can be integrated right now, you may come forward. But know that you can wait, and that you will not be able to come forward until you are something that can be integrated. Know also that I will always be here as an adult, and that my body will bring you to a place of safety.”',
  '“Only what can be integrated is welcome right now. Anything that’s too much can wait. The adult in me is still here, and my body can go back to safety.”'),
 (10, 'UNCLEAR', "Emulate's paragraph breaks off ('if that feels'); the published: once stable enough, notice what helps without making it a test of what it is; hand on heart if welcome, a comfortable breath, keep the room",
  'If not, then check in with yourself as to what will be the best response. Again, it doesn’t matter whether or not it’s literally a demon. Put your hand on your heart, if that feels',
  'If not, and you’re stable enough to stay present, check in with yourself as to what helps. Again, it doesn’t matter whether or not it’s literally a demon; this isn’t a test of what it is. Put your hand on your heart, if that feels welcome, take a comfortable breath, and keep the room available.'),
 (11, 'SHIFT', "warmth or distance, and keep the boundary either way (not either/or)", 'Ask yourself if it would be appropriate to send it some warmth or if you need to place a boundary with it.',
  'Notice whether warmth or distance helps, and keep your boundary either way.'),
 (12, 'LOST', 'return to the body and room', 'then do not continue to engage with it.', 'then stop engaging with it and come back to your body and the room.'),
 (13, 'WRONG', "whether the response helps you become clearer, steadier, less hooked (not whether it clears 'it'); a protector needn't show its fear quickly, comfort doesn't prove an interpretation",
  'Ask yourself if this way of responding to it seems to be clearing it.',
  'Ask yourself if this way of responding helps you become clearer, steadier, and less hooked. A protective part doesn’t have to show its fear quickly, and a comforting response doesn’t prove what it is either.'),
 (13, 'LOST', "love and boundaries don't need a verdict first", 'It is ok to use a combination of love and boundaries to interact with it.', 'You can use love and boundaries without deciding what it is first.'),
 (15, 'SHIFT', "the first impulse may be (not 'my first thought'); identify completely with the threatened self (not 'be it')", 'My first thought is to fight it', 'The first impulse may be to fight it'),
 (15, 'WRONG', "identify completely with the threatened self (not 'be it')", 'panic, be it, etc.', 'panic, become nothing but the threatened self, etc.'),
 (16, 'LOST', "pride gives it an opponent, panic gives it the nervous system (the sentence was garbled)",
  '…it becomes the center of your attention and when you hate it, give it a hook in you, or fight it from pride or panic….',
  '…it becomes the center of your attention. When you hate it, you give it a hook in you. Pride gives it an opponent, and panic gives it your nervous system.'),
 (17, 'SHIFT', "'the enemy' (the appendix's point is not to fight it)", 'So the next time the enemy enters the room, simply say to it,', 'So the next time it shows up, simply say,'),
 (17, 'LOST', "not defeat it from fear", 'I see that there is no need to defeat what I am experiencing.', 'I see that there is no need to defeat what I am experiencing from fear.'),
 (19, 'WRONG', "don't offer soft love as though inviting it in for tea (Emulate made it an instruction)", 'In this case, don’t approach it with soft sentimental love. Invite it in for tea.',
  'In this case, don’t approach it with soft sentimental love, as though you were inviting it in for tea.'),
 (19, 'LOST', 'the chest open but not exposed; the body has a perimeter', 'pull your shoulder blades back slightly, feel the boundary of the skin around your torso',
  'pull your shoulder blades back slightly so your chest is open but not exposed, feel the boundary of the skin around your torso and that this body has a perimeter,'),
 (24, 'LOST', 'the signs: persistent, paranoid, sleepless, dangerous, impossible to reality-test', 'It is not meant for people who may be going psychotic or experiencing other forms of destabilization.',
  'That is very different from a state that becomes persistent, paranoid, sleepless, dangerous, or impossible to reality-test, which may be psychosis or another kind of destabilization.'),
 (24, 'SHIFT', "hears commands (not 'hearing voices': the guide works with inner voices)", 'are hearing voices,', 'are hearing commands,'),
 (24, 'LOST', 'continue gently', 'keep doing it.', 'keep going, gently.'),
 (24, 'SHIFT', "isolated, frightened or unreal; stop deepening and get support (not 'don't do it')", 'non-relational, scared, and non-functional, don’t do it.', 'isolated, scared, or unreal, stop going deeper and get support.'),
 (28, 'UNCLEAR', "'Finally' twice in the appendix", 'Finally, some of these presences', 'Also, some of these presences'),
 (28, 'LOST', 'a special mission, a revelation that makes washing dishes seem beneath you', 'or trying to “download cosmic info” into you, etc.', 'or trying to “download cosmic info” into you, or giving you a special mission that makes the dishes seem beneath you, etc.'),
 (28, 'LOST', "the script: thank you for the imagery; no grand performance; a simple, honest act of care tomorrow morning, and its list",
  '“Unless the info you have to download is going to help me do the dishes or clean my room, I don’t need it.”',
  '“Thank you for the imagery. I don’t need a grand performance. Unless the info you have to download can become a simple, honest act of care tomorrow morning, like doing the dishes, cleaning my room, keeping a promise, apologizing, resting, eating or helping someone I love, I don’t need it.”'),
 (28, 'SHIFT', 'guidance worth keeping makes ordinary life more beautiful, honest, relational, humble, reliable and useful to other people',
  'the guidance has to help you do the dishes or clean your room in a more beautiful, honest, relational, humble, useful way.',
  'guidance worth keeping should make ordinary life, the dishes and the room included, more beautiful, honest, relational, humble, reliable, and useful to other people.'),
 (32, 'INVENTED', "'they all basically respond the same way'; the published: they all lead to the same practical training: can love stay present without giving up the boundary, can the mind become harder to hook",
  'The truth is, they all basically respond the same way. It’s good to learn how to relate to them with love, and it’s good to make your mind harder to hook, but beyond that, I don’t really want you becoming hobbyists in this area.',
  'The truth is, they all lead to the same practical training: can love stay present without giving up the boundary, and can your mind become harder to hook? Beyond that, I don’t really want you becoming hobbyists in this area.'),
])

build('HG38+39', [
 (1, 'SHIFT', "for sleep hypnosis (not 'if you are using this page to help you go to sleep'); a stray space where the link was", 'If you are using this page to help you go to sleep, use Nimja’s sleep playlist .',
  'If you want sleep hypnosis, use Nimja’s sleep playlist.'),
 (3, 'SHIFT', "decide whether to begin; one purpose", 'Preview, choose a purpose, decide to start.', 'Preview, choose one purpose, decide whether to start.'),
 (3, 'UNCLEAR', 'replaced by no-trance contact', 'eyes open or with no trance contact replacement.', 'eyes open, or replaced by no-trance contact.'),
 (3, 'SHIFT', "move (not 'move on')", 'move on, imagine,', 'move, imagine,'),
 (4, 'LOST', "the mind doesn't owe anybody a movie", 'movement, knowing etc.', 'movement, knowing etc. The mind doesn’t owe anybody a movie.'),
 (6, 'SHIFT', "which area or inner voice wants attention; what support is needed", 'Ask yourself where in your body (and/or voice) you need to stretch or release and what you need by way of support to do this.',
  'Ask yourself which area, or which inner voice, wants attention, and what support is needed.'),
 (8, 'WRONG', "the support carries 1% more effort, as if floating without losing contact (Emulate had you use 1% more effort)",
  'Use only 1% more effort than it takes to simply rest your weight on the support, or use the same weight and pressure.',
  'Notice where your weight is carried, and let the support carry 1% more of your effort, as if floating without losing contact, or keep the same weight and pressure.'),
 (8, 'UNCLEAR', 'alternate attention: ordinary awareness on the inhale, the support on the exhale', 'spending more time on in-breaths in normal awareness, and on out-breaths focusing on the support.',
  'turning your attention toward normal awareness on the in-breath and toward the support on the out-breath.'),
 (8, 'LOST', 'keep the support, then return', 'Return to normal weight and firm contact as you choose.', 'Keep the support, come back to the weight and firm contact you choose, and return.'),
 (10, 'LOST', 'noticing where attention lands between repetitions', "over and over, until suddenly, stop the rhythm.", "over and over, noticing where your attention lands in between, until suddenly, stop the rhythm."),
 (10, 'UNCLEAR', 'notice the first quiet beat, without trying to become blank', 'This will bring about its own rhythm, the first one that appears - do not try and make it blank.', 'Notice the first quiet beat - do not try and make your mind blank.'),
 (10, 'LOST', 'let ordinary rhythm resume and return', 'Then go back to using a normal rhythm.', 'Then let your normal rhythm come back, and return.'),
 (12, 'SHIFT', "one concern with several strands; yarn unwinding, bubbles settling, knots placed beside you ('have some by you' is new)",
  'A quick exercise for when you have several concerns going on. Visualise each one as a strand of yarn, or even better, have some by you to help.',
  'A quick exercise for when one concern has several strands. Imagine yarn unwinding, bubbles settling, or knots placed where you can see them beside you.'),
 (12, 'LOST', "count only the strands you set down; nothing is erased; which needs warmth, protection or action", 'How many did you end up with?',
  'Count only the strands you actually set down; nothing is erased. Which one needs warmth, protection, or action?'),
 (12, 'SHIFT', "keep one useful strand; return (not 'come back to this page')", 'Now pick one that is important to do something about, put the others somewhere you can see them, and come back to this page.',
  'Now keep one useful strand, put the others somewhere you can see them, and return.'),
 (14, 'SHIFT', "who or what needs to speak (not whoever you want to speak to)", 'until you are in a place where you can directly speak to whoever/whatever it is you want to speak to.',
  'until you are in a place where whoever or whatever needs to speak can speak.'),
 (14, 'LOST', 'notice a detail without assigning hidden meaning', 'Observe what you want to observe,', 'Notice a detail without giving it a hidden meaning,'),
 (16, 'SHIFT', "imagine warmth, steadiness or attention spreading (not 'the current condition')", 'Sense the current condition and sense it radiating outward to the next area',
  'Sense what is already there, and imagine warmth, steadiness or attention radiating outward to the next area'),
 (16, 'SHIFT', "without claiming medical repair; does the body want contact, space, words or ordinary care", 'Sense what the body needs to feel better, without thinking of medical terms.',
  'Notice what changes, without claiming any medical repair. Does the body want contact, space, words, or ordinary care?'),
 (16, 'WRONG', "return (not 'repeat the process')", 'and repeat the process.', 'and return.'),
 (18, 'WRONG', "patient care (unhurried), not working with a patient", 'First get ready as if you were going to work with a patient. Time, place, tools and boundaries.',
  'First get ready for some patient, unhurried care: time, place, tools and boundaries.'),
 (18, 'UNCLEAR', 'let the signal, feeling or younger state come only as close as is welcome', 'When you invite them in, the signal, the feeling or the younger state to come as close as you want them to be.',
  'Let the signal, the feeling or the younger state come only as close as is welcome.'),
 (18, 'SHIFT', "ask before responding; reconnect only where welcome; rest and reassess", 'Ask them what they need, wait and see if you want to reconnect with them. If not, rest and see again.',
  'Ask before you respond, wait, reconnect only where that’s welcome, rest, and see again.'),
 (18, 'UNCLEAR', "an inner adult or a borrowed function can help", 'speak to them.', 'let that help.'),
 (18, 'SHIFT', "'good as you', not 'as good as you can'", 'The goal is to be as good as you can and not erase your history.', 'Aim for “good as you,” not an erased history.'),
 (18, 'WRONG', "close the workspace (not 'as you would with a patient')", 'Finally, close as you would with a patient.', 'Finally, close the workspace.'),
 (20, 'SHIFT', "a quality you understand (warmth, boundary, steadiness, curiosity, dignity), 1% more access through posture, voice or attention; never becoming someone else",
  'Choose someone or something who has a characteristic you want to adopt. Close your eyes and imagine them. Now imagine yourself becoming them, standing, walking and talking like them, just 1% more, or if you are uncomfortable with this, simply observe them, but in either case be aware of how you now have more access to that quality.',
  'Choose a quality you understand, like warmth, a boundary, steadiness, curiosity or dignity. Close your eyes and imagine your posture, voice or attention with just 1% more access to it, or if you are uncomfortable with this, simply observe it.'),
 (20, 'LOST', 'to strengthen access, not replace identity', 'Repeat a few times.', 'Repeat a few times, to strengthen your access to it, not to become someone else.'),
 (20, 'SHIFT', "how would the quality meet today's situation", 'Now think of a situation you want to use that characteristic in.', 'How would that quality meet the situation you’re in today?'),
 (20, 'LOST', "keep the quality and one useful action, release the role, 'I am myself', return",
  'Finally let go of the person/thing, but keep the characteristic, and say to yourself "I am me", and notice how you have increased access to the characteristic you wanted.',
  'Finally keep the quality and one useful action, let go of the role, say to yourself "I am myself", and return.'),
 (22, 'WRONG', "the element's name: observable pacing", 'Things to do in between:', 'Observable pacing:'),
 (22, 'SHIFT', "genuine choice among the options ('do whatever comes to mind' is new)", 'Choice: do whatever comes to mind, answer the question', 'Genuine choice: answer the question'),
 (22, 'SHIFT', "record a word, sensation, impulse, objection or silence without taking it as proof (not 'no interpretation')", 'write anything that comes to mind, no interpretation.',
  'write down any word, sensation, impulse, objection, or silence that comes, without taking it as proof.'),
 (22, 'WRONG', "the element's name: handoff", 'Other autonomous:', 'Handoff:'),
], links={1: [{'published': 'Nimja’s sleep playlist', 'new': "Nimja's sleep playlist"}]})
