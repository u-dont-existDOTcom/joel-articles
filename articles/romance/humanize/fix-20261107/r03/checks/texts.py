"""r03's check texts in the romance article (2026-11-07). The monastic paragraph's third and fourth tries (S2: r01 and r02
read AI; the tell panel in ../panel-s2/PANEL.md agreed on the perks list and the balanced closing pair), second tries at S6,
S7, S8, S10 and S11 that go back to the live post's words and change only the sentences in its windows, and first tries at
S14 to S21 (../../live-check/AI-WINDOWS.json). Each text has the paragraph it leans on, or enough of his paragraphs before it
to reach Pangram's 50 words. Unchanged words are the live post's, as the seed tab shows them."""
TEXTS = {
    # S2, try 3: his two paragraphs kept; the perks list broken up (room and board, status, nobody expects you to ...);
    # the West sentence keeps his picture; the closing pair keeps his concession and gives the general point a place.
    'r03-s2b': ('Forced celibacy doesn’t abolish anyone’s sexuality. For most people it eventually sends it somewhere weird. '
                'Why wouldn’t it?\n\n'
                'Some people become monks for practical reasons too. In a poor country, the robes get you free room and '
                'board and status, and nobody expects you to earn a living or raise a family anymore. In the West the free '
                'food probably isn’t the draw, but a guy nobody respected much as a layman can shave his head, become '
                'Venerable Somebody, and suddenly people are bowing to him.\n\n'
                'Of course, he may sincerely want liberation too. Most of us have more than one reason for the big choices '
                'we make.'),
    # S2, try 4: the concession first, his "People can want several things at once" kept as the reason, and the
    # paragraph ends on his bowing picture instead of a balanced closing pair (the two paragraphs become one).
    'r03-s2c': ('Forced celibacy doesn’t abolish anyone’s sexuality. For most people it eventually sends it somewhere weird. '
                'Why wouldn’t it?\n\n'
                'Of course, plenty of monks sincerely want liberation. But people can want several things at once, and some '
                'become monks for practical reasons too. In a poor country, the robes get you free room and board and '
                'status, and nobody expects you to earn a living or raise a family anymore. In the West the free food '
                'probably isn’t the draw, but a guy nobody respected much as a layman can shave his head, become Venerable '
                'Somebody, and suddenly people are bowing to him.'),
    'r03-s6': ('Modern life barely has an intermediate stage between being interested in somebody and getting sexually '
               'entangled. One old example is bundling, a mostly extinct practice now especially associated with the Amish, '
               'even though it existed much more widely. Courting couples could spend the night together in bed, usually '
               'clothed, with the idea that they could talk and be close without having sex, which sounds a lot like the '
               'missing middle I’m talking about.\n\n'
               'Well, it didn’t exactly solve the problem. In late-eighteenth-century New England, where lots of couples '
               'bundled, 30–40 percent of brides were already pregnant on their wedding day. So it wasn’t a very reliable '
               'way to keep courtship nonsexual. I’m not trying to bring bundling back. I just think we need some stage that '
               'everybody recognizes, where two people can explore tenderness and attraction without immediately sliding '
               'toward sex, moving in together, and a life bond.'),
    'r03-s7': ('The most recent conflicts are the best place to look. Were you able to regulate at all during the conflict? What '
               'did you do to the other person? How did you repair afterward? What did you learn? Has your judgment gotten '
               'better, or do you keep falling for the same stuff?\n\n'
               'I’d also want to know what their friends or exes would say. Nobody’s a great judge of their own progress, me '
               'included.\n\n'
               'And when somebody tells me, “I shut down,” I ask what that means. Did you stop talking to your partner for '
               'days? Did they feel abandoned?'),
    'r03-s8': ('It shouldn’t have to happen that way, though. It’s a bad shortcut to the divine archetypes.\n\n'
               'Legitimately seeing someone as amazing doesn’t depend on what the seeing gives you. You’re already lost in '
               'the sauce once you start identifying with the way you see them, like she’s perfect, this is destiny, I’m '
               'the one who finally found her.'),
    'r03-s10': ('Toft also points out that a man can get feminine energy from nature, music, poetry, art, flowers, food, and '
                'other parts of life. I like that idea. A girlfriend shouldn’t have to be my only source of beauty, softness, '
                'sensuality, and inspiration.\n\n'
                'I’d rather make alone time normal from the start. Otherwise I end up waiting until I’m already overwhelmed '
                'and suddenly announcing, “I need time for myself!” and by then it can easily sound like I need time away '
                'from her.'),
    'r03-s11': ('The problem is when the role takes over the relationship. She can be my little girl sometimes without becoming '
                'my child. She still has to remain responsible for her life and keep reparenting herself.\n\n'
                'It can run the other way too. I make her Mom when I expect her to regulate me, soothe every wound, organize '
                'my life, and keep me functional.'),
    'r03-s14': ('Some women may only get turned on by pathology and danger. A woman may also feel her man has become so feminine '
                'that there is no contrast left.\n\n'
                'A lot of women want to feel that the man is dangerous in some way, but preferably in an exciting and '
                'defending way rather than threatening. Beauty and the Beast is a “tale as old as time” for a reason.\n\n'
                'So can a couple keep the polarity alive inside the safety?'),
    'r03-s15': ('If I have to prove I’m the man, something’s already fake, because then I have to defend that identity every '
                'time I hesitate or slip up.\n\n'
                'I don’t actually walk around thinking I’m some super-masculine guy. I cry, I need help, I get things wrong. '
                'Bee once called me her “wife.” I don’t recommend that as a polarity exercise, by the way.'),
    'r03-s16': ('Esther Perel makes the distinction that fantasy is play rather than a real-life request. So someone with a rape '
                'fantasy isn’t asking to actually be raped.\n\n'
                'A couple can keep a fantasy in their heads, or they can agree to act some part of it out.\n\n'
                'Fantasy should also add to arousal, not be the only way to get there, because I want to be able to enjoy '
                'the actual woman and the actual experience too.'),
    'r03-s17': ('Kim Anami goes further and treats sexual energy itself as a path to healing and spiritual awakening.\n\n'
                'She’s also collected a ton of stories from students who say the effects didn’t stay in the bedroom and '
                'spilled over into their health, work, money, creativity, and everything else. Her jade-egg practice is a '
                'preliminary training for the cervical O: pelvic-floor strength, attention, and arousal without needing a '
                'partner.'),
    'r03-s18': ('Let me show you how this looked for me. I’ve noticed in my own relationships that whenever a serious issue '
                'arises, both of us tend to turn to our separate circles of friends for support. Then I resent the one-sided '
                'story she’s telling, she resents the one-sided story I’m telling. Some of the friends may even be exes who '
                'want us to break up, and eventually neither of us wants to talk to the other’s friends anymore. That’s a '
                'pretty terrible time to be trying to run the rest of life with two people. If one person goes down, the '
                'other becomes the whole backup system for housing, money, children, health, and emotional crises. Who even '
                'has time for the relationship itself at that point?'),
    'r03-s19': ('Having the same confidant creates the opposite problem: now you may not have a release valve when you want '
                'privacy from your partner. There isn’t one perfect arrangement.\n\n'
                'If you do have separate confidants, you need enough emotional maturity to remember they will automatically '
                'be biased toward you. Take what they say with a grain of salt, since they’re only hearing your side, usually '
                'while you’re upset, and they may just be trying to protect you.'),
    'r03-s20': ('Then the questions change for me. If the romance changes, which parts are still supposed to remain? Are we '
                'promising actions, or low-key pretending to promise permanent feelings? Which needs are we still going to '
                'meet outside the relationship?\n\n'
                'And the biggie: what happens if one of us falls in love with someone else? What counts as betrayal, and '
                'what’s just a sign we need a serious talk? If our lives change, can we honestly sit down and rethink the '
                'agreement? If we split up, what do we still owe each other, and what do we owe our kids, if we have any?'),
    'r03-s21': ('We also find something like my warning in the New & Old Testaments. Ecclesiastes 5:4–6 says it is better not to '
                'make a vow than to make one and fail to keep it. If you tell the priest you didn’t mean what you promised, '
                'the passage warns that God will be angry and destroy your work.\n\n'
                'Matthew 5:33–37 and James 5:12 are stranger still beside wedding vows: let your “Yes” be “Yes” and your '
                '“No” be “No,” and anything beyond that comes from evil. If your yes is trustworthy, why would it need '
                'another layer? The extra promise actually starts to make me suspicious.'),
}
