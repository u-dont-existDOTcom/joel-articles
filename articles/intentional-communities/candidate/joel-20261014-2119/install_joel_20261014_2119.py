"""Install Joel's answers of 2026-10-14 21:19 UTC (questions 22 to 26) into HUMANIZED-SO-FAR.md and record them in
OWNER-EDITS.json. Run from candidate/.

What goes in:
- 22 and 23 (section 11): his own text of the first subsection, "Founderism: The Four Questions" through "Friends who
  come to visit" (joel-20261014-2119-attachment.txt), as he pasted it: P2 now defines founderism his way ("it's called
  founderism": "founderism isn't my term, it's in the commune literature"), P3 and P4 are his rewrites ("there was too
  much stuff in that p4"), P6 is my lead-in ("P6: ok good use yours"), P8 says "who picks the people who review the
  founder?" ("P8 agree"). His paste also has single spaces where the article had two in J3 ("etc,  and", "court.  Leaving").
- 24: section 4's "If one of the four gets skipped" ("p10 agree"). Section 8's "the research corpus" stays: it's a
  link to the research ("the research corpus is linked in the article... should be linked right there").
- 25 (section 10): his last paragraph, as written ("this version is clearer and passes").
- 26: section 4 without "and don't freeze into doctrine" ("sect 4: yes"); section 9's "The useful thing is how they
  learn:" ("sect 9: yes"); section 11's R15 without "There are pros and cons to each extreme, and again, a living
  balance must be struck." ("sect 11: agree agree"). Section 12: no change ("ok keep both, but free resource should be
  free resource/capacity at first not 2nd so it's defined where it first comes in": its first mention already reads
  "free resource/capacity"; my note on the questions page made it sound as if it didn't).
His characters are kept.
"""
import json, pathlib, re

C = pathlib.Path(__file__).resolve().parents[1]
J = C / 'joel-20261014-2119'
art_path = C / 'HUMANIZED-SO-FAR.md'
art = art_path.read_text(encoding='utf-8')
att = (J / 'joel-20261014-2119-attachment.txt').read_text(encoding='utf-8')
Q = '2026-10-14 21:19 UTC, his answers to questions 22 to 26 (joel-20261014-2119/)'


def rep(t, a, b):
    assert t.count(a) == 1, (a[:60], t.count(a))
    return t.replace(a, b)


def blocks(t):
    return [b.strip() for b in re.split(r'\n\s*\n', t) if b.strip()]


HIS = blocks(att)
assert HIS[0] == '# Founderism: The Four Questions' and HIS[-1].startswith('Friends who come to visit'), HIS[0]
H = {k: next(b for b in HIS if b.startswith(k)) for k in (
    'That person ends up', "I've seen founderism", 'A few things help', 'The questions so far', 'Then follow the practical',
    "It's a bit like the process")}

# section 11, his subsection
s = art.index('# Founderism: The Four Questions')
e = art.index('## How My Own Model Could Become a Cult')
sub = art[s:e]
OLD = {k: next(b for b in blocks(sub) if b.startswith(k)) for k in (
    'That person ends up', 'I know this personally', 'A few things help', 'Here are the four questions', 'Then follow the practical',
    "It's a bit like the process")}
new_sub = sub
for old_k, new_k in (('That person ends up', 'That person ends up'), ('I know this personally', "I've seen founderism"),
                     ('A few things help', 'A few things help'), ('Here are the four questions', 'The questions so far'),
                     ('Then follow the practical', 'Then follow the practical'), ("It's a bit like the process", "It's a bit like the process")):
    new_sub = rep(new_sub, OLD[old_k], H[new_k])
assert [b for b in blocks(new_sub) if not b.startswith('<!--')] == HIS, 'section 11 differs from his paste'
art = art[:s] + new_sub + art[e:]

# section 11, R15 (question 26)
R15_CUT = ' There are pros and cons to each extreme, and again, a living balance must be struck.'
art = rep(art, 'Some communities will be stricter gatekeepers, and others will be more lax.' + R15_CUT,
          'Some communities will be stricter gatekeepers, and others will be more lax.')

