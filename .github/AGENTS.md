# `.github/` Agent Instructions

- Treat workflow, ownership, publication, and repository-policy changes as consequential editorial-integrity changes.
- Declare explicit least-privilege workflow `permissions`; begin with `contents: read` and add write scopes only where required.
- Pin remote actions and reusable workflows to reviewed full 40-character commit SHAs; retain release tags only as comments.
- Never execute untrusted pull-request code in a privileged `pull_request_target` context.
- Keep unpublished private drafts, correspondence, source credentials, detector/API credentials, and secret values out of workflows, logs, artifacts, prompts, and state files.
- Automation must not silently soften arguments, alter owner-locked passages, or treat detector scores as editorial authority.
- PR templates must request exact editorial/citation/detector evidence, meaning-preservation review, proposed cuts, final-diff review, continuity updates, and residual uncertainty.
- CODEOWNERS does not prove branch protection. Do not claim rulesets, secret scanning, or push protection are enabled without GitHub settings/API evidence.
- Apply content-specific validation rather than software ceremony where software is absent.
