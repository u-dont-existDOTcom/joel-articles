# Argument and Evidence Architecture

This is the primary protocol for research-heavy articles, polemics, factual critiques, investigative pieces, contested biographies, institutional criticism, historical arguments, responses to videos or articles, and evidence-based cultural commentary. Facts determine article architecture, not merely sentence-level wording.

## 1. Identify the real claim before drafting

Record privately:

- the central conclusion;
- the narrowest version worth arguing;
- the strongest materially different explanation;
- the premises on which the conclusion depends;
- evidence for and against each premise;
- unresolved unknowns;
- what new fact would materially change the conclusion.

Do not choose the most dramatic story first and collect facts around it. Emotional motivation may explain why the article matters; it does not establish the factual thesis.

## 2. Build an argument-dependency map

Use a private ledger. For threshold-triggered work, prefer the deterministic `argument_ledger.py` helper so source IDs, evidence IDs, claim IDs, provenance, and dependency edges do not drift between passes:

| ID | Claim or premise | Type | Evidence | Certainty | Load-bearing? | Supports | What depends on it? | Counterevidence | Later update | Status/repair |
|---|---|---|---|---|---|---|---|---|---|---|

Classify each item as direct observation/primary fact, externally verified fact, interpretation, causal inference, plausible explanation, moral judgment, analogy, speculation, or unknown.

A premise is **load-bearing** when removing or reversing it would substantially alter the thesis, emotional framing, title, opening, section functions, analogies, jokes, conclusion, CTA, or derivative short forms.

## 3. Separate evidence from explanation

Use these categories:

- **Established:** directly supported by strong evidence.
- **Supported inference:** not directly observed, but the best explanation of the record.
- **Plausible:** compatible with the record but not strongly preferred.
- **Possible:** cannot be ruled out.
- **Unknown:** evidence does not meaningfully resolve it.
- **Contradicted:** inconsistent with stronger evidence.

Do not smuggle speculation into narrative certainty with phrases such as “clearly he must have,” “obviously she never,” “the only explanation is,” “he was simply being loyal,” “she did not want to know,” or “they were trying to hide.” A compelling story remains a hypothesis until the evidence distinguishes it from alternatives.

## 4. Test competing explanations symmetrically

For a materially disputed conclusion, test:

1. the strongest adverse interpretation;
2. the strongest benign interpretation;
3. a mixed or intermediate interpretation when supported.

Apply the same standard to each. Do not demand direct proof for the favored explanation while accepting circumstantial evidence for the disfavored one, or vice versa. After testing, state which interpretation is best supported and why. Do not manufacture false balance.

“Luck,” coincidence, placebo, pathology, providence, and an unseen mechanism are all explanations, not neutral defaults. When the evidence cannot distinguish among them, preserve the live alternatives or mark the cause unknown. A prudent action—such as stopping driving or seeking assessment—may be justified without resolving why the earlier outcome occurred.

A person's admirable legacy, objectionable personality, political affiliation, intelligence, age, vulnerability, victimization, charm, or reputation may affect prior plausibility. None is transaction-level proof.

## 5. Establish chronology before causality

Record:

- event dates;
- publication/disclosure dates;
- when information became publicly available;
- when it was sent to the relevant person;
- when receipt or acknowledgment is demonstrated;
- when later statements were made;
- whether those statements changed the known record.

Keep distinct: publicly available, sent, probably encountered, acknowledged, read, understood, and believed. Nearby events are not automatically causally connected.

## 6. Rank evidence by probative value

- **Decisive:** directly resolves a central premise or contradiction.
- **Strongly corroborating:** materially strengthens the conclusion but is not independently decisive.
- **Contextual:** clarifies chronology, incentives, background, or plausibility.
- **Relational/pattern evidence:** weak or ambiguous alone but potentially meaningful with independent items.
- **Texture:** humanizes or makes the story vivid while adding little proof.
- **Distracting:** provocative or emotionally satisfying material that invites side disputes without strengthening the core conclusion.

Do not confuse vividness with evidentiary weight. A dry dated record may matter more than an embarrassing photo, sexual joke, strange gift, or inflammatory quotation.

## 7. Evaluate evidence separately and cumulatively

For each item ask:

- What does it establish alone?
- What does it fail to establish?
- Is it independent of the other evidence?
- Does it corroborate a broader pattern?
- Does the pattern survive removal of weak or disputed items?

Do not inflate one weak item into a major conclusion. Do not dismiss a pattern merely because no single item proves the whole case. Ten repetitions of one dependent allegation are not ten independent facts. The cumulative conclusion may not exceed the combined scope of the evidence.

## 7A. Separate aggregate evidence from case-specific application

A study, trend, benchmark, historical pattern, institutional average, or population result may establish what usually happens under specified conditions. It does not automatically determine what is true, advisable, or likely for one person, community, organization, location, or disputed case.

Before applying general evidence locally, record:

- whether the relevant population or system matches;
- differences in baseline, incentives, geography, time, resources, law, culture, selection, and exposure;
- heterogeneity hidden by the average;
- what case-specific evidence exists;
- what observation would change the application.

