# Somatic Introduction — Attractor Aversion Gate

Date: 2026-08-31
Status: active owner correction for the current manual Introduction-generation experiment

## Owner correction

The model's recurrent failure is not lack of awareness of the AI-shaped completion attractor. It repeatedly recognizes the attractor and then returns to it anyway. Joel proposed an addiction/PTSD-style analogy: do not merely observe or intellectually reject the attractor; condition the process so the attractor itself functions as an aversive danger cue.

This is a computational/editorial analogue only. The model does not literally experience PTSD, craving, fear, aversion, or other subjective states.

## Operational rule

When a continuation suddenly feels satisfying because it:

- completes the paragraph,
- resolves the distinction,
- balances the preceding claim,
- supplies the obvious example or exception,
- produces a three-beat argument,
- restates an implication in cleaner words,
- turns two fragments into a thesis,
- creates a neat contrast or reversal,
- or makes the passage feel 'finished',

that satisfaction signal is treated as a hazard marker rather than a quality signal.

Do not polish the continuation. Do not invert it mechanically. Do not generate the balancing alternative. Abort the attracted continuation and return to the last live thought before the completion pull appeared.

## Aversion cue

Internal shorthand:

`NEAT = DANGER`

The stronger the urge to make the thought complete, elegant, symmetric, explanatory, or rhetorically satisfying, the stronger the presumption that the current continuation belongs to the recurrent model attractor.

## Recovery behavior

After the cue fires:

1. Remove the attracted continuation back to the last sentence or fragment that still felt discovered rather than completed.
2. Do not immediately repair the deletion.
3. Allow unrelated or only partly related active thoughts to remain in parallel.
4. Continue only if a new local thought has independent curiosity/value; otherwise stop.
5. Semantic reconciliation occurs later and must not be allowed to recreate the rejected architecture automatically.

## Relation to existing experiment rules

This extends, rather than replaces, the active mutation/recombination, scratch-mode, non-serialization, sentence-by-sentence overcompletion deletion, and 12-step attractor-recovery rules established in the current owner conversation.

The purpose is to change reinforcement direction: the recurrent completion attractor is not merely something to notice; noticing it should decrease the probability of following it.

No prose candidate is promoted by this file. No Pangram call, article mutation, or registered-master change is authorized.