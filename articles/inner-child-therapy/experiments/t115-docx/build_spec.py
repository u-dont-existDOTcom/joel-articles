#!/usr/bin/env python3
"""Turn 115: the docx Joel asked for (2026-10-26 12:24 UTC: "then whatever remains you can just give me as highlighted in a
docx so i can see what to work on directly"), as a spec that build_docx.js turns into the .docx.

The body is the whole guide as round 8 read it: the two Substack payloads (experiments/t114-substack/PAYLOAD-A.html and
-B.html), each line rebuilt the way the check read it (record_round8.py's quote rule, checked against the page's SHA-256
here too), so every window of round 8 lands on exactly the words it covered. On that body:
  - the pass (experiments/t115-pass/fixes.py) shows as tracked changes, each with a comment: the window it answers, the
    tell, what it keeps and drops, and the check of the changed block (experiments/t115-api/BLOCK-RESULTS.json);
  - every window round 8 read below Human with High confidence is shaded by kind, except in a paragraph the pass changed,
    where the changed block's own check decides what is shaded; each has a comment with its reading, round 6's reading of
    the same words and whose words they are (WHOSE.json; seams of three words or fewer are shaded gray with no comment);
  - the one suggestion (SUGGEST in fixes.py) is a comment on its words.
Track Changes is on in the file (build_docx.js), so whatever Joel types shows as his.

  build_spec.py      writes SPEC.json beside this file"""
import difflib
import hashlib
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
EXP = HERE.parent
ROOT = HERE.parents[3]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import substack_check_text as S  # noqa: E402
from paragraphs_alone import plain  # noqa: E402
from bs4 import BeautifulSoup, NavigableString, Tag  # noqa: E402

NOTE_URL = 'https://substack.com/profile/355021294-u-dont-existcom/note/c-349048098'
NOTE_LINE = ('wow, so true. it’s hard to trust people who trust people that dirsepect [or distrust] you… although, it matters '
             'that they know those people disrespect/distrust you, as well as whether the disrespect or distrust is earned or '
             'unearned, as well as how granular it is… like i don’t trust most people to tell me what i need to change about '
             'myself and be accurate and kind in that, but that doesn’t mean i don’t trust them in other ways. And i’d directly '
             'ask them why they trust those people who disrespect/distrust me?')
FIXES = json.loads((EXP / 't115-pass' / 'FIXES.json').read_text(encoding='utf-8'))
WIN = {(w['half'], w['start'], w['end']): w for w in json.loads((EXP / 't115-results' / 'WINDOWS.json').read_text(encoding='utf-8'))['items']}
_api = EXP / 't115-api' / 'BLOCK-RESULTS.json'
API = json.loads(_api.read_text(encoding='utf-8')) if _api.exists() else {'fixes': {}}
WHOSE = json.loads((HERE / 'WHOSE.json').read_text(encoding='utf-8'))
SHADE = {'AI': 'F4A6A6', 'Low': 'FFD966', 'Medium': 'BDD7EE', 'Nearly': 'E2ECF7', 'Seam': 'E4E4E4'}


def sha(s):
    return hashlib.sha256(s.encode('utf-8')).hexdigest()


def curl(s):
    keep = S.OPEN2
    S.OPEN2 = re.compile(r'(^|[\s\[{‘-])"')      # round 8's paste, as record_round8.py has it
    try:
        return S.smart(s)
    finally:
        S.OPEN2 = keep


def payload_blocks(half):
    """('h', level, text), ('p', raw, breaks) or ('note',) for each block of the payload, in order."""
    soup = BeautifulSoup((EXP / 't114-substack' / ('PAYLOAD-%s.html' % half)).read_text(encoding='utf-8'), 'html.parser')
    body = soup.find('div', class_='body') or soup
    out = []
    for el in body.children:
        if not isinstance(el, Tag):
            continue
        if el.name in ('h1', 'h2', 'h3', 'h4', 'h5', 'h6'):
            out.append(('h', int(el.name[1]), el.get_text().strip()))
            continue
        assert el.name == 'p', el.name
        raw, breaks = '', []
        for c in el.children:
            if isinstance(c, NavigableString):
                raw += str(c)
            elif c.name == 'br':
                breaks.append(len(raw))
            else:
                raw += c.get_text()
        if re.fullmatch(r'https?://\S+', raw.strip()):
            assert raw.strip() == NOTE_URL
            out.append(('note',))
            continue
        raw = raw.rstrip(' ')
        if raw.strip():
            out.append(('p', raw, breaks))
    return out