Do not use “research shows” as a substitute for the transfer argument. Do not dismiss general evidence merely because exceptions exist. Match the local conclusion to both.

## 7B. Keep explanatory systems and normative judgments separate

Data, causal mechanism, psychology, economics, law, historical interpretation, moral judgment, spiritual/traditional explanation, and lived experience answer different questions. Do not blend them into one mechanism or let one vocabulary validate another without evidence. State the bridge as established, inferred, analogical, source-specific, or unknown.

## 7C. State the status of synthesized models

A sequence, framework, scorecard, taxonomy, or decision rule may combine well-supported components without the complete combination having been directly validated. State whether the synthesis is source-derived, adapted, author-developed, model-assisted, heuristic, provisional, or established. Place that status beside the model rather than hiding it in an end disclaimer.

The status statement should not become generic self-undermining language. Match it to what is known and what would change confidence.

## 7D. Map source roles, access, and independent evidence streams

Before prose, record for each source:

- access level: full text, abstract, snippet, or secondhand;
- what Joel personally read or encountered;
- every rhetorical role it performs: evidence, terminology, mechanism proposal, countermodel, limitation, historical context, or analogy;
- what it supports and what it resists;
- the source's actual domain and where extrapolation begins;
- whether the lived observation preceded the reading;
- whether the evidence streams are genuinely independent.

Do not invent first-person source reactions. Phrase an abstract as “the abstract proposes,” not as something Joel read closely or found surprising. When a full source materially changes an abstract-based treatment, retire the old candidate and re-audit all source functions. One source may both converge with the article and supply its strongest countermodel.

## 7E. Attribute components and separate practice from evidence

Map separately:

- primary text or direct observation;
- established theory;
- lived experience;
- Joel's author-developed synthesis;
- proposed mechanism;
- practice instruction or exercise rationale;
- analogy;
- external evidence;
- competing interpretation;
- unresolved question.

Do not present an established theoretical component as only Joel's private idea. Do not credit that theory with the complete synthesis. A useful exercise or phenomenological rationale is not scientific evidence, and an analogy is not a mechanism. State scientific limitations at the exact disputed level rather than adding a generic philosophical disclaimer.

## 7F. Source-language and negative-claim discipline

For linguistic, doctrinal, or translation claims:

1. search aligned primary-language formulas and grammar;
2. compare translations and early parallels where available;
3. audit synonyms and neighboring formula families;
4. distinguish inability to express a distinction, absence of dedicated nouns, differently overlapping categories, and translator flattening;
5. use temporary neutral analytical labels while overloaded publication terms remain unresolved.

Claims such as “no passage,” “never explains,” or “the language has no way to say” remain provisional until this audit is complete. A partial counterexample narrows the claim; it does not automatically solve the whole mechanism.

## 7G. Keep adjacent mechanism steps distinct

Common access, coordination, cross-sensory binding, a unified phenomenal scene, reflective knowing, self-ascription, appropriation as me/mine, renewed becoming, and a permanent witness are non-equivalent claims. State which step the evidence supports and which it does not. Preserve exact modifiers identifying the object of cessation or release. Scope temporary phenomenology so a direct glimpse or meditation state is not mistaken for ordinary permanent functioning. A respondent who supports one local premise while rejecting the ontology is corroboration for that premise only.

## 8. Use a conclusion ladder

Adapt a ladder to the subject. A general version is:

1. an event/contact occurred;
2. a relationship or recurring pattern existed;
3. a material or reputational benefit was received;
4. information was publicly available;
5. actual awareness is demonstrated;
6. reasonable due diligence was absent;
7. judgment was impaired or seriously deficient;
8. practical or reputational assistance was provided;
9. a later account was incomplete, misleading, or contradictory;
10. knowing participation or deliberate complicity is established.

Failure to prove level 10 does not erase levels 1–9. Establishing lower levels does not imply the highest one.

## 9. Separate conduct from character and legacy

Evaluate the disputed act independently from the person's overall value. A person may have done important work, suffered unfair attacks, and generally acted with integrity while still making a severe mistake. A generally objectionable person may be falsely accused in one case.

Preserve deserved admiration and criticism independently. Do not use praise as collateral against documented failure, or one failure as a total biography without evidence.

## 10. Rebuild when a load-bearing premise fails

When new evidence contradicts or materially weakens a load-bearing premise:

1. stop line editing;
2. identify every dependent claim;
3. audit title/subtitle;
4. audit opening/thesis;
5. audit chronology and causal explanation;
6. audit section functions and transitions;
7. audit jokes and analogies;
8. audit repeated character judgments;
9. audit conclusion and CTA;
10. audit captions, summaries, social posts, videos, apps, and other derivative artifacts.

Do not preserve the old argument with caveats and glue. Recalculate the strongest supported conclusion from what remains. A beautiful paragraph built on a failed premise is still a failed paragraph.

In style-only mode, report the failed premise and its dependencies rather than silently changing the argument. In authorized substantive mode, rebuild all dependencies.

## 11. Use the strongest fair critique

