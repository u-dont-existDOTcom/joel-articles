#!/usr/bin/env python3
"""His answers on the Medium page (2026-11-22 22:24 UTC, review/teach-20261108/ANSWERS-T4.json) as a layer over the
fixed version: HIS-T4.json, which whole/build.py applies after the checks' replacements.

Each revised card's version replaces the paragraph the card showed (its "before", found in the fixed version as it was:
the live words, or a check's new paragraph). Three of his versions run across more than one paragraph: he rewrote
"Reverting to babyhood" whole (M-206: "just cut and replace the whole section with above"), the first part of
"Disconnect to connect" (M-219: "i fixed that whole part rather than just these 2 sentences"), and "Romance Shouldn't
Be Adjudicated" whole (M-285, with M-286 and M-287 empty: "i redid the whole section"); and M-76 takes M-77 in
("remove p2 i merged it in"). Each run's heading stays the live one (his versions start with the same heading).
Rejected cards (M-264, M-338, M-405: "pangram bug") change nothing.

Only obvious slips are fixed in his words (his standing word: "no need to ask me for obvious corrections"), each listed
in SLIPS with the reason; links he asked for, and the live links whose words are still there, are kept in LINKS.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
ROMANCE = HERE.parents[2]
ANS = json.loads((ROMANCE / 'review' / 'teach-20261108' / 'ANSWERS-T4.json').read_text(encoding='utf-8'))
REPL = {int(k): v for k, v in json.loads((HERE.parent / 'whole' / 'REPLACEMENTS-CHECKS.json').read_text(encoding='utf-8')).items()}
LIVE = {}
for line in (HERE.parent / 'live-check' / 'LIVE-POST-BLOCKS-20261122.jsonl').read_text(encoding='utf-8').splitlines():
    r = json.loads(line)
    if r.get('n') is not None:
        LIVE[r['n']] = r

# Obvious slips in his versions: (card, wrong, right, why). Each "wrong" must occur exactly once in his version.
SLIPS = [
    ('M-108', 'flight or flight mode', 'fight or flight mode', 'typo ("fight or flight", as the paragraph had it)'),
    ('M-126', 'dow did you', 'how did you', 'typo'),
    ('M-206', 'but I don’t want to hold onto the actual reality', 'but I want to hold onto the actual reality',
     'a "don’t" that turns the sentence round: the live paragraph said "I don’t want to leave the reality of me being me"'),
    ('M-285', 'to life me up', 'to lift me up', 'typo'),
    ('M-327', 'Anyway, If we', 'Anyway, if we', 'capital after the comma, left from "Anyway. If" (unlike Two Pillars’ locked "If")'),
    ('M-349', 'the depth of your connection will deepen', 'your connection will deepen',
     '"depth" and "deepen" doing one job twice (the kind of doubling of "the example couple ... as an example")'),
    ('M-349', 'but just completely nor directly nor unilaterally', 'but just not completely, directly or unilaterally',
     'a missing "not"'),
    ('M-361', 'jealousy wan\'t about', 'jealousy wasn\'t about', 'typo'),
    ('M-361', 'in there and then', 'then and there', 'the phrase "then and there"'),
]

# Obvious typos in the live post's own words, outside his answers (the non-word and punctuation scan of FIXED.md,
# 2026-11-22): (wrong, right, why). Each "wrong" is in one live paragraph, once, which no check or answer changed.
LIVE_TYPOS = [
    ('he briefly explained:: “Sex', 'he briefly explained: “Sex', 'a doubled colon'),
    ('By the the 17th century', 'By the 17th century', 'a doubled "the"'),
]

# Paragraph runs his versions replace whole: card -> (live paragraphs, the heading his text starts with)
RUNS = {
    'M-206': ([203, 204, 205, 206, 207], 'Reverting to babyhood'),
    'M-219': ([218, 219, 220], 'Disconnect to connect'),
    'M-285': ([282, 283, 284, 285, 286, 287, 288, 289, 290], 'Romance Shouldn’t Be Adjudicated'),
    'M-76': ([76, 77], None),
}
FOLDED = {'M-77': 'M-76', 'M-286': 'M-285', 'M-287': 'M-285'}

# Links in his new words: (card, anchor words, href, why)
LINKS = [
    ('M-223', 'And |breathwork', 'https://breathwork.u-dont-exist.com/',
     'he asked: "link breathwork to breathwork.u-dont-exist.com" (the live paragraph links its "Breathwork" there)'),
    ('M-223', 'Systema breathing', 'https://www.youtube.com/shorts/Nar2-nvomAk',
     'his standing rule: every mention of Systema breathing links the video he picked (2026-11-20)'),
    ('M-223', 'Somatic Modalities guide', 'https://ibogaqueen.substack.com/p/somatic-modalities-strategic-sequencing',
     'the live paragraph’s link, its words kept'),
    ('M-219', 'peer counseling', 'https://ibogaqueen.substack.com/p/hearthwork-an-integrated-peer-counseling',
     'the live paragraph’s link (220), its words kept'),
]
# Embeds he asked for: (card, where, what)
EMBEDS = [
    ('M-149', 'after the paragraph', 'https://www.instagram.com/reel/Dfd1gZGN3cZ',
     'he asked: "and right here you can put this url in" (live on Instagram 2026-11-22, light_of_my_soul_22)'),
]


def paras(text):
    return [p.strip() for p in re.split(r'\n\s*\n', text) if p.strip()]


def main():
    items = {i['id']: i for i in ANS['items']}
    slips_done = []
    out = []
    for i in ANS['items']:
        cid, st = i['id'], i['status']
        if st != 'revise' or cid in FOLDED:
            continue
        v = i['your_version']
        for c, wrong, right, why in SLIPS:
            if c == cid:
                assert v.count(wrong) == 1, (cid, wrong)
                v = v.replace(wrong, right)
                slips_done.append({'card': cid, 'was': wrong, 'now': right, 'why': why})
        live_n = int(cid[2:])
        links = re.findall(r'https://www\.pangram\.com/history/[0-9a-f-]{36}', i['comment'])
        rec = {'card': cid, 'comment': i['comment'], 'his_checks': links}
        if cid in RUNS:
            run, head = RUNS[cid]
            ps = paras(v)
            if head:
                first = ps[0].split('\n', 1)
                assert first[0].strip() == head, (cid, first[0])
                ps = ([first[1].strip()] if len(first) > 1 and first[1].strip() else []) + ps[1:]
            rec.update({'kind': 'run', 'live': run, 'after': ps,
                        'before_live': [LIVE[n]['text'] for n in run]})
        else:
            before = i['before']
            cur = REPL.get(live_n)
            where = 'live' if cur is None else 'check'
            if cur is None:
                assert re.sub(r'\s+', ' ', LIVE[live_n]['text']).strip() == re.sub(r'\s+', ' ', before).strip(), cid
            else:
                assert before in cur, (cid, 'before not in the fixed version')
            rec.update({'kind': 'para', 'live': live_n, 'before': before, 'from': where, 'after': paras(v)})
        out.append(rec)
    assert len(slips_done) == len(SLIPS), (len(slips_done), len(SLIPS))
    for wrong, right, why in LIVE_TYPOS:
        hits = [n for n, r in LIVE.items() if wrong in r['text']]
        assert len(hits) == 1 and LIVE[hits[0]]['text'].count(wrong) == 1 and hits[0] not in REPL, (wrong, hits)
        n = hits[0]
        out.append({'card': 'typo', 'kind': 'para', 'live': n, 'before': LIVE[n]['text'], 'from': 'live',
                    'after': [LIVE[n]['text'].replace(wrong, right)], 'comment': why, 'his_checks': []})
        slips_done.append({'card': 'live %d' % n, 'was': wrong, 'now': right, 'why': why})
    for c, words, href, why in LINKS:
        r = next(x for x in out if x['card'] == c)
        assert sum(p.count(words.replace('|', '')) for p in r['after']) == 1, (c, words)
    data = {'about': __doc__.strip().split('\n\n')[0], 'answers': 'review/teach-20261108/ANSWERS-T4.json',
            'slips': slips_done, 'links': [dict(zip(('card', 'words', 'href', 'why'), l)) for l in LINKS],
            'embeds': [dict(zip(('card', 'where', 'url', 'why'), e)) for e in EMBEDS],
            'folded': FOLDED, 'rejected': [i['id'] for i in ANS['items'] if i['status'] == 'rejected'],
            'changes': out}
    (HERE / 'HIS-T4.json').write_text(json.dumps(data, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print('changes', len(out), '| runs', sum(1 for x in out if x['kind'] == 'run'), '| slips', len(slips_done),
          '| rejected', data['rejected'])


if __name__ == '__main__':
    main()
