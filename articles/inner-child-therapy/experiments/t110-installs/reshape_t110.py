#!/usr/bin/env python3
"""Turn 110: Hear the Guard First and Before You Tell the Hardest Stuff the way GPT's review of the turn-109 sheet and I
agree on (experiments/t110-review/AGREED.md), as candidates for Joel's review page. Nothing is installed until he approves.

- Hear the Guard First (S1, with P8): the opening is his instruction and his question; then the exchange as one
  paragraph, in his own order from before turn 109 (his "It might say", the sting, "and that part remembers", his reply
  "Tell me what you remember, I'm listening." and his reason for it, his little one and "Peek-a-boo!", then pushing past
  and the Emmy); then the harder-voice paragraph, with "the Nurturer voice" named in place of "it the same" (P8); the
  roommate; the move-out paragraph, its long sentence split in two; the hopes paragraph; and the self-blame paragraph
  right after it, so "a job like that" still points at the part calling all this stupid.
- Before You Tell the Hardest Stuff (S3): his two danger lines go back after the dream line they limit, where he had them
  on 2026-10-19, so the section ends on the danger and the first paragraph is the topic and his "I'd assume".

Every other sentence is word for word and used once; the five word changes are EDITS below, and the check fails on any
other difference. The last two came after the first section check: a fresh cold read (experiments/t110-review/COLD-READ.md)
read "call it off" as calling off the guard, and couldn't tell which job "a job like that" meant, which GPT had also asked
to make plain.

  python3 reshape_t110.py            prints both candidates with their word counts
  python3 reshape_t110.py --install NOTE    installs both into the article (after his approval), NOTE saying which

Installing S1 also needs OWNER-EDITS.json in the same turn: joel-109-20261025 lists "It might say this will just be one
more performance" as text the article must not contain (turn 109 had made it "That part might say"), and bus-h3 holds the
section's paragraphs and their order (as experiments/t109-installs/owner_edits_t109f.py set them).
"""
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parents[1] / 'HUMANIZED-ARTICLE-SO-FAR.md'
SPLIT = re.compile(r'(?<=[.!?"”)])\s+(?=[A-Z"“(])')

SECTIONS = {
    'guard': {
        'head': '### Hear the Guard First', 'end': '\n### When to Change the Strategy',
        # as turn 109 left it (the second try): P1 voice and question (4 sentences), P2 harder voice (3), P3 performance (7),
        # P4 move-out (7), P5 hopes (4), P6 roommate (6), P7 self-blame (5)
        'counts': [4, 3, 7, 7, 4, 6, 5],
        'shape': [[(1, 1), (1, 2)],
                  [(3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (1, 3), (1, 4), (3, 6), (3, 7)],
                  [(2, 1), (2, 2), (2, 3)],
                  [(6, k) for k in range(1, 7)],
                  [(4, k) for k in range(1, 8)],
                  [(5, k) for k in range(1, 5)],
                  [(7, k) for k in range(1, 6)]],
    },
    'hardest': {
        'head': '#### Before You Tell the Hardest Stuff', 'end': '\n## Other Folks Also Have Hooks',
        # as turn 109 left it: P1 topic, "I'd assume" and the danger lines (5), P2 the DM (4: "Mr. Boopaloopa" is two to the
        # splitter), P3 reporting (3), P4 his question (3), P5 the dream (1)
        'counts': [5, 4, 3, 3, 1],
        'shape': [[(1, 1), (1, 2), (1, 3)],
                  [(2, k) for k in range(1, 5)],
                  [(3, k) for k in range(1, 4)],
                  [(4, k) for k in range(1, 4)],
                  [(5, 1), (1, 4), (1, 5)]],
    },
}

# (section, old words, new words): the only word changes
EDITS = [
    ('guard', 'That part might say this will just be one more performance',
     'It might say this will just be one more performance'),   # his words: it follows his question again
    ('guard', "I'd still keep it the same.", "I'd still keep the Nurturer voice."),   # P8: GPT's fix of what "the same" and "that voice" point to
    ('guard', 'toward your little one, and I think watching is what it wants anyway',
     'toward your little one. I think watching is what it wants anyway'),   # GPT's local readability fix: two sentences
    ('guard', 'who could call it off if things got to be too much',
     'who could call it all off if things got to be too much'),   # the cold read: "it" had just been the guard
    ('guard', 'Blaming yourself can be doing a job like that, too.',
     'Blaming yourself can be doing a protective job, too.'),   # GPT: tie self-blame to a part's protective job, plainly
]


def sentences(p):
    return [x for x in SPLIT.split(p) if x]


def section(s, key):
    spec = SECTIONS[key]
    i = s.index('\n' + spec['head'] + '\n') + 1
    j = s.index(spec['end'], i)
    return i, j


def old_paras(s, key):
    i, j = section(s, key)
    reader = re.sub(r'<!--.*?-->', '', s[i:j], flags=re.S)
    return [p.strip() for p in reader.split('\n\n')[1:] if p.strip()]


def candidate(s, key):
    """The section's new paragraphs: the old sentences in the new shape, then the three word changes."""
    spec = SECTIONS[key]
    paras = old_paras(s, key)
    S = [sentences(p) for p in paras]
    assert [len(x) for x in S] == spec['counts'], (key, [len(x) for x in S])
    used = sorted(x for xs in spec['shape'] for x in xs)
    assert used == sorted((p + 1, k + 1) for p in range(len(S)) for k in range(len(S[p]))), key
    new = [' '.join(S[p - 1][k - 1] for p, k in xs) for xs in spec['shape']]
    plain = list(new)
    for sec, a, b in EDITS:
        if sec != key:
            continue
        hits = [n for n, p in enumerate(new) if a in p]
        assert len(hits) == 1 and new[hits[0]].count(a) == 1, (key, a)
        new[hits[0]] = new[hits[0]].replace(a, b)
    # nothing but the edits changed: undo them and the sentences are the old ones, each once
    back = list(new)
    for sec, a, b in EDITS:
        if sec == key:
            back = [p.replace(b, a) for p in back]
    assert back == plain, key
    assert sorted(sum((sentences(p) for p in plain), [])) == sorted(sum(S, [])), key
    return paras, new


def install(s, key, note):
    i, j = section(s, key)
    sec = s[i:j]
    paras, new = candidate(s, key)
    notes = re.findall(r'<!--.*?-->', sec, flags=re.S)
    body = (SECTIONS[key]['head'] + '\n\n' + ''.join(n + '\n\n' for n in notes) + '<!-- ' + note + ' -->\n\n'
            + '\n\n'.join(new) + '\n')
    return s[:i] + body + s[j:]


def main():
    s = ART.read_text(encoding='utf-8')
    if '--install' in sys.argv:
        note = sys.argv[sys.argv.index('--install') + 1]
        for key in SECTIONS:
            s = install(s, key, note)
        ART.write_text(s, encoding='utf-8')
        print('installed')
        return
    for key in SECTIONS:
        old, new = candidate(s, key)
        print('==', key)
        for p in new:
            print('%4d | %s' % (len(p.split()), p))


if __name__ == '__main__':
    main()
