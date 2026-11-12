# Brief for the readers of his fixes

Each section of the file you are given is one of Joel's fixes: a model-written text (the "before": an article's drafted
words, or a fix a model proposed) and his version of it, shown as a word diff. `[-words-]` are what he took out, `{+words+}`
what he put in, the rest is unchanged. His comment, where there is one, says what he meant to do.

For every section, say which of these changes he made. Use only what the diff shows; quote it.

- **A. A list unpacked.** A run of category words or noun phrases ("nervous system, meaning-making system, body,
  environment, memories, dose") said as separate clauses, each with a verb and what happens or what to do.
- **B. A correction or contrast frame removed.** "X does not mean Y; it means Z", "not X but Y", "X, not Y", "X rather
  than Y", "instead of", "isn't X, it's Y", "X but not Y": said as the thing itself, or as its likely cause.
- **C. A repeated sentence shape broken.** Items or sentences built the same way ("Term plus X: definition." five times;
  "X is different from Y, and both are different from Z") made into different shapes, with different connectors
  ("plus", "along with", "as well as"; "Another is", "Lastly").
- **D. Bare commands joined to their reason.** A run of short imperatives ("Dim the lights. Lower the sound.") joined
  with why or when ("They're feeling overwhelmed, so dim the lights").
- **E. A referent made exact.** Who does it, to what, exactly ("hurt somebody" to "hurt themselves"; "water" to "pools
  of water"; "Sip" to "suggest they sip it"); or what counts ("would be one full pattern").
- **F. A term explained where it is used**, in brackets or an apposition right beside it ("tremor (shaking)"), or a
  jargon word replaced by the plain word.
- **G. A quip, aphorism, thesis or summing-up line cut**, or replaced by the concrete thing to do.
- **H. The reader made the one who acts, or the act named** ("Clinicians often use the Hunter criteria" to "We can use
  the same Hunter criteria that clinicians use"; "get medical help" to "call medics").
- **I. His own stance, experience or example added** (first person, a story, a named place or thing).
- **J. A hedge or slack added** ("maybe don't", "think twice", "you can still change your mind").
- **K. A normal-versus-danger limit said** ("not just regular sweating", "up to a point").
- **L. A spoken register**: casual words or connectors ("for that matter", "go ahead and", "So", "gotta").
- **M. Something cut as unneeded or said twice.**
- **N. Something added the reader needed** (a missing step, case, reason or fact).
- **O. Other**: anything else he changed that none of these names. Say what it is in a few words, with a quote.

Answer as JSON, one entry per section, in the section order, and nothing else:

```
[
 {"section": "A1", "id": "the id after the lane in the section heading",
  "codes": {"A": "before words -> his words", "C": "before -> his", ...},
  "other": ["what it is: before -> his", ...],
  "biggest": "the code of the one change that does the most to the text, and why, in one line"},
 ...
]
```

Quote briefly (a few words each side). Leave a code out when the section doesn't show it; don't stretch a code to fit.