Prefer the narrowest conclusion that is fully supported, addresses the real issue, does not depend on unknowable intent, survives removal of disputed peripheral details, acknowledges contrary evidence, states what is not proven, and would remain fair if applied to someone Joel admires.

Reasoning aid (not a publication template):

> The strongest supported criticism is not [overstatement]. The record establishes [decisive facts], which supports [precise conclusion], even though it does not establish [stronger allegation].

## 12. Derive the minimum decisive case only after the audit

Select three to six facts that resolve the central dispute, come from the strongest sources, stabilize chronology, directly answer the main defense where relevant, require little speculation, and remain persuasive without weaker material. Add the most important fairness limitation.

Use this minimum decisive case for the opening, summary, conclusion, YouTube comment, social post, spoken rebuttal, or short description. Audit first; compress second.

## 13. Keep uncertainty local

Place uncertainty beside the claim it affects. Name what is uncertain, why it matters, whether it changes the conclusion, and what would resolve it. Do not write an overconfident article with one final disclaimer, or repeat the same caveat after every sentence.

## 14. Research stop rule

Research is sufficiently complete for drafting when all load-bearing premises and strongest counterevidence have been examined; primary sources were sought where useful; chronology is stable; access failures and unknowns are documented; and further searching is unlikely to change the main conclusion enough to justify delay or complexity.

Do not claim exhaustive review unless completed. Stop pursuing peripheral curiosities once the decisive case is stable.

## 15. Make rhetoric follow evidence

Joel may remain funny, angry, irreverent, partisan, morally forceful, personal, or tender. Rhetoric must amplify a demonstrated contradiction rather than conceal a gap.

The strongest conclusion must remain supported after removing every joke, insult, political label, character claim, and legacy appeal. Once that test passes, restore the humor that improves the writing.

## 16. Preserve mixed evidence and real tension

When evidence supports good intentions with bad judgment, genuine achievement with serious failure, manipulation with avoidable credulity, strong conduct evidence with weak motive evidence, or a persuasive pattern without proof of the most extreme allegation, preserve that tension. Do not force a total hero, villain, victim, or hypocrite arc.

## 17. Short-form rule

Never draft a definitive short-form rebuttal before establishing the central disputed proposition, decisive chronology, strongest contrary fact, fairness limitation, and exact supported conclusion. Short forms need completed evidence architecture because they remove context.

## 18. Deterministic ledger operations

`argument_ledger.py` separates analytical judgment from bookkeeping.

The model/writer decides:

- what the real claim is;
- which premises are load-bearing;
- what each source establishes and fails to establish;
- evidence weight and independence;
- competing explanations;
- certainty;
- and which article or derivative destinations genuinely depend on a premise.

The script deterministically provides:

- source-packet and file hashes;
- stable source-segment IDs;
- evidence and claim IDs;
- explicit dependency edges;
- reference and cycle validation;
- scope/cap warnings;
- premise-failure impact reports;
- and rendering of an explicitly selected minimum decisive case.

It never edits article prose. It has no apply/rewrite command. An impact report is a review map, not permission to change the article.

Recommended flow:

```bash
python argument_ledger.py assess --task-type investigation --premise-risk high
python argument_ledger.py init sources/ --recursive --out argument-work \
  --task-type investigation --premise-risk high
python argument_ledger.py validate argument-work/argument-ledger.json
python argument_ledger.py impact argument-work/argument-ledger.json \
  --claim C-001 --status contradicted --confirmation source-audit \
  --basis "New verified source" --out argument-work/premise-impact.md
```

Use `ARGUMENT-LEDGER-QUICKSTART.md` for the full command sequence.

## 19. Over-editing safeguards

The ledger is threshold-triggered, not a ritual for every article. Before invoking it, state the proposed scope—none, minimal, standard, or full—and why. Ask Joel only when two scopes are genuinely reasonable and the extra bookkeeping would materially change time, complexity, or output. Otherwise use the least burdensome justified scope. Plain-text script sources stored in the Project (for example `argument_ledger.py.txt`) should be restored to their real `.py` filenames and run through Data Analysis when available; do not ask Joel to upload them again unless the source file is inaccessible or code execution is unavailable.

Use it when a research-heavy, investigative, polemical, contested, or high-stakes piece has medium/high premise risk, or when one factual correction could change multiple sections or derivative artifacts. Use `minimal` mode for a small claim cluster. Do not require a full ledger for personal essays, ordinary explainers, routine P1/P2 edits, or P2S style-only work unless a material disputed premise is present.

Scope rules:

- Map load-bearing premises and their direct dependents—not every factual sentence.
- Map only destinations that would materially change if the premise failed.
- Treat mode caps as brakes, never quotas.
- Use explicit edges only; do not let the script invent dependencies.
- A weakened premise triggers review, not automatic invalidation.
- A contradicted load-bearing premise can trigger a global dependency **review candidate**, never an automatic rewrite.
- Preserve alternative supports: an `any` dependency remains viable when another independent support survives.
- Stop using the ledger once the decisive case is stable and remaining unknowns are peripheral.
- Do not let the graph replace narrative judgment, lived material, mixed truth, or the article's human shape.
