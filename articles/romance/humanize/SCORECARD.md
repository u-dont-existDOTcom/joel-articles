# Pangram prediction scorecard: romance article

Built by `tools/humanization/pangram_ledger.py build` from `articles/romance/humanize/pangram-ledger.jsonl` (the ledger, one line per prediction, result and explanation) and the lane's records from before the ledger. A call is right when I said Human and Pangram read the text 100% Human, or I said AI and it didn't. Detector versions are never pooled: Pangram 4.0 and 4.1 read the same text differently. "Always AI" and "always Human" are what saying the same thing every time would have scored.

## By detector version

| version | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| pangram 4.1, the web app (Joel's account, GUI credits) | 49 | 31 (63%) | 57% | 43% | 76% | 0.220 (base 0.245, 49) |

## pangram 4.1, the web app (Joel's account, GUI credits)

| window | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| the latest 50 | 49 | 31 (63%) | 57% | 43% | 76% | 0.220 (base 0.245, 49) |
| the latest 100 | 49 | 31 (63%) | 57% | 43% | 76% | 0.220 (base 0.245, 49) |
| all | 49 | 31 (63%) | 57% | 43% | 76% | 0.220 (base 0.245, 49) |

The boundary mix (what was checked; accuracy differs a lot between a paragraph and a section):

| scope or kind | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| pair | 40 | 24 (60%) | 60% | 40% | 80% | 0.229 (base 0.240, 40) |
| paragraph | 3 | 3 (100%) | 0% | 100% | 100% | 0.124 (base 0.000, 3) |
| stretch | 2 | 2 (100%) | 50% | 50% | 50% | 0.145 (base 0.250, 2) |
| section | 4 | 2 (50%) | 75% | 25% | 25% | 0.234 (base 0.188, 4) |

Calibration:

| my chance of a 100% Human result | calls | mean chance | read Human |
|---|---|---|---|
| 0.2 to 0.4 | 2 | 0.28 | 0% |
| 0.4 to 0.6 | 44 | 0.51 | 41% |
| 0.6 to 0.8 | 10 | 0.62 | 90% |

## Misses since the ledger (18)

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

The latest:

| check | lineage, try | said | read | cause |
|---|---|---|---|---|
| [r02-s7](https://www.pangram.com/history/b214bd97-7c58-43f3-a521-4182f7b09433) | romance-s7, 1 | Human | AI or mixed | a generic reason clause kept |
| [r02-s8](https://www.pangram.com/history/c764c228-211b-4a27-bacd-f4165453876d) | romance-s8, 1 | Human | AI or mixed | a dashed three-part aside kept |
| [r02-s10](https://www.pangram.com/history/a6a557ab-5ea6-42b9-b3c1-6fe8d337f4db) | romance-s10, 1 | Human | AI or mixed | a contrast frame swapped for another |
| [r02-s11](https://www.pangram.com/history/84f5d138-9e2b-413c-8f68-00c170c3e702) | romance-s11, 1 | Human | AI or mixed | a three-item list in an if-clause |
| [r03-s7](https://www.pangram.com/history/3d834650-6176-4c1d-8335-2120f9396a73) | romance-s7, 2 | Human | AI or mixed | a general reason still tacked on, and a lead-in that stages the questions |
| [r03-s10](https://www.pangram.com/history/33b3a11b-cf85-45b0-9ced-eae1f40802a6) | romance-s10, 2 | Human | AI or mixed | split into a bare point and an Otherwise run-on |
| [r03-s15](https://www.pangram.com/history/4d84986b-1c55-4cbe-b422-8b7531e3f8d4) | romance-s15, 1 | Human | AI or mixed | a stock because-frame, and a cut that broke his callback |
| [r03-s21](https://www.pangram.com/history/7e5d0094-0f22-447a-bca2-defd47cb3131) | romance-s21, 1 | Human | AI or mixed | a question leading to a tidy conclusion, with the vow link still unsaid |
| [r04-s21](https://www.pangram.com/history/f71abb17-8e0f-49e8-8994-511b346467c1) | romance-s21, 2 | Human | AI or mixed | an explained link that reads as a tidy summary |
| [r04-s10](https://www.pangram.com/history/2fd8d48d-ee13-4d4f-be23-a363b2b548f4) | romance-s10, 3 | Human | AI or mixed | the panel's fixes kept general advice in a first-person frame |
| [r05-s9](https://www.pangram.com/history/8fca6b73-6ea6-428f-be00-b26f9d14e698) | romance-s9, 2 | Human | AI or mixed | an aside added to a summing-up line |
| [r05-s10](https://www.pangram.com/history/4b0f3653-382c-4562-a675-db6b9de90536) | romance-s10, 4 | Human | AI or mixed | his words in a new order still read as general advice |
| [r05-s21](https://www.pangram.com/history/1a346e61-fe80-4de3-acce-f6500fd1d2a7) | romance-s21, 3 | Human | AI or mixed | the short check reads his own verses AI too |
| [r06-secB](https://www.pangram.com/history/1a6ad01b-2191-4783-9d48-ad82d43642ac) | romance-sec-whole-world, 1 | AI | Human | the pair checks were too short to judge it |
| [r06-secD](https://www.pangram.com/history/76595855-5f60-40c7-bb11-8f79671182b0) | romance-sec-vows, 1 | Human | AI or mixed | his own two closing sentences, joined, read AI High |

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

