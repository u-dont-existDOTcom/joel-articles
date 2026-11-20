#!/usr/bin/env python3
"""apply_r45.py - his round-45 answers (ANSWERS-R45-20261120-1820.json, exported 2026-11-20 18:20:10 UTC) into the guide.
Each version goes in whole, from his last check (../../humanize/h61-20261120/HIS-CHECKS-R45.json):

- TEACH-HARM-GOD (revised; a2f4be55, Human High 100): B286, his paragraph with the script line in quotes, starting from
  what they believe ("Yes, I know you are God. ..."), and the arguing and nodding sentences said as the alternatives they
  are. His question with it, "but now you have to take out p2 right?": P2 on the page is "Non-combative philosophical
  grounding:", the label of the script (P3) his paragraph now quotes from; the label and the script go (B287, B288), and
  "Other useful lines: ..." (B289) follows his paragraph. What goes, kept here and in REMOVED-R45.json so it can come
  back: "I hear how vast and certain this feels." (his "Yes, I know you are God." starts from the same place), "Many
  traditions say God is in everyone. That makes every body sacred, not disposable." (his quoted line), "Peace is the
  godly move tonight.", "No proof is needed." (B289: "no proof", "Divine doesn't need a violent test") and "We protect
  life and sleep first." (B289: "no harm ... sleep first").
- TEACH-TOUCH (revised; 39cd2ecf, Human High 149): B391 and B392, his two paragraphs. The question keeps the bold the guide
  gave it (formatting, not words).
- DEMONS-HOOKS (answered; 3a1603ee, Human High 87): B401 and B404, option B with "Turn the lights down, and get them
  whatever help they need." ("i don't like always telling to go to a doctor"). The card's answer has no "Your version",
  so the text is his check's, with the leading space and the four-space indent his copy from the card carried left out.

  python3 articles/bad-trips/review/r45/apply_r45.py      (from the repo root)
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parents[1]
BJ = ART / 'GUIDE-SO-FAR-blocks.json'
MD = ART / 'GUIDE-SO-FAR.md'
ANS = json.loads((HERE / 'ANSWERS-R45-20261120-1820.json').read_text(encoding='utf-8'))
A = {i['id']: i for i in ANS['items']}
CHECKS = json.loads((ART / 'humanize' / 'h61-20261120' / 'HIS-CHECKS-R45.json').read_text(encoding='utf-8'))


def tidy(t):
    return re.sub(r'([,.]) {2,}', r'\1 ', t.strip())


def plain(md):
    return re.sub(r'(?<!\*)\*(?!\*)', '', md.replace('**', ''))


HARM = tidy(A['TEACH-HARM-GOD']['your_version'])
TOUCH_1, TOUCH_2 = [tidy(p) for p in A['TEACH-TOUCH']['your_version'].split('\n\n')]
Q = '"Would respectful touch help, or would you rather have space?"'
assert TOUCH_1.count(Q) == 1
TOUCH_1_MD = TOUCH_1.replace(Q, '**%s**' % Q)
# his demons version, from his check 3a1603ee (the question card has no "Your version"); read back on 2026-11-20
DEMONS_CHECKED = (" It might look passive, but this is how you become unhookable. When you meet a demon with love, the demon "
                  "has nothing to hook into, since its hooks catch on hatred, fear, pride and grandiosity, not on love.\n    "
                  "If someone's too overwhelmed to send love, because they're sick or too scared to think straight, help them "
                  "get steady first. Turn the lights down, and get them whatever help they need. Once they can think straight "
                  "again, you can teach them to send the demon love.")
DEMONS_1, DEMONS_2 = [tidy(p) for p in DEMONS_CHECKED.split('\n')]
assert 'whatever help they need' in A['DEMONS-HOOKS']['comment'] and DEMONS_2 in A['DEMONS-HOOKS']['comment']
assert DEMONS_1 in A['DEMONS-HOOKS']['comment']
REMOVED = {'B287': '**Non-combative philosophical grounding:**',
           'B288': ('> I hear how vast and certain this feels. Many traditions say God is in everyone. That makes every body '
                    'sacred, not disposable. Peace is the godly move tonight. No proof is needed. We protect life and sleep '
                    'first.')}


def main():
    assert A['TEACH-HARM-GOD']['status'] == 'revise' and A['TEACH-TOUCH']['status'] == 'revise'
    assert A['DEMONS-HOOKS']['status'] == 'answered'
    # each version is the text of his last check, word for word
    last = {k: v[-1]['link'].rsplit('/', 1)[-1][:8] for k, v in CHECKS['cards'].items()}
    assert last == {'TEACH-HARM-GOD': 'a2f4be55', 'TEACH-TOUCH': '39cd2ecf', 'DEMONS-HOOKS': '3a1603ee'}, last
    B = json.loads(BJ.read_text(encoding='utf-8'))
    assert '\n\n'.join(b['md'] for b in B) + '\n' == MD.read_text(encoding='utf-8')
    ids = [b['id'] for b in B]
    blk = lambda i: B[ids.index(i)]

    assert plain(blk('B286')['md']) in (A['TEACH-HARM-GOD']['before'], HARM)
    blk('B286')['md'] = HARM
    for i, old in REMOVED.items():
        if i in ids:
            assert blk(i)['md'] == old, (i, blk(i)['md'][:80])
    B = [b for b in B if b['id'] not in REMOVED]
    ids = [b['id'] for b in B]
    assert ids[ids.index('B286') + 1] == 'B289'

    t1, t2 = A['TEACH-TOUCH']['before'].split('\n\n')
    assert plain(blk('B391')['md']) in (t1, TOUCH_1) and plain(blk('B392')['md']) in (t2, TOUCH_2)
    blk('B391')['md'], blk('B392')['md'] = TOUCH_1_MD, TOUCH_2

    assert blk('B401')['md'] in (
        "It might look passive, but this is how you become unhookable. A demon can fight your hatred, feed on your fear, "
        "argue with your pride or seduce your grandiosity, but there's nothing in love for it to grab.", DEMONS_1)
    assert blk('B404')['md'] in (
        "When somebody is medically, physically, or psychologically too overwhelmed to reach love, stabilize first. Don't "
        "teach nondual demonology to somebody who needs the lights down and a doctor.", DEMONS_2)
    blk('B401')['md'], blk('B404')['md'] = DEMONS_1, DEMONS_2

    MD.write_text('\n\n'.join(b['md'] for b in B) + '\n', encoding='utf-8')
    BJ.write_text(json.dumps(B, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    (HERE / 'REMOVED-R45.json').write_text(json.dumps({
        'about': ('Blocks taken out by apply_r45.py at his question "but now you have to take out p2 right?" (TEACH-HARM-GOD, '
                  '2026-11-20 18:20 UTC): the script\'s label (the page\'s P2) and the script it labels, which his paragraph '
                  'now quotes from. To put them back, insert them after B286 in this order.'),
        'after': 'B286', 'blocks': [{'id': k, 'md': v} for k, v in REMOVED.items()]}, ensure_ascii=False, indent=1) + '\n',
        encoding='utf-8')

    OE = ART / 'OWNER-EDITS.json'
    oe = json.loads(OE.read_text(encoding='utf-8'))
    have = {e['id'] for e in oe['entries']}
    by = 'review/r45/ANSWERS-R45-20261120-1820.json (exported 2026-11-20 18:20:10 UTC), put in by review/r45/apply_r45.py'
    new = [
     {'id': 'r45-harm-his', 'status': 'applied',
      'what': ('When What They Say Turns Toward Harm, his first paragraph (round 45, TEACH-HARM-GOD; his check a2f4be55, Human '
               'High 100): the script line in quotes, starting from what they believe, the two mistakes as the alternatives'),
      'joel': ('2026-11-20 17:54 UTC: "your script was not in quotes and it didn\'t start from what they knew. i fixed that ... '
               'fixed the connectivity issue ... fixed the final connectivity issue, now all hum high"'),
      'applied_by': by, 'must_contain_exact': [HARM]},
     {'id': 'r45-harm-script-out', 'status': 'applied',
      'what': ('When What They Say Turns Toward Harm: the script\'s label and the script (B287, B288) out, his paragraph now '
               'quoting its line; "Other useful lines" follows it (review/r45/REMOVED-R45.json keeps the two blocks)'),
      'joel': '2026-11-20 17:54 UTC, with his version: "but now you have to take out p2 right?"',
      'applied_by': by, 'must_not_contain': ['Non-combative philosophical grounding', 'Peace is the godly move tonight.']},
     {'id': 'r45-touch-his', 'status': 'applied',
      'what': ('Touch, Consent, and Compassion, his two paragraphs (round 45, TEACH-TOUCH; his check 39cd2ecf, Human High '
               '149): "respectful touch", holding down said as what it does, "If they did permit touch, ..."'),
      'joel': ('2026-11-20 18:14 UTC: "adding "respectful" ... made the request clearer ... explained hold them down better, '
               'that lfipped it all human ... i fixed the lead-in, now it\'s all high conf"'),
      'applied_by': by, 'must_contain_exact': [TOUCH_1_MD, TOUCH_2]},
     {'id': 'r45-demons-his', 'status': 'applied',
      'what': ('Demons, Jinn, Entities, and Shadow Forces: the hooks kept (hatred, fear, pride and grandiosity, not love) and '
               '"get them whatever help they need" (round 45, DEMONS-HOOKS; his check 3a1603ee, Human High 87)'),
      'joel': ('2026-11-20 18:20 UTC: "why did you not check b yet? it\'s high conf hum ... i don\'t like always telling to go '
               'to a doctor, i would use this one ... and that\'s also high conf hum"'),
      'applied_by': by, 'must_contain_exact': [DEMONS_1, DEMONS_2]},
    ]
    oe['entries'] += [e for e in new if e['id'] not in have]
    OE.write_text(json.dumps(oe, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print('applied |', len(MD.read_text(encoding='utf-8').split()), 'words')


if __name__ == '__main__':
    main()
