"""My meaning review of section 14 (Emulate's text from emu-a/emu-e, Human in 433g), written as edits of each stretch's
exact text: each (old, new) below must occur in the stretch, so a typo in a quote stops the script."""
import json
d = json.load(open('rev-d/HG14.units.json', encoding='utf-8'))
body = {u['blocks'][0]: '\n\n'.join(u['paras']) for u in d['units'] if u['kind'] == 'emulate'}
E = {}  # block -> [(type, what, old, new)]
def fix(b, t, what, old, new):
    assert old in body[b], (b, old)
    E.setdefault(b, []).append((t, what, old, new))
fix(1, 'LOST', 'trust grows when the present-day adult becomes reliable', 'is you, as a person that you are right now.', 'is you, the person you are right now, becoming reliable.')
fix(2, 'INVENTED', "'in this post'", 'In this post I am going to talk about', 'Here I’m going to talk about')
fix(3, 'LOST', 'those qualities belong inside the adult relationship, not just the wounds', 'wondering at the world.', 'wondering at the world. Those belong in your relationship with it too, not just the wounds.')
fix(5, 'INVENTED', "'even more commonly'", 'or even more commonly – access a child part', 'or feel like a child part')
fix(6, 'LOST', "the name 'borrowed adulthood', 'provisional', the familiar practices it combines; 'many of the steps have been shown to be effective' is new",
    body[6], 'For that starting point, I use a provisional bridge I developed and call borrowed adulthood. Please note, it puts together familiar practices (witnessing, modeling, supported action, and handing over responsibility bit by bit), and I’m not claiming that the entirety of the steps has been validated as one treatment.')  # march-c: Emulate's "Please note" and "(to the best of my knowledge)" were its break
