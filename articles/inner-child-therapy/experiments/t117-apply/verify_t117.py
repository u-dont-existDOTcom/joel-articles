#!/usr/bin/env python3
"""Turn 117: each card's fate, checked in the guide as installed; and every word that differs from his file, listed.

  python3 articles/inner-child-therapy/experiments/t117-apply/verify_t117.py      (after apply_t117.py)

Writes DECISIONS.md: for each of the 44 cards, his answer (status and comment, word for word), what was done, and the
check that it is so in HUMANIZED-ARTICLE-SO-FAR.md; then every stretch where the guide's words differ from his file
(links, notes and quote marks set aside), so nothing changed that no card or answer asked for. Exit 1 when a check fails.
An approved card's check: its new words are in the guide and its old words are not, read the way the page showed them
(bold and links as plain text, his French quote marks as English ones, after Q1). A rejected or waiting card's: its
words are as they were."""
import difflib
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parents[1]
EXP = ART / 'experiments'
REVIEW = json.loads((EXP / 't116-review' / 'REVIEW.json').read_text(encoding='utf-8'))
ANSWERS = json.loads((EXP / 't117-answers' / 'ANSWERS-20261103-2332.json').read_text(encoding='utf-8'))
JOEL = (EXP / 't116-joel' / 'JOEL-GUIDE-20261103.md').read_text(encoding='utf-8')
FINAL = (ART / 'HUMANIZED-ARTICLE-SO-FAR.md').read_text(encoding='utf-8')
CHANGES = json.loads((HERE / 'CHANGES.json').read_text(encoding='utf-8'))
CARDS = {s['id']: s for s in REVIEW['suggestions']}
HIS = {a['id']: a for a in ANSWERS['items']}
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parents[3] / 'tools' / 'humanization'))
import typography_swap  # noqa: E402


def S(x):
    """X after the standard swap (E337 (gut)), which the build makes last."""
    return typography_swap.swap_text(x)[0]


def qn(s):
    """The text the way the page showed it, after Q1: no comments, links and bold as plain text, English quote marks."""
    s = re.sub(r'<!--.*?-->', '', s, flags=re.S)
    s = re.sub(r'\[([^\[\]]*)\]\s?\(<?[^()\s<>]+(?:\([^()\s]*\))?[^()\s<>]*>?\)', r'\1', s)
    s = s.replace('**', '').replace('*', '')
    s = re.sub(r'«[\xa0 ]?', '“', s)
    s = re.sub(r'[\xa0 ]?»', '”', s)
    s = re.sub(r'\xa0(?=[!?:;])', '', s)
    return S(s.replace('\xa0', ' '))


PLAIN = qn(FINAL)


def has(s):
    return qn(s) in PLAIN


def LATER(s):
    """A card's new words as a later card changed them (A5, on T4's Pharaoh: "what century" is "what year")."""
    return s.replace('what century', 'what year').replace('ntury Pharaoh', 'year Pharaoh')


def generic(card):
    """An approved card's edits: each change's new words (with a few words around) are in the guide, and its old ones not."""
    fails = []
    for e in card.get('edits', []):
        b, a = e['before'], e['after']
        if not a:
            if has(b) and len(b) > 3:
                fails.append('still there: "%s"' % b[:60])
            continue
        for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, b, a, autojunk=False).get_opcodes():
            if op == 'equal':
                continue
            nw = LATER(a[max(0, j1 - 12):j2 + 12])
            k = 12   # the old words with enough around them to be found once in his file
            while k < 60 and qn(JOEL).count(qn(b[max(0, i1 - k):i2 + k])) > 1:
                k += 6
            ow = b[max(0, i1 - k):i2 + k]
            if not has(nw):
                fails.append('new words not in the guide: "%s"' % qn(nw))
            if qn(ow) != qn(nw) and has(ow) and qn(ow) not in qn(nw):
                fails.append('old words still in the guide: "%s"' % qn(ow))
    return fails


def line_after(head, text):
    """The text comes right after the line HEAD (a heading, or the words ending a paragraph), past any notes."""
    i = FINAL.find(head)
    if i < 0:
        return False
    rest = re.sub(r'^(\s*<!--.*?-->\s*)*', '', FINAL[i + len(head):], flags=re.S).lstrip()
    return rest.startswith(text)


# his links (not his picture lines) and the four he typed with a space (the doubled one counted once), plus the last guide's that went back
N_LINKS = (len([m for m in re.finditer(r'\]\(([^)]*)\)', JOEL) if not m.group(1).startswith('Pictures/')]) + JOEL.count('] (') - JOEL.count('[[')   # the doubled link is one
           + sum(1 for c in CHANGES if c['why'] == "L1: the last guide's link back"))
P13 = re.sub(r'^\s*oops\. ok it should say:\s*', '', HIS['P13']['comment']).rstrip()
import apply_t117 as ap  # noqa: E402  (its DOG and notes; importing it applies nothing)

