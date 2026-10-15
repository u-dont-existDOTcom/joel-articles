"""Section 13 draft v12 (2026-10-15): v11 with H5-P2 and H5-P4, which read AI in batch 291g, rebuilt from Emulate round f
(emu-f/out/i01-emuA.txt and i02-emuA.txt, from v11) with the published meaning put back word by word, and Joel's line
back in its place. Writes v12.md and v12-fixes.json. Run from this folder: python3 make_v12.py"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent
JOEL = "So work out the process before it's about anyone in particular."


def blocks(md):
    return [b.strip() for b in re.split(r'\n\s*\n', md) if b.strip()]


v11 = blocks((HERE / 'v11.md').read_text(encoding='utf-8'))
i = v11.index('## When Somebody Has to Go')
assert v11[i + 2].startswith('That said,') and v11[i + 4].startswith('Also pick a mediator')
FIX = {
 'H5-P2': ((HERE / 'emu-f' / 'out' / 'i01-emuA.txt').read_text(encoding='utf-8'), [
   ("So it’s important to think about how this might be done ahead of time.", JOEL,
    'his line (his answer 13, 2026-10-11), as he wrote it'),
   ('What might constitute cause for immediate action', 'What conduct might constitute cause for immediate action',
    'trace T5 and the published-essay stance check of r8: conduct'),
   ('What process will be used to decide whether to place temporary restrictions on someone?',
    'Who will decide whether to place temporary restrictions on someone?', 'the published "who decides temporary restrictions"'),
   ('How will evidence be preserved?', 'Who will preserve the evidence?', 'the published "who preserves evidence" (trace T5 of r5: who, not how)'),
   ('How can the person reply to the accusations and request a review or appeal of the decision?',
    'How can the person reply and request a review or appeal of the decision without endangering others?',
    'the published "without endangering others"; "the accusations" was Emulate\'s')]),
 'H5-P4': ((HERE / 'emu-f' / 'out' / 'i02-emuA.txt').read_text(encoding='utf-8'), [
   ('Why bother? It is useful to agree on a mediator or ombud in advance as people often do not trust',
    'Also agree on a mediator or ombud in advance. Why bother? People often do not trust',
    'the published instruction ("Also choose ... before the crisis"), not "it is useful"; "Why bother?" after it, where '
    'it answers something')]),
}
log, text = [], {}
for pid, (t, fixes) in FIX.items():
    log.append({'id': pid, 'source': 'emu-f/out/' + ('i01' if pid == 'H5-P2' else 'i02') + '-emuA.txt (from v11)'})
    for old, new, why in fixes:
        assert t.count(old) == 1, (pid, old)
        t = t.replace(old, new)
        log.append({'id': pid, 'old': old, 'new': new, 'why': why})
    text[pid] = t
out = list(v11)
out[i + 2], out[i + 4] = text['H5-P2'], text['H5-P4']
(HERE / 'v12.md').write_text('\n\n'.join(out) + '\n', encoding='utf-8')
(HERE / 'v12-fixes.json').write_text(json.dumps(log, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print(text['H5-P2']); print(); print(text['H5-P4'])
