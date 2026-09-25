# Inner Child Therapy — raw-source delta, 2026-09-25

Status: **EXACT SNAPSHOT STORED ON WRITER BRANCH / NOT YET REGISTERED AS THE WORKING MASTER**

## Owner statement (Joel, 2026-09-25 18:23 UTC)

> "also i have modified the original AI guide to make sure the nurturing is not 'good enough' with non-cruelty, but i don't think it changes any sections we edited. pasting the substack AI guide now"

## Files

- Snapshot (exact owner paste): `experiments/SOURCE-SNAPSHOT-20260925-OWNER-SUBSTACK.html`, 151383 bytes, SHA-256 `20073058fef619d8a8f5aa7fef8337face5ed50cf89d17c8142138effdb125b6`.
- Baseline: `master.html`, 150330 bytes, SHA-256 `372a43cb69b3f736ae2df4bcce1a627aa5a0318ec4ecf55ee7a2b4edafbf13bd` (the 2026-09-20 registered working master).
- Method: prior raw source → current raw source, per the `parallel-source-humanization-lineages` lock. The humanized assembly is a separate, unsynced lineage, so it isn't the baseline.

## The seven text changes

1. **Borrow One Function at a Time** (Borrowed Nurturer). "Begin with non-cruelty if love feels inaccessible" → "Begin with non-judgement if love feels inaccessible". Added: "Non-judgement is enough to begin establishing the adult position, but not necessarily enough to ask the child to trust, open, or receive care. The next borrowed nurturer step is to find a nurturer in your life that you can remember fondly. If there was none, you can look to examples like Mr. Rogers, or spiritual love you’ve felt, if you have."
2. **A Smaller Doorway: Goodwill**.
   - "Warm love, goodwill, and simply refusing cruelty" → "Warm love, goodwill, and simply refusing judgement and especially refusing cruelty".
   - "There is no requirement to reach “I love you.”" → "… “I love you” right away."
   - "begin with non-cruelty without renaming it love or treating the difficulty as failure" → "begin with non-cruelty and non-judgement and borrow more love over time".
   - New paragraph: "Non-cruelty is the floor, not the whole relationship. If you normally attack, shame, abandon, or force the child, stopping that is the first requirement. But a child who has learned not to trust you may reasonably remain guarded when you merely stop hurting them. Once hostility is paused, borrow actual warmth, protection, or wisdom from a person, spiritual presence, memory, or other source that genuinely evokes it. Let the adult learn that feeling first; then bring it to the child. Do not demand trust as payment for a temporary ceasefire."
3. **Make a Simple Vow**. "a sincere wish for wellbeing or a commitment to non-cruelty" → "a sincere wish for wellbeing and a commitment to non-cruelty". Added: "Borrow the nurturer to improve this."
4. **A Heart-to-Child Loop**. "Non-cruelty is enough for a first session." → "Non-judgement is a place to start."
5. **Altered States Can Require Reparenting**. "It took some minutes, but the demon left" → "It took some minutes, but once that love was seen as enduring, the demon left".
6. Same section. "you can at least send love to your frightened inner child" → "you can first send love to your frightened inner child".
7. **Non-altered states can feel like this too**. "if you don’t have the inner parent developed" → "if you don’t have the loving, protective inner parent developed".

## Non-text changes

- Two images were re-uploaded with new asset IDs, both still 1122×1402 PNG:
  - the image near the top (`c8b6db18…` → `40c24f21…`);
  - the method map after "The image below maps out the details as best as I can fit" (`eba3d518…` → `718d0e76…`, alt now null).
  - Image content wasn't compared, since the CDN isn't reachable from here. The humanized My Journey ends on that sentence, so a sync should use the new map asset.
- Minor markup changes:
  - one empty paragraph added before the "Before You Try to Go Deep" h1;
  - an empty class attribute dropped from the title h1;
  - video-player UI markup and a poster-refresh timestamp changed.
- `~/work/lane/srcupdate/pairs.json`, SHA `cf6b6cb4d00b503eb0a4f199101ca5fd2eb6961add34473781fcd3c635929526`, holds 37 minimal unique replacement pairs. Applied in order to the baseline, they reproduce the snapshot byte for byte. The snapshot on this branch was built that way and hash-checked.

## Projection onto the humanization branch

None of the seven text changes falls in a section that has humanized text in `HUMANIZED-ARTICLE-SO-FAR.md`; those six source sections haven't been humanized yet. That confirms Joel's read. When they are humanized, the new wording is the source.

Direction check: the change (non-cruelty is the floor; borrow actual warmth and let the adult learn it before bringing it to the child) agrees with humanized text already accepted. Dangerous-adult P7 says "loving-kindness is easier to pick up from someone who already has some", and Joel's new Chicken-and-Egg opening says "the loving Nurturer".

## Registration (deliberately not done on this writer branch)

`master.html` is still the 2026-09-20 source. Its SHA is named in all of these:
- `OWNER-LOCKS.json` (`working-master-source-identity`);
- `SOURCE-EVIDENCE.json` (twice);
- `CURRENT-STATE.md`;
- `HUMANIZATION-HANDOFF-20260921.md`;
- `DETECTOR-EVIDENCE.json`;
- `EDITORIAL-STATUS.json`;
- `SOURCE-STRUCTURE-INVENTORY-20260920.json`.

Swapping the master is a registration/reconciliation step (`PARALLEL-WRITE-LOCK.json`: writer turns don't update current-state files). This branch therefore stores only the exact snapshot and this delta.

To register:
1. Copy the snapshot to `master.html`.
2. Update those references.
3. Regenerate the structure inventory. The changes to cover: one added text paragraph, one added empty paragraph, and two new image asset IDs.
4. Move the 2026-09-20 identity to a historical claim, as was done for 2026-09-15.
