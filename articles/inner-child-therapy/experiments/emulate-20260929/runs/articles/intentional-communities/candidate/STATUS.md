# Community article candidate: status

**Section 2 (2026-10-01, v3): a candidate, in `HUMANIZED-SO-FAR.md`.** Every paragraph reads 100% Human on Pangram alone, or with its neighbor where it is under 50 words, and the section 100% Human (618 words). It uses Joel's own C10 and C11, his edits, Emulate-based paragraphs with one-word fixes, and three paragraphs by the system's own writers. Four questions for Joel are on `community-section2-side-by-side.html`. Records: `s2/PREDICTIONS-s2.md`, `s2/r4/pangram-s2.jsonl`, `s2/TRACE-v3.md`, `s2/SENSE-v3.md`, `s2/GROUNDING-v3.md`; the morning's report is `s2/REPORT-s2-20261001.md`.

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
