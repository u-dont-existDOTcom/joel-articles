"""Section 14 draft v5 (2026-10-16): v4 with P2's childcare question at v3's length. v4's P2 read AI over its last 33 words when
alone (batch 305g: Human 89 words, AI 33), though Human in the heading group and the section; v3's P2, 11 words longer, read as
one Human window with the same last two sentences (303g). The screen of this wording (305g-x) read P2 alone Human (medium, one
window) and the heading group Human (high). The question keeps the published meaning that round r5's trace asked for, schooling
of any kind, not just attending a school. Writes v5.md and v5-fixes.json. Run from this folder: python3 make_v5.py"""
import json, pathlib

HERE = pathlib.Path(__file__).resolve().parent
FIX = [("Who keeps childcare and schooling going?",
        "Who keeps childcare going, and makes sure the kids’ schooling carries on?",
        'batch 305g: v4\'s shorter P2 split into two windows and its last 33 words read AI alone; at this length P2 reads as one '
        'Human window (305g-x). The published "keeps childcare and schooling going", schooling of any kind (trace r5 T1)')]
t = (HERE / 'v4.md').read_text(encoding='utf-8')
log = []
for old, new, why in FIX:
    assert t.count(old) == 1, old
    t = t.replace(old, new)
    log.append({'id': 'P2', 'old': old, 'new': new, 'why': why, 'disposition': 'b305/PREDICTIONS.md'})
(HERE / 'v5.md').write_text(t, encoding='utf-8')
(HERE / 'v5-fixes.json').write_text(json.dumps(log, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('wrote v5.md;', 'same as v4x.md' if t == (HERE / 'v4x.md').read_text(encoding='utf-8') else 'DIFFERS from v4x.md')
