#!/usr/bin/env python3
"""Turn 111: OWNER-EDITS.json after his answers of 2026-10-25 20:08 UTC (apply_t111.py). Seven entries whose strings his
decisions changed get the new text and a history note; one new entry records every decision, with what the article must
and mustn't contain now. Applied once; it refuses to run again."""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
P = HERE.parents[1] / 'OWNER-EDITS.json'
ART = HERE.parents[1] / 'HUMANIZED-ARTICLE-SO-FAR.md'
WHEN = 'Turn 111 (his answers of 2026-10-25 20:08 UTC, experiments/t111-answers/ANSWERS-20261025-2008.json)'
data = json.loads(P.read_text(encoding='utf-8'))
assert not any(e['id'] == 'joel-111-20261025' for e in data['entries']), 'already applied'
E = {e['id']: e for e in data['entries']}
md = re.sub(r'<!--.*?-->', '', ART.read_text(encoding='utf-8'), flags=re.S)


def para(start):
    hits = [p.strip() for p in md.split('\n\n') if p.strip().startswith(start)]
    assert len(hits) == 1, start
    return hits[0]


def note(e, text):
    e.setdefault('history', []).append(WHEN + ': ' + text)


# the seven his decisions changed
e = E['ldw-p8-actual-exchange']
e['must_contain'] = [x for x in e.get('must_contain', []) if not x.startswith('Like the two truths at bedtime')]
e.setdefault('must_not_contain', []).append('Like the two truths at bedtime, a true complaint and real love')
note(e, 'C5 approved: the proposal\'s last sentence ("Like the two truths at bedtime ...") is cut; the scene ends on "Thank you for that perspective."')

e = E['pr-opening-installed']
old = 'A real-life child of yours, or a calm pet, can also act as a companion that brings out the relationship with your own inner child. But those are also their own beings with their own needs as well. Let them come and go without making them responsible for the session.'
for k in ('must_contain', 'must_contain_exact'):
    if old in e.get(k, []):
        e[k] = [para('A real-life child of yours') if x == old else x for x in e[k]]
note(e, 'P5 approved: his 2026-10-02 answer as an article sentence after the first ("My son did that for me, and I think that\'s very common for parents.").')

e = E['bus-h3']
i = md.index('### Hear the Guard First')
j = md.index('\n### ', i + 10)
guard = [p.strip() for p in md[i:j].split('\n\n')[1:] if p.strip()]
assert len(guard) == 7 and guard[1].startswith('It might say')
e['must_contain_exact'] = ['### Hear the Guard First'] + guard
e['order'] = ['Two Common Guarding Patterns', 'Hear the Guard First', 'Whichever protective part showed up', 'It might say this will just be one more performance',
              'A harder voice can seem more fitting', "A new roommate doesn't win you over", "That part doesn't have to move out.",
              "If it's been calling all this stupid", 'Blaming yourself can be doing a protective job, too.']
note(e, 'S1 approved: the agreed order (experiments/t110-review/AGREED.md, reshape_t110.py), seven paragraphs.')

e = E['bus-p4-proposal']
olds = [x for x in e.get('must_contain_exact', []) + e.get('must_contain', []) if 'call it off if things got to be too much' in x]
new = ("It can keep watch while you take one small step toward your little one. I think watching is what it wants anyway, to find out "
       "if there's a grown-up here now who could call it all off if things got to be too much.")
for k in ('must_contain', 'must_contain_exact'):
    if k in e:
        e[k] = [new if 'call it off if things got to be too much' in x else x for x in e[k]]
assert olds, 'bus-p4-proposal had no string to update'
note(e, 'S1 approved: the sentence is two ("toward your little one. I think watching"), with "call it all off" (the cold read), both admitted by the owner-delivery gate.')

e = E['ba-p2-joel-20261017']
for k in ('must_contain', 'must_contain_exact'):
    if k in e:
        e[k] = [para('Over time, reparenting can help you take in') if x.startswith("Say they're the one who always remembers your appointments.") else x for x in e[k]]
