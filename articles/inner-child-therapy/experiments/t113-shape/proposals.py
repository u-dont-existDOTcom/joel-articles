#!/usr/bin/env python3
"""Turn 113: every edit proposed for Joel's review (his message of 2026-10-25 22:38 UTC, ../t113-answers/JOEL-20261025-2238.md:
"do the major edits as you suggested and then i can see what GPT thinks of all the changes (not just the headings idea but
fixing the way the sections read as you did with Hear the Guard)"), as operations on the article, checked here:

- a heading over each case, in the sections where each paragraph after the opening is its own case, so a reader can
  skip to theirs (his idea of 2026-10-25 21:40 UTC); every one a #### (the size of the guide's own small headings, like
  "Non-altered states can feel like this too" in Altered States Can Require Reparenting), so it reads as a signpost inside
  its section, never as one more section beside the ones already there (cold read A1's catch: at ###, Start With
  Whatever Showed Up's case headings would have stood level with Hear the Guard First);
- where a paragraph's first words name its case, those words become the heading and the sentence drops them
  (a "lead"), so nothing is said twice ("the first sentence of the para will often not connect anymore or be redundant");
- a long paragraph that holds two cases or two steps split in two, every sentence kept; once (Start With Whatever Showed
  Up), one sentence moves up three sentences to stay with what it is about (a 'move', checked: no word added or lost);
- his 109 A (Solomon's paradox's name on the gap, the rest of his sentence kept), the one sentence of new words.

A heading is LIFTED when its words are the paragraph's own (checked: a substring of it), and NEW otherwise; NEW words go
through the owner-delivery gate before Joel sees them (experiments/t113-gate/). A lead drop takes words away and nothing
else (checked). A split only adds a paragraph break at a sentence boundary (checked).

  python3 proposals.py            # checks every operation, writes PROPOSAL-ARTICLE.md and SECTIONS.json
  python3 proposals.py --show     # prints each section as it would read"""
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parents[1] / 'HUMANIZED-ARTICLE-SO-FAR.md'
OUT_MD = HERE / 'PROPOSAL-ARTICLE.md'
OUT_JSON = HERE / 'SECTIONS.json'
LINK = re.compile(r'\[([^\]]*)\]\([^)]*\)')

