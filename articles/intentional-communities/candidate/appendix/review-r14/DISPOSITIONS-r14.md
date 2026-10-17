# Rounds r12 to r14 on the appendix v7 and v8: what each finding got

Round r12 (2026-10-17, `../make_gate.py v7x review-r12 13 25`): one trace (Sonnet) of Christian's entry (13) and the research
paragraph in shape r6 (25). Round r12x (`../make_gate.py v7 review-r12x 25`): one trace of the research paragraph in shape r5.
Round r14 (`../make_gate.py v8 review-r14 12`): one trace of Doucleff's entry in shape d1 (12), one cold read of the appendix in
the article (Sonnet) and the stance check against the published essay with Joel's later positions (Sonnet, with an output
budget). The cold read and stance prompts of r12 and r12x were not run (they were for the final draft, r14's). Rounds r11,
r13 and r15 are marches (r13 unused, `../review-r13/README.md`).

## Traces

- r12, entry 13 (Christian, "Where do you start with the nuts and bolts?"): OK. The question has the book as its answer, so a
  reader still takes it as the place to start; "sequencing" is cut by Joel's ruling (the NOTE).
- r12, entry 25 in shape r6: NEEDS FIX. "So you can check it yourself" comes right after "the counterexamples, and the stuff I
  still couldn't verify", and a reader may take "it" as that stuff (SHIFT); the published inspects "the research". Not fixed:
  v8 (`../make_v8.py`) moved to r5 instead, which read Human as well and needed no fix.
- r12x, entry 25 in shape r5: OK. "It" is the research just named; "(a lot bigger!)" repeats the size claim; "etc." names no
  further content.
- r14, entry 12 in shape d1 ("... about kids taking part in family life. It's also about autonomy, and spreading out the work
  of caring for them."): OK. "It" is the book; "also" adds the same three topics; "them" is the kids.

## Cold read (r14)

All 25 entries OK. Phrases paused at: P8 "the partial-community option", P11 "in Reading Order" (the heading), P18
"separation" and "cohesion and capture", P25 "a 200-row ledger". All but the heading's are the published words; the heading is
published as well.

## Stance check (r14)

One conflict in the rewrite (minor): "If you're curious how I got to all this, the research behind it was a much bigger source
audit" makes the research the route by which Joel reached his whole model, where the essay presents it as a source audit that
checks claims ("I'm borrowing a pedagogy and a replication ambition, not claiming the Zapatistas already proved my whole
model"; "many methods in this article are mine"). Round r7's stance check had found no conflict in the same opening; the
published sentence decides, and the section's published heading is "Research Behind This Article". Fixed in v9
(`../make_v9.py`): "If you're curious about the research behind this, it was a much bigger source audit than would comfortably
fit in an article (a lot bigger!)." The same report calls "It's all in the public research report" a minor widening of "The
public research report shows ..."; trace r12x found "all" bounded by the list after the colon, so it stays.

Three contradictions in the published text, as in round r7: Christian's "start here for sequencing" (gone since v1 by Joel's
ruling; "Where do you start with the nuts and bolts?" is scoped to the nuts and bolts); section 13's "For the full sequence ...
read Diana Leafe Christian's" (section 13 v34 sends the reader to the book "for the nuts and bolts of all this"); and the
heading "Books and Papers, in Reading Order" over a list whose first group is child-rearing while a later entry was "start
here" (minor; with "start here" gone, the heading is the published one and stays).
