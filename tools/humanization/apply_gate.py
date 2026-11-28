#!/usr/bin/env python3
"""apply_gate.py - a paragraph of mine goes into an article only when a check of it by itself read Human High in every
window (gate bad-trips-2026-11-12l), unless it is a content change he approved (card C04, below).

Joel, 2026-11-12 22:34 UTC, after I put Active Seizure's rescue medicine paragraph into his guide because it read Human
Written in its section, two of its windows Low and the same paragraph AI Detected, 79% by itself: "btw the rule says we
can't pass paragraphs that read AI on their own, even if they read well in the section (unless the reason is they are
referencing something that would make sense only in the section and that's why it likely makes no sense to pangram). i
guess you need to stop passing over anything that's not human high because you're not learning." He fixed the paragraph
himself ("it was super obvious stuff just clarifying and reducing redundancy, now human high").

So for each paragraph of mine about to go in, the ledger must hold a check (a prediction with its result) whose text
holds the paragraph's words, whose scope is the paragraph by itself (paragraph, pair for one under 50 words with its
neighbour, sentence, or heading with its paragraph), and whose every window is Human at High confidence. A section or
stretch check counts only with --section-ok REASON, the case he named: the paragraph points to something only its
section has, which is why it can't make sense to Pangram alone. Nothing below Human High passes, Medium included: a
window short of High is mine to fix, not to pass on to him. His own versions don't go through this gate; they are his.

Rules audit 2026-11-28, card C04 (approved): a text that is a content change he approved (his own words, or a card he
approved) goes in without the Human High check, recorded with what he approved and where; the paragraph's humanizing
follows as its own work. Apply scripts pass owner_approved={"card": ..., "words": ..., "where": ...} (or --owner-card,
--owner-words, --owner-where on the command line); all three are required, so a bare claim doesn't pass. Everything else
is as above.

  python3 tools/humanization/apply_gate.py LEDGER --text "PARAGRAPH" [--text ...] [--file PARA.txt ...] [--section-ok REASON]
      [--owner-card CARD --owner-words "HIS WORDS" --owner-where "ANSWERS FILE, turn"]

As a module: ok, lines = check(recs, paragraph, section_ok=None, owner_approved=None); require(ledger, paragraphs,
section_ok=None, owner_approved=None) exits with
the reasons when any paragraph has no such check.
"""
import argparse, pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import pangram_ledger as PL  # noqa: E402

ALONE = ('paragraph', 'pair', 'sentence', 'heading')
IN_SECTION = ('section', 'stretch')


def plain(s):
    """The words as typed into Pangram: Markdown links as their words, no bold or italic marks, quotes and spaces made
    plain."""
    s = re.sub(r'!\[[^\]]*\]\([^)]*\)', '', s or '')
    s = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', s)
    s = s.replace('**', '').replace('__', '')
    s = re.sub(r'(?<![\w*])\*(?=\S)([^*\n]+?)(?<=\S)\*(?![\w*])', r'\1', s)
    s = re.sub(r'^#{1,6}\s+', '', s, flags=re.M)
    return PL._norm(s)


def windows(result):
    out = []
    for w in (result or {}).get('windows') or []:
        if isinstance(w, dict):
            out.append((w.get('label') or '', w.get('confidence') or '', w.get('words')))
    return out


def all_high(ws):
    # a window's label is "Human" from the web app's reader and "Human Written" from the API (pangram_api.py); until
    # 2026-11-25 this took only the first, so every text checked through the API failed the gate, Human High 118 in one
    # window included (lesson bad-trips-2026-11-25e; lane_push.py's boundary gate had the same slip, lesson
    # bad-trips-2026-11-24f)
    return bool(ws) and all(l in ('Human', 'Human Written') and c == 'High' for l, c, _ in ws)


def owner_record(owner_approved):
    """The line recording a content change he approved, or None when OWNER_APPROVED is None. Raises ValueError when the
    card, his words or where he said them is missing."""
    if not owner_approved:
        return None
    got = {k: str(owner_approved.get(k) or '').strip() for k in ('card', 'words', 'where')}
    gone = [k for k, v in got.items() if not v]
    if gone:
        raise ValueError('owner_approved needs the card, his words and where (missing: %s)' % ', '.join(gone))
    return ('in without the Human High check: a content change he approved, card %(card)s, his words "%(words)s", at '
            '%(where)s (rules audit 2026-11-28, card C04); the paragraph\'s humanizing follows as its own work' % got)


