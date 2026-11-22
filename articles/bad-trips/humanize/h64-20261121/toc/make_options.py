#!/usr/bin/env python3
"""make_options.py - PAGE-OPTIONS.json for make_page.py: the options (my pick, Fable's), the readers' scores, the
starting pick for each heading, a note on each changed heading (what it keeps of his words, what it loses, and the
remedy's evidence tag, which goes on its own line under the heading), and the sentences in the text that name a heading.

  python3 make_options.py
"""
import json, os, re
HERE = os.path.dirname(os.path.abspath(__file__))
G = 'https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/bad-trips-20261105/articles/bad-trips/humanize/h64-20261121/toc/'
NOW = {e['id']: e for e in json.load(open(os.path.join(HERE, 'NOW.json'), encoding='utf-8'))}
FAB = {e['id']: e for e in json.load(open(os.path.join(HERE, 'PROPOSAL-FABLE.json'), encoding='utf-8'))}
PICK = {e['id']: e for e in json.load(open(os.path.join(HERE, 'PROPOSAL-PICK.json'), encoding='utf-8'))}
SC = {r['reader']: r for r in json.load(open(os.path.join(HERE, 'SCORES.json'), encoding='utf-8'))['rows']}

TAGS = {'B152': 'Tried by Me and Friends', 'B159': 'Standard for Poisoning', 'B166': 'Tried by Me and Friends',
        'B181': 'Tried by Me and Friends', 'B183': 'Tried by Me and Friends', 'H54-CREATINE-H': 'Tried by Me',
        'H54-MANGO-H': 'Tried by Me and Friends', 'R30-OILS1': 'Tried by Me and Friends', 'B199': 'Some Human Studies',
        'R30-RUE1': 'Tried by Me and Friends', 'B185': 'Tried by Me and Friends', 'B189': 'Tried by Me and Friends',
        'B170': 'Tried by Me and Friends', 'B210': 'Tried by Me and Friends'}
EXTRA = {
    'B152': 'Both readers of Fable\'s list couldn\'t tell what ZHoly3O is; it stays, since it\'s your product and the link.',
}


def row(label, keys):
    rs = [SC[k] for k in keys if k in SC]
    f = ', '.join(str(r['first_right']) for r in rs)
    g = ', '.join(str(r['guesses']) for r in rs)
    s = ', '.join(str(r['right_by_second']) for r in rs)
    return '<tr><td>%s</td><td class="n">%d</td><td class="n">%s</td><td class="n">%s</td><td class="n">%s</td></tr>' % (label, len(rs), f, g, s)


notes, pick = {}, {}
for i, e in NOW.items():
    p, f = PICK[i], FAB[i]
    if p['heading'] != e['heading']:
        pick[i] = 'pick'
    parts = []
    if p.get('from') == 'pick':
        parts.append('My pick: ' + p['why'][0].upper() + p['why'][1:] + '.')
    elif f.get('why') and f['heading'] != e['heading']:
        why = f['why'].rstrip('.')
        for x, y in ((r'\bhis\b', 'your'), (r'\bHis\b', 'Your'), (r"\bhe'd\b", "you'd"), (r'\bhe prefers\b', 'you prefer'),
                     (r'\bhe\b', 'you'), (r'\bHe\b', 'You'), (r'\bhim\b', 'you')):
            why = re.sub(x, y, why)
        why = re.sub(r'needs the new name \(rule 9\)', 'takes the new name', why)
        parts.append('Fable: ' + why + '.')
    if i in EXTRA:
        parts.append(EXTRA[i])
    if i in TAGS:
        parts.append('Its evidence tag goes on its own line just under the heading, so the heading still fits: <b>[%s]</b>.' % TAGS[i])
    if parts:
        notes[i] = ' '.join(parts)

n_now = len(NOW)
cut_now = 46
q = ('<b>Substack\'s sidebar cuts 46 of your 62 headings.</b> I gave Fable the headings brief the inner child lane made from your '
     'picks there (every heading fits its room, says what the reader came for, keeps your words and your playful ones where '
     'it can). It kept 11 as they are and shortened 51, all of them fitting. Then fresh readers, who saw only a contents as the '
     'sidebar shows it, said where they would look first in 32 situations a reader brings (written from the text with the '
     'headings taken out, and checked by a second reader).<br><br>'
     '<b>Your evidence tags go under the headings, not in them</b>: in a heading, "[Tried by Me and Friends]" alone takes more '
     'than an h3\'s room, so the remedy\'s name would be cut. Each remedy below shows its tag.<br><br>'
     '<b>Each heading starts on my pick</b>: Fable\'s, with three headings back in your words where its readers went wrong '
     '("MDMA: Magnesium Alarm", "Trip After Trip?", "Feeling Good Forever?"). Change any you like, or use a button; your answers '
     'save as you click. When you\'re done, tell me in the chat (or press "Copy my answers" and paste them).')
table = ('<table class="sc"><tr><th>Contents</th><th>Readers</th><th>First pick right (of 32)</th><th>Guesses (of 32)</th>'
         '<th>Right by the 2nd pick</th></tr>' + row('Yours, as the sidebar cuts it', ['NOW-1', 'NOW-2'])
         + row('Fable\'s', ['FABLE-1', 'FABLE-2']) + row('My pick', ['PICK-1', 'PICK-2']) + '</table>')
git = ('This page is a view of files in Git: <a href="%sRESULTS.md">what the readers found, each heading and the 32 '
       'situations</a>.' % G)
pointers = ['"(more on that in Active Seizure)", in the DMSO section: Active Seizure keeps its heading.',
            '"(see Mental Stabilizers That Don\'t Abort the Trip)", in the Grounding Menu\'s Smell line: it takes the new name of '
            'that section, with a link to it.']
json.dump({'title': 'Bad Trips Guide, Round 47: Headings for the Sidebar', 'date': '21 November 2026',
           'options': {'pick': {'label': 'My pick', 'file': 'PROPOSAL-PICK.json'},
                       'fable': {'label': 'Fable\'s', 'file': 'PROPOSAL-FABLE.json'}},
           'hide_columns': [], 'scores': {'question': q, 'table': table, 'git': git}, 'pick': pick, 'notes': notes,
           'pointers': pointers}, open(os.path.join(HERE, 'PAGE-OPTIONS.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('options written;', len(pick), 'headings start on my pick;', len(notes), 'notes')
