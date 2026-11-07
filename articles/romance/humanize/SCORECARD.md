# Pangram prediction scorecard: romance article

Built by `tools/humanization/pangram_ledger.py build` from `articles/romance/humanize/pangram-ledger.jsonl` (the ledger, one line per prediction, result and explanation) and the lane's records from before the ledger. A call is right when I said Human and Pangram read the text 100% Human, or I said AI and it didn't. Detector versions are never pooled: Pangram 4.0 and 4.1 read the same text differently. "Always AI" and "always Human" are what saying the same thing every time would have scored.

## By detector version

| version | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| pangram 4.1, the web app (Joel's account, GUI credits) | 133 | 87 (65%) | 41% | 59% | 86% | 0.230 (base 0.241, 133) |

## pangram 4.1, the web app (Joel's account, GUI credits)

| window | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| the latest 50 | 50 | 34 (68%) | 34% | 66% | 98% | 0.234 (base 0.224, 50) |
| the latest 100 | 100 | 66 (66%) | 38% | 62% | 86% | 0.233 (base 0.236, 100) |
| all | 133 | 87 (65%) | 41% | 59% | 86% | 0.230 (base 0.241, 133) |

The boundary mix (what was checked; accuracy differs a lot between a paragraph and a section):

| scope or kind | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| pair | 50 | 31 (62%) | 54% | 46% | 84% | 0.233 (base 0.248, 50) |
| paragraph | 23 | 16 (70%) | 22% | 78% | 83% | 0.231 (base 0.170, 23) |
| stretch | 6 | 4 (67%) | 50% | 50% | 83% | 0.217 (base 0.250, 6) |
| section | 54 | 36 (67%) | 35% | 65% | 91% | 0.227 (base 0.228, 54) |

Calibration:

| my chance of a 100% Human result | calls | mean chance | read Human |
|---|---|---|---|
| 0.2 to 0.4 | 3 | 0.30 | 33% |
| 0.4 to 0.6 | 119 | 0.53 | 58% |
| 0.6 to 0.8 | 34 | 0.62 | 76% |
| 0.8 to 1.0 | 1 | 0.80 | 100% |

## Misses since the ledger (46)

| cause | misses |
|---|---|
| essay-shaped evaluation | 2 |
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
| idiom stacking | 1 |
| generic narrative | 1 |
| overlong join | 1 |
| untouched neighbour | 1 |
| context pattern (S2) | 1 |
| Low windows only | 1 |
| method spent | 1 |

The latest:

| check | lineage, try | said | read | cause |
|---|---|---|---|---|
| [r15-ideal](https://www.pangram.com/history/c4dd756c-09bc-429b-b1e6-2a40b529c9cf) | romance-low-ideal, 1 | Human | AI or mixed | the section by itself reads harsher, and my splitting join read AI Low |
| [r16-ideal147](https://www.pangram.com/history/d702b4c7-6d17-468b-8845-d52f3c80865d) | romance-low-ideal-p147, 1 | Human | AI or mixed | the term explained as a balanced flip read AI |
| [r16-jeal](https://www.pangram.com/history/184babff-d20a-4383-8e5d-c125b55aa48b) | romance-low-jeal, 2 | Human | AI or mixed | his argument paragraphs read AI in their section, though High by themselves |
| [r16-romance](https://www.pangram.com/history/a150beb8-264c-46c3-9dee-f050b5a0d065) | romance-low-romance, 1 | Human | AI or mixed | my changes to his gender claims read AI, and so did his own |
| [r18-nitty](https://www.pangram.com/history/04b5c93f-aba2-474f-88ed-b02ba1352338) | romance-low-nitty, 1 | Human | AI or mixed | 201's closing sentence, unchanged from the live post, read AI Low (40 words) in this short section by itself: a four-item list of what he is expected to do, with a "without ...ing" tail; my change, the bed line said inside its example, read in the High window with the rest |
| [r19-nitty201](https://www.pangram.com/history/42a42ec6-34ff-4549-b51f-af0bd77b77df) | romance-low-nitty-p201, 1 | Human | AI or mixed | the closing sentence still read as a list of what he is expected to do (Human Low, 41 words, up from AI Low in #108): giving the four items different shapes and making the tail the last item didn't take away the list |
| [r21-jeal366](https://www.pangram.com/history/613a0e10-1633-4eed-8792-1c5e763740fe) | romance-low-jeal-p366, 1 | Human | AI or mixed | idiom stacking |
| [r21-ideal147](https://www.pangram.com/history/458f64b3-e69f-43c9-ac06-47304b4a3ece) | romance-low-ideal-p147, 2 | Human | AI or mixed | generic narrative |
| [r22-jeal368](https://www.pangram.com/history/5a483771-c3cd-4cdd-89bc-07f2ba9838aa) | romance-low-jeal-p368, 1 | Human | AI or mixed | essay-shaped evaluation |
| [r22-jeal369](https://www.pangram.com/history/9c5519af-9216-4bfc-9a4c-dfeb4df6a593) | romance-low-jeal-p369b, 1 | Human | AI or mixed | essay-shaped evaluation |
| [r23-jeal367](https://www.pangram.com/history/915fd222-62e5-4597-8b0a-76908ac8259a) | romance-low-jeal-p367b, 2 | Human | AI or mixed | overlong join |
| [r23-ideal](https://www.pangram.com/history/d8ed78a9-d502-409b-9ae0-32a155a3ed74) | romance-low-ideal, 2 | Human | AI or mixed | untouched neighbour |
| [r24-jeal366](https://www.pangram.com/history/4d8ad356-99b1-48ed-824d-5d20731b67a8) | romance-low-jeal-p366, 2 | Human | AI or mixed | context pattern (S2) |
| [r24-ideal](https://www.pangram.com/history/48db01c8-ff82-44b4-aae4-6119f12172d7) | romance-low-ideal, 3 | Human | AI or mixed | Low windows only |
| [r26-jeal](https://www.pangram.com/history/8d1b8eb6-deb9-4a95-a0d9-707cb70ac464) | romance-low-jeal, 4 | Human | AI or mixed | method spent |

## Lineages still open (tries used of the cap)

| lineage | scope | tries | last read |
|---|---|---|---|
| romance-s2 | pair | 5 of 6 | Mixed |
| romance-s9 | pair | 2 of 6 | Mixed |
| romance-s10 | pair | 4 of 6 | Mixed |
| romance-s17 | pair | 3 of 6 | AI |
| romance-s21 | pair | 4 of 6 | Mixed |
| romance-tail | stretch | 1 of 2 | Mixed |
| romance-s22-p438 | paragraph | 1 of 6 | AI |
| romance-low-jeal | section | 4 of 2 | Mixed |
| romance-low-ideal | section | 3 of 2 | Mixed |
| romance-low-jeal-p366 | stretch | 2 of 2 | Mixed |
| romance-low-jeal-p367b | paragraph | 2 of 6 | AI |

