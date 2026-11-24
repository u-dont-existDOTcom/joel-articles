#!/usr/bin/env python3
"""PAGE-OPTIONS.json for the Self-Hypnosis guide's contents picks page (tools/humanization/contents_picks_page.py):
the second pick (PICK2-FOR-PAGE.json, from make_pick.py), Fable's first version, a note under every heading that moves,
changes level or goes (his answers of 2026-11-24 01:04 UTC), the text changes his answers call for (TEXT-CHANGES.json),
the link plan (LINK-PLAN.json) and the readers' scores (SCORES*.json).

  python3 make_page_options.py && python3 make_page.py PAGE-OPTIONS.json PICKS-PAGE.html
"""
import html, json, os

HERE = os.path.dirname(os.path.abspath(__file__))
GH = 'https://github.com/u-dont-existDOTcom/joel-articles/blob/main/articles/inner-signal/experiments/toc-20261123/'
POST = 'https://ibogaqueen.substack.com/p/guide-to-self-hypnosis-and-app-including'
J = lambda f: json.load(open(os.path.join(HERE, f), encoding='utf-8'))
E = html.escape


def main():
    now = J('CONTENTS-NOW.json')
    pick = {e['id']: e for e in J('PICK3-FOR-PAGE.json')}
    order = [e['id'] for e in J('PROPOSAL-PICK3.json')]
    st = J('STRUCTURE.json')
    fates = J('FATES-PICK2.json')
    head = {e['id']: e['heading'] for e in pick.values()}
    shown = []
    for e in now:
        p = dict(pick[e['id']])
        if p['kind'] == 'dropped':
            p['kind'], p['heading'] = 'dropped', '(goes)'
        elif p['heading'] == e['heading']:
            p['kind'] = 'kept'
        elif p['heading'].lower() == e['heading'].lower():
            p['kind'] = 'case'
        else:
            p['kind'] = 'mine' if p['by'] == 'mine' else 'fable'
        shown.append(p)
    json.dump(shown, open(os.path.join(HERE, 'PICK3-PAGE-OPTION.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    notes = {}
    for e in now:
        i, p, bits = e['id'], pick[e['id']], []
        if i in st['dropped']:
            bits.append('<b>Goes</b> (%s).' % E(st['dropped'][i][1]))
        if i in st['level']:
            bits.append('<b>Now an h%d</b> (%s).' % (st['level'][i][0], E(st['level'][i][1])))
        for ids, after, why in st['moves']:
            if i in ids:
                bits.append('<b>Moves</b> after “%s” (%s).' % (E(head[after]), E(why)))
        if p.get('why') and p['kind'] != 'dropped' and p['heading'] != e['heading']:
            bits.append(E(p['why']))
        for k in ('hard:' + i, 'repeat:' + i):
            if k in fates:
                bits.append('Readers: %s' % E(fates[k].split(':', 1)[1].strip()))
        if bits:
            notes[i] = '<br>'.join(bits)
    T = {t['id']: t for t in J('TEXT-CHANGES.json')}
    links = J('LINK-PLAN.json')['links']
    q = [
        {'id': 'Your answer 5', 'text': 'I read “s009 accept” as: only “Keep the Adult Part of Yourself in Charge” becomes an h2, so it '
         'now sits under “The Most Extreme Example” as its lesson, and that heading and “Reversing Accidental Affirmations” '
         'stay h1. Right, or did you mean both S008 and S009 under “Protecting Yourself from Hypnotists”?'},
        {'id': 'Your answer 10: the merge', 'text': '“Hypnosis-specific audit” joins “Find a Hypnotist Who Fits” in Appendix F: '
         'your three lists first, as they are, then your audit, as it is, then your “firmly encouraged” line and your “Then '
         'afterwards” paragraph. Two changes: ' + '; '.join(E(c) for c in T['T6']['changes']) + '. The audit as it would read '
         'there:<blockquote>' + ''.join('<p>%s</p>' % E(x) for x in T['T6']['inserted']) + '</blockquote>Keep it like this, or '
         'tell me what to change.'},
        {'id': 'Your answer 7: the general rule', 'text': '“The General Rule” goes, and this sentence ends “Could It Be Psychosis?”, '
         'linked: <blockquote>The general rule is the one in “Daily Life Is the Feedback”: if what you\'re doing is making you '
         'more paranoid, sleepless, grandiose, isolated or scared, or things feel more and more unreal, stop going deeper and '
         'get help.</blockquote>It keeps every warning sign of yours; the first half of your rule (more loving, grounded, '
         'relational, honest, functional) is what the linked section says.'},
        {'id': 'Your answer 11: daydreaming', 'text': 'After your line under “Keep Daydreaming?”, the same pointer you use under '
         '“Getting Anxious?”: <blockquote>%s For more on daydreaming, see Appendix E.</blockquote>' % E(J('SECTIONS.json')[79]['text']
                                                                                                         if False else T['T5']['before'])},
        {'id': 'Your answers 2 and 8: what goes', 'text': 'With the “Appendices” heading goes its note (“%s”), since your first '
         'section already says there are lots of appendices with extra tools. With “Appendix I: Sleep hypnosis” goes its line '
         '(“%s”): “Sleep Induction” links the same Nimja playlist. J and K become I and J, and “All sources used are in Appendix '
         'K” becomes “Appendix J”.' % (E(T['T2']['before']), E(T['T4']['before']))},
        {'id': 'Your S122 note: Systema', 'text': 'The guide didn\'t mention Systema anywhere yet. After your Buteyko lines, '
         'this, with its two links (the video you named as the best, and the Systema section of your somatic post):<blockquote>'
         + E(T['T7']['after_added']) + '</blockquote>The proposal for its heading is now “Buteyko & Systema”, so the sidebar '
         'names both. Keep it like this, or tell me what to change.'},
        {'id': 'What the readers of the proposal still found', 'text': 'Things renaming can\'t fix, for you to decide or leave: '
         '“The Inner Adult’s Three Jobs” now holds ten sections, only three of them jobs (your answers 4 and 9); “Daily Life Is '
         'the Feedback” sits under “When to Get Outside Help” though it is about every day; “Find a Hypnotist Who Fits” and '
         '“Take It to the Council” sit under “F: Self-Trust and Guidance”, and the council isn\'t explained before its section; '
         '“9. No-Trance Inner Contact” is in the induction library though it isn\'t an induction. Leave them, or say what to move.'},
        {'id': 'The links', 'text': '%d places in the text name another section, and each gets a link to it, with the name '
                                   'following the heading you pick where the text quotes one: <ul>%s</ul>Say if one shouldn\'t.' % (
            len(links), ''.join('<li>in “%s”: “%s” → “%s”</li>' % (E(head[l['in']]), E(l['text']), E(head[l['to']])) for l in links))},
    ]
    S1, S2 = J('SCORES.json')['reads'], J('SCORES-PICK2.json')['reads'] if os.path.exists(os.path.join(HERE, 'SCORES-PICK2.json')) else {}
    S1b = J('SCORES-PICK.json')['reads']
    rows = []
    for label, src, pref in (('Yours, as the sidebar shows it', S1, 'READ-NOW-SIDEBAR'), ('Yours, whole headings', S1, 'READ-NOW-FULL'),
                             ('First proposal', S1b, 'READ-PICK-'), ('Proposal', S2, 'READ-PICK2-')):
        rs = [r['tally'] for f, r in src.items() if f.startswith(pref)]
        if rs:
            rows.append('<tr><td>%s</td><td>%d</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>' % (
                label, len(rs), ' · '.join(str(t['right']) for t in rs), ' · '.join(str(t['wrong']) for t in rs),
                ' · '.join(str(t['guess']) for t in rs), ' · '.join(str(t['found']) for t in rs)))
    table = ('<div class="scroll"><table class="sc"><thead><tr><th>Contents</th><th>Readers</th><th>Right on first try (of 64)'
             '</th><th>Wrong</th><th>Guessed</th><th>Found in two tries</th></tr></thead><tbody>%s</tbody></table></div>' % ''.join(rows))
    ren = sum(1 for p in shown if p['kind'] in ('fable', 'mine', 'case'))
    O = {'title': 'Self-Hypnosis guide: your contents picks',
         'sub': 'For “Inner Signal Guide to Self-Hypnosis (& APP)”, 2026-11-24. Your picks save as you go.',
         'store': 'inner-signal-toc-20261124', 'primary': 'pick',
         'options': {'pick': {'label': 'Proposed', 'file': 'PICK3-PAGE-OPTION.json'},
                     'fable': {'label': 'Fable\'s first version', 'file': 'PROPOSAL-FABLE.json'}},
         'pick': {p['id']: ('pick' if p['kind'] in ('fable', 'mine', 'case', 'dropped') else 'now') for p in shown},
         'notes': notes,
         'kinds': {'fable': 'named for what readers look for', 'mine': 'my change to Fable\'s', 'case': 'style only',
                   'dropped': 'goes, by your answer', 'kept': ''},
         'questions': q,
         'scores': {'question': '<b>Which heading should each section of your Self-Hypnosis guide have in the contents sidebar?</b> '
                                '90 of your 164 headings are cut off there today; the proposal renames %d (some only to title '
                                'case), cuts off none, and has the structure you chose in your 15 answers (a note under each '
                                'heading that moves, changes level or goes). Each heading starts on the proposal: keep it, take '
                                'yours or Fable\'s, or write your own. Then the questions at the bottom. Nothing on the post '
                                'has changed yet. <a href="%s">The post</a>.' % (ren, POST),
                    'table': table, 'git': GH + 'RESULTS.md'}}
    json.dump(O, open(os.path.join(HERE, 'PAGE-OPTIONS.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('PAGE-OPTIONS.json: %d notes, %d questions, %d score rows' % (len(notes), len(q), len(rows)))


if __name__ == '__main__':
    main()
