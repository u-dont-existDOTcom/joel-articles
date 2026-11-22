# His six tries on round 38's teaching card (TEACH-BRAIN), read from his Pangram history

His round-38 export of 2026-11-12 18:19:16 UTC (`review/r38/ANSWERS-R38-20261112-1819.json`) has his version in "Your
version" and, in the comment, a link to each of his six checks with what he changed; his message with it: "some really
obvious problems again". He started from my brain-c3 (`humanize/h46-20261112/TEST-brain-c3.txt`, AI Generated, 100%,
0eeefa6e), not from brain-p1. Texts and readings from his history (web.pangram.com/api/history/<uuid>/, read
2026-11-12 18:2x UTC); windows as label and confidence with their word counts. Each step, what changed from the one
before, and his note:

1. c30b544b, AI Generated, 100% (eleven AI windows, High, Medium and Low): the heading's "DMSO + Humic Acid First" made
   "DMSO + Humic Acid  + Electrolytes First". ("first, i added electrolytes to this, because magnesium (and then
   potassium) can be depleted by some drugs esp MDMA and iboga, altho i don't think just electrolytes would be
   sufficient... it didn't change it to human of course")
2. 86262bd8, AI Generated, 100% (AI High 29, Medium 11, High 69, Medium 15, High 55): "check them over. Several of these
   checks look for recognized stroke warning signs:" made "check for stroke warning signs:". ("next i removed a little
   redundancy, but that didn't flip it")
3. ed86bddc, AI Detected, 20% (Human Low 36, Medium 23, High 36, Medium 21, Low 9, Low 6, Low 16; AI Low 39, the three
   sentences after the list): from 1, only the first line changed, "First, are they awake and breathing normally?" made
   "First, are unconscious or breathing abnormally?". ("ah, i found the exact problem with most of it, you didn't notice
   that your first symptom was not a symptom? it was the opposite, a sign of health. fixed that and now it's 80% human")
4. 0f807196, AI Detected, 19% (Human Medium 59, High 36, Medium 21, Low 31; AI Low 39): "Wetting or soiling themselves is
   another sign to watch for." its own line. ("then i moved "wetting or soiling" to new line since that was not
   following the sentenc ebefore it. that helped 1% i guess.")
5. 7158fa13, Mostly Human Written, 4% (Human High 28, Medium 11, High 74, Medium 15, Low 16, Low 39): "If it's safe, have
   them stand" made "If you can safely hold them as they try, have them stand", and 2's lead-in. ("then i saw that ai
   tell "if it's safe" which ai says ALLL THE TIME, so i reworded that to be more specific, and that gave another 15%
   towards human ... pretty much any time you see the word "safe" make sure it needs to be there and there's no
   ambiguitiy about what it's referring to or how one would ensure that.")
6. 4739068c, Human Written, Human High 174: the lead-in "check for stroke warning signs that would trigger a call to
   medics:", and the three sentences after the list made one, "When they're too out of it to help you do the checks, or
   if the brain-damage feeling stays despite sufficient treatment, then you've done what you can do, and it's time to call
   for help." ("clarified the last part and now it's all high conf human")

His final, the text of 6, in the guide with three obvious corrections (`review/r38/apply_r38.py`): "Humic Acid  +" with
one space, "are unconscious" made "are they unconscious", "-Wetting" made "- Wetting".

The minimal pair: 3 against 1. One line changed, a sign of health made the sign it stood for in a list of warning signs,
and eleven AI windows became seven Human windows and one AI Low.
