#!/usr/bin/env python3
"""Write RESULTS.md (the run's record, which GitHub renders) and PAGE-OPTIONS.json (what make_page.py turns into Joel's
picks page) from this folder's scores, proposals and reads. Every number comes from SCORES.json (score_reads.py) and the
reads' HARD lines; the notes say why each heading changed, in plain words, with what the readers did for it.

  python3 make_results.py [PAGE_URL]
"""
import html, json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', '..', '..', 'tools', 'humanization'))
import toc_sidebar as ts

GIT = 'https://github.com/u-dont-existDOTcom/joel-articles/blob/main/articles/nibbana/experiments/toc-20261123/'
POST = 'https://ibogaqueen.substack.com/p/what-if-everything-is-already-perfect-bdc'
RUNS = [  # key, label, contents file, reads
    ('now', 'Yours, as the sidebar shows it', None, ['READ-NOW-SIDEBAR-1.md', 'READ-NOW-SIDEBAR-2.md']),
    ('nowfull', 'Yours, whole (nothing cut off)', None, ['READ-NOW-FULL-1.md']),
    ('fable', "Fable's first version", 'PROPOSAL-FABLE.json', ['READ-FABLE-1.md']),
    ('pick1', 'First proposal (Fable + 10 of mine)', 'PROPOSAL-PICK.json', ['READ-PICK-1.md', 'READ-PICK-2.md']),
    ('pick2', 'Second (4 changed after readers)', 'PROPOSAL-PICK2.json', ['READ-PICK2-1.md', 'READ-PICK2-2.md']),
    ('final', 'Final proposal', 'PROPOSAL-PICK3.json', ['READ-PICK3-1.md', 'READ-PICK3-2.md']),
]
YOURS = ('now', 'nowfull')
KINDS = {'fit': 'cut off in the sidebar', 'reader': 'named for what readers look for', 'case': 'style only',
         'opus': "my change to Fable's", 'retest': 'changed after the readers', 'kept': ''}

