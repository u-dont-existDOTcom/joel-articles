"""The hypnosis guide's editor page of 2026-10-27 (EDITOR-27.json, EDITOR-27.html): questions 21, 22 and 23 on one page.

Joel, 2026-10-27 15:37 UTC (joel-20261027-1537-message.txt, with batch 481's recheck links): "21. your list of cards was a
json file? i can't read that", "22. give me the editor interface so i can see and edit what needs editing", "23. i need
that editor interface we developed remember that?". Question 21's page was published from his other account, so it didn't
open here, and the questions page's fallback was the cards' JSON file; questions 22 and 23 had come to him as options in
a list. So all three are now on one marking page (tools/humanization/suggestion_review.py, gate E265 and E269), published
from the account he is using:
- question 21: the 34 cards of ../../fix-20261026/review/build_review_481.py (Emulate's fixes, every new sentence the
  owner-delivery gate's delivered text), each with how its words read in his newest check (READINGS.json, readings.py)
  and, for batch 481's, how the words they replace read in the check before it;
- question 22: every other window of his newest check at less than High confidence, as stretches for him to keep or edit
  (advice "edit": no change of mine; Edit opens his own version of the paragraph);
- question 23: the hypnosis audit, the one AI window, as one stretch to keep or edit, with what Emulate's versions did to
  it.

  python3 articles/inner-signal/humanize/fix-20261027/review/build_editor_27.py
"""
import datetime
import hashlib
import importlib.util
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parents[1]
spec = importlib.util.spec_from_file_location('b481', H / 'fix-20261026/review/build_review_481.py')
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
br, sr = m.br, m.sr
READ = json.loads((HERE / 'READINGS.json').read_text(encoding='utf-8'))
RD = H / 'fix-20261026/b481/recheck/read'
RES = {p: json.loads((RD / ('RESULT-%s.json' % p)).read_text(encoding='utf-8')) for p in 'AB'}
FEED = {p: RES[p]['link'] for p in 'AB'}
MASTER_MD = (H / 'fix-20261026/b481/CANDIDATE-MASTER.md').read_text(encoding='utf-8')
MBL = sr.blocks(MASTER_MD)
GIT_FILE = 'articles/inner-signal/humanize/fix-20261027/review/EDITOR-27.html'
FLAT = str.maketrans({'“': '"', '”': '"', '‘': "'", '’': "'", ' ': ' '})

TYPES = {
    'held': {'label': 'Fix, reads High in place',
             'about': 'Emulate\'s version of a stretch that read AI in an earlier check. In your newest check it reads Human, '
                      'High confidence, where it stands.'},
    'raised': {'label': 'Fix, raised to High',
               'about': 'A stretch that read Human at Medium or Low confidence. In your newest check Emulate\'s version reads '
                        'Human, High confidence, where it stands.'},
    'notyet': {'label': 'Fix, still under High',
               'about': 'Emulate\'s version reads Human in your newest check, but at Medium or Low confidence.'},
    'short': {'label': 'Short line, under High',
              'about': 'A line of a few words that read Human at Medium or Low confidence (question 22). Pangram rarely gives '
                       'a line this short its top label. Keep it, or edit it.'},
    'medium': {'label': 'Longer stretch, under High',
               'about': 'A stretch of several words that read Human at Medium or Low confidence, with no fix yet. Keep it, '
                        'or edit it.'},
    'audit': {'label': 'The audit, AI',
              'about': 'The hypnosis audit, the one stretch of the guide that reads AI (question 23). Keep it, or edit it.'},
}
RANK = {('Human', 'High'): 0, ('Human', 'Medium'): 1, ('Human', 'Low'): 2, ('AI', 'Low'): 3, ('AI', 'Medium'): 4,
        ('AI', 'High'): 5}


def kind(label):
    return 'AI' if str(label).startswith('AI') else 'Human'


def says(r):
    """"Human, High (0.998)" for a reading."""
    return '%s, %s (%s)' % (r['label'], r['confidence'], r['calibrated'])


