# Checks of 2026-11-05 (turn 10): his CBD paragraphs, round 6's drafts, the first five minutes' P4

Pangram's web app on his account, through the Claude desktop app's browser pane (Claude in Chrome wasn't connected),
`tools/humanization/pangram_page_helpers.js`'s `__run` and `__readC`, each text's SHA-256 checked before the click and the
result read back from his history by SHA-256. Predictions in `../pangram-ledger.jsonl` before every check (the first
batch's predictions hashed each file with its final newline; the checked text is the same without it, noted on each
result). Every window's confidence is given; less than High is work to do (E278), Low first.

| text | try | result | windows | link |
|---|---|---|---|---|
| his three CBD paragraphs, with his video link | 1 | Human Written, 0% | High, Low ("For focal seizures outside those syndromes, the evidence is mixed, but still long-term."), High, Low ("I'd treat it as a plausible experimental adjunct remedy ...") | [result](https://www.pangram.com/history/01b892a4-ee16-4f06-bb77-52090f1aa4e7) |
| CBD-TRIAL, his second paragraph with the trial's points | 1 | Human Written, 1% | High, Medium, Low (the 7-OH-CBD sentence) | [result](https://www.pangram.com/history/fc22bbd5-30f8-44fe-a91f-0558402a2430) |
| CBD-TRIAL, T2 (the liver said plainly) | 2 | Human Written, 0% | High, Medium, High, Medium, High | [result](https://www.pangram.com/history/b50d4304-fb72-49b6-a5cf-b55f1fd269a7) |
| SEIZ-WARN A, the warning stage | 1 | AI Detected, 26% | AI Low (the opening), Human Medium | [result](https://www.pangram.com/history/f6fce8a6-b90d-4e4d-82f7-158db03e8ca8) |
| SEIZ-WARN A2 (the aura named) | 2 | Human Written, 0% | Human High (one window) | [result](https://www.pangram.com/history/9b155e42-fc18-433e-9eb8-e53c737cbc50) |
| SEIZ-WARN B, cannabis at an aura | 1 | AI Generated, 100% | High, Medium, High | [result](https://www.pangram.com/history/d0c33c95-5464-4a8f-8b75-28eaedc6e4c8) |
| SEIZ-WARN B2 (point first) | 2 | AI Generated, 100% | Medium, Low, Medium, High | [result](https://www.pangram.com/history/ce0a18e3-fcf7-4e9c-bd45-8b96081343d9) |
| SEIZ-WARN B3 (after the tell panel: why it varies first) | 3 | AI Generated, 100% | Medium, High, Medium | [result](https://www.pangram.com/history/a93d2e44-7bfa-4308-b7f7-762fb9997b9b) |
| SEIZ-WARN B4 (his CBD paragraph's way of bringing in studies) | 4 | AI Generated, 100% | Medium (one window) | [result](https://www.pangram.com/history/7e0bcdff-ef6d-432e-842f-24d7a0c30df8) |
| his P3 + my P4 D3 | 1 | AI Generated, 100% | High, Medium, High, Medium (his P3 included) | [result](https://www.pangram.com/history/0993c7c4-386c-4a5b-821b-f15f3beb738d) |
| his P3 + P4 D4 (each rule's purpose) | 2 | AI Generated, 100% | High (one window) | [result](https://www.pangram.com/history/f1b3e3bb-30f2-4399-8398-82bd3998b413) |
| his P3 + P4 D5 (after the tell panel: no "if they want to" frames) | 3 | AI Generated, 100% | High (one window) | [result](https://www.pangram.com/history/525ce8ca-ff4d-49cd-a47f-6304b4217035) |
| his P3 + P4 D6 (acts on things, like his P3) | 4 | AI Generated, 100% | High (one window) | [result](https://www.pangram.com/history/60fb8654-35a6-479d-b242-a9ee25f68002) |

Tell panels (Codex on his laptop, Sonnet, Haiku): `panel-B2/PANEL.md` and `panel-P4D4/PANEL.md`. Both agreed on every
sentence. On B2: mirrored "Some people say / Others say", a gloss, a safety closer, a balanced review. On P4 D4: three
parallel "if they want to" conditionals (two echo his P3's last sentence), paired endings, generic hazards.

What it shows. The making-sense read fixed the two Low or AI openings it could see: the 7-OH-CBD sentence ("first pass"
unexplained, its point unsaid) and the warning-stage opening (a vague frame; now it names the aura, which the next
paragraph needs). It did not carry the cannabis paragraph or P4, through four causally different tries each. P4 takes
his Human P3 to AI every time it follows it. Both went to him on round 6's page (SEIZ-WARN's second paragraph,
MOVE-YOURS), per E333 and AGENTS.md's "Reasoning only Joel has".
