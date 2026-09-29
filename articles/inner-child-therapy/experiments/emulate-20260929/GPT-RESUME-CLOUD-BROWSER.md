# Resume the Emulate run in the cloud browser

**For GPT Work.** Written by Claude for Joel on 2026-09-29. This replaces the browser parts of `RESUME.md`. Everything else in `GPT-OVERNIGHT-DIRECTIVE.md` still holds.

## Why the first run stopped

It used the browser on Joel's desktop, where a security check blocked pangram.com after 26 scans. **Use your own cloud browser this time**, the virtual browser that agent mode runs in, not Joel's local browser.

## Start like this

1. Open https://www.pangram.com/dashboard and https://www.tryemulate.ai in the cloud browser.
2. Ask Joel to take over the cloud browser and sign in to both. Wait until he says he's done.
3. Check you're on Joel's accounts: Pangram shows his credit balance, and Emulate shows his plan.
4. From then on, work unattended. If a site logs you out, stop and ask Joel to sign in again. Never create an account or type a password yourself.

**Pangram goes through the dashboard only.** Joel says the API is too costly. Stop checking if the balance drops below 300 credits. There are no PDF downloads, because they caused Save As popups on Joel's screen. Read results from the page instead.

## Work on the existing branch

Continue on `gpt/emulate-overnight-20260929`. Don't redo anything already saved. Reuse:
- `runs/emulate.jsonl` (56 saved versions);
- `runs/pangram.jsonl` (the results so far);
- `runs/part3-check-queue.json` (99 prepared output checks);
- `runs/part4-check-queue.json` (105 prepared splice and edit checks);
- `runs/active-baseline-queue.json` (the baselines still to do).

Before submitting any text, look in Pangram's History to see whether it has already been checked, so you never pay twice for the same text.

## Keep it simple

- **Record each result once:** one line in `runs/pangram.jsonl`, with the text file, its SHA-256, the headline label, every percentage shown, the flagged spans and the time.
- **Flagged spans:** the text of each element with background `rgba(255, 86, 48, 0.1)`, read from the result page.
- **Checkpoints:** commit and push every 10 results. Don't use new registers, reservations or verification layers; one `LEDGER.md` note per checkpoint is enough.
- **Pasting:** paste the saved text exactly. Before pressing "Check for AI", compare the first and last 10 words, and the word count Pangram shows, against the file.

## Order of work (the most useful data first)

1. **Part 3 checks** of the 56 saved outputs: each output alone; each paragraph alone when there's more than one; and B01 and D3 in context.
2. **The remaining learning baselines,** from `active-baseline-queue.json`.
3. **The articles,** in `ARTICLES.md` order:
   - baseline each h1 section, and mark the flagged paragraphs;
   - send only those to Emulate;
   - check each result alone and in its section;
   - apply Joel's choosing rule and assemble the article.
4. **Part 4:** the splices and edit tests in `part4-check-queue.json`. For cumulative runs, stop a pair at its first Human result.
5. **The probes still open:** D4 (Style settings, website only), D6 (links), and D7 (website options against API versions).
6. **The handoff:** update `HANDOFF-TO-PRO.md` and `MORNING-NOTE.md`.

## Emulate: use the website for the articles

- The charge test showed a website run gives two options for one charge. That doubles the versions for the same words.
- Before pressing "Keep this one", read both options' text from the page. In the charge test, option A's page text matched its Copy text exactly, so page text counts as exact.
- Save both options, then keep the one Joel's choosing rule picks.
- Use the API when the website fails, or when you need a single exact version quickly.

**Budgets:** 52,803 Emulate words were left at the last read. Split them as the directive says: articles' first pass up to 38,600, second runs up to 12,000, and a reserve of 2,000. Read `GET /v1/me` every 20 runs.
