# Preservation review: Bringing Reparenting Into Real Life

## Result

PASS for the frozen assembled excerpt. No unresolved source loss, substantive meaning change, or structural flow failure remains after the dating-reference repair. This review covers the assembled text and the exact editorial note prepared for a document comment; it does not certify the final ODT package or its rendered layout.

Reviewed assembly SHA-256: `1bc222ff5f78e4601d912ea6b9a821efc21c690e950df93393a8fea3e902aa30`.

Source SHA-256: `81c0e31546deefc2ae17b5aa0e5159143618a7d5e94770cb07c6cd36e20520b1`.

Approved plan SHA-256: `37398c91d712dd9318fff13f765780f68569368f112e3ab90c02c34a15cb0b1b`.

## Complete source comparison

I read the source and approved plan before seeing the assembly, then compared every source block with the assembled text. An independent comparison applied only the named operations below, rather than treating the preservation ledger as proof. All 69 original blocks were accounted for exactly once: 68 body/list blocks in the chapter and the original editorial note retained separately. All ledger original-text entries also matched the uploaded source exactly.

| Destination | Body/list blocks | Findings |
|---|---:|---|
| Opening | 2 | Both Borrowed Adulthood paragraphs retained; no added opening summary. |
| 1. Play and preferences | 8 | Spark hinge, childhood explanation, Focusing, and all experiment/beginner material retained. |
| 2. Differentiation | 17 | Rules/roles, contingent worth, four questions, definition, complete chameleon/James Bond paragraph, five daily practices, Key/Bowen attribution, and all five happiness-loyalty paragraphs retained. |
| 3. People and trust | 16 | Places, encounters, gradual disclosure, all five hard-disclosure paragraphs, ordinary support choices, all three Hearthwork paragraphs, and dating retained. |
| 4. Speaking up and conflict | 18 | Threat branch, both Speak Toward paragraphs, doctors, all seven Write It paragraphs, both repair paragraphs, relationship-capacity material, unsafe-feeling reflection, and full break paragraph retained. |
| 5. Endings | 5 | All three broad endings paragraphs and both Missing Someone paragraphs retained. |
| 6. Love and community | 2 | Both concluding paragraphs retained together, including community before or after an opening. |

The two source list blocks retain all four hook questions and all five differentiation practices. The source's existing linked reference keeps its exact URL and link text; Bee and all named references remain. No missing URL was invented for the title-only Treasuring the Inner Child’s Gift reference.

## Text changes checked

The three approved cuts are exact: the conformity generalization in P012, the final self-differentiation summary in P014, and “also isn’t realistic nor ideal, and ” in P057. Their surrounding examples and qualifications remain.

Three local transition repairs were checked: deletion of the doctors paragraph's dependent “The same goes for doctors” lead under its explicit new heading; the threat heading's “Someone” and the body's explicit relation to old experiences; and dating's “your support came from a lover” in place of “your support person were a lover.” These repairs do not add a new argument.

Five logged copy corrections were also checked: “it’s might” → “it might”; “mind,but” → “mind, but”; “hildhood” → “childhood”; the possessive and doubled space in “they’re you’re  reassurance machine”; and the missing space in “autopilot.Ask.” They fix mechanical errors without changing meaning. Ten source body blocks have these cuts or corrections; the other 58 body/list blocks retain their source text after Markdown/entity presentation decoding.

The presentation decoding only removes source markup escapes, restores list syntax, decodes spacing entities, and makes the already supplied link syntax usable. It introduces no missing content.

## Flow and qualification review

The initial dating opener had one concrete problem: after Hearthwork, “your support person” could identify the peer just discussed. The final wording removes that personal antecedent while preserving the reader's desire for romantic support. This issue is resolved in the frozen context.

Play's “too” remains intelligible after the opening's account of the little one's support needs. First Social Connections' “Then” can refer to the new people available in the preceding places-to-look paragraph. The doctors heading supplies the antecedent for “them” and makes the practical advocacy case independent of the preceding inner-imagery discussion.

The threat branch precedes reflection and regulation. The other person's right to say no remains, as do the distinctions between repairing harm and conceding the whole conflict, and between guilt and proof of fault or manipulation. The break paragraph has its own H3 outside the other-person-pattern discussion, retains the possibility that nobody is doing anything wrong, and preserves both returning and longer-term distance. Endings retains its many forms of change and the possibility of staying on new terms. The new order does not require leaving a relationship or completing identity work before receiving support.

## Editorial note and limits

P045 is absent from reader-facing body prose because its exact visible text is retained in editorial-note.txt for a genuine ODT comment beside the relationship-capacity discussion. The source typo “dirsepect,” all qualifications about earned/unearned distrust, the granular-trust example, and the final direct question remain. I verified that text against the source after removing only the Markdown emphasis wrapper and spacing entity. Final packaging still needs to ensure the actual ODT contains that exact comment at the intended location.

The review makes no new clinical, legal, bibliographic, or detector-certification claim. Existing factual claims were preserved, not newly researched or approved. Separate source-bound preservation records for the two changed units are in gate_r2/preservation.json and dating_gate/preservation.json.

## Staging ODT structural check

I subsequently inspected converted/Bringing_Reparenting_Into_Real_Life.odt without modifying it. The reviewed staging snapshot has SHA-256 `f800a495d5555cbb6cb0e48f77ae21aea056a9a234dd816a0247accc9d348eeb`.

After excluding the table-of-contents furniture and comment metadata, all 99 ordered content nodes are present: 31 headings and 68 body/list blocks. The only extracted-text difference from revised.md is that two incidental doubled spaces in P066 became single spaces. No word, punctuation mark, emoji, or source content disappeared.

The ODT contains one genuine office:annotation whose paragraph text exactly matches the source note. It is anchored in the Can They Change capacity paragraph. The hyperlink target and label match the existing source link. Both lists are actual bulleted-list structures, with four and five items. Heading outline levels are one H1, six H2s, twenty H3s, and four H4s. Focusing and bardo retain italic character styles.

At this staging point, the table of contents contains only its Contents title, and a separate Contents paragraph also exists. Entries and title furniture therefore still require the root agent's planned TOC update. This structural check does not substitute for that update or the final rendered-page review.
