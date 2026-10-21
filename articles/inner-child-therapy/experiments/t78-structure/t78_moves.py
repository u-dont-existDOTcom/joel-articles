"""Turn 78: apply GPT's r03 moves as Joel picked them (question 70: A).

A = GPT's candidate order, except:
  M01: H066 ("mess and all") stays early, at the start of Before You Try to Go Deep (after H041).
  M04: only Altered States as its own h1 right after When the Adult Voice Feels Fake; Joel's run
       (Altered States ... Physical Pain ... If You Want to Kill Yourself ... This human life) kept in
       his order and levels, except H212 -> h1 and H219 -> h2 (no h1 -> h3 skip). M04's two
       sub-moves (H358 into Hear the Protective Part First, H085 into When to Change the Strategy)
       are not taken: H358 stays with H356/H357, H085 stays in When Healing Turns Into Checking.
       GPT's help-first reorder inside If You Want to Kill Yourself is not taken (question 74).
  M06: only the end sections (How Much Happiness as an h1 with Somatic Heart Opening and When the
       Practice Feels Real but Stays Shallow under it); Ask God for a Loan, PRE-APPROVED! and
       When the Spiritual Relationship Hurts stay in Borrow Love at their levels.
Text: WH143 and WH404 pointer repairs; H216 pointer repair (Timing Is Individual now comes later);
      N001 heading; H298 renamed The Inner Guide; H355 heading dropped (all its paragraphs moved).
"""
import sys, re, json, difflib
sys.path.insert(0, '/tmp/claude-0/-home-claude/f9c31c84-00e6-5c6f-b00e-57cd53c4ea4f/scratchpad/t78')
from t78lib import parse, gpt, norm, ART

OUT = sys.argv[1] if len(sys.argv) > 1 else '/tmp/claude-0/-home-claude/f9c31c84-00e6-5c6f-b00e-57cd53c4ea4f/scratchpad/t78/moved.md'
s, chunks = parse()
fa, B = gpt()
oo, co = fa['original_order'], fa['candidate_order']

# units: preceding comments + one non-comment chunk
units, pending = [], []
for ch in chunks:
    if ch['kind'] == 'comment':
        pending.append(ch['raw'])
    else:
        units.append({'comments': pending, 'chunk': ch}); pending = []
trailing = pending

# map units to GPT ids
gn = [norm(B[i]['original_html'] or '') for i in oo]
mn = [u['chunk']['n'] for u in units]
sm = difflib.SequenceMatcher(a=gn, b=mn, autojunk=False)
gid = {}
for tag, i1, i2, j1, j2 in sm.get_opcodes():
    if tag == 'equal' or (tag == 'replace' and i2 - i1 == j2 - j1):
        for k in range(j2 - j1):
            r = difflib.SequenceMatcher(a=gn[i1 + k][:400], b=mn[j1 + k][:400]).ratio() if tag == 'replace' else 1
            if r > 0.6: gid[j1 + k] = oo[i1 + k]
    elif tag == 'replace':
        for j in range(j1, j2):
            best = max(range(i1, i2), key=lambda i: difflib.SequenceMatcher(a=gn[i][:400], b=mn[j][:400]).ratio())
            if difflib.SequenceMatcher(a=gn[best][:400], b=mn[j][:400]).ratio() > 0.6: gid[j] = oo[best]
uid = {g: j for j, g in gid.items()}
assert len(uid) == len(gid), 'two units mapped to one GPT id'

# target GPT order
T = [x for x in co]
def remove(ids):
    for x in ids:
        if x in T: T.remove(x)
def insert_after(anchor, ids):
    k = T.index(anchor) + 1
    T[k:k] = ids
def insert_before(anchor, ids):
    k = T.index(anchor)
    T[k:k] = ids
remove(['H066']); insert_after('H041', ['H066'])
run = oo[oo.index('H212'):oo.index('H271')]
remove(run); insert_before('H271', run)
loan = oo[oo.index('H120'):oo.index('H135')]
remove(loan); insert_before('H135', loan)
remove(['H358']); insert_after('H357', ['H358'])
remove(['H085']); insert_after('H084', ['H085'])
# sanity: the run in T is Joel's order (GPT's help-first reorder not taken)
assert T[T.index('H257'):T.index('H257') + 4] == ['H257', 'H258', 'H259', 'H260'], T[T.index('H257'):T.index('H257') + 4]

# unit order: mapped units in T order; unmapped units travel with the unit before them
followers, lead, last = {}, [], None
for j, u in enumerate(units):
    if j in gid: last = j
    elif last is None: lead.append(j)
    else: followers.setdefault(last, []).append(j)
drop = {uid['H355']}
order = list(lead)
for x in T:
    if x == 'N001':
        order.append('N001'); continue
    if x in uid:
        j = uid[x]
        if j in drop: continue
        order.append(j); order.extend(followers.get(j, []))
placed = [o for o in order if o != 'N001']
missing = [j for j in range(len(units)) if j not in placed and j not in drop]
dups = [j for j in set(placed) if placed.count(j) > 1]
assert not missing and not dups, (missing[:5], dups[:5])

# the dropped heading's notes go to the next unit (H356)
units[uid['H356']]['comments'] = units[uid['H355']]['comments'] + units[uid['H356']]['comments']

# heading changes
LV = {'H032': 2, 'H055': 2, 'H388': 2, 'H364': 1, 'H371': 2, 'H212': 1, 'H219': 2}
def set_level(j, lv):
    raw = units[j]['chunk']['raw']
    units[j]['chunk']['raw'] = re.sub(r'^#{1,6} ', '#' * lv + ' ', raw, count=1)
