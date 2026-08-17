# Argument Ledger Quickstart — v3.9

`argument_ledger.py` provides deterministic source IDs, claim/evidence IDs, provenance links, explicit dependency edges, validation, premise-failure impact reports, and minimum-decisive-case rendering. It never edits article prose.

## When to use it

Use the tool when both are true:

1. the task is research-heavy, investigative, materially contested, high-stakes, or built around a premise whose failure would change the article; and
2. premise risk is medium or high.

Do **not** use a full ledger by default for ordinary essays, personal reflections, P1/P2 edits, or P2S style-only rewrites. `minimal` mode is available when a small number of factual dependencies still need tracking.

Before invoking the script, state the proposed scope—`none`, `minimal`, `standard`, or `full`—and why. Ask Joel only when two scopes are genuinely reasonable and the extra bookkeeping would materially affect time, complexity, or output. Otherwise use the least burdensome justified scope. When `argument_ledger.py.txt` is stored in Project Sources and Data Analysis can access it, restore that exact source as `argument_ledger.py` and use it directly rather than asking Joel to upload it again.

```bash
python argument_ledger.py assess \
  --task-type investigation \
  --premise-risk high
```

## 1. Index the active source packet

```bash
python argument_ledger.py init sources/ \
  --recursive \
  --out argument-work \
  --project "Article title" \
  --task-type investigation \
  --premise-risk high
```

This produces:

- `argument-ledger.json`
- `argument-ledger.md`
- `source-index.json`
- `source-index.md`

The source packet is hashed. Text, Markdown, HTML, DOCX, and—when `pypdf` is installed—PDFs receive stable segment IDs. Unsupported files are still recorded by file hash.

## 2. Add only material evidence and claims

```bash
python argument_ledger.py add-evidence argument-work/argument-ledger.json \
  --description "Dated primary document" \
  --probative-value decisive \
  --source-segment S001-P0003 \
  --establishes "The event occurred before the later denial"

python argument_ledger.py add-claim argument-work/argument-ledger.json \
  --text "The event occurred before the later denial" \
  --kind verified-fact \
  --certainty established \
  --load-bearing \
  --evidence E-001 \
  --what-changes-it "A verified correction to the date or document"
```

Map only:

- load-bearing premises;
- the claims directly dependent on them;
- evidence that materially changes the conclusion;
- article or derivative destinations that would require repair.

Do not map every paragraph merely because it contains a factual sentence.

## 3. Link dependent claims and destinations

```bash
python argument_ledger.py add-claim argument-work/argument-ledger.json \
  --text "The later public account conflicts with the dated record" \
  --kind interpretation \
  --certainty supported-inference \
  --depends-on C-001 \
  --evidence E-002

python argument_ledger.py add-destination argument-work/argument-ledger.json \
  --type opening \
  --label "Opening contradiction" \
  --function "Establishes the article's central dispute" \
  --depends-on C-002
```

`dependency_logic` defaults to `all`. Use `any` only when one of several independent premises can support the claim or destination. Use `mixed` when the effect requires human review rather than deterministic invalidation.

## 4. Validate before drafting or repair

```bash
python argument_ledger.py validate argument-work/argument-ledger.json \
  --out argument-work/validation.json
```

Validation checks:

- broken provenance and dependency references;
- cycles;
- unsupported factual/causal claims;
- missing counterevidence review for load-bearing premises;
- excessive claim/evidence/destination counts;
- excessive dependency depth;
- too many non-load-bearing claims;
- texture or distracting evidence carrying too much of the argument.

Warnings are scope prompts, not commands to add more material.

## 5. Test premise failure without changing the article

```bash
python argument_ledger.py impact argument-work/argument-ledger.json \
  --claim C-001 \
  --status contradicted \
  --confirmation source-audit \
  --basis "Newly verified primary document" \
  --out argument-work/premise-impact.md \
  --json-out argument-work/premise-impact.json
```

The report:

- follows only explicit edges;
- distinguishes invalidated items from review-only items;
- preserves alternative supports;
- identifies affected titles, openings, sections, conclusions, captions, social posts, apps, and sibling artifacts;
- proposes a repair scope without modifying anything.

A `weakened` premise never triggers automatic invalidation. A contradicted load-bearing premise may produce a **global dependency review candidate**, but substantive repair still follows Joel's permission matrix.

## 6. Derive a minimum decisive case only after the audit

Mark three to six claims with `minimum_case: true` and an optional `decisive_rank`, then run:

```bash
python argument_ledger.py decisive-case argument-work/argument-ledger.json \
  --out argument-work/minimum-decisive-case.md
```

The tool will not select claims automatically. This prevents a mechanical summary from deciding what the article's strongest case is.

## Over-editing safeguards

- Scope selection defaults to the least burdensome justified option; ordinary, personal, copy-edit, and style-only work generally uses `none`, not an automatic ledger.
- Mode caps are warnings against mapping inflation, not targets to fill.
- Only explicit dependency edges propagate.
- Unmapped passages remain untouched.
- There is no `apply`, `rewrite`, or source-modification command.
- Premise-failure reports are advisory and require the edit contract.
- The tool should be retired from the active workflow once the decisive case is stable and remaining uncertainty is peripheral.
