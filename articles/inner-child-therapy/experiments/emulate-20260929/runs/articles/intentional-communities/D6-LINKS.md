# D6 link preservation, first flagged linked chunk

2026-09-29 21:22 UTC. Input `emulate-inputs/001-a.md` contained `[\*Where’s Utopia?\*](https://ibogaqueen.substack.com/p/wheres-utopia-click-read-more-my)` in the first flagged paragraph, plus the original heading. Emulate website Humanize, all Style settings Auto, generated two options for one 63-word charge (52,803 → 52,740).

- Option A rendered the URL on a new anchor, `Continue reading A New Age Might Come Suddenly`, after truncating the question. It did not preserve the original linked words or italics.
- Option B rendered no link. It mentioned a link “below” that does not exist in the output.

Both exact page texts and rendered HTML are saved in `runs/emulate/ic-001a-{A,B}.*`; B's page text matched the Copy button exactly after Keep. Neither option preserved the link on its words, so later Emulate inputs will omit Markdown links and inline emphasis/bold, with original formatting restored during assembly from the source and `links.json`. This is an observation about this run, not a claim that other runs cannot preserve links. Neither option is accepted for the article: A is truncated and invents “home movie glory”; B introduces a new opening and a missing “below” link cue. The first-person story requires Joel's review.
