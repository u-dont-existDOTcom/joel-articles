#!/usr/bin/env python3
"""Making-sense receipts (gate E365) for r20's checks (texts.py). Every sentence has its row: a sentence an earlier
receipt in this article already has a row for keeps it; the rest are written here by their place in the text. Writes
CHECK-<name>.txt and RECEIPT-<name>.json and checks each; exits 1 if one fails."""
import glob
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[5]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import sense_receipt as S  # noqa: E402
from texts import TEXTS  # noqa: E402

OLD = {}
for f in sorted(glob.glob(str(ROOT / 'articles' / 'romance' / 'humanize' / '**' / 'RECEIPT-*.json'), recursive=True)):
    if '/r20/' in f:
        continue
    for s in json.load(open(f, encoding='utf-8')).get('sentences', []):
        if s.get('s') and s.get('payoff'):
            OLD[s['s'].strip()] = (s['payoff'], s['follows'], s.get('link'))
# (first words of the sentence) -> (payoff, follows, link)
NEW = {
    'I’m Buddhist, and the early Buddhist texts have nothing on tantric sex':
        ('the early Buddhist texts have no tantric sex path, but many of their awakened people were lay people',
         'opens the section', None),
    'In DN 16, the Buddha talks about people who had died':
        ('DN 16 names hundreds of lay people at the first three stages of awakening', 'the evidence for it', 'In DN 16'),
    'SN 55.24 has an almost comic complaint':
        ('in SN 55.24 others grumbled that everyone was a stream-enterer', 'more evidence, with a joke', 'SN 55.24'),
    'And when the married couple':
        ('a married couple asked the Buddha how to stay together in future lives', 'a married couple’s case',
         'And when the married couple'),
    '“When both husband and wife are faithful':
        ('his answer: faithful, generous, kind spouses meet again in future lives', 'the Buddha’s advice',
         'When both husband and wife'),
    'Marriage, sex, and household life are not automatically':
        ('marriage and sex aren’t opposed to serious spiritual growth', 'what the texts show', 'Marriage, sex, and household life'),
    'The example I really like is Brad and Pam Keene':
        ('the Keenes’ marriage became part of their path', 'opens the paragraph', None),
    'Pam says her Kundalini process completed':
        ('Pam awakened while making love and later helped Brad awaken', 'what happened to them', 'Pam says'),
    'In the previous section, I mentioned':
        ('he mentioned the divine feminine and masculine before', 'a turn to Twin Flames', 'In the previous section'),
    'But there’s really something more special':
        ('Twin Flames feel more special than a masculine-feminine formula', 'what is more', 'But there’s really something'),
    'Maybe a better way to put it':
        ('yin and yang may put it better, each holding the seed of the other', 'a better way to say it',
         'Maybe a better way to put it'),
}
META = {
    'r20-spir304': ('Can making love be a spiritual practice?',
                    'A Buddhist or spiritual seeker wondering whether married life and sex rule out serious awakening.',
                    'It tells the reader serious awakening isn’t only for monks.'),
    'r20-spir312': ('Can making love be a spiritual practice?',
                    'Someone wondering whether a marriage can itself be a spiritual path.',
                    'It tells the reader of a couple whose marriage became part of their path.'),
}
Q = {
    'Q1': 'PASS: each changed sentence gives its point first, in plain words',
    'Q2': 'N/A: these paragraphs tell; they give no advice',
    'Q3': 'PASS: the texts, people and numbers are named as in the live post',
    'Q4': 'PASS: the stages of awakening are named where the stream-enterers first appear (E369)',
    'Q5': 'PASS: each sentence’s tie is in its words (the links field), or it opens its paragraph',
    'Q6': 'PASS: the order is the live post’s',
    'Q7': 'PASS: each change keeps what the paragraph tells the reader',
    'Q8': 'PASS: no item moved between groups',
    'Q9': 'PASS: one step per sentence',
}
LOW = [{'point': 'the AI and Low windows’ points', 'found': 'the section check with S17 in it (#45, '
        '../../r06/checks/RESULTS-r06.json or the ledger)', 'still_needed': 'yes: the section needs them', 'fate': 'changed'}]
bad = 0
for name, text in TEXTS.items():
    section, reader, why = META[name]
    r = S.make(text, section, reader)
    for s in r['sentences']:
        row = next((v for k, v in NEW.items() if s['s'].startswith(k)), None) or OLD.get(s['s'].strip())
        assert row, ('no row', name, s['s'][:60])
        pay, fol, link = row
        s['payoff'] = pay if pay.startswith('the reader learns ') else 'the reader learns ' + pay
        s['follows'] = fol
        if 'link' in s:
            s['link'] = link or 'none: it opens its paragraph, and the paragraph before it ends its own point'
    r['opens']['why_reading'] = why
    r['same_point'] = 'none: read the section from its heading to the next for these points; each is made once, here'
    r['questions'] = dict(Q)
    r['checked'] = LOW
    r['placement'] = ('Paragraphs 304 to 309 by themselves, for the section gate (E343), S17’s paragraphs after them left out.'
                      if name == 'r20-spir304' else
                      'Paragraph 312 with 313 after it (312 alone is under the web app’s 50 words), for the section gate.')
    (HERE / ('CHECK-%s.txt' % name)).write_text(text, encoding='utf-8')
    (HERE / ('RECEIPT-%s.json' % name)).write_text(json.dumps(r, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    probs = S.check(text, r)
    bad += bool(probs)
    print(name, 'PASS' if not probs else probs)
sys.exit(1 if bad else 0)
