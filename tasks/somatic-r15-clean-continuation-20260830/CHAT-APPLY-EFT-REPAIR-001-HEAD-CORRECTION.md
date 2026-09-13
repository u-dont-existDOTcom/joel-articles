# CHAT-APPLY-EFT-REPAIR-001 — head-field correction

This correction is part of the frozen execution packet.

In `CHAT-APPLY-EFT-REPAIR-001.md`, the field:

`Required starting head: ac1570f3e8945fecf80585d8fbe336c2a19ffbd6`

means **required source-state ancestor**, not required live branch tip.

The branch necessarily advanced when Chat committed the execution packet and this correction. Codex must:

1. read both packet files from the exact packet commit supplied in the supervisor directive;
2. verify that `ac1570f3e8945fecf80585d8fbe336c2a19ffbd6` is an ancestor of the live task branch;
3. verify the source candidate itself by exact Git blob `442349c82d92ac844447f27208924b720d9fa92a` and UTF-8 SHA-256 `9c2e8fe57335d51ac925bc9b63cee8125c24e471e2b9b8fda50cc44cf28f5b31`;
4. continue from the live branch tip only if intervening commits contain the Chat execution packet/correction and do not mutate the source candidate or registered master;
5. fail closed on any conflicting article mutation.

All other terms of `CHAT-APPLY-EFT-REPAIR-001.md` remain unchanged.