# Each section: its heading line, the level of its case headings, and its operations on paragraph k (1-based, the
# section's own paragraphs before the next heading of any level, notes not counted). Operations, applied in order:
#   ('head', k, text, 'lifted'|'new')   a heading just before paragraph k
#   ('lead', k, lead)                   paragraph k drops LEAD (its first words) and starts with a capital
#   ('split', k, start)                 paragraph k splits just before the sentence that starts with START
#   ('cut', k, old, new)                paragraph k's OLD becomes NEW, NEW being OLD with words taken out (checked)
#   ('move', sentence, before)          SENTENCE leaves its place in the section and goes just before the words BEFORE
#   ('swap', k, old, new)               paragraph k's OLD becomes NEW (new words: gated)
SECTIONS = [
    {'id': 'H-guard', 'line': '### Hear the Guard First', 'level': 4,
     'why': 'After your exchange (the question, what the part might say, your reply, and which voice to use), each paragraph is one thing the guard might do, or, the first, how you earn its trust, so a reader can go straight to theirs.',
     'ops': [('head', 4, 'Earning its trust, day to day', 'new'),
             ('head', 5, "If it won't step back", 'new'),
             ('head', 6, "If it's been calling all this stupid", 'lifted'),
             ('lead', 6, "If it's been calling all this stupid, "),
             ('head', 7, 'If it all feels like your fault', 'new')]},
    {'id': 'H-start', 'line': '## Start With Whatever Showed Up', 'level': 4,
     'why': 'After the path (what showed up, what to ask it, your line to say, and waiting), each paragraph is one of the things that can happen next. Your answer paragraph held two of them, a feeling to be present for and an instruction to be careful with, so it splits, and "How you picture all that is up to you" moves up three sentences to sit right after the forms an answer can take, which it is about. What to make of a fear or a stray thought gets its own paragraph.',
     'ops': [('move', 'How you picture all that is up to you, as long as it helps, and the simpler the better.', 'If it tells you to do something'),
             ('split', 4, 'If it tells you to do something'),
             ('head', 3, 'If no answer comes', 'new'),
             ('lead', 3, 'If nothing comes, '),
             ('head', 4, 'If you do get an answer', 'lifted'),
             ('lead', 4, 'Or if you do get an answer, '),
             ('head', 5, 'If it tells you to do something', 'lifted'),
             ('lead', 5, 'If it tells you to do something, '),
             ('head', 6, 'Which thoughts to talk to', 'new'),
             ('head', 8, "If it's anxiety", 'new'),
             # gate round 3 failed "When to stop" (it names no trigger); round 1 failed "If a part says no" (it leaves out the
             # hesitation and the cases, and says the sentence's opening twice). The fallback is his own condition, whole.
             ('head', 9, "If a part hesitates about being touched or about sex, or says no to going deeper in this work or to an altered state", 'lifted'),
             ('lead', 9, "If a part hesitates about being touched or about sex, or says no to going deeper in this work or to an altered state, ")]},
    {'id': 'H-change', 'line': '### When to Change the Strategy', 'level': 4,
     'why': 'Your first paragraph is the general case, nothing much changing; each one after it is a different reason to change course, and your last paragraph holds two of them.',
     'ops': [('head', 2, 'When your kind words sound empty', 'new'),
             ('head', 3, "If the relief doesn't last", 'new'),
             ('head', 4, 'How many tries would I give it?', 'lifted'),
             ('lead', 4, 'How many tries would I give it? '),
             ('head', 5, "If you'd rather stop", 'new'),
             ('split', 5, 'And if you keep following'),
             ('head', 6, 'If you keep following the reparenting steps correctly without getting the expected results', 'lifted'),
             ('lead', 6, 'And if you keep following the reparenting steps correctly without getting the expected results, ')]},
    {'id': 'H-escape', 'line': '## When Escape Leaves Reality Behind', 'level': 4,
     'why': 'After your opening on doses and protocols, each paragraph is its own warning, so a reader can find theirs: a trip that went badly, paranoia, being prone to mania or psychosis, who counts as trusted, coming back spaced out, stopping a medication or alcohol, and what you mix. Two paragraphs split where a second point starts: what to do when you can\'t tell what happened, after the paranoia examples and the THC line, and the medication warning, after coming back spaced out.',
     'ops': [('split', 3, 'If you can’t clearly understand what happened yourself'),
             ('split', 7, "And don't suddenly stop a medication"),
             ('head', 2, 'If a past trip went badly', 'new'),
             ('lead', 2, 'Your own drug history matters too. '),
             ('head', 3, 'Is your paranoia a warning sign?', 'new'),
             ('head', 5, 'If you might be prone to mania or psychosis', 'new'),
             ('head', 6, 'Who counts as trusted', 'new'),
             ('head', 7, 'If you keep coming back from trips confused or spaced out', 'new'),
             ('lead', 7, 'Say you keep coming back from trips confused or spaced out. '),
             ('head', 8, 'Before you quit a medication or alcohol', 'new'),
             ('lead', 8, 'And '),
             ('head', 9, 'What you mix', 'lifted')]},
    {'id': 'H-fake', 'line': '# When the Adult Voice Feels Fake', 'level': 4,
     'why': 'After Scott\'s line and your thoughts on why it can feel fake, each of the last three paragraphs is its own way through. Each heading is that paragraph\'s own first sentence or clause, so the paragraph starts right after it.',
     'ops': [('head', 5, 'Sometimes kindness feels scary more than fake', 'lifted'),
             ('lead', 5, 'Sometimes kindness feels scary more than fake. '),
             ('head', 6, 'Picturing one ideal parent seems to help some people', 'lifted'),
             ('lead', 6, 'And picturing one ideal parent seems to help some people. '),
             ('head', 7, 'For some people it only stops feeling fake in an altered state', 'lifted'),
             ('lead', 7, 'For some people it only stops feeling fake in an altered state, ')]},
    {'id': 'H-therapist', 'line': '# Finding a Therapist to Borrow Adulthood', 'level': 4,
     'why': 'After the first step, each paragraph is its own kind of help or its own question, so a reader looking for one of them can find it.',
     'ops': [('head', 2, 'Inner Child Reparenting therapists', 'lifted'),
             ('head', 3, 'If you want a licensed therapist', 'new'),
             ('head', 4, 'Before choosing a therapist', 'lifted'),
             ('lead', 4, 'Before choosing a therapist, '),
             ('head', 5, 'AI therapy', 'lifted'),
             ('lead', 5, 'Regarding AI therapy, ')]},
    {'id': 'H-hooks', 'line': '## Other Folks Also Have Hooks', 'level': 4,
     'why': 'After the question about what the other person keeps showing you, and its answer, each paragraph is a different case: whether they can change, a relationship that keeps making you feel less safe, having been hurt or threatened, and having hurt them yourself. The danger line gets its own paragraph and heading, so a reader who has been hurt or threatened finds it first, not under "meditate on why".',
     'ops': [('head', 3, 'Can they change?', 'new'),
             ('head', 5, 'If [a relationship](https://romance.u-dont-exist.com) keeps making you feel less safe', 'lifted'),
             ('lead', 5, 'If [a relationship](https://romance.u-dont-exist.com) keeps making you feel less safe, '),
             ('split', 5, "But if they've actually hurt or threatened you"),
             ('head', 6, "If they've actually hurt or threatened you", 'lifted'),
             ('lead', 6, "But if they've actually hurt or threatened you, "),
             ('head', 7, 'If you really did hurt them', 'lifted'),
             ('lead', 7, 'If you really did hurt them, '),
             ('cut', 7, 'Also easier said than done', 'Easier said than done')]},
    {'id': 'H-borrow', 'line': '## Borrow One Competency at a Time', 'level': 4,
     'why': 'After the idea (borrow one function at a time), each paragraph is one of the three jobs, so a reader who needs one of them can go straight there.',
     'ops': [('head', 2, 'For warmth', 'lifted'),
             ('lead', 2, 'For warmth, '),
             ('head', 3, 'For protecting', 'lifted'),
             ('lead', 3, 'For protecting, '),
             ('head', 4, 'For guiding', 'new')]},
    {'id': 'R-helping', 'line': "### How Would You Know It's Helping?", 'level': None,
     'why': 'Its first paragraph is 210 words, the longest in the guide but one: the question to ask, the signs of progress, the parenting picture, and what therapy should do for your days. Each gets its own paragraph, every sentence kept.',
     'ops': [('split', 1, 'Feeling calmer or having deeper insights'),
             ('split', 2, "It's like real parenting:"),
             ('split', 3, 'And if the therapy is actually working,')]},
    {'id': 'R-forgive', 'line': '# How to Forgive Without Forgetting', 'level': None,
     'why': 'Its order stays: the first paragraph says before the practice that you don\'t have to forgive first to get safe, set boundaries, hold someone accountable, get justice or get better, and the last answers it after. Only the last paragraph, 156 words, splits in two: that they still answer for it, and what can still be right.',
     'ops': [('split', 3, 'So a boundary can still be right.')]},
    {'id': 'W-solomon', 'line': '## Borrow Love—or Borrow the Perspective of Care', 'level': None,
     'why': 'Your 109 A: Solomon\'s paradox is the name of the gap the trick gets around, that people reason more wisely about other people\'s problems than about their own, so the name goes on that; the rest of your sentence stays.',
     'ops': [('swap', 3, 'has a rich history around it, and even has a name,',
              'has a rich history around it, and the blind spot behind it even has a name,')]},
]


