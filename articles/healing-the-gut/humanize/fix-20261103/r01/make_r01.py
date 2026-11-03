#!/usr/bin/env python3
"""Apply Joel's r01 decisions (2026-11-03 19:12 UTC, experiments/t03-answers) to master.html, writing r01.html.

Structure only, no humanizing: G1 explainer, G2 phase pointers, G3 phases in the Gem's order, G4 Phase 5 points to the
fuels, G5-G10 "My notes" lines (G5 with his sleep page linked, per his comment), G11 berberine note, G12 straight
apostrophes and quote marks everywhere in the reader text, G14 the Gem prompt replaced by his Google Doc link. G13 (the
stacks section) is kept; his answer goes into its humanizing. No API calls.
"""
import copy, hashlib, pathlib, re

from bs4 import BeautifulSoup, NavigableString

HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parents[2]
SRC = ART / 'master.html'
DOC = 'https://docs.google.com/document/d/18VZSIq0uCWRp_ECFg4YfdI49K-bu1BLV/edit?usp=sharing&ouid=106711125606588784425&rtpof=true&sd=true'

html = SRC.read_text(encoding='utf-8')
soup = BeautifulSoup(html, 'html.parser')


def one(found, what):
    assert len(found) == 1, '%s: %d matches' % (what, len(found))
    return found[0]


def li_starting(label):
    return one([li for li in soup.find_all('li') if li.find('p') and li.find('p').get_text().startswith(label)], label)


def new(tag, text=None, **attrs):
    t = soup.new_tag(tag, **attrs)
    if text is not None:
        t.string = text
    return t


def notes_li(parts):
    """<li><p><strong>My notes:</strong> parts...</p></li>; parts are strings or (text, href) links."""
    li, p = new('li'), new('p')
    p.append(new('strong', 'My notes:'))
    p.append(NavigableString(' '))
    for x in parts:
        if isinstance(x, tuple):
            p.append(new('a', x[0], href=x[1], target='_blank', rel='noopener noreferrer nofollow'))
        else:
            p.append(NavigableString(x))
    li.append(p)
    return li


# G2: a phase pointer after each cause's name, before its colon (the Gem's numbering, G3)
POINTERS = [('Severe stress/adrenal fatigue/poor sleep', '(Phase 1)'), ('Sitting, or lack of exercise and stretching', '(Phase 5)'),
            ('Years of accumulated shit in your guts', '(closest: Phase 4)'), ('Poor diet now', '(Phase 2)'),
            ('Parasites, H. pylori, mold, metals', '(Phases 3 and 6)'), ('SIBO', '(Phases 3 and 5)'),
            ('Plant foods', '(Phases 2 and 5)'), ('Leaky gut', '(Phase 5)'), ('IBS', '(Phase 4)'),
            ('Low stomach acid, enzymes, and thick bile', '(Phase 1)')]
for label, ptr in POINTERS:
    p = li_starting(label).find('p')
    if label.startswith('Parasites'):          # the colon is inside the bold label here
        st = p.find('strong')
        assert st.string == label + ':'
        st.string = label
        st.insert_after(NavigableString(' ' + ptr + ':'))
        continue
    # the first text node after the label that starts with ':'
    seen = ''
    for node in p.descendants:
        if isinstance(node, NavigableString):
            if len(seen) >= len(label) and node.startswith(':'):
                node.replace_with(NavigableString(' ' + ptr + str(node)))
                break
            seen += str(node)
    else:
        raise SystemExit('no colon after label %r' % label)

# G1: the explainer after Joel's NOTE
note = one([p for p in soup.find_all('p') if p.get_text().startswith('NOTE: this gut gem does not include')], 'NOTE')
note.append(NavigableString('So the phases below are only what the Gem will tell you, from the nine books. Where my notes in the causes above change or add to a phase, I point back to them under "My notes" in that phase.'))

# G3: the phases in the Gem's order
h4 = {re.sub(r'\s+', ' ', h.get_text()).split(':')[0]: h for h in soup.find_all('h4')}
ul = {k: h.find_next_sibling('ul') for k, h in h4.items()}
# Phase 4 (Nuclear option) becomes the Purge's last step
purge_ol = ul['Phase 3'].find('ol')
nuc_logic = one([p for p in ul['Phase 4'].find_all('p') if p.get_text().startswith('The Logic:')], 'nuclear logic')
nuc_step = ul['Phase 4'].find('ol').find('li')
step = new('li')
sp = new('p')
sp.append(new('strong', 'The “Nuclear” Option (Ruscio):'))
sp.append(NavigableString(' ' + nuc_logic.get_text().replace('The Logic: ', '', 1) + ' '))
for c in list(nuc_step.find('p').contents):
    sp.append(copy.copy(c))
step.append(sp)
purge_ol.append(step)
h4['Phase 4'].decompose()
ul['Phase 4'].decompose()
# Phase 5 (Investigation) becomes Phase 4, Brown only
h = h4['Phase 5']
h.clear()
h.append(new('strong', 'Phase 4: The Investigation (The Detective)'))
inv = ul['Phase 5']
src = one([p for p in inv.find_all('p') if p.get_text().startswith('Source:')], 'inv source')
for em in src.find_all('em')[1:]:
    pass
