#!/usr/bin/env python3
"""Turn 116: the owner-delivery gate's files (docs/HUMANIZATION-OWNER-DELIVERY-GATE.md) for the six suggestions on Joel's
reorganized guide (experiments/t116-joel/JOEL-GUIDE-20261103.md) that put words of mine into his paragraphs. Each is a
few words: a pointer that now points the wrong way, or a "that X" whose X his reorganization moved or cut. Every other
suggestion on the turn-116 page is a cut, a move, a typo fix or a question, outside the gate.

Each item gets a folder with DRAFT.txt (my words only, as they would read: the gate checks what the model wrote, and the
rest of the sentence is his; a first run with his whole sentence as the draft had the linter FAIL three items on his own
words, a list of three, "sometimes it helps" and "Now, once you've got"), CONTEXT.txt (its
section as it would read: the heading above it with its #s and the section's paragraphs, holding the draft once),
SOURCE.txt (the paragraph as it is now, and what the change must keep) and CHANGE.txt, and init writes ADMISSION.json.

  python3 make_gate_files.py"""
import json
import pathlib
import re
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
EXP = HERE.parent
GATE = ROOT / 'tools' / 'humanization' / 'owner_delivery_gate.py'
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
from paragraphs_alone import reader_blocks, plain  # noqa: E402
from substack_check_text import smart  # noqa: E402

GUIDE = (EXP / 't116-joel' / 'JOEL-GUIDE-20261103.md').read_text(encoding='utf-8')

# id: (a substring that finds the paragraph once, old words, new words, what the change must keep, why)
# MINE: the words of each change that are mine, the draft the gate checks (the rest of "new" is his)
MINE = {'G1': 'more on that in Noticing Counts, further on', 'G2': '(we get deeper into that further on)',
        'G3': 'your little one’s', 'G4': 'Your future self', 'G5': '(from Borrow Hindsight)', 'G6': 'the critical voice’s'}
ITEMS = {
    'G1': ('as described in Noticing Counts', '(as described in Noticing Counts)', '(more on that in Noticing Counts, further on)',
           'the instruction to notice who is doing the noticing, the borrowed adult, and the pointer to Noticing Counts',
           'His reorganization put Noticing Counts after this section (it is in Building Your Inner Adult now), so "as described in" points forward. "Further on" is his own way of pointing ahead (his "in « Untangling the Belonging Bargains » further on" and "« Altered States Can Deepen Therapy or Escapism » section further on").'),
    'G2': ('avoidance of differentiation', 'some avoidance of differentiation.', 'some avoidance of differentiation (we get deeper into that further on).',
           'his new phrase "avoidance of differentiation" and everything else in the paragraph',
           'He brought the word "differentiation" in here (it said "the pattern" before). Its own section, Differentiation: Keeping Your Own Ground, comes much later, in Bringing Reparenting Into Real Life, so this is the first time a reader meets the word. A pointer in his own form: "We get deeper into finding and building that self in « Untangling the Belonging Bargains » further on."'),
    'G3': ('earns that guard’s trust', 'that guard’s trust', 'your little one’s trust',
           'the roommate comparison, the rent, the real world day after day, and his two examples',
           'In the guide I gave him this paragraph sat under Hear the Guard First, where "that guard" was the protective part just met. He moved it to the end of Protecting and Building Trust With Your Little One and named it "Earning their trust, day to day", and cut Hear the Guard First; no guard has come up by this point (the security-guard image is later, in If the Love Isn\'t Coming Yet). His heading says whose trust: their, your little one\'s.'),
    'G4': ('That future you probably also knows', 'That future you', 'Your future self',
           'his question in the paragraph before, "probably also knows why you can\'t pull this off perfectly today", and the rest',
           'He cut the sentence that introduced the future self ("It\'s a question borrowed from your future self, ...") from the paragraph before, so "That future you" has nothing to point at. "Your future self" is the phrase he uses in The Chicken-and-Egg Problem ("Your future self might work").'),
    'G5': ('this cast of perfected future characters', 'this cast of perfected future characters in your mind',
           'this cast of perfected future characters (from Borrow Hindsight) in your mind',
           'his sentence and its job, opening the re-do section',
           'The cast is the wiser future versions of you and the other people in Borrow Hindsight (The Inner Guide), about 190 lines earlier; right before this section comes Forgiving Yourself, so "this cast" reads as if it had just been built.'),
    'G6': ('stay curious about its motivations', 'stay curious about its motivations', 'stay curious about the critical voice’s motivations',
           'the Mr. Rogers reframing trick, kernels of truth, not accepting its insults, and sending it on its way',
           '"Its" is the critical voice from the paragraph before the heading; between them comes the Mr. Rogers story about Lloyd, so the first "its" has no noun near it. The later "its" and "that voice" then follow from it.'),
}