# Why each heading changes, to Joel, in his terms. Checked against the section texts (SECTIONS.json).
NOTE = {
    'S004': "Your phrase from the section's first line; yours is cut off, and this says what the section is about (your grief for the world, activism, teaching).",
    'S005': "Yours is cut off. The section has three firsts (weed, mushrooms, ayahuasca): Fable's names only ayahuasca, and a reader with a mushroom question looks for psychedelics.",
    'S006': "Yours is cut off; without 'When' it fits.",
    'S007': "Yours is cut off; the question itself fits.",
    'S008': "Yours is cut off after 'May All Beings Be Lov…', so the sidebar never says this is where you start loving-kindness meditation. The blessing could open the section as a line of its own (question at the bottom).",
    'S009': "Yours is cut off. Keeps your claim (useless, or worse) as a question; Fable's 'Peak States Don't Stick' says something your heading didn't.",
    'S010': "Yours is cut off. The section answers why the books give lists and monastics won't describe their own experience (the Vinaya rules): the question a reader brings. Yours names the step in your story.",
    'S011': "Yours is cut off; your phrase without 'Then I Found'.",
    'S012': "Yours is cut off; same promise, shorter.",
    'S013': "Yours is cut off before the sutta's name shows; the name is what a reader looks for.",
    'S014': "Yours is cut off. Adds the name a reader looks for (Dōgen) and keeps your 'myriad things'.",
    'S015': "Yours is cut off. Keeps Bāhiya in the heading, so the first line ('both of us were really desperate') still says who 'us' is; Fable's 'Desperation Did the Trick' would need that line changed.",
    'S017': "Yours is cut off. The unimaginable half is the section's point (the fish and the air).",
    'S018': "Yours is cut off. Keeps your joke in two words; the whole line could open the section (question at the bottom).",
    'S019': "Yours is cut off, and both coinages can't fit together. The section says the two events differ only in scope; body-limited and body-uncontained are defined in its first lines.",
    'S020': "Capital only.",
    'S023': "Yours is cut off, and repeats 'Spiritual' from the line above.",
    'S024': "Yours is cut off, and 'Spiritual' would start three lines in a row.",
    'S025': "Alone in a manual's contents, 'What's Next?' reads as next steps; the section asks what comes after death.",
    'S026': "Yours is cut off by a few letters; the same question.",
    'S027': "Lower-case 'vs' (AP style).",
    'S028': "Yours is cut off; the section is about what the word means (unbinding).",
    'S029': "Yours is cut off; keeps your knobs.",
    'S031': "Yours is cut off. The objection the section answers, as a reader would ask it.",
    'S032': "Yours only just fits; without 'How' it fits with room.",
    'S033': "Your 'Awarenesses' needs the bold 'es', which the sidebar doesn't show. The section's point is the plural: the one-versus-many question 'ultimately separates Buddhism from prior teachings and new-age spirituality'. I first tried 'What Awareness Means'.",
    'S034': "Capitals only.",
    'S036': "Yours is cut off by one word; 'Makes' fits and doesn't echo 'Builds' on the line above.",
    'S037': "Yours only just fits; without 'The' it fits with room.",
    'S038': "Yours is cut off; the same claim without 'The Theory of'.",
    'S039': "Yours is cut off, and the Chantress Seba joke doesn't tell a sidebar reader this is the light imagery in the suttas. Keeps your 'light language'. Your heading holds the link to her YouTube channel, which goes with it unless it moves into the first line (question at the bottom).",
    'S040': "Lower-case 'the'.",
    'S041': "Yours is cut off before the key word; the objection in a reader's words.",
    'S042': "Yours is cut off. Both readers of the first proposal read 'Isn't It \"Unconditioned\"?' and Fable's 'Is Light Unfabricated?' as the same question (both words translate asaṅkhata). Naming what this section argues (a photon has no parts to assemble or decay) makes the line above the objection and this one the answer; the section ends 'So light isn't fabricated'.",
    'S043': "Yours is cut off (70 characters). Names the Einstein parallel the section opens with.",
    'S044': "Yours is cut off.",
    'S045': "Yours is cut off. Says what faded; Fable's 'How the Meaning Faded' doesn't say whose meaning.",
    'S046': "Yours is cut off after 'A Map Can Save Years –'. 'Map' in this heading also drew readers looking for which maps are worth using away from 'The Map Past Oneness'. Your own question in the section: 'What happens when we lay out the stages in a way that allows anyone to skip ahead to the answer?' Fable's other idea: 'The Risk of a Good Map'.",
    'S047': "Your words, with a straight apostrophe (your heading style). 'AtR' is spelled out only in the text of 'The Map Past Oneness'; a reader's version would be 'Who Certifies Awakening?'.",
    'S048': "Yours is cut off. The section says what stream entry is, the reader's question; the sections under it carry the rebirth part.",
    'S049': "Yours is cut off; the same point in three words.",
    'S050': "Yours is cut off. The section is your checklist for testing a claim to stream entry; this is the reader's question for it.",
    'S051': "Yours is cut off. The question the section answers (rebirth with no self); 'the dream of saṃsāra' is the next section's image.",
    'S052': "Yours is cut off. The section is the dream analogy for awakening.",
    'S053': "Yours is cut off; this is its first half. The section's own text is about science; the test is in the three sections under it, which readers found anyway. I first tried 'How to Test It Yourself'.",
    'S055': "Yours is cut off. Names success and danger without 'safe' (your rule). Fable's 'Did It Work? Is It Safe?' sat beside Fable's 'Is It Safe When \"I\" Vanish?', and its reader sent a meditation that turned frightening to the appendix.",
    'S057': "Yours is cut off; keeps your joke whole. Fable's 'Then a Cow Killed Bāhiya' starts with a 'Then' that hangs.",
    'S060': "Yours is cut off. 'Dangerous' is your word, from your heading, and 'the felt \"I\" vanishes' is your line; no 'safe' (your rule). 'Cool' doesn't fit as well. I first tried 'When the \"I\" Vanishes'.",
    'S016': "Kept: your name for it, used again later in the text. Fable's other idea, if you want it said that this is the experience itself: 'The Room Event: Nibbāna'.",
    'S058': "Kept as yours.",
}

