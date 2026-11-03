"""The hypnosis guide's cards of 1 November, after my second full read and the read for contradictions (REVIEW-FR2.json,
.html, .artifact.html, .md).

Joel, 2026-11-01 18:57 UTC: read the whole guide again (R-508: "we gotta read this whole guide again"), and "we should
also go thru the guide to make sure stuff isn't contradicting other stuff". The read's findings in our words are in the
guide already (../apply_fullread2.py); what it found in his own words comes to him here, in the marking page's form
(tools/humanization/suggestion_review.py, gate E265):
- F1.6 and F18.1: two lines of his that the guide now says twice (his rule: say a thing once);
- F7.5: his fingers script (his version of 30 October, N-276) steps back down on its last press;
- K9: his step 3 of Before you begin against the guide's own sessions on loveyhuasca (../CONTRADICTIONS.md).
The page also lists the punctuation and the two typos fixed in his words without a card (C-3, E308).

  python3 articles/inner-signal/humanize/fix-20261101/fullread2/review/build_page_fr2.py
"""
import collections
import datetime
import hashlib
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
D = HERE.parent
H = D.parents[1]
ROOT = H.parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
sys.path.insert(0, str(D))
import suggestion_review as sr  # noqa: E402
from apply_fullread2 import TOUCHES_HIS  # noqa: E402

