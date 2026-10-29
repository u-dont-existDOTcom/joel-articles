"""Joel's answers to the fix page (question 24), from his message of 2026-10-29 17:21 UTC: "approve all the cards and
where there's no "approve" option just take the advice given" (joel-20261029-1721-message.txt).

He didn't send the page's export, so this writes his decision in the export's form for apply_answers_28.py:
DECISIONS-20261029.json. Every fix card (my advice "approve") is approved. The four cards in his own words have no
Approve button (advice "edit": Keep it as it is / Edit it); my advice on each offered a wording, and "take the advice
given" takes it: the card's words replaced by the wording my note gave, the rest of his paragraph untouched. C-59's note
said "The same line is in Working with your guards, P6; your answer here goes for both", so its wording goes there too.

The file is named DECISIONS, not ANSWERS: the comparison gate counts an ANSWERS-*.json as his own words, and the four
wordings are mine, so they get a read beside his published text like any new words (E288).

  python3 articles/inner-signal/humanize/fix-20261029/build_decisions.py
"""
import datetime
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parent
ROOT = H.parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import suggestion_review as sr  # noqa: E402

C28 = H / 'fix-20261028' / 'comprehension'

# my advice on the four cards in his own words (REVIEW-28.json, advice_note), as replacements inside his paragraph
ADVICE = {
    'C-26': ('As you differentiate, you learn', 'As you become more your own person, you learn',
             'my note: "say it the way you\'d say it here, for example \\"As you become more your own person, you learn '
             'to tell which of those apply.\\""'),
    'C-59': ('I\u2019d stop there and not test it', 'I\u2019d stop there and not push past that no',
             'my note: "for example \\"I\'d stop there and not push past that no, even when it sounds like a '
             'prediction.\\" The same line is in Working with your guards, P6; your answer here goes for both."'),
    'C-90': ('rescue your child', 'rescue your inner child',
             'my note: "Keep it, or \\"your inner child\\" (or \\"your little one\\")": the first wording'),
    'C-91': ('when your consciously installed parental Protector isn\u2019t functioning',
             'when your inner adult\u2019s Protector isn\u2019t functioning',
             'my note: "\\"your inner adult\'s Protector\\" says the same with the guide\'s term"'),
}
ALSO = {'C-59': 'Working with your guards, P6'}


def main():
    review = json.loads((C28 / 'REVIEW-28.json').read_text(encoding='utf-8'))
    md = (H / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
    bl = sr.blocks(md)
    items = []
    for s in review['suggestions']:
        if s['advice'] == 'approve':
            items.append({'id': s['id'], 'status': 'approved', 'fate': 'approved (his message: "approve all the cards")'})
            continue
        assert s['advice'] == 'edit', s['id']
        old, new, why = ADVICE[s['id']]
        i = s['spans'][0]['block']
        text = bl[i]['text']
        assert text.count(old) == 1, (s['id'], old)
        item = {'id': s['id'], 'status': 'revise', 'your_version': text.replace(old, new),
                'fate': 'my advised wording (his message: "where there\'s no \\"approve\\" option just take the advice '
                        'given"); %s' % why}
        if s['id'] in ALSO:
            j = [k for k, b in enumerate(bl) if sr.where(bl, k) == ALSO[s['id']]]
            assert len(j) == 1 and bl[j[0]]['text'].count(old) == 1, ALSO[s['id']]
            item['also'] = [{'block': j[0], 'where': ALSO[s['id']], 'replace': old, 'with': new}]
        items.append(item)
    out = {'format': 'joel-suggestion-review-answers-v1', 'review_id': review['review_id'],
           'source': 'built from Joel\'s message of 2026-10-29 17:21 UTC (fix-20261029/joel-20261029-1721-message.txt), '
                     'not exported from the page',
           'built': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M UTC'), 'items': items}
    (HERE / 'DECISIONS-20261029.json').write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    n = {}
    for x in items:
        n[x['status']] = n.get(x['status'], 0) + 1
    print('DECISIONS-20261029.json:', n)


if __name__ == '__main__':
    main()
