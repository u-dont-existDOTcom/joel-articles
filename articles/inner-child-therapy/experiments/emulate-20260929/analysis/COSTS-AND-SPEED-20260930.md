# Speed and cost: Pangram, your checkers, Emulate and this chat

**By Claude, 2026-09-30.** The token counts are exact, from this session's records: the main chat and each worker. The dollar figures are API prices for the same tokens, meaning what the Claude part would cost if you paid per token. Your $200 Max plan works differently; see the last section.

## Prices used

- **Claude:** OpenRouter lists Anthropic's per-million-token rates.
  - Opus 5.5: $4 input, $20 output, $0.20 cache read ([OpenRouter](https://openrouter.ai/anthropic/claude-opus-5.5)).
  - Sonnet 5.5: $2 input, $10 output, $0.20 cache read ([OpenRouter](https://openrouter.ai/anthropic/claude-sonnet-5.5)).
  - Cache writes aren't listed there. I assumed 1.25 times the input rate, Anthropic's usual 5-minute rate, but I have no source for it today. Anthropic's own pricing page needed a permission I couldn't get during the turn.
- **Pangram:**
  - Website plans ([pangram.com/pricing](https://www.pangram.com/pricing)): Individual is $20 a month for 300,000 words; Professional is $65 a month for 1.5 million words, plus $200 of API credit.
  - API ([Pangram](https://www.pangram.com/knowledge-hub/what-is-pangrams-developers-plan)): $0.05 per 100 words, 20% off in batch.
  - On the dashboard, one credit covers 100 words, rounded up: 942 words cost 10 credits.
- **Emulate** ([tryemulate.ai/pricing](https://www.tryemulate.ai/pricing)):
  - Starter is $19 a month for 50,000 words, Max $49 for 300,000, Enterprise $199 for 2,000,000.
  - Extra words cost $1 per 2,500.
  - Every plan includes the API.
- **Claude Max 20x:** $200 a month. Anthropic publishes no token allowance for it. Its help pages give "at least 900 messages every 5 hours" and a guideline of 50 sessions a month, and no weekly figure ([Max plan usage](https://support.anthropic.com/en/articles/11014257-about-claude-max-plan-usage), [Claude Code with Max](https://support.claude.com/en/articles/11145838-use-claude-code-with-your-pro-or-max-plan)).

## One check, measured today

| check | what it checks | time | tokens | API-price cost |
|---|---|---|---|---|
| Pangram website, driven by a Sonnet worker | AI or human | 13 checks in 8.5 min, ~40 s each | 15.5M, mostly the worker re-reading its own growing context | $4.10, ~$0.32 a check (an earlier worker: $2.14 for 8, ~$0.27), plus 1 Pangram credit per 100 words, about $0.004–0.007 depending on your plan |
| Pangram API (not used yet) | AI or human | seconds, going by the docs (not measured) | none | $0.05 per 100 words: $0.05 a paragraph, $0.55 for a 1,050-word section |
| Your reviewer, 14 passages in one run (Opus) | AI or human, with reasons | 6.2–6.7 min, ~28 s a passage | ~445k a run | $1.37–1.38 a run, ~$0.10 a passage |
| Your linter | a few mechanical tells | under a second | none | $0 |
| Blind two-way trace (Sonnet) of a 1,000-word section | meaning, both ways | 14.6 min | 3.4M | $3.09 |
| Blind trace (Sonnet) of 13 short changed paragraphs | meaning, both ways | 11.1 min | 2.6M | $5.90 |
| This chat (Opus 5.5, max effort), today from 05:23 | directing, writing, reviewing | the whole day | 84M over 204 steps, mostly re-reading about 0.5M tokens of conversation each step | $52.92 |

The inner child chat's notes give the rest, which I didn't measure: the reviewer's repair mode takes 5 to 15 minutes a paragraph, the grounding review 5 to 10, a cold sense read 1 to 5, and a fresh writer 1 to 5.

## What that means

- **Pangram's website isn't cheap once you count the worker that drives it.** At API prices, the worker costs about six times what Pangram's API charges for a paragraph.
  - On your plans, the two come out about even in real money (the last section has the conversion).
  - The difference is what they use up: the website uses your Claude limits, while the API costs cash but answers in seconds, with no browser.
- **Your reviewer matches the website's speed per paragraph when it judges a whole section in one run:** about 28 seconds and $0.10 a passage. Judging one paragraph at a time is what makes it slow.
- **The checks Pangram can't do cost the most.** The meaning trace runs $3 to $6 a section, and the sense and grounding reviews are extra. You'd need them with Pangram anyway, because they check meaning, not AI-ness.
- **The biggest cost is this chat.** Every step re-reads about half a million tokens of conversation. So today's directing came to about $53 at API prices, more than all the checks together. Shorter chats that hand their state to the next one through Git would save the most.

## How to speed up your checkers

1. Judge every paragraph of a section in one reviewer run, as in today's test.
2. Run the sense, grounding and meaning checks at the same time, since none needs another's result.
3. Keep the repair mode (tickets) for paragraphs that fail, as the reviewer's README already says.
4. A small script calling Claude's API directly would be faster still. The reviewer's fixed instructions and examples (about 11,000 tokens) would be cached. My estimate is about $0.04 and a few seconds a paragraph. It needs an API key with its own billing, separate from your plan.

## Pangram or your checkers?

They do different jobs. My recommendation:
- **For pass or fail, use Pangram's API** instead of the website, if a small cash bill is fine.
  - At today's rate of checks, the three articles would cost about $45: one 1,000-word section took 12 paragraph checks and 1 section check, $1.15 at API rates, and the articles total about 38,000 words.
  - The website route comes to about the same in plan value, but it's slower and uses up Claude limits you need for the writing.
- **Keep your reviewer for why a paragraph fails, and batch it.** It explains sentence by sentence, which Pangram can't, and that's what the writers learn from.
- **It can't replace Pangram yet.** Its "human" agreed with Pangram all 11 times in today's test, but its "AI" was wrong 3 times in 4 on our own drafts near the line (`REVIEWER-ON-EMULATE-20260930.md`).

## Emulate first, or last?

This compares the two orders for one paragraph the system can't get past Pangram:

| | system first, Emulate last | Emulate first |
|---|---|---|
| time | about 20 minutes when the fast route works, up to about two hours on a hard paragraph (the inner child chat's notes) | seconds for the calls, then the meaning trace, fixes and checks: about 15 to 25 minutes (my estimate) |
| Emulate cost | none unless the loop fails | two calls, about $0.02–0.06 for a 75-word paragraph |
| Claude cost at API prices | several reviewer and writer runs plus this chat's steps: roughly $5 to $30 on a hard paragraph (my estimate from today's per-run costs) | the trace, fixes and checks: roughly $3 to $6 (my estimate) |
| meaning | kept, because the writers work from the guide | shifts in almost every sentence, so it needs the blind trace and your side-by-side review |
| learning | the system practices on every paragraph | only what the diagnosis step pulls out of each case |

My recommendation:
- **For the three published articles, Emulate first.**
  - The text is already yours, so the job is to change its shape without changing its meaning, not to write.
  - Emulate, the blind trace and your side-by-side review together are much faster.
  - The learning comes from finding which of your sentences flipped a paragraph. Today it was the escuelita proposal sentence, a run of actions after a colon.
- **For the inner child article and any new writing, keep the system first, as you decided.** Practice is the point there. It's also where Emulate's drift would hit the guide's conditions and safety lines.

## Your Max plan in dollars

- **The marginal cost is zero until a limit.** The plan costs $200 a month whatever you use, so an extra check costs nothing until it runs you into a limit.
- **The real price per token depends on how much of the allowance you use,** and Anthropic doesn't publish the allowance in tokens.
- **Today, at API prices:** this one chat and its workers used about $71: $53 for the chat and $18 for the workers.
- **A sample conversion:** if your month held 20 days like today, that would be about $1,400 of API-priced usage for your $200. Each API dollar would then cost you about 14 cents.
  - At that rate, a website Pangram check costs about 4.5 cents of your plan.
  - A reviewer passage costs about 1.4 cents.
  - Today's directing in this chat cost about $7.50.
- **The exact figure** would come from your usage page: the weekly percentage before and after a job whose tokens we know.
