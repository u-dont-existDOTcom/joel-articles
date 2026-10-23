"""Batch n5 (Nibbāna), part 2: Emulate's round 3 for recheck 5's red, spliced sentence by sentence (2026-10-23, Joel's
message of 20:35 UTC gave recheck 5's link).

The red (../recheck5/SCORE.md), all his published words:
- windows 78 to 80 (AI, Low / Medium / Low): "That creates a practical problem.", "In DN 3 and MN 56, the Buddha waits
  until a student’s mind is “ready, pliable, rid of hindrances, elated, and confident” before giving the teaching that
  opens the Dhamma-eye." (Medium, alone in its window) and "What happens when a stage map lets anyone skip to the
  answer?". The DN 3 sentence had read Human, High, in the first two rechecks and Human, Low, in the next two.
- window 15 (AI, Low): "They were disjoint, but not isolated: the flows ran into and through one another, connected
  everywhere without becoming one experience or one witnessed scene. Nothing observed them from behind. There was no
  cosmic knower celebrating its achievement." It read AI, Low, in the check of 2026-10-20 too, and Human, Low, in the
  four rechecks between.

Emulate ran on the whole paragraphs the red covers (E235, E244), three samples (bx, by, bz; BUNDLE3.json), the DN 3
stretch with his N4 12A already in ("That creates a practical problem." ends the paragraph before the heading). Only the
red sentences go back, each from the sample that keeps its meaning best; every change I made to Emulate's words is in
"mine" with its reason (docs/EMULATE-FALLBACK.md, section 4). Where no sample keeps a sentence's meaning, his words stay:
the room's "Nothing observed them from behind. There was no cosmic knower celebrating its achievement." (no sample keeps
the knower's "achievement", and one drops the knower), so only the long first sentence of the red is replaced there.

  python3 articles/nibbana/humanize/fix-20261023/n5/emulate_n5.py --prompt   writes REVIEW-PROMPT.txt for a fresh reader
  (install_n1.py calls apply() after his N4 answers, joel_2035.py)
"""
import argparse, html, json, pathlib, re, sys

N5 = pathlib.Path(__file__).resolve().parent
ROOT = N5.parents[4]


def sample(run, key):
    return (N5 / run / (key + '.out.txt')).read_text(encoding='utf-8').strip()


DN3_OLD = ('In DN 3 and MN 56, the Buddha waits until a student’s mind is “ready, pliable, rid of hindrances, elated, and '
           'confident” before giving the teaching that opens the Dhamma-eye.')
ROOM_OLD = ('They were disjoint, but not isolated: the flows ran into and through one another, connected everywhere without '
            'becoming one experience or one witnessed scene.')
# key: the paragraph's first words, the red text as it is in the working copy, the sample and the part used, my changes to
# Emulate's words with reasons, the windows, and the published text the meaning comes from
SPLICES = {
    'n5-practical': dict(
        first='The funny part is that the words may have survived', old='That creates a practical problem.',
        run='bz', key='NB-dn3', take=('That leads to a practical problem.', 'That leads to a practical problem.'), mine=[],
        windows='78 (Low) in recheck 5 (feed 54a79d39), alone; 86 (Low) in recheck 4 with the sentence before it',
        published='That creates a practical problem.'),
    'n5-dn3': dict(
        first='In DN 3 and MN 56', old=DN3_OLD,
        run='bz', key='NB-dn3', take=('In several sutta’s', 'confident.”'),
        mine=[('In several sutta’s, most notably DN 3 and MN 56 the Buddha', 'In DN 3 and MN 56, the Buddha',
               'the reader (REVIEW.md, item 2): "In several suttas, most notably" adds a claim; his sentence names the two '
               'suttas only'),
              ('the dhamma that', 'the Dhamma that', 'the article’s own spelling (E246)'),
              ('the dhamma eye', 'the Dhamma-eye', 'the article’s own spelling, as in the sentence it replaces (E246)')],
        windows='79 (Medium) in recheck 5, alone; Human, Low, in rechecks 3 and 4; Human, High, before',
        published=DN3_OLD),
    'n5-skip': dict(
        first='In DN 3 and MN 56', old='What happens when a stage map lets anyone skip to the answer?',
        run='bx', key='NB-dn3', take=('What happens when we lay out', 'skip ahead?'),
        mine=[('skip ahead?', 'skip ahead to the answer?',
               'the reader (REVIEW.md, item 3): "the answer", the teaching the Buddha holds back until the student is '
               'ready, is back; "skip ahead" alone read as jumping through the stages')],
        windows='80 (Low) in recheck 5, alone',
        published='What happens when a stage map lets anyone skip to the answer?'),
    'n5-room': dict(
        first='Awareness as one thing was gone.', old=ROOM_OLD,
        run='bz', key='NB-room', take=('Though disjoint', 'seen by a witness.'),
        mine=[('and everywhere they touched, they were connected', 'and they were connected everywhere',
               'the reader (REVIEW.md, item 4): "everywhere they touched" narrowed his "connected everywhere"')],
        windows='15 (Low) in recheck 5, with "Nothing observed them from behind. There was no cosmic knower celebrating its '
                'achievement.", which stay his; window 23 (Low) in the check of 2026-10-20; Human, Low, in rechecks 1 to 4',
        published=ROOM_OLD),
}


def new_text(s):
    out = sample(s['run'], s['key'])
    a, b = s['take']
    i = out.index(a)
    out = out[i:out.index(b, i) + len(b)]
    for x, y, _why in s['mine']:
        assert out.count(x) == 1, (x, out)
        out = out.replace(x, y)
    return out


def plain(fragment):
    return html.unescape(re.sub(r'<[^>]+>', '', fragment))