def check(recs, paragraph, section_ok=None, owner_approved=None):
    """(ok, lines): ok when a check of PARAGRAPH by itself (or, with SECTION_OK, in its section) read Human High in every
    window, or when OWNER_APPROVED ({"card", "words", "where"}) says he approved it as a content change; lines say which
    checks were found and why each does or doesn't count."""
    want = plain(paragraph)
    if not want:
        return False, ['an empty paragraph']
    # Rules audit 2026-11-28, card C04 (approved): a content change he approved goes in at once, recorded
    rec = owner_record(owner_approved)
    if rec:
        return True, [rec]
    lines, ok = [], False
    for p in PL.state(recs).values():
        if p['void'] or not p['result'] or want not in plain(p.get('text') or ''):
            continue
        scope, ws = p.get('scope'), windows(p['result'])
        link = p['result'].get('link') or p['id']
        read = ', '.join('%s %s %s' % (l, c, n) for l, c, n in ws) or 'no windows recorded'
        if all_high(ws) and scope in ALONE:
            ok = True
            lines.append('counts: %s (%s, by itself): %s' % (link, scope, read))
        elif all_high(ws) and scope in IN_SECTION and (section_ok or '').strip():
            ok = True
            lines.append('counts with --section-ok (%s): %s (%s): %s' % (section_ok.strip(), link, scope, read))
        elif all_high(ws):
            lines.append('not by itself: %s (%s): %s' % (link, scope, read))
        else:
            lines.append('not Human High: %s (%s): %s' % (link, scope, read))
    if not lines:
        lines.append('no check in the ledger holds these words')
    return ok, lines


def require(ledger, paragraphs, section_ok=None, owner_approved=None):
    recs = PL.read(ledger)
    bad = []
    for para in paragraphs:
        ok, lines = check(recs, para, section_ok, owner_approved)
        if ok and owner_approved:
            print('apply_gate: %s: %s' % (plain(para)[:60], lines[0]))
        if not ok:
            bad.append('"%s": %s' % (plain(para)[:90] + ('...' if len(plain(para)) > 90 else ''), '; '.join(lines)))
    if bad:
        raise SystemExit('apply_gate: not in until a check of it by itself reads Human High in every window (gate '
                         'bad-trips-2026-11-12l; Joel, 2026-11-12 22:34 UTC: "stop passing over anything that\'s not human '
                         'high because you\'re not learning"):\n  ' + '\n  '.join(bad))
    return True


def main():
    ap = argparse.ArgumentParser(description=__doc__.split('\n\n')[0])
    ap.add_argument('ledger')
    ap.add_argument('--text', action='append', default=[])
    ap.add_argument('--file', action='append', default=[])
    ap.add_argument('--section-ok', default=None)
    ap.add_argument('--owner-card', default=None, help='the card he approved (with --owner-words and --owner-where): these '
                    'texts are a content change of his, in without the Human High check (card C04)')
    ap.add_argument('--owner-words', default=None, help='his words approving it')
    ap.add_argument('--owner-where', default=None, help='where he said them: answers file and turn')
    a = ap.parse_args()
    owner = {'card': a.owner_card, 'words': a.owner_words, 'where': a.owner_where} if (
        a.owner_card or a.owner_words or a.owner_where) else None
    if owner:
        try:
            owner_record(owner)
        except ValueError as e:
            raise SystemExit('apply_gate: %s' % e)
    paras = list(a.text) + [pathlib.Path(f).read_text(encoding='utf-8') for f in a.file]
    if not paras:
        raise SystemExit('give the paragraphs of mine that are to go in, with --text or --file')
    recs = PL.read(a.ledger)
    bad = 0
    for para in paras:
        ok, lines = check(recs, para, a.section_ok, owner)
        bad += not ok
        print(('PASS' if ok else 'FAIL'), plain(para)[:80])
        for line in lines:
            print('   ', line)
    print('verdict:', 'PASS' if not bad else 'FAIL (%d of %d)' % (bad, len(paras)))
    sys.exit(1 if bad else 0)


if __name__ == '__main__':
    main()