def plain(s):
    return LINK.sub(r'\1', s)


def is_heading(b):
    return re.match(r'^#{1,6} ', b) is not None


def is_note(b):
    return re.fullmatch(r'(?:\s*<!--.*?-->\s*)+', b, flags=re.S) is not None


def section_slice(blocks, line):
    i = blocks.index(line)
    j = i + 1
    while j < len(blocks) and not is_heading(blocks[j]):
        j += 1
    paras = [k for k in range(i + 1, j) if not is_note(blocks[k])]
    return i, j, paras


def words(s):
    return plain(s).split()


def apply_section(blocks, sec):
    """Apply SEC's operations to the article's blocks in place; return (old paragraphs, new items, new words, problems).
    A new item is (kind, markdown): kind 'h2'..'h4' or 'p'."""
    i, j, paras = section_slice(blocks, sec['line'])
    old = [blocks[k] for k in paras]
    items = [['p', t] for t in old]          # the section's paragraphs as they will read, headings inserted below
    heads = {}                               # paragraph k -> heading text (k counts paragraphs after splits)
    new_words, probs = [], []
    for op in sec['ops']:
        kind = op[0]
        ps = [n for n, it in enumerate(items) if it[0] == 'p']
        if kind == 'split':
            _, k, start = op
            n = ps[k - 1]
            t = items[n][1]
            at = t.find(' ' + start)
            if at < 0 or t.count(' ' + start) != 1 or t[at - 1] not in '.!?"”)':
                probs.append('%s: split "%s" not at one sentence boundary of paragraph %d' % (sec['id'], start, k))
                continue
            items[n:n + 1] = [['p', t[:at]], ['p', t[at + 1:]]]
        elif kind == 'lead':
            _, k, lead = op
            n = ps[k - 1]
            t = items[n][1]
            if not t.startswith(lead):
                probs.append('%s: paragraph %d does not start with "%s"' % (sec['id'], k, lead))
                continue
            rest = t[len(lead):]
            items[n][1] = rest[0].upper() + rest[1:]
        elif kind == 'cut':
            _, k, a, b = op
            n = ps[k - 1]
            t = items[n][1]
            aw, bw = [w.lower() for w in a.split()], [w.lower() for w in b.split()]
            it = iter(aw)
            if t.count(a) != 1 or not all(any(w == x for x in it) for w in bw):
                probs.append('%s: cut "%s" is not in paragraph %d once, or adds words' % (sec['id'], a, k))
                continue
            items[n][1] = t.replace(a, b)
        elif kind == 'move':
            _, sent, before = op
            hits = [n for n, it in enumerate(items) if it[0] == 'p' and sent in it[1]]
            dest = [n for n, it in enumerate(items) if it[0] == 'p' and before in it[1]]
            if len(hits) != 1 or len(dest) != 1 or items[hits[0]][1].count(sent) != 1 or items[dest[0]][1].count(before) != 1:
                probs.append('%s: move "%s" not found once' % (sec['id'], sent[:40]))
                continue
            t = items[hits[0]][1]
            t = (t.replace(sent + ' ', '', 1) if (sent + ' ') in t else t.replace(' ' + sent, '', 1)).strip()
            items[hits[0]][1] = t
            items[dest[0]][1] = items[dest[0]][1].replace(before, sent + ' ' + before, 1)
        elif kind == 'swap':
            _, k, a, b = op
            n = ps[k - 1]
            t = items[n][1]
            if t.count(a) != 1:
                probs.append('%s: "%s" is not in paragraph %d once' % (sec['id'], a, k))
                continue
            items[n][1] = t.replace(a, b)
            new_words.append({'kind': 'sentence', 'paragraph': k, 'old': a, 'new': b})
        elif kind == 'head':
            _, k, text, how = op
            heads[k] = (text, how)
    # headings go in last, before the paragraph each names (paragraph numbers after the splits)
    ps = [n for n, it in enumerate(items) if it[0] == 'p']
    old_plain = plain(' '.join(old)).lower()
    for k in sorted(heads, reverse=True):
        text, how = heads[k]
        n = ps[k - 1]
        if how == 'lifted':
            if plain(text).lower() not in old_plain:
                probs.append('%s: lifted heading "%s" is not the section\'s own words' % (sec['id'], text))
        else:
            new_words.append({'kind': 'heading', 'paragraph': k, 'new': text})
        items.insert(n, ['h%d' % sec['level'], text])
    # checks: a lead drop only takes words away; a split only adds a break; nothing else changes
    before = ' '.join(words(' '.join(old)))
    after = ' '.join(words(' '.join(t for kd, t in items if kd == 'p')))
    if not any(op[0] == 'swap' for op in sec['ops']):
        bw, aw = before.split(), after.split()
        it = iter(w.lower() for w in bw)
        from collections import Counter
        moved = any(op[0] == 'move' for op in sec['ops'])
        if moved and Counter(w.lower() for w in aw) - Counter(w.lower() for w in bw):
            probs.append('%s: words added' % sec['id'])
        elif not moved and not all(any(w.lower() == x for x in it) for w in aw):
            probs.append('%s: the new paragraphs are not the old words with some taken away' % sec['id'])
        dropped = len(bw) - len(aw)
        leads = sum(len(words(op[2])) for op in sec['ops'] if op[0] == 'lead') + \
            sum(len(words(op[2])) - len(words(op[3])) for op in sec['ops'] if op[0] == 'cut')
        if dropped != leads:
            probs.append('%s: %d words dropped, but the leads hold %d' % (sec['id'], dropped, leads))
    # write back for the proposal copy of the article (not installed): the section's notes first, in their order, so
    # none is lost, then the section as it would read
    region = blocks[i + 1:j]
    rebuilt = [('#' * int(kd[1]) + ' ' + t) if kd != 'p' else t for kd, t in items]
    blocks[i + 1:j] = [b for b in region if is_note(b)] + rebuilt
    return old, items, new_words, probs


