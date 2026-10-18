# Turn 71's installs: register(name, old, new); `python3 t71.py install NAMES RESULTS.json` puts them in.

SP_PARKED = "<!-- Parked from Simple Practices (experiments/t65-guide/PARKED.md, with what each needs from Joel): Journal With Each Hand; And So That's the Way It Happened!; One Intention in the Morning, One Review at Night; Just Like Me. They go here, in that order. -->"


def xandria():
    x1 = d69('sp5-p1-x1')
    y1 = (A / 'experiments/t70-guide/drafts/sp5-p2-y1.txt').read_text(encoding='utf-8').strip()
    x3 = draft('x3-c')
    return '\n\n'.join([
        "<!-- Parked from Simple Practices (experiments/t65-guide/PARKED.md, with what it needs from Joel): Journal With Each Hand. It goes here. -->",
        "## “And So That’s the Way It Happened!”",
        "<!-- Turn 71 (E189, E190): his published line about Xandria first (question 43, 5: \"my words\", Joel 2026-10-17 22:59 UTC, experiments/t70-answers/JOEL-20261017-2259.md), then my humanized version of the rest of the guide's paragraph (experiments/t69-guide/drafts/sp5-p1-x1.txt): say it the way a grandpa would finish a story on the porch, \"Once upon a time…\" if the start is where you get stuck, out of the courtroom and into your life story, a memory you can handle for the first few tries. Alone Human Written (0.0063), https://www.pangram.com/history/29e78b5c-24af-4528-b385-6beadd266412 (turn 69); P1 and P2 together Human Written (0.056, medium, 146 words), https://www.pangram.com/history/ba400925-6f0a-41c8-b029-8aea387ee5ca (round t71a); the h2 Human Written (0.24, high, 226 words), https://www.pangram.com/history/c9f9e639-32af-46ea-a863-1bb460af2d8e (round t71c). Record: experiments/t71-guide/REVIEWS.md. -->",
        x1,
        "<!-- Turn 70 (E190, his moves: a spoken answer to the question, both sides said): saying it doesn't make the memory fiction, it's still what happened as far as you remember it, though details may be fuzzy; nobody's off the hook, you included, and any repair that's owed is still owed; if the line helps, keep it to one line (experiments/t70-guide/drafts/sp5-p2-y1.txt). Alone Human Written (0.14), https://www.pangram.com/history/d44e6e34-fcad-471f-896c-1320522ae688; with P1 Human Written (0.056, medium) (round t71a); the h2 Human Written (0.24, high), https://www.pangram.com/history/c9f9e639-32af-46ea-a863-1bb460af2d8e. -->",
        y1,
        "<!-- Turn 71: the guide's stop signs and its last step (experiments/t71-guide/drafts/x3-c.txt): keep an ear on who's narrating; if the voice starts sneering at the younger you, stop (the courtroom creeping back in, P1's image again); stop too if you feel more ashamed, or floaty and unreal, since more distance won't help with that; when it goes well, ask the younger you in the story what they need from you now. Turn 65's P3 (sp5-p3-b6) read Human alone but AI with P2 (0.99, round t71a); x3-a and x3-b read AI alone (round t71b). Alone Human Written (0.094), https://www.pangram.com/history/da1abaaf-29eb-4f7c-887d-fdf92fa54815 (round t71b); the h2 Human Written (0.24, high, 226 words), https://www.pangram.com/history/c9f9e639-32af-46ea-a863-1bb460af2d8e (round t71c). -->",
        x3,
        "<!-- Parked from Simple Practices (experiments/t65-guide/PARKED.md, with what each needs from Joel): One Intention in the Morning, One Review at Night; Just Like Me. They go here, in that order. -->",
    ])


register('xandria', SP_PARKED, xandria)