e.setdefault('must_not_contain', []).append("Say they're the one who always remembers your appointments.")
note(e, 'his cut, with C10: "i\'m surprised you didn\'t notice the next sentence after this is redundant. cut "Say they\'re the one who always remembers your appointments.""')

e = E['close-session-20261018']
e['must_contain'] = [x for x in e.get('must_contain', []) if x != 'Going back to your life is part of the healing, too.']
e.setdefault('must_not_contain', []).append('Going back to your life is part of the healing, too.')
note(e, 'C7 approved: "Going back to your life is part of the healing, too." is cut; the section ends on "whatever you\'re still feeling can come along."')

e = E['joel-109-20261025']
e['must_not_contain'] = [x for x in e['must_not_contain'] if x != 'It might say this will just be one more performance']
note(e, 'S1 approved: "It might say", his word from before turn 109, is back, since the sentence follows his question again.')

# the record of every decision
data['entries'].append({
    'id': 'joel-111-20261025',
    'status': 'applied',
    'what': 'His answers from the turn-110 review sheet: S1 approved; S3 in his version ("this person"); cuts C3 to C9, C11, C12 approved; C10 '
            'rejected with his added sentence and his cut of the next paragraph\'s first sentence; P2 and P5 approved; P6 in his version (his '
            'sentence for Just Like Me P2, the tonglen link kept) with his cut in P1; Q1 his sentence; Q2 and Q3 answered with their basis '
            '("people i know"; "People in Re-evaluation Counseling say this especially. it\'s also sort of common therapy advice"), no text '
            'change. Installed by experiments/t111-installs/apply_t111.py.',
    'joel': '2026-10-25 20:08 UTC (the sheet\'s export) and 20:14 UTC (experiments/t111-answers/JOEL-20261025-2014.md)',
    'where': 'Hear the Guard First; Before You Tell the Hardest Stuff; Ill Will and Loving-Kindness; Borrow Love; Love Doesn\'t Have to Wait; '
             'Catch the Hook; Close the Session; Untangling the Belonging Bargains; Let the Child Be Bad at Things; Borrowed Adulthood in '
             'Relationship; How to Forgive Without Forgetting; Missing Someone; Don\'t Give the Inner Adult Away; Remind Yourself; Just Like Me; '
             'If the Love Isn\'t Coming Yet',
    'must_contain': [
        'So I’d ask this person, before handing over any tricky specifics',
        "Having someone like that while you're struggling can be an enormous blessing. If it's more distributed, with various people you can count on for small parts, that can be more sustainable, even if it doesn't feel as monumental.",
        "This is sort of a gentler version of Tibetan Buddhism's [tonglen](https://www.lionsroar.com/how-to-practice-tonglen-meditation/) practice (which I learned from Pema Chödrön), where we imagine taking in the suffering of others, transmuting it in our heart, and sending out love and peace to them.",
        'Once a truce is made, we can begin to let down our defenses.',
        "I'd keep what you feel around them in mind, and look at their track record too.",
        "My son did that for me, and I think that's very common for parents.",
        "I'd still keep the Nurturer voice.",
        'Blaming yourself can be doing a protective job, too.',
    ],
    'must_not_contain': [
        'So I’d ask them, before handing over', "So it's worth noticing what it's doing to you.",
        "The quest for self-knowledge is a life's journey", 'Sometimes human beings need to be being, not always doing.',
        'Either way, that\'s pl/ork in its most literal form', ', which is ordinary', '(nobody gets a gold star for forgiving fastest)',
        "(nobody's checking their inbox)", 'Some of them make it worse trying to get away from it.', "I'd leave out forgiving them",
        'What people most often say helped', "I'd keep whatever you feel around them",
    ],
})
P.write_text(json.dumps(data, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('updated 7, added joel-111-20261025')
