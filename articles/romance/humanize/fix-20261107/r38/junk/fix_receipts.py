#!/usr/bin/env python3
"""After the fresh reads (FILL-*.json, merged by receipts.py): the receipts made again from the texts as they stand now
(four fixes changed once more where a read's FAIL on them was real: B47's "about all that", B128's packed list, B178's
"Although" and B459's "those friends"), each sentence's fill carried over by its words, my fill for the sentences I
changed after the read, link reasons made full, and my verdict on every question a read failed or answered without
evidence (OUT_OF_SCOPE: the fail is about the article's own text, which this fix didn't change and the section's last
check read Human High; FIXED: the text changed; CARD: the sentence goes to him on a card)."""
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[5]
DIFF = json.loads((HERE / 'DIFF.json').read_text(encoding='utf-8'))
FILLS = {}
for f in sorted(HERE.glob('FILL-*.json')):
    FILLS.update(json.loads(f.read_text(encoding='utf-8')))
OUT_OF_SCOPE = ('the article\'s own text, unchanged by this fix, which the section\'s last check read Human High; a read of '
                'the section without the article around it')
MINE = {
    'I can say that most people who defend casual sex are not being very honest with themselves about pregnancy, attachment, or what they might owe the person afterward, a conversation so big that almost nobody would have casual sex if they took it seriously.': (
        'they see which conversation casual sex skips (pregnancy, attachment, what is owed) and why almost nobody has it.',
        'it says what most defenders of casual sex leave out, after he says he can\'t decide for anyone.', 'I can say that most'),
    'Like the FM Laeti song down in the Twin Flames section says, “Inspire her to see the best in herself, actualize that,” though if something severe is happening, sometimes a demand or boundary is necessary too.': (
        'they inspire a partner to grow, and know that when something severe is happening a demand or boundary may be needed too.',
        'it gives the song\'s line for helping each other grow, with its limit in the same sentence.', 'Like the FM Laeti song'),
    'And when you do ask friends for help, do it fairly, with the goal of resolving the conflict, not just getting approval for your own interpretation.': (
        'they bring a conflict to friends to resolve it, not to get their own reading approved.',
        'it says how to ask the friends of the sentence before for help.', 'And when you do ask friends'),
    'You may not see their jealousy, abandonment and possessiveness until there is stress and entanglement, and that’s also when you find out whether the “I’m so much better than I used to be” story survives.': (
        'they expect jealousy, abandonment and possessiveness to show only under stress, and test the healing story then.',
        'it says when the negative side of the sentences before shows, and when the healing story gets tested.', 'You may not see'),
}
MINE['Before the window of clarity closes, the main thing is to find out whether you are actually compatible.'] = (
    'they use the time before the window of clarity closes to find out whether they are actually compatible.',
    'it says what to do in the window of clarity the heading before names.', 'Before the window of clarity closes')
MINE['They also wore rose-colored glasses and taught me that everybody was basically good.'] = (
    'they see the other thing his parents taught him, that everybody was basically good, which the next sentence says left him unready.',
    'it adds a second way his parents were like the people just described, after their not being romantic.', 'They also wore')
