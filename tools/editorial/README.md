# Editorial delivery gate

`editorial_gate.py` checks source/owner binding, literal assembly, known cluster accounting, diagram sync, declared ordering, two-site reference review, semantic-review records and exact delivery artifacts. `package` blocks the marked package operation when those checks fail. Run from this directory or add it to PYTHONPATH. The tools require the pinned requirements.txt.

Example: `python tools/editorial/editorial_gate.py check --bundle articles/intentional-communities/candidate/finalization-20261019 --phase delivery`

For the owner-facing archive use `package --bundle ... --out Community-Finalization-r03.zip`. The package includes a separately verified canonical-format review ZIP. No publisher API or detector is called. The loopback adapter in RegisteredService accepts enrolled task IDs and expected hashes, not client approval fields. Tests start and stop the service; no daemon is deployed.

Semantic judgments, completeness of discovering overlaps, reviewer identity and owner approval are not proven by this code. A local contract is not isolated from a same-account writer. See docs/EDITORIAL-EXECUTION-ENFORCEMENT.md for actual scope and stronger deployment options.
