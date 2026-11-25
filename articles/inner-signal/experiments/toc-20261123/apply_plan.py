#!/usr/bin/env python3
"""The final contents of the Self-Hypnosis guide (PROPOSAL-FINAL.json and STRUCTURE-FINAL.json, from make_final.py) as
one edit to the post: the new order of its blocks, every heading's text and level, the text changes his answers call for
(TEXT-CHANGES.json and the two below), and every section link (LINK-PLAN.json and the three below).

  python3 apply_plan.py [--pointer]

Reads LIVE-BODY-20261123.html (the live post, unchanged since 2026-11-20: catchup/LIVE-POST-META-inner-signal-20261125.json).
Writes PLAN.json (what changes, for people), EDITOR-OPS.json (for apply_in_editor.js), BEFORE.md and AFTER.md (the guide
as readers see it, for section_refs.py and the checks) and pangram/SEC-<id>-after.txt for each section whose body text
changes. --pointer adds the linked sentence at the end of "Protection From Hypnotists" (put to him on 2026-11-25).

The edit is by block: the post's 720 top-level blocks keep their order except where a section moves; a divider line
belongs to the heading after it; a dropped heading's divider passes to the next section if that one has none.
"""
import hashlib, json, os, re, sys
from bs4 import BeautifulSoup, Tag

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', '..', '..', 'tools', 'humanization'))
sys.path.insert(0, os.path.join(HERE, '..', '..', '..', 'nibbana', 'experiments', 'toc-20261123'))
import section_links as sl
from check_texts import lines_of

BASE, POST = 'https://ibogaqueen.substack.com', 202810155
J = lambda f: json.load(open(os.path.join(HERE, f), encoding='utf-8'))

