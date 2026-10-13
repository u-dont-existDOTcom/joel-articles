"""Install Joel's section 4 and section 12 of his 2026-10-13 21:00 UTC message (joel-20261013-attachment.txt)
into HUMANIZED-SO-FAR.md, and record them in OWNER-EDITS.json. Run from candidate/.

His text goes in as written, with only these changes:
- obvious typos: "otther" -> "other", "heal. and" -> "heal and", "3:" -> "3)" in his numbered list, double spaces,
  trailing spaces;
- in his section 4 P8, the published words that came along from the side-by-side page's struck text are taken out
  ("taken critically. Most are treasure. Some seem like late additions. I consider the Abhidhamma a scholastic wrong
  turn." and "the same way: devoted enough to practice them and secure enough to disagree."). His own ruling of
  2026-10-02 cut them (ledger s4-p13 bans "Abhidhamma" and "secure enough to disagree"); what is left is his v10
  paragraph with his new opening. The same thing happened with his section 8 P10 on 2026-10-07;
- links and italics put back where his words keep their anchor text, and the published images where they stood.
"""
import json, pathlib, re

C = pathlib.Path(__file__).resolve().parents[1]
J = C / 'joel-20261013'
art_path = C / 'HUMANIZED-SO-FAR.md'
art = art_path.read_text(encoding='utf-8')


def lines(name):
    return [l.rstrip() for l in (J / name).read_text(encoding='utf-8').split('\n') if l.strip()]


def fix(t):
    t = re.sub(r'(?<=\S)  +(?=\S)', ' ', t)
    return t.rstrip()


def rep(t, a, b):
    assert t.count(a) == 1, (a, t.count(a))
    return t.replace(a, b)


IMG7 = '[image 7](https://substackcdn.com/image/fetch/$s_!vVsb!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe8999a94-f206-40e6-9a8d-bb9afa8c38fe_800x560.svg)'
IMG8 = '[image 8](https://substackcdn.com/image/fetch/$s_!7tAF!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F66730244-8446-4321-83f0-f353d46a8e1e_770x844.jpeg)'
IMG17 = '[image 17](https://substackcdn.com/image/fetch/$s_!3uG-!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7daf9ea4-807c-49c1-99b3-6993e837a010_800x540.svg)'
for img in (IMG7, IMG8, IMG17):
    assert img in art, img[:40]

# ---------- section 4 ----------
s4 = [fix(l) for l in lines('s4-joel-raw.txt')]
assert s4[0] == 'The Four Parts That Have to Pl/ork Together' and s4[5] == 'Founded on Freedom'
p = {i: s4[i] for i in range(len(s4))}
p[2] = rep(p[2], '3: medicine pl/ork', '3) medicine pl/ork')
p[2] = rep(p[2], 'I hope pl/ork isn’t too corny.', 'I hope *pl/ork* isn’t too corny.')
p[4] = rep(p[4], 'We help each otther heal. and choose love over fear.', 'We help each other heal and choose love over fear.')
p[4] = rep(p[4], 'using the escuelita model', 'using the *escuelita* model')
p[9] = rep(p[9], ' taken critically. Most are treasure. Some seem like late additions. I consider the Abhidhamma a scholastic wrong turn. with a critical reading.', ' with a critical reading.')
p[9] = rep(p[9], 'teachings the same way: devoted enough to practice them and secure enough to disagree. in that same critical manner', 'teachings in that same critical manner')
p[9] = rep(p[9], 'the early Buddhist suttas,', 'the early [Buddhist suttas](https://suttacentral.net/),')
p[12] = rep(p[12], 'Inner-child reparenting means', '[Inner-child reparenting](https://ibogaqueen.substack.com/p/inner-child-self-love-tips-and-guided) means')
p[13] = rep(p[13], 'built on somatic regulation first', 'built on [somatic regulation](https://ibogaqueen.substack.com/p/somatic-modalities-strategic-sequencing) first')
p[15] = rep(p[15], 'Hearthwork distributes', '[Hearthwork](https://ibogaqueen.substack.com/p/hearthwork-an-integrated-peer-counseling) distributes')
p[18] = rep(p[18], 'check out my Romance Guide,', 'check out my [Romance Guide](https://ibogaqueen.substack.com/p/romance-advice-i-wish-my-parents),')
p[26] = rep(p[26], 'in the Bruderhof community', 'in the [Bruderhof](https://www.bruderhof.com/intentional-community) community')
p[26] = rep(p[26], 'at Twin Oaks,', 'at [Twin Oaks](https://www.twinoaks.org/about-twinoaks-community/about-income-sharing),')
heads = {0: '# ', 5: '## ', 10: '### ', 14: '### ', 19: '### ', 22: '### '}
blocks = []
for i in range(len(s4)):
    blocks.append(heads.get(i, '') + p[i])
    if i == 0:
        blocks.append(IMG7)
    if i == 11:
        blocks.append(IMG8)
s4_md = '\n\n'.join(blocks)
note4 = ('<!-- CANDIDATE: section 4 v11 (2026-10-13): Joel\'s final section from his message of 2026-10-13 21:00 UTC ("here is '
         'the final section (human on pangram)"), as written; obvious typos fixed (otther, "heal. and", "3:", double spaces); in '
         'his P8 the published words that came along from the side-by-side page\'s struck text taken out (his own 2026-10-02 '
         'cut, ledger s4-p13); links, italics and the two images back where they stood. Records: joel-20261013/. Not accepted '
         'until Joel says so. -->')
