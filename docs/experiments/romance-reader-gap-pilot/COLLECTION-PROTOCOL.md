# Blind reader packet collection protocol — Romance

Status: **MECHANICAL COLLECTION ONLY.** This stage performs no editorial analysis.

## Purpose

Separate source retrieval and byte/line verification from the expensive reader-reasoning pass. The collector may access GitHub. The later Pro reader must not.

The collector also packages the **controller instructions** needed to run the later Pro stage, so the human does not have to return to GitHub after collection. These controller files are operational instructions, not article content, and must remain unavailable to the Pro reader except for the Pro protocol itself.

## Frozen source

- repository: `u-dont-existDOTcom/joel-articles`
- branch: `main`
- source: `articles/romance/master.md`
- expected SHA-256: `f1c2b9a3f0f3d9e123c3870ca5d741af8ed99bbf6f138e68b845de04b1a12a2c`
- window size: 90 source lines

Stop on any source-identity mismatch.

## Controller support files

Retrieve these exact files from branch `experiment/obsidian-romance-gap-map` without interpreting them:

- `docs/experiments/romance-reader-gap-pilot/FRESH-READER-BLIND-PROTOCOL.md`
- `docs/experiments/romance-reader-gap-pilot/HANDOFF-PROMPTS.md`

Package copies under a separate `controller/` directory:

- `controller/FRESH-READER-BLIND-PROTOCOL.md`
- `controller/HANDOFF-PROMPTS.md`

These files are for the human/controller. `FRESH-READER-BLIND-PROTOCOL.md` is pasted into the fresh Pro conversation at startup. `HANDOFF-PROMPTS.md` remains controller-only.

Do **not** retrieve or package the reader-gap register, Canvas, external benchmark, PR body, README conclusions, or previous audits.

## Preferred deterministic collection

From a clean checkout containing the packet compiler, run it against the exact `main` source:

```bash
python scripts/compile_blind_reader_packet.py \
  articles/romance/master.md \
  --expected-sha256 f1c2b9a3f0f3d9e123c3870ca5d741af8ed99bbf6f138e68b845de04b1a12a2c \
  --lines-per-window 90 \
  --out-dir /tmp/romance-blind-reader-packet/windows
```

The compiler must:

1. hash the exact source bytes before creating output;
2. fail closed on SHA mismatch;
3. preserve exact source bytes in contiguous, non-overlapping line windows;
4. hash every window;
5. prove that concatenating the windows reproduces the exact source SHA-256;
6. write `manifest.json` plus one `window-*.md` file per reveal step.

Do not edit, normalize, reflow, summarize, annotate, or otherwise transform the source text.

After compilation, place the manifest and windows under `windows/` and the two support files under `controller/`. Package the resulting directory as one ephemeral ZIP for the human/controller.

Recommended layout:

```text
romance-blind-reader-packet/
├── windows/
│   ├── manifest.json
│   ├── window-001-lines-0001-0090.md
│   ├── window-002-lines-0091-0180.md
│   └── ...
└── controller/
    ├── FRESH-READER-BLIND-PROTOCOL.md
    └── HANDOFF-PROMPTS.md
```

## If collection is performed through a GitHub-connected ChatGPT instead of a local checkout

The collector must remain mechanical:

1. access only the canonical `main` source named above for article content;
2. verify the expected SHA-256 using exact source bytes; if the available GitHub tool cannot establish exact bytes/SHA-256, report that limitation and do not claim verification;
3. extract the same contiguous 90-line windows in order;
4. preserve exact text and line order;
5. retrieve only the two controller support files named above from `experiment/obsidian-romance-gap-map`;
6. create an ephemeral packet with `windows/` and `controller/` as shown above;
7. perform **no reader-question generation, gap analysis, architecture review, or external research**.

A collector that cannot establish exact source identity is lower-assurance and must say so explicitly in its receipt.

## Collection receipt

Return only the packet plus this receipt:

```json
{
  "source": {
    "repository": "u-dont-existDOTcom/joel-articles",
    "branch": "main",
    "path": "articles/romance/master.md",
    "expected_sha256": "f1c2b9a3f0f3d9e123c3870ca5d741af8ed99bbf6f138e68b845de04b1a12a2c",
    "observed_sha256": "...",
    "verification": "verified|unverified-tool-boundary"
  },
  "packet": {
    "window_count": 0,
    "lines_per_window": 90,
    "coverage": "exact-contiguous-nonoverlapping|lower-assurance",
    "manifest": "windows/manifest.json",
    "pro_protocol": "controller/FRESH-READER-BLIND-PROTOCOL.md",
    "handoff_prompts": "controller/HANDOFF-PROMPTS.md"
  },
  "analysis_performed": false
}
```

## Reader isolation boundary

The complete ZIP may be held by the human/controller, but **must not be uploaded wholesale to the Pro reader**.

The Pro reader receives:

1. the complete text of `controller/FRESH-READER-BLIND-PROTOCOL.md` plus the startup instruction from `controller/HANDOFF-PROMPTS.md`;
2. window 1 only;
3. after it freezes checkpoint 1, window 2 only;
4. and so on.

`HANDOFF-PROMPTS.md` stays controller-only. Do not attach the ZIP, future windows, future-window manifest, canonical source, GitHub repository, or a directory containing unrevealed windows to the Pro conversation.

The manifest's hashes and line ranges may be used by the controller for verification, but the reader does not need future-window metadata to perform the editorial test.