QUESTIONS = [
    ('Spiritual Bypass Warning',
     "<b>“Spiritual Bypass Warning”</b> (##) has no text of its own. Under it are “Realization Isn’t Enough” (your bypassing story and how to tell fake gurus) and “Friends Are Everything” (community, peer counseling). {S022} Readers looking for how to tell a real teacher from a fake one stop at it, and clicking it lands on “Realization Isn’t Enough”, so they get there. Keep it, rename it to cover both (Fable’s idea: “Before You Start”, which fits), or drop it so the two stand as ## headings? Dropping it changes the post’s structure, not just a name."),
    ('Loving-kindness',
     "<b>“Loving-Kindness (Mettā)”</b> is a ### under “Enlightened or Deluded?”, but it’s the next step of your story: you start mettā, it cures your depression, and you learn that people who hate themselves need a loving inner adult first. “Why Monks Stay Vague” later calls it “the loving kindness key”. {S008} Make it a ## of its own? And the 🫶🏿 blessing (“May All Beings Be Loving, Peaceful &amp; Free”) leaves the heading in every version: open the section with it as a line of its own?"),
    ('Enlightened Fingers',
     "<b>“Enlightened Fingers”</b> is a ### under “The Room Event”, but it’s a second event, “some months after” the room, asleep in a parked car. Make it a ## beside “The Room Event”, with “Two Scopes of Nibbāna” (which compares the two) after it? Your whole line (“Your fingers are already enlightened, but your hand is deluded.”) can’t fit as a heading: open the section with it?"),
    ('Rebirth sections',
     "<b>“Who Gets Reborn?”</b> and <b>“Waking From the Dream”</b> sit under “What Is Stream Entry?”, but they’re about rebirth and the dream analogy. Your heading for the parent was “Entering The Stream To End Rebirth”. Put them under a ## of their own (“Ending Rebirth”, its second half), or leave them? Readers found “Who Gets Reborn?” where it is."),
    ('Appendix',
     "<b>“Appendix”</b> (#) has no text and one section: <b>Vanishing \"I\": Dangerous?</b> (your micro-disappearances, and whether biking or driving through one is safe). {S059} Keep it, drop “Appendix” so the section is its own #, or move the section into the manual after “What Remains Afterward”?"),
    ('Your own phrases',
     "Renaming takes some of your own words out of the contents: “dangerous or cool?” (the appendix), “Light Language Like Chantress Seba Never Seen Before!” with its link to her YouTube channel (the link goes too unless it moves into that section’s first line), “Body-Limited and Body-Uncontained” (defined in that section’s first lines anyway), the blessing and the fingers line (both above). Which, if any, should open its section as a line of its own, and where should the Chantress Seba link go?"),
]


def load(name):
    return json.load(open(os.path.join(HERE, name), encoding='utf-8'))


def esc(s):
    return html.escape(s, quote=False)


def same(a, b):
    f = lambda s: s.replace('’', "'").replace('“', '"').replace('”', '"')
    return f(a) == f(b)


