# Instagram embeds in Joel's published posts (2026-11-21 to 22)

Joel, 2026-11-21 19:07 UTC, after we found that Substack shows a deleted Instagram post as a blank box: "yes and add that
the joel-articles rules to do that" (list every dead embed, and make the check a rule). The rule is lesson
embeds-2026-11-21a (`docs/lessons/2026-11-21-1907-embeds.md`).

## What Substack does with an Instagram embed

- The post stores only an empty `InstagramToDOM` div whose `data-attrs` hold the id, title, author and `thumbnail_url`
  (a snapshot image Substack saved: `IG-snapshot-<id>.jpg`, a render of the embed, or `IG-meta-<id>.jpg`, the post's cover).
- Substack's script (bundle chunk 44642 on 2026-11-21) builds a sandboxed `data:` iframe for every reader, starting at
  520px, which loads Instagram's `embed.js` with the captioned embed and reports its height to the page.
- A dead post (deleted, private or restricted): Instagram's embed page sends only LOADING, never MEASURE, so its own
  iframe stays 2px tall and Substack's frame stays a blank 520px box, with no link.
- The frame never shrinks: the height is `Math.max` of several numbers including `document.documentElement.scrollHeight`,
  never less than the frame's own height (a post that renders 727px tall at 340px wide kept an 893px frame).
- Nothing in a post changes either: the caption and comments strip can't be turned off, and the sizing can't be fixed
  from the post.

## The 18 embeds on 2026-11-21 (all 102 published posts)

| Post | Instagram posts (author) | State |
| --- | --- | --- |
| 5-MeO-DMT ("Bufo") Guide | DQ_V5uZje4f (@cerebral_liberty) | live |
| Did Psychedelics Turn You LGBTQCIA+? | DP464qoCoND (@matthabusby), DTwLkregXm7 (@jordan_sather_) | dead: both now their cover images (below) |
| Did Psychedelics Turn You LGBTQCIA+? | DKnWYEmuUeW (@rigostarr) | live |
| Detoxing Quaxines, Parasites, ... | DR5GK_GkiLB (@gfbeef), DMoQEMqR_sL (@abcnews_au) | live |
| Somatic Therapy Modalities Map | DeM0MS0Mpch (@idasimones) | live |
| Somatic Therapy Modalities Map | DfZHKYpRzuG | dead: gone from the post when it was republished at 2026-11-21 19:12 UTC |
| Romance Advice I Wish My Parents Taught Me | DejqbH4xJtA (@britty_paige), Dc9hwfziBn8 (@evangelistjohnsonaluko) | live |
| Haoma: Loveyhuasca + Metta NMT + ZHoly3O ... | DQu5523D1F8 (@musicalbreathwork) | live |
| What If Everything Is Already Perfect? | Dfd1gZGN3cZ (@light_of_my_soul_22) | live |
| Inner Child Self-Love Reparenting Guide | DevfZkyDZSx, DdpLUKVyIaK, DYF3KH7EqsU, DdFgsXRjLYO, Dee0IoAEvnr (@monanyree), DeM0MS0Mpch (@idasimones) | live |

Every embed's saved snapshot image loaded, the dead ones' too.

## What was done

- 2026-11-22 17:26 UTC: the bug report (blank box for dead posts, frame never shrinks) and a request for a way to hide
  the caption and comments strip went to Substack through its support chat (substack.com/support), Joel's pick; its
  assistant answered that it submitted the report to the embeds team.
- 2026-11-22 17:28 UTC, Joel's pick: in "Did Psychedelics Turn You LGBTQCIA+?" the two dead embeds became their
  `IG-meta` cover images, captioned "@matthabusby on Instagram" and "@jordan_sather_ on Instagram", with no change to
  the text, through the editor's Update now with the post's settings unchanged (paid subscribers only) and no email.
  The nodes as they were are in `lgbtq-dead-embeds-before.json`, for undoing it.

## Checking again

Save a post's page, run `python3 tools/humanization/post_embeds.py POST.html --instagram`, open any instagram.com page
in the browser pane, paste `tools/humanization/instagram_alive.js`, then the line it printed.
