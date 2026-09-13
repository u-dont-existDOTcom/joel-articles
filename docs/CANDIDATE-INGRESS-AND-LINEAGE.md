# Candidate ingress and lineage binding

Status: ACTIVE workflow rule for iterative article editing, humanization, detector repair, and supervised-writing lanes.

## Problem this prevents

A newly pasted candidate can be byte-identical to an older candidate while still not being the immediately previous candidate or the current workflow target. Semantic similarity, historical identity, conversational recency, and workflow position are separate facts. Never collapse them into an unqualified statement such as `this is the same one`.

## Mandatory ingress binding

Before auditing, comparing, accepting, rejecting, or routing any user-pasted candidate:

1. Treat the literal current user paste as a new **ingress event**.
2. Bind its exact UTF-8 bytes to a SHA-256 before semantic comparison.
3. Record or resolve separately:
   - `current_ingress` — the literal text supplied in the current turn;
   - `immediately_previous_candidate_ingress` — the last candidate paste in conversation/workflow order;
   - `historical_exact_match` — any older candidate with the same exact byte identity;
   - `active_expected_target` — the movement/task the workflow currently expects.
4. `same candidate` means exact byte identity only. Similar wording, same semantic function, same movement, or normalized equivalence must be described with a different term.
5. Never use bare `same`, `again`, `previous`, or `last one` when more than one comparison referent exists. Name the referent explicitly, e.g. `byte-identical to candidate 102 from the earlier distinction movement; not the immediately previous settling candidate`.

## Historical replay does not rewind the cursor

If a current paste exactly matches a historical candidate but does not match the active expected target:

- classify it as a **historical replay ingress**;
- answer/audit the literal current paste if useful;
- do not silently rewind article state, candidate lineage, or the next-target cursor;
- do not treat the historical match as evidence that it was the immediately preceding candidate;
- advance or rewind the workflow only on an explicit owner instruction or an accepted operation that actually changes the active target.

## Cursor rule

Long iterative lanes must maintain a compact task-local active cursor containing at minimum:

- active lane/article/branch;
- current expected target;
- last completed/accepted movement ID and exact candidate hash;
- last candidate ingress ID/hash;
- whether the last ingress was on-cursor, off-cursor, or a historical replay;
- protocol path for candidate ingress binding;
- explicit condition that advances or rewinds the cursor.

Read the active cursor before interpreting the next pasted candidate. Update it immediately after an accepted movement, explicit rewind, or target change.

## Response rule

When an exact historical match exists, report both axes explicitly:

- identity axis: what earlier candidate it matches exactly;
- recency/workflow axis: whether that candidate is or is not the immediately previous candidate/current expected target.

Do not let a correct historical hash match produce a misleading conversational statement.
