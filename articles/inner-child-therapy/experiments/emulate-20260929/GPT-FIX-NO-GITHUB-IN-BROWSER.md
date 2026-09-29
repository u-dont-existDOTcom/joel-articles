# Fix for the cloud run: the browser never opens GitHub

**For GPT.** Written by Claude on 2026-09-29 for Joel. Read this before `CLOUD-WORK-START.md` and `GPT-RESUME-CLOUD-BROWSER.md`. It changes only what's below; everything else in them still holds.

## What stopped the run

The cloud browser worked on Pangram: all 99 prepared output checks went through. It stopped at the first article section, when the browser was sent to a raw GitHub file link. Its URL policy refuses those links and says not to work around it.

## The fix

- **The browser only opens Pangram** (and Emulate's website). It never opens GitHub, raw or not.
- **Read every text through the GitHub connector or your code tool,** then paste it into Pangram's text box. That isn't a workaround of the browser policy, because the browser never goes to GitHub.
- If you can't read a file without the browser, stop and say which file and which route failed. Don't try other GitHub links in the browser.

## Paste the prepared texts, not the Markdown

The article rows in `runs/active-baseline-queue.json` point at the Markdown section files. Those have every link URL and image line in them, which Pangram would check along with the prose. **`runs/article-baseline-queue.json` replaces those rows.** It lists 52 checks, 38,296 words, in Joel's order: the community article (17 checks), the hypnosis guide (32) and neuro de-armoring (3). Each points to a file in `runs/articles/<slug>/paste/`.

- Each file is what a reader sees: headings as lines, links as their words. Images, captions, the Share and Subscribe buttons, and the embedded cards for other posts are left out.
- Hypnosis sections under 150 words are grouped with the section after them. The shortest check is 184 words.
- Neuro de-armoring is split at its "Part 2" and "Part 3" headings. Your earlier chunk files split in the middle of a list. Every number in the article's text is in the paste files; Claude checked.
- Paragraphs are separated by blank lines, in the same order as in the section's Markdown file, so a flagged paragraph maps straight back to its Markdown paragraph (with its links) for the Emulate step.
- **Before you click Check for AI:** the text box must equal the file exactly, and Pangram's word count must be within 8% of the queue's `words`.
- `build_article_paste.py` made these files from the section files. It's safe to rerun and gives the same bytes.

## Already done: don't check again

Claude checked `intentional-communities-baseline-01` ("The New Age May Dawn Suddenly") at 14:44 UTC on Joel's account, with the exact text of the paste file. The row is in `runs/claude-pangram.jsonl`.

- **AI Detected**, 58% AI, 42% Human, 972 words scanned, Pangram 4.0: "AI-generated content appears throughout." Credits went from 1,995 to 1,985.
- **Highlighted spans** (the row has their exact text):
  1. the heading through the end of the first paragraph ("…we were supposedly escaping?");
  2. "Escuelita means “little school.”" through "…a strangely useful comparison sample.";
  3. "He felt tricked, began exposing what was happening…" through "Zendik went in the other direction.";
  4. "Apparently kindergarten had already failed…" to the end of the section.

## Where to write

This branch, `claude/emulate-gpt-fix-20260929`, is your `dcc0489` plus these files and nothing else. Fast-forward `gpt/emulate-overnight-20260929` to it and keep writing there as before.

Only flagged paragraphs go to Emulate. Every dose, compound, unit and timing in neuro de-armoring stays exact. Stop Pangram below 300 credits.