# Inline text changes: (id, section, text to find once in the post, what it becomes, why)
EDITS = [
    ('T8', 'S001', 'working with sleep, influence, and more inductions', 'influence, and more inductions',
     'answer 8: the sleep appendix goes, so the list of what the appendices cover no longer names it'),
    ('T1', 'S001', 'All sources used are in Appendix K.', 'All sources used are in Appendix J.', 'answer 8: K becomes J'),
    ('T5', 'S079', 'What are you avoiding doing in the real world by doing this?”',
     'What are you avoiding doing in the real world by doing this?” For more on daydreaming, see Appendix E.',
     'answer 11: the pointer "Getting Anxious?" has for Appendix D'),
    ('T6a', 'S120', 'interview them a bit:', 'interview them a bit more:', 'answer 10: his three lists now come first'),
    ('T6b', 'S120', ' After it\'s over, check how well your critical thinking is working when you look back on how it went.', '',
     'answer 10: this sentence joins the start of his "Then afterwards" paragraph'),
    ('T6c', 'S131', 'Then afterwards, check in about what was actually done',
     'Then afterwards, check how well your critical thinking is working when you look back on how it went, and check in '
     'about what was actually done', 'answer 10'),
    ('Q7', 'S122', 'Breathe in small amounts through your nose and let it out quietly, through your nose too.',
     'By simply pursing your lips together on exhale, you can slow down your exhale. Slower exhales, combined with not '
     'breathing more on inhales, lead to overall reduction in breathing. That slight oxygen hunger feels a bit anxiogenic '
     'for the first 20 seconds or so, but after that, you’ll feel much calmer.',
     'his answer of 2026-11-25 11:18 ("7 b": the somatic guide\'s way here too): the nose-out sentence becomes the three '
     'sentences of his somatic guide\'s Breathwork section, word for word; the rest of his paragraph stays'),
    ('Q8', 'S019', 'The longer version of this exercise can be found in my', 'There is more on borrowed adulthood in my',
     'his answer of 2026-11-25 11:18 ("8 a"): the inner child guide no longer has the adult hat exercise; the sentence '
     'points to its "Borrowed Adulthood" section'),
    ('Q9', 'S124', 'or even a free intro session, please see', 'or even a free intro session for paid subscribers, please see',
     'his answer of 2026-11-25 11:18 ("9 yes"): the somatic guide gives one free session to paid subscribers'),
    # a sentence that names a section by its old heading takes the new name (answer 13; headings brief, rule 9)
    ('N04', 'S001', '“Let the next response guide you” section', '“Let the Response Guide You” section', 'answer 13'),
    ('N13', 'S040', '"Already trancey? Stabilize before dipping deeper."', '"Already Trancey?"', 'answer 13'),
    ('N15', 'S042', 'after induction in Let the next response guide you.', 'after induction in Let the Response Guide You.', 'answer 13'),
    ('N16', 'S042', 'called "When you\'re already trancey"', 'called "Already Trancey?"', 'answer 13'),
    ('N17', 'S042', 'and the Come all the way back section', 'and the Come All the Way Back section', 'answer 13'),
    ('N19', 'S063', '‘Come all the way back’ procedure', '‘Come All the Way Back’ procedure', 'answer 13'),
    ('N20', 'S065', 'the cue from "A shortcut back into hypnosis"', 'the cue from "A Shortcut Back In"', 'answer 13'),
    ('N21', 'S067', '(see “When this needs more support than a guide can provide”)', '(see “When to Get Outside Help”)', 'answer 13'),
    ('N28', 'S108', 'See "A shortcut back into hypnosis" for a quick way back in.', 'See "A Shortcut Back In" for a quick way back.',
     'answer 13; "in" goes so the sentence doesn\'t say "back in" twice'),
    ('N29', 'S118', '(see “Come all the way back”)', '(see “Come All the Way Back”)', 'answer 13'),
    ('N31', 'S127', '(the two-hand practice in Working with your inner child)', '(the two-hand practice in Inner Child Practices)', 'answer 13'),
    ('N32', 'S130', 'see “Using synchronicity as your own wake-up bell” in Appendix B', 'see “Synchronicity as a Bell” in Appendix B', 'answer 13'),
]
# New paragraphs: (id, section it ends, [[text, link target or None], ...], why). A target is a section id or a URL.
NEW_P = [
    ('T3', 'S143', [['The general rule is the one in “', None], ['Daily Life Is the Feedback', 'S086'],
                    ['”: if what you\'re doing is making you more paranoid, sleepless, grandiose, isolated or scared, or '
                     'things feel more and more unreal, stop going deeper and get help.', None]],
     'answer 7: "The General Rule" goes; this sentence keeps every warning sign of his'),
    ('T7', 'S122', [['Try the continuous breathing from Systema (a Russian martial art) too: it helps not just with relaxing, '
                     'but with getting into trance and flow states more deeply. You can learn it from ', None],
                    ['the best video on it I\'ve seen so far', 'https://www.youtube.com/shorts/Nar2-nvomAk'],
                    [', and ', None],
                    ['my somatic guide explains it more', 'https://ibogaqueen.substack.com/i/201523223/systema-circular-breathing-and-compassionate-relaxing-martial-arts'],
                    ['.', None]],
     'his note of 2026-11-24 21:05 UTC: Systema\'s continuous breathing beside the Buteyko lines'),
]
NEW_P.append(('P1', 'S007', [['If you do let a hypnotist work on you, or listen to a stranger\'s hypnosis recording, go through the questions in “', None],
                          ['Find a Hypnotist Who Fits', 'S131'], ['” first.', None]],
           'question 3 of 2026-11-25 ("yes"): both final readers looked here for what to check before playing a stranger\'s recording'))
