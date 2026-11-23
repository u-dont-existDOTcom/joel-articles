#!/usr/bin/env python3
"""section_links_x1123a.py - link each section that questions 34 to 56 and this turn's report name to its anchor on the
live post (lesson toc-2026-11-23b; the post's 25 anchors read on 2026-11-23: live_anchors_20261123.txt)."""
import pathlib
import re
import sys

P = pathlib.Path(__file__).resolve().parents[2] / 'OWNER-QUESTIONS.md'
U = 'https://ibogaqueen.substack.com/i/181671197/'
TOP, OPEN = U + 'a-complete-guide-to-bio-de-armoring', U + 'psychology-is-the-software-biology-is-the-hardware'
P1, A, B, C, E = (U + 'part-1-the-science-why-we-do-this', U + 'a-the-metabolic-red-line',
                  U + 'b-the-overheating-cpu-glutamate-excitotoxicity', U + 'c-the-hardened-circuit-dynorphin-and-deltafosb',
                  U + 'e-the-save-button-memory-reconsolidation')
P2, HTP, ATP, UMP = (U + 'part-2-reducing-anxiety-and-depression', U + 'serotonin-bottleneck-pattern-5-htp-low-dose-p5p',
                     U + 'fixing-atp-signaling-if-cortisol-isnt-high', U + 'dopamine-receptor-burnout-daws-pattern-uridine-monophosphate')
EL, GS, SA, SC, P5 = (U + '1-electrolytes-choose-your-path', U + '2-the-glutamate-shield-anxiety',
                      U + 'scenario-a-the-glutamate-storm', U + 'scenario-c-the-void', U + 'part-5-the-timeline-the-8-week-path')

# (question, words as they stand, anchor): the first mention in that question's block
LINKS = [
    (34, 'The warning at the top', TOP), (34, 'Weeks 1–2', P5),
    (35, 'The warning at the top', TOP), (35, "the Shield's cycle rule", GS), (35, 'Weeks 1–2', P5),
    (36, 'The warning at the top', TOP), (36, 'the 5-HTP line in the Shield', GS), (36, 'Weeks 3–5', P5),
    (37, 'The opening', OPEN), (37, 'Part 1', P1),
    (38, 'The science', B), (38, 'the opening', OPEN), (38, 'Scenario A', SA),
    (39, 'Section A', A), (39, 'a paragraph in section B', B),
    (40, 'The science part', B), (40, 'Scenario A', SA),
    (41, "Weeks 1–2 Rescue line", P5), (41, 'science part', B), (41, 'Scenario A', SA),
    (42, 'the timing rule', GS),
    (43, 'Your paragraph in section C', C), (43, 'the timeline', P5), (43, 'Scenario C', SC),
    (44, 'The trials paragraph', C),
    (45, 'The science part', C), (45, 'Week 8+', P5),
    (46, 'Section E', E), (46, 'Scenario A', SA),
    (47, 'Part 2', ATP), (47, 'Weeks 1–2', P5),
    (48, 'The 5-HTP section', HTP), (48, 'Weeks 3–5', P5),
    (49, 'The 5-HTP section', HTP),
    (50, 'Part 2', ATP), (50, "the Shield's headings", EL),
    (51, 'Part 2', ATP), (51, 'Week 8+', P5),
    (52, 'The same list', EL),
    (53, 'Weeks 3–5', P5),
    (54, 'Scenario A', SA),
    (55, 'Its stages', P5),
    (56, 'Weeks 1–2', P5),
]
REPORT = [
    ('starving the brain of excitement at the top', TOP, 'at the top'), ("the\n  Void's", SC, "Void's"),
    ("UMP's hoped-for return", UMP, "UMP's"),
    ('the 5-HTP stop signs end', HTP, '5-HTP stop signs'),
    ('a new item before the agmatine warning', TOP, 'the agmatine warning'),
    ('the stop-signs paragraph at the top', TOP, 'at the top'),
]


def link(block, words, url, inner=None):
    inner = inner or words
    i = block.find(words)
    if i < 0:
        sys.exit('not found: %r' % words)
    j = i + words.index(inner)
    if block[max(0, j - 1)] == '[':
        return block
    return block[:j] + '[%s](%s)' % (inner, url) + block[j + len(inner):]


def main():
    t = P.read_text(encoding='utf-8')
    if U + 'scenario-a-the-glutamate-storm)' in t[t.index('## Open questions'):t.index('## For you to do')]:
        sys.exit('already linked')
    for q in sorted({n for n, _, _ in LINKS}):
        start = t.index('**🟣 %d.' % q)
        nxt = re.search(r'\n\*\*🟣 \d+\.|\n- 🟢 \*\*Not contradictions', t[start + 5:])
        end = start + 5 + nxt.start()
        block = t[start:end]
        for n, words, url in LINKS:
            if n == q:
                block = link(block, words, url)
        t = t[:start] + block + t[end:]
    for words, url, inner in REPORT:
        i = t.index(words)
        block = t[i:i + len(words)]
        t = t[:i] + link(block, words, url, inner) + t[i + len(words):]
    P.write_text(t, encoding='utf-8')
    print('linked', len(LINKS) + len(REPORT))


if __name__ == '__main__':
    main()
