# Inner Child safety H2 — V41 indirect-exclusion preservation repair

Date: 2026-09-22
Status: **INTERNAL ONLY / SINGLE PU7 REPAIR FROM TELL-CLEAN V40 / FRESH GATES REQUIRED / NOT PANGRAM-TESTED**

## V40 gate results

Fresh stateless Venice tell audit:
- no definite AI tells;
- mixed areas preserved;
- multiple genuine Human-facing relations;
- final verdict: `DEFINITE_AI_REMAINS: NO`.

Fresh semantic preservation audit:
- PU1 PASS
- PU2 PASS
- PU3 PASS
- PU4 PASS
- PU5 PASS
- PU6 PASS
- PU7 PARTIAL
- PU8 PASS

Only blocking preservation gap:
`The child shouldn't be brought into this at all` did not unambiguously state that indirect routes are also excluded.

## Repair

Add only the minimum route-general qualifier:
`even indirectly`.

No route inventory.
No new paragraph.
No helper module.
No additional policy explanation.

## Exact internal V41

> ## When the Present-Day Adult Is Dangerous to the Child
>
> Think about this as if there were an actual child in the room. An adult tells you they enjoy frightening or humiliating vulnerable people. Would you bring the child over just to see how the child reacts? No. If the child recoils, that reaction only tells you the child is frightened. It doesn't tell you the adult is safe, and it may give the adult exactly the reaction they wanted. The child shouldn't be brought into this at all, even indirectly.
>
> The opposite mistake is to treat anything disturbing in the adult as proof of danger. Someone can be horrified by an intrusive thought they have no wish to act on. A strange belief or something harmful in their past can matter too without telling you what they intend now. That has to be worked out from the adult's own choices, not from the child's reaction.
>
> Suppose later the first adult says, “That's changed. I don't want to do that anymore.” There is still no reason to bring the child back to find out whether it is true. The change can show up in the adult's life instead, over time, in how they treat vulnerable people when taking advantage would still be tempting. That work can stay between the adult and whoever is helping them. The child doesn't need to be there.

## Required next gates

1. new stateless Venice tell audit;
2. preservation re-audit;
3. two fresh local-boundary cold reads;
4. Pangram only if all pass.
