# The whole-article recheck of r07 (2026-11-04)

r07 is r06 with the stacks section's last two paragraphs (P80, P81) redone, the only places r06's whole-article check read AI (`../../r06/substack/README.md`). The recheck goes through the same free route and the same temporary draft. The steps and checks are in `PASTED.json`.

- **Prediction**, frozen before the paste: `gut-article-whole#105`, AI at 0.35. That is a guess against: in their section alone, through the API, the whole section read AI (5% human), his own paragraphs included.
- **The paste:** the editor's 3,387 words are the payload's. The rendered post is `CHECKED-TEXT-A.txt` exactly (74 lines, SHA-256 84a87ddb...).
- **The label:** the Pangram extension in the Claude in Chrome browser labeled the post **Human**. That browser is not Joel's Brave (gate E353). Its full analysis opens in the extension's side panel, which this session can't read.
- **Still to come:** the result page (`https://www.pangram.com/feed/<uuid>`) from Joel. The secret link is open in his Brave. Once his link is in, it is read headless (`tools/humanization/pangram_feed_read.js`) into `RESULT-A.json` and `WINDOWS.md`, and the ledger gets the result.
