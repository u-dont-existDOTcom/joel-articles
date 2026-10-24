"""Batch n6 (Nibbāna): Emulate's round 4 for recheck 6's red, spliced sentence by sentence (2026-10-23, Joel's message of
22:29 UTC gave recheck 6's link).

The red (../recheck6/SCORE.md; feed 6d05010a, Mostly Human Written, 1.1% AI, 6 of 121 windows AI, all Low):
- window 35: "The texts distinguish that from ordinary sense-consciousness (viññāṇaṃ) established when one thing perceives
  another." (his published words; light green in recheck 5);
- windows 81 and 82: the MN 89 note his N4 15 nested: "In MN 75, the Buddha says ...", then "So enlightenment isn’t a
  simple bliss switch." with the next question, "Does the Dhamma now feel intuitively coherent rather than merely
  conceptual?" (the note is the plain version he passed, plain-29; the question is his published words);
- windows 91 and 92: the first two sentences of the lucid-dream paragraph (his published words), and window 96: the first
  two sentences of his 12:30 rewrite "I used to attribute ...": the neighbours of his N4 16 move.

Emulate ran on the whole paragraphs the red covers (E235, E244), three samples (ca, cb, cc; BUNDLE4.json). Only the red
sentences go back, each from the sample that keeps its meaning best; every change I made to Emulate's words is in "mine"
with its reason. Where no sample keeps a sentence's meaning, his words stay: "So enlightenment isn’t a simple bliss
switch." (no sample has it) and his "I used to attribute ..." sentences (each sample loses "the famous stanza I loved", the
certainty of "I found out", or who said it).

Inline markup is kept by position: a link or italics outside a replaced sentence stays where it was, and one inside it
goes on the same words in the new sentence, or is dropped (and recorded) when those words are gone.

  python3 articles/nibbana/humanize/fix-20261023/n6/emulate_n6.py --prompt   writes REVIEW-PROMPT.txt for a fresh reader
  (install_n1.py calls apply() after batch n5)
"""
import argparse, html, json, pathlib, re, sys

N6 = pathlib.Path(__file__).resolve().parent
ROOT = N6.parents[4]


def sample(run, key):
    return (N6 / run / (key + '.out.txt')).read_text(encoding='utf-8').strip()


SPLICES = {
    'n6-aware': dict(
        first='I use awareness to mean bare', run='ca', key='NB-aware',
        old='The texts distinguish that from ordinary sense-consciousness (viññāṇaṃ) established when one thing perceives '
            'another.',
        take=('It is in contrast to', 'perceives another.'),
        mine=[('viññånaü (“sense consciousness”)', 'viññāṇaṃ (“sense consciousness”)',
               'Emulate garbled the diacritics; the article\'s own spelling (E246)')],
        windows='35 (Low) in recheck 6, alone; Human, Low, in recheck 5'),
    'n6-mn75': dict(
        first='The standard isn', run='ca', key='NB-mn89note',
        old='In MN 75, the Buddha says that what ordinary people perceive as sensual pleasure, he felt as pain.',
        take=('Also remember this quote', 'he feels as pain.'),
        mine=[('Also remember this quote from the Buddha in MN 75 where he says',
               'Also, there’s this quote from the Buddha in MN 75 where he says',
               'the quote comes here for the first time (MN 75 came earlier, with the leper), so there is nothing to '
               'remember')],
        windows='81 (Low) in recheck 6, after his N4 15 nested the note'),
    'n6-question': dict(
        first='Does the Dhamma now feel intuitively', run='cb', key='NB-mn89note',
        old='Does the Dhamma now feel intuitively coherent rather than merely conceptual?',
        take=('Does the dhamma make', 'merely conceptual?'),
        mine=[('the dhamma', 'the Dhamma', 'the article’s own spelling (E246)'),
              ('to yuo now', 'to you now', 'a typo')],
        windows='82 (Low) in recheck 6, with "So enlightenment isn’t a simple bliss switch.", which stays (no sample has it)'),
    'n6-lucid': dict(
        first='The lucid-dream comparison from earlier', run='cc', key='NB-lucid',
        old='The lucid-dream comparison from earlier also shapes how I understand the seven-life limit said to be had by the '
            'stream-enterer. Once the dream is known as a dream, it becomes naturally difficult to remain stuck in it, '
            'similar to how hard it is to be absorbed in a movie when the lights go on and you remember you’re in a '
            'theater.',
        take=('To follow up on the lucid dreaming analogy', 'you\'re in a theater.'),
        mine=[('the fact that the Stream Entered individual has', 'the idea that the stream-enterer has',
               'his "said to be": the seven-life limit is the suttas\' claim, not a fact he asserts; and the article\'s own '
               'term (E246)'),
              ('and it relates in that once you know', 'and that analogy shapes how I understand it: once you know',
               'the reader (REVIEW.md, item 4): his own reading ("shapes how I understand") was lost, and "it relates" was '
               'vague'),
              ('stay in a movie', 'stay absorbed in a movie',
               'the reader (item 4): "absorbed" was lost, and "stay in a movie" could read as staying in the seat')],
        windows='91 and 92 (Low) in recheck 6, the paragraph before his N4 16 move; "If you’ve ever had a lucid dream, '
                'you know what I’m talking about." stays his'),
}


