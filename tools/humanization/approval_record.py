#!/usr/bin/env python3
"""approval_record.py - what Joel approved, revised and rejected on the marking pages, by article and kind of card.

Gate bad-trips-2026-11-07a. Joel, 2026-11-07 12:08 UTC, after approving every card of rounds 12 to 21 of the Bad Trips
guide: "you're asking me to approve things that are clearly good / you should be learning what you actually need to ask my
opinion on, like if meaning might have changed or there's a downside to consider ... make sure you're continuously learning
from what i approve vs what i revise or reject so you have a good understanding of what needs asking".

This reads every answers file his marking pages exported (format joel-suggestion-review-answers-v1, anywhere under
articles/) and takes each card's latest answer. It tallies them by article and type, and lists what he wrote: each card he
revised or rejected, with his comment and his own version, and each comment he left on a card he approved ("didn't need to
ask me for this" was one). A type he has approved every time, ALWAYS_N cards or more and none revised or rejected, is
marked: a card of that type goes to him only when it differs in meaning or downside from the ones he approved.

Nothing is written to a shared file: the record is worked out from the answers files each time, so it is current, and no
two lanes edit it. suggestion_review.py prints the article's record when it checks or builds a page, and names it in the
problem when a card says no "ask_because".

    python3 tools/humanization/approval_record.py                      # every article, type by type
    python3 tools/humanization/approval_record.py --article bad-trips  # one article, with what he wrote
    python3 tools/humanization/approval_record.py --json
"""
import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FORMAT = 'joel-suggestion-review-answers-v1'
DECIDED = ('approved', 'revise', 'rejected')
ALWAYS_N = 5


def answers_files(root=ROOT, article=None):
    """(path, data) for each answers file under articles/ (or one article's folder)."""
    base = root / 'articles' / article if article else root / 'articles'
    if not base.is_dir():
        return
    for f in sorted(base.rglob('*.json')):
        if 'answers' not in f.name.lower():
            continue
        try:
            d = json.loads(f.read_text(encoding='utf-8'))
        except (ValueError, UnicodeDecodeError, OSError):
            continue
        if isinstance(d, dict) and str(d.get('format') or '').startswith(FORMAT) and isinstance(d.get('items'), list):
            yield f, d


def review_cards(folder, rid, cache={}):
    """{card id: card} from the REVIEW*.json beside an answers file whose review_id is RID: answers read from a published
    page's saved decisions carry only ids and answers, so the type and title come from the page's own review."""
    key = (str(folder), rid)
    if key not in cache:
        cards = {}
        for f in sorted(Path(folder).glob('REVIEW*.json')):
            try:
                d = json.loads(f.read_text(encoding='utf-8'))
            except (ValueError, UnicodeDecodeError, OSError):
                continue
            if isinstance(d, dict) and d.get('review_id') == rid and isinstance(d.get('suggestions'), list):
                cards.update({c.get('id'): c for c in d['suggestions'] if isinstance(c, dict)})
        cache[key] = cards
    return cache[key]


def article_of(path, root=ROOT):
    parts = Path(path).relative_to(root).parts
    return parts[1] if len(parts) > 2 and parts[0] == 'articles' else '?'


def latest(root=ROOT, article=None):
    """{(article, review id, card id): the card's latest answer}. An answer beats a later export that shows the card
    pending (an export from a browser that never saw his answer)."""
    best = {}
    for f, d in answers_files(root, article):
        art = article_of(f, root)
        rid = d.get('review_id') or str(f.parent.relative_to(root))
        for it in d['items']:
            if not isinstance(it, dict) or not it.get('id'):
                continue
            key = (art, rid, it['id'])
            when = d.get('exported_at') or max([h.get('at') or '' for h in it.get('history') or [] if isinstance(h, dict)]
                                               or [''])
            new = dict(it, when=when, file=str(f.relative_to(root)), review_id=rid, article=art)
            if not new.get('type') or not new.get('title'):
                card = review_cards(f.parent, rid).get(it['id']) or {}
                new['type'] = new.get('type') or card.get('type')
                new['title'] = new.get('title') or card.get('title')
            old = best.get(key)
            if old is not None:
                od, nd = old.get('status') in DECIDED, it.get('status') in DECIDED
                if od and not nd or od == nd and when <= old['when']:
                    continue
            best[key] = new
    return best


def record(root=ROOT, article=None):
    """{article: {type: {'approved', 'revise', 'rejected', 'pending': counts, 'pushback': [cards he revised or rejected],
    'notes': [cards he approved with a comment]}}}"""
    rec = {}
    keep = ('review_id', 'id', 'title', 'where', 'status', 'comment', 'your_version', 'when')
    for (art, rid, cid), it in sorted(latest(root, article).items()):
        st = it.get('status') if it.get('status') in DECIDED else 'pending'
        e = rec.setdefault(art, {}).setdefault(it.get('type') or '?', {'approved': 0, 'revise': 0, 'rejected': 0,
                                                                        'pending': 0, 'pushback': [], 'notes': []})
        e[st] += 1
        if st in ('revise', 'rejected'):
            e['pushback'].append({k: it.get(k) for k in keep})
        elif st == 'approved' and (it.get('comment') or '').strip():
            e['notes'].append({k: it.get(k) for k in keep})
    return rec


def always_approved(entry):
    """He approved every card of this type: ALWAYS_N or more, none revised or rejected."""
    return entry['approved'] >= ALWAYS_N and not entry['revise'] and not entry['rejected']


def type_line(t, e):
    answered = e['approved'] + e['revise'] + e['rejected']
    s = '%s: %d approved, %d revised, %d rejected' % (t, e['approved'], e['revise'], e['rejected'])
    if e['pending']:
        s += ', %d unanswered' % e['pending']
    if always_approved(e):
        s += ' (all %d approved: ask only when one differs in meaning or downside)' % answered
    return s


def summary(art_rec, types=None):
    """Lines giving his record on one article, type by type (only the given types, if any)."""
    return [type_line(t, e) for t, e in sorted(art_rec.items()) if types is None or t in types]


def clip(s, n=160):
    s = ' '.join((s or '').split())
    return s if len(s) <= n else s[:n - 3] + '...'


def report(rec, detail):
    out = []
    for art in sorted(rec):
        out.append('# %s' % art)
        out += ['  ' + x for x in summary(rec[art])]
        if not detail:
            continue
        for t, e in sorted(rec[art].items()):
            for it in e['pushback']:
                out.append('  %s %s, %s %s: %s' % (it['status'].upper(), t, it['review_id'], it['id'], clip(it['title'], 80)))
                if (it.get('comment') or '').strip():
                    out.append('      his comment: "%s"' % clip(it['comment']))
                if (it.get('your_version') or '').strip():
                    out.append('      his version: "%s"' % clip(it['your_version']))
            for it in e['notes']:
                out.append('  APPROVED with a comment, %s, %s %s: "%s"' % (t, it['review_id'], it['id'], clip(it['comment'])))
    return out


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--article', help="an article's folder name under articles/ (shows what he wrote, too)")
    ap.add_argument('--detail', action='store_true', help='show what he wrote for every article')
    ap.add_argument('--json', action='store_true')
    a = ap.parse_args(argv)
    rec = record(ROOT, a.article)
    if a.json:
        print(json.dumps(rec, indent=1, ensure_ascii=False))
        return 0
    if not rec:
        print('no answers files found')
        return 0
    print('\n'.join(report(rec, a.detail or bool(a.article))))
    return 0


if __name__ == '__main__':
    sys.exit(main())
