# Inner Child Therapy architecture

<!-- article-id: inner-child-therapy -->

Indexes: articles/inner-child-therapy/CURRENT-STATE.md + articles/inner-child-therapy/master.html

This graph indexes the exact registered working Substack source. It does not imply that every current paragraph has completed humanization, citation review, or owner-final review. Direct current Joel corrections outrank the graph and are reconciled through current state/owner locks.

## Overview

```mermaid
flowchart TD
    s01["Listen & Watch:"]
    s02["The Chicken-and-Egg Problem"]
    s03["My Journey"]
    s04["Before You Try to Go Deep"]
    s05["Borrow the Adult Before You Can Be the Adult"]
    s06["The Three Adult Functions"]
    s07["When the Adult Voice Feels Fake"]
    s08["Sometimes There Isn’t a Clear Child Yet"]
    s09["The Inner Guide Comes Later"]
    s10["Simple Practices"]
    s11["When Love Still Feels Missing"]
    s12["If You Want to Kill Yourself"]
    s13["Altered States Can Deepen the Therapy"]
    s14["When the Practice Feels Real but Stays Shallow"]
    s15["How to Forgive Without Forgetting"]
    s16["When One Life Has Ended and the Next Hasn’t Begun"]
    s17["Borrowed Adulthood in Relationship"]
    s18["You Are Worthy of Love. Always."]
    s19["Appendix"]

    s01 --> s02
    s02 --> s03
    s03 --> s04
    s04 --> s05
    s05 --> s06
    s06 --> s07
    s07 --> s08
    s08 --> s09
    s09 --> s10
    s10 --> s11
    s11 --> s12
    s12 --> s13
    s13 --> s14
    s14 --> s15
    s15 --> s16
    s16 --> s17
    s17 --> s18
    s18 --> s19
```

## Active reconciliation dependencies

```mermaid
flowchart LR
    raw["2026-09-20 raw Substack master"] --> reconcile["Source vs humanization reconciliation"]
    oldhuman["Historical humanization assembly"] --> reconcile
    ownerp1["Direct owner-final Write-It P1"] --> writeit["Keep the Draft placement decision"]
    reconcile --> writeit
    oldcheck["Earlier owner-final checking wording"] --> checking["When More Processing Becomes the Hook reconciliation"]
    reconcile --> checking
    writeit --> stable["Stable current reader-visible boundary"]
    checking --> stable
    stable --> review["Comprehension to preservation to architecture to humanization to Pangram when applicable"]
```

## Authority / placement notes

- master.html is exact current raw-source authority, not whole-article owner-final prose.
- Historical humanization files are derived evidence, not competing masters.
- Joel's direct owner-final Write-It P1 is higher semantic authority but absent from the raw source and remains placement-reconciliation pending.
- The new checking section occupies functions previously held by owner-final evaluation/stop prose. Do not decide that conflict from timestamp or detector status alone.
- Native/editor object order is indexed in SOURCE-STRUCTURE-INVENTORY-20260920.json.
- No publication export is registered.

## Update rule

Update this file whenever section order, protected-function placement, owner supersession routing, or the real stopping point changes. Cosmetic wording edits do not require graph churn.
