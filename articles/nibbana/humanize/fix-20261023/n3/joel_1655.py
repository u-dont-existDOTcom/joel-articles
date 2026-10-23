"""Batch n3: Joel's answers to the clarity list, his message of 2026-10-23 16:55 UTC (../joel-20261023-1655-message.txt),
put into the working copy by install_n1.py (which calls apply() last, after the 14:14 fix).

What goes in, each replacing its stretch of the working copy (found by its exact text; the clarity list's numbers):
- his own words for 1, 3, 4, 6, 7, 8, 10, 14, 15, 16, 17, 20, 22, 24, and for the second recheck's one red paragraph,
  the photon one (his "there was 1 a span" fix; it is also item 9: "fixed it at the top there");
- the readers' plain versions he passed ("ok passes", "possibly human") for 2, 5, 11, 12, 13, 18, 19, 21, 23, 25 to 29,
  as the clarity list gave them (CLARITY.md), with two changes, each listed in CHANGES below with its reason;
- the four small snags ("fix the snags also"): short glosses, mine;
- saṃsāra defined where it first comes, not where it comes second (his 6: "it should have been defined where it first
  came in the article, but instead it's defined int he second place it came, so we need to fix that ... fix samsara in
  the other parts as i mentioned"): mine.

Links, italics and bold go back on the same words; where the words changed, MARKS says where each goes or why it goes.
His text is his as he typed it (his straight quotes kept, as with his earlier fixes); obvious typos fixed are in TYPOS.
"""
import html, json, pathlib, re

N3 = pathlib.Path(__file__).resolve().parent
F = N3.parent
MSG = F / 'joel-20261023-1655-message.txt'
CLARITY = F / 'clarity' / 'CLARITY.md'

TYPOS = {'joel-3': [('Advaita vedanta', 'Advaita Vedanta')]}

# number -> the stretch of the working copy it replaces, as (the paragraph's first words, the stretch's first words,
# the stretch's last words); None for the stretch = the clarity list's quote. A wider stretch is where his text (or the
# plain version) starts or ends beyond the quote.
WIDER = {
    3: ('Even after the little king or queen fantasy disappears', 'Even after the little king', 'into a self & world.'),
    6: ('This also explains the famous quote', 'Exactly. It’s saṃsāra', 'that establishment fully unweaves.'),
    18: ('I now call this body-uncontained nibbāna', 'I now call this body-uncontained', 'the fingers nibbāna event.'),
    27: ('Nibbāna is genuinely needed as the trigger', 'But without the ammunition', 'without immutably overwriting the old view.'),
}
PHOTON_OLD = ('The suttas repeatedly call nibbāna unestablished or unsupported. Ud 8.1 gives it no coming, going, standing, '
              'passing, or arising. SN 12.38 and SN 22.53 tie unestablished consciousness to ending renewed existence. '
              'SN 12.64, of all images, uses a beam of light with nowhere to land. Quantum physics likewise says a photon’s '
              'state isn’t established as one definite outcome until measured. Saṃsāra is the unestablished becoming '
              'established as a definite relational world.')

# the two changes to plain versions he passed
CHANGES = {
    2: [('the illusory cycle of birth, death, joy, and suffering called saṃsāra', 'the illusory cycle of saṃsāra',
         'saṃsāra is now defined where it first comes (his 6), and the rebirth paragraph four paragraphs before this one '
         'calls it the beginningless cycle again, so a third gloss here would repeat it')],
    23: [('Now I think there’s nothing wrong', 'Now I realize there’s nothing wrong',
          'his "Now I realize" put back: the plain version had softened it to "Now I think", which changes his claim '
          '(AGENTS.md: never silently soften the owner\'s argument)')],
}

# where a mark's words changed: number -> {the old mark's words: (the new words, a longer unique stretch of the new text
# that holds them, or None) or None to drop the mark, with the reason in MARK_NOTES}
MARKS = {
    3: {'sat chit ananda': None},
    4: {'saṃsāric': None},
    8: {'saṅkhata': ('saṅkhata', 'saṅkhata things arise')},
    13: {'State-dependent learning ': ('state-dependent learning', None)},
    21: {'not nibbāna': None},
    24: {'ignorance is not knowing that the euphoria of merging isn’t happiness compared with the bliss and peace of release':
         ('ignorance is not knowing that the ecstatic euphoria you get from merging multiple experiences into one doesn\'t '
          'count as real happiness when compared with the bliss and peace of release', None)},
    28: {'one fruition event is what establishes stream entry.':
         ('a single event, the nibbāna fruition, is what establishes stream entry', None)},
}
MARK_NOTES = {
    3: 'the italics on "sat chit ananda" go: his new paragraph no longer has those words',
    4: 'the italics on "saṃsāric" go: he put the word in quotes, which marks it the same way',
    21: 'the italics on "not nibbāna" go: the plain version says "it isn’t nibbāna (nibbāna means unbinding)"',
}

