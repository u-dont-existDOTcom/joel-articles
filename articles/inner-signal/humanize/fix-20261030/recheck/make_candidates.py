"""The whole guide's recheck of 30 October: CANDIDATE-MASTER.md, the guide as it stands (HUMANIZED-SO-FAR.md, with his
answers of 14:35 UTC and the fixes from my full read) plus my suggestions for four paragraphs of his own versions, in
place so the recheck reads them where they stand, and SUGGESTIONS.json (his words, my suggestion and why, for his cards
page). His versions from his last answers (J5, R-96, R-630 and the rest) go in as he wrote them: the recheck is also how
we learn what his versions do in place.

  python3 articles/inner-signal/humanize/fix-20261030/recheck/make_candidates.py
"""
import hashlib
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parents[1]
ROOT = H.parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
sys.path.insert(0, str(H / 'fix-20261025' / 'review'))
import suggestion_review as sr  # noqa: E402
from apply_answers import set_block_text  # noqa: E402

GUIDE_SHA = '975fdb3c2ac7d4a92856683866cf14d758cbf907e6ec408d605ceec3a1faed2b'

# (id, findings, start of his paragraph, old words, new words, whose, why)
SUGGESTIONS = [
    ('S-14', ['F1.3', 'F1.4'], '“How do I do this?” you ask.',
     [('since it\'s not "achieving something" but this', 'since it\'s not "achieving something", but this'),
      ('to demonstrate the results of all parts of your mind talking to each other and trusting each other more.',
       'to see the results in your day-to-day life, with all parts of your mind talking to each other and trusting each '
       'other more.')],
     'his edit of 28 October (ED-A1)',
     'A comma before "but", and where the results show: your published version says they are "proven in ordinary life", '
     'and "demonstrate the results" had lost that.'),
    ('S-20', ['F1.5', 'F1.6'], "You'll follow whatever you notice",
     [("- as you're invited.", '- and let it shape your next invite.'),
      ('& any real-world actions.', '& any real-world actions it calls for.')],
     'his edit of 28 October (ED-A3), which kept "as you\'re invited" from before',
     '"as you\'re invited" leaves a reader asking who invites; your published version runs the other way: what you notice '
     'shapes your next invitation. And the actions are the ones the session points to ("it calls for").'),
    ('S-24', ['F1.7'], "Keep in mind that it's normal, even for people who do think in words",
     [('to sometimes notice feelings before words.', 'to sometimes notice feelings before words. And "not sure" is a '
       'perfectly good answer to these questions. They\'re just here to help you pick instructions that work for you.')],
     'his own paragraph of 28 October (ED-A5: "couldn\'t even understand what the original was talking about")',
     'Your published version also told the reader that "not sure" is a fine answer and that the questions only pick '
     'workable instructions; nothing in the guide says it now. This says it plainly.'),
    ('S-782', ['F21.2'], 'Not everybody has an inner voice (Nedergaard and Lupyan 2024)',
     [('Not everybody has an inner voice (Nedergaard', 'The study Not everybody has an inner voice (Nedergaard')],
     'his edit of 25 October (CV-8.9)',
     'The study\'s title isn\'t marked as a title, so the sentence first reads as a claim ("Not everybody has an inner '
     'voice ... is not about"). "The study" in front makes it a title.'),
]
# his version from his last answers: the suggestion goes on his cards page only (E297, the exercise taught once)
CARD_ONLY = [
    ('S-636', ['E297'], 'Here is my basic inner child love practice technique.',
     [('Here is my basic inner child love practice technique. Put your hand over your heart and your other hand on your '
       'solar plexus, and say', 'Do the two-hand practice from Working with your inner child, and say')],
     'his version of 30 October (R-630)',
     'The same exercise is taught four times in the guide (you: "we have 4 of these in different versions in there ... '
     'Let\'s make sure we aren\'t giving people exercises over and over"). It\'s taught once now, in The two-hand '
     'practice; the induction and the troubleshooting line name it instead of teaching it again. This would do the same '
     'here and keep your words for the inner child.'),
]


def main():
    md = (H / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
    assert hashlib.sha256(md.encode('utf-8')).hexdigest() == GUIDE_SHA, 'the guide changed'
    bl = sr.blocks(md)
    raw = re.split(r'\n\s*\n', md.rstrip('\n'))
    assert len(raw) == len(bl)
    out, lost, rec = list(raw), [], []
    for sid, fids, start, edits, whose, why in SUGGESTIONS + CARD_ONLY:
        hits = [b for b in bl if b['text'].startswith(start)]
        assert len(hits) == 1, sid
        b = hits[0]
        t = b['text']
        for old, new in edits:
            assert t.count(old) == 1, (sid, old)
            t = t.replace(old, new)
        if (sid, fids, start, edits, whose, why) in SUGGESTIONS:
            out[b['i']] = set_block_text(raw[b['i']], t, lost)
        rec.append({'id': sid, 'findings': fids, 'block': b['i'], 'where': sr.where(bl, b['i']), 'whose': whose,
                    'his': b['text'], 'suggestion': t, 'why': why,
                    'in_recheck': (sid, fids, start, edits, whose, why) in SUGGESTIONS})
    assert not lost, lost
    master = '\n\n'.join(out) + '\n'
    (HERE / 'CANDIDATE-MASTER.md').write_text(master, encoding='utf-8')
    (HERE / 'SUGGESTIONS.json').write_text(json.dumps({'guide_sha256': GUIDE_SHA, 'master_sha256': hashlib.sha256(
        master.encode('utf-8')).hexdigest(), 'suggestions': rec}, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print(len(rec), 'suggestions;', sum(r['in_recheck'] for r in rec), 'in the recheck')


if __name__ == '__main__':
    main()
