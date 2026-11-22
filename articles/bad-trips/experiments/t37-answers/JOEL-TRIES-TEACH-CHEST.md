# His twelve tries on round 37's teaching card (TEACH-CHEST), read from his Pangram history

His round-37 export of 2026-11-12 16:47:47 UTC (`review/r37/ANSWERS-R37-20261112-1647.json`) has his version in "Your
version" and, in the comment, a link to each of his twelve checks with what he changed. He started from my chest-c3
(`humanize/h46-20261112/TEST-chest-c3.txt`, AI Generated, 100%, 2f1b6aa2), which three fresh readers of my own read
against his fixes had passed ("MARKED: none" on the last). Texts and readings from his history
(web.pangram.com/api/history/<uuid>/, read 2026-11-12 16:5x UTC); windows as label and confidence (H/A, High/Medium/Low)
with their word counts. Each step, what changed from the one before, and his note:

1. 662fc897, AI Generated, 100% (A-M 52, A-L 19, A-M 19, A-L 21, A-M 31): "The pain is severe, or new to them." and "It
   won't let up or keeps getting worse." made one line, "The pain is severe or keeps getting worse."; "I'd still use DMSO"
   made "I'd still use the same treatment". ("first i removed some redundancy, which helped reduce ai conf")
2. 9a67129a, AI Detected, 52% (H-M 23, H-L 42, A-L 40, A-M 14, A-L 17): "For chest pain that's mild and familiar, I'd just
   use DMSO, as long as it's holding steady and they're fully alert." made "For steady chest pain that's mild, I'd just use
   DMSO, as long as they're fully alert." ("removed some more redundancy, now it's half human (and btw i had no idea what
   "familiar" chest pain was talking about, why would that be in an emergency manual, that woul dbe for a general health
   manual)")
3. a95a5939, 53%: "The pain is severe or keeps getting worse." made "The pain keeps getting worse." ("removed one more
   redundant word, helped a bit")
4. f8da7677, 53.5%: "still let the medics check them." made "still let the medics check them later." ("then i clarified
   with one word at the end and it became 1% more human")
5. 7146713a, 54% (H-M 53, H-L 8, A-L 40, A-M 32): "keeps getting worse" made "is worsening". ("now i changed the ai
   phrasing "keeps getting ..." and the ifrst half went from low conf to med conf human")
6. 1b6974d8, Human Written (H-H 41, H-M 29, H-L 47): "It's more serious if:" made "For the following more serious signs
   (or if unsure), I'd also call medics:"; "Then I'd still use the same treatment, but call medics at the same time. When
   you're unsure which kind it is, treat it as the serious kind." cut; "DMSO can also block ..." made "Keep in mind that
   DMSO can also block ...". ("then i noticed the payoff was way too late, moved that up, now it's all human, but only a
   third is high conf and still some is low conf")
7. 8f2d89bb, Human Written (H-M 45, H-L 19, H-M 19, H-L 42): my chest-c3 with his first sentence and only the payoff
   moved up (the lead-in as in 6, my seven list lines unchanged, my two after-list sentences cut, my last sentence as I had
   it). ("then i tested only the last payoff fix on the original, and that's all it needed to flip human")
8. cc512b29, Human Written (H-H 41, H-M 80): 6, with the last sentence "so even if the pain fades, it could still be worth
   having a medical checkup later." ("went back to the one before that bc it's better, then fixed the low conf section by
   clarifying")
9. 41c0688b, Human Written (H-M 67, H-L 51): "Hard movement brought it on, like dancing or climbing stairs." made "Hard
   movement (dancing, climbing) brought it on."; "From the chest it spreads" made "It spreads from the chest". ("clarified
   what hard movement is by moving the explanation closer, that didn't help")
10. c326e6a2, Mostly Human Written, 5% (H-M 41, H-L 28, H-L 51): "(dancing, climbing)" made "(like dancing or climbing)".
    ("tried uncompressing the clarification of hard movement (like...), that made it more AI")
11. ab03714d, Human Written, High 120: "Shortness of breath or sweating comes with it." made "Shortness of breath or
    sweating shows up also." ("even with the last change that made it worse, i changed only one thing, removed the third
    "it" (too many its!), and now it's all high conf human")
12. cabd68b6, Human Written (H-H 46, H-M 9, H-H 70): "I'd just use DMSO" made "I'd just use DMSO + magnesium chloride on
    the chest". ("but i want to add magnesium chloride and explain this is topical for chest pain (everywhere it's
    mentioned, tho hopefully only here), this is still high conf human of course")

His final, the text of 12, in the guide (`review/r37/apply_r37.py`):

    For steady chest pain that's mild, I'd just use DMSO + magnesium chloride on the chest, as long as they're fully
    alert. For the following more serious signs (or if unsure), I'd also call medics:
    - The pain is worsening.
    - Hard movement (like dancing or climbing) brought it on.
    - It spreads from the chest into an arm or the jaw.
    - Shortness of breath or sweating shows up also.
    - Any of the stroke signs from the brain checks above show up, like slurred speech or a drooping face.
    - They feel faint, or they collapse.

    Keep in mind that DMSO can also block pain signals, so even if the pain fades, it could still be worth having a
    medical checkup later.

The minimal pair: 7 against my chest-c3. The same list, and the action ("I'd also call medics") said before it instead of
after it, took it from AI Generated, 100% to Human Written.
