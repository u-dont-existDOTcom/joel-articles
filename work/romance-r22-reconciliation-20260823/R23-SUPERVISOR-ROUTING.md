# Romance r23 supervisor / execution routing

Updated: 2026-08-24

Owner instruction for this Romance article task. This is a workflow constraint, not article prose or article authority.

## Standing routing rule

- Keep the original Chat conversation as the **supervisor** for discussion, editorial judgment, synthesis, repository reading, source comparison, and actions available through its current connectors/tools.
- **Repository involvement alone is not a reason to create a ChatGPT Work task.** If Chat can read or mutate the required GitHub state through its current connector, keep that work in Chat.
- Create **one bounded ChatGPT Work task** only when the next step genuinely requires a capability the supervising Chat lacks, such as terminal/shell execution, local-filesystem tooling unavailable in Chat, running tests or scripts, command-line Git, or another execution-heavy local/cloud capability.
- Work should normally act as the **terminal/local executor** for those bounded steps. Do not route local browser automation, Playwright inspection, local test execution, local materialization, or similar machine-local work through GitHub Actions merely because GitHub is canonical.
- GitHub is the **canonical state, provenance, and synchronization layer**, not the default execution bus. Prefer direct terminal execution in Work when the required machine/profile/repository is locally available, then commit/push the resulting code/evidence/checkpoint to GitHub after the bounded execution completes.
- Use GitHub Actions only when hosted execution, CI, concurrency/permission enforcement, or another genuinely GitHub-native property is itself required. Do not introduce an Actions queue for work that can run directly on the appropriate local/cloud executor.
- The supervising Chat owns delegation: create the bounded Work task in the appropriate local or cloud environment, follow it, retrieve its result, reconcile it with GitHub authority, and continue automatically in the original Chat.
- Do **not** ask Joel to shuttle prompts, logs, commands, files, or results between Chat and Work when the system can perform that handoff itself.
- After the bounded execution step finishes, return control to the original Chat for judgment, synthesis, state decisions, and the next routing choice.

## Scope and precedence

This rule applies to the active Romance article task unless Joel explicitly changes it. Joel's current direct instruction outranks this file. It does not authorize publication, detector spending, article promotion, or authority changes by itself.
