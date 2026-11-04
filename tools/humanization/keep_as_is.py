#!/usr/bin/env python3
"""keep_as_is.py - what Joel has said stays as it is in an article (a joke, a coinage, a word he meant, a device), and the
cuts he meant, kept in Git so no later pass flags, "fixes" or puts them back.

Lesson E340. On the turn-116 marking page I asked whether "As Lao Tsu might have said (if I could ever have
read that whole boring Art of War book)" should name Sun Tzu. Joel, 2026-11-03 23:32 UTC: "that's the joke yeah you
forgot. i guess you need to somehow keep track of the jokes in an article more durably, add that as one of the rules in
the repo, how to durably keep track of stuff you'd otherwise flag in an article". A joke, a word he chose ("I might be
asking", where I'd have written "you"), a sentence that runs on into its heading, a name changed on purpose ("X"): each
looks like something to fix to a reader who doesn't know, and every new pass, chat or account is that reader. A ruling
that lives only in a chat is asked again.

The article's KEEP-AS-IS.json, next to its Markdown:
  {"format": "joel-keep-as-is-v1", "article": its Markdown,
   "keep": [{"id", "kind" (joke, voice, coinage, spelling, device, choice, placement, spacing), "quote": the exact words
             (found in the article, quote marks and no-break spaces aside), "what": why it looks like something to fix and
             why it isn't, "joel": his words, or "", "when", "where": the card or message, "basis": "his answer", "his
             approval of a card that kept it", or "my reading, not asked" (a judgment, marked as one)}],
   "cuts": [{"id", "quote": words from the cut text, "what", "joel", "when", "where", "basis"}]}   cuts he meant: no
             suggestion puts them back.

Who checks it:
  - suggestion_review.py check (every marking page): a card that highlights or changes kept words, or puts a meant cut
    back, is refused unless the card says why in "keep_ack" (he asked to change it after all);
  - render_article_so_far.py (every turn's article page): a kept quote that is gone from the article, or a meant cut
    that is back, goes in a red box at the top, and the render exits 1;
  - any script that flags things: kept(article, words) before it flags.

  python3 tools/humanization/keep_as_is.py check ARTICLE.md        # kept words all there, no meant cut back
  python3 tools/humanization/keep_as_is.py is-kept ARTICLE.md "words"   # exit 0 if the words are kept (or a meant cut)
  python3 tools/humanization/keep_as_is.py list ARTICLE.md
"""
import argparse
import json
import pathlib
import re
import sys

FILE = 'KEEP-AS-IS.json'
FORMAT = 'joel-keep-as-is-v1'
KINDS = {'joke', 'voice', 'coinage', 'spelling', 'device', 'choice', 'placement', 'spacing'}
STRAIGHT = str.maketrans({'‘': "'", '’': "'", '“': '"', '”': '"', '«': '"', '»': '"', '\xa0': ' '})


def norm(s):
    """Words as a reader sees them: no comments, links and bold as plain text, straight quote marks, one space."""
    s = re.sub(r'<!--.*?-->', ' ', s, flags=re.S)
    s = re.sub(r'\[([^\[\]]*)\]\s?\([^()\s]*(?:\([^()\s]*\))?[^()\s]*\)', r'\1', s)
    s = s.replace('**', '').translate(STRAIGHT)
    s = re.sub(r'"\s+', '"', s)
    s = re.sub(r'\s+"(?=[\s.,;:!?)]|$)', '"', s)
    return re.sub(r'\s+', ' ', s).strip()


def path_for(article):
    """The ledger of the article family ARTICLE is in: the nearest KEEP-AS-IS.json up to its folder under articles/."""
    d = pathlib.Path(article).resolve().parent
    for p in [d] + list(d.parents):
        if (p / FILE).exists():
            return p / FILE
        if p.parent.name == 'articles':
            break
    return d / FILE


def load(article):
    """The article's ledger ({"keep": [], "cuts": []} when it has none)."""
    p = path_for(article)
    if not p.exists():
        return {'format': FORMAT, 'keep': [], 'cuts': []}
    led = json.loads(p.read_text(encoding='utf-8'))
    if led.get('format') != FORMAT:
        raise SystemExit('%s: not a %s file' % (p, FORMAT))
    return led


def problems(led):
    """What is wrong with the ledger itself: [message]."""
    out, ids = [], set()
    for part in ('keep', 'cuts'):
        for e in led.get(part, []):
            i = e.get('id') or '?'
            if i in ids:
                out.append('%s: id used twice' % i)
            ids.add(i)
            for k in ('quote', 'what', 'when', 'where', 'basis'):
                if not (e.get(k) or '').strip():
                    out.append('%s: no %s' % (i, k))
            if part == 'keep' and e.get('kind') not in KINDS:
                out.append('%s: kind must be one of %s' % (i, ', '.join(sorted(KINDS))))
    return out


