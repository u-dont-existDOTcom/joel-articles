"""Install Joel's message of 2026-10-15 11:04 UTC (joel-20261015-1104-message.txt). Run from candidate/.

27, "this passes": his section 4 reparenting paragraph and the three-sentence paragraph after it, the two his message
of 2026-10-14 21:19 had meant to include ("here's the fixed reparenting + 3 sentence para:"). Both go in as he wrote
them. The links the article has on "Inner-child reparenting" and "somatic regulation" stay on the same words (his
paste is plain text, as anything copied from the page is). His second paragraph names reparenting ("And this
reparenting journey is built on"), which settles the I1 "it" his way.
"""
import json, pathlib

C = pathlib.Path(__file__).resolve().parents[1]
art_path = C / 'HUMANIZED-SO-FAR.md'
art = art_path.read_text(encoding='utf-8')
WHEN = '2026-10-15 11:04 UTC: "27: this passes:" (joel-20261015/joel-20261015-1104-message.txt)'

L1 = '[Inner-child reparenting](https://ibogaqueen.substack.com/p/inner-child-self-love-tips-and-guided)'
L2 = '[somatic regulation](https://ibogaqueen.substack.com/p/somatic-modalities-strategic-sequencing)'
OLD_A = (L1 + ' means learning to identify as the best inner adult, which is comprised of the three inner adult roles: '
         'Nurturer, Protector, and Guide. The newly developed adult reparents their newly recognized inner child. The '
         'child receives all that love, protection, and guidance that you give it, and in this process actually gains '
         'more freedom to remain alive inside you.')
A_REST = (' means learning to identify as the best holistic inner adult, which is comprised of the three inner adult '
          'roles: Nurturer, Protector, and Guide. The newly developed adult reparents their newly recognized inner child. '
          'The child receives all that love, protection, and guidance that you give it, and as a result, your little one '
          'gains more freedom to remain alive inside you, which brings back the joy of life that many adults have '
          'forgotten about.')
NEW_A = L1 + A_REST
OLD_B = ('And inner pl/ork is built on ' + L2 + " first. Listening to the body's feelings before making a decision with "
         'the mind. And that actually symbolizes the adult/child relationship to me in some way as well.')
B_HEAD = 'And this reparenting journey is built on '
B_REST = (" first. I.e., listening to the body's feelings before making a decision with the mind. And that actually "
          'symbolizes the adult/child relationship to me in some way as well.')
NEW_B = B_HEAD + L2 + B_REST


def rep(t, a, b):
    assert t.count(a) == 1, (a[:60], t.count(a))
    return t.replace(a, b)


art = rep(art, OLD_A, NEW_A)
art = rep(art, OLD_B, NEW_B)
art = rep(art, '<!-- CANDIDATE: section 4 v11.2 (2026-10-14 21:19):',
          '<!-- CANDIDATE: section 4 v11.3 (2026-10-15 11:04): v11.2 with Joel\'s reparenting paragraph and the '
          'three-sentence paragraph after it, as he wrote them ("27: this passes"; joel-20261015/), the links kept on '
          'the same words. Pangram: fix-20261015b/PREDICTIONS.md. Before: section 4 v11.2 (2026-10-14 21:19):')
art_path.write_text(art, encoding='utf-8')

L = json.load(open(C / 'OWNER-EDITS.json', encoding='utf-8'))
have = {e['id']: e for e in L['entries']}
e = have['s4-p11']
e['must_contain'] = [A_REST.strip().split(' The newly')[0][len('means '):],
                     'The newly developed adult reparents their newly recognized inner child.',
                     'your little one gains more freedom to remain alive inside you, which brings back the joy of life that many adults have forgotten about.']
e['what'] += ' (2026-10-15 11:04: his new version, "the best holistic inner adult" and "your little one ... the joy of life"; entry s4-joel-20261015-1104.)'
e = have['s4-p12']
e['must_contain'] = ["first. I.e., listening to the body's feelings before making a decision with the mind.",
                     'symbolizes the adult/child relationship to me in some way as well.']
e['what'] += ' (2026-10-15 11:04: his new version, "And this reparenting journey is built on" and "I.e., listening"; entry s4-joel-20261015-1104.)'
e = have['s4-joel-20261014-i1']
e['must_contain'] = [B_HEAD.strip()]
e['must_not_contain'] = ["And it's built on", 'And inner pl/ork is built on']
e['what'] += (' 2026-10-15 11:04: his own fix names reparenting ("And this reparenting journey is built on"); '
              'that replaces my "inner pl/ork" choice.')
L['entries'].append({
    'id': 's4-joel-20261015-1104', 'status': 'applied', 'when': WHEN,
    'what': 'Section 4, Inner pl/ork: his reparenting paragraph and the three-sentence paragraph after it, as written '
            '(links on "Inner-child reparenting" and "somatic regulation" kept).',
    'joel': open(C / 'joel-20261015' / 'joel-20261015-1104-message.txt', encoding='utf-8').read().split('\n\n', 1)[1].strip(),
    'must_contain_exact': [A_REST.strip(), B_HEAD.strip(), B_REST.strip()],
})
json.dump(L, open(C / 'OWNER-EDITS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
open(C / 'OWNER-EDITS.json', 'a', encoding='utf-8').write('\n')
print('installed; ledger entries:', len(L['entries']))
