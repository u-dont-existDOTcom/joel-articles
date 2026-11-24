# Round 56: what happened to each point of his answers (his export of 2026-11-24 21:26 UTC)

[His answers](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/articles/bad-trips/review/r56/ANSWERS-R56-20261124-2126.json),
put in by [apply_r56.py](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/articles/bad-trips/review/r56/apply_r56.py)
and recorded by [record_r56.py](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/articles/bad-trips/review/r56/record_r56.py)
([every check](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/articles/bad-trips/humanize/h75-20261124/RESULTS.md)).

## CHLORIDE-CLAIM

| His point | Where it went |
|---|---|
| "remove the source then if there's no source" | The link to the absorption study (Firoz and Graber 2001) is out of the amounts paragraph, and the guide's record of his edits now holds its address as one no link may point to, so no later rewrite brings it back (`must_not_link`, a new check with its test). The other link in the paragraph, on diarrhea, stays: its study says what the sentence says. |
| "but i definitely can't recommend using anything other than what i know works best" | The sentence says his claim as what he knows, in the words of his round-55 comment, where turn 66 had narrowed it to what the study shows: "I use it mostly because it's what I know works best: it absorbs faster and better than any other form, so you can see how it's helping, usually within a minute." The API reads the paragraph [Human High in one window](https://www.pangram.com/history/f330e220-03a5-4821-9919-6427d4660e2a). |

## WIFE-LAST

| His point | Where it went |
|---|---|
| "a" | In: his second wife's paragraph ends "since potassium gets depleted once magnesium runs low". The API reads it [Human High in one window](https://www.pangram.com/history/e74a7e6b-7047-4e54-af54-64070d2b5879) with one space after "At the hospital,". |

## The card's slip

The question showed him "poorly absorbed (4%%)": its string was written for %-formatting and never formatted. From
2026-11-25 the review tool refuses a card or an intro that shows "%%" (`percent_problems`, with tests; lesson
bad-trips-2026-11-24t), and round 57's page was checked for it by hand.