def checked(raw):
    """The paragraph curled as the post shows it, and that text without the emoji joiners (the checked line). The two
    differ only where a joiner was dropped; the docx shows the curled text, so its emoji stay whole."""
    c = curl(raw)
    return c, c.replace('‍', '').replace('️', '')


def kind_of(label, conf, cal, words):
    if words <= 3 and label == 'Human':
        return 'Seam'
    if label.startswith('AI'):
        return 'AI'
    if conf == 'Low':
        return 'Low'
    return 'Nearly' if (cal or 0) >= 0.985 else 'Medium'


def trim(old, new):
    """Split two strings into a common word prefix, the differing middles and a common word suffix."""
    ow, nw = old.split(' '), new.split(' ')
    p = 0
    while p < min(len(ow), len(nw)) and ow[p] == nw[p]:
        p += 1
    s = 0
    while s < min(len(ow), len(nw)) - p and ow[-1 - s] == nw[-1 - s]:
        s += 1
    pre = ' '.join(ow[:p]) + (' ' if p else '')
    return pre, ' '.join(ow[p:len(ow) - s]), ' '.join(nw[p:len(nw) - s])


def sentences(s):
    """The sentences of s, each with the spaces after it, so that they join back to s exactly."""
    out, start = [], 0
    for m in re.finditer(r'(?<=[.!?…])[”"’)]*\s+', s):
        out.append(s[start:m.end()])
        start = m.end()
    if start < len(s):
        out.append(s[start:])
    assert ''.join(out) == s
    return out


def word_diff(o, n, tag):
    ot, nt = re.findall(r'\S+\s*', o), re.findall(r'\S+\s*', n)
    out = []
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, ot, nt, autojunk=False).get_opcodes():
        if op == 'equal':
            out.append([''.join(ot[i1:i2]), 'keep', None])
        if op in ('delete', 'replace'):
            out.append([''.join(ot[i1:i2]), 'del', tag])
        if op in ('insert', 'replace'):
            out.append([''.join(nt[j1:j2]), 'ins', tag])
    return out


def sentence_diff(o, n, tag):
    """A readable tracked change: sentences that stay are kept; a changed sentence that pairs with a new one (most of its
    words shared) shows its word changes when there are at most two; anything else is struck and inserted whole."""
    os_, ns = sentences(o), sentences(n)
    out = []
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, os_, ns, autojunk=False).get_opcodes():
        if op == 'equal':
            out.append([''.join(os_[i1:i2]), 'keep', None])
            continue
        olds, news = os_[i1:i2], ns[j1:j2]
        j = 0
        for x in olds:
            k = next((k for k in range(j, len(news)) if difflib.SequenceMatcher(None, x.split(), news[k].split()).ratio() >= 0.5), None)
            if k is None:
                out.append([x, 'del', tag])
                continue
            out += [[y, 'ins', tag] for y in news[j:k]]
            wd = word_diff(x, news[k], tag)
            regions = sum(1 for i, w in enumerate(wd) if w[1] != 'keep' and (i == 0 or wd[i - 1][1] == 'keep'))
            out += wd if regions <= 2 else [[x, 'del', tag], [news[k], 'ins', tag]]
            j = k + 1
        out += [[y, 'ins', tag] for y in news[j:]]
    return [w for w in out if w[0]]


class Doc:
    def __init__(self):
        self.blocks, self.comments = [], []

    def comment(self, text):
        self.comments.append({'id': len(self.comments) + 1, 'text': text})
        return len(self.comments)


def window_note(wm):
    r6 = wm['round6_text'] if wm['round6_text'] != 'not in round 6 as it is now' else 'these words weren\'t there in round 6'
    kd = kind_of(wm['label'], wm['confidence'], wm['calibrated_confidence'], wm['words'])
    whose = WHOSE.get(wm['id']) or ('Mine. I left it: nearly High (0.985 or more).' if kd == 'Nearly' else
                                    'Mine. I found no tell I could take out here without losing something; I left it.')
    lab = 'AI' if wm['label'].startswith('AI') else 'Human'
    return 'Round 8: %s, %s confidence (%.3f). Round 6, same words: %s. %s' % (lab, wm['confidence'], wm['calibrated_confidence'] or 0, r6, whose)


def fix_note(f):
    v = API['fixes'].get(f['id'], {})
    head = {'cut': 'My pass: a cut, nothing added.', 'reword': 'My pass: its point said plainly.'}[f['kind']]
    return '%s Round 8 read: %s. The tell: %s. It keeps %s; it drops %s. %s' % (
        head, f['windows'], f['tells'], f['keeps'], f['loses'], v.get('summary', 'Its block is not checked yet.'))


