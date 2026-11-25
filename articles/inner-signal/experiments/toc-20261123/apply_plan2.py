#!/usr/bin/env python3
"""The second edit of the Self-Hypnosis post on 2026-11-25: his marking-page answers (answers/JOEL-20261125-1600.json)
and his two names for question 4, as one change in the editor.

  python3 apply_plan2.py

Reads LIVE-BODY-20261125-after.html (the live post after the first edit; its sha256 is the live body's, checked from the
laptop at 16:20 UTC) and his answers file. Every paragraph he approved goes in exactly as the card showed it (the
answers file carries each one before and after); what his comments ask for is in COMMENTS below, with his words.
Writes PLAN2.json (for people), EDITOR-OPS2.json (for apply_in_editor.js), AFTER2.md (the guide as it would read) and
pangram/t2/<key>.txt for the sections whose text hasn't been checked as it goes in.

No block moves. A new paragraph follows the block it belongs after; his new section goes above the divider before
"H: Demons, Jinn & Presences". A link in a sentence brought from another guide comes with it (his comment on C12:
"always carry the links").
"""
import hashlib, json, os, re, sys
from bs4 import BeautifulSoup, Tag

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import apply_plan as ap1
sl, lines_of, kind, fnv = ap1.sl, ap1.lines_of, ap1.kind, ap1.fnv

BASE_FILE = 'LIVE-BODY-20261125-after.html'
BASE_SHA = '3f76d79ed8cfab0e2564d44b18348caf1d5e87c517a9d60c593016533f2bbfee'
ANSWERS = 'answers/JOEL-20261125-1600.json'

# question 4, his words of 2026-11-25 16:14 UTC: "ok you can use Become a Trustworthy Adult and Working With Your Inner Child"
RENAMES = {'The Inner Adult’s Three Jobs': 'Become a Trustworthy Adult',
           'Inner Child Practices': 'Working With Your Inner Child'}
# cards he approved as shown: the paragraph goes from "before" to "my_version" in his answers file
APPROVED = ['C05', 'C17', 'C10', 'C09', 'C04', 'C12', 'C13', 'Q7b', 'M05', 'M06', 'C16', 'C02']
# what his comments ask for: (id, heading of its section, text found once there, what it becomes, his words)
COMMENTS = [
    ('C06', 'Start From the Whole', 'When something specific comes up, that’s the time to sort out what it is.',
     'Once you feel comfortable in your wholeness, then you can investigate parts with a gentle curiosity.',
     'the first sentence here should say, "Once you feel comfortable in your wholeness, then you can investigate parts '
     'with a gentle curiosity. "'),
    ('C03', 'Love First, Trust Later', 'Even that takes some warmth, and if you don\'t have any yet',
     'That takes warmth, and if you don\'t have any yet',
     '"in line": the inner child guide has "That takes warmth, and if there isn’t any yet, borrow some.", where it is '
     'their trust that takes warmth'),
    ('C18', 'Reparenting Therapy',
     'The sequence for doing this with borrowed adulthood and the arrangement of 3 functions of adulthood, etc, is not '
     'from these authors, however.',
     'The sequence for doing this reparenting therapy is not from these authors, however.',
     'i\'d say "The sequence for doing this reparenting therapy is not from these authors, however." and link '
     'reparenting therapy to innerchild.u-dont-exist.com'),
    ('Q4-mention', 'Inner Child Love', 'in Inner Child Practices)', 'in Working With Your Inner Child)',
     'the one place the guide names that group in a sentence takes its new name'),
]
# links: (id, heading of its section, the words, where they go, why)
LINKS = [
    ('C12', 'Don\'t Rush the Repair', 'warmlines', 'https://www.warmline.org/',
     'his comment on C12: "i had warmlines linked in the inner child guide tho make sure it\'s still linked right? '
     'always carry the links"; the link is the inner child guide\'s, in "Dip Your Toes In First"'),
    ('M06', 'Calm the Body Directly', 'Rolfing', 'https://www.youtube.com/watch?v=mIvVfqTIQgA',
     'the somatic guide links "Rolfing" in this sentence; carried with it (the same rule)'),
    ('C18', 'Reparenting Therapy', 'reparenting therapy', 'http://innerchild.u-dont-exist.com/',
     'his comment on C18; the address as the sentence already had it, on "the arrangement of 3 functions of adulthood"'),
    ('Q4-mention', 'Inner Child Love', 'Working With Your Inner Child', '#§working-with-your-inner-child',
     'the link that pointed at "Inner Child Practices" follows the heading'),
]
NEW_SECTION_ABOVE = 'H: Demons, Jinn & Presences'
NEW_SECTION_LEVEL = 2


