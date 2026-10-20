# Selected-text export oracle repair

The owner-upload comparison contains bold paragraph labels before the prose. The review interface correctly exports selected-text offsets relative to the whole passage. The browser test selected a later text node but incorrectly expected that node's local offsets. Thus the exact quote, note, decisions and persistence passed while the combined export check failed.

The test now computes expected offsets from a DOM Range beginning at the passage boundary. This preserves the contract rather than relaxing it: the expected quote, whole-passage offsets, scope, comment and decision history must all match. Article HTML and review UI are unchanged. A regression guards against returning text-node-local offsets. The exact affected browser test is rerun; prior successful unchanged review files are not regenerated.
