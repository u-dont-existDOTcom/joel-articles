# Claude's API test (2026-09-29, 00:30 UTC)

Four calls to `POST /v1/humanize`, run from Joel's computer. The key is read from a file outside the repo and never printed. `GET /v1/me` showed plan `pro`, 58,527 words left before the calls and 58,017 after (510 charged), and a limit of 3,000 words per call. Each call took 5–9 seconds and returned one version; `reads_human` was `null`.

| input | version | Pangram alone | in the section (headings, Joel's P1, Claude's P2, then this) |
|---|---|---|---|
| B02_after_a (75 words; 100% AI before) | 1 | 100% Human (170 words) | — |
| B02_after_a | 2 | 100% Human (114) | — |
| B01_m34 (180 words; 100% AI before) | 1 | 100% Human (202) | 100% Human (450) |
| B01_m34 | 2 | 100% Human (203) | Mostly Human, 8% AI (451); flagged: its first two sentences, "It's okay for the Protector to go first. It's okay for you to…" |

**What it kept and what it didn't** (Claude's read):
- **B02 version 1** turns the draft's point around: "most of the time you can just tick them off", where the guide says to keep only what helps, not what earns a tick. It also adds a claim that isn't in the draft.
- **B02 version 2** garbles the same point: "then tick it off anyway".
- **B01 version 1** is the one that passed in context. It muddles who's doing what ("do this exercise for your Protector. They probably can think of a few things they do…") and ends on "Only do things that actually help."
- **B01 version 2** is closest in meaning. It turns "at midnight" into "when you wake up in the middle of the night", adds an em dash, and drops the check-mark point.
- **Tells**, in all four: "warm and fuzzy", "debrief", runs of five questions in a row ("Were you afraid? Did you not know…?"), "It's okay… It's okay…", and British spellings ("cancelling", "Afterwards", "got back to you").

Every version passed alone, but one flipped in context. And the version that passed in context wasn't the one that kept the meaning best.