def build():
    md = ART.read_text(encoding='utf-8')
    blocks = re.split(r'\n\s*\n', md.strip('\n'))
    blocks = [b.strip('\n') for b in blocks]
    report, probs = [], []
    for sec in SECTIONS:
        old, items, nw, pr = apply_section(blocks, sec)
        probs += pr
        report.append({'id': sec['id'], 'heading': sec['line'], 'case_level': sec['level'], 'why': sec['why'],
                       'old': [plain(t) for t in old], 'old_md': old,
                       'new': [{'kind': k, 'text': plain(t), 'md': t} for k, t in items], 'new_words': nw,
                       'ops': [list(op) for op in sec['ops']]})
    return '\n\n'.join(blocks) + '\n', report, probs


def main():
    new_md, report, probs = build()
    for p in probs:
        print('PROBLEM', p)
    if probs:
        sys.exit(1)
    OUT_MD.write_text(new_md, encoding='utf-8')
    OUT_JSON.write_text(json.dumps({'article': str(ART.relative_to(HERE.parents[3])), 'sections': report}, indent=1,
                                   ensure_ascii=False) + '\n', encoding='utf-8')
    n_new = sum(len(r['new_words']) for r in report)
    n_heads = sum(1 for r in report for x in r['new'] if x['kind'] != 'p')
    print('%d sections, %d headings (%d with new words), %d new-word items in all' %
          (len(report), n_heads, sum(1 for r in report for w in r['new_words'] if w['kind'] == 'heading'), n_new))
    if '--show' in sys.argv:
        for r in report:
            print('\n' + '=' * 6, r['heading'])
            for x in r['new']:
                print(('  [%s] ' % x['kind']) + x['text'])


if __name__ == '__main__':
    main()
