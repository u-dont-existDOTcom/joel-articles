# Romance detector checkpoint — preservation r11 assembly

Updated: 2026-08-22

Status: task-working detector/edit state only. Canonical `main:articles/romance/master.md` remains unchanged. PR #29 must not be merged wholesale.

## Stable aggregate baseline

Preservation-r10:

- Part 1 SHA-256 `4ab1ad34f171bb75d2f93e261757cca469a655b629508eb3b91ab05ebc83c0ef`, 10,316 words; Pangram 4.0 Human `0.9456760883331299`, AI `0.05432389676570892`, assisted `0.0`.
- Part 2 SHA-256 `9e4c6a522c95741c7dfc9e040b2dcc40773427cbc0aef8f45211de77208b0c85`, 9,892 words; Pangram 4.0 exact Human `1.0`, AI `0.0`, assisted `0.0`.
- Part 2 is frozen byte-for-byte unless a semantic dependency actually requires changing it.

## Selected Part-1 repairs for the next aggregate

### Slow Steady

Exact preservation-proved candidate SHA-256 `2def6737f8763f6e3a92405166dd27f9d0e30ec043a57a216ffbc05bf6bb72f4`, 540 words.

Only change: delete `But the first night isn’t necessarily the final ceiling either.` because the immediately following Bee development anecdote performs the same function with lived evidence.

Pangram 4.0 local result: Human `1.0`, AI `0.0`, assisted `0.0`. Stable local section ledger reached first Human result at 2 paid calls.

### Casual Sex / Situationship

Final local candidate SHA-256 `e59a9cf974a6252930f774d8246512d68d1137b64481194571488e3814897d04`, 866 words.

Only change from preservation-r10 Casual: replace the STI/attachment paragraph with:

`You can test for STIs and tell each other what you know. If you don't know, say so. Attachment is less cooperative. Both of you can mean it when you say this is only sex, and then one of you wakes up attached anyway. If you’re both really numb or robotic about sex, maybe not.`

Preservation proof: 15 protected units, one authorized semantic-reword delta, zero unexplained deltas.

Pangram 4.0 final local call 6: Human `0.9496374130249023`, AI `0.05036260932683945`, assisted `0.0`. The first 825 words are one High-confidence Human segment; the only AI segment is the unchanged 41-word free-love-community ending.

The local section is now **6/6 hard capped**. No seventh local call. That same final paragraph was inside the Human tail of the older full Casual control, so current evidence supports treating the residual as composition-sensitive rather than authorizing a new rewrite.

### Maturity / patient cross-split

Use the exact known-green rollback at SHA-256 `7d60bc1c38669848e7e27d313603e4ee8970e34bf3896673160ea6a61c106002`, 247 words.

It changes only the Part-1 patient-role tail while leaving the preceding dependency-role paragraphs and Part-2 Key-guru/con­descension continuation unchanged. The complete cross-split boundary is therefore exactly the prior Pangram 4.0 measurement at Human `1.0`, AI `0.0`, assisted `0.0`; no new paid local call is needed.

The older `recovery-20260821/MATURITY-PATIENT-HOLD.md` has been corrected: this was a known-green local realization, not prose already materialized in semantic-r9/r10.

## Exhausted sections that must not be locally resubmitted

- `part1-talk-before-sex`: 6/6; unresolved local detector signal remains. Preserve current faithful r10 realization and defer any further decision to aggregate/context or narrow owner resolution.
- `part1-affection-simmer`: 6/6; preserve the r10 preservation-proved aggregate composition.
- `part1-casual-sex-situationship`: 6/6 after the final call recorded above.
- `primal-not-a-performance`: 6/6; do not reopen because exact preservation-r10 Part 2 is already 100% Human in aggregate.

## Assembly contract

The deterministic materializer is:

`work/romance-detector-repair-20260820/tools/materialize_preservation_r11.py`

It starts from exact preservation-r10, applies only the three Part-1 operations above, asserts every old span occurs exactly once, preserves heading/native-marker/Markdown-link-destination identities, asserts protected anchors, and requires Part 2 to remain byte-identical.

Next safe detector action after successful materialization and invariant readback: submit exactly one fresh Part-1 aggregate Pangram 4 measurement. Reuse the existing exact Part-2 100%-Human evidence because Part 2 is unchanged.
