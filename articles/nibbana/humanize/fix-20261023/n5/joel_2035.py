"""Batch n5 (Nibbāna), part 1: Joel's answers to the reader's edit (question N4), put in word for word.

His message of 2026-10-23 20:35 UTC (../joel-20261023-2035-message.txt): "N4 1a 2 b 3a 4 a 5a 6a 7a 8a 9a 10a 11a 12a 13a
14a 15a 16a 17a 18a". So seventeen of the eighteen proposals in ../readers-edit/READERS-EDIT.md go in as written there,
and number 2 (cut "As they say, “life is stranger than fiction.” ...") stays out. He picked A on four where my pick was
B (5, 8, 9 and 16); they go in like the rest (gate E250).

How each kind goes in:
- A new heading takes the level of the heading of the section it splits, as number 18 says ("same ## level as its
  neighbours"), so it shows in the post's table of contents like the others (the article sends skimmers there: "use the
  Table of Contents on the left side of the window"). Where an existing heading moves down (6 and 11), it keeps its
  level, and the new one takes its old place at the same level.
- The readers worked from a reading text that hid pictures, so two moves needed a decision about a picture beside the
  moved paragraph. 17: the skydiving picture ("Yfw you thought I was kidding about meditating while skydiving.") goes
  with the caution paragraph it jokes about, which names skydiving. 14: the nuggets-and-sauces picture ("This one’ was
  over my head") stays where it was, now inside Frank's story, as the proposal moves only the monk's paragraph; it could
  be about either man, so the questions page asks him (question N5).
- Pangram doesn't read headings, so 1, 3, 4, 5, 6, 8, 10, 11, 13 and 18 leave the checked text as it was; 7, 9, 12, 14,
  15, 16 and 17 change it, and are read in place in recheck 6.

install_n1.py calls apply() after batch n4; the record is EDITS-n5-joel.json beside this file.
"""
import html, json, pathlib, re
from html.parser import HTMLParser

N5 = pathlib.Path(__file__).resolve().parent
VOID = {'br', 'img', 'hr', 'input', 'meta', 'link', 'source', 'wbr', 'area', 'base', 'col', 'embed', 'param', 'track'}
MSG = 'fix-20261023/joel-20261023-2035-message.txt'
PROPOSALS = 'fix-20261023/readers-edit/READERS-EDIT.md'


class _Blocks(HTMLParser):
    """The top-level blocks of the editor HTML (the children of the editor div), as (tag, start, end)."""

    def __init__(self, text):
        super().__init__(convert_charrefs=False)
        self.text, self.depth, self.cur, self.out = text, 0, None, []
        self.starts = [0] + [m.end() for m in re.finditer('\n', text)]

    def _off(self):
        line, col = self.getpos()
        return self.starts[line - 1] + col

    def handle_starttag(self, tag, attrs):
        if self.depth == 1:
            o = self._off()
            if tag in VOID:
                self.out.append((tag, o, self.text.index('>', o) + 1))
            else:
                self.cur = [tag, o]
        if tag not in VOID:
            self.depth += 1

    def handle_startendtag(self, tag, attrs):
        if self.depth == 1:
            o = self._off()
            self.out.append((tag, o, self.text.index('>', o) + 1))

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        self.depth -= 1
        if self.depth == 1 and self.cur is not None:
            o = self._off()
            self.out.append((self.cur[0], self.cur[1], self.text.index('>', o) + 1))
            self.cur = None


def blocks(work):
    p = _Blocks(work)
    p.feed(work)
    return [(t, a, b, plain(work[a:b])) for t, a, b in p.out]


def plain(fragment):
    return html.unescape(re.sub(r'<[^>]+>', '', fragment)).strip()


def one(work, test, what):
    hits = [b for b in blocks(work) if test(b)]
    assert len(hits) == 1, ('exactly one block must be', what, len(hits))
    return hits[0]


def para(work, first):
    return one(work, lambda b: b[0] == 'p' and b[3].startswith(first), 'a paragraph starting ' + repr(first))


def heading(work, title):
    return one(work, lambda b: re.fullmatch(r'h[1-6]', b[0]) and b[3] == title, 'the heading ' + repr(title))


def h(level, title):
    return '<%s>%s</%s>' % (level, html.escape(title, quote=False), level)


def section_level(work, pos):
    """The level of the last heading before POS: the heading of the section that a new heading at POS splits."""
    hs = [b for b in blocks(work) if re.fullmatch(r'h[1-6]', b[0]) and b[1] < pos]
    return hs[-1][0], hs[-1][3]


def insert_heading(work, title, first):
    t, a, b, _p = para(work, first)
    level, parent = section_level(work, a)
    return work[:a] + h(level, title) + work[a:], {'heading': title, 'level': level, 'splits': parent, 'before': first}


