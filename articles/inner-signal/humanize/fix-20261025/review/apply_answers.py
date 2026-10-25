"""Put Joel's review-page answers of 2026-10-25 into the hypnosis guide (HUMANIZED-SO-FAR.md), with every change recorded.

His message of 19:42 UTC (../joel-20261025-1942-message.txt): "ok i accept all the answers i didn't mark, and here is what
i marked ." with his answers file (ANSWERS-20261025-1940.json, exported from the review page). So a suggestion goes in
when he approved it, when he revised it (his version, word for word), or when he left it unmarked and my advice was
"approve"; one he left unmarked with my advice "leave" stays out. His comments asked for three things more, done here as
passes over the whole guide: "the kid" becomes "your little one" (RR-7.3: "check all "the kid" instances and auto-fix"),
no quote marks around inner child (RR-2.1: "check and remove quotes if you find it elsewhere for that"), and IC-T1's
they/them on the inner child words the other suggestions add in its section (its note promised that).

Where two answers change one paragraph, both go in, change by change, from the same original (each one's words, diffed
against the paragraph as it was); a change inside words another answer cut goes with the cut, and the cases the review
page named as either/or are settled as its notes said (IC-A9 replaces RR-2.3's paragraph; ST-8.2 takes RR-8.8's commas
with the line it moves). Links and italics stay on the same words (html_text_edit.set_text). Follow-on fixes that two
answers together need are listed in FOLLOW_ON and recorded.

  python3 articles/inner-signal/humanize/fix-20261025/review/apply_answers.py [--check]   # --check: report only
Writes HUMANIZED-SO-FAR.md and review/APPLIED.json (every suggestion's fate, and each changed paragraph before and after).
"""
import argparse
import difflib
import hashlib
import html
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import html_text_edit  # noqa: E402
import suggestion_review as sr  # noqa: E402

ARTICLE = ROOT / 'articles/inner-signal/humanize/HUMANIZED-SO-FAR.md'
REVIEW = HERE / 'REVIEW.json'
ANSWERS = HERE / 'ANSWERS-20261025-1940.json'
OUT_RECORD = HERE / 'APPLIED.json'

# a paragraph that only one of two answers decides: (block's suggestion that wins, the one that falls away, why)
SUPERSEDES = [
    ('IC-A9', 'RR-2.3', 'IC-A9 replaces the whole paragraph with your six questions; RR-2.3 changed only its first question (the page: "if you approve that, this one falls away").'),
    ('CV-8.9', 'TY-6', 'Your own version of the paragraph already has no space before the comma.'),
]
# words an answer changed that another answer cut: the cut wins
CUT_WINS = {('CV-6.6', 'RR-8.4'): 'CV-6.6 cuts "You must be the one authoring these. You must see them.", the sentence RR-8.4 added "cues" to.'}
# follow-on fixes two answers together need (his rule: the "after" shows the result with any follow-on fix already made)
FOLLOW_ON = [
    ('Let the next response guide you', 'and then try doing it without looking at the screen.',
     'and then try doing the inner meeting without looking at the screen.',
     'CV-4.5 cuts the sentence that named the inner meeting, so RR-5.7\'s "Read through these sections, and then try doing it" names it.'),
    ('Finish without forcing a revelation', 'keep a promise etc)! Whatever it is,', 'keep a promise etc). Whatever it is,',
     'CV-4.9 cuts "or it may be that there is nothing to do!", whose "!" stayed; IC-B2 starts the next sentence after it.'),
    ('Installing the synchronicity cue', 'They do not authorize you to make a decision.', 'These cues do not authorize you to make a decision.',
     'CV-6.5 to 6.8 cut the four sentences before it, so the paragraph began with "They" and nothing for it to point to; it gets RR-8.4\'s "cues", which you approved for the sentence CV-6.6 cut.'),
    ('Appendix G: Altered states',
     'I’d learn to do inner-child therapy sober first, in your ordinary mindstate, since that’s the one you’ll be living in, and get enough Nurturer and Protector in the room before you go deep.',
     'I’d learn the inner child work sober first, with enough Nurturer and Protector in the room before you go deep (see the inner child reparenting section).',
     'IC-A17 and IC-B19 add the same lines; as IC-A17\'s note said, the full words stay in "Inner child reparenting" and Appendix G points to them, keeping what its next sentence ("Borrowed is fine") needs.'),
]
THE_KID = [('Listen to the kid for as long as it takes until it\'s comfortable enough', 'Listen to your little one for as long as it takes until they\'re comfortable enough'),
           ('small promises to the kid,', 'small promises to your little one,'),
           ('show my kid I’m for real', 'show my little one I’m for real')]   # self-talk; Emulate's words, in none of his sources