class _Inline:
    """A paragraph's inner HTML as plain text with the positions of its inline tags."""

    def __init__(self, inner):
        spans, out, stack, pos = [], [], [], 0
        for m in re.finditer(r'<(/?)(\w+)[^>]*>|([^<]+)', inner):
            if m.group(3) is not None:
                t = html.unescape(m.group(3))
                out.append(t)
                pos += len(t)
            elif m.group(2) == 'br':
                raise ValueError('a line break inside the paragraph')
            elif not m.group(1):
                stack.append((m.group(0), m.group(2), pos, len(spans) + len(stack)))
            else:
                open_tag, name, start, order = stack.pop()
                assert name == m.group(2), (name, m.group(2))
                spans.append((order, [start, pos, open_tag, '</%s>' % name]))
        assert not stack
        # in the order they opened (2026-10-24): two tags on the same words came out the other way round, <em><a> for his
        # <a><em>, in four places; the same as tools/humanization/html_text_edit.py
        self.spans = [s for _o, s in sorted(spans, key=lambda x: x[0])]
        self.text = ''.join(out)

    def replace(self, old, new):
        assert self.text.count(old) == 1, old[:60]
        i = self.text.index(old)
        j, d = i + len(old), len(new) - len(old)
        dropped, kept = [], []
        for s in self.spans:
            a, b, o, c = s
            if b <= i:
                kept.append(s)
            elif a >= j:
                kept.append([a + d, b + d, o, c])
            elif a >= i and b <= j:
                words = self.text[a:b]
                k = new.find(words)
                if k >= 0 and new.count(words) == 1:
                    kept.append([i + k, i + k + len(words), o, c])
                else:
                    dropped.append(o + words + c)
            else:
                raise ValueError('a tag crosses the replaced text: ' + o)
        self.text = self.text[:i] + new + self.text[j:]
        self.spans = kept
        return dropped

    def html(self):
        # Tags that close at one place close in the reverse of the order they opened, so nesting is kept (2026-10-24: a
        # link inside italics that ended where the italics ended came out as <em><a>...</em></a> before this)
        events = []
        for n, (a, b, o, c) in enumerate(self.spans):
            events.append(((a, 1, -b, n), o))
            events.append(((b, 0, -a, -n), c))
        events.sort(key=lambda e: e[0])
        out, last = [], 0
        for (p, _k, _x, _n), tag in events:
            out.append(html.escape(self.text[last:p], quote=False))
            out.append(tag)
            last = p
        out.append(html.escape(self.text[last:], quote=False))
        return ''.join(out)


def new_text(s):
    out = sample(s['run'], s['key'])
    a, b = s['take']
    i = out.index(a)
    out = out[i:out.index(b, i) + len(b)]
    for x, y, _why in s['mine']:
        assert out.count(x) == 1, (x, out)
        out = out.replace(x, y)
    return out


def para_bounds(work, first):
    hits = [(m.start(1), m.end(1)) for m in re.finditer(r'<p\b[^>]*>(.*?)</p>', work, re.S)
            if html.unescape(re.sub(r'<[^>]+>', '', m.group(1))).lstrip().startswith(first)]
    assert len(hits) == 1, ('one paragraph must start with', first, len(hits))
    return hits[0]