# mine: the four snags and saṃsāra's definition, each (the paragraph's first words, old, new, why)
MINE = [
    ('snag-cosmic-witness', 'It took me many years to finally learn',
     'before dissolving the cosmic witness.',
     'before dissolving the cosmic witness (that one universal awareness behind everything).',
     'the snag: "dissolving the cosmic witness" was never explained; the gloss points back to the paragraph where he '
     'tells of "one universal, happy awareness" (the modern seeker marketplace)'),
    ('snag-vinaya', 'Later I found that some of the uselessness',
     'tells anyone not fully ordained about',
     'tells anyone who isn’t fully ordained (a layperson or a novice, say) about',
     'the snag: "not fully ordained" was never explained'),
    ('snag-vinaya-fruit', 'Later I found that some of the uselessness',
     'or a path or fruit of awakening.',
     'or a path or fruit of awakening (a stage of enlightenment).',
     'the snag: "a path or fruit of awakening" was never explained'),
    ('snag-soh', 'I owe Soh a great deal',
     'he says sensory unification isn’t required for functioning',
     'he says sensory unification (that pulling-together of the senses) isn’t required for functioning',
     'the snag: "sensory unification" read as a different thing from the "unification" defined in the paragraph just '
     'before ("whatever pulls everything together so that a person can talk, cross a road ..."); the gloss ties it '
     'back, which also shows why his claim makes no sense to Joel'),
    ('snag-batgap', 'Most seekers, now as before the Buddha',
     'BatGap</a> or',
     'BatGap</a> (Buddha at the Gas Pump) or',
     'the snag: the short form "BatGap" was never spelled out (the opening names "Buddha at the Gas Pump")'),
    ('samsara-first', 'The finger episode was a small flashback',
     'misapprehended as saṃsāra.',
     'misapprehended as saṃsāra, the beginningless cycle of birth, death, joy &amp; suffering.',
     'his 6: saṃsāra defined where it first comes; the words are his own definition from the rebirth paragraph'),
    ('samsara-second', 'I didn’t believe in rebirth in my last lifetime',
     'life is a beginningless cycle of birth, death, joy &amp; suffering, called saṃsāra.',
     'life is that beginningless cycle of saṃsāra.',
     'his 6: the rebirth paragraph had the definition, at saṃsāra\'s second mention; it now refers back to it'),
]


def message_parts():
    """His words by number from the message file (and 'photon' for his fix of the red paragraph)."""
    msg = MSG.read_text(encoding='utf-8')
    out = {}
    a = msg.index('His fix of it: "') + len('His fix of it: "')
    out['photon'] = msg[a:msg.index('"\n', a)]
    for m in re.finditer(r'\n(\d+): (.*?)(?=\n\d+: |\nlearn some pangram lessons)', msg, re.S):
        n, body = int(m.group(1)), m.group(2).strip()
        if '"' in body and n not in (6,):
            out[n] = body[body.index('"') + 1:body.rindex('"')]
        elif n == 6:
            out[n] = body.split('change it to "', 1)[1].split('" which passes', 1)[0]
        else:
            out[n] = None  # an answer with no text of his ("ok passes", "fixed it at the top there")
    return out


def clarity_items():
    md = CLARITY.read_text(encoding='utf-8')
    secs = re.split(r'\n### (\d+)\. ', md)
    out = {}
    for k in range(1, len(secs), 2):
        n, body = int(secs[k]), secs[k + 1]
        out[n] = {'heading': body.split('\n', 1)[0].strip(),
                  'quote': re.search(r'\n> (.*)\n', body).group(1),
                  'plain': re.search(r'\*\*Plainer \((?:.*?)\):\*\* (.*)\n', body).group(1)}
    return out