for g, lv in LV.items(): set_level(uid[g], lv)
r = units[uid['H298']]['chunk']['raw']
assert r.strip() == '# The Inner Guide Comes Later', r
units[uid['H298']]['chunk']['raw'] = '# The Inner Guide'

# text repairs
def edit(g, old, new):
    raw = units[uid[g]]['chunk']['raw']
    assert raw.count(old) == 1, (g, old)
    units[uid[g]]['chunk']['raw'] = raw.replace(old, new)
edit('H143', 'And you can ask yourself again, ', 'And you can ask yourself, ')
edit('H404', "I'll talk more about those next, but", "I'll talk more about those in the appendix, but")
edit('H216', "it's the same test as back in Timing Is Individual.", "it's the same test as in Timing Is Individual, further down.")

# turn-78 notes, first among each unit's notes
A = "Turn 78 (Joel's answer to question 70: A, 2026-10-21 00:49 UTC, experiments/t78-answers/JOEL-20261021-0049.md; GPT's r03 files in experiments/t78-structure/gpt-r03/)"
NOTES = {
 'H309': f"<!-- {A}: these four paragraphs on not handing over your judgment moved here from The Inner Guide (GPT's M05). -->",
 'H066': f"<!-- {A}: Joel's \"mess and all\" paragraph stays early, here at the start of Before You Try to Go Deep, so the order doesn't tell people to wait until they're sorted out; the rest of First Social Connections, Done Right moved to Borrowed Adulthood in Relationship (GPT's M01, my change). -->",
 'H356': f"<!-- {A}: When Love Still Feels Missing's three paragraphs moved here (GPT's M02 moved the first two; the third, whose \"Taking the hostility out\" carries on the second's \"least cruel response\", came with them instead of going to Hear the Protective Part First). The heading went, since all of its paragraphs moved. -->",
 'H317': f"<!-- {A}: Borrow Hindsight and Remember When You Already Did It moved here from Simple Practices, and Notice the Part That Came Here from When Love Still Feels Missing (GPT's M02). -->",
 'H080': f"<!-- {A}: When Healing Turns Into Checking moved here from Before You Try to Go Deep, just before Simple Practices (GPT's M03). Its outcomes paragraph stays in it (M04's move of it not taken). -->",
 'H316': f"<!-- {A}: Simple Practices moved here, right after Building Trust, with Catch the Hook as its first practice (GPT's M03). -->",
 'H049': f"<!-- {A}: Catch the Hook moved here from Before You Try to Go Deep; Other Folks Also Have Hooks went to Borrowed Adulthood in Relationship (GPT's M03, M07). -->",
 'H212': f"<!-- {A}: Altered States is its own h1 here, right after When the Adult Voice Feels Fake, which now ends on the escape warning. Joel's run (altered states, physical pain, If You Want to Kill Yourself) stays together in his order (GPT's M04 as I'd change it); When Escape Leaves Reality Behind is an h2 under it. -->",
 'H298': f"<!-- {A}: renamed from The Inner Guide Comes Later, since its Timing Is Individual says the Guide doesn't always come later; its four paragraphs on handing over your judgment moved to Don't Give the Inner Adult Away (GPT's M05). -->",
 'H364': f"<!-- {A}: How Much Happiness Do You Know Is Possible? is an h1 here near the end, with Somatic Heart Opening and When the Practice Feels Real but Stays Shallow under it as h2s (GPT's M06, the half I'd take; Ask God for a Loan stays in Borrow Love). -->",
 'H384': f"<!-- {A}: one relationship chapter: First Social Connections, Done Right, Opening up honestly, Other Folks Also Have Hooks, Write It. Don't Send It Yet., Speak Toward What You Are Building (now an h2) and GPT's new heading Hearthwork: Taking Turns (GPT's M07). -->",
 'H401': f"<!-- {A}: Finding a Therapist to Borrow Adulthood moved before You Are Worthy of Love. Always., so the article ends on the encouragement, then the Appendix (GPT's M08). -->",
}
for g, n in NOTES.items():
    units[uid[g]]['comments'] = [n] + units[uid[g]]['comments']

# emit
parts = []
for o in order:
    if o == 'N001':
        parts.append(f"<!-- {A}: GPT's new heading for the peer-counseling paragraphs (M07); its wording, which Joel can change. -->")
        parts.append('## Hearthwork: Taking Turns'); continue
    if o == uid['H271']:
        parts.append("<!-- Turn 78: Joel's divider after If You Want to Kill Yourself, as in his 2026-10-19 upload (turn 77's rebuild left it out). -->")
        parts.append('---')
    parts.extend(units[o]['comments']); parts.append(units[o]['chunk']['raw'])
parts.extend(trailing)
out = '\n\n'.join(parts) + '\n'
open(OUT, 'w', encoding='utf-8').write(out)
json.dump({'gid': {str(j): g for j, g in gid.items()}, 'order': order, 'unmapped_units': [j for j in range(len(units)) if j not in gid],
           'unmapped_gpt': [g for g in oo if g not in uid]}, open(OUT + '.map.json', 'w'), indent=0)
print('units', len(units), 'mapped', len(gid), 'unmapped units', [(j, units[j]['chunk']['n'][:50]) for j in range(len(units)) if j not in gid])
print('unmapped GPT ids', [g for g in oo if g not in uid])
print('wrote', OUT, len(out), 'chars (was', len(s), ')')
