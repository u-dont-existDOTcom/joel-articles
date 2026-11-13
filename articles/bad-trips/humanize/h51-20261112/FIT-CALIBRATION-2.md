# The universal fit read, scored before use (turn 41, 2026-11-12)

Joel, 2026-11-12 22:34 UTC, on the fit read of turn 40, whose questions had the bad trips guide built in: "i wanted it to
be universal not just for this guide. sense checks in general should be able to understand this kind of thing like a real
reader would. a real reader understands they happen to be reading a guide on bad trips and overdoses." The read
(`tools/humanization/fit_read_brief.md`) now takes what the text is and the reader's moment as its first two lines, reads
as that reader, and asks of every line four questions: ANYWAY, CAN'T TELL, FROM, and MISREAD (read quickly, does it
sound like the opposite of what it means; from his fix "(which is a good thing)" after "it shrank the area of the brain
that died", "shrinking brain sounds bad on a cursory read lol").

## Held out: another article's reader

Twelve lines written for a gut-healing article's reader at home in the protocol's first week (`fit2/EXPECTED.md`, written
before any read): six to mark (more gas once fiber goes up, a gut lining sealing, fasting before a procedure, zonulin
coming down, a trial that halved the bacteria with nothing saying that is the aim, a ward round) and six to pass.

| reader | marked of the six | passed of the six |
|---|---|---|
| Sonnet (`fit2/ans-sonnet.txt`) | 5: it missed the halved bacteria (MISREAD) | 5: it marked "Expect your stools to change for the first few days, so don't stop over that alone." |
| Haiku (`fit2/ans-haiku.txt`) | 6 | 5: the same stools line |

Both marked the stools line for telling the reader to expect what is already happening, which was its point (it says not
to stop over it). One wording fix after the scores: ANYWAY now says that a line which tells you to expect a change, and
not to worry about it, fits.

## Known answer: the evidence paragraph he fixed

On brainev-c2 (`../h50-20261112/TEST-brainev-c2.txt`), which the first version passed but for its heading, the universal
read (Sonnet, `fit2/ans-known-sonnet.txt`) marked the mechanism sentence as stroke pharmacology that doesn't fit a bad
trip, the point of his fix "drug overdose is not "after a stroke"", and the opening's "stroke" framing and the
preliminary trial, both of which he changed. It did not find the misread he fixed ("it shrank the area of the brain that
died"); it marked that sentence for a different reason, and it marked many lines on several counts. This is not held out:
the MISREAD question was written from his fix of it.

So: a read that knows what the text is and who reads it, from any article, finds most of the lines that don't fit, and
over-marks some; each mark is changed or kept with why it fits, as before. Read by a Sonnet agent; gate
bad-trips-2026-11-12j as made universal by bad-trips-2026-11-12k (`sense_receipt.py`'s "fit" field).

## After use (turn 42, 2026-11-13)

On Chest Pain's evidence paragraph (`../h52-20261113/reads/fit-cp-c2.txt`) the read marked every line, the animal and
lab findings as FROM ("animal and lab-dish findings don't apply to a person with chest pain right now") though each said
where it was found. A second wording fix: FROM now says that a study's finding, said with where it was found, is evidence
the reader can weigh, not a rule carried over. Not yet scored again.
