# Pangram prediction scorecard: nibbana article

Built by `tools/humanization/pangram_ledger.py build` from `articles/nibbana/humanize/pangram-ledger.jsonl` (the ledger, one line per prediction, result and explanation) and the lane's records from before the ledger. A call is right when I said Human and Pangram read the text 100% Human, or I said AI and it didn't. Detector versions are never pooled: Pangram 4.0 and 4.1 read the same text differently. "Always AI" and "always Human" are what saying the same thing every time would have scored.

## By detector version

| version | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| pangram 4.1, the API (Joel's key, run on his laptop; E218) | 19 | 8 (42%) | 74% | 26% | 63% | 0.227 (base 0.194, 19) |

## pangram 4.1, the API (Joel's key, run on his laptop; E218)

| window | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| the latest 50 | 19 | 8 (42%) | 74% | 26% | 63% | 0.227 (base 0.194, 19) |
| the latest 100 | 19 | 8 (42%) | 74% | 26% | 63% | 0.227 (base 0.194, 19) |
| all | 19 | 8 (42%) | 74% | 26% | 63% | 0.227 (base 0.194, 19) |

The boundary mix (what was checked; accuracy differs a lot between a paragraph and a section):

| scope or kind | calls | right | always AI would be | always Human would be | I said Human | Brier (base-rate Brier, calls with a chance) |
|---|---|---|---|---|---|---|
| paragraph | 15 | 7 (47%) | 73% | 27% | 53% | 0.220 (base 0.196, 15) |
| pair | 4 | 1 (25%) | 75% | 25% | 100% | 0.251 (base 0.188, 4) |

Calibration:

| my chance of a 100% Human result | calls | mean chance | read Human |
|---|---|---|---|
| 0.2 to 0.4 | 2 | 0.32 | 0% |
| 0.4 to 0.6 | 17 | 0.49 | 29% |

## Misses since the ledger (11)

| cause | misses |
|---|---|
| a paragraph alone is harsher than the article | 7 |
| a Low window read Human | 1 |
| underrated a plain split | 1 |
| a neutral signpost reads AI where his casual frame read Human | 1 |
| a misread page: the caution never read Human | 1 |

The latest:

| check | lineage, try | said | read | cause |
|---|---|---|---|---|
| [n1_nde](https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/community-joel-1018/articles/nibbana/humanize/fix-20261023/n1/API-CHECKS.md#n1_nde) | NB-P92, 1 | Human | AI or mixed | a paragraph alone is harsher than the article |
| [n1_percentages](https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/community-joel-1018/articles/nibbana/humanize/fix-20261023/n1/API-CHECKS.md#n1_percentages) | NB-P134, 1 | Human | AI or mixed | a paragraph alone is harsher than the article |
| [n1_diamond](https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/community-joel-1018/articles/nibbana/humanize/fix-20261023/n1/API-CHECKS.md#n1_diamond) | NB-P230, 1 | Human | AI or mixed | a paragraph alone is harsher than the article |
| [n1_science](https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/community-joel-1018/articles/nibbana/humanize/fix-20261023/n1/API-CHECKS.md#n1_science) | NB-P237, 1 | AI | Human | a Low window read Human |
| [n1_driving](https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/community-joel-1018/articles/nibbana/humanize/fix-20261023/n1/API-CHECKS.md#n1_driving) | NB-P266, 1 | Human | AI or mixed | a paragraph alone is harsher than the article |
| [n1_nde_t2](https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/community-joel-1018/articles/nibbana/humanize/fix-20261023/n1/API-CHECKS.md#n1_nde_t2) | NB-P92, 2 | Human | AI or mixed | a paragraph alone is harsher than the article |
| [n1_percentages_t2](https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/community-joel-1018/articles/nibbana/humanize/fix-20261023/n1/API-CHECKS.md#n1_percentages_t2) | NB-P134, 2 | AI | Human | underrated a plain split |
| [n1_diamond_t2](https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/community-joel-1018/articles/nibbana/humanize/fix-20261023/n1/API-CHECKS.md#n1_diamond_t2) | NB-P230, 2 | Human | AI or mixed | a paragraph alone is harsher than the article |
| [n1_driving_t2](https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/community-joel-1018/articles/nibbana/humanize/fix-20261023/n1/API-CHECKS.md#n1_driving_t2) | NB-P266, 2 | Human | AI or mixed | a paragraph alone is harsher than the article |
| [n1_science_t2](https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/community-joel-1018/articles/nibbana/humanize/fix-20261023/n1/API-CHECKS.md#n1_science_t2) | NB-P237, 2 | Human | AI or mixed | a neutral signpost reads AI where his casual frame read Human |
| [n1_driving_t3](https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/community-joel-1018/articles/nibbana/humanize/fix-20261023/n1/API-CHECKS.md#n1_driving_t3) | NB-P266, 3 | Human | AI or mixed | a misread page: the caution never read Human |

## Lineages still open (tries used of the cap)

| lineage | scope | tries | last read |
|---|---|---|---|
| NB-P92 | paragraph | 3 of 6 | Mixed |
| NB-P165 | paragraph | 3 of 6 | AI |
| NB-P230 | paragraph | 3 of 6 | AI |
| NB-P237 | paragraph | 2 of 6 | AI |
| NB-P266 | pair | 3 of 6 | Mixed |
| NB-whole | article | 1 of unlimited (Substack) | pending |

