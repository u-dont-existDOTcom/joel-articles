#!/usr/bin/env python3
"""substack_check_text.py - the text Pangram's check of a Substack post reads, rebuilt from the HTML that was pasted into
the post (2026-10-22, the hypnosis guide's recheck).

A check made by Pangram's extension on a Substack post (its result page is https://www.pangram.com/feed/<uuid>) reads the
post's paragraphs, not its headings, images, embeds or a paid reader's subscribe buttons, up to its first 99,999
characters. tools/humanization/pangram_feed_read.js takes the whole result from the page, the checked text included, and
that text cost about 25,000 tokens of a worker's context for each half of a long guide, every time it was read out of the
page. The text can be rebuilt from the payload instead: the paragraphs and list items in order, one per line, with two
rules found by comparing the rebuild with the page's text, chunk by chunk, until their SHA-256 matched:
  - a paragraph that is only a link to a post (a bare URL) became an embedded card when it was pasted; the check reads
    none of the card, or only its subtitle (part B of 2026-10-21: the card of "shadow-work-and-tripsitting-yourself" gave
    the line "Quick Triage Web-App Version HERE", while part A's card of the sky-hypnosis post gave nothing), so a card's
    lines are given in META.json's "embeds" ({url: [lines]}) when the page shows them, and a card without an entry gives
    none;
  - the post shows straight quotes as curly ones (an opening quote after a space, a bracket or a dash; a closing one and
    an apostrophe elsewhere), except in an embedded Substack note, whose paragraphs keep their straight quotes;
  - a paragraph's trailing spaces go, and so do the emoji joiners and presentation selectors (U+200D, U+FE0F) (the
    Nibbāna post's check of 2026-10-20, rebuilt from Joel's editor HTML of 2026-10-22).
So only the windows are read from the page (a compact line each), and the rebuilt text is checked against the page's own
SHA-256 of its text (pangram_feed_read.js prints it with the windows when asked).

Two exceptions seen since (2026-10-25, the Inner Child guide's round 6, both halves matched only with them): in that paste a
straight double quote after "(" or "—" came out as a closing one, four times ("(”Once upon a time…”", "pas—”we do"), where
the rule above makes it an opening one; and an embedded note's line was curled ("it’s"). So when a rebuild misses the
page's SHA-256, compare the two in chunks (a SHA-256 of each 5,000 characters on both sides finds the place fast) before
trusting either rule; articles/inner-child-therapy/experiments/t108-results/record_round6.py shows the change it needed.

  python3 tools/humanization/substack_check_text.py text PAYLOAD.html [--limit 99999]
          the rebuilt text's length and SHA-256
  python3 tools/humanization/substack_check_text.py result PAYLOAD.html WINDOWS.txt META.json --out RESULT.json
          a RESULT file like pangram_feed_read.js's: META.json's fields, the windows from WINDOWS.txt (the page's compact
          "label,confidence,start,end,words,ai_likelihood,is_humanized,calibrated_confidence,uncertainty" entries,
          separated by ";", label H or A and confidence H, M or L), and the rebuilt text; it stops unless the text's SHA-256
          is META.json's "text_sha256", the windows tile the text from 0 to its end, and their words and labels add up
          to what the page gives for its windows ("windows_word_sum", "windows_ai", "windows_human"; the result's own
          "word_count" counts differently)
"""
import argparse, hashlib, json, re, sys