T1_RULES = [('the "child"', 'your little one'), ('your "inner child"', 'your little one'), ('the "inner child"', 'your little one'),
            ('to your "inner child" they\'re', 'to your little one they\'re'),
            ('if he/she doesn\'t, it is', 'if they don\'t, it is'), ('he/she doesn\'t', 'they don\'t'), ('he/she is', 'they are'),
            ('he/she reaches', 'they reach'), ('he/she needs', 'they need'), ('him/her', 'them'), ('his/her', 'their'),
            ('he/she', 'they'), ('your "inner child."', 'your little one.'), ('the inner child no matter', 'your little one no matter'),
            ('blaming the inner child for', 'blaming your little one for')]
INNER_CHILD_QUOTES = re.compile(r'["“‘\']inner child["”’\']')


def region(before, after):
    """(p, s): BEFORE and AFTER share their first p and last s characters; the change is what's between."""
    p = 0
    while p < min(len(before), len(after)) and before[p] == after[p]:
        p += 1
    s = 0
    while s < min(len(before), len(after)) - p and before[len(before) - 1 - s] == after[len(after) - 1 - s]:
        s += 1
    return p, s


def hunks(before, after):
    """The changes from BEFORE to AFTER as [(start, end, new)] in BEFORE's characters, word by word; two changes with
    less than a few characters of unchanged text between them are one."""
    ta = [(m.group(0), m.start()) for m in re.finditer(r'\w+|[^\w\s]|\s+', before)]
    tb = [m.group(0) for m in re.finditer(r'\w+|[^\w\s]|\s+', after)]
    ops = difflib.SequenceMatcher(None, [t for t, _ in ta], tb, autojunk=False).get_opcodes()
    out = []
    for op, i1, i2, j1, j2 in ops:
        if op == 'equal':
            continue
        a = ta[i1][1] if i1 < len(ta) else len(before)
        z = ta[i2 - 1][1] + len(ta[i2 - 1][0]) if i2 > i1 else a
        new = ''.join(tb[j1:j2])
        if out and a - out[-1][1] < 6:   # a short gap of unchanged text: one change
            pa, pz, pn = out[-1]
            out[-1] = (pa, z, pn + before[pz:a] + new)
        else:
            out.append((a, z, new))
    return out


def place(text, before, a, z, new):
    """TEXT with BEFORE[a:z] made NEW, found by enough of BEFORE's words around it to be found once; None if it can't be."""
    for size in (0, 12, 25, 50, 100, 200):
        for left, right in ((size, 0), (0, size), (size, size)):
            a0, a1 = max(0, a - left), min(len(before), z + right)
            o = before[a0:a1]
            if o and text.count(o) == 1:
                return text.replace(o, before[a0:a] + new + before[z:a1], 1)
    return None