def seq(md):
    return [(k, b) for k, b in reader_blocks(re.sub(r'<!--.*?-->', '', md, flags=re.S))]


def line(kind, b):
    t = plain(re.sub(r'^#+\s*', '', b) if kind == 'h' else b)
    t = smart(t).replace('‍', '').replace('️', '')
    return ('#' * len(re.match(r'^#+', b).group(0)) + ' ' + t) if kind == 'h' else t


def section_of(s, i):
    """The heading above block i and the paragraphs between it and the next heading, as lines."""
    h = max(j for j in range(i + 1) if s[j][0] == 'h')
    out = [line(*s[h])]
    for k, b in s[h + 1:]:
        if k == 'h':
            break
        if k == 'p':
            out.append(line(k, b))
    return out


def sentence_with(par, words):
    parts = re.split(r'(?<=[.!?…])["”’)]*\s+(?=[A-Z“"(‘\'0-9«])', par)
    hits = [p for p in parts if words in p]
    assert len(hits) == 1, (words, len(hits))
    return hits[0]


def init(d):
    files = ['--draft', str(d / 'DRAFT.txt'), '--context', str(d / 'CONTEXT.txt'), '--source', str(d / 'SOURCE.txt'),
             '--manifest', str(d / 'ADMISSION.json')]
    if not (d / 'ADMISSION.json').exists():
        out = subprocess.run([sys.executable, str(GATE), 'init'] + files, capture_output=True, text=True)
        if out.returncode not in (0, 2):
            sys.exit(out.stdout + out.stderr)
    m = json.loads((d / 'ADMISSION.json').read_text(encoding='utf-8'))
    return m['lint']['verdict_at_init'], [x['label'] for x in m['lint']['findings']]


def main():
    s = seq(GUIDE)
    inputs = {}
    for gid, (find, old, new, keeps, why) in ITEMS.items():
        hits = [i for i, (k, b) in enumerate(s) if k == 'p' and find in plain(b)]
        assert len(hits) == 1, (gid, len(hits))
        i = hits[0]
        before = line('p', s[i][1])
        assert before.count(old) == 1, (gid, old)
        after = before.replace(old, new)
        ctx = section_of(s, i)
        ctx = [after if x == before else x for x in ctx]
        context = '\n\n'.join(ctx)
        draft = MINE[gid]
        assert draft in new and context.count(draft) == 1, (gid, 'draft')
        sentence = sentence_with(after, new)
        d = HERE / gid
        d.mkdir(exist_ok=True)
        (d / 'DRAFT.txt').write_text(draft, encoding='utf-8')
        (d / 'CONTEXT.txt').write_text(context + '\n', encoding='utf-8')
        (d / 'SOURCE.txt').write_text(
            'The paragraph as it is now, in Joel\'s guide (his byline; his own reorganized file of 2026-11-03, his words and '
            'characters, French-style spacing included):\n\n%s\n\nWhat the change must keep: %s.\n' % (before, keeps), encoding='utf-8')
        (d / 'CHANGE.txt').write_text(
            'The change, in this one sentence: "%s" becomes "%s". The sentence as it would read: "%s" Why: %s It adds no '
            'claim, tone or promise; every other word and character of the paragraph is his and stays as it is.\n'
            % (old, new, sentence, why), encoding='utf-8')
        v, labels = init(d)
        m = json.loads((d / 'ADMISSION.json').read_text(encoding='utf-8'))
        inputs[gid] = {'the_change': {'old': old, 'new': new, 'why': why}, 'candidate_sha256': m['candidate_sha256'],
                       'context_sha256': m['context_sha256'], 'source_sha256': m['source_sha256'],
                       'lint_findings': m['lint']['findings'], 'lint_verdict': v}
        print('%s lint %-6s %s | %s' % (gid, v, labels, draft))
    (HERE / 'GATE-INPUTS.json').write_text(json.dumps(inputs, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')


if __name__ == '__main__':
    main()