def tokens(inner):
    """The HTML of a paragraph's inside as tokens: ('c', html, char), ('o', html, tag), ('e', html, tag), ('v', html, tag)."""
    out, i = [], 0
    while i < len(inner):
        if inner[i] == '<':
            j = inner.index('>', i) + 1
            t = inner[i:j]
            name = re.match(r'</?\s*([a-zA-Z0-9]+)', t).group(1).lower()
            kind = 'e' if t.startswith('</') else ('v' if name in ('br', 'img', 'hr') or t.endswith('/>') else 'o')
            out.append((kind, t, name))
            i = j
        elif inner[i] == '&':
            j = inner.index(';', i) + 1
            out.append(('c', inner[i:j], html.unescape(inner[i:j])))
            i = j
        else:
            out.append(('c', inner[i], inner[i]))
            i += 1
    return out


def pairs(toks):
    st, out = [], []
    for k, t in enumerate(toks):
        if t[0] == 'o':
            st.append(k)
        elif t[0] == 'e':
            a = st.pop()
            assert toks[a][2] == t[2], (toks[a], t)
            out.append((a, k))
    assert not st
    return out


def plain_of(toks):
    return ''.join(t[2] for t in toks if t[0] == 'c')


def replace_span(inner, old_plain, new_plain, marks=None):
    """Replace OLD_PLAIN (the plain text of a stretch of INNER, a paragraph's inside HTML) with NEW_PLAIN, putting each
    link, italic or bold of the stretch back on the same words in the new text (MARKS: old words -> (new words, context)
    or None to drop). Returns (the new inner HTML, the marks kept, the marks dropped)."""
    marks = marks or {}
    toks = tokens(inner)
    cidx = [k for k, t in enumerate(toks) if t[0] == 'c']
    text = ''.join(toks[k][2] for k in cidx)
    assert text.count(old_plain) == 1, ('the stretch must occur once in its paragraph', old_plain[:80])
    ps = text.index(old_plain)
    pe = ps + len(old_plain)
    ts, te = cidx[ps], cidx[pe - 1] + 1
    prs = pairs(toks)
    changed = True
    while changed:
        changed = False
        for a, b in prs:
            inside_a, inside_b = ts <= a < te, ts <= b < te
            if (inside_a or inside_b) and not (ts <= a and b < te):
                ts, te = min(ts, a), max(te, b + 1)
                changed = True
    # the plain text the widened range covers, so the new text keeps any words the widening took in
    span_plain = plain_of(toks[ts:te])
    pre_extra = span_plain[:span_plain.index(old_plain)]
    post_extra = span_plain[span_plain.index(old_plain) + len(old_plain):]
    new_full = pre_extra + new_plain + post_extra
    kept, dropped, spans = [], [], []
    top = [(a, b) for a, b in prs if ts <= a and b < te and not any(ts <= a2 < a and b < b2 < te for a2, b2 in prs)]
    for a, b in sorted(top):
        words = plain_of(toks[a:b + 1])
        inner_html = ''.join(t[1] for t in toks[a + 1:b])
        open_t, close_t = toks[a][1], toks[b][1]
        target, ctx = words, None
        if words in marks:
            if marks[words] is None:
                dropped.append(words)
                continue
            target, ctx = marks[words]
            if target != words:
                inner_html = html.escape(target, quote=False)
        if ctx:
            assert new_full.count(ctx) == 1, ('context must occur once', ctx)
            s = new_full.index(ctx) + ctx.index(target)
        else:
            assert new_full.count(target) == 1, ('a mark\'s words must occur once in the new text', words, target)
            s = new_full.index(target)
        spans.append((s, s + len(target), open_t + inner_html + close_t))
        kept.append(target)
    spans.sort()
    for (s1, e1, _x), (s2, _e2, _y) in zip(spans, spans[1:]):
        assert e1 <= s2, 'two marks overlap in the new text'
    body, at = [], 0
    for s, e, h in spans:
        body.append(html.escape(new_full[at:s], quote=False))
        body.append(h)
        at = e
    body.append(html.escape(new_full[at:], quote=False))
    body = ''.join(body)
    # tags that were inside the range but not in a top pair (a <br>, say) would be lost: there are none here
    assert all(t[0] in ('c', 'o', 'e') for t in toks[ts:te]), 'a void tag in the stretch'
    out = ''.join(t[1] for t in toks[:ts]) + body + ''.join(t[1] for t in toks[te:])
    return out, kept, dropped