def merge(before, changes, notes):
    """BEFORE with every change applied in turn: a cut by its exact words (tidied where it joins, sr.cut_text), any other
    answer change by change, each found by the unchanged words around it. A change whose words an earlier one took is
    tried again after the others; one that still can't be placed is a conflict: CUT_WINS settles it, anything else stops
    the script for a decision. Additions go first, then cuts, then rewrites."""
    def kind(c):
        if c[2]:
            return 1
        p, q = region(before, c[1])
        return 0 if p + q == len(before) else 2
    present = {c[0] for c in changes}
    kept = []
    for c in changes:
        win = next((w for (w, l) in CUT_WINS if l == c[0] and w in present), None)
        if win:   # its words are inside the cut: it goes with them
            notes.append('%s over %s: %s' % (win, c[0], CUT_WINS[(win, c[0])]))
            continue
        kept.append(c)
    text, pending = before, [(sid, after, cut, None) for sid, after, cut in sorted(kept, key=kind)]
    for _round in range(4):
        later = []
        for sid, after, cut, todo in pending:
            if cut:
                old = before[cut[0]:cut[1]]
                if text.count(old) == 1:
                    k = text.index(old)
                    text = sr.cut_text(text, k, k + len(old))
                else:
                    later.append((sid, after, cut, None))
                continue
            left = []
            for a, z, new in (todo if todo is not None else hunks(before, after)):
                t2 = place(text, before, a, z, new)
                if t2 is None:
                    left.append((a, z, new))
                else:
                    text = t2
            if left:
                later.append((sid, after, None, left))
        if not later or len(later) == len(pending):
            pending = later
            break
        pending = later
    for sid, _after, _cut, todo in pending:
        raise SystemExit('%s can\'t go in with the others on its paragraph (%r): %r' % (sid, todo, before[:100]))
    return text


# ---------------------------------------------------------------- Markdown blocks, with links kept on their words
PREFIX = re.compile(r'^(#{1,6}\s+|[-*+]\s+|\d+\.\s+|>\s?)')


def split_block(raw):
    m = PREFIX.match(raw)
    return (m.group(0), raw[m.end():]) if m else ('', raw)


def md_to_html(body):
    out = []
    for s in sr.segments(body):
        t = html.escape(s['t'], quote=False)
        if s['em']:
            t = '<em>%s</em>' % t
        if s['href']:
            t = '<a href="%s">%s</a>' % (html.escape(s['href'], quote=True), t)
        out.append(t)
    return ''.join(out)


def html_to_md(h):
    out, stack = [], []
    for m in re.finditer(r'<(/?)(a|em)(?:\s+href="([^"]*)")?>|([^<]+)', h):
        if m.group(4) is not None:
            out.append(html.unescape(m.group(4)))
        elif m.group(2) == 'em':
            out.append('*')
        elif not m.group(1):
            stack.append(html.unescape(m.group(3)))
            out.append('[')
        else:
            out.append('](%s)' % stack.pop())
    return ''.join(out)