SPECIAL = {
    'L1': lambda: [] if (not re.search(r'\]\((?!https?://)', FINAL) and 'chatgpt.com' not in FINAL and 'shame.innerself' not in FINAL
                         and len(re.findall(r'\]\(https?://', FINAL)) == N_LINKS) else ['a link without https://, a chatgpt.com tag or the dead shame address, or not %d links' % N_LINKS],
    'L2': lambda: [x for x in ['40c24f21', 'f302980e', '4PxC3zZ2Mus', '718d0e76', 'somatic-modalities-strategic-sequencing', '4TYvq-d0-XM',
                               'EMBED https://ibogaqueen.substack.com/p/treasuring-the-inner-childs-gift', 'foHCbX0xjAU&t=58s', 'c4ab39d5',
                               '969adf28', 'bc40d36b'] if x not in FINAL],
    'L3': lambda: [] if ('uncropped%20study%20on%20pain.png' in FINAL and '10000001000002400000026F6724EE68' not in FINAL) else ['the uncropped screenshot'],
    'P10': lambda: [] if line_after('# Borrow Your Love For Someone Else\n', ap.DOG) else ['the dog paragraph under Borrow Your Love For Someone Else'],
    'P11': lambda: [] if (not has('starting with pleasure and pain, and gain and loss')
                          or 'joel-118-four-pairs' in (ART / 'OWNER-EDITS.json').read_text(encoding='utf-8')) else ['the four pairs are back'],
    'P12': lambda: [] if has('so “meet the protector first” would fit right in over there') and not has('my section, “meet') else ['P12'],
    'P13': lambda: [] if P13 in FINAL else ['his re-do text, word for word'],
    'R4': lambda: [] if has('to close out properly. Re-evaluation Counseling, a global movement of peer counseling, always ends on this “Present Time” reminder.') else ['R4: the sentence moved'],
    'C2': lambda: [] if not has('Do the same if you can’t stop yourself') else ['the crisis sentence is back'],
    'A1': lambda: [] if has('My ex, X, taught me') and has('another ex of mine (X)') and 'Xandria' not in FINAL else ['A1'],
    'A2': lambda: [] if has('As Lao Tsu might have said (if I could ever have read that whole boring Art of War book)') else ['A2'],
    'A3': lambda: [] if has('“What’s a ‘boundary’?”, I might be asking.') else ['A3'],
    'A4': lambda: [] if S('so that you:\n\n### Don’t Sell Your Inner Adult To Buy An Outer Adult') in FINAL else ['A4'],
    'A5': lambda: [] if has('like what year Pharaoh Tutankhamun was crowned') else ['A5'],
    'A6': lambda: [x for x in ['Instead of Blame', 'Just Like Me', 'Ideal Parent Figure', 'If a part hesitates about being touched',
                               'Then borrow.', 'The inner Guide is the closest thing here to a Higher Self'] if has(x)],
    'F1': lambda: [] if line_after('as best as I can fit:\n', '<!--') or '718d0e76' in FINAL.split('as best as I can fit:')[1][:200] else ['F1'],
    'F2': lambda: [] if (line_after('## Gentle Meditation and Mantra\n', 'If the hook is stuck')
                         and FINAL.split('## Gentle Meditation and Mantra\n')[1].lstrip().startswith('<!-- EMBED https://www.youtube.com/watch?v=JQs2watlFws')
                         and '\n## https://' not in FINAL) else ['F2: his video moved or still a heading'],
    'F3': lambda: [] if '\n## What to Make of a Passing Feeling\n' in FINAL and '\n### What to Make' not in FINAL else ['F3'],
    'F4': lambda: [] if (line_after('### The Joy In Sorrow\n', S(ap.CARDS['F4']['inserts'][0]['text'])) and '\n### Jelaluddin' not in FINAL
                         and 'PULL QUOTE' in FINAL.split('### The Joy In Sorrow')[1][:400]) else ['F4'],
    'F5': lambda: [x for x in ['\n## Finding People and Building Trust\n', '\n## When One Life Has Ended', '\n## The Love Has to Move\n'] if x not in FINAL],
    'F6': lambda: [] if S('\n##### Mo’ Money, Mo’ Problems\n') in FINAL else ['F6'],
    'Q1': lambda: [] if ('«' not in FINAL and '»' not in FINAL and not re.search(r'\xa0[!?:;]', FINAL) and FINAL.count(' :)') == 2
                         and typography_swap.swap_text(FINAL)[1] == 0) else ['Q1, or a curly mark or em dash left after the swap'],
}
DONE = {
    'L1': 'Links back: the last guide\'s, where his words and their sentence still are (52), his typed ones made real, and the card\'s fixes. One stays out: "definitely not with others" in the thug story, where he put his own link on "not with others".',
    'L2': 'All eleven of the live post\'s pictures and videos as notes where they go, not only the seven the card named: it missed the mantra video, the Cosmic Jackpot picture, the Treasuring post card and Key\'s audio meditation. Key\'s audio followed an intro line his guide no longer has, so it goes after Key\'s paragraph.',
    'L3': 'His uncropped screenshot in place of the cropped one.',
    'P10': 'His dog paragraph back, in his characters from the last guide (straight apostrophes; the card showed curly ones by mistake).',
    'P11': 'Rejected: the four pairs stay out. The heading still says "Four Pairs That Commonly Hook the Child": one question about it in this turn\'s message.',
    'P12': 'Cut "my section," (so “meet the protector first” would fit right in over there).',
    'P13': 'His text in place of the sentence, word for word.',
    'R4': 'Waiting, a "leave" card: no change.',
    'C1': 'Cut "(which is called «therapeutic holding» in the literature)", and the full stop inside the quote.',
    'C2': 'Rejected: the crisis sentence stays out.',
    'A1': 'The other Xandria is X: "My ex, X, taught me".',
    'A2': 'Kept, and on the article\'s keep-as-is list (KEEP-AS-IS.json), so no card asks about it again.',
    'A3': 'Kept ("I" is right: he is learning this too), and on the keep-as-is list.',
    'A4': 'Kept, and on the keep-as-is list.',
    'A5': '"what century" is "what year".',
    'A6': 'The cuts stay cut, and are on the keep-as-is list\'s list of cuts he meant.',
    'F1': 'The study chart where the "." was (the "." goes).',
    'F2': 'Rejected: his video stays where he put it, a line and not a heading (his file had it in Heading 2 style), so Substack makes it a video; the mantra video goes back after "For the Benefit of All Beings:" with the address he gave. The empty heading line in Close the Session (no words), which was also on this card, went.',
    'F4': 'The quote is the first paragraph of The Joy In Sorrow, quote marks closed, with a note to make it a pull quote in Substack.',
    'F6': 'An h5.',
    'Q1': 'English quote marks (35 pairs) and no space before ! ? : ; (38). The card said 40 spaces: two of those are the smileys " :)", which keep theirs. Then, last, the standard swap of every article since 2026-11-03 (E337 (gut), "yes make that swapping standard"): all quote marks straight, these included, and each em dash a spaced en dash.',
}


