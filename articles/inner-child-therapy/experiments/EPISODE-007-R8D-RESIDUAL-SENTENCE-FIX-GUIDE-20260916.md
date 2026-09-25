# Episode 007 R8D — residual sentence-level fix guide

Date: 2026-09-16

Status: **TARGETED RESIDUAL REPAIR; known-green spans frozen**

Candidate: `EPISODE-007-MY-JOURNEY-CANDIDATE-R8D-SENTENCE-PASS-20260916.json`

Detector evidence: `EPISODE-007-R8D-PANGRAM-SCREENSHOT-RESULT-20260916.json`

Blind prediction: `EPISODE-007-R8D-BLIND-PREDICTION-BEFORE-SCREENSHOT-20260916.md`

## Freeze

Do not change the Human/high 348-word opening/Pema span, the Human/high 150-word `Borrow adulthood. Do not surrender it.` + autobiography span, or the Human/medium 50-word final sentence beginning `The three adult jobs from the map...` for detector reasons.

## Residual 1 — 187-word AI/high region

### Current 1
`If something in your life is actually dangerous, sometimes you have to leave or get practical help.`

Disposition: **rewrite, keep as direct action**.

Instruction: Start from what the adult has to do when danger is outside the mind. Avoid a generic maxim or mirrored safe/unsafe wording. This sentence should not set up a complete safety mini-essay; it should simply move the reader to practical action.

### Current 2
`Meditation can help with the pain while you're dealing with it.`

Disposition: **merge; do not keep as a standalone balancing sentence**.

Instruction: Preserve the function that spiritual practice can alter the experience of pain, but make it subordinate/incidental to the practical action. Do not create `outside action + inside benefit` as two matched halves.

### Current 3
`It can't replace getting out of danger, and calling the danger merely “your story” doesn't protect the kid from it.`

Disposition: **merge/compress**.

Instruction: End on the concrete protection failure, not a responsible-therapy moral. The point is that if actual danger is reframed as only mental/spiritual material, the action needed to protect the child does not happen. Do not restate that meditation cannot replace action if the prior sentence already makes it clear.

### Current 4
`Say you grew up learning that what you wanted didn't matter.`

Disposition: **keep or minimum-dose rewrite**.

Instruction: This is a good lived setup. It can stay short. Its job is to place the reader inside the emerging-self problem, not introduce a no-self lecture.

### Current 5
`Now you're finally figuring out what you think, maybe even learning to say no, and somebody tells you there is no self.`

Disposition: **rewrite/continue directly from Current 4**.

Instruction: Keep the interruption: a person is only beginning to discover their own opinions/refusals when the no-self teaching arrives. Avoid a formal developmental explanation. Let the social weirdness carry the thought.

### Current 6
`Maybe years later that feels freeing.`

Disposition: **delete as a separate sentence; preserve only if needed inside Current 5/7**.

Instruction: The later-freedom qualification is a fairness caveat, not a separate rhetorical beat. If retained, tuck it into the live sentence as a subordinate qualification rather than pausing to balance the argument.

### Current 7
`Right then it can sound like the old message all over again.`

Disposition: **rewrite/merge**.

Instruction: Keep the concrete recurrence: the person's own wants/no can be invalidated again. Avoid the abstract `old message` summary if a more immediate description is available. Do not add a new symptom or metaphor.

### Current 8
`Sometimes learning what you want and being able to say no has to come first.`

Disposition: **delete as a separate takeaway**.

Instruction: This is the neat conclusion that completes the mini-essay. Preserve the timing function by letting it be evident in the lived setup, or place it inside the preceding sentence without making it the paragraph's moral.

### Current 9
`If you tell a therapist, “No, that's not right for me,” and they say the disagreement itself is resistance, then how could you ever tell them they're wrong?`

Disposition: **keep the interaction; minimum-dose rewrite only**.

Instruction: This is the strongest live sentence in the region. Preserve the actual exchange and self-sealing logic. The question may stay if it sounds natural; otherwise state the impossibility directly. Do not turn it into an abstract falsifiability explanation.

### Current 10
`Maybe they've misunderstood you, or maybe what they're doing just isn't right for you.`

Disposition: **merge; remove the matched `maybe / maybe` pair**.

Instruction: Preserve both helper fallibility and method/goal mismatch without constructing two equal alternatives. One can be primary and the other incidental, or both can sit loosely in the same sentence.

### Current 11
`They have to be able to hear that without turning your no into more proof that they were right all along.`

Disposition: **delete as a separate closer; embed only the necessary criterion**.

Instruction: Do not end on a generic good-helper rule. If explicitness is needed, fold the condition into Current 9/10: disagreement must be able to remain disagreement rather than becoming evidence for the therapist. Then stop.

### Region-level architecture instruction

Do not produce three complete mini-essays for danger, no-self, and therapy. The no-self and therapy material share one live pressure: a person is beginning to have an opinion/no, and an external authority can erase that no by redefining it. Let the no-self thought hand directly into the therapy disagreement instead of concluding first and restarting. The danger material can remain a shorter practical example before that.

Aim for **unequal thought duration**: short danger example, longer emerging-self/no thought, short concrete therapy exchange. No recap.

## Residual 2 — 45-word AI/high region

### Current 12
`“Find the wounded child and love them” sounded simple until I tried it.`

Disposition: **delete or merge into the next sentence unless the hinge is needed**.

Instruction: The sentence currently announces a `simple theory -> complications` framework. If the following lived material already makes that clear, remove the announcement. If retained, keep it extremely light and do not make it a thesis.

### Current 13
`A protective part could stop me before I even got close to the child.`

Disposition: **keep meaning but demote from equal obstacle #1**.

Instruction: Mention protective parts as an obstacle on the way, but do not allocate a self-contained sentence merely to fill the first failure slot. Let it lead into the more important second problem.

### Current 14
`And when I did get through, sometimes I wasn't sitting with the child anymore—I was him.`

Disposition: **make this the dominant thought**.

Instruction: This is the more important failure because it directly creates the borrowed-adulthood problem. Give it more rhetorical weight than the protective-part issue. Let the sequence be: difficulty getting near child -> when access succeeds, adult perspective can disappear. Do not summarize the two as equal categories afterward.

### Known-Human tail — freeze

`The three adult jobs from the map don't work too well when the adult has vanished, so I started looking for a way to have an adult there before I could reliably be that adult myself.`

Disposition: **KEEP BYTE-FOR-BYTE for detector reasons unless Joel identifies a real editorial defect.**

Instruction: The screenshot marks this 50-word tail Human/medium. It already performs the causal bridge to borrowed adulthood without a tidy named-solution close. Do not reopen it merely because confidence is Medium; the current task is removing known AI/high spans.

## Next generation method

Process each disposition locally. Do not imagine a whole fresh section. After local rewrites are complete, integrate them around the frozen Human spans, run preservation proof, then audit the complete section. If the same region remains AI/high after this second sentence-level pass, stop same-context generation for that region and ask Joel for the natural realization rather than adding another anti-pattern layer.