# Universal Project Bootstrap

Before substantive work, read `u-dont-existDOTcom/universal-dev-architecture/LESSON-INDEX.md` and the relevant current universal patterns. Current owner instructions and verified project state override universal guidance.

Treat chat context as temporary working memory and keep durable project state in Git. For long-running or multi-session work, maintain a concise current-state checkpoint with the goal, active decisions/constraints, completed work, current step, remaining work, blockers, relevant artifacts/commits, and next safe action.

After interruption, a new thread, context compaction, or model switch, inspect actual repository state first, reconcile the checkpoint, identify what survived, and resume from the latest verified durable boundary without repeating completed work.

Follow the current universal lesson-closeout pattern for substantive work.
