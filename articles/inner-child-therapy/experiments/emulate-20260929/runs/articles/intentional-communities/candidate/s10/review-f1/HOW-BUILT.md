# How the review-f1 prompts were built (2026-10-10, section 10 v2)

Two prompts are too large to keep twice in the repository, so they aren't committed. Each is rebuilt from this commit's files with the command below (run from the repository root, with `main`'s tools as of 07c83374); the sha256 is the prompt each agent actually read, built in Claude's cloud workspace, where the article paths began `/home/claude/joel-articles/` (the report paths inside the prompts carry that prefix).

- `GROUNDING-PROMPT.txt` (194,102 bytes, sha256 6a468d6df30b580bb4f10e437df07302e340b0446870380a754f153a09e5b97b), read by a fresh Opus agent, report `GROUNDING-f1.md`:
  `python3 tools/humanization/reviewer/reviewer.py --article <candidate>/HUMANIZED-SO-FAR.md --source <candidate>/../original.md grounding <candidate>/s10/review-f1/grounding-draft.md <candidate>/s10/review-f1/grounding-target.json OUT`
  (HUMANIZED-SO-FAR.md as it was before section 10 v2 was installed, i.e. with v1.)
- `STANCE-PROMPT.txt` (101,995 bytes, sha256 6f9aae12d0513a8c2dd3a7c63636514b6bce1702e00521ddb0f140085bdba571), read by a fresh Opus agent, report `STANCE-f1.md`:
  `python3 tools/humanization/stance_check_prompt.py --essay <candidate>/../original.md --rewrite <candidate>/s10/section-v2.md --out OUT --scope 'section 10 ("From One Community to a Movement"), rewritten' --topic 'building intentional communities' --report <candidate>/s10/review-f1/STANCE-f1.md`
  (section-v2.md with the heading "Federated Communities Make a Movement, Improve Resilience", as it was before Joel chose the shorter heading.)

The other prompts are committed: `TRACE-PROMPT-H.txt` with `trace-in-H.md` (a fresh Sonnet agent, report `trace-H.md`; the shared brief says Sonnet is enough) and `SENSE-PROMPT.txt` (a fresh Sonnet agent; it returned its lines instead of writing `SENSE-f1.md`, which holds them as returned).
