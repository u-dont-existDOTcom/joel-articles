# Write It. Don't Send It Yet.: the Tyler paragraphs, 2026-09-27

Status: **INSTALLED 2026-09-27. Owner-accepted (Joel, 20:29 UTC: "tyler's story is good"). All pass: P4, P5, P5 + P6, and the whole section (100% Human, 498 words).**

## Trigger

Joel, 2026-09-27 04:19: "i wonder if the lesson i'm giving here to my friend tyler now about how to voice your concerns about others' behaviors coming from concern about your own behaviors would fit somewhere in the guide… i think it could go into Write it. don't send it yet since that's where i talk about high IQ & EQ communication when you're mad."

Joel, 16:29: "yes include the smoking example with Tyler and name him, he would be honored actually, you can include the story directly rather than make it abstract. My friend Tyler experienced this, then wasn't sure he responded correctly, and also not sure if he should have 'thrown the first stone' since he was a sinner also, then we came to this better version showing he was actually the perfect person to point out the problem, because he had the problem himself. Considering he's an evangelical Christian with extremely strong beliefs and preaching on youtube, the fact that he really appreciated how I was interpreting Jesus' message is pretty important to me."

## Authority

Joel's pasted chat (2026-09-27 04:19; kept only in the session, not in the repo). Every fact below is from it or from his 16:29 message:
- Tyler asked the smoker, "do you think it's wise to smoke in front of an infant?"
- The reply: "do you think it's wise to mind your own business?"
- Tyler: "well I believe in Christ so I thought you might care about life too."
- Tyler: "I smoked in front of an infant before and I'm ashamed of it now."
- Tyler: "look at myself, don't pull their speck from their eye when I've got a log in mine".
- Joel: "if you actually have the problem they have, and you want to call them out for it, call yourself out for it instead".
- Joel: "it's also in the way your voice sounds too like you can say all the right words but if the tone is accusatory it doesn't matter".
- Joel's version: "hey man, when I was younger I smoked cigarettes, and I smoked in front of an infant not realizing how selfish that was… and I notice you doing the same thing… I would ask you to please have some concern for him. I have a young child now, so this kind of thing really touches me deeply…" Tyler: "Let's change concern to compassion".

Left out: the photos, where the man works, the delivery job and the other stories in the chat. None of it is part of the lesson, and it's the stranger's privacy.