fix(7, 'LOST', 'notice what is present without demanding warmth, wisdom or certainty', 'Access a witnessing position, if necessary.', 'Access a witnessing position, if necessary: notice what’s there without demanding warmth, wisdom or certainty.')
fix(8, 'SHIFT', 'borrow only the warmth, boundary or direction needed now', 'Borrow whatever you need – warmth, direction, etc.', 'Borrow only what you need right now – warmth, a boundary or direction.')
fix(12, 'LOST', 'use a remembered person when that helps, or an imagined adult whose intention is to take good care of you', 'Just imagine a good adult.', 'Use someone you remember when that helps, or just imagine a good adult whose intention is to take good care of you.')
fix(13, 'LOST', 'how would a decent adult hear distrust without retaliating, defending their goodness, collapsing or leaving', 'especially when it seems like any response will be retaliatory, defensive, collapsing, leaving, etc. Borrow a decent adult’s response.', 'especially when the child doesn’t trust you and every response you can think of is retaliating, defending your goodness, collapsing or leaving. How would a decent adult hear that distrust? Borrow that one response.')
fix(13, 'SHIFT', 'adult identity can develop after the behavior', 'you’ll become an adult after you act like one.', 'feeling like an adult can come after you act like one.')
fix(15, 'SHIFT', 'letting a younger state speak is not regressing or becoming younger', 'It is possible to regress psychologically and allow those younger states to talk, but still maintain adult judgement.', 'You can let those younger states talk and still keep your adult judgement.')
fix(15, 'UNCLEAR', 'the wish to carry fewer decisions, while the internal adult remains present', 'need or whatever it is you feel you need less responsibility.', 'honest need, or the wish to carry fewer decisions, while the adult in you stays present.')
fix(16, 'LOST', 'the adult listens too', 'evaluating, protecting me and stopping me if needed', 'listening, evaluating, protecting me and stopping me if needed')
fix(19, 'SHIFT', "'him/her' for the younger state; when love is available; trust can question, remember and take its time; love stays", body[19], 'If the younger part doesn’t believe you love it yet, you can still love it, when that love is there for you to give. Its trust can question your promises, remember the times you didn’t protect it, and take its time. The love can stay while that happens.')
fix(20, 'SHIFT', "you don't have to love me back", 'It’s okay if you don’t love me yet.', 'You don’t have to love me back.')
fix(21, 'SHIFT', "that isn't a way to end the complaint; repair after an internal attack (the adult's own), not the child attacking; 'him/her'", body[21], 'That isn’t a way to end the complaint. Hear the truth in it and answer it seriously. Hearing anger without hitting back, admitting a real failure, and making repair after you’ve turned on the child inside are evidence too, alongside the meals, the limits that protect, the appointments and the kept promises. Show your love by not retaliating, but don’t substitute not retaliating for loving the younger part.')
fix(22, 'LOST', 'what each position teaches: a vow followed by blame teaches that love depends on receiving it correctly', 'Keep in mind that the position that made the vow', 'Notice what each position teaches the others: a vow of love followed by blame when it’s doubted teaches that love depends on receiving it correctly. And keep in mind that the position that made the vow')
fix(23, 'INVENTED', "'only a few years younger'", 'the defendant is you, only a few years younger.', 'the defendant is a younger you.')
fix(23, 'SHIFT', 'punishment cannot retroactively create the capacity that was missing', 'would simply punishing you make any difference to the person you were when you committed the offence?', 'remember that punishing yourself now can’t go back and give the person you were then the capacity they were missing.')
fix(25, 'INVENTED', "'that will help you get in touch'", 'that will help you get in touch with your inner child', 'for connecting with your inner child')
fix(26, 'UNCLEAR', "'come it with love'", 'if there is resistance come it with love, if you feel or see something come it with love.', 'if there is resistance, meet it with love, and if you feel or see something, meet that with love too.')
fix(26, 'LOST', 'a conversation rather than a performance', 'Just communicate with your child from your heart.', 'Let it be a conversation with your child from your heart, not a performance.')
fix(29, 'UNCLEAR', 'the inner child, not children', 'to enjoy your children.', 'to enjoy your inner child.')
fix(32, 'WRONG', 'the Protector turns warmth into something the child can believe', body[32], 'Your Protector is what turns that warmth into something the child can believe.')
fix(33, 'LOST', 'the unsafe conversation; the person who destabilizes us; keep a small promise', "'I will leave that conversation', 'I will stop texting that person'", "'I will leave the unsafe conversation', 'I will stop texting the person who destabilizes us'")
fix(33, 'LOST', 'keep a small promise', "'I will do x'", "'I will keep a small promise'")
fix(34, 'SHIFT', "'ICW' and 'IC' aren't the guide's words; what turns decorative; trust begins when you handle the consequence ('deal with the fallout if you don't' is new)", body[34], 'This is where inner-child work often turns into fluffy decoration - people talk lovingly to their inner child, but then send the destabilizing message, skip the meal, avoid the task, and break the promise. Trust begins when you actually handle the consequence.')
fix(35, 'UNCLEAR', 'if warmth is unavailable, a protective act can begin the relationship', "If you can't bring any warmth to the Protector, that's okay, just work with them on doing protective things for your child.", "If warmth isn't available, that's okay, a protective act can start the relationship.")
fix(35, 'LOST', "completion without immediate relief isn't failure; a tick doesn't prove it helped", "Also, make sure that doing them is actually helpful - don't just be ticking things off a list.", "Doing it without feeling better right away isn't automatically failure, and ticking it off a list doesn't prove it helped.")
fix(37, 'LOST', 'the label matters much less than orienting the whole system toward a life', 'Higher Adult, etc.', 'Higher Adult, etc. The name matters much less than whether it can point the whole system toward a life.')
fix(38, 'LOST', 'direction can ask for something difficult', 'Invite it to give direction in an effective way,', 'Invite it to give direction, even ask for something difficult,')
fix(38, 'LOST', 'without erasing either person', 'without punishing the other person for needing space. Etc.', 'without punishing the other person for needing space, and without erasing either of you. Etc.')  # march-c: Emulate's "Etc." was the break
fix(40, 'SHIFT', 'begin with the function you can actually reach; protection may come before warmth', 'Begin working with the adult function, perhaps beginning with protection, then warmth.', 'Begin with the adult function you can actually reach; protection may come before warmth.')
fix(42, 'LOST', 'use parts language when you recognize a protective pattern; a sensation, distraction or objection doesn\'t establish its cause; notice it first', body[42], 'Feel free to use this parts language when you actually recognize a protective pattern, or when it’s useful to explore. A sensation, a distraction or an objection doesn’t tell you its own cause. Notice it first: hunger may just need food, skepticism may be reasonable, and a sentence may simply not fit.')
fix(44, 'LOST', "not failures; the guard at the door, in its usual charming way", 'These are all common manifestations of protectors.', 'I wouldn’t call those failures. They’re often the protector, the guard at the door, showing up in its usual charming way.')
fix(45, 'SHIFT', 'a voice, not necessarily a protector', 'One of the most important protectors to become aware of', 'One important voice to become aware of')
fix(46, 'LOST', 'you are trying to protect something; I want to understand; the script as quoted words', body[46], '“I notice you. You’re trying to protect something, and I want to understand. Can I ask you what you’re afraid would happen if you stopped?”')
fix(47, 'WRONG', "the fears: lying to yourself again, another performance, being destroyed by the pain (not 'feel your pain'), spirituality to avoid reality, forgiving too early, calling fantasy guidance, abandoning them after the session ('therapy' is new)", 'that you’ll fall for your bullshit again, or that you’ll spiritualize this issue, or feel your pain, or forgive someone too early, or believe your fantasies again, or leave them hanging once the therapy session is over.', 'that you’ll lie to yourself again, or that this will turn into another performance, or that feeling the pain will destroy you, or that you’ll use spirituality to dodge reality, forgive too early, call a fantasy guidance, or leave them hanging the moment the session is over.')
fix(48, 'SHIFT', "the script: that makes sense, you don't have to move yet, what would help you trust me 1% more", body[48], 'Now, tell the protective part that makes sense, that it doesn’t have to move yet, and ask what would help it trust you 1% more.')
fix(49, 'INVENTED', "'99% of the time'; usually the protector needs evidence more than another spiritual insight", '99% of the time, the answer will be some non-spiritual thing like', 'Usually the protector needs evidence more than another spiritual insight: things like')
fix(49, 'LOST', 'write down the truth', 'owe someone money.', 'owe someone money, or writing down the truth.')
fix(51, 'INVENTED', 'a forum question; the published: the Protector is more than a voice saying no, practiced as a bodily sequence', body[51], 'The Protector is more than an inner voice saying no. Want to “embody” it? Practice the following sequence:')  # march-c: the question was the break; Emulate's "practice the following sequence to “embody”" kept
fix(56, 'LOST', 'not perfect certainty, just enough evidence for the next step', '(5) verify sufficient safety (based on reality), and finally', '(5) verify enough safety (not perfect certainty, just enough real evidence for the next step), and finally')
fix(57, 'LOST', 'protection includes ending the scan when vigilance no longer helps', '(6) stand down and rest.', '(6) stand down and rest: protecting includes ending the scan once more vigilance isn’t helping.')
fix(60, 'INVENTED', "'Client', the therapy 'you are doing'", 'Client, I want to talk about the connection between the reparenting therapy you are doing, and the self hypnosis. I think it can be a perfect fit.', 'I connect my reparenting therapy to self hypnosis. I think they’re a perfect fit.')  # march-c: Emulate's short "I think it can be a perfect fit." was the break
fix(60, 'SHIFT', 'stay with a recognizable protector, or the sensation, feeling or preference actually present', 'just work with whatever protector you do have, either in the form of a sensation, feeling, or preference)', 'stay with a protector you recognize, or with whatever sensation, feeling or preference is actually there)')
fix(62, 'LOST', "'I am here'; explain everything; healed today; the closing quote", '“Little one, you don’t have to do anything for me, you don’t have to tell me anything, you don’t even have to be healed.', '“Little one, I am here. You don’t have to explain everything, you don’t even have to be healed today.')
fix(62, 'UNCLEAR', 'the closing quote', 'to help you feel less alone in this world.', 'to help you feel less alone.”')
fix(63, 'LOST', 'a safer relationship', 'a relationship?', 'a safer relationship?')
fix(65, 'LOST', 'inspect before deciding what it means', 'Be as adult as you can)', 'Be as adult as you can)\n\nLook at what’s there before you decide what it means')
fix(65, 'LOST', 'some changes need quiet, sleep, or ordinary time', 'Wait a while for the effect of what you have done to sink in.', 'Wait a while for the effect of what you have done to sink in. Some changes need quiet, sleep or just ordinary time.')
fix(65, 'LOST', 'rest: stop before care becomes another performance; reassess later what actually helped', 'Rest a while and then reassess to see how things are now.', 'Rest, and stop before the care turns into another performance. Then come back later and ask what actually helped.')
fix(76, 'SHIFT', "reparenting doesn't have to be solemn (not a rule to have fun)", "It is important for reparenting to remember to have fun.", "Reparenting doesn't have to be solemn.")
fix(77, 'UNCLEAR', "Emulate's output breaks off ('[...]'); the published: rest doesn't require helplessness, reduce decisions for a defined period, unfinished tasks somewhere visible, the adult keeps watch, you can move, stop and return", body[77], "Resting without being helpless: sometimes you just need to rest, and that doesn't have to mean being helpless. Cut down on decisions for a set period, put unfinished tasks somewhere you can see them, and let the adult in you keep watch. You can still move, stop and come back.")
fix(79, 'SHIFT', "when it feels fake (not 'doesn't work')", 'If speaking or visualization doesn’t work,', 'If speaking or visualization feels fake,')
fix(79, 'SHIFT', 'all three, and us', '“To eat, or to clean my desk, or to not text someone who makes me feel unsafe.”', '“I will eat, clean the desk, and not text the person who makes us feel unsafe.”')
rv = []
for u in d['units']:
    if u['kind'] != 'emulate':
        continue
    b = u['blocks'][0]
    if b in E:
        rv.append({'block': b, 'verdict': 'FIX', 'problems': [{'type': t, 'what': w, 'replace': o, 'with': n} for t, w, o, n in E[b]]})
    else:
        rv.append({'block': b, 'verdict': 'OK'})
links = {11: [{'published': 'Inner Child Self-Love Reparenting Guide', 'new': 'Inner Child Self-Love Reparenting Guide'}], 60: [{'published': 'reparenting therapy', 'new': 'reparenting therapy'}]}
for r in rv:
    if r['block'] in links:
        r['links'] = links[r['block']]
json.dump(rv, open('rev-d/HG14.review.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(sum(len(v) for v in E.values()), 'fixes in', len(E), 'stretches')
