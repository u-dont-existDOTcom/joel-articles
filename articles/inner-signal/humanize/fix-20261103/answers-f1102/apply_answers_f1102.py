"""Put Joel's answers to Hypnosis Guide Cards, 2 November (3) (REVIEW-F1102) into the hypnosis guide, and record the read.

His export of 2026-11-03 00:38 UTC (ANSWERS-20261103-0039.json here, word for word; it was his whole message of 00:39 UTC):
- E-61, revise, no version, his comment: "cut all this. you didn't notice the massive overcompletion here? prob this whole
  guide is full of it then." The pairs of minds in Forget the left-brain/right-brain cartoon (blocks 61 and 62) go.
- C-92, approved: his inner child guide's rent line with the joke in brackets, as the card showed it.
- E-119, revise, his version of the two-hand practice's last two paragraphs (blocks 118 and 119): the breathing goes into
  the first line, and "Keep breathing gently through the whole practice." goes.
- E-380, revise, his version of Nothing happens and It feels fake (blocks 380 to 382), with his comment: "yes it directly
  tests as ai just these 2 paragraphs: <his check of the two paragraphs as they were> fixed them on my first attempt, yes i
  know i invented a word, that's cool you can invent words for informal pieces like this if they sound right: <his check of
  his version>". The heading goes in as he wrote it, in quotes; "imposterous" is his word and stays.
- C-480, approved: his Core prompts caveat joined to its sentence, as the card showed it.
- E-762, revise, "i fixed it in the whole section": his version of Appendix K's opening and its two subsections (blocks 758
  to 762, single line breaks between them). Blocks 758 and 762 change; the headings and block 760 are as they were. The
  book titles' italics and the links stay where they were (set_block_text puts plain text back into the block's Markdown).

Nothing in his versions is an obvious typo, so they go in word for word. In E-119, "and you breathe out" goes in as he
wrote it; question 31 asks whether he meant "as you breathe out".

  python3 articles/inner-signal/humanize/fix-20261103/answers-f1102/apply_answers_f1102.py [--check]
Writes HUMANIZED-SO-FAR.md, APPLIED-F1102-ANSWERS.json and read/READ-RECORD.json.
"""
import argparse
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
import compare_read as cr  # noqa: E402
import suggestion_review as sr  # noqa: E402
from apply_answers import set_block_text  # noqa: E402

GUIDE = H / 'HUMANIZED-SO-FAR.md'
REVIEW = H / 'fix-20261102' / 'f1102' / 'REVIEW-F1102.json'
ANSWERS = HERE / 'ANSWERS-20261103-0039.json'
BEFORE = '66eb95e7beac2ceac9ac01347f93c8de2960bcb7fad4b769fe8fa2ec07347b25'