def apply(work):
    recs = []
    for key, s in SPLICES.items():
        a, b = para_bounds(work, s['first'])
        p = _Inline(work[a:b])
        old = s['old']
        if p.text.count(old) != 1:  # the editor's straight apostrophes
            old = old.replace('’', "'")
        new = new_text(s)
        dropped = p.replace(old, new)
        work = work[:a] + p.html() + work[b:]
        recs.append({'key': key, 'old': s['old'], 'new': new, 'windows': s['windows'],
                     'source': 'Emulate sample %s (%s)' % (s['run'], s['key']),
                     'mine': [{'replace': x, 'with': y, 'why': w} for x, y, w in s['mine']],
                     'markup_dropped': dropped, 'check': None, 'try': None,
                     'result': 'read in place in the next recheck (recheck 7)',
                     'review': 'fix-20261023/n6/REVIEW.md', 'triage': 'fix-20261023/n6/TRIAGE.json'})
    (N6 / 'EDITS-n6.json').write_text(json.dumps(recs, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    return work, recs


def context(lines, s):
    k = next(i for i, l in enumerate(lines) if s in l)
    return (lines[k - 1] if k else ''), lines[k], (lines[k + 1] if k + 1 < len(lines) else '')


PROMPT = '''You check {n} rewritten passages in Joel's long article on nibbāna (Buddhist enlightenment), written for a general Substack audience, in his casual first-person voice with jokes and emoji. Each NOW is a detector-passing rewrite of only the sentence(s) marked WAS in its paragraph; WAS is his text, the meaning to keep.

Work quickly: this is a short reading task, so don't deliberate at length.

For each item, say in a few words each:
1. MEANING: does NOW keep every point, claim, condition and image of WAS, with the same strength (nothing made more or less certain, nothing turned into a different claim, no cause turned into a coincidence)? KEPT, or what CHANGED or was LOST, and anything ADDED that a reader would take as a claim.
2. SENSE: would a reader understand the paragraph with NOW in it, between BEFORE and AFTER? OK, or the words that stop them and why.
End each item with one line, `VERDICT: OK` or `VERDICT: CHANGED`. Judge meaning and sense only, not style or grammar (the casual grammar is on purpose), and suggest the smallest possible rewrite only for a problem you report.

Write your report with a single Write call to `{report}`, one "## Item N" part per item, then reply with only the verdicts, one line per item. Don't read any other file, don't run commands, and don't use the web.

{items}'''


def prompt(text_before):
    notes = {'n6-aware': 'a dense paragraph on two kinds of awareness in the suttas',
             'n6-mn75': 'a note under a self-check question for stream entry ("Are you more joyful and enjoyable to be '
                        'around without becoming a people-pleaser, as in MN 89?")',
             'n6-question': 'the next self-check question in the same list',
             'n6-lucid': 'the first paragraph of the section "Why nibbāna is “awakening”"; the section before it ends on '
                         'stream entry\'s "release date" (at most seven more lives)'}
    lines = [l for l in text_before.split('\n') if l.strip()]
    done = text_before
    for s in SPLICES.values():
        done = done.replace(s['old'], new_text(s))
    dlines = [l for l in done.split('\n') if l.strip()]
    items = []
    for n, (key, s) in enumerate(SPLICES.items(), 1):
        _b, para, _a = context(lines, s['old'])
        before, now_para, after = context(dlines, new_text(s))
        items.append('## Item %d (%s)\n\nBEFORE:\n%s\n\nPARAGRAPH WITH WAS:\n%s\n\nWAS:\n%s\n\nNOW:\n%s\n\n'
                     'PARAGRAPH WITH NOW:\n%s\n\nAFTER:\n%s\n' % (n, notes[key], before, para, s['old'], new_text(s),
                                                                 now_para, after))
    return PROMPT.format(n=len(SPLICES), report=(N6 / 'REVIEW.md').resolve(), items='\n'.join(items))


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('--prompt', action='store_true')
    a = ap.parse_args(argv)
    if a.prompt:
        sys.path.insert(0, str(ROOT / 'tools/humanization'))
        import substack_check_text as C
        text = (N6.parent / 'recheck6' / 'DRAFT-TEXT.txt').read_text(encoding='utf-8')
        (N6 / 'REVIEW-PROMPT.txt').write_text(prompt(text), encoding='utf-8')
        print('REVIEW-PROMPT.txt written')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
