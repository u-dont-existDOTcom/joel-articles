# Two fresh reads scored against what Joel fixed (turn 38, 2026-11-12)

Joel, 2026-11-12 16:48 UTC: "so we need to figure out how you can understand when things don't make sense, when they're
indefinite in reference, when they're logically overlapping and redundant, when they are compressed, and most of all,
when the payoff comes too late."

Before using any read as a gate, I scored two of them on seven texts of mine that he fixed, against flags written down
before any read ran (`GOLD.json`, from his comments on each fix; the texts and each reader's moment in `CASES.json`):

- the old read: `tools/humanization/his_fixes_brief.md` (gate 12g), a fresh reader marking sentences that read one of the
  eight ways my drafts differ from his fixes;
- the new read: `tools/humanization/reader_moment_brief.md`, a fresh reader put in the reader's moment, reading one
  sentence at a time and saying what they can do, where they get stuck, what repeats, what is packed, and where the
  payoff comes.

Each read was a fresh Sonnet agent given the brief and one text. The replies that came back are in `answers/`, with the
two prompts for one text.

## Four of the seven new reads were stopped

The new read on ss-r1-fix2, cbd-before and pfa-before ended with: "API Error: Sonnet 5.5's safeguards flagged this
message (https://www.anthropic.com/legal/aup). This sometimes happens with safe, normal conversations." (details
`[reasoning_extraction]`). On chest-c3 the reader's write of its answer was stopped by a safety classifier, and it reported
that it had not finished. pfa-before's answer file was partly written when its reader was stopped; it is not counted
below. None of the four was run again or reworded. Every old read finished.

## Scores

A flag counts when the read named the words he fixed, or the sentence for the reason he gave. Half: the sentence was
flagged for another reason. "Brief": the old brief quotes this very fix as one of its examples, so its hit there proves
little (the old brief's examples come from five of these seven fixes).

| text | his flag | new read | old read |
|---|---|---|---|
| chest-c3 | the action (call medics) after the list of signs | stopped | missed |
| chest-c3 | "familiar" chest pain in an emergency guide | stopped | missed |
| chest-c3 | serious signs that overlap (severe, new, won't let up, keeps getting worse) | stopped | missed |
| chest-c3 | the unsure case and a second DMSO line after the list | stopped | missed |
| ss-r1-fix2 | what counts as one pattern | stopped | hit (brief) |
| ss-r1-fix2 | the closing pair overlapping and packed | stopped | hit (brief) |
| oral-p1 | "is a different problem from ..., and both are different from ..." | missed | hit (brief) |
| oral-p1 | "etc." standing in for states to check | hit | hit |
| oral-p1 | "because that word alone doesn't tell you much" adds nothing | missed | missed |
| pfa-before | "hurt somebody" (themselves) | stopped | hit (brief) |
| pfa-before | "Put away the car keys" (out of reach) | stopped | half |
| pfa-before | "water" (pools of water) | stopped | hit (brief) |
| pfa-before | "roads, balconies, water, weapons, crowds, and strangers" packed | stopped | hit |
| room-before | "Sip rather than chug" (who sips?) | half (a repeat of the water line) | hit |
| room-before | "Ask before touching" (ask what?) | missed | missed |
| room-before | the commands before the why (his "They're feeling overwhelmed, so ...") | hit (the verdict comes after the checklist) | hit (brief) |
| room-before | the quips | hit (both as repeats) | half (one) |
| aftermath-before | "content" | hit | hit |
| aftermath-before | "every fear was false" | hit | half (as a contrast pair) |
| aftermath-before | the run of one-word commands | missed | hit |
| aftermath-before | "Let the system settle." | hit | hit |
| cbd-before | "known CBD" | stopped | hit |
| cbd-before | "adjunct" | stopped | hit (brief) |
| cbd-before | the 2025 study detail, no use in a seizure | stopped | hit |

On the nine flags neither brief gives away (oral-p1's "etc." and "because", room-before's sip, ask and quips, and
aftermath-before's four): the new read 5.5, the old read 6, both together 7. On chest-c3, the one text of these he fixed
after the old brief was written, the old read found none of his four.

What the readers flagged that he left alone:

- Room: both flagged the five questions ("Is the light too bright? Is the music horrible? ..."), the old read for their
  shared shape, the new read wanting them gone. He kept all five word for word.
- Oral: the new read wanted "remedy" gone and a line on when to call an ambulance first; he kept "remedy" and added no
  such line. Aftermath: it wanted a line on when the morning needs outside help; he added none.
- The old read marked ten of aftermath's ten sentences and twelve of room's eighteen.

## What this says

1. Neither read finds what he finds. Both missed "Ask before touching" and "because that word alone doesn't tell you
   much"; the old read missed everything in chest-c3, the case his message is about; and both flag plenty he keeps.
2. The new read catches the words that don't fit the reader's moment ("content", "the system", "every fear was false",
   "etc.") and, in the room text, a payoff that comes late. It cannot see a run across sentences (the one-word commands),
   and it adds content he would not.
3. The safeguards stopped it on four of seven texts, so it cannot be a gate. It stays written down here, not used.
4. What carried in his own tries is structural, and testable without a reader: in Chest Pain his try 7 changed one thing
   on my chest-c3, the action said before the list ("For the following more serious signs (or if unsure), I'd also call
   medics:") with the two sentences after the list cut, and it read Human. My Brain Feels Damaged's checks (brain-c3)
   and Acute Medical's opening have the same shape: the action after the checks. The next test is that move on them
   (`../h48-20261112/`).
