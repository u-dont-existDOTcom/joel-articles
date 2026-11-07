# Pangram prediction scorecard: romance article

Built by `tools/humanization/pangram_ledger.py build` from `articles/romance/humanize/pangram-ledger.jsonl` (the ledger, one line per prediction, result and explanation) and the lane's records from before the ledger. A call is right when I said Human and Pangram read the text 100% Human, or I said AI and it didn't. Detector versions are never pooled: Pangram 4.0 and 4.1 read the same text differently. "Always AI" and "always Human" are what saying the same thing every time would have scored.

## By detector version

| version | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| pangram 4.1, the web app (Joel's account, GUI credits) | 74 | 45 (61%) | 49% | 51% | 77% | 0.227 (base 0.250, 74) |

## pangram 4.1, the web app (Joel's account, GUI credits)

| window | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| the latest 50 | 50 | 31 (62%) | 46% | 54% | 72% | 0.227 (base 0.248, 50) |
| the latest 100 | 74 | 45 (61%) | 49% | 51% | 77% | 0.227 (base 0.250, 74) |
| all | 74 | 45 (61%) | 49% | 51% | 77% | 0.227 (base 0.250, 74) |

The boundary mix (what was checked; accuracy differs a lot between a paragraph and a section):

| scope or kind | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| pair | 40 | 24 (60%) | 60% | 40% | 80% | 0.229 (base 0.240, 40) |
| paragraph | 12 | 8 (67%) | 17% | 83% | 67% | 0.222 (base 0.139, 12) |
| stretch | 2 | 2 (100%) | 50% | 50% | 50% | 0.145 (base 0.250, 2) |
| section | 20 | 11 (55%) | 45% | 55% | 80% | 0.233 (base 0.247, 20) |

Calibration:

| my chance of a 100% Human result | calls | mean chance | read Human |
|---|---|---|---|
| 0.2 to 0.4 | 3 | 0.30 | 33% |
| 0.4 to 0.6 | 65 | 0.52 | 49% |
| 0.6 to 0.8 | 19 | 0.63 | 84% |

## Misses since the ledger (29)

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

The latest:

| check | lineage, try | said | read | cause |
|---|---|---|---|---|
| [r05-s10](https://www.pangram.com/history/4b0f3653-382c-4562-a675-db6b9de90536) | romance-s10, 4 | Human | AI or mixed | his words in a new order still read as general advice |
| [r05-s21](https://www.pangram.com/history/1a346e61-fe80-4de3-acce-f6500fd1d2a7) | romance-s21, 3 | Human | AI or mixed | the short check reads his own verses AI too |
| [r06-secB](https://www.pangram.com/history/1a6ad01b-2191-4783-9d48-ad82d43642ac) | romance-sec-whole-world, 1 | AI | Human | the pair checks were too short to judge it |
| [r06-secD](https://www.pangram.com/history/76595855-5f60-40c7-bb11-8f79671182b0) | romance-sec-vows, 1 | Human | AI or mixed | his own two closing sentences, joined, read AI High |
| [r08-s22](https://www.pangram.com/history/3db3f31c-8a87-4199-96ab-00252e5cf2d3) | romance-s22, 1 | Human | AI or mixed | the lesson's moves carried one sentence, not the paragraphs |
| [r09-dam](https://www.pangram.com/history/6e961014-b2c3-4ac1-a1f9-fc14ed151a24) | romance-low-dam, 1 | Human | AI or mixed | a list joined to its reason with because-otherwise reads AI |
| [r10-s22a](https://www.pangram.com/history/ead32a56-1843-4b68-a719-32a2e9883f21) | romance-s22-p437, 1 | AI | Human | the triad said with and between its parts and really, the way he talks |
| [r10-s22c](https://www.pangram.com/history/23efa093-652e-4eba-b470-11ec7271ffc2) | romance-s22-p439, 1 | AI | Human | the pair of don'ts said as one instruction, helpers without a because |
| [r11-sit](https://www.pangram.com/history/17571efe-d46a-4d00-8f65-f652735cd2c4) | romance-low-sit, 1 | Human | AI or mixed | an aphorism pair joined with but, and a staged line said flat, read AI |
| [r11-clar](https://www.pangram.com/history/5be9455c-ecdf-47b5-9029-fbd366a7e165) | romance-low-clar, 1 | Human | AI or mixed | the point moved up left a bare pair of if-sentences |
| [r12-s22](https://www.pangram.com/history/5b774f10-ccab-4399-9df1-c6786e26457f) | romance-s22, 2 | AI | Human | 438 in the shape of his own advice: no AI window left |
| [r12-sit34](https://www.pangram.com/history/64bc0365-4a4d-4b26-be2a-e67cd570e349) | romance-low-sit-p34, 1 | Human | AI or mixed | his claims said to the reader still read as general claims |
| [r13-sit34](https://www.pangram.com/history/9aff51d6-f991-4478-8992-900611eb5e97) | romance-low-sit-p34, 2 | AI | Human | his opening joined read Medium; his three claims still Low |
| [r13-slow](https://www.pangram.com/history/db9d87a7-249e-44f8-a1e3-2facc9bc1b6c) | romance-low-slow, 1 | Human | AI or mixed | the join moved the Low window onto his five-part list |
| [r13-disc](https://www.pangram.com/history/3b1a8ec3-9c1c-4834-8a23-3fe5787d139d) | romance-low-disc, 1 | Human | AI or mixed | the section by itself reads Low where the whole post read Human |

## Lineages still open (tries used of the cap)

| lineage | scope | tries | last read |
|---|---|---|---|
| romance-s2 | pair | 5 of 6 | Mixed |
| romance-s9 | pair | 2 of 6 | Mixed |
| romance-s10 | pair | 4 of 6 | Mixed |
| romance-s17 | pair | 3 of 6 | AI |
| romance-s21 | pair | 4 of 6 | Mixed |
| romance-sec-spiritual-sex | section | 1 of 2 | Mixed |
| romance-sec-vows | section | 1 of 2 | Mixed |
| romance-tail | stretch | 1 of 2 | Mixed |
| romance-sec-bypass | section | 1 of 2 | Mixed |
| romance-s22-p438 | paragraph | 1 of 6 | AI |
| romance-low-sit | section | 1 of 2 | Mixed |
| romance-low-slow | section | 1 of 2 | Mixed |
| romance-low-disc | section | 1 of 2 | Mixed |