BLOB = 'https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/community-joel-1018/'
LANE = 'articles/inner-signal/humanize/'
ARTICLE = LANE + 'HUMANIZED-SO-FAR.md'
GIT_FILE = LANE + 'fix-20261101/fullread2/review/REVIEW-FR2.html'
MD = (H / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
BL = sr.blocks(MD)
READ = 'My second full read of the guide, beside your published version (1 November)'
CONTRA = 'The read for contradictions (1 November)'

TYPES = {
    'repeat': {'label': 'Said twice',
               'about': 'Your words, in the guide twice. The card keeps them in one place. Approve, Reject or Revise.'},
    'yours': {'label': 'Your own words',
              'about': 'A suggestion for a sentence you wrote. Approve uses the suggestion; Reject keeps your words; '
                       'Revise lets you write your own.'},
    'contradiction': {'label': 'Contradiction',
                      'about': 'Your words here say something another part of the guide takes back. Approve, Reject or '
                               'Revise.'},
}


def block_with(s, section=None):
    hits = [b['i'] for b in BL if s in b['text'] and (section is None or b['section'] == section)]
    assert len(hits) == 1, (s[:60], hits)
    return hits[0]


def card(cid, typ, title, i, old, new, what, why, stays, deciding, note, found, label=None):
    t = BL[i]['text']
    assert t.count(old) == 1, (cid, old[:60])
    k = t.find(old)
    s = {'id': cid, 'type': typ, 'title': title, 'where': sr.where(BL, i),
         'spans': [{'block': i, 'start': k, 'end': k + len(old.rstrip())}],
         'edits': [{'block': i, 'before': t, 'after': t.replace(old, new)}], 'inserts': [], 'moves': [],
         'what': what, 'why': why, 'stays': stays, 'advice': 'approve', 'advice_note': note, 'found_by': found,
         'deciding': deciding}
    if label:
        s['approve_label'] = label
    return s


def main():
    S = []
    # F1.6: his dad's line, in full in Affirmations Done Right (published) and in his step 6 (T-495, 30 October)
    i44 = block_with('My dad always said: “Always, and in everything, expect the very best.')
    i = block_with('As my dad always said, "Always and in everything, expect the very best.')
    old = ('As my dad always said, "Always and in everything, expect the very best. But be prepared to take what you get. '
           'The best might come afterwards!"')
    new = 'As my dad always said, "Be prepared to take what you get. The best might come afterwards!"'
    S.append(card('F1.6', 'repeat', '“As my dad always said …”', i, old, new,
                  'In step 6 of Before you begin, your dad’s line keeps the half this step is about, “Be prepared to take '
                  'what you get. The best might come afterwards!” The whole line stays where you explain it, at the start '
                  'of Affirmations Done Right.',
                  'Your dad’s line is in the guide twice, word for word: it opens Affirmations Done Right (as you published '
                  'it), and it is in your version of step 6 (30 October). In Affirmations Done Right it is the subject; '
                  'here the step is about what to do when nothing changes, which is the line’s second half.',
                  'Affirmations Done Right as it is, and the rest of step 6 word for word.',
                  'Approve uses the shorter line in step 6; Reject keeps it in full in both places; Revise lets you write '
                  'your own.',
                  'I’d approve: the line still comes back in step 6, where it helps, without the whole of it again.',
                  READ, 'use this wording'))
    assert i44 < i
    # F7.5: his fingers script (N-276) steps back down on its last press
    i = block_with('you bring yourself into a clear state of awareness.')
    old = 'you bring yourself into a clear state of awareness.'
    new = 'you bring yourself into the clearest state of awareness yet.'
    S.append(card('F7.5', 'yours', '“… into a clear state of awareness”', i, old, new,
                  '“you bring yourself into a clear state of awareness” becomes “you bring yourself into the clearest '
                  'state of awareness yet”.',
                  'The script steps up, from “a place of clearer awareness” to “an even clearer state of awareness”, and '
                  'then back down to “a clear state of awareness”, on the press that should take it furthest. In your '
                  'published version each press takes you further (“Again — clearer, not sleepier.”). The sentence is in '
                  'your version of the script (30 October), so it’s yours to decide.',
                  'The rest of the script, word for word.',
                  'Approve uses the new wording; Reject keeps yours; Revise lets you write your own.',
                  'I’d approve: it keeps your words and makes the last press the clearest, as your published script does.',
                  READ, 'use this wording'))
    # K9: step 3 of Before you begin against the guide's sessions on loveyhuasca
    i = block_with('If you are intoxicated and/or more confused than usual')
    for s_ in ('I found that especially amplified with loveyhuasca.', 'already open for some reason (loveyhuasca,',
               'Self-hypnosis can be powerful when you are in an altered state of consciousness'):
        block_with(s_)
    S.append(card('K9', 'contradiction', '“If you are intoxicated and/or …”', i,
                  'intoxicated and/or more confused than usual', 'intoxicated and more confused than usual',
                  '“intoxicated and/or more confused than usual” becomes “intoxicated and more confused than usual”.',
                  'As it is, being intoxicated is by itself a reason to get support instead of doing exploratory hypnosis. '
                  'Elsewhere the guide does self-hypnosis on loveyhuasca: your own sessions in Why doing it myself worked '
                  'better for me, Already Trancey? (for when you’re already open, loveyhuasca first in its list), and '
                  'Stabilize before you interpret (“Self-hypnosis can be powerful when you are in an altered state of '
                  'consciousness (e.g. when you’re on loveyhuasca …”). With “and”, the stop is for being intoxicated and '
                  'more confused than usual, and the rest of the sentence (“or for whatever reason not able to keep '
                  'yourself safe”) still stops anyone a substance has made unsafe.',
                  'The rest of step 3 word for word, with its pointer to Already Trancey? for when you’re already open.',
                  'Approve uses “and”; Reject keeps “and/or”; Revise lets you write your own.',
                  'I’d approve: step 3 then agrees with your own sessions and Appendix G, and it still stops anyone who '
                  'isn’t safe.',
                  CONTRA, 'use this wording'))
    # F18.1: his inner child guide's line, at the end of Finish without forcing a revelation and in the care workshop
    block_with('tell your little one, "That’s enough for today. We’re going back to the life we’re building."')
    i = block_with('Tell your little one, "That\'s enough for today. We\'re going back to the life we\'re building."')
    old = 'Tell your little one, "That\'s enough for today. We\'re going back to the life we\'re building." '
    S.append(card('F18.1', 'repeat', '“That\'s enough for today …”', i, old, '',
                  'Cuts “Tell your little one, "That\'s enough for today. We\'re going back to the life we\'re building."” '
                  'from the care workshop (Appendix J). The line stays at the end of Finish without forcing a revelation.',
                  'Your line from your inner child guide is in the guide twice: at the end of Finish without forcing a '
                  'revelation, where every session ends, and here in the care workshop. The workshop closes in its next '
                  'sentence anyway (“Close the workspace, reassure yourself that you are one whole person, that you\'re '
                  'an adult now, and come back.”).',
                  'The line in Finish without forcing a revelation, and the rest of the care workshop word for word.',
                  'Approve cuts it here; Reject keeps it in both places; Revise lets you write your own.',
                  'I’d approve: the line is said once, where every session ends, and the workshop still closes the same '
                  'way.',
                  READ, 'cut it'))
    S.sort(key=lambda s: (s['spans'][0]['block'], s['spans'][0]['start']))
    n = collections.Counter(s['type'] for s in S)
    applied = json.loads((D / 'APPLIED-FULLREAD2.json').read_text(encoding='utf-8'))
    fates = applied['fates']
    review = {
        'format': sr.FORMAT, 'review_id': 'inner-signal-hypnosis-guide-cards-20261101',
        'title': 'Hypnosis Guide Cards, 1 November',
        'intro': [
            'Your hypnosis guide as it is in Git, after my second full read of it (every paragraph, beside your '
            'published version) and the read for contradictions you asked for.',
            'The read found %d things. The %d in our words (Emulate\'s or mine) are fixed in the guide already, and so '
            'are the eight contradictions in our words; the two-hand practice is taught once now, as you asked. What it '
            'found in your own words is here: <b>%d lines said twice</b>, <b>one suggestion</b> for your fingers script, '
            'and <b>one contradiction</b>. Approve, Reject or Revise.' % (
                applied['findings'], fates['fixed'] - len(TOUCHES_HIS), n['repeat']),
            'In your own words, only punctuation and a few slips changed without a card (two typos, an "ie." that means '
            '"for example", and a label in front of your words that wasn\'t yours), as you said for commas. The Markdown '
            'copy of this page lists each one, before and after.',
            'Your answers save as you click. When you\'re done, click <b>Copy my answers</b> (or <b>Save them as a '
            'file</b>) and send them to me.',
        ],
        'git_file': GIT_FILE, 'article': {'file': ARTICLE, 'sha256': hashlib.sha256(MD.encode('utf-8')).hexdigest()},
        'links': {'guide': BLOB + ARTICLE, 'review': BLOB + LANE + 'fix-20261101/fullread2/review/REVIEW-FR2.md'},
        'built': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M UTC'),
        'types': TYPES, 'suggestions': S,
    }
    probs = sr.check(review, BL)
    for p in probs:
        print('PROBLEM', p)
    (HERE / 'REVIEW-FR2.json').write_text(json.dumps(review, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    if probs:
        sys.exit(1)
    page = sr.page(review, MD, BL)
    (HERE / 'REVIEW-FR2.html').write_text(page, encoding='utf-8')
    (HERE / 'REVIEW-FR2.artifact.html').write_text(sr.artifact_view(page), encoding='utf-8')
    (HERE / 'REVIEW-FR2.md').write_text(cards_md(review), encoding='utf-8')
    print(len(S), 'cards:', dict(n))


def marked(j, spans):
    t = BL[j]['text']
    for sp in sorted((x for x in spans if x['block'] == j), key=lambda x: -x['start']):
        t = t[:sp['start']] + '**' + t[sp['start']:sp['end']] + '**' + t[sp['end']:]
    return t


# what each change made without a card is, said to him (apply_fullread2.TOUCHES_HIS has the record's reasons)
SAID = {
    'F6.11': 'two typos in your version of 1 November: a missing "with", and "its" for the plural "methods"',
    'F7.6': 'the closing quotation mark of your script (a straight one, after a curly opening one)',
    'F11.17': 'the "DO NOT:" label and "Utilize", which weren\'t yours (Emulate\'s, in front of your words); your '
              '"guard parts" stays',
    'F13.5': 'after "dialog rhythm", a comma for the colon, and "for example:" for "ie." (which means "that is")',
    'F13.19': 'quotation marks around the five questions (straight ones, like the others in your paragraph) and a comma '
              'after "Instead"; your words as they are',
}


def touches_his():
    """The changes in his words made without a card (apply_fullread2.TOUCHES_HIS): [(where, what, old, new)]."""
    out = []
    assert set(SAID) == set(TOUCHES_HIS)
    for fid in TOUCHES_HIS:
        why = SAID[fid]
        n = int(fid[1:].split('.')[0])
        old, new = json.loads((D / ('FIXES-%d.json' % n)).read_text(encoding='utf-8'))[fid]
        hit = [b['i'] for b in BL if new.strip('\n') in b['text']]
        assert len(hit) == 1, (fid, len(hit))
        out.append((sr.where(BL, hit[0]), why, old.strip('\n'), new.strip('\n')))
    return out


def cards_md(review):
    """Every card as a page GitHub renders, in the guide's order (the page's readable copy in Git)."""
    types = review['types']
    out = ['# %s: every card' % review['title'], '',
           'The page\'s cards as text, in the order of the guide. Built %s from [the guide so far](%s). To answer, use '
           'the page; or write your answer under a card\'s number in a message to me.' % (
               review['built'], review['links']['guide']), '']
    section = None
    for s in review['suggestions']:
        b = s['spans'][0]['block']
        if BL[b]['section'] != section:
            section = BL[b]['section']
            out += ['## %s' % (section or 'The opening'), '']
        out += ['### %s: %s (%s)' % (s['id'], s['title'], types[s['type']]['label']), '']
        for e in s['edits']:
            out += ['**Now** (the words it changes in bold):', '', '> %s' % marked(e['block'], s['spans']), '',
                    '**How it would read:**', '', '> %s' % e['after'], '']
        out += ['**Why:** %s' % s['why'], '', '**My advice:** %s' % s['advice_note'], '']
    out += ['## Your words changed without a card', '',
            'Punctuation and a few slips in your own words, fixed in the guide without a card, as you said for commas '
            'on 1 November ("you didn\'t need to ask me for commas if they are clearly needed"). Tell me if any of them '
            'should go back.', '']
    for where, why, old, new in touches_his():
        out += ['- **%s**: %s.' % (where, why), '', '  Before: %s' % old, '', '  After: %s' % new, '']
    return '\n'.join(out).replace('\n\n\n', '\n\n') + '\n'


if __name__ == '__main__':
    main()
