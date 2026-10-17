"""Section 12 v15 (2026-10-17, Joel's message of 17:16 UTC, joel-20261017/joel-20261017-1716-message.txt), his 44c:
"i was not saying to put the prose in, i wanted the actual screenshot with the link and my caption as that quote aside to
you." So his P2 goes back as he wrote it (my two sentences about the study out), and the screenshot stays after it, with a
caption that is his aside ("altho it's kind of a "no, duh" study"), "altho" dropped because it only joined his sentence to
me, and the link on "study". Where the screenshot finally goes is question 46 (the anomie point he asked about).
The ledger: the 13:11 study entry is superseded by this one. Idempotent. Run from candidate/: python3 fix-20261017b/install_44c.py"""
import json, pathlib

HERE = pathlib.Path(__file__).resolve().parent
C = HERE.parent
ART = C / 'HUMANIZED-SO-FAR.md'
URL = 'https://www.psypost.org/social-freedom-shapes-whose-version-of-reality-you-adopt-new-research-suggests/'
PROSE = (' A [new study](%s) found that where relationships are easy to make and break, people even feel less on the same page '
         'with whoever doesn\'t help them reach their goals. Kind of a "no, duh" study, but still.' % URL)
OLD_PROD = ('<!-- The screenshot is Joel\'s, sent 2026-10-17 13:11 (candidate/images/psypost-relational-mobility.png); the '
            'Substack image goes in when he uploads it. -->')
CAPTION = '[caption] It\'s kind of a "no, duh" [study](%s).' % URL
NEW_PROD = ('<!-- The screenshot is Joel\'s, sent 2026-10-17 13:11 (candidate/images/psypost-relational-mobility.png), with his '
            'aside to me as its caption and the link to the write-up (his 44c of 17:16); the Substack image goes in when he '
            'uploads it, linked to the write-up. Question 46 asks whether it moves to section 2 with the anomie point. -->')
OLD_NOTE = '<!-- CANDIDATE: section 12 v14 (2026-10-17, after Joel\'s 13:11 message)'
NEW_NOTE = ('<!-- CANDIDATE: section 12 v15 (2026-10-17, after Joel\'s 17:16 message): his P2 as he wrote it again, without '
            'my two sentences about the study (his 44c: "i was not saying to put the prose in"), and his screenshot after it '
            'with his aside as the caption, the link on "study". Pangram results: fix-20261017b/. Before: section 12 v14 '
            '(2026-10-17, after Joel\'s 13:11 message)')

md = ART.read_text(encoding='utf-8')
if PROSE in md:
    assert md.count(PROSE) == 1 and md.count(OLD_PROD) == 1 and md.count(OLD_NOTE) == 1
    md = md.replace(PROSE, '').replace(OLD_PROD, CAPTION + '\n' + NEW_PROD).replace(OLD_NOTE, NEW_NOTE)
    ART.write_text(md, encoding='utf-8')
    print('section 12 v15 installed')
else:
    assert CAPTION in md, 'neither the old nor the new text is in the article'
    print('section 12 v15 already in')

L = json.loads((C / 'OWNER-EDITS.json').read_text(encoding='utf-8'))
ids = {e['id']: e for e in L['entries']}
old = ids['s12-joel-20261017-1311-psypost']
old['status'] = 'superseded'
old['superseded_by'] = 's12-joel-20261017-1716-44c'
if 's12-joel-20261017-1716-44c' not in ids:
    L['entries'].append({
        'id': 's12-joel-20261017-1716-44c', 'status': 'applied', 'words': 'his',
        'what': 'Section 12: his P2 as written (my two sentences about the PsyPost study out); his screenshot after it, with his '
                'aside to me as the caption and the link on "study". Where it finally goes is question 46.',
        'joel': '44c i was not saying to put the prose in, i wanted the actual screenshot with the link and my caption as that '
                'quote aside to you.',
        'when': '2026-10-17 17:16 UTC (joel-20261017/joel-20261017-1716-message.txt)',
        'must_contain': ["Instead we optimize to fit the career market with all the little energy we've got.",
                         'It\'s kind of a "no, duh" study.'],
        'must_not_contain': ['people even feel less on the same page with whoever', 'Kind of a "no, duh" study, but still.'],
        'must_link': [{'text': 'study', 'url': URL}]})
if 'all-joel-20261017-1716-43' not in ids:
    L['entries'].append({
        'id': 'all-joel-20261017-1716-43', 'status': 'claim', 'words': 'his',
        'what': 'The exclamation rule (his 43): an exclamation is content; "!" becomes "." only where the sentence still reads '
                'right with a period. Otherwise cut the exclamation phrase itself, fix the AI structure under it, find a real '
                'turn of thought, or give him the paragraph. Applied in sections 15 and 16 (fix-20261017b/), in the gate doc.',
        'joel': '43 the problem is you can\'t just change ! to . if the actual wording was put in as an exclamation. you can\'t '
                'change "That\'s it!" to "that\'s it." ... so either take out the exclamation phrases themselves, replace the '
                'exclamation marks alone only if it makes sernse to, or idk ask me if you need help.',
        'when': '2026-10-17 17:16 UTC (joel-20261017/joel-20261017-1716-message.txt)',
        'must_not_contain': ["That's it."]})
(C / 'OWNER-EDITS.json').write_text(json.dumps(L, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
print('ledger: %d entries' % len(L['entries']))
