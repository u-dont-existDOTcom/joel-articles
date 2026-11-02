"""Put Joel's answers to Hypnosis Guide Cards, 1 November (2) (REVIEW-S1101) into the hypnosis guide, with every card's fate.

His export of 2026-11-02 (ANSWERS-20261102-1643.json here, word for word), sent with his message of 16:43 UTC
(joel-20261102-1643-message.txt: no text, the two answers files): 10 approved, 15 revised. Most revised versions are texts
he checked in Pangram and linked in his comment; their full texts, read from those links, are in
joel-pangram/texts-raw.json (each checked against the page's SHA-256) and EDITS-joel-20261102-pangram.json.

- An approved card goes in as the card showed it (its edits' "after"), except W-509 and W-513: his note on W-509 says
  the approved version still read AI in Pangram and links his own Pattern 3 to 7, so his text goes in (below).
- A revised card goes in as his version, word for word, one paragraph a line, except the obvious typos (TYPOS, each
  listed). Where his version takes in more of the section than the card did, it replaces the paragraphs PLANS names,
  and every paragraph of the guide it doesn't name stays.
- E-406: his "your version" is the minimal pair he checked last (f418aed4); his note says "altho it still reads ai to
  me without the other fixes", so his fuller version (ff307b0a, "Bring it down to Earth") goes in.
- W-509 and W-513 (Pattern 3 to 7): his text 6c87cdc9 ("finally fully human high conf") up to the McHappyness example,
  then Pattern 7 from 54ec1675 (his last, "100% high conf human ... by uncompressing one low conf sentence"), because
  he says of the McHappyness quip "but i still like that mcd quip you can keep that in".
- W-605: his text c341e75a ("now 100% human high conf"), with the body-signal example he prefers to keep; his "your
  version" field holds the card's version, not his.
- W-762: his first line is the heading without its number; the heading keeps its "9." like the other practices.

  python3 articles/inner-signal/humanize/fix-20261102/apply_answers_s1101.py [--check]

Writes HUMANIZED-SO-FAR.md and APPLIED-S1101.json (each card's fate, the typo fixes, what each plan replaced, and
which blocks of the old guide became which blocks of the new one).
"""
import argparse
import hashlib
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parent
ROOT = H.parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
sys.path.insert(0, str(H / 'fix-20261025' / 'review'))
import suggestion_review as sr  # noqa: E402
from apply_answers import set_block_text  # noqa: E402

GUIDE = H / 'HUMANIZED-SO-FAR.md'
REVIEW = H / 'fix-20261101' / 'sections' / 'review' / 'REVIEW-S1101.json'
ANSWERS = HERE / 'ANSWERS-20261102-1643.json'
PANGRAM = HERE / 'joel-pangram' / 'texts-raw.json'
LINK = 'https://www.pangram.com/history/'

# his texts from his Pangram links, for the cards whose "your version" isn't his final text
U6C, U54, UC3, UFF = ('6c87cdc9-aca4-4293-8eaa-22a8fa2884c6', '54ec1675-46cc-4e67-b3e1-6bf54ff01151',
                      'c341e75a-0155-457e-a490-4a97db7f9e28', 'ff307b0a-ff97-476c-be72-68ceef371b0e')

# obvious typos in his versions: (card, wrong, right, why)
TYPOS = [
    ('E-107', 'you gain access all of', 'you gain access to all of', 'a missing "to"'),
    ('E-107', 'what it can be like to as free as', 'what it can be like to be as free as', 'a missing "be"'),
    ('E-107', 'to talk.  I understand', 'to talk. I understand', 'a double space'),
    ('W-282', 'feel your spine  at the same time', 'feel your spine at the same time', 'a double space'),
    ('E-315', 'might half wake up and still', 'might half wake you up and still', 'a missing "you"'),
    ('E-406', 'What’s this lofty love is asking me to do?', 'What’s this lofty love asking me to do?', 'a stray "is"'),
    ('E-406', 'relationship repair?"', 'relationship repair?”', 'the closing quote mark matches the opening one'),
    ('W-579', 'when they want time to take to process', 'when they want to take time to process', 'two words swapped'),
    ('W-589', 'The Nurturer to brings love in', 'The Nurturer brings love in', 'a stray "to"'),
    ('W-605', 'check how well you\'re critical thinking is working', 'check how well your critical thinking is working',
     '"you\'re" for "your"'),
]

