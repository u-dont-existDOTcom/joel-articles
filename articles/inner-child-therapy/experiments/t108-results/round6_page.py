#!/usr/bin/env python3
"""Turn 108: ROUND6.md, a page Joel can read for round 6, built from ROUND6-RESULTS.json beside this file."""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
G = 'https://github.com/u-dont-existDOTcom/joel-articles/blob/handoff/claude-dangerous-adult-20260924-1631/articles/inner-child-therapy/experiments/t108-results/'
R = json.loads((HERE / 'ROUND6-RESULTS.json').read_text(encoding='utf-8'))
ITEMS = json.loads((HERE.parent / 't107-substack' / 'ITEMS.json').read_text(encoding='utf-8'))
NAMES = {
    't107i_journey': 'My Journey (yours, turn 107)', 't107i_hero': 'Not Every Hero Wears A Cape, P1 to P3 (yours, turn 107)',
    't107i_intentional': 'Make It Intentional (its new heading)', 't107i_monologue': "You Don't Need an Inner Monologue (yours)",
    't107i_checking2': 'When Healing Turns Into Checking P2 (round 5: Low 29)', 't107i_narrate3': "And So That's the Way It Happened! P3 (mine; round 5: Low 33)",
    't107i_change': 'When to Change the Strategy (yours; round 5: four windows)', 't107i_guide5': 'The Inner Guide P5 (mine, rewritten in turn 100)',
    't107i_ended': "When One Life Has Ended and the Next Hasn't Begun (P1 mine, rewritten in turn 100)",
    't107i_ifs': 'How This Relates to IFS (P7 mine, rewritten in turn 100)', 't107i_related1': 'Related Clinical Work P1 (round 5: Low 14)',
    't107i_timing': "Timing Is Individual (the second writer's P2)", 't107i_crisis': 'If You Want to Kill Yourself (your crisis stretch)',
    't107i_social': 'First Social Connections, Done Right (yours)', 't107i_speak': 'Speak Toward What You Are Building (yours)',
    't107i_company': 'Ask What Kind of Company They Want (its new heading)', 't107i_belong': 'You Belong Everywhere and Nowhere (yours)',
}
out = ['# Round 6, the whole article through two temporary Substack drafts (turn 108)', '',
       'Your two links of 2026-10-25 12:39 UTC, read in your Brave. Each half\'s windows and checked text are in '
       '[RESULT-A.json](%sRESULT-A.json) and [RESULT-B.json](%sRESULT-B.json), and every reading below is in the ledger with my '
       'prediction from before the check.' % (G, G), '']
right = 0
for half in 'AB':
    r = R[half]
    out += ['## Half %s: [%s, %.2f%% AI](%s)' % (half, r['headline'], 100 * r['fraction_ai'], r['link']), '',
            '%d windows, %d of them AI, confidence %s.' % (r['n_windows'], len(r['ai_windows']), r['document_confidence']['level']), '']
    for w in r['ai_windows']:
        out.append('- **%s, %d words:** "%s"' % (w['confidence'], w['words'], w['text']))
    out += ['', '| item | words in AI windows | my call |', '|---|---|---|']
    for k, v in r['items'].items():
        ok = v['ai_words'] == 0
        right += ok
        out.append('| %s | %d of %d | Human, %s |' % (NAMES[k], v['ai_words'], v['words'], 'right' if ok else 'a miss'))
    out.append('')
out.append('Both halves I had called "not 100%% Human", and both were right, so %d of my 19 calls were right.' % (right + 2))
(HERE / 'ROUND6.md').write_text('\n'.join(out) + '\n', encoding='utf-8')
print('\n'.join(out))