# section 4 (questions 24 and 26)
S4_P1_OLD = ('Nothing suppressed, everything processed. Each of us guides our own practice, and our practices weave the community '
             'into the quilt that keeps us all warm and safe. Whatever answers we find stay fluid and organic, and don\'t freeze into doctrine.')
S4_P1_NEW = S4_P1_OLD.replace(', and don\'t freeze into doctrine.', '.')
art = rep(art, S4_P1_OLD, S4_P1_NEW)
art = rep(art, '\nIf one of them gets skipped, it will need to be dealt with eventually,', '\nIf one of the four gets skipped, it will need to be dealt with eventually,')

# section 9 (question 26)
art = rep(art, "The useful thing isn't their diagram. It's how they learn:", 'The useful thing is how they learn:')

# section 10 (question 25)
S10_OLD = next(b for b in blocks(art) if b.startswith('When you create or apply a rule to deal with a collision of two principles'))
S10_NEW = ("Whenever you create or apply a rule, it's best practice to store the full case history so it can be re-evaluated in "
           "future: what happened, the principles that actually conflicted, your first judgments, and your final decision and "
           "rationale. Any dissenting opinions should go in there as well, along with the consequences in the case. When the rule "
           "changes because of a new case, run the old case through again to see how it would turn out. That saves each "
           "generation from having to rediscover the same constitutional fight from scratch.")
msg = (J / 'joel-20261014-2119-message.txt').read_text(encoding='utf-8')
assert S10_NEW in msg
art = rep(art, S10_OLD, S10_NEW)

# candidate notes
NOTE = ' Records: joel-20261014-2119/; Pangram results in fix-20261014b/RESULTS.md. Before: section %s'
art = rep(art, '<!-- CANDIDATE: section 4 v11.1 (2026-10-14):',
          '<!-- CANDIDATE: section 4 v11.2 (2026-10-14 21:19): v11.1 with "If one of the four gets skipped" (Joel\'s 24, '
          '"p10 agree") and without "and don\'t freeze into doctrine" (his 26, "sect 4: yes").' + NOTE % '4 v11.1 (2026-10-14):')
art = rep(art, '<!-- CANDIDATE: section 9 v15 (2026-10-14):',
          '<!-- CANDIDATE: section 9 v16 (2026-10-14 21:19): v15 with "The useful thing is how they learn:" for "The useful '
          'thing isn\'t their diagram. It\'s how they learn:" (Joel\'s 26, "sect 9: yes").' + NOTE % '9 v15 (2026-10-14):')
art = rep(art, '<!-- CANDIDATE: section 10 v2 (2026-10-10),',
          '<!-- CANDIDATE: section 10 v3 (2026-10-14 21:19): v2 with Joel\'s last paragraph of 21:19 UTC, as written ("this '
          'version is clearer and passes").' + NOTE % '10 v2 (2026-10-10),')
art = rep(art, '<!-- CANDIDATE: section 11 v14 (2026-10-14):',
          '<!-- CANDIDATE: section 11 v15 (2026-10-14 21:19): Joel\'s own text of the first subsection, through "Friends who '
          'come to visit", as he pasted it at 21:19 UTC ("i fixed it, pasted.passes pangram"): his P2 definition, P3 and P4, my P6 '
          'lead-in ("ok good use yours"), P8\'s "the people who review the founder" ("agree"); and R15 without its "living balance" '
          'sentence (his 26).' + NOTE % '11 v14 (2026-10-14):')
art_path.write_text(art, encoding='utf-8')