# Each revised card: the guide's paragraphs his version replaces, in order, as (block, [his line numbers]); a block
# with no lines is taken out (its words are in his version); ('same', k) is his line k unchanged (a heading the guide
# has) and stays; ('number', k) is his line k with the guide's own list number kept in front. Every planned block's
# first words are checked before it changes.
PLANS = {
    'E-107': [(104, [0]), (105, [1]), (106, [2]), (107, [])],
    'W-164': [(159, ('same', 0)), (160, [1]), (161, [2]), (162, [3]), (163, [4]), (164, [5])],
    'W-274': [(274, [0])],
    'W-282': [(275, [0]), (276, [1]), (277, ('same', 2)), (278, [3]), (279, [4]), (280, [5]), (281, ('same', 6)),
              (282, [7])],
    'E-315': [(315, [0]), (316, [1])],
    'W-358': [(358, [0])],
    'E-368': [(368, [0]), (369, [1])],
    'E-406': [(405, ('same', 0)), (406, [1])],
    'W-509': [(505, ('same', 0)), (506, [1]), (507, [2]), (508, ('same', 3)), (509, [4]), (510, []), (511, [5]),
              (512, ('same', 6)), (513, [7]), (514, []), (515, [8]), (516, [9]), (517, ('same', 10)), (518, [11]),
              (519, [12]), (520, [13]), (521, ('same', 14)), (522, [15]), (523, [16])],
    'W-579': [(575, ('same', 0)), (576, [1]), (577, [2]), (578, [3]), (579, [4])],
    'W-589': [(583, ('same', 0)), (584, [1]), (585, [2]), (586, [3]), (587, [4]), (588, [5]), (589, [6]), (590, [7]),
              (591, [8]), (592, [9]), (593, [10]), (594, [11])],
    'W-596': [(596, [0])],
    'W-605': [(605, ('same', 0)), (606, [1]), (607, [2]), (608, []), (609, [3]), (610, []), (611, [4]), (612, []),
              (613, [5]), (614, [6]), (615, [7]), (616, [8])],
    'W-685': [(677, ('same', 0)), (678, [1]), (679, []), (680, [2]), (681, []), (682, []), (683, ('same', 3)),
              (684, [4]), (685, [5])],
    'W-687': [(686, ('same', 0)), (687, [1])],
    'W-762': [(758, ('number', 0)), (759, [1]), (760, [2]), (761, [3]), (762, [4]), (763, [5]), (764, [6]),
              (765, [7]), (766, [8])],
}
# the first words of each planned block as it is now (so a plan can't land on the wrong paragraph)
STARTS = {104: 'Let the child speak without handing', 105: 'Let the parts of you that feel younger',
          106: '"It is okay for a younger part', 107: 'That way you keep the good parts', 159: 'Don’t rush the repair',
          160: 'When your inner child does show up', 161: 'If you can, tell them something like',
          162: 'What does your inner child need?', 163: 'When a younger you, a guard', 164: 'A. Prepare yourself',
          274: 'Say something like, "Only what I can integrate', 275: 'Once you’ve got your bearings, ask for one',
          276: '"Please show me the next truth, symbol', 277: 'Stay awake when your mind likes to escape',
          278: 'If your mind keeps drifting off', 279: 'Pick one thing in the room', 280: 'Ask for what fits',
          281: 'Make the hypnosis more alert', 282: 'If being still tends to make you sleepy',
          315: 'If your recording cuts out partway', 316: 'Sleep recordings are different',
          358: 'Don’t feel that you have to end the session', 368: 'Once or twice a week, when it’s useful',
          369: 'Then, if you can, do the normal thing', 405: 'You become too blissful or diffuse',
          406: 'If the bliss spreads out', 505: 'Pattern 3: Presuppositions', 506: 'A presupposition hides',
          507: 'A safe one sounds like this', 508: 'Pattern 4: Gentle cause-effect bridges', 509: 'Bridge words are words',
          510: 'Here\'s an example of some of the overly', 511: 'I prefer the communion version',
          512: 'Pattern 5: Embedded invitations', 513: 'An embedded invitation places', 514: 'or, "As I sit here',
          515: 'With your inner child, it could be', 516: 'One at a time is plenty', 517: 'Pattern 6: Ethical double binds',
          518: 'A manipulative double bind is', 519: 'An ethical double bind also gives', 520: '"Would you like some warmth',
          521: 'Pattern 7: Conversational postulates', 522: 'A conversational postulate is',
          523: '"Can my subconscious show me the next thing', 575: 'What I will not use NLP for',
          576: 'Here is a list of things I don\'t do', 577: 'I don\'t use NLP to convince',
          578: 'On the other hand, I also don\'t use NLP', 579: 'As an example, I won’t tell anyone',
          583: 'Running the whole NLP sequence', 584: 'Here is a rough outline', 585: 'Induce yourself',
          586: 'Ask yourself for permission', 587: 'Get a representation', 588: 'Find out if that part',
          589: 'Gently change an aspect', 590: 'Bring in your three good adults', 591: 'Then anchor the good state',
          592: 'Imagine running into a scenario', 593: 'Check in with your body', 594: 'Then come all the way back out',
          596: 'What to do when you feel like you’re being pushed', 605: 'Hypnosis-specific audit',
          606: 'Before accepting a hypnotic recording', 607: 'What induction mechanics', 608: 'Can my responses lead',
          609: 'Does the hypnotist treat', 610: 'Is the hypnotist using identity roles', 611: 'Keep in mind though, the answer',
          612: 'Continuing with the job interview', 613: 'Are fractionation, cues', 614: 'Is the hypnotist implicitly',
          615: 'When we\'re ready to exit hypnosis', 616: 'When any answer to these questions',
          677: 'Forgiveness without bypass', 678: 'We cannot force forgiveness', 679: 'A helpful understanding',
          680: 'You might say to the part of you that got hurt', 681: 'Some questions that may be helpful',
          682: 'What actually happened?', 683: 'Forgiving yourself', 684: 'For self-forgiveness, name what you did',
          685: 'Do what you can to put it right, or', 686: 'Appendix G: Altered states',
          687: 'I’m not saying you should use substances', 758: '9. No-trance inner contact',
          759: 'For the no trance inner contact', 760: 'For pacing (warm-up)', 761: 'For the suggestion: in your mind',
          762: 'Now keep your sense of agency', 763: 'Keep aware of the subtle inner signal', 764: 'Hand off the role',
          765: 'Integration/exit', 766: 'There\'s no elaborate exit protocol'}