start = art.index('<!-- CANDIDATE: section 4 v10')
end = art.index('<!-- Section 5:', start)
art = art[:start] + note4 + '\n\n' + s4_md + '\n\n' + art[end:]

# ---------- section 12 ----------
s12 = [fix(l) for l in lines('s12-joel-raw.txt')]
assert s12[0] == 'The Math of Absorption, and Who This Isn’t For'
q = {i: s12[i] for i in range(len(s12))}
q[5] = rep(q[5], 'a lot of peer counseling going on', 'a lot of [peer counseling](https://ibogaqueen.substack.com/p/hearthwork-an-integrated-peer-counseling) going on')
q[7] = rep(q[7], '“free resource,”', '“[free resource](https://www.rc.org/),”')
q[9] = rep(q[9], 'Then she took my son.', 'Then [she took my son](https://youtu.be/0eOInpVYnsk?si=dbxjP76Rbk5FmjDs).')
q[15] = rep(q[15], 'a good fit for you right now if:', 'a good fit for you *right now* if:')
blocks = []
for i in range(len(s12)):
    blocks.append(('# ' if i == 0 else '') + q[i])
    if i == 4:
        blocks.append(IMG17)
s12_md = '\n\n'.join(blocks)
note12 = ('<!-- CANDIDATE: section 12 v12 (2026-10-13): Joel\'s rewrite from his message of 2026-10-13 21:00 UTC ("section 12 i '
          'rewrote a bit, still passes pangram fully"), as written; trailing spaces taken out; links, the italics on "right now" '
          'and image 17 back where they stood. Records: joel-20261013/. Not accepted until Joel says so. -->')
start = art.index('<!-- CANDIDATE: section 12 v11')
end = art.index('# Your Little Forming Group Already Is the Community', start)
art = art[:start] + note12 + '\n' + s12_md + '\n\n' + art[end:]
art_path.write_text(art, encoding='utf-8')
(J / 'section4-v11.md').write_text(s4_md + '\n', encoding='utf-8')
(J / 'section12-v12.md').write_text(s12_md + '\n', encoding='utf-8')

# ---------- ledger ----------
L = json.load(open(C / 'OWNER-EDITS.json', encoding='utf-8'))
have = {e['id']: e for e in L['entries']}
for old, new in [('s12-joel-20261012-1723', 's12-joel-20261013-2100'), ('s4-joel-20261012-1723', 's4-joel-20261013-2100')]:
    have[old]['status'] = 'superseded'
    have[old]['superseded_by'] = new
plain = lambda t: re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', t).replace('*', '')
E = [
 {'id': 's4-joel-20261013-2100',
  'what': 'Section 4: Joel\'s final section from his message of 2026-10-13 21:00 UTC ("here is the final section (human on pangram)"), '
          'as written. It moves the pl/ork definition and the leaking paragraph up under the four-parts heading, rewrites the '
          'old P3 ("And let\'s face it: ... That\'s more like a situationship."), renames "One principle runs through all of them" '
          'to "Founded on Freedom" (P1 less individualistic: "our practices weave the community into the quilt"), opens inner '
          'pl/ork with reparenting, rewrites the listener paragraph, merges the jealousy lines with the Romance Guide, makes '
          'medicine pl/ork and the container open with full sentences, gives his reason for less money, and puts back that the '
          'container gives the first three a stable place. Obvious typos fixed; the struck published words in his P8 taken out '
          '(his own cut, s4-p13).',
  'status': 'applied',
  'joel': 'p4-p3 is terrible ... the heading also doesn\'t make sense with the first para ... here is the final section (human on pangram), try to learn lessons and see what you could have figured out yourself',
  'must_contain': [plain(p[i]) for i in (3, 4, 6, 7, 11, 17, 20, 23, 24, 31)] + [
      'Note, Pl/ork means play + work.', 'Speaking of jealousy, check out my',
      'To give an example of striking the balance: My contemplative practice is grounded in the early'],
  'must_not_contain': ['One principle runs through all of them', 'In a nutshell', 'Also, a note on agreements',
                       'and this part is the container itself', 'Doing serious plant medicines carefully',
                       'Membership, land, resources, governance', 'Personally, I’m aiming',
                       'It covers the dyads that will form']},
 {'id': 's12-joel-20261013-2100',
  'what': 'Section 12: Joel\'s rewrite from his message of 2026-10-13 21:00 UTC ("section 12 i rewrote a bit, still passes pangram '
          'fully"), as written: "like a Heavy Flow Maxi Pad", "in different ratios", the eight-versus-eighty paragraph cut and its '
          'point folded into "Once there are 80 members ...", "a difficult catch-22 for fledgling groups", "dangerously tilted '
          'towards elitism", "submit it to yourself", and the crisis item folded into the first item with "free resource '
          'calculator". Trailing spaces taken out; links and the italics on "right now" back.',
  'status': 'applied',
  'joel': 'then section 12 i rewrote a bit, still passes pangram fully',
  'must_contain': [plain(q[i]) for i in (3, 6, 8, 12, 13, 14, 16)] + ['But before you submit your application to the community, submit it to yourself.'],
  'must_not_contain': ['There is a difficult paradox to consider.', 'The problem is that, in a group of eight people',
                       'and the ratio varies', '(A founding group shouldn’t pretend it can give you those.)']},
]
for e in E:
    if e['id'] not in have:
        L['entries'].append(e)
json.dump(L, open(C / 'OWNER-EDITS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('installed section 4 v11 and section 12 v12; ledger entries', len(L['entries']))
