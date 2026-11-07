# Pangram prediction scorecard: romance article

Built by `tools/humanization/pangram_ledger.py build` from `articles/romance/humanize/pangram-ledger.jsonl` (the ledger, one line per prediction, result and explanation) and the lane's records from before the ledger. A call is right when I said Human and Pangram read the text 100% Human, or I said AI and it didn't. Detector versions are never pooled: Pangram 4.0 and 4.1 read the same text differently. "Always AI" and "always Human" are what saying the same thing every time would have scored.

## By detector version

| version | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| pangram 4.1, the web app (Joel's account, GUI credits) | 113 | 76 (67%) | 39% | 61% | 85% | 0.228 (base 0.238, 113) |

## pangram 4.1, the web app (Joel's account, GUI credits)

| window | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| the latest 50 | 50 | 38 (76%) | 22% | 78% | 98% | 0.229 (base 0.172, 50) |
| the latest 100 | 100 | 70 (70%) | 37% | 63% | 83% | 0.228 (base 0.233, 100) |
| all | 113 | 76 (67%) | 39% | 61% | 85% | 0.228 (base 0.238, 113) |

The boundary mix (what was checked; accuracy differs a lot between a paragraph and a section):

| scope or kind | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| pair | 45 | 28 (62%) | 56% | 44% | 82% | 0.230 (base 0.247, 45) |
| paragraph | 19 | 14 (74%) | 16% | 84% | 79% | 0.223 (base 0.133, 19) |
| stretch | 2 | 2 (100%) | 50% | 50% | 50% | 0.145 (base 0.250, 2) |
| section | 47 | 32 (68%) | 32% | 68% | 91% | 0.231 (base 0.217, 47) |

Calibration:

| my chance of a 100% Human result | calls | mean chance | read Human |
|---|---|---|---|
| 0.2 to 0.4 | 3 | 0.30 | 33% |
| 0.4 to 0.6 | 103 | 0.52 | 60% |
| 0.6 to 0.8 | 25 | 0.62 | 88% |

## Misses since the ledger (37)

| cause | misses |
|---|---|
| mirrored pair and a list kept | 1 |
| the check had no human context and the perks rewrite kept a list | 1 |
| a polished argument in my second paragraph | 1 |
| a generic reason clause kept | 1 |
| a dashed three-part aside kept | 1 |
| a contrast frame swapped for another | 1 |
| a three-item list in an if-clause | 1 |
| a general reason still tacked on, and a lead-in that stages the questions | 1 |
| split into a bare point and an Otherwise run-on | 1 |
| a stock because-frame, and a cut that broke his callback | 1 |
| a question leading to a tidy conclusion, with the vow link still unsaid | 1 |
| an explained link that reads as a tidy summary | 1 |
| the panel's fixes kept general advice in a first-person frame | 1 |
| an aside added to a summing-up line | 1 |
| his words in a new order still read as general advice | 1 |
| the short check reads his own verses AI too | 1 |
| the pair checks were too short to judge it | 1 |
| his own two closing sentences, joined, read AI High | 1 |
| the lesson's moves carried one sentence, not the paragraphs | 1 |
| a list joined to its reason with because-otherwise reads AI | 1 |
| the triad said with and between its parts and really, the way he talks | 1 |
| the pair of don'ts said as one instruction, helpers without a because | 1 |
| an aphorism pair joined with but, and a staged line said flat, read AI | 1 |
| the point moved up left a bare pair of if-sentences | 1 |
| 438 in the shape of his own advice: no AI window left | 1 |
| his claims said to the reader still read as general claims | 1 |
| his opening joined read Medium; his three claims still Low | 1 |
| the join moved the Low window onto his five-part list | 1 |
| the section by itself reads Low where the whole post read Human | 1 |
| the section by itself reads AI where the whole post read Human | 1 |
| paragraph 34 reads AI in its section whatever I do; the section by itself reads harsher | 1 |
| the section by itself reads harsher, and my splitting join read AI Low | 1 |
| the term explained as a balanced flip read AI | 1 |
| his argument paragraphs read AI in their section, though High by themselves | 1 |
| my changes to his gender claims read AI, and so did his own | 1 |
| 201's closing sentence, unchanged from the live post, read AI Low (40 words) in this short section by itself: a four-item list of what he is expected to do, with a "without ...ing" tail; my change, the bed line said inside its example, read in the High window with the rest | 1 |
| the closing sentence still read as a list of what he is expected to do (Human Low, 41 words, up from AI Low in #108): giving the four items different shapes and making the tail the last item didn't take away the list | 1 |

The latest:

| check | lineage, try | said | read | cause |
|---|---|---|---|---|
| [r11-sit](https://www.pangram.com/history/17571efe-d46a-4d00-8f65-f652735cd2c4) | romance-low-sit, 1 | Human | AI or mixed | an aphorism pair joined with but, and a staged line said flat, read AI |
| [r11-clar](https://www.pangram.com/history/5be9455c-ecdf-47b5-9029-fbd366a7e165) | romance-low-clar, 1 | Human | AI or mixed | the point moved up left a bare pair of if-sentences |
| [r12-s22](https://www.pangram.com/history/5b774f10-ccab-4399-9df1-c6786e26457f) | romance-s22, 2 | AI | Human | 438 in the shape of his own advice: no AI window left |
| [r12-sit34](https://www.pangram.com/history/64bc0365-4a4d-4b26-be2a-e67cd570e349) | romance-low-sit-p34, 1 | Human | AI or mixed | his claims said to the reader still read as general claims |
| [r13-sit34](https://www.pangram.com/history/9aff51d6-f991-4478-8992-900611eb5e97) | romance-low-sit-p34, 2 | AI | Human | his opening joined read Medium; his three claims still Low |
| [r13-slow](https://www.pangram.com/history/db9d87a7-249e-44f8-a1e3-2facc9bc1b6c) | romance-low-slow, 1 | Human | AI or mixed | the join moved the Low window onto his five-part list |
| [r13-disc](https://www.pangram.com/history/3b1a8ec3-9c1c-4834-8a23-3fe5787d139d) | romance-low-disc, 1 | Human | AI or mixed | the section by itself reads Low where the whole post read Human |
| [r14-jeal](https://www.pangram.com/history/c1f9d639-b2d0-417e-b23d-3436710bc371) | romance-low-jeal, 1 | Human | AI or mixed | the section by itself reads AI where the whole post read Human |
| [r15-sit](https://www.pangram.com/history/3d3ed19d-6339-4508-9946-0b2f51be91bc) | romance-low-sit, 2 | Human | AI or mixed | paragraph 34 reads AI in its section whatever I do; the section by itself reads harsher |
| [r15-ideal](https://www.pangram.com/history/c4dd756c-09bc-429b-b1e6-2a40b529c9cf) | romance-low-ideal, 1 | Human | AI or mixed | the section by itself reads harsher, and my splitting join read AI Low |
| [r16-ideal147](https://www.pangram.com/history/d702b4c7-6d17-468b-8845-d52f3c80865d) | romance-low-ideal-p147, 1 | Human | AI or mixed | the term explained as a balanced flip read AI |
| [r16-jeal](https://www.pangram.com/history/184babff-d20a-4383-8e5d-c125b55aa48b) | romance-low-jeal, 2 | Human | AI or mixed | his argument paragraphs read AI in their section, though High by themselves |
| [r16-romance](https://www.pangram.com/history/a150beb8-264c-46c3-9dee-f050b5a0d065) | romance-low-romance, 1 | Human | AI or mixed | my changes to his gender claims read AI, and so did his own |
| [r18-nitty](https://www.pangram.com/history/04b5c93f-aba2-474f-88ed-b02ba1352338) | romance-low-nitty, 1 | Human | AI or mixed | 201's closing sentence, unchanged from the live post, read AI Low (40 words) in this short section by itself: a four-item list of what he is expected to do, with a "without ...ing" tail; my change, the bed line said inside its example, read in the High window with the rest |
| [r19-nitty201](https://www.pangram.com/history/42a42ec6-34ff-4549-b51f-af0bd77b77df) | romance-low-nitty-p201, 1 | Human | AI or mixed | the closing sentence still read as a list of what he is expected to do (Human Low, 41 words, up from AI Low in #108): giving the four items different shapes and making the tail the last item didn't take away the list |

## Lineages still open (tries used of the cap)

| lineage | scope | tries | last read |
|---|---|---|---|
| romance-s2 | pair | 5 of 6 | Mixed |
| romance-s9 | pair | 2 of 6 | Mixed |
| romance-s10 | pair | 4 of 6 | Mixed |
| romance-s17 | pair | 3 of 6 | AI |
| romance-s21 | pair | 4 of 6 | Mixed |
| romance-sec-spiritual-sex | section | 1 of 2 | Mixed |
| romance-tail | stretch | 1 of 2 | Mixed |
| romance-sec-bypass | section | 1 of 2 | Mixed |
| romance-s22-p438 | paragraph | 1 of 6 | AI |
| romance-low-jeal | section | 2 of 2 | Mixed |
| romance-low-ideal | section | 1 of 2 | Mixed |
| romance-low-ideal-p147 | pair | 1 of 6 | Mixed |
| romance-low-romance | section | 1 of 2 | Mixed |