# ---------------------------------------------------------------- question 21: the cards, as they read now

OLD_WHY = {   # the ten cards of batches 479 and 480: what they were, then how they read in his newest check
    'HG-S7': 'Your inner child guide\'s whole sentence, with the rent joke, read AI (High) three checks ago. Emulate\'s '
             'version, with your "keeps" put back, has read Human (High) where it stands since. "Grown-up" becomes '
             '"person"; the sentences around it say it\'s you.',
    'HG-S2': 'This whole paragraph read AI (High) four checks ago. Emulate\'s version has read Human where it stands since. '
             'Your two published points are back in it: the practices are familiar ones, and you don\'t claim the whole '
             'sequence is proven as one treatment.',
    'HG-S3a': 'The end of this paragraph read AI (Low) four checks ago. Emulate\'s version, without "you can" (the gate\'s '
              'check counts it as coaching), has read Human where it stands since. The section\'s own heading is in it so a '
              'reader can find it, and your "not stable" stays.',
    'HG-S3b': 'These two sentences read AI (four Low windows) four checks ago. Emulate\'s three short sentences read Human '
              'where they stand, at Medium and Low the check before last, and High in your newest. Each of your words keeps '
              'what it does: "stop" ends the induction, "less" asks less of you, "quiet" stops the talking.',
    'HG-S8': 'These two sentences (IC-A14, the inner child alignment card you approved) read AI (Medium and High) three checks '
             'ago, after the edits above them. Emulate\'s version has read Human where it stands since. It ends on your '
             'card\'s "or a bit of each".',
    'HG-S9': 'These two sentences read AI (Low and Medium) three checks ago, after the edits above them, though they hadn\'t '
             'changed. Emulate\'s three sentences have read Human where they stand since. One word to know: '
             '"internalized" becomes "adopted", and the brackets still say it came from how you were treated.',
    'HG-S4': 'These are your own two sentences from your inner child guide, and here they read AI (Low and High) four checks '
             'ago. Emulate\'s one sentence has read Human where it stands since. It keeps both points: it has to make sense '
             'to you, and anything big or hard to undo waits till you\'re calm and have checked it against what you know. '
             'One change in strength: your "can wait" becomes "wait".',
    'HG-S5': 'This line, from your inner child guide (the inner child alignment added it), read AI (High) here four checks '
             'ago. Emulate\'s version, ending on your own three words from that guide, "no faking required", read Human '
             '(High) the check before last. (The gate\'s check counts "you don\'t have to" as coaching, and a reviewer turned '
             'down "Don\'t fake it." because it makes your permission a rule.)',
    'HG-S6': 'Your published test, word for word, read AI here (High, 17 words) four checks ago. Emulate\'s question has read '
             'Human where it stands since. It asks the same test: whether this way of responding helps you get clearer, '
             'steadier and less hooked.',
    'HG-S10': 'This sentence, from your inner child guide (the inner child alignment added it, IC-B19), read AI (Low) three '
              'checks ago. Emulate\'s version has read Human where it stands since. It keeps both conditions: someone stable, '
              'and not someone who will take over your trip.',
}
NEW_NOTE = {   # batch 481's cards whose advice changes with his newest check
    'HG-S14': ('leave', 'It reads no better than the wording it replaces (Medium both times, 0.982 then 0.976), so the '
                        'change buys nothing. Approve it anyway if you like Emulate\'s wording.'),
    'HG-S25': ('approve', 'It reads better than what\'s there now (Low 0.879 then, Medium 0.987 now), though not High yet.'),
    'HG-S28': ('approve', 'It reads better than what\'s there now (Low 0.618 then, Medium 0.961 now), though not High yet.'),
    'HG-S29': ('leave', 'It moved from Low (0.575) to Low (0.813), still under High, and it loses your ready-to-say lines. '
                        'Reject keeps them.'),
    'HG-S31': ('approve', 'A small change that moved it from Low (0.531) to Medium (0.989). Reject keeps your sentence.'),
}