def suggest_note(s):
    cut = [x for x in curl(plain(s['old'])).split('. ') if x and x + '.' not in curl(plain(s['new'])) and x not in curl(plain(s['new']))]
    return ('A suggestion only, since you approved this paragraph as it is. Round 8 read: %s. The tell: %s. The cut: "%s" '
            '(nothing added). It keeps %s.' % (s['windows'], s['tells'], '. '.join(cut).rstrip('.') + '.', s['keeps']))


def paragraph(doc, half, c, line, ls, R, breaks):
    """The runs of one paragraph: tracked changes for the pass's fixes in it, shading and comments for the rest."""
    fixes = [f for f in FIXES['fixes'] if curl(plain(f['old'])) in c]
    suggs = [s for s in FIXES['suggest'] if curl(plain(s['old'])) in c]
    # segments of the curled paragraph: [text, 'keep'|'del'|'ins', fix id], the fix as a word-level diff
    assert len(fixes) <= 1, [f['id'] for f in fixes]
    segs = [[c, 'keep', None]]
    for f in fixes:
        o, n = curl(plain(f['old'])), curl(plain(f['new']))
        at = c.index(o)
        mid = sentence_diff(o, n, f['id'])
        segs = [s for s in [[c[:at], 'keep', None]] + mid + [[c[at + len(o):], 'keep', None]] if s[0]]
        assert ''.join(t for t, kd, _ in segs if kd != 'ins') == c, f['id']
    changed = bool(fixes)
    # spans [a, e) with a kind and a comment, in old coordinates (unchanged paragraph) or new coordinates (changed one)
    spans = []
    if not changed:
        joiners = [i for i, ch in enumerate(c) if ch in '‍️']

        def to_c(j):            # a checked-line index to an index in the curled paragraph
            for i in joiners:
                if i <= j:
                    j += 1
            return j
        for w in R['windows']:
            if w['label'] == 'Human' and w['confidence'] == 'High':
                continue
            a, e = max(w['start'], ls) - ls, min(w['end'], ls + len(line)) - ls
            if a >= e or not line[a:e].strip():
                continue
            wm = WIN[(half, w['start'], w['end'])]
            a2 = a + len(line[a:e]) - len(line[a:e].lstrip())
            e2 = e - (len(line[a:e]) - len(line[a:e].rstrip()))
            kd = kind_of(wm['label'], wm['confidence'], wm['calibrated_confidence'], wm['words'])
            spans.append([to_c(a2), to_c(e2 - 1) + 1, kd, None if kd == 'Seam' else window_note(wm)])
    else:
        for f in fixes:
            for a, e, label, conf, cal, words in API['fixes'].get(f['id'], {}).get('para_windows', []):
                kd = kind_of(label, conf, cal, words)
                spans.append([a, e, kd, '%s, the check of its block after the change: %s, %s confidence (%.3f) here.' % (f['id'], label, conf, cal or 0)])
    # runs
    runs, pos_old, pos_new = [], 0, 0
    fix_c = {f['id']: doc.comment(fix_note(f)) for f in fixes}
    span_c = {}
    for t, kd, tag in segs:
        if kd == 'del':
            runs.append({'t': t, 'del': True, 'fix': tag})
            pos_old += len(t)
            continue
        base = pos_new if changed else pos_old
        cuts = {0, len(t)}
        for a, e, _, _ in spans:
            cuts |= {x - base for x in (a, e) if 0 < x - base < len(t)}
        if kd == 'keep':
            cuts |= {b - pos_old for b in breaks if 0 < b - pos_old < len(t)}
        for i0, i1 in zip(sorted(cuts), sorted(cuts)[1:]):
            run = {'t': t[i0:i1]}
            if kd == 'ins':
                run['ins'], run['fix'] = True, tag
            if kd == 'keep' and pos_old + i0 in breaks:
                run['br_before'] = True
            g0, g1 = base + i0, base + i1
            for n, (a, e, sk, note) in enumerate(spans):
                if a <= g0 < e:
                    run['shade'] = SHADE[sk]
                    if note and n not in span_c:
                        span_c[n] = doc.comment(note)
                        run.setdefault('cstart', []).append(span_c[n])
                    if note and g1 >= e:
                        run.setdefault('cend', []).append(span_c[n])
            runs.append(run)
        if kd == 'keep':
            pos_old += len(t)
        pos_new += len(t)
    for fid, cid in fix_c.items():
        tracked = [i for i, r in enumerate(runs) if r.get('fix') == fid]
        runs[tracked[0]].setdefault('cstart', []).insert(0, cid)
        runs[tracked[-1]].setdefault('cend', []).append(cid)
    for s in suggs:
        o = curl(plain(s['old']))
        runs = anchor(runs, c.index(o), c.index(o) + len(o), doc.comment(suggest_note(s)))
    for r in runs:
        r.pop('fix', None)
    return runs


