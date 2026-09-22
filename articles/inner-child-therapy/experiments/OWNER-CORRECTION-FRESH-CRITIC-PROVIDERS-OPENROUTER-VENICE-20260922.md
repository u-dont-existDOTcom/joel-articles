# Owner correction — fresh critic providers include OpenRouter and Venice

Date: 2026-09-22
Status: **DIRECT OWNER CORRECTION / ACTIVE HUMANIZATION EXECUTION RULE**

## Owner correction

Fresh-context tell auditing is not Railway-specific.

Acceptable genuinely fresh critic surfaces include:
- a new Railway Agent thread;
- a stateless/fresh OpenRouter API request;
- a stateless/fresh Venice.ai API request;
- another genuinely isolated model session.

The critic receives only the exact candidate plus the current rubric. It must not receive prior candidate history, prior defenses, detector scores, same-context reasoning, or hidden target information.

## Current execution findings

OpenRouter:
- an existing Railway service still exposes an `OPENROUTER_API_KEY` variable;
- a fresh OpenRouter request using that stored credential returned HTTP 401;
- therefore that stored credential is stale/invalid and is not treated as the current connected OpenRouter route;
- ChatGPT plugin lookup reports OpenRouter is not installed as a current ChatGPT plugin.

Direct OpenAI fallback:
- two already-connected API credentials were tested only as fresh-context critics;
- both returned HTTP 429;
- no critique was obtained.

Venice:
- current public Venice documentation confirms an OpenAI-compatible API at `https://api.venice.ai/api/v1`;
- GPT-5.6 Sol is available there;
- no accessible local/Railway `VENICE_API_KEY` variable or config file was found;
- Venice is not installed as a ChatGPT plugin.

## Current consequence

V20 remains internal and unaudited by a genuinely fresh critic.

Do not show V20 to Joel merely because provider routing was attempted.

Once a Venice or current OpenRouter key is securely connected to an accessible execution environment:
1. send exact V20 bytes + corrected rubric in a stateless fresh request;
2. any definite AI tell -> repair internally;
3. use a second new stateless request on the repaired bytes;
4. owner delivery only after the fresh-context tell gate is actually satisfied.


## 2026-09-22 credential-placement recovery

Owner reported the Venice key had been added.

Verification found:
- `inner-child-humanization-exp` initially had no service, so Railway could not inject shared variables into a local critic command;
- an empty `critic-runner` service was created with no deployment;
- `VENICE_API_KEY=${{shared.VENICE_API_KEY}}` was attached by reference without reading/copying a secret;
- the rendered service value was zero-length;
- Railway GraphQL `variables(projectId, environmentId)` returned **no shared variables** for `inner-child-humanization-exp`;
- the same shared-variable query returned none for the other accessible Railway projects;
- therefore no Venice secret is presently stored in accessible Railway shared-variable state.

Required human-only action:
set `VENICE_API_KEY` **directly on the existing `critic-runner` service in production**, not in Shared Variables. This overwrites the empty reference without exposing the secret to Chat.
