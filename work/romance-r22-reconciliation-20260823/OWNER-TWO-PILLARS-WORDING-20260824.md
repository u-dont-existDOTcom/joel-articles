# Owner wording — Two Pillars missing-function recovery — 2026-08-24

Status: **owner-final local realization; owner-reported Pangram Human, low confidence; accepted as good enough; materialized and promoted as the registered working-master realization on PR #46.** `main` remains unchanged until the PR is merged.

## Exact owner-final tested wording

Preserve these exact tested bytes, including the double space after `rare.` and capitalized `If` after the comma:

`Maybe an unusually strong couple can get away without much community. I think that's rare.  But sometimes a friend who actually knows us both sees the pattern before either of us does. On the other hand, If both people are falling apart, there is only so much anyone else can do.`

Exact text SHA-256: `cd8de93fda39fcdf13c4b1f6ba2f9250c11c40f8c8298f281055e37bafed6291`.

## Supersession / detector evidence

This supersedes both:

1. the earlier r23 realization in which the known-green caveat came first and the owner sentence followed it; and
2. the assistant's r23r1 proposal that removed `Community isn't magic either;` but retained the order `caveat → But sometimes...`.

Joel manually tested the r23r1 ordering and reported **AI, low confidence**. He then changed the structure to the exact ordering above and manually tested it as **Human, low confidence**, explicitly saying that result is `good enough`.

Treat these as owner-reported short-boundary Pangram results. No exact structured probability was supplied, and neither result is a full Part-2 certification. Do not normalize punctuation/whitespace/capitalization and then transfer the Human result to changed bytes.

## Function / fidelity

The underlying r23 function is unchanged: a friend who genuinely knows both partners may see a relationship pattern before either partner sees it. The limitation on what community can do also remains. The owner correction changes their **thought order**:

`strong couple may manage → mutual friend can sometimes see the pattern → counter-limit when both partners are falling apart`

rather than the prior `strong couple → limit/caveat → mutual-friend counterpoint` structure.

The broader old three-sentence generic mutual-friends block remains rejected as duplicative.
