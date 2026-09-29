# Handoff 1: Inner Child Therapy, humanizing by hand (Claude)

Written by Claude on 2026-09-29, 04:00 UTC, so Joel can open a fresh chat for this project.

## Where it lives

- **Repo:** `joel-articles`, branch `handoff/claude-dangerous-adult-20260924-1631`. Never touch `main`, never force-push, and merges need Joel's OK.
- **The article:** `articles/inner-child-therapy/HUMANIZED-ARTICLE-SO-FAR.md`.
  - Render it with `python3 tools/render_article_so_far.py <out.html>`, from `articles/inner-child-therapy/`. The render also runs the owner-edits check against `OWNER-EDITS.json`.
  - Send the rendered HTML to Joel at the end of every turn.
- **Rules and lessons:** all in `articles/inner-child-therapy/tools/`:
  - `HUMANIZATION-GATE.md`: the process, plus Joel's bans;
  - `JOEL-FIXES-CATALOGUE-20260928.md`: every one of Joel's fixes;
  - `PREDICTIONS.md`: every Pangram check, with the call made before it;
  - `tells_lint.py`: the linter;
  - `reviewer/`: the reviewer prompts;
  - `calibration/`: texts with known Pangram results.
- **The current section's record:** `experiments/MAKE-THE-PROTECTOR-VISIBLE-20260928.md`, with lessons P1–P7.

## Where the work stands

The section is under `# Building Trust With Your Little One`, with the h2 `## Keep Your Word`. The h2 is a candidate that replaced the guide's "Make the Protector Visible", because every other heading tried flipped the section to AI.
- **P1 is Joel's paragraph** (his "What's a 'boundary'?" fix). Keep it exact.
- **P2 is Claude's s2j** ("You can protect your little one from yourself too…"). It passes alone, joined to P1, under both headings, and with the paragraph before the headings.
- **Next are guide paragraphs 3 and 4:** "the Protector can go first", then "make one act specific", "rehearse" and "afterward, look at what happened".
  - The 2 a.m. paragraph is out for now.
  - Emulate's versions of Claude's draft of P3–P4 are in `experiments/emulate-20260929/runs/CLAUDE-API-TEST.md`. One of them passed in context but muddles the meaning.
- **After this section:** "Love Doesn't Have to Wait for Trust", then "Make a Simple Vow". Both are under the same h1.
- **Open question for Joel:** whether "Keep Your Word" stays, since it overlaps with "Make a Simple Vow". He could also give a minimal fix for the last two sentences of his P1, which is the span every failing heading flagged.

## How to check on Pangram

Use Joel's dashboard in the built-in browser pane, tab `seed`, at https://www.pangram.com/dashboard.
- `tools/pangram_batch_gen.py drafts.json out.json key1 key2 key3` builds a browser batch of up to 3 checks. Each check:
  - fills the textarea;
  - verifies its SHA-256;
  - clicks "Check for AI";
  - reads the result and the flagged spans (background `rgba(255, 86, 48, 0.1)`).
- Keep each batch to 3 checks, because the call has a 50-second deadline. If the last read times out, read the page separately.
- Log a prediction in `PREDICTIONS.md` before every check.

## Getting changes onto GitHub from the cloud container

The container can't push. Instead:
1. **Commit and make a patch.** Commit in `/root/work/joel-articles` with `git -c user.name=Claude -c user.email=noreply@anthropic.com commit`, ending the message with the Co-Authored-By and Claude-Session lines. Then run `git format-patch -1 HEAD --stdout > /mnt/user-data/outputs/xfer22/xferNN-0001.patch`.
2. **Copy it to Joel's laptop.** Use `device_commit_files` to write it to `/home/joel/ai-work/claude-dangerous-lane/inbox/`.
3. **Apply and push there.** Use Desktop Commander `start_process` with deviceId `cf376439-4f04-4ddd-aeab-1a1c826fe34c` and bash. The guarded one-liner checks PREV, TREE and SHA, then runs `git am` and pushes; copy it from any recent turn.
4. **Resync the container:** `git fetch origin && git reset --hard origin/<branch>`, only when there's no diff.

Stay inside `/home/joel/ai-work/claude-dangerous-lane` on the laptop.

## Joel's standing rules for this project

- One paragraph at a time. Check each paragraph on Pangram alone and in its section, with its headings.
- Show every draft in context, next to the guide's original.
- Report every cut and every move in the same message.
- Never use "the kid". Invent no facts about Joel's life. Don't polish Joel's words.
- Banned: "doesn't get to decide", "Fine," / "Good," / "Great," as a clause of their own, and wry humor. Don't overuse made-up scenes.
- Read the clock only at the start and end of a turn, and report both times.
- Learn from Joel's minimal fixes, and ask him for one when stuck, showing the flagged span.
