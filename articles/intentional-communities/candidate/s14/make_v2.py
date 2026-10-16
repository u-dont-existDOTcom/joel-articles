"""Section 14 draft v2 (2026-10-16): v1 with a break in each paragraph the march read found none in (review-r1, reading b:
every paragraph but P6, his father's lines). Each break is made from what the paragraph already says and placed where the
reaction belongs (E176 and section 13's landing lesson: at most three of the seven paragraphs end on a short line). Exact
old -> new pairs on v1; writes v2.md and v2-fixes.json. Run from this folder: python3 make_v2.py"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent
bl = [b.strip() for b in re.split(r'\n\s*\n', (HERE / 'v1.md').read_text(encoding='utf-8')) if b.strip()]
assert bl[0] == '# Dissolution and Exit' and bl[1].startswith('[image 18]') and len(bl) == 9
IDS = ['P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7']
text = dict(zip(IDS, bl[2:]))
FIX = {
 'P1': [("looking forward to its first harvest, but that’s exactly when it needs to be talked about.",
         "looking forward to its first harvest. Who would? But that’s exactly when it needs to be talked about.",
         'a question that follows from the sentence before it (who would want to talk about it then), mid-paragraph')],
 'P2': [("and for any unresolved claims?", "and for any unresolved claims? That’s a lot of loose ends!",
         'a remark about the list itself (E176: "That\'s a lot of deciding, I realize." passed march and trace)')],
 'P3': [("assign a bridge/successor for each critical function in advance. The institution may not be salvageable, but people "
         "still need breakfast, and basic life shouldn’t depend on reviving the commune.",
         "assign a bridge/successor for each critical function in advance, so basic life doesn’t depend on reviving the commune. "
         "The institution may not be salvageable, but who’s making breakfast tomorrow?",
         'the published "the people still need breakfast" as a question, the break; the basic-life clause moves up so the '
         'paragraph doesn\'t end on a short line')],
 'P4': [("without turning every friendship into evidence. People may leave hurt,",
         "without turning every friendship into evidence. Who wants that? People may leave hurt,",
         'a question about the sentence before it, mid-paragraph')],
 'P5': [("don’t have to die at the same time. American Commune",
         "don’t have to die at the same time. What a relief! American Commune",
         'the published "There is consolation in the fact that ..." said as a reaction, right after the fact it is about')],
 'P7': [("can go on.", "can go on. That gives me hope.",
         'the writer\'s own reaction to the closing claim; P2 and P7 are the only paragraphs that end on a short line')],
}
log = []
for pid, fixes in FIX.items():
    for old, new_s, why in fixes:
        assert text[pid].count(old) == 1, (pid, old)
        text[pid] = text[pid].replace(old, new_s)
        log.append({'id': pid, 'old': old, 'new': new_s, 'why': why})
(HERE / 'v2.md').write_text('\n\n'.join(bl[:2] + [text[p] for p in IDS]) + '\n', encoding='utf-8')
(HERE / 'v2-fixes.json').write_text(json.dumps(log, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
for p in IDS:
    print('%s %3d words | %s' % (p, len(text[p].split()), text[p][:160]))
print(len(log), 'fixes')
