"""CHANGED.json for part B's recheck (2026-10-23, after Joel's message of 18:13 UTC): each edit of batches 476 and 477
(../../fix-20261020/EDITS41.json) whose words are in part B's checked text (TEXT-B.txt), as the stretch around its
change, with my chance that it reads red. part_forecast.py adds each one's neighbours itself (gate E249).

  python3 articles/inner-signal/humanize/fix-20261023/recheck-b2/make_changed_b.py   (after make_recheck.py)
"""
import difflib, json, pathlib, re, sys

X = pathlib.Path(__file__).resolve().parent
REPO = X.parents[4]
sys.path.insert(0, str(REPO / 'tools' / 'humanization'))
import substack_check_text as C  # noqa: E402

EDITS = REPO / 'articles/inner-signal/humanize/fix-20261020/EDITS41.json'
CHANCE = {'476': (0.02, 'a spelling fix in a paragraph that read Human (no Pangram check for spelling, Joel 2026-10-06)'),
          '477': (0.25, "Emulate's sample br for the Low red of recheck B (\"You don’t have to fix this. I’m here now.\"); "
                        "Emulate splices have read Human in place most times, and this one joins three short sentences "
                        "into two")}


def plain(md):
    md = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', md)
    return re.sub(r'[*_]{1,2}([^*_]+)[*_]{1,2}', r'\1', md)


def stretch(text, old, new, pad=45):
    """The part of NEW around where it differs from OLD, widened until it occurs once in TEXT."""
    o, n = C.smart(plain(old)), C.smart(plain(new))
    sm = difflib.SequenceMatcher(None, o, n, autojunk=False)
    ops = [op for op in sm.get_opcodes() if op[0] != 'equal']
    a, b = ops[0][3], ops[-1][4]
    for p in range(pad, len(n) + pad, 15):
        s = n[max(0, a - p):min(len(n), b + p)].strip()
        s = s[s.find(' ') + 1:] if max(0, a - p) > 0 else s
        s = s[:s.rfind(' ')] if min(len(n), b + p) < len(n) else s
        if len(s) >= 20 and text.count(s) == 1:
            return s
    return None


def main():
    text = (X / 'TEXT-B.txt').read_text(encoding='utf-8')
    out, missing = [], []
    for e in json.loads(EDITS.read_text(encoding='utf-8')):
        b = str(e.get('batch'))
        if b not in CHANCE:
            continue
        s = stretch(text, e['old'], e['new'])
        if s is None:
            missing.append(e['key'])
            continue
        chance, why = CHANCE[b]
        out.append({'name': '%s (batch %s): %s' % (e['key'], b, e['source'][:60]), 'text': s, 'chance_red': chance, 'why': why})
    # the red he chose to keep (his answer 2c of 2026-10-23: the hypnosis audit stays a list of seven questions), read
    # High in recheck B (window 14) and unchanged since
    last = json.loads((X.parent / 'recheck' / 'RESULT-B.json').read_text(encoding='utf-8'))
    w = last['windows'][14]
    kept = last['text'][w['start_index']:w['end_index']].strip()
    assert str(w['label']).startswith('AI') and kept.startswith('Before accepting a recording') and text.count(kept) == 1
    out.append({'name': 'kept red by his 2c: Appendix C\'s hypnosis audit questions', 'text': kept, 'chance_red': 0.9,
                'why': 'read AI, High, in recheck B, unchanged since; it stays a list by his answer 2c'})
    (X / 'CHANGED.json').write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print('%d changed stretches in part B; not in part B (part A or gone): %s' % (len(out), ', '.join(missing) or 'none'))


if __name__ == '__main__':
    main()