POINTER = None
# Section links beyond LINK-PLAN.json, found on 2026-11-25: (section, words to link, target, why)
MORE_LINKS = [
    ('S039', 'appendix C', 'S119', 'a pointer the plan had missed'),
    ('S148', 'a no-trance inner contact', 'S157', '"No-Trance Inner Contact" leaves the library, so its mention there points to it'),
    ('S130', 'skilled outside support', 'S131', '"Find a Hypnotist Who Fits" moves out from under this paragraph, which led into it'),
]
# What a link's words become after the edits above (the plan lists the words as they are in the live post)
LINK_WORDS_AFTER = {4: 'Let the Response Guide You', 13: 'Already Trancey?', 15: 'Let the Response Guide You', 16: 'Already Trancey?',
                    17: 'Come All the Way Back', 19: 'Come All the Way Back', 20: 'A Shortcut Back In', 21: 'When to Get Outside Help',
                    28: 'A Shortcut Back In', 29: 'Come All the Way Back', 31: 'Inner Child Practices', 32: 'Synchronicity as a Bell',
                    7: 'Appendix J'}
# the date in the subtitle changes with the post (gate E323); the version only when he says
SUBTITLE = ('Last update: Nov 20, 2026', 'Last update: Nov 25, 2026')
MERGE_BEFORE = 'You should be able to be firmly encouraged'      # S120's paragraphs go in before this block of S131
PRE_TAKEOVER = {'S157': 'S040'}    # the divider before "Induction" now comes before "No-Trance Inner Contact", right above it


def kind(b):
    if re.fullmatch(r'h[1-6]', b.name):
        return b.name
    if b.name == 'div' and b.find('hr') and not b.get_text(strip=True):
        return 'hr'
    if b.name == 'p' and 'button-wrapper' in (b.get('class') or []):
        return 'button'
    return b.name


def fnv(text):
    """32-bit FNV-1a over the UTF-16 code units of the text without whitespace (the same in apply_in_editor.js)."""
    h = 0x811c9dc5
    data = re.sub(r'\s+', '', text).encode('utf-16-le')
    for k in range(0, len(data), 2):
        h ^= data[k] | (data[k + 1] << 8)
        h = (h * 0x01000193) & 0xffffffff
    return h