**Scripture, verified** (ESV, Bible Gateway, https://www.biblegateway.com/passage/?search=Matthew%207%3A3-5%3BJohn%208%3A7&version=ESV):
- Matthew 7:5: "You hypocrite, first take the log out of your own eye, and then you will see clearly to take the speck out of your brother's eye."
- John 8:7: "Let him who is without sin among you be the first to throw a stone at her."
- Tyler quoted the log and speck himself. Using its second half as the answer to his first-stone worry is my addition, and it goes to Joel as that.

## Placement

After P3, which ends "So what was he actually trying to say? A lot of the time it's just 'that hurt.'" P4 opens with the other answer, "Other times it's 'I did this too.'", so the story is the writer's other message. The section is about what to say when you're mad, and this is Joel's own lesson on how.

## Drafts

**P4.** 87 words, sha256 975e7a9d4048f2f0fe4229390bfdbe69cb54d9823e3658238ecf4a17ec292147.

> Other times it's "I did this too." My friend Tyler saw a guy smoking in front of a baby and asked him if he thought that was wise. The guy asked if he thought it was wise to mind his own business, and Tyler said, "Well, I believe in Christ, so I thought you might care about life too." Afterward he wasn't sure he'd handled it right, or whether he should have thrown the first stone at all, since he'd smoked in front of a baby himself.

**P5.** 119 words, sha256 e0bae649ef72e1f78d576435a9c3f7d922db2fc57ee68cf91c76c5f6679b6836. Joel's line is owner text.

> But Jesus also said to take the log out of your own eye first, and then "you will see clearly to take the speck out of your brother's eye." That's exactly what made Tyler the right person to say something. If you actually have the problem they have, and you want to call them out for it, call yourself out for it instead. What we came up with was something like, "Hey man, when I was younger I smoked in front of an infant, not realizing how selfish that was, and I notice you doing the same thing. I'd ask you to please have some compassion for him. I have a young child now, so this really touches me."

**P6.** 48 words, sha256 4d6b0d8699ff58f5af3337f95e18b382f2fec98ea6ec441883a65e68c12c1472. The first two sentences are Joel's. It's under 50 words, so it's checked with P5 (P5 + P6, sha256 ced1f026e37bfeb35567a581f4b12768d4a71819b92bddb6e945d6affad4eb8d) and in the section.

> It's also how your voice sounds, though. You can say all the right words, but if the tone is accusatory, it doesn't matter. Tyler's an evangelical Christian who preaches on YouTube, so it meant a lot to me that he liked this take on what Jesus was saying.

## Gate

**Linter.**
- P4: REVIEW. E41's "you might" is inside Tyler's quote: KEEP. B4 on the exchange sentence: KEEP, since it's the two lines of dialogue.
- P5: REVIEW, with Joel's line passed as owner. B4 on the version: KEEP, since it's the quote.
- P6: CLEAR.

**Sense read.**
- P4: sometimes what the angry writer means is "I did this too". Tyler saw a man smoking by a baby, asked if that was wise, got "is it wise to mind your own business?", and answered with Christ. Then he doubted himself, and wondered if he'd thrown the first stone, having done it himself.
- P5: Jesus also said to take the log out first and then you'll see clearly to help with the speck. That's what made Tyler the right person to speak. Joel's rule follows, then the better version.
- P6: tone matters as much as words, and it meant a lot that a preacher liked this reading.
- Each paragraph says what it refers to.

**Marching (E66).** P4 is a story in its order with one bridge line. P5 goes answer, rule, version. It's a sequence, but the version is a long quoted thing and not a step. P6 has two beats.

**Last-sentence test (E74).**
- P4 ends on the doubt, which is where the story leaves off, not a moral.
- P5 ends on the version.
- P6 ends on Joel's own stake, which is new.
- None of them is a restatement or a "So".

**Inventory.**
- T01 ABSENT: Joel's first person is his own ("What we came up with"; "it meant a lot to me", from his message).
- T02 ABSENT.
- T03 UNCERTAIN → KEEP: "Other times it's 'I did this too'" is the bridge from P3's question, and it's the live thought, not a generic connector.
- T04 ABSENT: a real story, in the order it happened.
- T05 ABSENT: real details.
- T06 ABSENT.
- T07 ABSENT.
- T08 UNCERTAIN → KEEP: "That's exactly what made Tyler the right person to say something" interprets the Jesus line, but it's Joel's own reading (16:29: "he was actually the perfect person to point out the problem, because he had the problem himself").
- T09 ABSENT.
- T10 ABSENT.
- T11 see T03.
- T12 ABSENT.
- T13 ABSENT: the mirrored "is it wise to mind your own business?" is a detail nobody would invent.
- T14 ABSENT.
- T15 ABSENT.
- T16 ABSENT.
- T17 UNCERTAIN → KEEP: Joel's rule is a principle, but it's his, from the chat.
- T18 ABSENT.
- T19 UNCERTAIN → KEEP: "Other times it's 'I did this too'" states the point before the story. It's the answer to P3's question, which is why it's there.
- T20 ABSENT.
- T21 ABSENT.
- T22 ABSENT: 0.0 coach phrases outside quotes.
- T23 ABSENT.
- T24 ABSENT.
- T25 ABSENT.
- T26 ABSENT: "smoked in front of an infant/baby" three times, in the story, in Tyler's past and in the version, since that's the point.
- T27 ABSENT.
- T28 n/a (the section ends on Joel's stake).
- T29 ABSENT.
- C01 ABSENT.
- C02 ABSENT: "he" is Tyler throughout P4; "him" in the version is the baby.
- C03 ABSENT: every fact is from the chat or Joel.
- C04 ABSENT: the scripture is verified, and it's linked in the article.

**Stance ledger.**
- The section's stance: communicate when mad without regretting it (P2), and find what the writer was trying to say (P3). The story is both.
- The article already cites Jesus (Borrow One Competency's "What would Jesus do?").
- Nothing here says to stay silent. Joel's point is that the person who has the problem is the right one to raise it.

**Checks planned:** P4 alone; P5 alone; P5 + P6; the whole section (P1–P6).

## Results (Pangram 4.0, Joel's account, 2026-09-27, the turn that started 16:31)

- P4 alone: Human Written, 100% Human, 91 words scanned (short text).
- P5 alone: 100% Human, 122 words scanned (short text). The first click didn't submit; the unchanged, hash-verified text was submitted on the second.
- P5 + P6: 100% Human, 173 words scanned (short text).

## The whole section, recorded before its call

P1–P3 (as installed) and P4–P6. 480 words, sha256 8fdd4401d5a20de33f3f4cb2e8c567aa6064a86a89acfb207b9fa48914b9383b. Scratch: `tyler/section_r1.txt`.

**Section-scale inventory (E70).**
- T02 ABSENT: instructions in P1, P2 and P5, spread out.
- T03 ABSENT: P4's opener answers P3's question.
- T08 ABSENT.
- T20 ABSENT: the endings are a cooler place, the timing, "that hurt", the doubt, the quoted version, and Joel's stake.
- T26 ABSENT: "Jesus" in P5 and P6 is the same thread.
- T29 ABSENT in each paragraph.

**Result (the whole section):** Human Written, 100% Human, 498 words scanned, no short-text caveat. The first coordinate click didn't submit; the hash-verified text was submitted by the button's ref. Installed as a candidate after P3, with the Matthew 7:3-5 link on the quote.
