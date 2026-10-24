"""Batch n8 (Nibbāna): Joel's GPT edit of 2026-10-24, put into the working copy (his message of 19:52 UTC: "i had GPT
apply all the nibbana cuts for you to save your credits, and it also fixed some other ai tells it saw, i checked the output
and it's 100% human on pangram. so save the result").

GPT worked from the eighth recheck's draft (its page text, which read 100% Human, feed 355a29d0) and gave back two texts
(../gpt/): Nibbana_After_Approved_Cuts.txt, his N6 picks applied (13 cuts) with edits of its own in other paragraphs, and
Nibbana_Updated_Draft.txt, then ten style edits (its comparison page, Nibbana_Local_Comparison.html, lists those ten).
../gpt/diff_gpt.py lines the final text up with ours: 40 paragraphs changed, and no heading, caption, picture or other
paragraph (the verse in the Bāhiya section only has its line breaks in GPT's copy). ../gpt/REVIEW.md has my read of each.

Each changed paragraph gets GPT's final text, change by change: the paragraph is diffed word by word (punctuation
apart) against GPT's, and
each changed stretch is replaced in place, so a link or italics outside it stays where it was, and one inside it goes on
the same words, or is dropped and recorded when those words are gone.

  (install_n1.py calls apply() after batch n7)
"""
import difflib, html, json, pathlib, re, sys

N8 = pathlib.Path(__file__).resolve().parent
FIX = N8.parent
sys.path.insert(0, str(FIX.parent / 'fix-20261023' / 'n6'))
import emulate_n6 as E6  # noqa: E402  (para_bounds and the inline-markup class)

MOVED = []  # tags whose ends moved, recorded with their paragraph
STRAIGHT = str.maketrans({'“': '"', '”': '"', '‘': "'", '’': "'"})


def smart(s):
    sys.path.insert(0, str(FIX.parents[3] / 'tools' / 'humanization'))
    import substack_check_text as C
    return C.smart(s)


def changes():
    d = json.loads((FIX / 'gpt' / 'DIFF.json').read_text(encoding='utf-8'))['Nibbana_Updated_Draft.txt']['changed']
    squash = lambda s: re.sub(r'\s+', '', s)
    out = []
    for c in d:
        if c['gpt'] is None or squash(c['ours']) == squash(c['gpt']):
            continue
        if c['ours'].startswith('In the seen, there is only the seen,'):
            continue  # the verse: only its line breaks differ in GPT's copy
        out.append((c['ours'], c['gpt']))
    return out


def tokens(s):
    return [(m.group(0), m.start()) for m in re.finditer(r'\w+|[^\w\s]|\s+', s)]  # words, marks, spaces apart


def replace_span(p, i, j, new):
    """E6._Inline.replace for the stretch p.text[i:j], by position."""
    d = len(new) - (j - i)
    dropped, kept = [], []
    for s in p.spans:
        a, b, o, c = s
        if b <= i:
            kept.append(s)
        elif a >= j:
            kept.append([a + d, b + d, o, c])
        elif a >= i and b <= j:
            words = p.text[a:b]
            k = new.find(words)
            if k >= 0 and new.count(words) == 1:
                kept.append([i + k, i + k + len(words), o, c])
            else:
                dropped.append(o + words + c)
        elif a <= i and b >= j:  # the stretch is inside the tag: the tag grows or shrinks with it
            kept.append([a, b + d, o, c])
        elif a > i:  # the tag starts inside the stretch and ends after it: it takes the stretch's new words too
            kept.append([i, b + d, o, c])
            MOVED.append('%s now starts at "%s"' % (o, new[:40]))
        else:  # the tag starts before the stretch and ends inside it: it takes the stretch's new words too
            kept.append([a, i + len(new), o, c])
            MOVED.append('%s now ends at "%s"' % (o, new[-40:]))
    p.text = p.text[:i] + new + p.text[j:]
    p.spans = kept
    return dropped


def para_bounds(work, first):
    """The inner HTML bounds of the one paragraph whose text, quotes curled, starts with FIRST."""
    plain = lambda inner: smart(html.unescape(re.sub(r'<[^>]+>', '', inner))).lstrip()
    hits = [(m.start(1), m.end(1)) for m in re.finditer(r'<p\b[^>]*>(.*?)</p>', work, re.S)
            if plain(m.group(1)).startswith(first)]
    assert len(hits) == 1, ('one paragraph must start with', first, len(hits))
    return hits[0]


def apply(work):
    recs = []
    for ours, gpt in changes():
        a, b = para_bounds(work, ours[:40])
        inner = work[a:b]
        tail = re.search(r'(?:<br\b[^>]*>\s*)+$', inner)  # trailing breaks (two paragraphs end on them) stay as they are
        suffix = tail.group(0) if tail else ''
        p = E6._Inline(inner[:len(inner) - len(suffix)])
        cur = smart(p.text)
        first = ours[:40]
        assert re.sub(r'\s+', ' ', cur).strip() == re.sub(r'\s+', ' ', ours).strip(), ('not the recheck text', first)
        ta, tb = tokens(cur), tokens(gpt)
        dropped = []
        ops = difflib.SequenceMatcher(None, [t for t, _ in ta], [t for t, _ in tb], autojunk=False).get_opcodes()
        for op, i1, i2, j1, j2 in reversed(ops):
            if op == 'equal':
                continue
            i = ta[i1][1] if i1 < len(ta) else len(cur)
            j = ta[i2 - 1][1] + len(ta[i2 - 1][0]) if i2 > i1 else i
            new = ''.join(t for t, _ in tb[j1:j2])
            dropped += replace_span(p, i, j, new)
            cur = cur[:i] + new + cur[j:]
        assert re.sub(r'\s+', ' ', smart(p.text)).strip() == re.sub(r'\s+', ' ', gpt).strip(), ('not GPT\'s text', first)
        out = p.html()
        if out.startswith('When <em>nibbāna is the experiential fruition'):
            # his italics were on the whole condition ("when it's the experiential fruition of practicing the Eightfold
            # Path"); GPT's sentence starts with that condition, so they start with it again
            out = out.replace('When <em>nibbāna is', '<em>When nibbāna is', 1)
            MOVED.append('<em> starts at "When" again, as his italics covered the whole condition')
        work = work[:a] + out + suffix + work[b:]
        recs.append({'old': ours, 'new': gpt, 'source': 'Joel\'s GPT edit of 2026-10-24 (../gpt/Nibbana_Updated_Draft.txt)',
                     'markup_dropped': dropped, 'markup_moved': MOVED[:]})
        MOVED.clear()
    (N8 / 'EDITS-n8.json').write_text(json.dumps(recs, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    return work, recs
