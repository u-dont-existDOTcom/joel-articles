**Section 4 (2026-10-02, v5): a draft for Joel, not installed yet.** As published it read 87% AI. v5 reads 100% Human as a section (1,449 words), and every paragraph passes alone or with a neighbor that passes alone (`s4/PREDICTIONS-s4.md`, `s4/r*/pangram-s4.jsonl`). The gate ran on v1 to v3 (traces, cold reads, grounding, and the new whole-article stance check, which caught four conflicts on v1 and two on v2). Its fresh-agent checks on the ten paragraphs changed after v3 (P5, P11, P12, P15 to P19, P29, P30) haven't run: every agent call failed on the account's weekly limit (resets 2026-10-06 14:00 UTC). It goes into `HUMANIZED-SO-FAR.md` after those checks and Joel's answers on P5 (the four examples) and P16 (the evidence line). Side-by-side: `community-section4-side-by-side.html`; fixes: `s4/fixlog-s4.json` and `s4/build_s4.py`; stance ledger: `s4/STANCE-LEDGER-s4.md`.

**Section 3 (2026-10-02, v10): a candidate, in `HUMANIZED-SO-FAR.md`,** with Joel's edits of 00:52 and his own characters (straight apostrophes in P7 and P9; curled, his P9 read 100% AI). The section reads 100% Human (560 words). Open: P7's "it's inner being shaped by outer" (two added words passed alone but flipped the section to 13% AI; my opinion: keep his).

**Section 2 proposal (2026-10-02):** from the abstract-agent sweep (`ABSTRACT-AGENTS-s1-s3.md`), "Almost right away, they brought up the oldest objection…" for "The oldest objection … showed up almost right away." The pair with the paragraph before it reads 100% Human (`s2/r5/`); the section check waits for Joel's answer.

# Community article candidate: status

**Section 3 (2026-10-01, v8): a candidate, in `HUMANIZED-SO-FAR.md`.** As published, all nine paragraphs and the section were 100% AI. Now every paragraph reads 100% Human alone or with a neighbor that passes alone, and the section 100% Human (481 words). Every paragraph is an Emulate version with small logged fixes (`s3/fixlog-s3.json`); the path there, with each prediction and result, is `s3/PREDICTIONS-s3.md`. Side by side: `community-section3-side-by-side.html`.

**Section 2 (2026-10-01, v3.1, Joel's edits of 18:06 in): a candidate, in `HUMANIZED-SO-FAR.md`.** Every paragraph reads 100% Human on Pangram alone, or with its neighbor where it is under 50 words, and the section 100% Human (630 words). It uses Joel's own C10 and C11, his edits, Emulate-based paragraphs with one-word fixes, and three paragraphs by the system's own writers. Joel has answered the questions on `community-section2-side-by-side.html`. Records: `s2/PREDICTIONS-s2.md`, `s2/r4/pangram-s2.jsonl`, `s2/TRACE-v3.md`, `s2/SENSE-v3.md`, `s2/GROUNDING-v3.md`; the morning's report is `s2/REPORT-s2-20261001.md`.

**Paused (2026-09-30, 16:10 UTC onward).** Joel asked whether this work runs under the inner child chat's rules, and said to keep going only if it does. It doesn't: section 1 was assembled without most of that chat's gate (`articles/inner-child-therapy/tools/HUMANIZATION-GATE.md` on the inner child branch). The three articles wait until that chat has reviewed `EMULATE-FALLBACK-INSTRUCTIONS.md` and Joel has decided how they go on.

Section 1 ("The New Age May Dawn Suddenly") passes Pangram but isn't ready:
- **Pangram:** the original section read 58% AI. `002-section-candidate.md` reads 100% Human (1,057 words), and each rewritten paragraph is 100% Human alone. The two paragraphs under 50 words were checked together.
- **Blind trace:** a fresh agent traced it both ways against the original, without my notes, and found 61 changes of meaning or strength, about ten of them substantive (`ic01-blind-trace.md`; my summary and proposed fixes are in `ic01-TRACE-FINDINGS.md`). None of the fixes is applied yet.
- **Joel's decisions (16:10):**
  - He approved "It's the sort of thing that doesn't make it into the history books", "a question that for him was primary", "This was boring as hell at the time" and "I grew up on shoulders".
  - He approved the East Wind deletion too, but on my wrong premise, so it's open again (`ic01-TRACE-FINDINGS.md`).
  - Use the Pangram credits; skip the whole-article checks when every section passes.

**v3 installed (2026-09-30, Joel's rulings sent 18:58 UTC):** `002-section-candidate.md` is now v3. It reads 100% Human as a section (1,053 words scanned) and paragraph by paragraph (`v3/pangram-v3.jsonl`).
- **The escuelita paragraph** is variant B: Joel's Zapatista sentences, with his proposal sentence reworded. His full original came back 100% AI alone, and variant C, which kept his proposal sentence, came back 49% AI.
- **The fixes:** `v3/fixlog-v3.json` has all 16, each with its reason in Joel's words. `v3/owner-edits-v3.json` checks his rulings, and they pass.
- **The blind trace** of v3 is `v3/blind-trace-v3.md`. Its sense notes were fixed before any Pangram call.
- **The pages:** the side-by-side page is `community-section1-side-by-side.html`, marked against the version Joel reviewed. The article so far is `community-article-so-far.html`.

**Earlier next steps (2026-09-30):**
- `community-section1-side-by-side.html` shows the original beside the candidate, with my recommendation for every change that matters.
- Once Joel answers, the fixes go in under the shared rules: `AGENTS.md`, `docs/HUMANIZATION-GATE.md` and `docs/EMULATE-FALLBACK.md` on branch `claude/universal-humanization-rules-20260930`, then `main`.
- The rules this experiment's directive set for itself no longer govern article work.

Files:
- `ic01-fixlog.json`: the 12 logged changes, with the words before and after, and why.
- `emulate-api/`: the four Emulate API versions, exact. Two calls each went to the opening paragraph and the escuelita paragraph, each sent alone.
- `community-section1-pilot.html`: each original paragraph beside its candidate, with the fixes marked.
- The plain text of the candidate equals `ic01-section-v2.txt`, the text that passed.

Sections 2 to 17 are not assembled.
