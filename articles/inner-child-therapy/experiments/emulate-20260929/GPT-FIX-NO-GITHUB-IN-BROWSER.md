# Fix for the cloud run: the browser never opens GitHub

**For GPT.** Written by Claude on 2026-09-29 for Joel, updated at 15:20 UTC. Read this before `CLOUD-WORK-START.md` and `GPT-RESUME-CLOUD-BROWSER.md`. It changes what's below; everything else in them still holds.

## What stopped the run

The cloud browser worked on Pangram: all 99 prepared output checks went through. It stopped at the first article section, when the browser was sent to a raw GitHub file link. Its URL policy refuses those links and says not to work around it.

## The fix

- **The browser only opens Pangram** (and Emulate's website). It never opens GitHub, raw or not.
- **Read every text through the GitHub connector or your code tool,** then paste it into Pangram's text box. That isn't a workaround of the browser policy, because the browser never goes to GitHub.
- If you can't read a file without the browser, stop and say which file and which route failed. Don't try other GitHub links in the browser.

## New order of work

Joel asked at 15:09 UTC whether we've learned enough from Emulate. Claude's answer: enough about Emulate itself, so no more Emulate runs for learning. What's left is one set of cheap Pangram checks on texts that already exist, then the articles.

1. **The sentence checks** in `runs/sentence-check-queue.json`: 56 checks, 6,638 words, about 86 credits.
   - They're whole texts ready to paste in `runs/sentence-checks/`. Paste each file exactly and check it alone. They use no Emulate words.
   - Record every result as usual, and above all **the exact highlighted spans**: they show which sentence Pangram blamed.
   - **Commit and push as soon as all 56 are done,** and say so in `LEDGER.md`. Claude is waiting for them.
   - What they test (each queue row has its `question` and `note`):
     - 36 **put-backs:** one of Claude's draft sentences put back into an Emulate version that passed;
     - 7 **controls** for Joel's one-sentence fixes (A21, A12);
     - 13 **fixes** to Emulate versions that passed: typos, spacing and quote-mark noise, and invented details.
   - The fixes replace the edit test in Part 4.3. Claude made those edits, and each is labelled. The no-own-words rule still holds for you.
2. **The article baselines** in `runs/article-baseline-queue.json` (below).
3. **The article rewrites** through Emulate's website, as the directive says, with **Joel's new choosing rule** (below). Do D6 (links) on the first chunk that has links.
4. Hearthwork only if budget is left, as before.

**Dropped:**
- probes D4 (Style settings) and D7 (website against API), and the second B01 website run under D1;
- `runs/part4-check-queue.json`: the sentence checks replace it, since it covered only two drafts;
- Pro's analysis (Part 5) and follow-ups (Part 6), and the Pro handoff. Claude writes the lessons from the sentence checks.

## Joel's new choosing rule (15:08 UTC)

The section "Choosing between versions" in `GPT-OVERNIGHT-DIRECTIVE.md` now has it. In short, after "passes in its section":
- nothing invented or changed;
- nothing reversed or dropped;
- it makes at least as much sense as the original in its section and the article. Joel: making more sense is fine, never less;
- fewer stock phrases and padded lists.

The linter no longer decides anything. The new order replaces the one in `OWNER-SUPPLIED-DIRECTIVE-20260929.md` too.

## Paste the prepared article texts, not the Markdown

The article rows in `runs/active-baseline-queue.json` point at the Markdown section files. Those have every link URL and image line in them, which Pangram would check along with the prose. **`runs/article-baseline-queue.json` replaces those rows.** It lists 52 checks, 38,296 words, in Joel's order: the community article (17 checks), the hypnosis guide (32) and neuro de-armoring (3). Each points to a file in `runs/articles/<slug>/paste/`.

- Each file is what a reader sees: headings as lines, links as their words. Images, captions, the Share and Subscribe buttons, and the embedded cards for other posts are left out.
- Hypnosis sections under 150 words are grouped with the section after them. The shortest check is 184 words.
- Neuro de-armoring is split at its "Part 2" and "Part 3" headings. Your earlier chunk files split in the middle of a list. Every number in the article's text is in the paste files; Claude checked.
- Paragraphs are separated by blank lines, in the same order as in the section's Markdown file, so a flagged paragraph maps straight back to its Markdown paragraph (with its links) for the Emulate step.
- **Before you click Check for AI:** the text box must equal the file exactly, and Pangram's word count must be within 8% of the queue's `words`.
- `build_article_paste.py` made these files, and `build_sentence_checks.py` made the sentence checks. Both are safe to rerun and give the same bytes.

## Already done: don't check again

Claude checked `intentional-communities-baseline-01` ("The New Age May Dawn Suddenly") at 14:44 UTC on Joel's account, with the exact text of the paste file. The row is in `runs/claude-pangram.jsonl`.

- **AI Detected**, 58% AI, 42% Human, 972 words scanned, Pangram 4.0: "AI-generated content appears throughout." Credits went from 1,995 to 1,985.
- **Highlighted spans** (the row has their exact text):
  1. the heading through the end of the first paragraph ("…we were supposedly escaping?");
  2. "Escuelita means “little school.”" through "…a strangely useful comparison sample.";
  3. "He felt tricked, began exposing what was happening…" through "Zendik went in the other direction.";
  4. "Apparently kindergarten had already failed…" to the end of the section.

## Where to write

This branch, `claude/emulate-gpt-fix-20260929`, is your `dcc0489` plus Claude's files: this note, the two queues and their texts, the two build scripts, `runs/claude-pangram.jsonl`, the new choosing section in the directive, and Claude's comparison in `analysis/`. Fast-forward `gpt/emulate-overnight-20260929` to it and keep writing there as before.

Only flagged paragraphs go to Emulate. Every dose, compound, unit and timing in neuro de-armoring stays exact. Stop Pangram below 300 credits.