def anchor(runs, a, e, cid):
    """Split an unchanged paragraph's runs so that comment cid spans [a, e)."""
    out, pos = [], 0
    for r in runs:
        t = r['t']
        cuts = sorted({0, len(t)} | {x - pos for x in (a, e) if 0 < x - pos < len(t)})
        for i0, i1 in zip(cuts, cuts[1:]):
            r2 = dict(r, t=t[i0:i1])
            for k in ('cstart', 'cend', 'br_before'):
                r2.pop(k, None)
            if i0 == 0:
                for k in ('cstart', 'br_before'):
                    if r.get(k):
                        r2[k] = list(r[k]) if isinstance(r[k], list) else r[k]
            if i1 == len(t) and r.get('cend'):
                r2['cend'] = list(r['cend'])
            if pos + i0 == a:
                r2.setdefault('cstart', []).append(cid)
            if pos + i1 == e:
                r2.setdefault('cend', []).append(cid)
            out.append(r2)
        pos += len(t)
    return out


KEY = [
    'This is the whole guide as round 8 read it (your two Pangram links of today), with my pass in it and every spot still below Human, high confidence marked. Track Changes is on, so anything you type shows as yours.',
    'My pass is here as tracked changes, proposals until you decide: accept or reject each one (any you leave as it is, I\'ll take as accepted). Each has a comment with the window it answers, the tell, what it keeps and drops, and the check of its block after the change.',
    'The shaded spots are the windows round 8 read below Human, high that my pass didn\'t change. Each has a comment with its reading, round 6\'s reading of the same words, and whose words they are.',
    'RED: AI. AMBER: Human, Low. BLUE: Human, Medium. PALE BLUE: Human, Medium but nearly High (0.985 or more). GRAY: a seam, three words or fewer where the detector changed its mind between two stretches; usually nothing to fix, so no comment.',
    'When you\'re done, send me the docx back. I\'ll put in what you accepted and wrote, and then the next whole-guide check reads all of it.',
]


def main():
    doc = Doc()
    for half in 'AB':
        R = json.loads((EXP / 't115-results' / ('RESULT-%s.json' % half)).read_text(encoding='utf-8'))
        seq = payload_blocks(half)
        lines, items = [], []
        for b in seq:
            if b[0] == 'p':
                c, line = checked(b[1])
                lines.append(line)
                items.append((b, c, line))
            elif b[0] == 'note':
                lines.append(NOTE_LINE)
                items.append((b, NOTE_LINE, NOTE_LINE))
            else:
                items.append((b, None, None))
        assert sha('\n'.join(lines)) == sha(R['text']), (half, 'the rebuilt text is not the checked text')
        pos, k = 0, 0
        for b, c, line in items:
            if b[0] == 'h':
                doc.blocks.append({'type': 'h', 'level': b[1], 'runs': [{'t': b[2]}]})
                continue
            ls = pos
            pos += len(line) + 1
            if b[0] == 'note':
                doc.blocks.append({'type': 'p', 'quote': True, 'runs': [{'t': 'An embedded note of yours: ' + c, 'i': True}]})
                continue
            doc.blocks.append({'type': 'p', 'runs': paragraph(doc, half, c, line, ls, R, b[2])})
    spec = {'title': 'Inner Child Therapy: the spots below Human, high (round 8)', 'key': KEY, 'blocks': doc.blocks,
            'comments': doc.comments, 'author': 'Claude', 'date': '2026-10-26T14:00:00Z', 'shade': SHADE}
    (HERE / 'SPEC.json').write_text(json.dumps(spec, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    n_ins = sum(1 for b in doc.blocks for r in b['runs'] if r.get('ins'))
    n_del = sum(1 for b in doc.blocks for r in b['runs'] if r.get('del'))
    shaded = sum(1 for b in doc.blocks for r in b['runs'] if r.get('shade'))
    print('blocks %d, comments %d, inserted runs %d, deleted runs %d, shaded runs %d' % (len(doc.blocks), len(doc.comments), n_ins, n_del, shaded))


if __name__ == '__main__':
    main()