SKIP = {'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'hr', 'iframe', 'figure', 'picture', 'img', 'source'}
OPEN1 = re.compile(r"(^|[\s(\[{“\"—-])'")
OPEN2 = re.compile(r'(^|[\s(\[{‘—-])"')
LABEL = {'H': 'Human', 'A': 'AI-Generated'}
CONF = {'H': 'High', 'M': 'Medium', 'L': 'Low'}


def _lines(el, out, embeds=None, note=False):
    """Append (line, curl) for each paragraph or list item under EL. A paragraph of an embedded Substack note (inside a
    "FeedProseMirror" body) keeps its straight quotes in the check, so it isn't curled."""
    from bs4 import NavigableString, Tag
    if isinstance(el, NavigableString):
        return
    if el.name in SKIP:
        return
    classes = el.get('class') or []
    if el.name == 'div' and ('captioned-image-container' in classes or 'image-gallery-embed' in classes):
        return
    note = note or 'FeedProseMirror' in classes
    if el.name == 'p':
        txt = el.get_text()
        if 'button-wrapper' in classes and 'checkout_url' in str(el):
            return
        if re.fullmatch(r'https?://\S+', txt.strip()):
            out.extend((x, True) for x in (embeds or {}).get(txt.strip(), []))
            return
        if txt.strip():
            out.append((txt.rstrip(' '), not note))
        return
    if el.name == 'li':
        if any(isinstance(c, Tag) and c.name in ('p', 'ul', 'ol') for c in el.children):
            for c in el.children:
                if isinstance(c, Tag):
                    _lines(c, out, embeds, note)
        elif el.get_text().strip():
            out.append((el.get_text().rstrip(' '), not note))
        return
    for c in el.children:
        _lines(c, out, embeds, note)


def smart(s):
    s = OPEN1.sub(lambda m: m.group(1) + '‘', s)
    s = s.replace("'", '’')
    s = OPEN2.sub(lambda m: m.group(1) + '“', s)
    return s.replace('"', '”')


def checked_text(html, limit=99999, embeds=None):
    """The text the check reads, from the payload pasted into a post or from Joel's editor HTML of a post (the
    contenteditable body). Each line is curled on its own (smart() reads only the character before a quote, and a line's
    start counts as a space, so this is the same as curling the joined text), and the emoji joiners and presentation
    selectors (U+200D, U+FE0F) go: the check of the Nibbāna post (2026-10-20) has "❤" and "😶🌫" for the editor's
    "❤️" and "😶‍🌫️"."""
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')
    body = soup.find('div', class_='body') or soup
    out = []
    for c in body.children:
        _lines(c, out, embeds)
    text = '\n'.join(smart(x) if curl else x for x, curl in out)
    return text.replace('\u200d', '').replace('\ufe0f', '')[:limit]


def windows(compact):
    out = []
    for e in [x for x in compact.strip().split(';') if x.strip()]:
        lab, conf, a, b, wc, ai, hz, cal, unc = e.split(',')
        out.append({'label': LABEL.get(lab, lab), 'confidence': CONF.get(conf, conf), 'ai_likelihood': float(ai),
                    'word_count': int(wc), 'start_index': int(a), 'end_index': int(b), 'is_humanized': hz == '1',
                    'calibrated_confidence': float(cal) if cal else None, 'uncertainty_highlighting': unc == '1'})
    return out


def result(html, compact, meta, limit=99999):
    text = checked_text(html, limit, meta.get('embeds'))
    sha = hashlib.sha256(text.encode('utf-8')).hexdigest()
    if meta.get('text_sha256') and sha != meta['text_sha256']:
        raise SystemExit('the rebuilt text (SHA-256 %s) is not the checked text (%s): compare them chunk by chunk' % (sha, meta['text_sha256']))
    ws = windows(compact)
    pos = 0
    for w in ws:
        if w['start_index'] != pos:
            raise SystemExit('the windows leave a gap or overlap at %d' % pos)
        pos = w['end_index']
    if pos != len(text):
        raise SystemExit('the windows end at %d, the text at %d' % (pos, len(text)))
    # the result's own word_count isn't the sum of its windows' (part A of 2026-10-21: 18,687 against 18,414 on the page
    # itself), so the check is against the sum the page gives for its windows, read with them
    if meta.get('windows_word_sum') is not None and sum(w['word_count'] for w in ws) != meta['windows_word_sum']:
        raise SystemExit('the windows hold %d words, the page\'s %d' % (sum(w['word_count'] for w in ws), meta['windows_word_sum']))
    for lab, key in (('AI-Generated', 'windows_ai'), ('Human', 'windows_human')):
        if meta.get(key) is not None and sum(w['label'] == lab for w in ws) != meta[key]:
            raise SystemExit('%d %s windows, the page has %d' % (sum(w['label'] == lab for w in ws), lab, meta[key]))
    return dict(meta, text_sha256=sha, windows=ws, text=text,
                text_source='rebuilt from the pasted payload by tools/humanization/substack_check_text.py; SHA-256 matches the page')


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    sub = ap.add_subparsers(dest='cmd', required=True)
    t = sub.add_parser('text'); t.add_argument('payload'); t.add_argument('--limit', type=int, default=99999)
    r = sub.add_parser('result'); r.add_argument('payload'); r.add_argument('windows'); r.add_argument('meta')
    r.add_argument('--out', required=True); r.add_argument('--limit', type=int, default=99999)
    a = ap.parse_args(argv)
    html = open(a.payload, encoding='utf-8').read()
    if a.cmd == 'text':
        x = checked_text(html, a.limit)
        print(len(x), hashlib.sha256(x.encode('utf-8')).hexdigest())
        return 0
    meta = json.load(open(a.meta, encoding='utf-8'))
    d = result(html, open(a.windows, encoding='utf-8').read(), meta, a.limit)
    with open(a.out, 'w', encoding='utf-8') as f:
        json.dump(d, f, ensure_ascii=False, indent=1)
        f.write('\n')
    print('%s: %d windows, %d words, %s %s' % (a.out, len(d['windows']), d['word_count'], d.get('prediction_short'), d.get('headline')))
    return 0


if __name__ == '__main__':
    sys.exit(main())