def text_of(b):
    return b.get_text('')


def link_spans(b):
    """[start, end) of every link's words in the block's text."""
    out, pos = [], 0
    def walk(n, inside):
        nonlocal pos
        for c in n.children:
            if isinstance(c, Tag):
                a = pos
                walk(c, inside or c.name == 'a')
                if c.name == 'a':
                    out.append((a, pos))
            else:
                pos += len(str(c))
    walk(b, False)
    return out


def segments(md):
    """A paragraph of his with Markdown links, as [[text, href or None], ...]."""
    out, at = [], 0
    for m in re.finditer(r'\[([^\]]+)\]\((https?://[^)\s]+)\)', md):
        if m.start() > at:
            out.append([md[at:m.start()], None])
        out.append([m.group(1), m.group(2)])
        at = m.end()
    if at < len(md):
        out.append([md[at:], None])
    return out


def main():
    html = open(os.path.join(HERE, BASE_FILE), encoding='utf-8').read()
    assert hashlib.sha256(html.encode()).hexdigest() == BASE_SHA, 'the base is not the live body of 16:20 UTC'
    B = [b for b in BeautifulSoup(html, 'html.parser').children if isinstance(b, Tag)]
    K = [kind(b) for b in B]
    T = [text_of(b) for b in B]
    isH = lambda k: re.fullmatch(r'h[1-6]', K[k]) is not None
    heads = {T[k]: k for k in range(len(B)) if isH(k)}
    assert len(heads) == sum(1 for k in range(len(B)) if isH(k)), 'two headings with the same words'
    for old, new in RENAMES.items():
        assert old in heads and new not in heads, (old, new)
    def section_blocks(h):
        k = heads[h]
        out = []
        for j in range(k + 1, len(B)):
            if isH(j):
                break
            out.append(j)
        return out
    ans = {i['id']: i for i in json.load(open(os.path.join(HERE, ANSWERS), encoding='utf-8'))['items']}
    edits, new_after, plan_cards = [], {}, []

    def add_edit(eid, k, a, b, why, allow_link=False):
        """Replace a by b in block k: a is found once in the whole post, and (unless said) touches no link."""
        assert a != b and a, eid
        assert sum(t.count(a) for t in T) == 1 and T[k].count(a) == 1, (eid, 'not found once', a[:50])
        at = T[k].index(a)
        if not allow_link:
            assert not any(s < at + len(a) and e > at for s, e in link_spans(B[k])), (eid, 'the words to replace include a link')
        edits.append({'id': eid, 'block': k, 'from': a, 'to': b, 'why': why})

    def narrow(before, after):
        """The part that changes, with enough of the sentence before it to be found once in the post."""
        i = 0
        while i < min(len(before), len(after)) and before[i] == after[i]:
            i += 1
        j = 0
        while j < min(len(before), len(after)) - i and before[-1 - j] == after[-1 - j]:
            j += 1
        c = 24
        while True:
            a = before[max(0, i - c):len(before) - j]
            if (a and sum(t.count(a) for t in T) == 1) or i - c <= 0:
                break
            c += 12
        return a, before[max(0, i - c):i] + after[i:len(after) - j]

    for cid in APPROVED:
        it = ans[cid]
        assert it['status'] == 'approved', (cid, it['status'])
        assert not it['your_version'] or it['your_version'] == it['my_version'], (cid, 'he changed the text: read it')
        before, after = it['before'], it['my_version']
        ks = [k for k in range(len(B)) if T[k] == before]
        assert len(ks) == 1, (cid, 'paragraph found %d times' % len(ks))
        k = ks[0]
        paras = after.split('\n\n')
        if paras[0] != before:
            a, b = narrow(before, paras[0])
            add_edit(cid, k, a, b, 'card %s, approved %s' % (cid, it['updated'][:16]))
        if len(paras) > 1:
            assert len(paras) == 2, cid
            new_after.setdefault(k, []).append({'p': segments(paras[1]), 'id': cid})
        plan_cards.append({'id': cid, 'title': it['title'], 'where': it['where'], 'comment': it['comment'],
                           'before': before, 'after': after})
    for eid, sec_h, a, b, why in COMMENTS:
        ks = [k for k in section_blocks(sec_h) if a in T[k]]
        assert len(ks) == 1, (eid, sec_h, len(ks))
        # these two replace words that carry a link; the link they get instead is in LINKS
        add_edit(eid, ks[0], a, b, why, allow_link=(eid in ('Q4-mention', 'C18')))
    # two edits in one block must not overlap
    for k in {e['block'] for e in edits}:
        spans = sorted((T[k].index(e['from']), T[k].index(e['from']) + len(e['from'])) for e in edits if e['block'] == k)
        assert all(spans[n][1] <= spans[n + 1][0] for n in range(len(spans) - 1)), ('edits overlap in block', k)

    def after_text(k):
        t = T[k]
        for e in edits:
            if e['block'] == k:
                t = t.replace(e['from'], e['to'])
        return t
    # his new section, as he revised it on the page
    n = ans['N001']
    assert n['status'] == 'revise' and n['your_version'].startswith('## Past Life & Ancestral Trauma\n\n')
    parts = [re.sub(r' {2,}', ' ', p).strip() for p in n['your_version'].split('\n\n')]
    new_head = parts[0][3:]
    assert new_head not in heads
    new_section = [{'h': [NEW_SECTION_LEVEL, new_head]}] + [{'p': segments(p), 'id': 'N001'} for p in parts[1:]]
    above = heads[NEW_SECTION_ABOVE]
    insert_before = above - 1 if K[above - 1] == 'hr' else above       # above its divider, if it has one
    # the blocks in order
    doc, expected = [], []
    for k in range(len(B)):
        if k == insert_before:
            doc += new_section
            expected.append([NEW_SECTION_LEVEL, new_head])
        if isH(k):
            name = RENAMES.get(T[k], T[k])
            doc.append({'i': k, 'h': [int(K[k][1]), name]} if name != T[k] else {'i': k})
            expected.append([int(K[k][1]), name])
        else:
            doc.append({'i': k})
        doc += new_after.get(k, [])
    all_after = [after_text(x['i']) if 'i' in x else ''.join(t for t, _ in x['p']) for x in doc if 'h' not in x or 'i' in x]
    links = []
    for lid, sec_h, words, href, why in LINKS:
        ks = [k for k in section_blocks(sec_h) if words in after_text(k)]
        assert len(ks) == 1 and after_text(ks[0]).count(words) == 1, (lid, sec_h, words, len(ks))
        t = after_text(ks[0])
        a = t.index(words)
        b = a + len(words)
        while sum(x.count(t[a:b]) for x in all_after) != 1:
            assert a > 0 or b < len(t), (lid, 'no unique context')
            a, b = max(0, a - 12), min(len(t), b + 12)
        links.append({'id': lid, 'find': t[a:b], 'words': words, 'href': href, 'why': why})
    ops = {'post': ap1.POST, 'blocks': len(B),
           'fingerprint': [[k, fnv(T[k])] for k in range(len(B)) if K[k] in ('p', 'h1', 'h2', 'h3', 'h4', 'blockquote', 'ul', 'ol') and T[k].strip()],
           'edits': [{'id': e['id'], 'from': e['from'], 'to': e['to']} for e in edits],
           'links': [{'find': l['find'], 'words': l['words'], 'href': l['href']} for l in links],
           'order': doc, 'expected_headings': expected}
    json.dump(ops, open(os.path.join(HERE, 'EDITOR-OPS2.json'), 'w', encoding='utf-8'), ensure_ascii=False)
    plan = {'from': ANSWERS + ' and his message of 2026-11-25 16:14 UTC', 'base': BASE_FILE, 'base_sha256': BASE_SHA,
            'renames': RENAMES, 'cards': plan_cards,
            'edits': [{k: e[k] for k in ('id', 'from', 'to', 'why')} for e in edits],
            'new_paragraphs': [{'id': x['id'], 'after_block': k, 'after': T[k][-80:], 'text': ''.join(t for t, _ in x['p'])}
                               for k, xs in sorted(new_after.items()) for x in xs],
            'new_section': {'heading': new_head, 'level': NEW_SECTION_LEVEL, 'above': NEW_SECTION_ABOVE,
                            'paragraphs': [''.join(t for t, _ in x['p']) for x in new_section[1:]],
                            'links': [[t, h] for x in new_section[1:] for t, h in x['p'] if h]},
            'links': links, 'blocks': [len(B), len(doc)], 'headings': len(expected)}
    json.dump(plan, open(os.path.join(HERE, 'PLAN2.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    # the guide as it would read
    after, by_sec, cur = [], {}, None
    for x in doc:
        if 'h' in x:
            cur = x['h'][1]
            after.append('#' * x['h'][0] + ' ' + cur)
            continue
        if 'p' in x:
            ls = [''.join(t for t, _ in x['p'])]
        elif isH(x['i']):
            cur = T[x['i']]
            after.append('#' * int(K[x['i']][1]) + ' ' + re.sub(r'\s+', ' ', cur).strip())
            continue
        else:
            ls = lines_of(B[x['i']])
            for e in edits:
                if e['block'] == x['i']:
                    assert sum(l.count(e['from']) for l in ls) == 1, (e['id'], 'not found once in the block as read')
                    ls = [l.replace(e['from'], e['to']) for l in ls]
            ls = [l for l in ls if l.strip()]
        after += ls
        by_sec.setdefault(cur, []).extend(ls)
    open(os.path.join(HERE, 'AFTER2.md'), 'w', encoding='utf-8').write('\n\n'.join(after) + '\n')
    os.makedirs(os.path.join(HERE, 'pangram', 't2'), exist_ok=True)
    specs = {}
    for key, h in (('IS-t2-S017', 'Start From the Whole'), ('IS-t2-S021', 'Love First, Trust Later'),
                   ('IS-t2-S032', 'Don\'t Rush the Repair'), ('IS-t2-S162', 'Reparenting Therapy'), ('IS-t2-N001', new_head)):
        text = '\n\n'.join(by_sec[h]).strip()
        f = 'pangram/t2/%s.txt' % key
        open(os.path.join(HERE, f), 'w', encoding='utf-8').write(text + '\n')
        specs[key] = {'file': f, 'section': h, 'words': len(text.split()), 'sha256': hashlib.sha256(text.encode()).hexdigest()}
    json.dump(specs, open(os.path.join(HERE, 'pangram', 't2', 'SPECS.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('%d blocks -> %d; %d headings (%d renamed, 1 new); %d edits, %d new paragraphs, %d paragraphs in the new section, %d links'
          % (len(B), len(doc), len(expected), len(RENAMES), len(edits), sum(len(v) for v in new_after.values()),
             len(new_section) - 1, len(links) + len(plan['new_section']['links'])))
    for key, v in specs.items():
        print(' ', key, v['words'], 'words', v['sha256'][:12], v['section'])


if __name__ == '__main__':
    main()