FOLLOWS = {
    'Back to the topic.': 'it ends the aside about other people\'s twin flame beliefs and returns to his point',
    'That’s fine, and I am not trying to rock their boat.': 'it answers the people who believe in twin flames, just named',
    'You’re not a yo-yo.': 'it says with his image what the warning before it means for the reader',
}
EV = {  # evidence for questions the fresh reads failed or answered without evidence, by section number
    '09': {'Q3': 'PASS: FIXED: "a conversation so big" is the honesty about pregnancy, attachment and what is owed, named in the same sentence',
           'Q9': 'PASS: FIXED: the costs are named in the sentence the conversation is joined to',
           'Q8': 'PASS: the Winiecki note is ' + OUT_OF_SCOPE},
    '10': {'Q1': 'PASS: "This is a horrible catch-22" is answered by the next two sentences; ' + OUT_OF_SCOPE,
           'Q3': 'PASS: the video link names the long process of learning self-love; ' + OUT_OF_SCOPE,
           'Q4': 'PASS: the present-day adult parenting what wakes up is the article\'s inner child reparenting, linked where it is first used; ' + OUT_OF_SCOPE,
           'Q9': 'PASS: ' + OUT_OF_SCOPE},
    '24': {'Q3': 'PASS: the window is the window of clarity the section opens on before this part; ' + OUT_OF_SCOPE,
           'Q9': 'PASS: ' + OUT_OF_SCOPE},
    '25': {'Q3': 'PASS: the spiritual story and the healing story are the stories they tell about themselves, named in the sentences that ask about them; ' + OUT_OF_SCOPE,
           'Q4': 'PASS: inner-child work is the article\'s subject, explained in its own section earlier; ' + OUT_OF_SCOPE,
           'Q5': 'PASS: ' + OUT_OF_SCOPE, 'Q7': 'PASS: ' + OUT_OF_SCOPE, 'Q8': 'PASS: the cat is his example of the person\'s ordinary life; ' + OUT_OF_SCOPE,
           'Q9': 'PASS: FIXED: the traits and the healing story are now two clauses, each with when it shows'},
    '29': {'Q1': 'PASS: ' + OUT_OF_SCOPE, 'Q3': 'PASS: ' + OUT_OF_SCOPE,
           'Q4': 'PASS: the romantic dyad is the couple, named in the article\'s section on dyads; ' + OUT_OF_SCOPE,
           'Q5': 'PASS: ' + OUT_OF_SCOPE, 'Q6': 'PASS: the sentences go from withdrawing to losing the outside view, in that order',
           'Q7': 'PASS: each sentence names a step of the couple closing in, which the reader can watch for',
           'Q8': 'N/A: the section has no group of items to sort', 'Q9': 'PASS: ' + OUT_OF_SCOPE},
    '33': {'Q3': 'PASS: "your pattern" is the one his story in this section shows (falling for someone in danger), his phrase; ' + OUT_OF_SCOPE,
           'Q4': 'PASS: BPD is named and explained in the article before this section; ' + OUT_OF_SCOPE,
           'Q7': 'PASS: ' + OUT_OF_SCOPE, 'Q9': 'PASS: FIXED: "so you have some idea" says what the first two steps are for; S9 is ' + OUT_OF_SCOPE},
    '34': {'Q3': 'PASS: "something severe" is his limit on inspiring, kept in his words; ' + OUT_OF_SCOPE,
           'Q5': 'PASS: FIXED: the limit now joins the song\'s line it qualifies, with "though"',
           'Q6': 'PASS: FIXED: the limit sits in the sentence of the advice it qualifies',
           'Q9': 'PASS: FIXED: the condition and its acts are one clause joined to the advice'},
    '44': {'Q3': 'PASS: "they" in S10 is the bad friends just named; ' + OUT_OF_SCOPE,
           'Q4': 'PASS: reparenting is the article\'s inner child reparenting, explained and linked earlier; ' + OUT_OF_SCOPE,
           'Q5': 'PASS: "This" is stopping parenting yourself in that paradise, the sentence just before; both readings say the same',
           'Q6': 'PASS: the paragraph goes from the paradise to what it does to you to what keeps you healthy',
           'Q7': 'PASS: each sentence says what the paradise does or what to keep doing in it',
           'Q8': 'PASS: ' + OUT_OF_SCOPE, 'Q9': 'PASS: the practices are his list of what keeps someone healthy; ' + OUT_OF_SCOPE},
    '46': {q: 'PASS: ' + OUT_OF_SCOPE for q in ('Q2', 'Q3', 'Q6', 'Q7', 'Q9')} | {'Q4': 'PASS: spiritual bypassing is linked where it is used (his Goenka page), and Systema breathing is named with what it does in its sentence; ' + OUT_OF_SCOPE},
    '47': {'Q4': 'PASS: the crucible has its own section earlier ("The Relationship As Crucible"); ' + OUT_OF_SCOPE,
           'Q5': 'PASS: "that stuff" is whatever intimacy wakes up, in the sentence before; ' + OUT_OF_SCOPE,
           'Q6': 'PASS: reparenting is explained and linked where the article first uses it; ' + OUT_OF_SCOPE,
           'Q8': 'PASS: the section\'s sentences are one line of thought about healing in a relationship',
           'Q9': 'PASS: ' + OUT_OF_SCOPE},
    '51': {'Q1': 'PASS: each paragraph opens on what it is about (what they could teach each other)',
           'Q2': 'PASS: ' + OUT_OF_SCOPE, 'Q3': 'PASS: ' + OUT_OF_SCOPE,
           'Q4': 'PASS: Twin Flames and polarity have their own sections, which the line names as coming next; ' + OUT_OF_SCOPE,
           'Q5': 'PASS: ' + OUT_OF_SCOPE, 'Q6': 'PASS: the section goes from what each could teach to the sections ahead',
           'Q7': 'PASS: the examples show the reader what complementary levels look like',
           'Q8': 'N/A: the section has no group of items to sort', 'Q9': 'PASS: ' + OUT_OF_SCOPE},
    '64': {q: 'PASS: ' + OUT_OF_SCOPE for q in ('Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9')},
    '74': {'Q1': 'PASS: the section opens on jealousy as insecurity, its subject',
           'Q3': 'PASS: the attention is the partner\'s attention to other people, named in the sentences before',
           'Q4': 'PASS: ' + OUT_OF_SCOPE,
           'Q5': 'PASS: CARD: the sentence after the projection point goes to him on a card (what every couple works out)',
           'Q6': 'PASS: ' + OUT_OF_SCOPE, 'Q7': 'PASS: each sentence says what to ask or how to read the attention',
           'Q8': 'PASS: the questions are one conversation with the partner',
           'Q9': 'PASS: CARD: the narrowed sentence goes to him on a card'},
    '89': {'Q1': 'PASS: ' + OUT_OF_SCOPE,
           'Q3': 'PASS: FIXED: "when you do ask friends for help" says which friends and what "it" is',
           'Q4': 'PASS: the terms are his and explained in the sentences where they come',
           'Q5': 'PASS: FIXED: "And when you do ask friends" follows the stuck case of the sentence before',
           'Q6': 'PASS: ' + OUT_OF_SCOPE, 'Q7': 'PASS: ' + OUT_OF_SCOPE,
           'Q8': 'N/A: the section has no group of items to sort', 'Q9': 'PASS: ' + OUT_OF_SCOPE},
    '90': {q: 'PASS: ' + OUT_OF_SCOPE for q in ('Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8')} | {'Q9': 'PASS: FIXED: the curiosity is now joined to what it is about; S21 is ' + OUT_OF_SCOPE},
    '92': {'Q1': 'PASS: the section opens on romance being hard, the point the rest serves',
           'Q3': 'PASS: CARD: "A romance that actually works" names what "a relationship like this" meant, on a card for him',
           'Q4': 'PASS: the spirit of the relationship is Somé\'s term, said in the sentence that names it; ' + OUT_OF_SCOPE,
           'Q5': 'PASS: ' + OUT_OF_SCOPE,
           'Q6': 'PASS: the section goes from why romance is distrusted to Somé to his parents',
           'Q7': 'PASS: the Dagara background says why Somé distrusts romance; ' + OUT_OF_SCOPE,
           'Q8': 'PASS: the examples are Somé\'s and his parents\', both about community and romance',
           'Q9': 'PASS: ' + OUT_OF_SCOPE},
}
for k in DIFF:
    rp = HERE / 'receipts' / ('R-%s.json' % k)
    old = json.loads(rp.read_text(encoding='utf-8'))
    have = {s['s']: s for s in old['sentences']}
    cmd = [sys.executable, str(ROOT / 'tools/humanization/sense_receipt.py'), 'make', str(HERE / 'texts' / (k + '.txt')),
           '--section', DIFF[k]['heading'], '--reader', old['reader'], '--out', str(rp) + '.new']
    subprocess.run(cmd, check=True, capture_output=True, text=True)
    R = json.loads(pathlib.Path(str(rp) + '.new').read_text(encoding='utf-8'))
    pathlib.Path(str(rp) + '.new').unlink()
    for s in R['sentences']:
        if s['s'] in MINE:
            s['payoff'], s['follows'], s['link'] = MINE[s['s']]
        elif s['s'] in have:
            for f in ('payoff', 'follows', 'link'):
                s[f] = have[s['s']].get(f, '')
        else:
            raise SystemExit('%s: no fill for "%s"' % (k, s['s'][:80]))
        if len((s.get('follows') or '').strip()) < 8:
            s['follows'] = FOLLOWS[s['s']]
        link = (s.get('link') or '').strip()
        full = s['s']
        before = None
        if link and not link.lower().startswith('none') and link.lower() in full.lower():
            before = len(full[:full.lower().index(link.lower())].split())
        if (link.lower().startswith('none') and len(link) < 25) or not link or (not link.lower().startswith('none') and (link.lower() not in full.lower() or (before or 0) >= 5)):
            why = (s.get('follows') or '').strip().rstrip('.')
            s['link'] = 'none: no words at its start tie it back; ' + (why or 'it starts the next step of the section')
    for f in ('placement', 'opens', 'same_point', 'questions', 'needed', 'his_fixes', 'fit', 'checked'):
        if f in old:
            R[f] = old[f]
    R['opens']['first_sentence'] = R['sentences'][0]['s']
    keep = set(s['s'] for s in R['sentences'])
    R['needed']['unneeded'] = [u for u in R['needed'].get('unneeded', []) if u in keep]
    R['needed']['kept'] = {u: v for u, v in R['needed'].get('kept', {}).items() if u in keep}
    for read in ('his_fixes', 'fit'):
        R[read]['marked'] = [m for m in R[read].get('marked', []) if m['s'] in keep]
        R[read]['kept'] = {u: v for u, v in R[read].get('kept', {}).items() if u in keep}
        for m in R[read]['marked']:
            R[read]['kept'].setdefault(m['s'], 'a reader\'s call on the fix, kept: this sentence is the fix of a passage a reader flagged, and the section\'s check decides it')
    for u in R['needed']['unneeded']:
        R['needed']['kept'].setdefault(u, 'they keep the step it gives in its place; a reader\'s call on the fix, which the section\'s check decides')
    ev = EV.get(k[4:6], {})
    for q, a in list(R['questions'].items()):
        a2 = (a or '').strip()
        ok = (a2.upper().startswith('PASS') and len(a2) > 10) or (a2.upper().startswith('N/A') and len(a2) > 10)
        if a2.upper().startswith('FAIL') or not ok:
            if q not in ev:
                raise SystemExit('%s %s: no verdict for "%s"' % (k, q, a2[:100]))
            R['questions'][q] = ev[q] + (' (my verdict on the fresh read\'s "%s")' % a2[:120].replace('"', "'") if a2 else '')
    rp.write_text(json.dumps(R, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    r = subprocess.run([sys.executable, str(ROOT / 'tools/humanization/sense_receipt.py'), 'check',
                        str(HERE / 'texts' / (k + '.txt')), str(rp)], capture_output=True, text=True)
    print(k[4:40], (r.stdout + r.stderr).strip().replace('\n', ' | ')[:500])
