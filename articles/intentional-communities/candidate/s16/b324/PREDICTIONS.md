# Predictions and Pangram results: batch 324g (2026-10-17, section 16's baseline)

Pangram's web app (the dashboard in the desktop app's browser pane, Joel's Pro account). The published text of section 16, "Practice Comes Before Property", as it stands in the article (the same bytes as `original.md`): twelve groups of at least 50 words by spaces (a short paragraph with its neighbor, each heading with the paragraph under it) and the whole section with its caption (`../make_baseline.py`). Predictions written before the run.

## Batch 324g

| text | mine | why | Pangram |
|---|---|---|---|
| S16-A | AI | the colon and its list of four wrong steps, then six imperatives in a row ("Practice together. Process a real conflict. ...") | **AI** (AI Generated, low, 57 words, AI likelihood 1.00), 03:47:13, [check](https://www.pangram.com/history/863aa9ae-3bb7-4460-b45a-2a6ed19856b6) |
| S16-B | AI | staged economic rules in policy language ("provision members reliably and allocate the common fairly", "not from declaring money impure") | **AI** (AI Generated, low, 72 words, AI likelihood 0.99), 03:47:23, [check](https://www.pangram.com/history/65096b55-73cc-4274-b10a-fc92fbb9c2ed) |
| S16-C | AI | a list of six obligations, "Fine.", and the goats as a two-beat punchline | **AI** (AI Generated, low, 62 words, AI likelihood 1.00), 03:47:34, [check](https://www.pangram.com/history/93bfd8eb-20cd-40a6-a6dc-61a137392392) |
| S16-D | AI | "Inner pl/ork can begin where you live." then a list of four practices that "do not wait for a deed"; two balanced claims about the weekly group | **AI** (AI Generated, low, 68 words, AI likelihood 1.00), 03:47:45, [check](https://www.pangram.com/history/3d9f514b-1b5f-4b5b-9045-56eef1402d4c) |
| S16-E | AI | four imperatives with lists, "if you're hippie enough" at the end | **Human** (Human Written, low, 54 words, AI likelihood 0.46), 03:47:55, [check](https://www.pangram.com/history/1c6de0d6-3931-4a41-91b0-605fc52b57dd) |
| S16-F | AI | as E, then "will teach you more than another year of imagining the ideal village" | **AI** (AI Generated, low, 77 words, AI likelihood 0.96), 03:48:06, [check](https://www.pangram.com/history/51784b49-0635-4220-873d-724f31c84e4a) |
| S16-G | AI | an announcing line ("Here is the first month ..."), imperatives, "Practice before you have an audience." | **AI** (AI Generated, low, 75 words, AI likelihood 1.00), 03:48:16, [check](https://www.pangram.com/history/cf43f0fd-ae78-4e7b-a350-927eae62fb1c) |
| S16-H | AI | a list of five places and a contrast tail ("kinder rather than more impressed with themselves"), then the communities named | **AI** (AI Generated, low, 58 words, AI likelihood 1.00), 03:48:27, [check](https://www.pangram.com/history/41ec2d9a-8468-4b8d-87ef-05a0c2b2f657) |
| S16-I | AI | "what no manifesto can:" and a list of four with a joke at the end, then a one-line instruction | **AI** (AI Generated, low, 50 words, AI likelihood 0.98), 03:48:37, [check](https://www.pangram.com/history/9d175530-25c1-40c0-889a-358527b2d221) |
| S16-J | AI | "I have no application form for you and no retreat to sell." and a tidy closing generalization with a list of four | **AI** (AI Generated, low, 54 words, AI likelihood 0.62), 03:48:48, [check](https://www.pangram.com/history/18f13c2c-5d1f-460b-b5fd-659b9a701131) |
| S16-K | AI | three short sentences of biography, then "Maybe ... Maybe ..." and "does not require one institution, one founder, or one official version" | **AI** (AI Generated, low, 59 words, AI likelihood 0.88), 03:48:59, [check](https://www.pangram.com/history/5351d20c-f247-43ce-aaa4-7278f9993977) |
| S16-L | AI | the "Maybe" pair and the closing chiasmus ("If you build ... If you teach ...") | **AI** (AI Generated, low, 54 words, AI likelihood 0.91), 03:49:11, [check](https://www.pangram.com/history/5d563e0a-79bc-4f92-b685-1988c8ef011e) |
| S16v0 | Mixed | a section is called Mixed; every group above reads AI to me | **AI** (AI Generated, high, 662 words, AI likelihood 0.99), 03:49:24, [check](https://www.pangram.com/history/33125b24-eb5a-4f0a-a34c-aa4f73ccbb57) |

Results of 324g (Pangram's History, 2026-10-17 03:47:13 to 03:49:24 UTC): 11 of 13 predictions right. Every group reads AI (0.62 to 1.00) but E, the list of what remote readers can build (Human, low, 0.46); the whole section reads 100% AI, high (0.99). The misses: E (called AI) and the whole section (called Mixed, the rule for a section; it read AI throughout). Emulate round a takes the section whole (`../emu-a/`); the repeats check (`../review-r1/`) decides the dedup first.
