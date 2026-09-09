# Somatic aquatic bodywork — owner-reported detector split — 2026-09-09

Status: **OWNER-REPORTED DETECTOR LOCALIZATION / BOUNDARY-SPECIFIC / NO CHAT PANGRAM CALL**.

## Exact candidate

The tested candidate was:

```text
## Aquatic Bodywork / Water Therapy

Hale is trained in aquatic bodywork, and she finds the water especially effective for bringing people back toward their inner child. Sometimes people get so young in the water that they feel as if they're back in the womb. There's also a physical side to it that I find interesting: floating lets somebody stretch and move you through positions that would be difficult or impossible to get into the same way on land.

Some people are just prone to ear infections, even with clean water and earplugs, and for them this may not be worth doing very often.

The bigger problem Hale has noticed is how emotionally open people can become. She doesn't like starting with the water before knowing what somebody is already feeling and what they want to work on, so she'll do some inner-child work with them first. Then the aquatic work can take them further into it. She uses massage afterward to help ground them again, and she stays available in case something is still open and they need more help with it after the session.

That's something I'd ask a water therapist about beforehand: if the session opens up much more than expected, what do you actually do then?
```

## Owner report

Joel reported:

- through the end of the ear-infection paragraph, immediately before `The bigger problem Hale has noticed...`: **Human / medium confidence**;
- beginning with `The bigger problem Hale has noticed...` and continuing through the remaining tail: **AI / high confidence**.

No numerical fractions, Pangram model/version, History identity, or exact detector-window metadata were supplied. Do not infer them.

## Editorial interpretation

This is strong boundary-local evidence that the first two paragraphs should not be reopened merely because the tail fails.

The AI-shaped tail coincides with the point where the model compresses Hale's care sequence into a complete explanatory/procedural movement: problem statement -> pre-water preparation -> water -> massage grounding -> continued availability -> reader screening question.

The sequence itself remains owner-protected content. The detector/editorial problem is the model realization/topology, not the existence of an ordered practitioner sequence.

Do not locally optimize the Human/medium prefix. Do not treat `The bigger` as a banned phrase. Change the architecture of the tail rather than token-editing it.