AS_PARKED = "<!-- Parked between this section and When the Practice Feels Real but Stays Shallow (experiments/t65-guide/PARKED.md): Altered States Can Deepen the Therapy, Altered States Can Require Reparenting and Non-altered states can feel like this too (his own stories, guides and images; their first-person lines his words, question 43, 7 and 8, except \"If a voice or urge is directing you towards harm ...\", the guide's wording). They go here, in that order. -->"
IMG = "<!-- IMAGE https://substackcdn.com/image/fetch/$s_!wo9Y!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F969adf28-c95f-4c96-bea8-3505a29137cc_638x786.jpeg : A dark black-and-white drawing of a gaunt, long-limbed creature with long stringy hair, crouched over a person asleep in bed with its face right over theirs, by a curtained window. The guide's alt text for it is \"Jinn Al Kaboos – that attacks you while sleeping\". -->"
AS_H1 = "https://www.pangram.com/history/ff62d372-f0bd-409a-8c28-d771cfb0975d"   # round t71h, the h1 as installed: Human Written (0.0059, high, 1209 words)
AS_H2 = "https://www.pangram.com/history/433adc21-9efd-4f86-aed6-30f3fbb81357"   # round t71h, the h2 with its h4: Human Written (0.0046, high, 1009 words)


def altered(p345=None):
    """The three Altered States sections. P345 is the list of draft stems for the h1's last three guide paragraphs, or
    None to park them (they read AI in every version tonight)."""
    def c(s):
        return '<!-- ' + s + ' -->'
    sec = 'the h1 as installed Human Written (0.0059, high, 1209 words), ' + AS_H1 + ' (round t71h)'
    h2 = 'the h2 with its h4 Human Written (0.0046, high, 1009 words), ' + AS_H2 + ' (round t71h), and ' + sec
    parts = [
        '# Altered States Can Deepen the Therapy',
        c("Turn 71 (the overnight run): the guide's first paragraph, with his answer that gentle meditation or self-hypnosis can help (2026-10-12 03:13 UTC, \"should mention both\"; OWNER-EDITS altered-states-gentle-20261012b), pointing back to When the Urge to Escape Arrives, which says it already. His published line \"When you’re ready, my self-hypnosis guide or lucid-dreaming guide can take it deeper.\" is his words (question 43, 7), with the guide's two links. The entheogens are named with no amounts. Loveyhuasca has no link: loveyhuasca.info opens his Ultimate Psychedelic Protocol page, the recipe link E162 keeps out (OWNER-EDITS q8c-acacia-why-20261011c). \"synergize with it\" is the cold read's fix (COLD-READ-t71-altered.md). experiments/t71-guide/drafts/as1-c.txt. Alone Human Written (0.085), https://www.pangram.com/history/ad902e54-5ce0-4f3b-b0d5-613ce6e01c2e; " + sec + ". Record: experiments/t71-guide/REVIEWS.md."),
        draft('as1-c'),
        c("Turn 71: the guide's gate, said once by pointing back to the guards and the caution signs in When the Urge to Escape Arrives (the guide's \"A personal history of voices, ...\" sentence is replaced by his caution signs there, OWNER-EDITS q2-altered-states-voices-20261011), with the guide's borrowing from steady support that won't take over; then his 2026-10-11 03:47 UTC answer 2a, fitted with no words changed but \"as stated\" dropped: \"But feeling attacked by a demon on a psychedelic is not necessarily paranoia. It can be real, and it's also not bad unless you're unprepared. It can be supremely empowering when you can send love and see how it fixes the situation.\" experiments/t71-guide/drafts/as2-c.txt (as2-a and as2-b read Human alone but their gate sentence read AI in the h1). Alone Human Written (0.033), https://www.pangram.com/history/532b8c30-b74b-4561-815f-126062f1775f; " + sec + "."),
        draft('as2-c'),
    ]
    if p345:
        parts += [draft(s) for s in p345]
    else:
        parts.append(c("Parked (experiments/t71-guide/REVIEWS.md; question 45): the guide's last three paragraphs of this h1: a past opening as a reference point (once, only in that state, in ordinary life); the beautiful state as a hook, and what changes after it; if your little one can't receive the love, meet what's in the way rather than going bigger. Every version read AI alone or in the h1 (rounds t71c to t71f, and fresh writers). They go here."))
    parts += [
        '## Altered States Can Require Reparenting',
        c("Turn 71: his paragraph as his October guide has it (question 43, 8: \"my words\", 2026-10-17 22:59 UTC). Alone Human Written (0.0016), https://www.pangram.com/history/778eb69d-e2e9-4955-8877-9e529510a3a0; " + h2 + "."),
        draft('ar1-j'),
        c("Turn 71: his ghosts-and-window paragraph as his guide has it (43, 8). Alone Human Written (0.025), https://www.pangram.com/history/8f74323b-8eac-4d51-a7ee-a56ba71ee9f2; " + h2 + "."),
        draft('ar2-j'),
        c("Turn 71: his sleep-paralysis paragraph as his guide has it (43, 8), then the guide's image and his caption. Alone Human Written (0.0015), https://www.pangram.com/history/c192bdf5-b381-4e84-9e77-64a908bc3eb6; " + h2 + "."),
        draft('ar3-j'),
        IMG,
        draft('ar-cap'),
        c("Turn 71: his 2026-10-12 03:13 UTC answer, next to his sleep-paralysis story as he asked (\"that's worth mentioning\"; OWNER-EDITS altered-states-trance-20261012b), fitted: my \"Sleep paralysis is a trance-like state, and\" before his \"trance can be ...\" (the cold read's fix: nothing had called it a trance), sentences and commas added, and two typos fixed (he typed \"commmitted\" and \"its'\"; I put \"committed\" and \"it's\"). experiments/t71-guide/drafts/ar-tr-b.txt. Alone Human Written (0.0004, medium), https://www.pangram.com/history/0ddeb99e-f4e0-4d0b-a4f7-5a710c4bf97d; " + h2 + "."),
        draft('ar-tr-b'),
        c("Turn 71: his sending-love paragraph as his October guide has it, \"once that love was seen as enduring\" included (43, 8). Alone Human Written (0.00004), https://www.pangram.com/history/3a5c68d7-c881-4429-9edc-31746381ad4b; " + h2 + "."),
        draft('ar4-j'),
        c("Turn 71: his training-others paragraph (43, 8), with the guide's two links. Alone Human Written (0.011), https://www.pangram.com/history/eba950d4-9a16-474f-bc8a-aaab84a85c99; " + h2 + "."),
        draft('ar5-j'),
        c("Turn 71: the guide's astral-plane paragraph as published, with his thugs line (43, 8) and its link. Alone Human Written (0.0016), https://www.pangram.com/history/cae85d43-d7e2-4643-8013-513d1f8543c4; " + h2 + "."),
        draft('ar6-g'),
        c("Turn 71: the guide's first two sentences (\"your frightened little one\" for its \"inner child\"), then his \"If I were to do that\" line (43, 8) moved up so its \"that\" points at borrowing support, then the guide's warning in my words: a presence that enjoys your fear, or demands you hurt or use anybody, yourself included, isn't one of your grown-ups, whatever it says it is (\"demands\" is the cold read's fix: the guide's \"demands harmful obedience\" had become a dare). experiments/t71-guide/drafts/ar7-b.txt. Alone Human Written (0.0096, medium), https://www.pangram.com/history/08027ad7-c8fc-4eac-aa14-8611909857e5; " + h2 + "."),
        draft('ar7-b'),
        c("Turn 71: borrowed adulthood again, from the guide, with its last sentence as published; the cold read's fixes, \"Borrowing support like that\" for an unclear \"It\", and \"starts to become your own\" for the guide's \"can begin internalizing\". experiments/t71-guide/drafts/ar8-b.txt. Alone Human Written (0.0022), https://www.pangram.com/history/44ad3b9c-a11a-482a-a5b5-aa72fe87ba2f; " + h2 + "."),
        draft('ar8-b'),
        c("Turn 71: the guide's \"If a voice or urge ...\" sentence, which he says is the guide's wording, not his, and \"ok if it passes\" (2026-10-17 22:59 UTC); its last sentence without \"capacity\" (O40). experiments/t71-guide/drafts/ar9-a.txt. Alone Human Written (0.0096), https://www.pangram.com/history/4ce4eb4a-ccb7-409a-8cae-786b7f7ead4c; " + h2 + "."),
        draft('ar9-a'),
        '#### Non-altered states can feel like this too',
        c("Turn 71: the guide's two paragraphs as published (the 💀 is his own placement, which EMOJI-LIST.md counts). P1 alone Human Written (0.071), https://www.pangram.com/history/3daa06f9-aecd-4b46-9fe7-5e0d0decbba5; P2 is 43 words, under the web app's 50, so the h4 stands for it: Human Written (0.060, medium), https://www.pangram.com/history/a5a2ee4e-2d14-40ca-8d63-8f45874c9805; " + h2 + "."),
        draft('an1-g'),
        draft('an2-g'),
    ]
    return '\n\n'.join(parts)