def card_why(sid, why, r):
    now, before = r['now'], r['before']
    head = 'Your newest check (part %s): %s, where it stands.' % (now['part'], says(now))
    if r['batch'] != 'b481':
        return head + ' ' + OLD_WHY[sid]
    # batch 481's own text gives the reading of the check before (it called it "your last check"); a first sentence that
    # gave only that reading ("Read Human (Medium, 0.989) ... in your last check (part A).") becomes one sentence with the
    # replaced words' reading
    why = why.replace('in your last check', 'in the check before').replace('In your last check', 'In the check before')
    if why.startswith('Read Human (') and '). ' in why:
        why = 'The words it replaces read %s in the check before. ' % says(before) + why.split('). ', 1)[1]
    return head + ' ' + why


def add_cards():
    added, covered = [], set()
    for sid, name, old_ref, new_ref, typ, title, why, note in m.CARDS:
        d = m.GATES[new_ref[0]] / name
        delivered = (d / 'FOR-JOEL.txt').read_text(encoding='utf-8')
        old_c, new_c = m.SPOTS[old_ref[0]][old_ref[1]], m.SPOTS[new_ref[0]][new_ref[1]]
        assert delivered == new_c['new'], sid
        r = READ[sid]
        now = r['now']
        high = (now['label'], now['confidence']) == ('Human', 'High')
        ntyp = ('held' if r['batch'] != 'b481' else 'raised') if high else 'notyet'
        advice, nnote = NEW_NOTE.get(sid, ('approve', note))
        i = old_c['block']
        s = br.add(sid, ntyp, title, advice, edits=[(i, old_c['old'], new_c['new'])], why=card_why(sid, why, r),
                   note=nnote, found_by=m.FOUND_481 if new_ref[0] == 'b481' else m.FOUND)
        added.append((sid, i, old_c['old'], new_c['new']))
        covered |= windows_over(new_c['new'])
    by = {}
    for sid, i, old, new in added:
        by.setdefault(i, []).append((sid, old, new))
    for i, edits in by.items():   # every changed paragraph, all its cards applied, is the one the newest check read
        t = br.BL[i]['text']
        for sid, old, new in edits:
            t = t.replace(br.locate(sid, t, old), new)
        assert t == m.MASTER[i]['text'], (i, [e[0] for e in edits])
    return covered


def windows_over(words):
    """(part, window number) of every window of the newest check over WORDS."""
    w = words.translate(FLAT).strip()
    out = set()
    for p, r in RES.items():
        t = r['text'].translate(FLAT)
        if t.count(w) == 1:
            a = t.index(w)
            b = a + len(w)
            out |= {(p, i) for i, x in enumerate(r['windows']) if x['start_index'] < b and x['end_index'] > a}
    return out


# ---------------------------------------------------------------- question 22: every other window under High

def line_blocks(part):
    """The master block of each line of the part's checked text (in order: each line is a paragraph or list item)."""
    nm = lambda s: sr.norm_map(s)[0].strip()
    texts = [(b['i'], nm(b['text'])) for b in MBL if not b['level']]
    lines = RES[part]['text'].split('\n')
    first = nm(lines[0])
    j = next(k for k, (_i, t) in enumerate(texts) if t == first or t.startswith(first[:60]))
    out = []
    for line in lines:
        ln = nm(line)
        hit = next(k for k in range(j, min(j + 40, len(texts))) if texts[k][1] == ln or (ln and texts[k][1].startswith(ln[:60])))
        out.append(texts[hit][0])
        j = hit + 1
    return out


def window_pieces(part, w):
    """[(block, its words in this window)] for window W, one per line it touches."""
    text = RES[part]['text']
    lines, pos, out = text.split('\n'), 0, []
    lb = line_blocks(part)
    for k, line in enumerate(lines):
        a, b = pos, pos + len(line)
        lo, hi = max(a, w['start_index']), min(b, w['end_index'])
        if lo < hi and text[lo:hi].strip():
            out.append((lb[k], text[lo:hi].strip()))
        pos = b + 1
    return out