def main(page_url=''):
    now = load('CONTENTS-NOW.json')
    ids = [e['id'] for e in now]
    NOW = {e['id']: e for e in now}
    FINAL = {e['id']: e for e in load('PROPOSAL-FINAL.json')}
    FABLE = {e['id']: e for e in load('PROPOSAL-FABLE.json')}
    heads = {k: ({i: NOW[i]['heading'] for i in ids} if f is None else {e['id']: e['heading'] for e in load(f)})
             for k, _, f, _ in RUNS}
    S = load('SCORES.json')['reads']
    key = load('EXPECTED-REVIEWED.json')['situations']
    sit = dict(re.findall(r'(?m)^(\d+)\. (.*)$', open(os.path.join(HERE, 'SITUATIONS.md'), encoding='utf-8').read()))
    hard = {}  # read -> {line: why}
    for _, _, _, reads in RUNS:
        for r in reads:
            hard[r] = {int(n): w.strip() for n, w in re.findall(r'(?m)^HARD:\s*(\d+)\s*\|\s*(.*)$',
                                                                   open(os.path.join(HERE, 'reads', r), encoding='utf-8').read())}
    line = {i: n + 1 for n, i in enumerate(ids)}
    allreads = [r for _, _, _, rs in RUNS for r in rs]
    finalreads = RUNS[-1][3]
    yourreads = [r for k, _, _, rs in RUNS if k in YOURS for r in rs]

    def label(i, text):
        if same(text, FINAL[i]['heading']):
            return 'this heading'
        if same(text, NOW[i]['heading']):
            return 'yours'
        if same(text, FABLE[i]['heading']):
            return "Fable's"
        return '“%s”' % text

    # what readers did, per section: the situations whose answer is that section, grouped by the heading they saw
    ev = {}
    for k, _, _, reads in RUNS:
        for r in reads:
            for n, p in S[r]['per'].items():
                for i in key[n]['right']:
                    g = ev.setdefault(i, {}).setdefault(n, {})
                    lab = label(i, heads[k][i])
                    g.setdefault(lab, [0, 0])
                    g[lab][1] += 1
                    g[lab][0] += p['kind'] == 'right'

    def evidence(i, md=False):
        out = []
        for n, g in sorted(ev.get(i, {}).items(), key=lambda x: int(x[0])):
            if len(g) < 2:
                continue  # every reader saw the same words: nothing to compare
            order = sorted(g, key=lambda l: (l == 'this heading', l != 'yours'))
            parts = ['%d of %d with %s' % (g[l][0], g[l][1], l) for l in order]
            out.append(('Readers looking for it (“%s”) went here first: ' % sit[n]) + '; '.join(parts) + '.')
        return out

    def flags(i, reads):
        return [hard[r][line[i]] for r in reads if line[i] in hard[r]]

    def flagline(i):
        y, f = flags(i, yourreads), flags(i, finalreads)
        if not f:
            return ''
        return ('%d of %d readers of the final list called it hard (%d of %d with yours). One said: %s'
                % (len(f), len(finalreads), len(y), len(yourreads), f[0][:150] + ('…' if len(f[0]) > 150 else '')))

    def qflag(i):
        a = flags(i, allreads)
        return '%d of %d readers called it hard.' % (len(a), len(allreads)) if a else ''

    # ---- scores
    rows = []
    for k, lab, _, reads in RUNS:
        t = [S[r]['tally'] for r in reads]
        rows.append((lab, len(reads), *[' · '.join(str(x[c]) for x in t) for c in ('right', 'near', 'wrong', 'guess', 'found')]))
    changed_sits = []
    for n in sorted(key, key=int):
        a = sum(S[r]['per'][n]['kind'] == 'right' for r in yourreads)
        b = sum(S[r]['per'][n]['kind'] == 'right' for r in finalreads)
        if a / len(yourreads) != b / len(finalreads):
            changed_sits.append((n, a, b))
    ncut_now = sum(not ts.shown(NOW[i]['heading'], NOW[i]['level'])[0] for i in ids)
    nchanged = sum(FINAL[i]['heading'] != NOW[i]['heading'] for i in ids)
    head_cols = ('Contents', 'Readers', 'Right on first try (of 36)', 'Near (its parent)', 'Wrong', 'Guessed', 'Found in two tries')
    table_html = ('<div class="scroll"><table class="sc"><thead><tr>' + ''.join('<th>%s</th>' % c for c in head_cols) + '</tr></thead><tbody>'
                  + ''.join('<tr><td>%s</td>' % esc(r[0]) + ''.join('<td class="n">%s</td>' % c for c in r[1:]) + '</tr>' for r in rows)
                  + '</tbody></table></div>'
                  + '<p class="legend">36 situations, each a reader looking for one thing (written from your text with the headings taken out, and checked by a second reader). '
                  'Each fresh reader saw only one contents list, drawn as the sidebar draws it, and named the heading they would click first. '
                  'One number per reader. The final list was read with the curly apostrophe in S047, its only difference from this proposal.</p>'
                  + '<p class="legend"><b>Where it changed</b> (readers of yours → readers of the final list who went to the right section first):</p><ul class="legend">'
                  + ''.join('<li>“%s”: %d of %d → %d of %d</li>' % (esc(sit[n]), a, len(yourreads), b, len(finalreads)) for n, a, b in changed_sits)
                  + '</ul>')
    question_html = ('<b>Which heading should each section of your Nirvāna guide have in the contents sidebar?</b> '
                     '%d of your 60 headings are cut off there today; the proposal changes %d and cuts off none. '
                     'It is picked for every heading to start with: keep it, take yours or Fable’s, or write your own. Then the six questions at the bottom. '
                     'Nothing on the post has changed yet. <a href="%s">The post</a>.') % (ncut_now, nchanged, POST)
    git_html = ('This page is a view of <a href="%sRESULTS.md">the run’s record in Git</a>, which has the same lists and numbers. '
                'Your answers save to this page and in this browser; “Copy my answers” gives the same record to paste into the chat.') % GIT

    notes, pick = {}, {}
    for i in ids:
        parts = []
        if i in NOTE:
            parts.append(esc(NOTE[i]))
        parts += [esc(x) for x in evidence(i)]
        fl = flagline(i)
        if fl:
            parts.append(esc(fl))
        if parts:
            notes[i] = '<br>'.join(parts)
        pick[i] = 'now' if FINAL[i]['heading'] == NOW[i]['heading'] else 'pick'
    questions = []
    for qid, text in QUESTIONS:
        text = re.sub(r'\{(S\d{3})\}', lambda m: qflag(m.group(1)), text)
        questions.append({'id': qid, 'text': text})
    opts = {'title': 'Nirvāna guide: your contents picks',
            'sub': 'For “What If Everything Is Already Perfect? (v2.2)”, 2026-11-23. Your picks save as you go.',
            'store': 'nibbana-toc-20261123', 'primary': 'pick',
            'options': {'pick': {'label': 'Proposed', 'file': 'PROPOSAL-FINAL.json'},
                        'fable': {'label': "Fable's first version", 'file': 'PROPOSAL-FABLE.json'}},
            'pick': pick, 'notes': notes, 'kinds': KINDS, 'questions': questions,
            'scores': {'question': question_html, 'table': table_html, 'git': git_html}}
    json.dump(opts, open(os.path.join(HERE, 'PAGE-OPTIONS.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

    # ---- RESULTS.md
    def st(t, lvl):
        f, _, w, room = ts.shown(t, lvl)
        return 'cut off' if not f else ('only just fits' if room - w < 12 else 'fits')
    md = ['# Nirvāna guide: contents test, 2026-11-23', '',
          'For [What If Everything Is Already Perfect? (v2.2)](%s). Run the way the Inner Child and bad trips contents were done '
          '([how](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/docs/FIXING-AN-ARTICLE.md), section 3). '
          'Nothing on the post has changed yet.' % POST, '']
    if os.path.exists(os.path.join(HERE, 'APPLIED.md')):
        md += ['**In the post since 2026-11-23 18:01 UTC:** your picks, your six answers and 13 section links; two of your picks wait for you because they read below High in Pangram ([APPLIED.md](%sAPPLIED.md)).' % GIT, '']
    if page_url:
        md += ['**Your picks page:** [%s](%s). Pick a heading for each section and answer the six questions; your answers save there.' % (page_url, page_url), '']
    md += ['## What fresh readers found', '',
           '%d of the 60 headings are cut off in the sidebar today. The proposal changes %d of the 60 and cuts off none.' % (ncut_now, nchanged), '',
           '| ' + ' | '.join(head_cols) + ' |', '|' + '---|' * len(head_cols)]
    md += ['| %s |' % ' | '.join(str(c) for c in r) for r in rows]
    md += ['', '36 situations, each a reader looking for one thing, written from the text with the headings taken out and checked by '
           'a second reader ([situations](%sSITUATIONS.md), [answer key](%sEXPECTED-REVIEWED.json)). Each fresh reader (Sonnet) saw only one '
           'contents list, drawn as the sidebar draws it, and named the heading they would click first; one number per reader. '
           'Scored by [score_reads.py](%sscore_reads.py). The final list was read with the curly apostrophe in S047, its only '
           'difference from the proposal.' % (GIT, GIT, GIT), '',
           '### Where it changed', '', '| Situation | Right first, with yours | With the final list |', '|---|---|---|']
    md += ['| %s | %d of %d | %d of %d |' % (sit[n], a, len(yourreads), b, len(finalreads)) for n, a, b in changed_sits]
    md += ['', '## The proposal, heading by heading', '',
           '| Line | Yours | Proposed | Why |', '|---|---|---|---|']
    for i in ids:
        e, f = NOW[i], FINAL[i]
        lvl = '#' * e['level']
        yours = '%s %s (%s)' % (lvl, e['heading'].replace('|', '\\|'), st(e['heading'], e['level']))
        if f['heading'] == e['heading']:
            prop, why = 'kept', NOTE.get(i, '')
        else:
            prop = '%s (%s)' % (f['heading'].replace('|', '\\|'), st(f['heading'], e['level']))
            if not same(FABLE[i]['heading'], f['heading']) and not same(FABLE[i]['heading'], e['heading']):
                prop += "<br>Fable's: %s" % FABLE[i]['heading'].replace('|', '\\|')
            why = NOTE.get(i, '')
        extra = evidence(i) + ([flagline(i)] if flagline(i) else [])
        why = '<br>'.join([x for x in [why] + extra if x]).replace('|', '\\|')
        md.append('| %d %s | %s | %s | %s |' % (line[i], i, yours, prop, why))
    md += ['', '## Questions on the page', '']
    for q in questions:
        md.append('- **%s.** %s' % (q['id'], re.sub(r'</?b>', '**', q['text']).replace('&amp;', '&')))
    md += ['', '## How it was done', '',
           '1. The live post read on 2026-11-23 ([its HTML](%sLIVE-BODY-20261123.html), a personal share token removed); '
           '[the sections](%sARTICLE-SECTIONS.md) and the contents as the sidebar shows it ([yours](%sTOC-NOW-SIDEBAR.md)).' % (GIT, GIT, GIT),
           '2. Three fresh readers on yours (two sidebar, one whole headings).',
           '3. Fable renamed with the headings brief ([its list](%sPROPOSAL-FABLE.json), [its notes](%sPROPOSAL-FABLE-NOTES.md)); '
           'the repeat check passed with a fate for every flagged pair ([fates](%sFATES-PICK3.json)).' % (GIT, GIT, GIT),
           '4. Fresh readers on each version: the first proposal (two), Fable’s (one), then four headings changed where readers '
           'went wrong (two), then S033 back to Fable’s (two). [All the reads](%sreads/READ-PICK3-1.md) are in the reads folder.' % GIT,
           '5. No other post of yours links to a section of this one, and this one has no links to its own sections, so renaming breaks no link.',
           '', '## After your picks', '',
           'Your picks go into the post by script ([section_links.py](https://github.com/u-dont-existDOTcom/joel-articles/blob/main/tools/humanization/section_links.py)), '
           'with the sentence fixes a renamed heading needs and the post’s “Updated” date, and I check the sidebar on the live post.', '']
    open(os.path.join(HERE, 'RESULTS.md'), 'w', encoding='utf-8').write('\n'.join(md))
    print('RESULTS.md and PAGE-OPTIONS.json written;', nchanged, 'changed,', ncut_now, 'cut now;', len(changed_sits), 'situations changed')


if __name__ == '__main__':
    main(*sys.argv[1:])