register('altered', AS_PARKED, lambda: altered(globals().get('P345')))


WORTHY_LAST = "Be patient with yourself, and gentle, including with the part of you that thinks you should be over it by now. You are more than your pain and your past. That's easy to lose sight of when you've spent so long looking at them. And you aren't alone. There's help, and lots of other people are out there learning to look after their own little ones."
TEA_H2 = "https://www.pangram.com/history/e8c37784-487f-4de7-96d8-6d72844c30a9"   # round t71g: Human Written (0.13, high, 270 words)


def appendix(ap10='ap10-c', ap11='ap11-c', ap14='ap14-a'):
    def c(s):
        return '<!-- ' + s + ' -->'
    h2 = 'the h2 Human Written (0.13, high, 270 words), ' + TEA_H2 + ' (round t71g)'
    return '\n\n'.join([
        WORTHY_LAST,
        '# Appendix',
        c("Parked (experiments/t71-guide/REVIEWS.md; question 46): How This Relates to IFS, with its h3 Related Clinical Work. Every version of the IFS paragraphs read AI as an h2 (rounds t71d to t71f); Related Clinical Work read Human alone (drafts/ap9-d, 0.19) but goes in with its h2. The guide's first-person lines there are waiting on Joel's word (E189). It goes here."),
        '## Teachers and Practice Resources',
        c("Turn 71 (the overnight run): the guide's credits, with its two first-person sentences as published (they wait on Joel's word, E189; OWNER-EDITS appendix-first-person-pending-20261018) and Daja's links. The guide's Gemini-thread sentence is out: https://g.co/gemini/share/fe062bfb8847 opened on \"Link doesn't exist\" (2026-10-18), so it waits on him (question 46). \"the three grown-up jobs\" for the guide's \"Three Adults framing\" (the article's own phrase); the cold read's fix, \"Her work is less ...\" for an unclear \"It's less ...\" (COLD-READ-t71-appendix.md). experiments/t71-guide/drafts/%s.txt. Alone Human Written (0.091), https://www.pangram.com/history/00815251-070a-4e59-89b2-638c74a446c3; %s." % (ap10, h2)),
        draft(ap10),
        c("Turn 71: Lisa Romano; Key, with the guide's link, credited for the Guide's direction and the Bowen-based identity and differentiation work, pointing back to Four Pairs That Commonly Hook the Child (the cold read's fix: my first version only had her pointing out the Guide), and her Nairobi meditation. experiments/t71-guide/drafts/%s.txt. Alone Human Written (0.24, medium), https://www.pangram.com/history/48efac73-5baa-433a-bf91-37a59d2fc3ea; %s." % (ap11, h2)),
        draft(ap11),
        c("Turn 71: Open Path Collective and his Somatic Therapies Guide. 40 words, under the web app's 50, so the h2 stands for it: %s." % h2),
        draft(ap14),
    ])


register('appendix', WORTHY_LAST, appendix)