def para_bounds(work, first):
    hits = [(m.start(1), m.end(1)) for m in re.finditer(r'<p\b[^>]*>(.*?)</p>', work, re.S)
            if plain(m.group(1)).lstrip().startswith(first)]
    assert len(hits) == 1, ('one paragraph must start with', first, len(hits))
    return hits[0]


def replace_in_para(inner, old, new):
    """Replace OLD with NEW in a paragraph's inner HTML, keeping its links on the same words (the paragraph may hold only
    links as inline markup)."""
    tags = re.findall(r'<(\w+)', inner)
    assert set(tags) <= {'a'}, ('only links can be kept', set(tags))
    links = [(plain(m.group(2)), m.group(1), m.group(0)) for m in re.finditer(r'(<a [^>]*>)(.*?)</a>', inner, re.S)]
    text = plain(inner)
    assert text.count(old) == 1, old[:60]
    text = text.replace(old, new)
    body = html.escape(text, quote=False)
    for words, open_tag, _whole in links:
        w = html.escape(words, quote=False)
        assert body.count(w) == 1, ('a link’s words must be in the new text once', words)
        body = body.replace(w, open_tag + w + '</a>')
    return body


def apply(work):
    recs = []
    for key, s in SPLICES.items():
        a, b = para_bounds(work, s['first'])
        new = new_text(s)
        work = work[:a] + replace_in_para(work[a:b], s['old'], new) + work[b:]
        recs.append({'key': key, 'old': s['old'], 'new': new, 'windows': s['windows'],
                     'source': 'Emulate sample %s (%s)' % (s['run'], s['key']),
                     'mine': [{'replace': x, 'with': y, 'why': w} for x, y, w in s['mine']],
                     'published': s['published'], 'check': None, 'try': None,
                     'result': 'read in place in the next recheck (recheck 6)',
                     'review': 'fix-20261023/n5/REVIEW.md', 'triage': 'fix-20261023/n5/TRIAGE.json'})
    (N5 / 'EDITS-n5.json').write_text(json.dumps(recs, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    return work, recs


def context(lines, s):
    k = next(i for i, l in enumerate(lines) if s in l)
    return (lines[k - 1] if k else ''), lines[k], (lines[k + 1] if k + 1 < len(lines) else '')


PROMPT = '''You check {n} rewritten passages in Joel's long article on nibbāna (Buddhist enlightenment), written for a general Substack audience, in his casual first-person voice with jokes and emoji. Each NOW is a detector-passing rewrite of only the sentence(s) marked WAS in its paragraph; PUBLISHED is what he published, the meaning to keep.

For each item, say in a few words each:
1. MEANING: does NOW keep every point, claim, condition and image of PUBLISHED, with the same strength (nothing made more or less certain, nothing turned into a different claim, no cause turned into a coincidence)? KEPT, or what CHANGED or was LOST, and anything ADDED that a reader would take as a claim.
2. SENSE: would a reader understand the paragraph with NOW in it, between BEFORE and AFTER? OK, or the words that stop them and why.
End each item with one line, `VERDICT: OK` or `VERDICT: CHANGED`. Judge meaning and sense only, not style or grammar (the casual grammar is on purpose), and suggest the smallest possible rewrite only for a problem you report.

Write your report with a single Write call to `{report}`, one "## Item N" part per item, then reply with only the verdicts, one line per item. Don't read any other file, don't run commands, and don't use the web.

{items}'''


def prompt(text_before):
    """TEXT_BEFORE: the checked text of the working copy with his N4 answers in and these splices not yet in."""
    notes = {'n5-practical': 'the last sentence of a paragraph that ends a section; the next section (after a heading) '
                             'opens with the DN 3 paragraph, item 2',
             'n5-dn3': 'the first sentence of the section "A Map Can Save Years – and Create Counterfeits"',
             'n5-skip': 'the question that ends the same paragraph; the paragraph after it answers it',
             'n5-room': 'his account of the central experience of the article (the "room event", the first full '
                        'nibbāna); the two sentences after the rewritten one stay his'}
    lines = [l for l in text_before.split('\n') if l.strip()]
    done = text_before
    for s in SPLICES.values():
        done = done.replace(s['old'], new_text(s))
    dlines = [l for l in done.split('\n') if l.strip()]
    items = []
    for n, (key, s) in enumerate(SPLICES.items(), 1):
        _b, para, _a = context(lines, s['old'])
        before, now_para, after = context(dlines, new_text(s))
        items.append('## Item %d (%s)\n\nBEFORE:\n%s\n\nPARAGRAPH WITH WAS:\n%s\n\nWAS:\n%s\n\nPUBLISHED:\n%s\n\nNOW:\n%s\n\n'
                     'PARAGRAPH WITH NOW:\n%s\n\nAFTER:\n%s\n' % (n, notes[key], before, para, s['old'], s['published'],
                                                                 new_text(s), now_para, after))
    return PROMPT.format(n=len(SPLICES), report=(N5 / 'REVIEW.md').resolve(), items='\n'.join(items))


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('--prompt', action='store_true')
    a = ap.parse_args(argv)
    if a.prompt:
        sys.path.insert(0, str(ROOT / 'tools/humanization'))
        import substack_check_text as C
        # the text before these splices: the working copy as install_n1.py leaves it, with this batch taken back out
        work = (ROOT / 'articles/nibbana/humanize/HUMANIZED-SO-FAR.html').read_text(encoding='utf-8')
        text = C.checked_text(work)
        for s in SPLICES.values():
            text = text.replace(new_text(s), s['old']) if s['old'] not in text else text
        (N5 / 'REVIEW-PROMPT.txt').write_text(prompt(text), encoding='utf-8')
        print('REVIEW-PROMPT.txt written')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