def main(pointer=False):
    html = open(os.path.join(HERE, 'LIVE-BODY-20261123.html'), encoding='utf-8').read()
    B = [b for b in BeautifulSoup(html, 'html.parser').children if isinstance(b, Tag)]
    K = [kind(b) for b in B]
    T = [b.get_text('') for b in B]
    final = J('PROPOSAL-FINAL.json')
    st = J('STRUCTURE-FINAL.json')
    dropped = st['dropped']
    head = {e['id']: e['heading'] for e in final}
    # sections by block index
    sec, cur, n = {'S000': {'h': None, 'pre': None, 'body': []}}, 'S000', 0
    for i, k in enumerate(K):
        if re.fullmatch(r'h[1-6]', k):
            n += 1
            cur = 'S%03d' % n
            sec[cur] = {'h': i, 'pre': None, 'body': [], 'level': int(k[1]), 'was': re.sub(r'\s+', ' ', T[i]).strip()}
        else:
            sec[cur]['body'].append(i)
    ids = ['S%03d' % k for k in range(1, n + 1)]
    for a, b in zip(['S000'] + ids, ids):      # a divider right before a heading belongs to that heading
        if sec[a]['body'] and K[sec[a]['body'][-1]] == 'hr':
            sec[b]['pre'] = sec[a]['body'].pop()
    now = {e['id']: e for e in J('CONTENTS-NOW.json')}
    assert all(sec[i]['was'] == now[i]['heading'] and sec[i]['level'] == now[i]['level'] for i in ids), 'the body and CONTENTS-NOW.json differ'
    order = [e['id'] for e in final]
    # dividers: a dropped heading's divider passes on; a section placed right above a divided one takes the divider
    gone = set()
    for d in dropped:
        if sec[d]['pre'] is not None:
            nxt = ids[ids.index(d) + 1]
            if nxt not in dropped and sec[nxt]['pre'] is None:
                sec[nxt]['pre'] = sec[d]['pre']
            else:
                gone.add(sec[d]['pre'])
            sec[d]['pre'] = None
    for taker, giver in PRE_TAKEOVER.items():
        assert order.index(taker) + 1 == order.index(giver) and sec[taker]['pre'] is None
        sec[taker]['pre'], sec[giver]['pre'] = sec[giver]['pre'], None
    new_p = list(NEW_P)
    edits = list(EDITS)
    # the new order of blocks
    doc = [{'i': i} for i in sec['S000']['body']]
    for i in order:
        s, e = sec[i], next(x for x in final if x['id'] == i)
        if s['pre'] is not None:
            doc.append({'i': s['pre']})
        doc.append({'i': s['h'], 'h': [e['level'], e['heading']]} if (e['heading'], e['level']) != (s['was'], s['level']) else {'i': s['h']})
        body = [{'i': k} for k in s['body']]
        if i == 'S001':
            body += [{'i': k} for k in sec['S002']['body']]          # answer 1: its two sentences end this section
        if i == 'S131':
            at = next(k for k, x in enumerate(body) if T[x['i']].startswith(MERGE_BEFORE))
            body[at:at] = [{'i': k} for k in sec['S120']['body']]     # answer 10: the audit, before his "firmly encouraged" line
        for pid, where, segs, _ in new_p:
            if where == i:
                body.append({'p': [[t, (sl.anchor(head[h]) if h and h.startswith('S') else h)] for t, h in segs], 'id': pid})
        doc += body
    for d in ('S090', 'S144', 'S147'):
        gone.update(sec[d]['body'])
    gone.update(sec[d]['h'] for d in dropped)
    used = [x['i'] for x in doc if 'i' in x]
    assert len(used) == len(set(used)) and set(used) | gone == set(range(len(B))) and not set(used) & gone, 'blocks lost or doubled'
    # every edit is found once, in its section
    whole = '\n'.join(T)
    for eid, where, a, b, _ in edits:
        assert whole.count(a) == 1, (eid, whole.count(a))
        assert any(a in T[k] for k in sec[where]['body']), (eid, 'not in', where)
    after_text = {}
    def text_after(k):
        t = T[k]
        for _, _, a, b, _ in edits:
            t = t.replace(a, b)
        return t
    # links: the words as they will read, found once with enough of the sentence around them
    links = []
    plan_links = [(l['n'], l['in'], LINK_WORDS_AFTER.get(l['n'], l['text']), l['to']) for l in J('LINK-PLAN.json')['links'] if l['n'] not in (25, 35)]
    plan_links += [(25, 'S079', 'Appendix E', 'S129')]
    plan_links += [(36 + k, w, t, to) for k, (w, t, to, _) in enumerate(MORE_LINKS)]
    plan_links += [(39, 'S019', 'Inner Child Self-Love Reparenting Guide', 'https://ibogaqueen.substack.com/i/189761959/borrowed-adulthood')]
    all_after = [text_after(k) for k in used]
    for num, where, words, to in plan_links:
        if to in dropped:
            to = dropped[to][0]
        outside = to.startswith('http')
        blocks = sec[where]['body'] + (sec['S120']['body'] if where == 'S131' else [])
        hits = [(k, m.start()) for k in blocks for m in re.finditer(re.escape(words), text_after(k))]
        assert len(hits) == 1, (num, where, words, len(hits))
        k, at = hits[0]
        t, a, b = text_after(k), at, at + len(words)
        while sum(x.count(t[a:b]) for x in all_after) != 1:
            assert a > 0 or b < len(t), (num, 'no unique context')
            a, b = max(0, a - 12), min(len(t), b + 12)
        links.append({'n': num, 'in': where, 'find': t[a:b], 'words': words, 'to': to, 'heading': '' if outside else head[to],
                      'href': to if outside else sl.anchor(head[to]), 'unchecked': '' if outside else (sl.unchecked(head[to]) or '')})
    expected = [[e['level'], e['heading']] for e in final]
    ops = {'post': POST, 'blocks': len(B), 'subtitle': list(SUBTITLE),
           'fingerprint': [[k, fnv(T[k])] for k in range(len(B)) if K[k] in ('p', 'h1', 'h2', 'h3', 'h4', 'blockquote', 'ul', 'ol') and T[k].strip()],
           'edits': [{'id': e, 'from': a, 'to': b} for e, _, a, b, _ in edits],
           'links': [{'find': l['find'], 'words': l['words'], 'href': l['href']} for l in links],
           'order': doc, 'expected_headings': expected}
    json.dump(ops, open(os.path.join(HERE, 'EDITOR-OPS.json'), 'w', encoding='utf-8'), ensure_ascii=False)
    plan = {'from': 'PROPOSAL-FINAL.json, STRUCTURE-FINAL.json, TEXT-CHANGES.json, LINK-PLAN.json', 'pointer_sentence': pointer,
            'sections': [{'id': e['id'], 'heading': e['heading'], 'level': e['level'], 'was': sec[e['id']]['was'], 'was_level': sec[e['id']]['level']} for e in final],
            'dropped': dropped, 'moves': st['moves'], 'levels': st['level'],
            'edits': [{'id': e, 'in': w, 'from': a, 'to': b, 'why': y} for e, w, a, b, y in edits],
            'new_paragraphs': [{'id': p, 'ends': w, 'text': ''.join(t for t, _ in segs), 'why': y} for p, w, segs, y in new_p],
            'links': links, 'blocks_removed': sorted(gone)}
    json.dump(plan, open(os.path.join(HERE, 'PLAN.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

    # the guide as readers see it, before and after
    def lines(k):
        out = lines_of(B[k])
        return out
    def after_lines(x):
        if 'p' in x:
            return [''.join(t for t, _ in x['p'])]
        if 'h' in x:
            return []
        out = lines(x['i'])
        for _, _, a, b, _ in edits:
            out = [l.replace(a, b) for l in out]
        return [l for l in out if l.strip()]
    before = []
    for k in range(len(B)):
        before += (['#' * int(K[k][1]) + ' ' + re.sub(r'\s+', ' ', T[k]).strip()] if K[k][0] == 'h' and K[k] != 'hr' else lines(k))
    after, by_sec, cur = [], {}, 'S000'
    hid = {sec[i]['h']: i for i in ids}
    for x in doc:
        if 'i' in x and x['i'] in hid:
            cur = hid[x['i']]
            e = next(y for y in final if y['id'] == cur)
            after.append('#' * e['level'] + ' ' + e['heading'])
            continue
        ls = after_lines(x)
        after += ls
        by_sec.setdefault(cur, []).extend(ls)
    open(os.path.join(HERE, 'BEFORE.md'), 'w', encoding='utf-8').write('\n\n'.join(before) + '\n')
    open(os.path.join(HERE, 'AFTER.md'), 'w', encoding='utf-8').write('\n\n'.join(after) + '\n')
    os.makedirs(os.path.join(HERE, 'pangram'), exist_ok=True)
    changed = sorted({w for _, w, a, b, _ in edits if not w == 'S120'} | {w for _, w, _, _ in new_p} | {'S131', 'S001'})
    specs = {}
    for i in changed:
        text = '\n\n'.join(by_sec[i]) + '\n'
        f = 'pangram/SEC-%s-after.txt' % i
        open(os.path.join(HERE, f), 'w', encoding='utf-8').write(text)
        specs[i] = {'file': f, 'heading': head[i], 'words': len(text.split()), 'sha256': hashlib.sha256(text.encode()).hexdigest()}
    json.dump(specs, open(os.path.join(HERE, 'pangram', 'SEC-SPECS.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    ren = sum(1 for x in doc if 'h' in x)
    print('%d blocks -> %d; %d headings (%d renamed or re-levelled), %d blocks removed, %d edits, %d new paragraphs, %d links; %d sections with changed text'
          % (len(B), len(doc), len(expected), ren, len(gone), len(edits), len(new_p), len(links), len(changed)))
    print('sections to check:', ', '.join('%s (%d words)' % (i, specs[i]['words']) for i in changed))


if __name__ == '__main__':
    main('--pointer' in sys.argv)