def span_in(i, words):
    """The span of WORDS in block i of the working copy (its text equals the master's where no card changed it)."""
    t = br.BL[i]['text']
    nt, idx = sr.norm_map(t)
    nw = sr.norm_map(words)[0].strip()
    k = nt.find(nw)
    if k < 0 or not nw:
        return None
    return {'block': i, 'start': idx[k], 'end': idx[k + len(nw) - 1] + 1}


def short_why(texts):
    t = ' '.join(texts).strip()
    if re.fullmatch(r'(?:[A-Z]\.|\d+\.|[A-Z]\.?)', t):
        return 'A list letter or number on its own line.'
    if t.lower().strip('.()') in ('etc', 'etcetera', 'etc., etc', 'ie', 'yes', 'v', 'tired?'):
        return 'A word or two on its own.'
    return 'A short line of your script or list.'


def add_stretches(covered):
    rows = []
    for part in 'AB':
        for i, w in enumerate(RES[part]['windows']):
            if (kind(w['label']), w['confidence']) == ('Human', 'High') or kind(w['label']) == 'AI':
                continue
            if (part, i) in covered:
                continue
            rows.append((part, i, w, window_pieces(part, w)))
    # windows that share a block go on one card
    groups = []
    for row in rows:
        blocks_ = {b for b, _ in row[3]}
        g = next((g for g in groups if g['blocks'] & blocks_), None)
        if g:
            g['rows'].append(row)
            g['blocks'] |= blocks_
        else:
            groups.append({'rows': [row], 'blocks': set(blocks_)})
    made, missing = 0, []
    for g in groups:
        part, i0 = g['rows'][0][0], g['rows'][0][1]
        spans, reads, texts, whose = [], [], [], set()
        for part_, i, w, pieces in g['rows']:
            for b, words in pieces:
                sp = span_in(b, words)
                if sp is None:
                    missing.append((part_, i, b, words[:50]))
                    continue
                spans.append(sp)
            seg = RES[part_]['text'][w['start_index']:w['end_index']].strip().replace('\n', ' / ')
            texts.append(seg)
            reads.append('%s, %s (%.3f), %d word%s: “%s”' % (kind(w['label']), w['confidence'], w['calibrated_confidence'],
                                                             w['word_count'], '' if w['word_count'] == 1 else 's',
                                                             seg if len(seg) < 140 else seg[:137] + '...'))
        if not spans:
            continue
        short = all(w['word_count'] <= 6 for _p, _i, w, _x in g['rows'])
        sid = 'ED-%s%d' % (part, i0)
        title = re.sub(r'\s+', ' ', texts[0])[:48].rstrip() + ('...' if len(texts[0]) > 48 else '')
        if short:
            why = (short_why(texts) + ' Pangram reads lines this short as human (90 to 99% sure, its "calibrated" number) '
                   'but rarely gives them its top label, so a rewording of the line itself seldom reaches High.')
            note = ('Keep it: it\'s the form of your script or list, and an induction\'s short lines are there on purpose. '
                    'Edit it if you\'d say it differently anyway; I check every edit in your next recheck.')
        else:
            why = ('This reads Human, but at less than High confidence, which a later Pangram version is likeliest to read AI '
                   '(your rule of 26 October). No fix on this page covers it yet.')
            note = ('Your call. Edit it in your own words and I\'ll check your version in the next recheck; or keep it, and '
                    'I\'ll try Emulate\'s re-run on it (batch 482) and bring you a card.')
        br.S.append({'id': sid, 'type': 'short' if short else 'medium', 'title': title, 'advice': 'edit',
                     'reading': 'Your newest check (part %s): ' % part + '; '.join(reads), 'why': why, 'advice_note': note,
                     'keep_label': 'keep it as it is', 'spans': sorted(spans, key=lambda s: (s['block'], s['start'])),
                     'edits': [], 'inserts': [], 'moves': []})
        made += 1
    return made, missing


