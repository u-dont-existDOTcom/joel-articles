# Romance r23r2 — raw Substack native-object recovery

Updated: 2026-08-24

Status: publishing-source provenance only. This does **not** change `articles/romance/master.md`, article authority, owner-final status, or publication state.

## Source authority

Joel supplied raw Substack editor HTML directly in chat on 2026-08-24 after the provisional Markdown-only clipboard helper had already been generated. Per the active Substack protocol, the supplied raw editor HTML supersedes reconstruction for native-object identity/metadata and placement. The registered GitHub r23r2 master remains authority for prose.

The supplied raw HTML contains older/superseded prose in many places. That prose is **not** publication authority and must not be reintroduced. It is used only for native-object/source markup and link recovery.

## Recovered native objects from the supplied raw editor HTML

In source order:

1. image `6993d48e-37c8-4ccc-be3a-1e7fe695cb2a_1122x1402.png` — `Image2ToDOM`, 1122×1402, source byte metadata 2,181,781;
2. Share button — `ButtonCreateButton`, `%%share_url%%`;
3. digest-post preview — `DigestPostEmbed`, node `864d4289-6efd-4077-9204-3b05a0af2c8e`, canonical URL `https://ibogaqueen.substack.com/p/somatic-modalities-strategic-sequencing`;
4. image `cbf41294-3c6b-4ac7-b5b6-dd52b242b919_1055x1491.png` — `Image2ToDOM`, 1055×1491, source byte metadata 2,208,503;
5. YouTube `QqP3p_ysd84`;
6. image `abc295d2-f1ec-414c-83e0-c4df99fe5de3_1024x1535.png` — `Image2ToDOM`, 1024×1535, source byte metadata 2,389,704;
7. YouTube `ysZ_O50hhgM`;
8. YouTube `Nc0NU5PWO8Q`;
9. YouTube `450p7goxZqg`;
10. YouTube `SitT9ojqV1U`;
11. Subscribe button — `ButtonCreateButton`, `%%checkout_url%%`.

No standalone native Substack-uploaded video appears in the supplied raw editor HTML, so it does not require the native-video split/manual-insertion exception.

## r23r2-only object

The registered r23r2 master also contains YouTube `Li--FKwJu0Q`, which is not present in the supplied older raw editor HTML. Preserve it as a current r23r2 article object at its registered marker location, using the same confirmed native YouTube transfer structure keyed by its exact video ID. Do not drop it merely because the supplied historical HTML predates it.

## Transfer rule

- Registered r23r2 Markdown master SHA-256 remains `f1c2b9a3f0f3d9e123c3870ca5d741af8ed99bbf6f138e68b845de04b1a12a2c` and controls prose.
- Raw editor HTML controls recovered native-object metadata and placement anchors.
- Transfer payload removes only editor locks such as `contenteditable="false"` and `draggable="true"`; it retains native object classes, children, `data-component-name`, `data-attrs`, URLs, dimensions, order, and placement.
- Digest-post embed remains a digest preview rather than being misclassified by descendant media.
- YouTube remains its own object type.
- Share and Subscribe are retained as rich native button objects.
- The older raw-source `Interactive Claude app guide here.` heading is not in r23r2 and must not be reintroduced.

A user-facing local helper was generated from this reconciliation; external Substack publication/destination validation remains a separate owner action.