# the ledger
L = json.load(open(C / 'OWNER-EDITS.json', encoding='utf-8'))
have = {e['id']: e for e in L['entries']}
e = have['s11-joel-20261011-1835']
J3_OLD = next(x for x in e['must_contain_exact'] if x.startswith("It's a bit like the process of getting married."))
J3_NEW = H["It's a bit like the process"].split(' Leaving a commune is the divorce half')[0] + ' '
assert J3_NEW.replace(' ', '') == J3_OLD.replace(' ', ''), 'J3 differs by more than spaces'
R15_OLD = next(x for x in e['must_contain_exact'] if x.startswith('Peer counseling can become peer surveillance'))
assert R15_OLD.endswith(R15_CUT.strip())
e['must_contain_exact'] = [J3_NEW if x == J3_OLD else R15_OLD[:-len(R15_CUT)] if x == R15_OLD else x for x in e['must_contain_exact']]
e['what'] += (' (2026-10-14 21:19: J3 with single spaces, as in his paste of section 11; R15 without "There are pros and cons to '
              'each extreme, and again, a living balance must be struck." (his 26); entry s11-joel-20261014-2119 checks both.)')
e = have['s4-joel-20261013-2100']
assert S4_P1_OLD in e['must_contain']
e['must_contain'] = [S4_P1_NEW if x == S4_P1_OLD else x for x in e['must_contain']]
e['what'] += ' (2026-10-14 21:19: without "and don\'t freeze into doctrine", his 26; entry s4-joel-20261014-2119 checks it.)'

new = [
 {'id': 's11-joel-20261014-2119', 'status': 'applied',
  'what': ('Section 11, "Founderism: The Four Questions" through "Friends who come to visit": his own text of 21:19 UTC, as '
           'pasted (P2\'s definition, his P3 and P4, my P6 lead-in, P8\'s "the people who review the founder"); and R15 without '
           'its "living balance" sentence (his 26).'),
  'joel': ('22 no, founderism isn\'t my term, it\'s in the commune literature ... 23 section 11  i fixed it, pasted.passes pangram. '
           'lmk if i overlooked anything, there was too much stuff in that p4 tho | P6: ok good use yours | P8 agree | 26 ... sect 11: agree agree'),
  'when': Q,
  'must_contain_exact': [b for b in HIS[1:]],
  'must_not_contain': ['I call it founderism', 'I know this personally.', 'Here are the four questions about the founder:',
                       'who picks the reviewers?', 'There are pros and cons to each extreme']},
 {'id': 's4-joel-20261014-2119', 'status': 'applied',
  'what': 'Section 4: "If one of the four gets skipped" (his 24, "p10 agree") and P1 of "Founded on Freedom" without "and don\'t freeze into doctrine" (his 26).',
  'joel': '24 ... p10 agree | 26 sect 4: yes', 'when': Q,
  'must_contain': [S4_P1_NEW, 'If one of the four gets skipped, it will need to be dealt with eventually,'],
  'must_not_contain': ["and don't freeze into doctrine", 'If one of them gets skipped']},
 {'id': 's8-joel-20261014-2119', 'status': 'applied',
  'what': 'Section 8: "the research corpus" stays, linked to the research (his 24: "the research corpus is linked in the article... should be linked right there").',
  'joel': '24 the research corpus is linked in the article... should be linked right there. reviewer doesn\'t know about links or something?',
  'when': Q,
  'must_contain': ['I looked through [the research corpus](https://innerself.185-233-106-15.sslip.io/blog/commune-article-research/) for a well-documented case'],
  'must_not_contain': ["all the research I'd gathered"]},
 {'id': 's9-joel-20261014-2119', 'status': 'applied', 'words': 'proposed',
  'what': 'Section 9: "The useful thing is how they learn:" for "The useful thing isn\'t their diagram. It\'s how they learn:" (my proposal, his 26: "sect 9: yes").',
  'joel': '26 ... sect 9: yes', 'when': Q,
  'must_contain': ['The useful thing is how they learn:'], 'must_not_contain': ["The useful thing isn't their diagram."]},
 {'id': 's10-joel-20261014-2119', 'status': 'applied',
  'what': 'Section 10, the last paragraph: his version of 21:19 UTC, as written.',
  'joel': '25 Section 10\'s last paragraph:  this version is clearer and passes: ...', 'when': Q,
  'must_contain_exact': [S10_NEW],
  'must_not_contain': ['to deal with a collision of two principles']},
]
for n in new:
    assert n['id'] not in have
    L['entries'].append(n)
json.dump(L, open(C / 'OWNER-EDITS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('installed; ledger entries', len(L['entries']))