def move_heading_down(work, old_title, new_title, first):
    """Number 6 and 11: NEW_TITLE takes the old heading's place, at its level; OLD_TITLE moves down above FIRST."""
    t, a, b, _p = heading(work, old_title)
    work = work[:a] + h(t, new_title) + work[b:]
    t2, a2, b2, _p2 = para(work, first)
    return work[:a2] + h(t, old_title) + work[a2:], {'heading': new_title, 'level': t, 'in_place_of': old_title,
                                                      'moved': old_title, 'before': first}


def move_blocks(work, first_moved, n_blocks, after_first, after_extra=0, before=False):
    """Take the block starting FIRST_MOVED and the N_BLOCKS - 1 blocks after it, and put them after the paragraph
    starting AFTER_FIRST and the AFTER_EXTRA blocks that follow it (or before it, with BEFORE)."""
    bl = blocks(work)
    i = next(k for k, b in enumerate(bl) if b[0] == 'p' and b[3].startswith(first_moved))
    a, b = bl[i][1], bl[i + n_blocks - 1][2]
    moved = work[a:b]
    rest = work[:a] + work[b:]
    bl2 = blocks(rest)
    j = next(k for k, x in enumerate(bl2) if x[0] == 'p' and x[3].startswith(after_first))
    at = bl2[j][1] if before else bl2[j + after_extra][2]
    return rest[:at] + moved + rest[at:], [x[0] + ': ' + x[3][:80] for x in bl[i:i + n_blocks]]