# ---------------------------------------------------------------- question 23: the audit

AUDIT_FIRST = 'Before accepting a recording or live suggestion, ask:'
EMULATE_CM = (H / 'fix-20261026/b481/cm/HG-audit-list-605.out.txt').read_text(encoding='utf-8').strip()


def add_audit():
    i = next(b['i'] for b in br.BL if b['text'] == AUDIT_FIRST)
    blocks_ = list(range(i, i + 9))
    assert br.BL[blocks_[-1]]['text'].startswith('When an answer is unclear'), br.BL[blocks_[-1]]['text']
    w = next(w for w in RES['B']['windows'] if kind(w['label']) == 'AI')
    br.S.append({
        'id': 'ED-AUDIT', 'type': 'audit', 'title': 'The hypnosis-specific audit', 'advice': 'edit',
        'reading': ('Your newest check (part B): AI, High (%.3f), %d words, from "Before accepting" to "Does the exit '
                    'restore ...", the one AI window in the guide, as in every check since you kept it as a list (your '
                    '2c).' % (w['calibrated_confidence'], w['word_count'])),
        'why': ('Emulate\'s three versions keep four of its seven questions but change what the other three ask. Question 2, '
                '"Can at least one answer lead to pause, modification, full alertness, or stopping?", came back as "Does the '
                'answer help to modify the process so that it allows for me to remain fully alert, or should I stop?"; '
                'question 3, "Does the speaker treat not noticing as secret proof that the process worked?", as "Am I going '
                'to be expected to not be aware of something that they want to be secret proof that they succeeded?"; and '
                'question 6 lost its "hidden claim". Emulate\'s closest version (sample cm), for ideas only (it hasn\'t been '
                'through the gate, and its questions 2, 3 and 6 change what they ask): ' + EMULATE_CM.replace('\n\n', ' / ')),
        'advice_note': ('Your call. Keep it (my default): part B reads Mostly Human with it, and it\'s the one AI stretch. Or '
                        'edit it: your own words for questions 2, 3 and 6 at least, and the rest yours or Emulate\'s closest '
                        'wording above; I check your version in the next recheck.'),
        'keep_label': 'keep the list as it is',
        'spans': [{'block': b, 'start': 0, 'end': len(br.BL[b]['text'])} for b in blocks_ if br.BL[b]['text'].strip()],
        'edits': [], 'inserts': [], 'moves': [],
    })


def cards_md(review):
    """Every card as a page GitHub renders, in the guide's order: the readable copy of the editor page in Git, for an
    account where the page doesn't open (AGENTS.md: an artifact is only a view of a file in Git)."""
    types = review['types']
    out = ['# %s: every card' % review['title'], '',
           'The editor page\'s cards as text, in the order of the guide (`EDITOR-27.json` holds the same, for the scripts). '
           'Built %s from [the guide so far](%s). To answer, use the editor page; or write your answer under a card\'s '
           'number in a message to me.' % (review['built'], review['links']['guide']), '']
    section = None
    for s in review['suggestions']:
        b = (s.get('spans') or [{}])[0].get('block')
        sec = br.BL[b]['section'] if b is not None else None
        if sec != section:
            section = sec
            out += ['## %s' % (sec or 'The opening'), '']
        out += ['### %s: %s (%s)' % (s['id'], s['title'], types[s['type']]['label']), '']
        if s['advice'] == 'edit':
            if s.get('reading'):
                out += ['**Pangram read:** %s' % s['reading'], '']
            out += ['**As it is now:**', ''] + ['> %s' % br.BL[i]['text'] for i in sorted({sp['block'] for sp in s['spans']})] + ['']
            out += ['**Why it\'s here:** %s' % s['why'], '', '**My advice:** %s' % s['advice_note'], '']
            continue
        for e in s.get('edits', []):
            out += ['**Now:**', '', '> %s' % e['before'], '', '**How it would read:**', '', '> %s' % (e['after'] or '(cut)'), '']
        out += ['**Why:** %s' % s['why'], '', '**What stays:** %s' % s['stays'], '',
                '**My advice:** %s' % ((s.get('advice_note') or '') if sr.OWN_ADVICE.match(s.get('advice_note') or '') else
                                       ('Leave it as it is. ' if s['advice'] == 'leave' else 'Approve. ') + (s.get('advice_note') or '')), '']
    return '\n'.join(out).replace('\n\n\n', '\n\n') + '\n'


