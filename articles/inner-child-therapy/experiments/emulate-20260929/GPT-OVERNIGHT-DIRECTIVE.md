# Overnight run: Emulate and Pangram

**For GPT.** Written by Claude for Joel on 2026-09-28. Paths are relative to `articles/inner-child-therapy/experiments/emulate-20260929/` in the `joel-articles` repo, unless they start with `tools/`. Those are in `articles/inner-child-therapy/tools/`.

## Who does what

- **Work** handles implementation and the cloud browser, in Parts 1–4 and 6. It runs Emulate (https://tryemulate.ai) and Pangram (https://www.pangram.com/dashboard) in the cloud browser. It saves every text and result exactly, runs the splice scripts, keeps the ledger and commits.
- **Pro** handles the reasoning, in Part 5. It reads the data and writes the analysis, and it doesn't use the browser.
  - If Work can hand off to Pro on its own, it does.
  - If it can't, Work stops after Part 4 and writes `HANDOFF-TO-PRO.md`, saying where everything is and what Pro should do (Part 5, copied in). Joel pastes that to Pro in the morning.

## What this is for

1. **Humanize Joel's articles** (listed in `ARTICLES.md`) with Emulate. Check them on Pangram, so they pass and still say everything they said.
2. **Collect the data Claude needs** to learn what Emulate does that beats Pangram. Joel has tried the paraphrasing apps, and they never worked, so this isn't only paraphrasing.
   - Don't assume what it does. Measure it.
   - Every article section is also a before-and-after pair, so both jobs feed the same dataset.

## Hard rules

- **Accounts.** Use Joel's Emulate and Pangram accounts only.
  - If either site asks you to sign in, stop and ask Joel to take over the browser and sign in.
  - Never create an account, type a password, buy anything, or change a plan or setting.
- **Emulate's API first, the website as a fallback.** Joel has an Emulate API key.
  - Read the key from the environment variable `EMULATE_API_KEY`. If Joel has to give it to you another way, keep it in memory only.
  - Never print, log, save or commit the key, and never put it in a report.
  - Use the API docs Joel points you to; they aren't public. Call the endpoint that does what the website's Humanize button does, with the same settings (Auto).
  - Record each request's settings and the full response text in `emulate.jsonl`, without the key.
  - Use the website for an input when the API is missing, fails twice in a row, or can't take that input, and note it.
  - Probe D7 checks whether the API and the website give the same kind of output.
- **Budgets.** Track both in `LEDGER.md` as you go.
  - **Emulate:** at most 50,000 words, and at most 3,000 words per submission, which is Emulate's own limit. It charges the words you paste.
    - Split: learning sets A–D up to 7,000; articles up to 40,000; reruns up to 3,000.
    - Joel allows up to 59,000 if the articles need it (2026-09-28, 23:54). Use the extra only for articles, Hearthwork included.
    - If you still run out, stop that kind of work and list what's left in the morning note.
  - **Pangram:** 1 credit per 100 words. Joel says credits aren't a problem. Still, read the balance before you start, log what each check costs, and stop checking if the balance drops below 300.
- **Emulate's output never replaces Joel's own writing.** Only two things of his go to Emulate: the control C2, and the odd sentence of his inside a set A "before" text. Their outputs are data only.
  - In the articles, a paragraph that already reads Human in the baseline check stays exactly as it is, whoever wrote it. So does any passage `ARTICLES.md` marks as Joel's, even if Pangram flags it. Those paragraphs still go into the Pangram checks of their section.
  - A flagged paragraph where Joel tells his own story in the first person still goes to Emulate. Mark it in `QUALITY-<slug>.md` for Joel to approve.
  - Nothing replaces anything in Joel's published articles. The humanized articles are candidates, saved next to the originals.
- **Never edit Emulate's output with your own words,** not even one word. Your words are AI text, so they would spoil the data.
  - The only exception is the edit test in Part 4.3, where every edit is labelled.
  - Mechanical splicing is fine: cutting and joining whole sentences or paragraphs taken from the two versions.
- **Save every text exactly:**
  - UTF-8, taken from Emulate's copy button;
  - no retyping, no quote or dash conversion, no trimming inside the text.
- **Paste exactly into Pangram.** Every Pangram check uses the saved file, exactly. After pasting, confirm the box holds the whole file: its first 10 words, its last 10 words, and a word count Pangram reports within 8% of the file's.
- **Privacy.** Send Emulate and Pangram only the files in this folder and the articles Joel lists: nothing else from the repo, no chats, no names. Don't make Emulate share links.
- **Git.**
  - Create a branch `gpt/emulate-overnight-20260929` from `origin/handoff/claude-dangerous-adult-20260924-1631`, and commit and push small commits to it as you go.
  - Never touch `main` or the handoff branch. Never force-push, never merge, never commit a secret.
  - If you have no repo access, build the same folder and give Joel a zip.
- **Never guess a result.** A check you couldn't read is "unread", not "Human". If Pangram hasn't shown a result yet, wait 10 seconds and read again. Don't resubmit, because every submission costs credits.
- **When something breaks** (a button moves, a run fails), write it in `LEDGER.md` and go on to the next item. Don't try the same failing step more than twice.

## Where things are

- `inputs/MANIFEST.md` lists every learning input, with word counts and any earlier Pangram result.
- `inputs/learning/A_joelfixes/` holds **29 AI drafts that Joel later fixed by hand** (2,233 words).
  - Each `*_before.txt` goes to Emulate.
  - Its `*_joel_after_REFERENCE_ONLY.txt` is Joel's fix, which never goes to Emulate.
  - This is the most valuable set, because it gives three versions of the same text: the AI draft, Emulate's version, and Joel's.
- `inputs/learning/B_protector/` holds **24 of Claude's drafts of one inner child section** (2,385 words), the same content written many ways.
  - B01 is the next step of the inner child article.
- `inputs/learning/C_controls/` holds **two texts that already read Human**.
  - C1 is Claude's.
  - C2 is Joel's own writing, so its output is data only.
- `inputs/learning/CONTEXT_section_so_far.txt` is the inner child section as it stands: two headings, Joel's paragraph and Claude's paragraph. It's only for Pangram context checks and never goes to Emulate.
- `inputs/learning/E_holdout/` holds 5 guide paragraphs and `BRIEF.md`. Claude will use them for a transfer test later. **They never go to Emulate, and nobody else writes them.**
- `inputs/articles/` holds Joel's four articles as Markdown, converted from the Substack editor. The raw HTML is in `inputs/articles/raw/`. `ARTICLES.md` lists them in order, with notes.
- `tools/tells_lint.py` is Claude's linter. Run it with `python3 tools/tells_lint.py FILE`.
- `tools/JOEL-FIXES-CATALOGUE-20260928.md` is Joel's fixes grouped by kind.

## What you produce

```
runs/
  emulate/<run_id>.txt        Emulate output, exact
  emulate/<run_id>.lint.txt   tells_lint report on it
  emulate.jsonl               one line per Emulate run
  splices/<id>.txt            mechanical splice and edit-test texts
  align/<run_id>.json         sentence alignment (Part 4.1)
  pangram.jsonl               one line per Pangram check
  pangram/<check_id>.pdf      Pangram's report, if it offers a download
  articles/<slug>/            original.md, sections/, humanized.md, links.json, STATUS.md
LEDGER.md                     budgets used, times, anything that went wrong
HANDOFF-TO-PRO.md             (if Work can't hand off itself)
analysis/                     Pro's files (Part 5)
MORNING-NOTE.md               for Joel, at most 10 lines
```

**`emulate.jsonl` fields:**
- `run_id`
- `input_file`, `input_words`
- `style`: every Style setting shown, including what Auto picked
- `started_utc`
- `output_file`, `output_words`
- `words_charged`
- `notes`

**`pangram.jsonl` fields:**
- `check_id`, `text_file`
- `variant`: one of `baseline`, `output`, `output_paragraph`, `context`, `section`, `full_article`, `splice`, `edit` or `transfer`
- `words_scanned`
- `label`: the headline, such as "Human Written", "AI Generated" or "AI Detected"
- every category percentage shown (AI, AI-assisted, Human and so on)
- the confidence text, if shown
- `flagged_spans`: the exact text of every highlighted span. In today's page these are the elements with background `rgba(255, 86, 48, 0.1)`. Read them from the page, and also from the Detail tab if it shows segments.
- `checked_utc`

## Part 1. Baselines (Work)

Check every learning input as it is on Pangram, using the variant `baseline`.

- Where `MANIFEST.md` already gives a result, recheck only 5 of them, to see whether Pangram gives the same answer as before.
- For the articles, check each h1 section as it is, with its headings, in chunks of up to 3,000 words if it's longer. Mark every paragraph inside a flagged span. Only those paragraphs get rewritten.

## Part 2. Emulate runs (Work)

Leave Style on Auto unless a probe below says otherwise. Send one input per run, through the API or on the website (paste it, press Humanize, copy the result). Don't chat with Emulate. Chat edits cost words and aren't part of the test.

Go in this order, and stop at the budget:

1. **Set A.** Every `*_before.txt`.
2. **Set C.** Both files.
3. **Articles,** in the order `ARTICLES.md` gives.
   - **Chunks.** Send the flagged paragraphs of one h1 section per run, if that's under 2,800 words. Otherwise split at h2, then h3, then paragraph breaks. Group sections under 150 words with their neighbours in the same h1.
   - **Headings.** Keep the headings in the paste as lines, so Emulate sees the structure. The assembled article uses the original headings; note any heading Emulate changed.
   - **Only flagged paragraphs.** If a section is only partly flagged, send each run of flagged paragraphs on its own, and put the results back between the paragraphs that stay.
   - **Links.** Probe D6 decides how to handle them. Send the first chunk that has links with its Markdown links left in.
     - If Emulate keeps every link on the same words, keep pasting links in.
     - If it doesn't, take the links out of the paste and record them in `links.json` (anchor text, URL, paragraph). Afterwards, put each one back on the same words, or on the rewritten words that mean the same. Note any link whose words vanished.
     - Treat italics and bold the same way.
   - **Images and captions.** Leave them out of the paste, and put them back where they were.
   - **Assembly.** Save `humanized.md` and `humanized.html` for each article. The HTML is clean and semantic: h1–h4, p, a, em, strong, lists, blockquote, and figure with the original image URL and caption. Joel works in HTML.
4. **Set B.** Every file.
5. **Probes (set D).** Each one answers one question:
   - **D1 (is it stable?):** run B01, A01 and A02 a second time with the same settings.
   - **D2 (what does a second pass do?):** run two outputs that passed back through Emulate.
   - **D3 (what does it do with headings?):** run B05, which is B01 with its two headings on top.
   - **D4 (what do the Style settings change?):** run B01 twice more, once set to second person and casual, once to first person. Record the exact settings.
   - **D5 (does it write a paragraph differently inside a longer piece?):** compare the paragraphs in B03's output that cover B01's content with B01's own outputs.
   - **D6 (does it keep links?):** see Links, under Articles above.
   - **D7 (do the API and the website match?):** if you can use both, run B01, A01 and A03 through each and compare. If they differ in kind, say so in the morning note. Keep using the API unless its outputs fail Pangram more often.

## Part 3. Check every output (Work)

For each Emulate output:

- **The whole output** (variant `output`).
- **Each paragraph alone** (`output_paragraph`), when there's more than one.
- **B01 in context** (`context`), and the same for D3 and D4: `CONTEXT_section_so_far.txt`, then a blank line, then the output. This is the real next step of the inner child article.
- **Article sections:**
  - Check each section put back together, with its original headings and the paragraphs that stayed (`section`).
  - When an article is done, check it whole (`full_article`). If it's too long for one check, use chunks of whole sections that overlap by one section.
  - If a seam between two sections is flagged and the budget allows, run the flagged paragraphs on both sides of it through Emulate together once, and check again.
  - If a section shows any AI, run Emulate once more on the original text, not on the failed output. Keep both runs, and never hand-fix.
- **Linter:** run `tools/tells_lint.py` on every output and save the report beside it.

## Part 4. Mechanical experiments (Work)

This part tells us the most. Use a Python script so every splice is exact.

1. **Alignment.** For each pair (input, output), split both into sentences and align them. One input sentence can match 0, 1 or 2 output sentences. Word overlap with `difflib` is enough. Save `runs/align/<run_id>.json`.
2. **Splices.** Pick 12 pairs where the input was at least 80% AI and the output 0% AI. Prefer sets A and B, 60–200 words, with at least 4 multi-paragraph pairs.
   - **Forward:** start from the input. Replace one aligned unit at a time with Emulate's version of it, one unit per check, and check each.
   - **Backward:** start from the output. Put back one original unit at a time, and check each.
   - **Cumulative:** replace units in order from first to last, checking after each, until the verdict turns Human.
   - For multi-paragraph pairs, also do forward and backward with whole paragraphs as the units.
   - This shows whether particular sentences carry the verdict, or only the whole piece does, and which original sentences bring the AI verdict back.
3. **Edit test.** This is the only place your own words are allowed, and each one is labelled. Take 4 outputs that passed and make three separate edits to each:
   - (a) change one word, as if fixing a fact;
   - (b) rewrite one sentence yourself so it says the same thing;
   - (c) add one sentence of your own.

   Check each edited version. This tells Joel whether Emulate's output can be corrected by hand, or by a model, without going back to AI.

## Part 5. Analysis (Pro)

Read everything in `runs/`, plus `inputs/MANIFEST.md`, `ARTICLES.md`, Joel's reference texts in set A, and `tools/JOEL-FIXES-CATALOGUE-20260928.md`. Write these in `analysis/`:

1. **`PAIRS.md`**, one entry per pair:
   - the input, the output, and the Pangram result before and after, with the flagged spans;
   - the alignment, with each unit marked kept, reworded, split, merged, moved, cut or added;
   - one line on what changed beyond the words.

   For set A, put Joel's version beside them.
2. **`MOVES.md`**, what Emulate does, measured and not assumed. Name each move in plain words, then give:
   - how often it happens, out of how many pairs;
   - 2–3 exact examples, with pair id and before and after;
   - whether it also happens to the controls (C1, C2);
   - whether Joel makes the same move in his fixes (set A).

   Cover at least:
   - sentence count and length, and the order of sentences and points;
   - topic sentences, and summary or closing lines;
   - lists and groups of three, questions, and contrasts ("not X but Y");
   - hedges, asides and parentheses;
   - concrete detail: added, cut, or invented;
   - first and second person, and register;
   - punctuation (dashes, semicolons, colons);
   - paragraph breaks and headings;
   - how much of the input's meaning is kept.

   Separate the moves it makes everywhere, which are its style, from the moves the splice data ties to the verdict changing, which are the signal.

   End with a short section, labelled as your opinion: what still reads machine-made to you in Emulate's outputs, with examples.
3. **`SPLICES.md`**, what the splice experiments show:
   - whether the flip comes from particular sentences, from how many are changed, or only from the whole piece;
   - which kinds of units flip it;
   - which original sentences bring AI back when they're put back.

   Use the flagged spans.
4. **`FRAGILITY.md`**, the edit test turned into advice: which edits Emulate's output survives.
5. **`SLOP-PREP.md`,** groundwork for a question Claude will take on. Some readers say Emulate's output still sounds like AI, even when Pangram passes it. Don't judge that here; lay out the material:
   - Run `tools/tells_lint.py` on every Emulate output, on every set A "before", on every Joel "after" in set A, and on Claude's own passing paragraphs (the `tools/calibration/PASS_*.txt` files without "joel" in the name).
   - Put the four groups side by side in one table, with each linter rule's hits per 100 words.
   - List the 10 Emulate outputs that passed Pangram but have the most linter hits, with the hits quoted.
6. **`LESSONS.md`**, rules Claude could follow when writing by hand. For each rule give:
   - the rule in one sentence;
   - the evidence (pair ids, splice results);
   - how confident you are;
   - what result would prove it wrong.

   Mark any rule a chat model can't follow as such, for example one that depends on word probabilities. Don't write a rule the data doesn't support. Say "no clear pattern" where there isn't one.
7. **Transfer test: not for Pro.** Claude will do it later with `inputs/learning/E_holdout/`, after reading this analysis. Don't read those files, and don't write paragraphs of your own.
8. **`QUALITY-<slug>.md`, one per article,** going section by section:
   - List what the original says (its points, facts, names, numbers, links), and whether the humanized version keeps each one.
   - List anything added. **Any new "I…" experience or fact about Joel's life means the section is rejected** (Joel's rule).
   - List any of Joel's bans that appear (below).
   - **For neuro de-armoring:** every compound, dose, unit, timing, warning and study claim must match the original exactly. Any change means the section is rejected.
   - List every coined word or catchy phrase of Joel's that the rewrite changed, such as "pl/ork", "Hearthwork", "wizdumb" or the emojis in headings. Joel wants them kept, and he decides.
   - Mark the paragraphs where Joel tells his own story, and say whether the rewrite still tells it truly.
   - Give each section a verdict: ready, needs a fix (say what), or failed Pangram.
9. **`MORNING-NOTE.md`** for Joel, at most 10 lines: what's done, what passed, what needs him, and the budget used.

## Part 6. Pro's follow-up checks (Work, if there's budget and time)

Pro may list up to 20 more checks in `analysis/FOLLOWUPS.md`, each with the question it answers. They can only be splices, or texts Pro wrote and labelled. Work runs them and adds the results.

## Joel's bans (check every output, and every text Pro writes)

- "doesn't get to decide" and its family ("doesn't get to", "gets to", "gets a vote"), said of a feeling or a thing;
- "Fine," "Good," or "Great," as a clause on its own;
- wry humor;
- too many made-up scenes (a caution, not a ban);
- lists that over-explain;
- invented facts about Joel's life or experience;
- in the inner child article, always "your little one", never "the kid";
- phrases Joel dislikes:
  - "that's doing some work"
  - "load-bearing"
  - "tells on itself"
  - "metabolize" or "digest" meaning deal with
  - "clean" as praise
  - "does its work"
  - "That's not X. It's Y."