def apply(work):
    rec = []

    def done(n, kind, text_changed, **kw):
        rec.append(dict(item=n, pick='A', kind=kind, pangram_text_changed=text_changed, **kw))

    # 1. A heading where the cost of the trips begins.
    work, d = insert_heading(work, 'When the Afterglow Wore Off', 'But the afterglow only lasted 1-2 weeks')
    done(1, 'heading', False, **d)
    # 2. B: "As they say, “life is stranger than fiction.” It really does seem like a dream, to me anyway." stays.
    rec.append(dict(item=2, pick='B', kind='left as it is', pangram_text_changed=False,
                    note='the line stays: it starts the article’s dream thread'))
    # 3. The suttas' part of "Then I Found The Map Past Oneness".
    work, d = insert_heading(work, 'What the Suttas Say About Unification', 'MN 137 gives a two-step recipe.')
    done(3, 'heading', False, **d)
    # 4. The room event under its own name.
    work, d = insert_heading(work, 'The Room Event', 'So, back to desperate little me in bed beside the then-wife I feared.')
    done(4, 'heading', False, **d)
    # 5. His two terms, above the paragraphs that name them.
    work, d = insert_heading(work, 'Body-Limited and Body-Uncontained Nibbāna',
                             'The finger episode was a small flashback of my full first nibbāna experience')
    done(5, 'heading', False, **d)
    # 6. "What’s Next?" where "What “Already Perfect” Means" was; that heading moves down above its definition. The empty
    # paragraph after the father video stays where it is, before the heading, as his spacing after a video.
    work, d = move_heading_down(work, 'What “Already Perfect” Means', 'What’s Next?', 'By “already perfect,” I mean that')
    done(6, 'heading and a heading moved', False, **d)
    # 7. The Parinibbāna bullet ends after its first Iti 44 sentence; the rest becomes a paragraph under the list.
    t, a, b, _p = one(work, lambda x: x[0] == 'ul' and 'Parinibbāna:' in x[3], 'the taxonomy list')
    ul = work[a:b]
    cut_h = html.escape('parinibbāna.', quote=False) + ' Iti 44 also shows'
    assert ul.count(cut_h) == 1 and ul.endswith('</p></li></ul>'), 'the Parinibbāna bullet must end the list'
    k = ul.index(cut_h) + len(html.escape('parinibbāna.', quote=False))
    rest = ul[k + 1:-len('</p></li></ul>')]
    new_ul = ul[:k] + '</p></li></ul>'
    work = work[:a] + new_ul + '<p>' + rest + '</p>' + work[b:]
    done(7, 'bullet split into a paragraph', True, bullet_ends='Iti 44 agrees on the difference between nibbāna & '
         'parinibbāna.', paragraph=plain(rest)[:90] + ' ...')
    # 8. A heading for the SN 22.22 paragraph.
    work, d = insert_heading(work, 'Why the Tangle Is Heavy', 'In SN 22.22 the five aggregates')
    done(8, 'heading', False, **d)
    # 9. The parenthetical and the space before it.
    t, a, b, _p = para(work, 'In SN 22.22 the five aggregates')
    old = 'the burden (even an arahant feels the first dart) of suffering'
    assert work[a:b].count(old) == 1
    work = work[:a] + work[a:b].replace(old, 'the burden of suffering') + work[b:]
    done(9, 'cut', True, cut='(even an arahant feels the first dart)', sentence_now='... the five aggregates that make up '
         'the unified body-mind are the burden of suffering, and craving is ...')
    # 10. The second subject of "Binding Assembles the Mind".
    work, d = insert_heading(work, 'The Capacity for Suffering', 'The main question for me and for the Buddha is whether')
    done(10, 'heading', False, **d)
    # 11. "What the Books Never Made Clear" where "How the Experiential Key Can Fade" was; that heading moves down.
    work, d = move_heading_down(work, 'How the Experiential Key Can Fade', 'What the Books Never Made Clear',
                                'The suttas clearly show that the Buddha succeeded in liberating')
    done(11, 'heading and a heading moved', False, **d)
    # 12. "That creates a practical problem." up across the heading, to end the paragraph before it.
    s12 = 'That creates a practical problem. '
    t, a, b, _p = para(work, s12 + 'In DN 3 and MN 56')
    assert work[a:b].startswith('<p>' + s12)
    work = work[:a] + '<p>' + work[a + 3 + len(s12):]
    t, a, b, _p = para(work, 'The funny part is that the words may have survived')
    assert work[a:b].endswith('the picture on the box has.</p>')
    work = work[:b - 4] + ' ' + s12.strip() + work[b - 4:]
    done(12, 'sentence moved up across the heading', True, sentence=s12.strip(),
         now_ends='... doesn’t mean that the picture on the box has. That creates a practical problem.',
         section_opens='In DN 3 and MN 56, the Buddha waits until ...')
    # 13. The section's second half, about AtR and the people in it.
    work, d = insert_heading(work, 'AtR’s Authentication Culture', 'AtR’s map saved me, but I still can’t recommend')
    done(13, 'heading', False, **d)
    # 14. The monk's paragraph after Frank's second paragraph and the video its colon introduces; the picture after the
    # monk's paragraph stays where it was (question N5).
    work, moved = move_blocks(work, 'But the problem isn’t as surprising with a YouTube star', 1,
                              'Frank did suffer much less after softening his identity', after_extra=1)
    nxt = blocks(work)
    k = next(i for i, x in enumerate(nxt) if x[3].startswith('But the problem isn’t as surprising with a YouTube star'))
    assert nxt[k - 1][0] == 'div' and 'youtube' in work[nxt[k - 1][1]:nxt[k - 1][1] + 200], 'after the video'
    done(14, 'paragraph moved', True, moved=moved, now_after='Frank did suffer much less ... YouTube channel: and its video',
         picture='the picture “This one’ was over my head” stays between Frank’s two paragraphs (question N5)')
    # 15. The rest of the MN 89 bullet, as a nested item under its question.
    t, a, b, _p = one(work, lambda x: x[0] == 'ul' and 'Are you more joyful' in x[3], 'the stream-entry questions')
    ul = work[a:b]
    m = re.search(r'(<li><p>Are you more joyful.*?</a>\?) (The standard isn.*?)(</p></li>)', ul, re.S)
    assert m and 'So enlightenment isn' in m.group(2)
    nested = m.group(1) + '</p><ul><li><p>' + m.group(2) + '</p></li></ul></li>'
    ul = ul[:m.start()] + nested + ul[m.end():]
    work = work[:a] + ul + work[b:]
    done(15, 'nested item', True, question='Are you more joyful and enjoyable to be around without becoming a '
         'people-pleaser, as in MN 89?', nested=plain(m.group(2))[:80] + ' ... So enlightenment isn’t a simple bliss switch.')
    # 16. The section's last paragraph up, after its first one (the comic after the first paragraph now follows both).
    work, moved = move_blocks(work, 'For me, nibbāna was really like waking up from a dream', 1,
                              'The lucid-dream comparison from earlier also shapes')
    done(16, 'paragraph moved', True, moved=moved, now_after='The lucid-dream comparison from earlier ... If you’ve ever '
         'had a lucid dream, you know what I’m talking about.', section_ends='the Diamond Sutra verse and its picture')
    # 17. The caution and its skydiving picture to the end of "Try a Tiny Bit of Nibbāna".
    work, moved = move_blocks(work, 'The farther unification loosens, the less useful you become', 2,
                              'A similar version may work even better while walking')
    assert 'skydiving' in moved[1], moved
    done(17, 'paragraph moved, with its picture', True, moved=moved, now_after='A similar version may work even better '
         'while walking: ... Either way, see whether the self loosens.')
    # 18. What lingers afterward.
    work, d = insert_heading(work, 'What Remains Afterward', 'Most of the unification usually returns afterward.')
    done(18, 'heading', False, **d)
    out = {'source': MSG, 'answers': 'N4 1a 2 b 3a 4 a 5a 6a 7a 8a 9a 10a 11a 12a 13a 14a 15a 16a 17a 18a',
           'proposals': PROPOSALS, 'edits': rec}
    (N5 / 'EDITS-n5-joel.json').write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    return work, rec
