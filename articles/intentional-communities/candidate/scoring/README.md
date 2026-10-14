# Rule Scoring Sheet

The page: https://claude.ai/artifact/NeH9dPAYfd1vGDSMTy1fGN. Only the Claude account that published it can republish it. Its data lives in the page's own store.

- `rule-scoring-sheet.html` is the page's source. It declares the `db` and `user` capabilities and reads three collections: `sets` (one document per set: F, I, W), `items` (one per example, `F1` to `F14`, `I1` to `I6`, `W1`, `W2`) and `scores` (Joel's answers, one document per item).
- `seed/` holds the documents written to `sets` and `items` after the first publish (`writes.json` is the batch that wrote them).
- Joel's answers: read the `scores` collection with the ArtifactData tool (list, collection `scores`), from the account that published the page. If Joel uses the page from his other account, he can press "Copy answers" on the page and paste them into the chat.
- Why the page exists: Joel, 2026-10-12 17:23 UTC: "if you're not clear about how to apply rules you can give me a list of examples i can score." When a rule's application is unclear, add a set here and point him to it from the questions page.