def set_block_text(raw, new_text, lost):
    prefix, body = split_block(raw)
    inner = md_to_html(body)
    new_inner, dropped, moved = html_text_edit.set_text(inner, new_text)
    lost += dropped
    return prefix + html_to_md(new_inner)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--check', action='store_true')
    args = ap.parse_args()
    md = ARTICLE.read_text(encoding='utf-8')
    review = json.loads(REVIEW.read_text(encoding='utf-8'))
    answers = json.loads(ANSWERS.read_text(encoding='utf-8'))
    sha = hashlib.sha256(md.encode('utf-8')).hexdigest()
    assert sha == review['article']['sha256'] == answers['article']['sha256'], 'the guide changed since the review'
    bl = sr.blocks(md)
    raw = re.split(r'\n\s*\n', md.rstrip('\n'))
    assert len(raw) == len(bl), (len(raw), len(bl))
    def raw_text(i):
        return ''.join(x['t'] for x in sr.segments(split_block(raw[i])[1]))
    mismatched = [b['i'] for b in bl if raw_text(b['i']) != b['text']]   # only the post card the review joined
    A = {x['id']: x for x in answers['items']}
    S = {s['id']: s for s in review['suggestions']}
    fate = {}
    for sid, s in S.items():
        st = A[sid]['status']
        if st == 'approved':
            fate[sid] = 'approved'
        elif st == 'revise':
            fate[sid] = 'revised (his version)'
        elif st == 'rejected':
            fate[sid] = 'rejected'
        else:
            fate[sid] = 'accepted (unmarked, my advice approve)' if s['advice'] == 'approve' else 'left (unmarked, my advice leave)'
    applied = [sid for sid in S if fate[sid].startswith(('approved', 'revised', 'accepted'))]
    notes, lost = [], []
    gone = {}
    for win, lose, why in SUPERSEDES:
        if win in applied and lose in applied:
            gone[lose] = why
    # each block's changes
    per_block = {}
    for sid in applied:
        s = S[sid]
        if sid == 'IC-T1':
            continue   # a pass after the others, so the words they add get it too
        edits = s['edits']
        if A[sid]['status'] == 'revise':
            assert len(edits) == 1, sid
            edits = [{'block': edits[0]['block'], 'before': edits[0]['before'], 'after': A[sid]['your_version'].strip()}]
        for e in edits:
            if sid in gone and (sid != 'TY-6' or e['block'] == S['CV-8.9']['edits'][0]['block']):
                continue
            cut = None
            if s['type'] in ('caveat', 'repeat') and A[sid]['status'] != 'revise':
                sp = [x for x in s['spans'] if x['block'] == e['block']]
                if len(sp) == 1 and e['after'] == sr.cut_text(e['before'], sp[0]['start'], sp[0]['end']):
                    cut = (sp[0]['start'], sp[0]['end'])
            per_block.setdefault(e['block'], []).append((sid, e['after'], cut))
    # ST-8.2 moves RR-8.8's line: the commas go with it
    if 'ST-8.2' in applied and 'RR-8.8' in applied:
        src = [e for e in S['ST-8.2']['edits'] if e['after']][0]
        rr = S['RR-8.8']['edits'][0]
        line_old = rr['before'].replace('In other words: ', '')
        line_new = rr['after'].replace('In other words: ', '')
        per_block[src['block']] = [(sid, after.replace(line_old, line_new), cut) if sid == 'ST-8.2' else (sid, after, cut)
                                   for sid, after, cut in per_block[src['block']]]
        per_block[rr['block']] = [x for x in per_block[rr['block']] if x[0] != 'RR-8.8']
        notes.append('ST-8.2 with RR-8.8: the line moved into "It is my cue to:" has RR-8.8\'s commas.')
    text = {b['i']: b['text'] for b in bl}
    touched = set(per_block) | {i for sid in applied for k in ('inserts', 'moves') for x in S[sid][k]
                                for i in (x.get('blocks') or [x['before']]) if i < len(bl)}
    assert not (touched & set(mismatched)), sorted(touched & set(mismatched))
    changed = {}
    for i, changes in per_block.items():
        before = bl[i]['text']
        removals = [sid for sid, after, _cut in changes if after == '']
        if removals:
            changed[i] = ''
            continue
        changed[i] = changes[0][1] if len(changes) == 1 else merge(before, changes, notes)
    # passes: IC-T1, "the kid", quotes around inner child, follow-on fixes
    if 'IC-T1' in applied:
        for e in S['IC-T1']['edits']:
            t = changed.get(e['block'], text[e['block']])
            for a, z in T1_RULES:
                t = t.replace(a, z)
            assert not re.search(r'him/her|he/she|his/her|"inner child"', t), t[:200]
            changed[e['block']] = t
    for i in list(text):
        t = changed.get(i, text[i])
        if not t:
            continue
        t2, did = t, []
        for a, z in THE_KID:
            if a in t2:
                t2 = t2.replace(a, z)
                did.append('"%s" to "%s"' % (a, z))
        if INNER_CHILD_QUOTES.search(t2):
            t2 = INNER_CHILD_QUOTES.sub('inner child', t2)
            did.append('no quote marks around inner child')
        if t2 != t:
            changed[i] = t2
            notes.append('pass on %s: %s' % (sr.where(bl, i), '; '.join(did)))
    for section, a, z, why in FOLLOW_ON:
        hits = [i for i, t in changed.items() if t and a in t and bl[i]['section'] == section]
        assert len(hits) == 1, (section, a, hits)
        changed[hits[0]] = changed[hits[0]].replace(a, z)
        notes.append('follow-on in %s: %s' % (sr.where(bl, hits[0]), why))
    assert not any(re.search(r'\b(the|my) kid\b', changed.get(i, text[i]) or '') for i in text)
    if 'IC-T1' in applied and 'RR-2.1' in applied:
        notes.append('RR-2.1 (your version) with IC-T1 (approved) on "Love doesn’t have to wait for trust", P4: your version took the'
                     ' quote marks off two of its three "inner child"s; IC-T1 makes all three "your little one" and him/her they/them,'
                     ' as it said for the section, and your "Their age might not be your chronological age." stays word for word.')
    # the new Markdown, block by block
    new_raw = {}
    for i, t in changed.items():
        if t == '':
            new_raw[i] = None
            continue
        parts = t.split('\n\n')
        if len(parts) > 1:   # a paragraph break (ST-11.2): the second part is a new plain paragraph
            first = set_block_text(raw[i], parts[0], lost)
            new_raw[i] = [first] + parts[1:] if all('](' not in p for p in parts[1:]) else None
            if new_raw[i] is None:
                raise SystemExit('a split paragraph with links in its second part: %s' % sr.where(bl, i))
            continue
        new_raw[i] = [set_block_text(raw[i], t, lost)]
    # inserts and moves
    before_at, moved = {}, set()
    for sid in applied:
        for ins in S[sid]['inserts']:
            mdl = ('#' * int(ins['kind'][1]) + ' ' if ins['kind'] != 'p' else '') + ins['text']
            before_at.setdefault(ins['before'], []).append((ins.get('seq', 0), sid, [mdl]))
        for mv in S[sid]['moves']:
            moved.update(mv['blocks'])
            before_at.setdefault(mv['before'], []).append((mv.get('seq', 0), sid, ('move', mv['blocks'])))
    def block_out(i):
        if i in new_raw:
            return new_raw[i] or []
        return [raw[i]]
    out = []
    for j in range(len(raw) + 1):
        for _seq, _sid, what in sorted(before_at.get(j, []), key=lambda x: (x[0], x[1])):
            if isinstance(what, tuple):
                for i in what[1]:
                    out += block_out(i)
            else:
                out += what
        if j < len(raw) and j not in moved:
            out += block_out(j)
    new_md = '\n\n'.join(out) + ('\n' if md.endswith('\n') else '')
    # checks
    old_links = re.findall(r'\]\(([^)\s]+)\)', md)
    new_links = re.findall(r'\]\(([^)\s]+)\)', new_md)
    missing = [u for u in set(old_links) if new_links.count(u) < old_links.count(u)]
    record = {
        'answers': ANSWERS.name, 'review': REVIEW.name, 'article_before_sha256': sha,
        'article_after_sha256': hashlib.sha256(new_md.encode('utf-8')).hexdigest(),
        'counts': {f: sum(1 for x in fate.values() if x == f) for f in sorted(set(fate.values()))},
        'superseded': gone, 'notes': notes, 'links_dropped_by_edits': lost, 'links_missing_after': missing,
        'fates': fate,
        'paragraphs': [{'block': i, 'where': sr.where(bl, i), 'before': text[i], 'after': changed[i],
                        'by': sorted({sid for sid in applied if any(e['block'] == i for e in S[sid]['edits'])})}
                       for i in sorted(changed)],
        'inserted': [{'before': sr.where(bl, j) if j < len(bl) else 'the end', 'by': sid, 'text': w}
                     for j, lst in sorted(before_at.items()) for _s, sid, w in lst if not isinstance(w, tuple)],
        'moved': [{'blocks': [sr.where(bl, i) for i in w[1]], 'to_before': sr.where(bl, j) if j < len(bl) else 'the end', 'by': sid}
                  for j, lst in sorted(before_at.items()) for _s, sid, w in lst if isinstance(w, tuple)],
    }
    print(json.dumps(record['counts']), '| changed paragraphs:', len(changed), '| inserted:', len(record['inserted']),
          '| moved:', len(record['moved']), '| superseded:', list(gone), '| links dropped:', lost, '| links missing:', missing)
    for n in notes:
        print('NOTE', n)
    if args.check:
        return
    OUT_RECORD.write_text(json.dumps(record, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    ARTICLE.write_text(new_md, encoding='utf-8')
    print('wrote', ARTICLE.relative_to(ROOT), 'and', OUT_RECORD.relative_to(ROOT))


if __name__ == '__main__':
    main()