def main():
    rows, bad = [], 0
    for s in REVIEW['suggestions']:
        sid = s['id']
        a = HIS[sid]
        st = a['status']
        if sid in SPECIAL:
            fails = SPECIAL[sid]()
        elif st == 'approved':
            fails = generic(s)
        else:
            fails = ['no check']
        if sid == 'T1':
            fails += [x for x in ('A**n**', 'free as a bird.** **And') if x in FINAL]
        bad += bool(fails)
        done = DONE.get(sid) or ('Done as the card showed.' if st == 'approved' else 'No change.')
        rows.append((sid, s['title'], st, (a.get('comment') or '').strip(), done, fails))
    # every word that differs from his file
    jw, fw = qn(JOEL).split(), qn(FINAL).split()
    diffs = []
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, jw, fw, autojunk=False).get_opcodes():
        if op != 'equal':
            diffs.append((' '.join(jw[max(0, i1 - 3):i2 + 3]), ' '.join(fw[max(0, j1 - 3):j2 + 3])))
    out = ['# Turn 117: his answers on the turn-116 marking page, and what was done', '',
           'His answers, exported from the page at 2026-11-03 23:32 UTC: [ANSWERS-20261103-2332.json](../t117-answers/ANSWERS-20261103-2332.json). '
           'Put in by [apply_t117.py](apply_t117.py) (every change, old and new: [CHANGES.json](CHANGES.json)); checked by '
           '[verify_t117.py](verify_t117.py) in the guide as installed, [HUMANIZED-ARTICLE-SO-FAR.md](../../HUMANIZED-ARTICLE-SO-FAR.md).', '',
           '%d cards, %d with a failed check. The last step of the build is the standard swap (E337 (gut)): every curly quote mark '
           'straight and each em dash a spaced en dash, so the checks below read both texts after it.' % (len(rows), bad), '',
           '| Card | Title | His answer | His comment | What was done | Check |', '|---|---|---|---|---|---|']
    for sid, title, st, cm, done, fails in rows:
        cell = lambda x: x.replace('|', '\\|').replace('\n', ' / ')
        out.append('| %s | %s | %s | %s | %s | %s |' % (sid, cell(title), st, cell(cm), cell(done), 'FAIL: ' + cell('; '.join(fails)) if fails else 'ok'))
    out += ['', '## Every stretch where the words differ from his file', '',
            'Read the way the page showed his file (links, bold and notes as plain text, English quote marks), so what is '
            'left is what a card or an answer changed. %d stretches; the changes log names each one\'s card.' % len(diffs), '']
    for o, n in diffs:
        out.append('- his: %s\n  now: %s' % (o.replace('\n', ' '), n.replace('\n', ' ')))
    (HERE / 'DECISIONS.md').write_text('\n'.join(out) + '\n', encoding='utf-8')
    print('cards %d, failed checks %d, stretches that differ %d' % (len(rows), bad, len(diffs)))
    for sid, title, st, cm, done, fails in rows:
        if fails:
            print('FAIL', sid, fails[:4])
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main())