def missing(md, led):
    """Kept entries whose words are no longer in the article (a placement's, in the article with its notes: a video is
    an EMBED note)."""
    text = norm(md)
    return [e for e in led.get('keep', []) if (e['quote'] not in md if e.get('kind') == 'placement' else norm(e['quote']) not in text)]


def back(md, led):
    """Meant cuts whose words are in the article again."""
    text = norm(md)
    return [e for e in led.get('cuts', []) if norm(e['quote']) in text]


def kept(words, led):
    """The entries (kept words or meant cuts) that WORDS fall inside or cover: before flagging WORDS, check this."""
    w = norm(words)
    if not w:
        return []
    return [e for e in led.get('keep', []) + led.get('cuts', []) if w in norm(e['quote']) or norm(e['quote']) in w]


ONE = str.maketrans({'‘': "'", '’': "'", '“': '"', '”': '"', '«': '"', '»': '"', '\xa0': ' '})   # one character for one


def ranges(text, led):
    """[(start, end, entry)]: where each kept quote is in TEXT (a block's plain text), quote marks and no-break spaces
    aside, offsets in TEXT."""
    t = text.translate(ONE)
    out = []
    for e in led.get('keep', []):
        q = e['quote'].translate(ONE)
        k = t.find(q)
        while k >= 0:
            out.append((k, k + len(q), e))
            k = t.find(q, k + 1)
    return out


def card_problems(card, block_texts, led):
    """A marking-page card that highlights words inside kept ones, changes kept words, or puts a meant cut back:
    [message]. BLOCK_TEXTS[i] is block i's text. A card with "keep_ack" (why he wants it changed after all) passes."""
    if card.get('keep_ack') or not (led.get('keep') or led.get('cuts')):
        return []
    sid, out = card.get('id', '?'), []
    for sp in card.get('spans', []):
        i = sp.get('block')
        if not (isinstance(i, int) and 0 <= i < len(block_texts)):
            continue
        a, b = sp['start'], sp['end']
        for s0, e0, e in ranges(block_texts[i], led):
            over = min(b, e0) - max(a, s0)
            if over > 0 and over >= max(1, (b - a) / 2):   # the highlight is (mostly) inside the kept words
                out.append('%s: highlights "%s", inside words Joel said stay as they are (%s, %s: %s)'
                           % (sid, block_texts[i][a:b][:50], e['id'], e['where'], e['what']))
    for e in card.get('edits', []):
        b, a = norm(e.get('before') or ''), norm(e.get('after') or '')
        for k in led.get('keep', []):
            q = norm(k['quote'])
            if q in b and q not in a:
                out.append('%s: changes "%s", which Joel said stays as it is (%s, %s)' % (sid, k['quote'][:50], k['id'], k['where']))
        for c in led.get('cuts', []):
            q = norm(c['quote'])
            if q in a and q not in b:
                out.append('%s: puts back "%s", which Joel cut on purpose (%s, %s)' % (sid, c['quote'][:50], c['id'], c['where']))
    for ins in card.get('inserts', []):
        for c in led.get('cuts', []):
            if norm(c['quote']) in norm(ins.get('text') or ''):
                out.append('%s: puts back "%s", which Joel cut on purpose (%s, %s)' % (sid, c['quote'][:50], c['id'], c['where']))
    return out


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest='cmd', required=True)
    for name in ('check', 'list'):
        sub.add_parser(name).add_argument('article')
    k = sub.add_parser('is-kept')
    k.add_argument('article')
    k.add_argument('words')
    a = ap.parse_args(argv)
    led = load(a.article)
    if a.cmd == 'list':
        for part in ('keep', 'cuts'):
            for e in led.get(part, []):
                print('%s %s [%s] "%s": %s (%s, %s)' % (part, e['id'], e.get('kind', 'cut'), e['quote'], e['what'], e['where'], e['basis']))
        return 0
    if a.cmd == 'is-kept':
        hits = kept(a.words, led)
        for e in hits:
            print('%s: "%s" (%s, %s)' % (e['id'], e['quote'], e['where'], e['what']))
        print('kept' if hits else 'not on the list')
        return 0 if hits else 1
    md = pathlib.Path(a.article).read_text(encoding='utf-8')
    probs = problems(led)
    gone, again = missing(md, led), back(md, led)
    for p in probs:
        print('LEDGER', p)
    for e in gone:
        print('GONE %s: "%s" is no longer in the article (%s, %s)' % (e['id'], e['quote'], e['where'], e['what']))
    for e in again:
        print('BACK %s: "%s" is in the article again, though Joel cut it on purpose (%s)' % (e['id'], e['quote'], e['where']))
    print('%d kept, %d meant cuts: %d gone, %d back, %d ledger problems'
          % (len(led.get('keep', [])), len(led.get('cuts', [])), len(gone), len(again), len(probs)))
    return 1 if (probs or gone or again) else 0


if __name__ == '__main__':
    sys.exit(main())
