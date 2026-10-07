# Abstract concepts or feelings as agents: Joel's ratings (2026-10-02)

Joel, 21:16: "maby we can do a special training on it if you want to get more clarity you could ask me to rate a number of versions of it for how ai it looks or something (and you also first tell me your guess)." I gave ten lines with my guesses, on a scale of 1 (a person talking) to 5 (AI). His answer, 23:49: "agree, except for 8 i'd say (4). 10: (2)".

| # | line | my guess | Joel |
|---|---|---|---|
| 1 | "So the anger goes there, trying to get some justice." | 4 | 4 |
| 2 | "Politics will become a way of carrying emotional material that people can't name." | 3 | 3 |
| 3 | "Money won't fix that." | 1 | 1 |
| 4 | "Grief doesn't keep a schedule." | 5 | 5 |
| 5 | "My jealousy got the better of me that night." | 1 | 1 |
| 6 | "Loneliness drove a lot of people into those comment sections." | 2 | 2 |
| 7 | "Shame does its work in the dark." | 5 | 5 |
| 8 | "The vision can't determine a departing member's share." | 3 | 4 |
| 9 | "Fear makes the decision before you've even noticed it." | 4 | 4 |
| 10 | "Hope kept that commune going for three more winters." | 3 | 2 |

Where we differed: line 8 is an abstract agent doing an abstract job in a general claim (a published AI sentence from the community article), and he rated it more AI; line 10 is a small, concrete story with a time span, and he rated it more human. The idioms (3, 5) and the aphorisms (4, 7) we agreed on.

## Joel's rulings, 2026-10-07 (community article)

| line | where | Joel |
|---|---|---|
| "Once a kid is already living inside the disagreement, goodwill doesn't answer those questions." | section 8 P28, a rewrite of the published "Goodwill doesn't answer those questions after a child is already living inside the disagreement." | AI. 20:21 UTC: "that AI tell again, in the linter. abstracts doing things." It read AI in about 25 wordings; the cut passed. |
| "Modern life trains us to perform competence while hiding whatever might complicate the performance." | the published article, a later section | Human. 23:50 UTC: "actually very human to say ... so common it's almost cliche, it's not a witty AI quip, you know?" |
| "Nobody's status buys silence." | section 8 P19, from the published "nobody's status buys silence" | Between. 23:50 UTC: "intermediate between an ai quip and what a human would normally say, and it passed pangram so it's ok" |

So the tell is the neat, quotable line where an abstraction does a person's job to make the sentence land ("Grief doesn't keep a schedule", "Shame does its work in the dark", "goodwill doesn't answer those questions"). A phrase people say all the time, even a cliché, is ordinary speech ("Money won't fix that", "Modern life trains us"). A word list can't tell them apart, and neither can a parser: the linter (O6) only collects candidates, and `abstract_agents_prompt.py` has a fresh agent judge them against these ratings.