src.clear()
src.append(new('strong', 'Source:'))
src.append(NavigableString(' Benjamin Brown ('))
src.append(new('em', 'Digestive Health Solution'))
src.append(NavigableString(')'))
logic = one([p for p in inv.find_all('p') if p.get_text().startswith('The Logic:')], 'inv logic')
logic.append(NavigableString(' (The last two are Phase 6, below.)'))
inv_steps = inv.find('ol').find_all('li', recursive=False)
env_step, brain_step = inv_steps[1], inv_steps[2]
assert env_step.get_text().startswith('Check Environment') and brain_step.get_text().startswith('Check Brain')
env_step.extract(); brain_step.extract()
# Phase 6 (Restoration) becomes Phase 5
h = h4['Phase 6']
h.clear()
h.append(new('strong', 'Phase 5: Restoration & Maintenance (The Gardener)'))
rest = ul['Phase 6']
# G4: Fuel the Mitochondria points back to Leaky gut
fuel = one([li for li in rest.find_all('li') if li.get_text().startswith('Fuel the Mitochondria')], 'fuel')
fuel.clear()
fp = new('p')
fp.append(new('strong', 'Fuel the Mitochondria:'))
fp.append(NavigableString(' see the fuels under Leaky gut, above (glutamine, butyrate and TCA intermediates).'))
fuel.append(fp)
# the new Phase 6: Refractory Cases, with Nathan's and Hopper's steps moved word for word
h6 = new('h4')
h6.append(new('strong', 'Phase 6: Refractory Cases (The Hazmat Team)'))
u6 = new('ul')
for lab, rest_parts in (('Source:', [' Neil Nathan (', ('em', 'Toxic'), '), Annie Hopper (', ('em', 'Wired for Healing'), ')']),
                        ('The Logic:', [' For cases that are "sensitive to everything," or that relapse right away despite perfect adherence.'])):
    li, p = new('li'), new('p')
    p.append(new('strong', lab))
    for x in rest_parts:
        p.append(new(x[0], x[1]) if isinstance(x, tuple) else NavigableString(x))
    li.append(p)
    u6.append(li)
li, p = new('li'), new('p')
p.append(new('strong', 'The Protocol:'))
li.append(p)
ol6 = new('ol')
ol6.append(env_step)
ol6.append(brain_step)
li.append(ol6)
u6.append(li)
rest.insert_after(h6)
h6.insert_after(u6)

# G5-G10: "My notes" at the end of each phase
phase_ul = {}
for h in soup.find_all('h4'):
    k = re.sub(r'\s+', ' ', h.get_text()).split(':')[0]
    phase_ul[k] = h.find_next_sibling('ul')
NOTES = {
    'Phase 1': ['for stress and ', ('sleep', 'http://sleep.u-dont-exist.com'), ' see Severe stress above, and for stomach acid and bile see Low stomach acid.'],
    'Phase 2': ['see Poor diet now and Plant foods, above.'],
    'Phase 3': ["the H2O2 swap above is mine, not the books'. For berberine and H. pylori see Parasites, and for SIBO yogurt see SIBO, above."],
    'Phase 4': ["two things the books don't cover, old impaction and colon hydrotherapy (Years of accumulated shit, above) and psychedelics for IBS (IBS, above)."],
    'Phase 5': ['see Leaky gut above for colostrum, zinc carnosine, BPC-157, ozonated zeolite and the fuels, and Sitting above for movement and yoga.'],
    'Phase 6': ["Matt's note on mopping up mycotoxins with fermented colostrum is under Leaky gut, above."],
}
for k, parts in NOTES.items():
    phase_ul[k].append(notes_li(parts))

# G11: berberine
berb = one([p for p in soup.find_all('p') if p.get_text().startswith('I would not recommend general')], 'berberine')
berb.append(NavigableString(' (My own advice is different for H. pylori, where berberine works well: see Parasites, above.)'))

# G14: the Gem prompt moves to his Google Doc; paid subscribers get the link below the paywall line
pw = soup.find('div', class_='paywall-editor')
for sib in list(pw.find_next_siblings()):
    sib.decompose()
lp = new('p')
lp.append(NavigableString('Here they are, in a Google Doc: '))
lp.append(new('a', 'Gut Health Architect custom instructions', href=DOC, target='_blank', rel='noopener noreferrer nofollow'))
lp.append(NavigableString('.'))
pw.insert_after(lp)

# G12: straight apostrophes and quote marks in every piece of reader text (attributes and URLs untouched)
STRAIGHT = str.maketrans({'‘': "'", '’': "'", '“': '"', '”': '"'})
for node in list(soup.find_all(string=True)):
    if node.parent.name in ('script', 'style'):
        continue
    s = str(node)
    t = s.translate(STRAIGHT)
    if t != s:
        node.replace_with(NavigableString(t))

out = str(soup)
(HERE / 'r01.html').write_text(out, encoding='utf-8')
print('r01.html', hashlib.sha256(out.encode('utf-8')).hexdigest())