def main():
    covered = add_cards()
    made, missing = add_stretches(covered)
    add_audit()
    br.S.sort(key=lambda s: (br.first_block(s), br.order_key(s['id'])))
    br.overlaps()
    n = {t: sum(1 for s in br.S if s['type'] == t) for t in TYPES}
    review = {
        'format': sr.FORMAT, 'review_id': 'inner-signal-hypnosis-guide-editor-20261027',
        'title': 'Hypnosis Guide Editor',
        'intro': [
            'This is your hypnosis guide as it is in Git now, with everything you approved, and everything I\'d like you to '
            'look at highlighted where it is. Your newest check (<a href="%s">part A</a>, <a href="%s">part B</a>) gives '
            'every card its reading.' % (FEED['A'], FEED['B']),
            '<b>Emulate\'s fixes</b> (question 21, %d cards): %d read Human at High confidence where they stand, and %d '
            'still read Medium or Low. Click <b>Approve</b>, <b>Reject</b> or <b>Revise</b> on each. Two of them I\'d now '
            'leave (one reads no better than the wording it replaces, the other gains little and loses your ready-to-say '
            'lines); they\'re hidden until you tick "The ones I\'d leave".'
            % (n['held'] + n['raised'] + n['notyet'], n['held'] + n['raised'], n['notyet']),
            '<b>The stretches under High</b> (question 22, %d cards): every other place Pangram read at Medium or Low '
            'confidence, %d of them short lines. Each has <b>Keep</b> and <b>Edit it</b>; Edit opens the paragraph for '
            'you to change in place.' % (n['short'] + n['medium'], n['short']),
            '<b>The audit</b> (question 23, one card, near the end): the one AI stretch, with what Emulate did to it. Keep '
            'it or edit it the same way.',
            'Your answers save as you click. When you\'re done, click <b>Copy my answers</b> (or <b>Save them as a file</b>) '
            'and send them to me; cards you leave unmarked keep my advice only if you say so.',
        ],
        'git_file': GIT_FILE, 'article': {'file': br.ARTICLE, 'sha256': hashlib.sha256(br.MD.encode('utf-8')).hexdigest()},
        # the cards as a page GitHub renders (EDITOR-27.md), never the JSON: he can't read that (his message, 21)
        'links': {'guide': br.BLOB + br.ARTICLE,
                  'review': br.BLOB + 'articles/inner-signal/humanize/fix-20261027/review/EDITOR-27.md'},
        'built': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M UTC'),
        'types': TYPES, 'suggestions': br.S,
    }
    probs = sr.check(review, br.BL)
    for p in probs:
        print('PROBLEM', p)
    (HERE / 'EDITOR-27.json').write_text(json.dumps(review, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    if probs:
        sys.exit(1)
    page = sr.page(review, br.MD, br.BL)
    (HERE / 'EDITOR-27.html').write_text(page, encoding='utf-8')
    (HERE / 'EDITOR-27.artifact.html').write_text(sr.artifact_view(page), encoding='utf-8')
    (HERE / 'EDITOR-27.md').write_text(cards_md(review), encoding='utf-8')
    print(len(br.S), 'cards:', n, '; stretch cards', made, '; pieces not found in the working copy:', len(missing))
    for x in missing:
        print('  not found', x)


if __name__ == '__main__':
    main()