# a source link whose words his version doesn't keep goes on the words of his that say the same thing:
# (card, block, his words, the link, why)
RELINK = [
    ('W-282', 282, 'suggest yourself into greater alertness',
     'https://www.tandfonline.com/doi/full/10.1080/00029157.2018.1496318',
     'the study the old words "Instead of getting more relaxed with the hypnosis, try getting more alert" linked to; '
     'his sentence says the same thing'),
]


def his_text(cid, x, pangram):
    """The text of his that goes in for card CID, and where it comes from."""
    if cid == 'E-406':
        return pangram[UFF], 'his Pangram text ' + LINK + UFF
    if cid == 'W-509':
        a, b = pangram[U6C], pangram[U54]
        return (a[:a.index('Pattern 7')] + b[b.index('Pattern 7'):],
                'his Pangram texts %s%s (Patterns 3 to 6, with the McHappyness example) and %s%s (Pattern 7)' % (
                    LINK, U6C, LINK, U54))
    if cid == 'W-605':
        return pangram[UC3], 'his Pangram text ' + LINK + UC3
    return x['your_version'], 'his version on the cards page'


def his_lines(cid, text):
    """His version: obvious typos fixed (each recorded), then one paragraph (or heading) a line, spaces trimmed."""
    notes = []
    t = text
    for c, wrong, right, why in TYPOS:
        if c == cid:
            assert t.count(wrong) == 1, (cid, wrong)
            t = t.replace(wrong, right)
            notes.append('typo fixed (%s): "%s" -> "%s"' % (why, wrong, right))
    lines = [ln.strip() for ln in t.split('\n') if ln.strip()]
    return lines, notes


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--check', action='store_true')
    a = ap.parse_args()
    review = json.loads(REVIEW.read_text(encoding='utf-8'))
    answers = json.loads(ANSWERS.read_text(encoding='utf-8'))
    pangram = json.loads(PANGRAM.read_text(encoding='utf-8'))
    md = GUIDE.read_text(encoding='utf-8')
    sha = hashlib.sha256(md.encode('utf-8')).hexdigest()
    assert sha == review['article']['sha256'] == answers['article']['sha256'], 'the guide changed since the cards page'
    assert answers['review_id'] == review['review_id']
    bl = sr.blocks(md)
    raw = re.split(r'\n\s*\n', md.rstrip('\n'))
    assert len(raw) == len(bl)
    for i, s in STARTS.items():
        assert bl[i]['text'].startswith(s), (i, bl[i]['text'][:60])
    A = {x['id']: x for x in answers['items']}
    assert {s['id'] for s in review['suggestions']} == set(A)
    new_raw, fates, lost, notes_all, replaced = {}, {}, [], {}, {}
    for s in review['suggestions']:
        sid = s['id']
        x = A[sid]
        comment = ['his comment: ' + x['comment']] if x['comment'] else []
        if x['status'] == 'approved' and sid not in ('W-509', 'W-513'):
            assert s['advice'] == 'approve' and s['edits'], sid
            for e in s['edits']:
                i = e['block']
                assert e['before'] == bl[i]['text'] and i not in new_raw, (sid, i)
                new_raw[i] = [set_block_text(raw[i], e['after'], lost)]
            fates[sid] = 'approved: the card\'s version went in'
            notes_all[sid] = comment
            continue
        if sid == 'W-513':
            assert x['status'] == 'approved'
            fates[sid] = 'approved, then replaced by his own Pattern 3 to 7 (his note on W-509), which rewrites this ' \
                         'paragraph too'
            notes_all[sid] = comment
            continue
        assert x['status'] in ('revise', 'approved'), sid
        text, source = his_text(sid, x, pangram)
        assert text.strip(), sid
        lines, notes = his_lines(sid, text)
        used = []
        for i, part in PLANS[sid]:
            assert i not in new_raw, (sid, i)
            if isinstance(part, tuple):
                how, k = part
                if how == 'same':
                    assert lines[k] == bl[i]['text'], (sid, i, lines[k], bl[i]['text'])
                else:
                    num = re.match(r'(\d+\.\s+)', bl[i]['text']).group(1)
                    assert num + lines[k] == bl[i]['text'], (sid, i)
                    notes.append('his heading "%s" keeps the guide\'s number: "%s"' % (lines[k], bl[i]['text']))
                used.append(k)
                continue
            new_raw[i] = [set_block_text(raw[i], lines[k], lost) for k in part]
            used += part
        assert sorted(used) == list(range(len(lines))), (sid, sorted(used), len(lines))
        for c, i, words, url, why in RELINK:
            if c == sid:
                [r] = new_raw[i]
                assert r.count(words) == 1 and url not in r, (sid, i)
                new_raw[i] = [r.replace(words, '[%s](%s)' % (words, url))]
                gone = [x_ for x_ in lost if url in x_]
                assert len(gone) == 1, (sid, url)
                lost.remove(gone[0])
                notes.append('source link kept on his words "%s" (%s)' % (words, why))
        replaced[sid] = [{'block': i, 'was': bl[i]['text'],
                          'now': [lines[k] for k in part] if isinstance(part, list) else part[0]}
                         for i, part in PLANS[sid]]
        fates[sid] = 'his version (%s)' % source
        notes_all[sid] = notes + comment
    out, block_map = [], {}
    for i, r in enumerate(raw):
        parts = new_raw.get(i, [r])
        block_map[i] = list(range(len(out), len(out) + len(parts)))
        out += parts
    new = '\n\n'.join(out) + '\n'
    assert len(sr.blocks(new)) == len(out)
    rec = {'answers': str(ANSWERS.relative_to(H)), 'answers_sha256': hashlib.sha256(ANSWERS.read_bytes()).hexdigest(),
           'pangram_texts': str(PANGRAM.relative_to(H)), 'before_sha256': sha,
           'after_sha256': hashlib.sha256(new.encode('utf-8')).hexdigest(),
           'fates': fates, 'notes': notes_all, 'replaced': replaced,
           'typos': [{'card': c, 'was': w, 'now': r, 'why': y} for c, w, r, y in TYPOS], 'links_dropped': lost,
           'changed_blocks': sorted(new_raw), 'block_map': block_map}
    print(json.dumps({k: v for k, v in rec.items() if k in ('before_sha256', 'after_sha256', 'links_dropped')},
                     indent=1))
    from collections import Counter
    print(Counter(v.split(':')[0].split(' (')[0] for v in fates.values()), len(new_raw), 'blocks changed,',
          len(bl), '->', len(out), 'blocks')
    if not a.check:
        GUIDE.write_text(new, encoding='utf-8')
        (HERE / 'APPLIED-S1101.json').write_text(json.dumps(rec, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')


if __name__ == '__main__':
    main()