def para_bounds(work, first):
    """The inside of the one paragraph (p or li > p) whose plain text starts with FIRST."""
    hits = []
    for m in re.finditer(r'<p\b[^>]*>(.*?)</p>', work, re.S):
        if html.unescape(re.sub(r'<[^>]+>', '', m.group(1))).lstrip().startswith(first):
            hits.append((m.start(1), m.end(1)))
    assert len(hits) == 1, ('one paragraph must start with', first, len(hits))
    return hits[0]


def apply(work):
    joel = message_parts()
    items = clarity_items()
    recs = []

    def do(key, first, old_plain, new_plain, marks, source, shape, extra=None):
        nonlocal work
        a, b = para_bounds(work, first)
        inner = work[a:b]
        new_inner, kept, dropped = replace_span(inner, old_plain, new_plain, marks)
        work = work[:a] + new_inner + work[b:]
        r = {'key': key, 'old': old_plain, 'new': new_plain, 'marks_kept': kept, 'marks_dropped': dropped,
             'source': source, 'shape': shape, 'check': None, 'try': None,
             'result': 'read in place in the next recheck (recheck 4)'}
        r.update(extra or {})
        recs.append(r)

    # his fix of the second... third recheck's red paragraph (feed f2b77491, windows 92 and 93)
    do('joel-photon', 'The suttas repeatedly call nibbāna unestablished', PHOTON_OLD, joel['photon'], {},
       'fix-20261023/joel-20261023-1655-message.txt', 'his own words, the third recheck\'s red paragraph',
       {'windows': '92 (Low) and 93 (Low) in the third recheck (feed f2b77491)',
        'his_check': 'his message: "there was 1 a span" and his fix of it'})
    for n in range(1, 30):
        if n == 9:
            continue  # his 9: "fixed it at the top there", the photon paragraph above
        it = items[n]
        if n in WIDER:
            first, s0, s1 = WIDER[n]
            a, b = para_bounds(work, first)
            p = html.unescape(re.sub(r'<[^>]+>', '', work[a:b]))
            old = p[p.index(s0):p.index(s1) + len(s1)]
        else:
            old = it['quote']
            # the paragraph is the one that holds the quote
            first = None
            for m in re.finditer(r'<p\b[^>]*>(.*?)</p>', work, re.S):
                pt = html.unescape(re.sub(r'<[^>]+>', '', m.group(1)))
                if old in pt:
                    assert first is None, ('the quote is in two paragraphs', n)
                    first = pt.lstrip()[:40]
            assert first, ('the quote is in no paragraph', n, old[:60])
        if joel.get(n):
            new = joel[n]
            typos = []
            for x, y in TYPOS.get('joel-%d' % n, []):
                assert x in new
                new = new.replace(x, y)
                typos.append([x, y])
            do('joel-%d' % n, first, old, new, MARKS.get(n), 'fix-20261023/joel-20261023-1655-message.txt',
               'his own words (clarity item %d, %s)' % (n, it['heading']),
               {'typos_fixed': typos, 'his_check': 'his message: passes', 'mark_note': MARK_NOTES.get(n)})
        else:
            new = it['plain']
            notes = []
            for x, y, why in CHANGES.get(n, []):
                assert new.count(x) == 1, (n, x)
                new = new.replace(x, y)
                notes.append({'replace': x, 'with': y, 'why': why})
            do('plain-%d' % n, first, old, new, MARKS.get(n), 'fix-20261023/clarity/CLARITY.md',
               'the reader\'s plain version he passed (clarity item %d, %s)' % (n, it['heading']),
               {'changes': notes, 'his_check': 'his message: ' + {11: 'passes as possibly human', 12: 'passes as possibly human',
                                                                     13: 'possibly human', 23: 'good passes'}.get(n, 'passes'),
                'mark_note': MARK_NOTES.get(n)})
    for key, first, old_html, new_html, why in MINE:
        a, b = para_bounds(work, first)
        inner = work[a:b]
        assert inner.count(old_html) == 1, (key, old_html)
        work = work[:a] + inner.replace(old_html, new_html) + work[b:]
        recs.append({'key': key, 'old': old_html, 'new': new_html, 'source': 'mine', 'shape': why, 'check': None,
                     'try': None, 'result': 'read in place in the next recheck (recheck 4)'})
    (N3 / 'EDITS-n3.json').write_text(json.dumps(recs, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    return work, recs