HIS_CHECKS = {
    'E-380, the two paragraphs as they were (his test)': {
        'link': 'https://www.pangram.com/history/db67603a-b644-4667-b07a-140220544dd3',
        'result': 'AI Generated (fraction AI 1.0); windows AI (High, 12 words), AI (Medium, 24), AI (High, 32), '
                  'AI (Medium, 33), AI (High, 44), AI (Medium, 16)'},
    'E-380, his version': {
        'link': 'https://www.pangram.com/history/580be4c0-6fde-4f65-ba3b-559352c4d4ef',
        'result': 'Human Written (fraction AI 1.4e-17); windows Human (High, 106 words), Human (Medium, 4: " am I getting '
                  'warm?"), Human (High, 60)'},
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--check', action='store_true')
    a = ap.parse_args()
    review = json.loads(REVIEW.read_text(encoding='utf-8'))
    answers = json.loads(ANSWERS.read_text(encoding='utf-8'))
    md = GUIDE.read_text(encoding='utf-8')
    sha = hashlib.sha256(md.encode('utf-8')).hexdigest()
    assert sha == BEFORE == review['article']['sha256'] == answers['article']['sha256'], 'the guide changed since the cards page'
    bl = sr.blocks(md)
    raw = re.split(r'\n\s*\n', md.rstrip('\n'))
    assert len(raw) == len(bl) == 772
    A = {x['id']: x for x in answers['items']}
    S = {s['id']: s for s in review['suggestions']}
    assert sorted(A) == sorted(S)
    new_raw, lost, fates = {}, [], {}

    # E-61: cut the pairs of minds
    x = A['E-61']
    assert x['status'] == 'revise' and not x['your_version'].strip() and x['comment'].startswith('cut all this.')
    assert [s['block'] for s in S['E-61']['spans']] == [61, 62]
    assert bl[58]['text'] == 'Forget the left-brain/right-brain cartoon'
    assert bl[61]['text'].startswith('The mind of love and the mind of analysis') and bl[62]['text'].startswith('Analysis with no love')
    new_raw[61], new_raw[62] = [], []
    fates['E-61'] = ('revise, no version: "cut all this. you didn\'t notice the massive overcompletion here? prob this whole '
                     'guide is full of it then." Both paragraphs cut (blocks 61 and 62); lesson E328, and the whole guide '
                     'read for overcompletion (fix-20261103/overcompletion/)')

    # C-92 and C-480: approved, the cards' edits
    for cid in ('C-92', 'C-480'):
        assert A[cid]['status'] == 'approved' and not A[cid]['comment'].strip()
        for e in S[cid]['edits']:
            assert e['before'] == bl[e['block']]['text']
            new_raw[e['block']] = [set_block_text(raw[e['block']], e['after'], lost)]
        fates[cid] = 'approved: the card\'s version went in'

    # E-119: his version of the two-hand practice's last two paragraphs
    x = A['E-119']
    assert x['status'] == 'revise'
    p = [s.strip() for s in re.split(r'\n\s*\n', x['your_version'].strip())]
    assert len(p) == 2 and p[0].startswith('Gently breathe in lots of love') and p[1].startswith('This practice works as an induction')
    assert bl[118]['text'].startswith('Begin to send love') and bl[119]['text'].startswith('Keep breathing gently')
    new_raw[118] = [set_block_text(raw[118], p[0], lost)]
    new_raw[119] = [set_block_text(raw[119], p[1], lost)]
    fates['E-119'] = ('revise: his version went in (the breathing in the first line; "Keep breathing gently through the '
                      'whole practice." gone). "and you breathe out" as he wrote it; question 31 asks if he meant "as"')

    # E-380: his version of Nothing happens and It feels fake, the heading in his quotes
    x = A['E-380']
    assert x['status'] == 'revise'
    p = [s.strip() for s in re.split(r'\n\s*\n', x['your_version'].strip())]
    assert len(p) == 3 and p[1] == '"It feels fake"'
    assert bl[379]['text'] == 'Nothing happens' and bl[381]['text'] == 'It feels fake' and raw[381] == '## It feels fake'
    new_raw[380] = [set_block_text(raw[380], p[0], lost)]
    new_raw[381] = ['## ' + p[1]]
    new_raw[382] = [set_block_text(raw[382], p[2], lost)]
    assert 'imposterous' in p[2]
    fates['E-380'] = ('revise: his version went in, the heading as he wrote it ("It feels fake" in quotes) and his word '
                      '"imposterous"; his checks: the two paragraphs as they were read AI Generated '
                      '(https://www.pangram.com/history/db67603a-b644-4667-b07a-140220544dd3), his version Human Written '
                      '(https://www.pangram.com/history/580be4c0-6fde-4f65-ba3b-559352c4d4ef); read 2026-11-03 after 00:39 UTC')

    # E-762: his version of Appendix K's opening and its two subsections
    x = A['E-762']
    assert x['status'] == 'revise' and x['comment'].strip() == 'i fixed it in the whole section'
    v = x['your_version'].strip().split('\n')
    assert len(v) == 5
    assert v[1] == bl[759]['text'] and v[2] == bl[760]['text'] and v[3] == bl[761]['text']
    assert bl[757]['text'] == 'Appendix K: Sources and further reading'
    new_raw[758] = [set_block_text(raw[758], v[0], lost)]
    new_raw[762] = [set_block_text(raw[762], v[4], lost)]
    fates['E-762'] = ('revise: his version of the section went in; it changes Appendix K\'s opening paragraph (the Cochrane '
                      'line) and the first paragraph of Indirect language and re-entry cues ("That\'s where I \\"formally\\" '
                      'learned these techniques from..."); the headings and the Healing the Divided Self paragraph are as they were')

    assert not lost, lost
    out = []
    for j, r in enumerate(raw):
        out += new_raw.get(j, [r])
    new = '\n\n'.join(out) + '\n'
    after = hashlib.sha256(new.encode('utf-8')).hexdigest()
    nb = sr.blocks(new)
    # the links and italics in the Sources paragraphs survived
    for t in ('[article about self hypnosis](https://www.ishhypnosis.org/encyclopedia/self-hypnosis/)',
              "[Nimja's tutorial on hypnotic language patterns](https://learn.nimja.com/techniques/hypnotic_language)",
              '[his tutorial on triggers](https://learn.nimja.com/techniques/triggers)', '*Healing the Divided Self*'):
        assert t in new, t
    rec = {'answers': ANSWERS.name, 'answers_sha256': hashlib.sha256(ANSWERS.read_bytes()).hexdigest(),
           'review': str(REVIEW.relative_to(ROOT)), 'before_sha256': sha, 'after_sha256': after, 'fates': fates,
           'changed_blocks_before': sorted(new_raw), 'blocks': [len(bl), len(nb)], 'his_checks': HIS_CHECKS,
           'typos_fixed': [], 'his_words_kept_as_written': ['"imposterous" (his coinage)', '"and you breathe out" (question 31)',
                                                             'the heading "It feels fake" in quotes']}
    print(json.dumps(rec, indent=1, ensure_ascii=False))
    if a.check:
        return
    GUIDE.write_text(new, encoding='utf-8')
    (HERE / 'APPLIED-F1102-ANSWERS.json').write_text(json.dumps(rec, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    olds = {b['text'] for b in bl}
    changed = [b['text'] for b in nb if b['text'] not in olds]
    d = HERE / 'read'
    d.mkdir(parents=True, exist_ok=True)
    cr.record(d, findings=[], coverage=sorted({cr.phash(t) for t in changed}), dispositions={},
              article='HUMANIZED-SO-FAR.md at %s: the %d paragraphs his answers to the cards of 2 November (3) changed '
                      '(C-92 and C-480 approved, E-119, E-380 and E-762 his own versions, E-61 cut), read by the lead '
                      'session in place (E284, E294)' % (after[:8], len(changed)))


if __name__ == '__main__':
    main()
