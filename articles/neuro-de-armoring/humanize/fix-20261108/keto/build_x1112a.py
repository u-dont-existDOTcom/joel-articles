"""Neuro De-Armoring Cards, 12 November: the rats and the salts in his clause (SC-48c).

His answers on x1111c (exported 2026-11-12 18:23 UTC) sent SC-48b back with his version, now in the article
(apply_x1111c.py). His clause, checked against the review he cites (KETO-PTSD.md, "His clause, checked"), says two things
the review says differently: the rats were given BHB by injection, not the salts, and the review calls it an open
question whether the salts can match the diet in people. Texts in texts_x1111d.py; the fresh reads are
needed/sp48c/READ.md and his-fixes/sp48c/READ.md.

  python3 articles/neuro-de-armoring/humanize/fix-20261108/keto/build_x1112a.py
"""
import datetime
import hashlib
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parents[1]
ROOT = H.parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent / 'sci-cde'))
import sense_receipt as S  # noqa: E402
import suggestion_review as sr  # noqa: E402
import texts_x1111c as C  # noqa: E402
import texts_x1111d as T  # noqa: E402
from build_x1108b import Q_ANS  # noqa: E402

BLOB = 'https://github.com/u-dont-existDOTcom/joel-articles/blob/main/'
LANE = 'articles/neuro-de-armoring/humanize/'
REL = LANE + 'fix-20261108/keto/'
KEY = 'SP48C'
MD = (H / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
BL = sr.blocks(MD)
RAW = [x for x in re.split(r'\n\s*\n', MD) if x.strip()]
READER = ('someone with trauma or in withdrawal who is anxious, wired, numb or foggy, wanting to know what is going on in '
          'their brain and which of the protocol\'s tools does what')
WHOSE = ('his own: block 48\'s first four sentences, as he wrote them in his answer on SC-48 (2026-11-08 15:08 UTC, '
         'APPLIED-X1108B.json)')
HIS = T.plain(C.HIS)
BENGAY = 'That\'s a bit like putting some Bengay on a broken leg.'
MOUSE = ('and in mice that couldn\'t hold on to extinction learning (learning that a cue is now safe), an HDAC blocker made '
         'the new learning last (Whittle & Singewald, 2014).')
FORUM = 'some astounding BHB salt reviews on forums, like for brain injury repair'
RATS = 'BHB injections work for rats with trauma'


def new_block():
    (r,) = [k for k, x in enumerate(RAW) if x.startswith(T.START)]
    new = RAW[r]
    for a, b in T.SWAPS:
        assert new.count(a) == 1, a
        new = new.replace(a, b)
    return new


NEW_MD = new_block()
S8_NEW = [s for s in S.sentences(T.plain(NEW_MD)) if s.startswith('No controlled trial')][0]
SPLIT = S8_NEW.replace('(Youssef, et al, 2022), although we can see', '(Youssef, et al, 2022). But we can see')
assert SPLIT != S8_NEW

CARD = dict(
    id='SC-48c', title='The rats and the salts in your clause: what the review you cite says',
    what='Two phrases in the clause you added to block 48\'s last sentence change to what the review you cite says: "the '
         'salts work for rats with trauma" becomes "BHB injections work for rats with trauma", and "although not nearly as '
         'proven for humans as the keto diet is" becomes "although in humans it\'s still an open question whether the '
         'salts work as well as the keto diet".',
    why='Your version is in, as you wrote it, with a broken link, a typo and the citation\'s brackets fixed. Checked '
        'against the review you cite ([Engelhardt, et al, 2026](%s)), two points read differently there. The rats '
        'weren\'t given the salts: BHB injected under the skin eased their anxiety after a trauma model ([Yamanashi, et '
        'al, 2020](%s)), BHB injected twice a day for a week prevented anxiety and fear behaviors in male and female rats '
        '([Jung, et al, 2025](%s)), and MCT oil by mouth, which raises BHB, reduced anxiety ([Yoshioka, et al, 2026](%s)). '
        'None had the salts by mouth, which is what a reader on Strategy A takes. And the review doesn\'t rank the salts '
        'below the diet in people: it says no ketogenic therapy has yet been shown to work for PTSD against a control '
        'group, and calls it "an open question" whether supplements can match the diet, though it adds that the diet "may '
        'exert more sustained effects". You were right to put the rats in. I\'d left them out as adding nothing to the '
        'mouse finding, when they\'re closer evidence than it, BHB itself in a trauma model. I couldn\'t read the Reddit '
        'thread (blocked from here), so your forum point stays as you wrote it.'
        % (T.ENGELHARDT, T.YAMANASHI, T.JUNG, T.YOSHIOKA),
    stays='Your forum point and its link, the rest of the sentence and of the paragraph, as your version has them.',
    deciding='Whether the rats and the salts against the diet say what the review you cite says.',
    advice='Approve. I\'m sure of what the rats were given and of what the review says. Two fresh readers stumble on the '
           'sentence\'s two "although"s; if you\'d like it split at your first one, with nothing else changed: "%s" One of them would '
           'also cut the forum and rat clauses as not about PTSD in people, which I wouldn\'t: they\'re your points, and '
           'the rats are the closest animal evidence for BHB itself.' % SPLIT,
    ask='his own: two phrases of the clause you wrote change to what the review you cite says')

SPEC = dict(
    pays=['they learn what the protocol\'s ketones do in the brain that a mood drug doesn\'t, and that the learning '
          'result comes from mice',
          'they learn that people with PTSD on a keto diet with BHB supplements have improved, and by how much',
          'they learn that PTSD treatment hadn\'t helped has nearly or fully gone on the diet in two people',
          'they learn how far the evidence in people goes, what forum reports and rat studies add, and that whether the '
          'salts match the diet is still open'],
    follows=['it says what "the underpinnings" are and how the protocol gets at them',
             'it turns from the mouse finding to people with PTSD',
             'it adds two longer cases to the four-week study',
             'it ends on the limit of the evidence in people and what else there is'],
    links=['The ketone BHB', 'In people with PTSD', 'on the diet', 'No controlled trial of the diet'],
    checked=[('the ketone BHB blocks HDACs; in mice an HDAC blocker made extinction learning last',
              'as on SC-48 (Shimazu et al. 2013; Whittle and Singewald 2014)',
              'yes: they learn why the protocol uses ketones for PTSD rather than for mood', 'kept'),
             ('what has been seen in people with PTSD on a keto diet',
              'as on SC-48b (Edwards et al. 2024; Bellamy and Laurent 2025; Laurent 2026; Youssef et al. 2022)',
              'yes: they learn what has been seen and how far it goes', 'kept'),
             ('astounding BHB salt reviews on forums, like for brain injury repair',
              'his link to a Reddit thread, blocked to this session\'s tools as content, so not read; his point, as '
              'firsthand reports', 'yes: they learn people report striking results from the salts, as reports', 'kept'),
             ('the salts work for rats with trauma',
              'BHB by injection under the skin (Yamanashi et al. 2020, full text) or twice a day by injection (Jung et al. '
              '2025), MCT oil by mouth (Yoshioka et al. 2026); none had the salts by mouth',
              'yes: they learn BHB itself eased trauma-like anxiety in rats, given by injection', 'changed'),
             ('not nearly as proven for humans as the keto diet is',
              'the review he cites: no efficacy for PTSD in people shown against a control group, and whether supplements '
              'can match the diet is an open question (Engelhardt et al. 2026)',
              'yes: they learn the salts\' place beside the diet in people is not settled yet', 'changed')])
NEEDED_KEPT = {
    BENGAY: 'they get the author\'s own picture of a mood drug used on a broken structure, his words, which only he can cut',
    MOUSE: 'they learn why blocking HDACs matters for PTSD: it made the learning that a cue is now safe last, shown so far '
           'in mice with another HDAC blocker',
    FORUM: 'they learn that people report striking results from the salts themselves, as firsthand reports, the author\'s '
           'own point and link',
    RATS: 'they learn that BHB itself eased trauma-like anxiety and fear in rats, the closest animal evidence for the ketone '
          'this protocol uses, the author\'s own point'}


def receipt(b):
    text = T.plain(NEW_MD)
    where = sr.where(BL, b).rsplit(',', 1)[0]
    r = S.make(text, where, READER, his_text=HIS, whose=WHOSE)
    mine = [x for x in r['sentences'] if not x.get('his')]
    assert len(mine) == len(SPEC['pays']), len(mine)
    for x, p, f, k in zip(mine, SPEC['pays'], SPEC['follows'], SPEC['links']):
        x['payoff'] = p
        x['follows'] = f
        assert k in x['s'], (k, x['s'][:40])
        x['link'] = k
    sents = S.sentences(text)
    r['opens'] = {'first_sentence': sents[0],
                  'why_reading': 'they learn the paragraph answers why the drugs they tried haven\'t fixed their PTSD'}
    r['checked'] = [{'point': a, 'found': f, 'still_needed': s, 'fate': fate} for a, f, s, fate in SPEC['checked']]
    r['needed'] = {'reader': 'a fresh reader (Haiku) given tools/humanization/needed_read_brief.md and only this paragraph '
                             '(needed/sp48c/READ.md)', 'unneeded': [BENGAY, MOUSE, FORUM, RATS], 'kept': dict(NEEDED_KEPT)}
    s4, s5, s6 = sents[3], sents[4], sents[5]
    r['his_fixes'] = {
        'reader': 'a fresh reader (Haiku) given tools/humanization/his_fixes_brief.md and the paragraph, one sentence a '
                  'line (his-fixes/sp48c/READ.md)',
        'marked': [{'s': s4, 'difference': '4'}, {'s': s5, 'difference': '1'}, {'s': s6, 'difference': '1'},
                   {'s': S8_NEW, 'difference': '1 and 2'}],
        'kept': {s4: 'his own sentence, from his answer on SC-48; only he changes it',
                 s5: 'in his version twice (SC-48, SC-48b); the humanizing pass takes it up with its Pangram check',
                 s6: 'in his version (SC-48b); the humanizing pass takes it up with its Pangram check',
                 S8_NEW: 'his clause and his shape after "(Youssef, et al, 2022)"; the card changes only what the review '
                         'he cites says differently, and offers him the split at his first "although"'}}
    (c,) = [x['i'] for x in BL if x['text'].startswith('If your cortisol is normal or low')]
    r['same_point'] = ('none: read section C from its heading to the next for what ketosis has done in people and rats with '
                       'PTSD; it appears once. Block %d gives three adults whose depression and anxiety went on a keto '
                       'diet (Calabrese 2024), another condition, and stays where it is' % c)
    r['placement'] = ('where the block is now (block %d), after the reasons the drugs fall short; the evidence ends it, '
                      'after the mouse finding it answers for people and rats' % b)
    r['questions'] = dict(Q_ANS)
    probs = S.check(text, r)
    (HERE / ('%s.receipt.json' % KEY)).write_text(json.dumps(r, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    return probs


def main():
    (b,) = [x['i'] for x in BL if x['text'].startswith(T.START)]
    edit = {'block': b, 'before': sr.block_text(BL, b), 'after': T.plain(NEW_MD)}
    (HERE / ('%s.md' % KEY)).write_text(NEW_MD + '\n', encoding='utf-8')
    (HERE / ('%s.txt' % KEY)).write_text(T.plain(NEW_MD) + '\n', encoding='utf-8')
    bad = ['%s: %s' % (KEY, x) for x in receipt(b)]
    c = CARD
    card = {'id': c['id'], 'type': 'science', 'title': c['title'], 'advice': 'approve',
            'spans': [{'block': b, 'start': 0, 'end': len(edit['before'])}], 'edits': [edit],
            'what': c['what'], 'why': c['why'], 'stays': c['stays'], 'deciding': c['deciding'],
            'advice_note': c['advice'], 'ask_because': c['ask'], 'approve_label': 'use it',
            'found_by': 'His version of SC-48b (answers exported 2026-11-12 18:23 UTC), checked against the review it cites',
            'receipt': [REL + '%s.receipt.json' % KEY]}
    review = {
        'format': 'joel-suggestion-review-v1',
        'review_id': 'neuro-de-armoring-cards-20261112-x1112a',
        'title': 'Neuro De-Armoring Cards, 12 November: the rats and the salts in your clause',
        'intro': ['Your version of the ketone card is in the article. Checked against the review you cite, two points in '
                  'your clause read differently there; this card puts the review\'s wording to you.',
                  'One card. No compound, dose, unit or timing changes.',
                  'Strategy A\'s promise and the other ketone steps go to the read of the whole protocol.'],
        'git_file': REL + 'REVIEW-X1112A.html',
        'article': {'file': LANE + 'HUMANIZED-SO-FAR.md', 'sha256': hashlib.sha256(MD.encode('utf-8')).hexdigest()},
        'built': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
        'links': {'guide': BLOB + LANE + 'HUMANIZED-SO-FAR.md', 'review': BLOB + REL + 'REVIEW-X1112A.md'},
        'types': {'science': {'label': 'A claim corrected',
                              'about': 'Something the sources don\'t support, changed as little as the science allows.'}},
        'suggestions': [card],
    }
    bad += ['PROBLEM ' + x for x in sr.check(review, BL)]
    (HERE / 'REVIEW-X1112A.json').write_text(json.dumps(review, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    for x in bad:
        print(x)
    if bad:
        return 1
    page = sr.page(review, MD, BL)
    (HERE / 'REVIEW-X1112A.html').write_text(page, encoding='utf-8')
    (HERE / 'REVIEW-X1112A.artifact.html').write_text(sr.artifact_view(page), encoding='utf-8')
    out = ['# %s' % review['title'], ''] + [p + '\n' for p in review['intro']]
    out += ['## %s: %s' % (card['id'], card['title']), '', '*%s*' % sr.where(BL, b), '', '**Now:**', '',
            '> %s' % edit['before'], '', '**As it would read:**', '', '> %s' % edit['after'], '',
            '**What changes:** %s' % card['what'], '', '**Why:** %s' % card['why'], '',
            '**What stays:** %s' % card['stays'], '', '**You\'re deciding:** %s' % card['deciding'], '',
            '**My advice:** %s' % card['advice_note'], '']
    (HERE / 'REVIEW-X1112A.md').write_text('\n'.join(out) + '\n', encoding='utf-8')
    print('ok', card['id'], 'block', b)
    return 0


if __name__ == '__main__':
    sys.exit(main())
