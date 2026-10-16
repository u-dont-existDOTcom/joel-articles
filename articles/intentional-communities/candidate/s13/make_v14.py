"""Section 13 draft v14 (2026-10-15): v13 with Joel's answer to question 32 (18:28 UTC, "32b"): his published sentence
about his research report in place of my aside. Writes v14.md and v14-fixes.json. Run from this folder: python3 make_v14.py"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent


def blocks(md):
    return [b.strip() for b in re.split(r'\n\s*\n', md) if b.strip()]


v9 = blocks((HERE / 'v13.md').read_text(encoding='utf-8'))
IDS = [None, 'H1-P1', 'H1-P2', 'H1-P3', 'H1-P4', None, 'H2-P1', 'H2-P2', 'H2-P3', 'H2-P3b', 'H2-P4', None, 'H3-P1',
       'H3-P2', 'H3-P3', 'H3-P4', 'H3-P5', None, 'H4-P1', 'H4-P2', 'H4-P3', 'H4-P4', 'H4-P5', 'H4-P6', 'H4-P7', 'H4-P8',
       'H4-P9', None, 'H5-P1', 'H5-P2', 'H5-P3', 'H5-P4']
assert len(IDS) == len(v9) and all((i is None) == b.startswith('#') for i, b in zip(IDS, v9))
text = {i: b for i, b in zip(IDS, v9) if i}

FIX = {
 'H5-P3': [("(It's true that at first [my research](https://innerself.185-233-106-15.sslip.io/blog/commune-article-research/) "
            "kinda leaned too far toward the nation-state.)",
            "[My research](https://innerself.185-233-106-15.sslip.io/blog/commune-article-research/) initially leaned too far "
            "that way.",
            'Joel, 32 b (2026-10-15 18:28 UTC): his published sentence, as written; the link is to his research report, '
            '"so it\'s about that"')],
}
log = []
for pid, fixes in FIX.items():
    t = text[pid]
    for old, new, why in fixes:
        assert t.count(old) == 1, (pid, old)
        t = t.replace(old, new)
        log.append({'id': pid, 'old': old, 'new': new, 'why': why})
    text[pid] = t
out = [b if i is None else text[i] for i, b in zip(IDS, v9)]
(HERE / 'v14.md').write_text('\n\n'.join(out) + '\n', encoding='utf-8')
(HERE / 'v14-fixes.json').write_text(json.dumps(log, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('v14.md:', len([b for b in out if not b.startswith('#')]), 'paragraphs;', len(log), 'fixes; changed:', sorted(FIX))
