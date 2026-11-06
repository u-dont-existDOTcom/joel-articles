# Bug report for AskRigor: the terms ask is vague, and the terms aren't in it

Joel asked for this report on 2026-11-06 at 19:40 UTC ("submit a bugreport to askrigor because you shouldn't be giving
vague words about me not accepting, you should say "Do you accept the terms so I can use AskRigor? Here are the
terms:""). It goes to AskRigor's own lesson queue with `submit_lesson_candidate`.

**Status: not sent yet.** The first version was refused by AskRigor's privacy check ("found personal or identifying
details"), which then asks for a rewrite in general terms, shown to you, and your yes before it is sent again. Below is
the rewrite: no file paths, no version strings, no account details. Reply "send the AskRigor report" and it goes.

## The report, as it would be sent

- **Category:** usability
- **General lesson:** When an account must accept the free contributor notice (a new account, or the notice changed),
  AskRigor should put the full notice and its version in the plain-text result and word the ask as a direct question,
  "Do you accept the terms so I can use AskRigor? Here are the terms:", because an app that passes only the text to the
  AI leaves it with vague words, no terms to show and no version to accept.
- **What happened:** after the notice changed, the research access check returned only "Choose free contributor mode or
  activate an existing paid private entitlement before research use." The notice and its version were only in the
  structured part of the result, which the app does not show the AI. So the AI told the user, vaguely, that acceptance
  was needed, could not show the terms or say what had changed, and could not find the version to accept with.
- **What should happen:** the text result says that acceptance is needed and why (new account, or the terms changed
  since the accepted version), gives the full notice and its version, and gives the AI the question to ask: "Do you
  accept the terms so I can use AskRigor? Here are the terms:", then the notice, with paid private mode named as the
  other choice for accounts that have it.
- **Why:** the text part of the access result is built from the account's status alone; the notice and version go only
  into the structured part.
- **Part to change:** the research access tool's text result (the status check, and the refusals that point to it).
- **Existing rules:** none in the protocols; the skill's "show the exact returned notice" can't be followed when the
  notice isn't in the text.
- **Made-up test:** an account accepted an earlier notice, the server is on a newer one, and the app reads only text.
  Expected: the text says the terms changed, gives the new notice and its version, and asks the question. Control: an
  active account on the current notice gets no notice and no question.
- **Detailed report** (your account has detailed reports on): the same steps; the cause, with high confidence; the
  proposed change (add the reason, the question, the full notice and its version to the text whenever access isn't
  active on the current notice, say the same in the skill and the server's instructions, and test that the text alone is
  enough to ask and accept).

## What I did meanwhile

You had accepted, so I accepted the current notice for you with the version AskRigor's public source code gives, and
AskRigor now reads your account as active in free contributor mode. The terms you accepted, word for word from that
source:

> Free AskRigor use is reciprocal: what AskRigor learns from your research is saved for its research library. That
> includes deidentified structured research progress and, for each finished research answer whose findings would help
> other people, a findings card: the question in general terms, the main findings and how certain they are, the public
> studies behind them, and what public online communities reported, summarized without their posts or names: the
> communities, counts of what people reported, and links to the forum threads AskRigor read, never YouTube comments or
> video IDs. AskRigor never saves raw chat, prompts, identity or contact details, private health narratives, uploads, or
> raw source or provider bodies. Saved research is reviewed and does not become evidence, conclusions, or scientific
> authority merely because it was saved or repeated. Your findings cards are published in AskRigor's public Atlas as
> soon as they are saved, written without you and marked "Not checked by supervisors yet" until AskRigor's owner has
> reviewed them, and people who sign in can vote and comment on them. If you ask to delete a findings card, everything
> that ties it to you is removed, and the card leaves the Atlas unless AskRigor's owner has already accepted its
> findings; no reason is needed. An accepted finding stays while it is valid: it is corrected or taken down when someone
> shows it is wrong, and rewritten or removed if it could identify anyone. Paid private access saves research findings
> or lesson feedback only when you accept saving them for that answer, and requires an active verified entitlement.
