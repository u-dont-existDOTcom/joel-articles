"""The side-by-side pages of 2026-10-14: each changed section beside the published one.

New map versions (in-context/icNN-vM.json) from the last ones: the same rows and source starts, the
article starts that changed today fixed, the notes of earlier turns dropped (they answered questions
that are closed now), today's notes on the rows that changed, and the open questions (22 to 26 on the
questions page) as proposal rows under the paragraphs they'd change. Highlights are against main at
0353ed22, the version Joel last saw (his 10-13 texts, merged at the start of this turn).

Run from the candidate folder: python3 fix-20261014/make_pages.py
"""
import json, pathlib, subprocess, sys

CAND = pathlib.Path(__file__).resolve().parent.parent
REPO = CAND.parents[2]
sys.path.insert(0, str(REPO / 'tools' / 'humanization'))
import render_in_context as R  # noqa: E402

SINCE = '0353ed22'
CUR = R.paragraphs((CAND / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8'))
DROP = (' · changed this turn', ' · changed for your answer', ' (PROPOSAL)', ', a proposal')
FIRST = ('Your published section is on the left. On the right is the version now in the article so far. '
         'Highlighted words are new since the version you last saw (your texts of 10-13, merged this morning), '
         'and struck words are ones that went.')
NOT_YET = 'Not checked in Pangram yet: I\'ll check it once you pick.'


def para(start):
    """The plain text of the article paragraph that starts with START (links as their text)."""
    return R.plain(R.find(CUR, start, start))[0]


DRAFTS = json.loads((CAND / 'fix-20261014' / 'drafts.json').read_text(encoding='utf-8'))


def draft(key):
    v = DRAFTS[key]
    return v['text'] if isinstance(v, dict) else v


def swap(start, old, new):
    text = para(start)
    assert text.count(old) == 1, (start, old)
    return text.replace(old, new)


def build(name, old, meta, intro, fixes=None, changed=None, proposals=None, drop_blocks=(), keep=None, splits=None):
    fixes, changed, proposals, splits = fixes or {}, changed or {}, proposals or [], splits or {}
    m = json.loads((CAND / 'in-context' / old).read_text(encoding='utf-8'))
    out = {'title': m['title'], 'meta': meta, 'intro': intro, 'blocks': []}
    used = set()
    for bi, blk in enumerate(m['blocks']):
        if bi in drop_blocks:
            continue
        rows = []
        for r in blk['rows']:
            r2 = {k: v for k, v in r.items() if k not in ('notes', 'note', 'flag', 'repeats')}
            lab = r2.get('label', '')
            for d in DROP:
                lab = lab.replace(d, '')
            r2['label'] = lab
            if 'article' in r2:
                r2['article'] = fixes.get(r2['article'], r2['article'])
                if keep is not None and not any(r2['article'].startswith(k) for k in keep):
                    continue
                for k, (suffix, notes) in changed.items():
                    if r2['article'].startswith(k):
                        r2['label'] = (lab + ' · ' + suffix) if lab else suffix
                        r2['notes'] = notes
                        used.add(k)
            rows.append(r2)
            for p in proposals:
                if 'article' in r2 and r2['article'].startswith(p['after']):
                    rows.append({'label': p['label'], 'text': p['text'], 'proposal_of': r2['article'],
                                 'source': r2.get('source', []), 'notes': p['notes']})
                    used.add('P:' + p['label'])
        split = splits.get(bi)
        if split:
            # a block whose rows sit under two headings in the article (section 6's subheading)
            at = next(i for i, r in enumerate(rows) if r.get('article', '').startswith(split[0]))
            out['blocks'].append({'headings': blk.get('headings', []), 'rows': rows[:at]})
            out['blocks'].append({'headings': [split[1]], 'rows': rows[at:]})
        else:
            out['blocks'].append({'headings': blk.get('headings', []), 'rows': rows})
    missing = [k for k in changed if k not in used] + [p['label'] for p in proposals if 'P:' + p['label'] not in used]
    assert not missing, (name, missing)
    path = CAND / 'in-context' / name
    path.write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    return path


PAGES = []

# Section 2
PAGES.append((build('ic02-v4.json', 'ic02-v3.json',
    'Community article · section 2 · v3.2, 2026-10-14 · in the article so far as a candidate',
    [FIRST,
     'What changed: your F4 sentence and your F6 clause, from your Rule Scoring Sheet answers of 03:04 UTC, as you wrote them. Nothing else.',
     'Pangram\'s web app: each of the two paragraphs reads Human alone (58 words each, 05:11 UTC, batch 275g), and the whole section 100% Human (627 words, 05:11:23 UTC), on the first try.'],
    changed={
        'Communal ownership entails folks': ('changed today', [
            'Your F4 answer, as you wrote it: "No, taking away the idea of a boss does not make everyone less passive, selfish, thieving, nor suddenly unlearning learned helplessness."',
            'Pangram: Human alone (58 words, 05:11:02 UTC, 275g).']),
        'People want to go back to the old way': ('changed today', [
            'Your F6 answer, as you wrote it: "... a baby is born or jealousy rears its head."',
            'Pangram: Human alone (58 words, 05:11:12 UTC, 275g).'])}),
    'community-section2-side-by-side.html'))

# Section 3
PAGES.append((build('ic03-v4.json', 'ic03-v3.json',
    'Community article · section 3 · v12, 2026-10-14 · in the article so far as a candidate',
    [FIRST,
     'What changed: two sentences, for flags that two or more cold reads raised in the sweep of 10-13 (a reader with no other context, asked where they got lost).',
     'Pangram\'s web app: both paragraphs read Human alone, and the section 100% Human (558 words, 05:30:36 UTC, batch 276g), on the first try.'],
    fixes={'The deeper problem is that someone carries': 'The deeper problem is that somebody'},
    changed={
        'Meeting procedure isn’t going to solve': ('changed today', [
            'Three cold reads lost track of the five "it"s, and none could say what "whoever raises it has to find somebody who agrees with him or her before they get to talk about it" was. The published version names it: whether the motion requires a second. Now: "It can only decide whose turn it is to talk about the hatred, and whether a motion about it needs somebody to second it."',
            'Pangram: Human alone (77 words, 05:30:14 UTC, 276g).']),
        'The deeper problem is that somebody': ('changed today', [
            'Five cold reads asked what "the others" were. The published version: "authority earned in one role can be spent in every other role". Now: "somebody who\'s earned authority in one role can use it in all their other roles", and "a gifted teacher" is back from the published (a meaning trace read "good" as weaker).',
            'Pangram: Human alone (83 words, 05:30:24 UTC, 276g).'])}),
    'community-section3-side-by-side.html'))

# Section 4
PAGES.append((build('ic04-v6.json', 'ic04-v5.json',
    'Community article · section 4 · v11.1, 2026-10-14 · your final section, in the article so far as a candidate',
    [FIRST,
     'What changed: three words, for your I1 answer ("Unclear"): "And inner pl/ork is built on somatic regulation first." for "And it\'s built on somatic regulation first."',
     'Pangram\'s web app: the whole section reads 100% Human (1,555 words, 05:31:01 UTC, batch 276g). That paragraph reads AI beside the reparenting paragraph before it, with my words (276g) and in your own (278g, a control at 06:03:58 UTC), so it isn\'t the new words.',
     'Two questions on the questions page are here as proposals, highlighted against the text now in the article: 24 (under "If one of them gets skipped") and 26 (under "Nothing suppressed, everything processed").'],
    fixes={"And it's built on somatic regulation": 'And inner pl/ork is built on'},
    changed={
        'And inner pl/ork is built on': ('changed today', [
            'Your I1 answer: the "it" was unclear. It names the subsection\'s subject now, inner pl/ork. I didn\'t use "reparenting": the stance check found it pulling against section 5\'s "Reparenting, somatic capacity, and peer counseling come first". Say if you meant reparenting.'])},
    proposals=[
        {'after': 'Nothing suppressed, everything processed.', 'label': 'PROPOSAL · question 26 (my pick: yes)',
         'text': swap('Nothing suppressed, everything processed.', 'stay fluid and organic, and don\'t freeze into doctrine.', 'stay fluid and organic.'),
         'notes': ['The repeats check: two paragraphs later, "When agreements get frozen, religious communities tend to call the frozen version doctrine." says it again, with the secular "process" beside it.', NOT_YET]},
        {'after': 'If one of them gets skipped', 'label': 'PROPOSAL · question 24 (my pick)',
         'text': swap('If one of them gets skipped', 'If one of them gets skipped', 'If one of the four gets skipped'),
         'notes': ['Two cold reads asked whether "them" is the first three parts or all four. The land and labor clause after it is about the container, so the four.', NOT_YET]}]),
    'community-section4-side-by-side.html'))

# Section 6
PAGES.append((build('ic06-v4.json', 'ic06-v3.json',
    'Community article · section 6 · v22, 2026-10-14 · in the article so far as a candidate',
    [FIRST,
     'What changed: one paragraph. It explains the technosphere at its first use in the text and says what the independence and the way out are from. Cold reads asked "independence from what?" (two), "an exit from what?" (three) and what the technosphere is (two; your rule of 10-09: explain a name at its first mention).',
     'Pangram\'s web app: the paragraph reads Human alone (69 words, 06:01:07 UTC, batch 277g), and the section 100% Human (687 words, 06:01:18 UTC), on the first try.'],
    changed={
        'Ok, so on a personal level,': ('changed today', [
            'Now: "cultivating more human independence from the technosphere, all the machines and systems modern life runs on," and "a way out of the technosphere" for "an exit" (a meaning trace said "a way out of it" could point at the community).',
            'The gloss says what the sources say: the technosphere is all the technological objects and systems people have made (a concept credited to the geologist Peter Haff and others; Wikipedia, "Anthroposphere").'])},
    splits={0: ('I just read this post from', '## Facing the Polycrisis: Is There Hope For Humanity?')}),
    'community-section6-side-by-side.html'))

# Section 7
PAGES.append((build('ic07-v3.json', 'ic07-v2.json',
    'Community article · section 7 · v4, 2026-10-14 · in the article so far as a candidate',
    [FIRST,
     'What changed: one sentence says what ZEGG and Tamera are at their first mention (two cold reads: the names are never introduced).',
     'Pangram\'s web app: the paragraph reads Human alone (68 words, 05:31:13 UTC, batch 276g), and the section 100% Human (486 words, 05:31:25 UTC), on the first try.'],
    fixes={'ZEGG and Tamera have spent decades': 'ZEGG, a community near Berlin'},
    changed={
        'ZEGG, a community near Berlin': ('changed today', [
            'Now: "ZEGG, a community near Berlin, and Tamera, another in Portugal,". Sources: Wikipedia, "ZEGG (community)" (founded in 1991 in Bad Belzig, about 80 km south-west of Berlin) and "Dieter Duhm" (Tamera, co-founded in south-western Portugal in 1995).'])}),
    'community-section7-side-by-side.html'))

# Section 8
PAGES.append((build('ic08-v3.json', 'ic08-v2.json',
    'Community article · section 8 · v29, 2026-10-14 · in the article so far as a candidate',
    [FIRST,
     'What changed: your F10 answer ("revert to yours") and five fixes for flags that two or more cold reads raised in the sweep of 10-13.',
     'Pangram\'s web app: each changed paragraph reads Human alone (the promo-video paragraph beside the one before it, since it\'s under 50 words), and the section 100% Human (1,841 words, 06:02:37 UTC, batch 277g), all on the first try.',
     'One question on the questions page is here as a proposal: 24, under your paragraph on dangerous children.'],
    fixes={"What's going on at Tamera's": "Tamera's Children's Place has repeated",
           'No upbringing can provide perfect freedom': 'Belonging and freedom should go hand in hand.'},
    changed={
        'What she said is more useful': ('changed today', [
            'Four cold reads took "another promo video" to point back at the video of your son just above; the article shows no promo video before this. Now: "the usual promo video".',
            'Pangram: with the paragraph before it, Human (67 words, 06:01:28 UTC, 277g).']),
        'One of the biggest reasons I think': ('changed today', [
            'Five cold reads asked who the Ye\'kuana are. Now: "the Ye\'kuana, an Indigenous people of the Venezuelan rainforest she lived with,". Sources: Wikipedia, "Jean Liedloff" and "Ye\'kuana" (a rainforest people of Venezuela; The Continuum Concept is based on her time living with them).',
            'Pangram: Human alone (109 words, 06:01:40 UTC, 277g).']),
        'I also reject the suburban panic': ('changed today', [
            'Two cold reads couldn\'t find what "that gift" was, and "Fear like that" skipped back a sentence. Your F2, F5 and F8 answers took out an abstract thing doing what a person does, so people are the subject now: "When adults panic like that, kids can lose all those grownups without the panic actually preventing abuse." (The published: "Fear can destroy that gift".)',
            'Pangram: Human alone (69 words, 06:01:51 UTC, 277g).']),
        'Create a no-secrets rule': ('changed today', [
            'Three cold reads had to reread my "A surprise isn\'t a secret, because at the end of a certain date it has to be told." Now: "A surprise has an end date." (The published: "Surprises have an ending date".)',
            'Pangram: Human alone (56 words, 06:02:03 UTC, 277g).']),
        'Protecting children is the duty': ('changed today', [
            'Your F10 answer, "Fix it (revert to yours)": my sentence from before your 10-07 text is back, with your "what happened": "A scared or confused kid may get mixed up telling what happened and still need protection." If you meant the published sentence, it\'s "A frightened or confused child may tell a story imperfectly and still need protection."',
            'Pangram: Human alone (136 words, 06:02:16 UTC, 277g).']),
        'Make sure kids have relationships': ('changed today', [
            'Five cold reads asked whose kids these were, why they were taken and what the state asked for. Now: "In 1984, Vermont authorities raided a religious community in Island Pond and took 112 kids into custody over suspected abuse. A judge turned down the state\'s blanket request to hold them, because it couldn\'t name any specific case, and the kids went home that same day."',
            'Sources: VTDigger (21 June 2024, the link in the paragraph), Nicole Bazilchuk\'s article on the raid, and The Christian Science Monitor (26 June 1984): the Northeast Kingdom Community Church; 112 children taken into custody amid allegations of child abuse; Judge Frank Mahady, noting the state couldn\'t name individual cases, refused to let it hold them; the children went home that day.',
            'Pangram: Human alone (124 words, 06:02:26 UTC, 277g).'])},
    proposals=[
        {'after': 'Sometimes we also need to protect', 'label': 'PROPOSAL · question 24 (my pick)',
         'text': swap('Sometimes we also need to protect', 'I looked through the research corpus for', 'I looked through all the research I\'d gathered for'),
         'notes': ['Two cold reads asked which corpus. The link would stay on the new words. Your words of 10-07, so it\'s your call.', NOT_YET]}]),
    'community-section8-side-by-side.html'))

# Section 9
PAGES.append((build('ic09-v4.json', 'ic09-v3.json',
    'Community article · section 9 · v15, 2026-10-14 · in the article so far as a candidate',
    [FIRST,
     'What changed: the caracoles explained at their first mention (two cold reads: unexplained), and the closing words of my paragraph on what happened after the Escuelita cut, because your paragraph "Now, the Zapatistas also don\'t prove my whole money-free economy goal" says it in the same section (the repeats check).',
     'Pangram\'s web app: both paragraphs read Human alone, and the section 100% Human (1,037 words, 05:31:59 UTC, batch 276g), on the first try.',
     'One question on the questions page is here as a proposal: 26, under your paragraph "And that\'s not me saying that."'],
    changed={
        'In 2005, a few college buddies': ('changed today', [
            'Now: "one of the Zapatista caracoles ("snails"), the regional centers that tie their villages together in Chiapas". Source: Wikipedia, "Zapatista territories" (from 2003 the autonomous municipalities were coordinated through caracoles, community centers; in November 2023 they were to keep serving locals, closed to outsiders).',
            'Pangram: Human alone (65 words, 05:31:35 UTC, 276g).']),
        'As part of my research': ('changed today', [
            'Cut, as a proposal: ", not claiming they already proved my whole model". The paragraph still says the evidence wasn\'t found. Say if you want it back.',
            'Pangram: Human alone (108 words, 05:31:47 UTC, 276g).'])},
    proposals=[
        {'after': "And that's not me saying that", 'label': 'PROPOSAL · question 26 (my pick: yes)',
         'text': swap("And that's not me saying that", "The useful thing isn't their diagram. It's how they learn:", 'The useful thing is how they learn:'),
         'notes': ['The repeats check: your paragraph just before ends "A new ecovillage can\'t copy the diagram everyone can see", and this one says "The useful thing isn\'t their diagram." right after. With the cut, "It\'s" would have nothing to point to, so: "The useful thing is how they learn".', NOT_YET]}]),
    'community-section9-side-by-side.html'))

# Section 10: unchanged; the page is for question 25
P9_10 = 'When you create or apply a rule'
PAGES.append((build('ic10-v3.json', 'ic10-v2.json',
    'Community article · section 10 · v2, unchanged, 2026-10-14 · for question 25',
    [FIRST,
     'Nothing changed in this section. The sweep of 10-13 flagged the opening of its last paragraph, "a collision of two principles" (four cold reads: none named, abrupt; the published opens "And when two principles collide", after the solidarity limits).',
     'The two openings I tried are below. Each read AI alone in Pangram (276g at 05:32:11 UTC, 279g at 06:10:09 UTC), so the paragraph stays as it is; it passes alone and in the section. This opening failed in most wordings on 10-10 too. Question 25 on the questions page.'],
    proposals=[
        {'after': P9_10, 'label': 'TRIED, read AI alone (276g) · not proposed',
         'text': draft('E-S10P9f'),
         'notes': ['Names the pair from the paragraph before. Pangram: AI-Generated, the whole paragraph (103 words, 05:32:11 UTC, 276g).']},
        {'after': P9_10, 'label': 'TRIED, read AI alone (279g) · not proposed',
         'text': draft('E-S10P9fA'),
         'notes': ['The pair named inside the opening. Pangram: AI-Generated, the whole paragraph (99 words, 06:10:09 UTC, 279g).']}]),
    'community-section10-side-by-side.html'))

# Section 11
P2_11 = 'That person ends up with real influence'
PAGES.append((build('ic11-v5.json', 'ic11-v4.json',
    'Community article · section 11 · v14, 2026-10-14 · in the article so far as a candidate',
    [FIRST,
     'What changed: P9\'s "no real way ... no matter how many meetings it holds" (seven cold reads: circles are never set up in this section) and P10\'s "the daily signs of founderism" (two: signs of what?). Each reads Human alone, and the section 100% Human (1,690 words, 06:21:26 UTC, batch 282g), on the fourth section try.',
     'The other fixes are questions 22 and 23 on the questions page, shown as proposals under the paragraphs they\'d change: the definition of founderism (P2), P4\'s prediction question and its repeated "Can it replace the founder?", P6\'s lead-in to the four questions, and P8\'s reviewers. P2, P4 and P6 each pass alone, but with any of them in, Pangram puts an AI window on P4\'s run of questions in the section (277g, 280g, 281g, 282g).',
     'Question 26 (a repeat in your words) is under your paragraph "Peer counseling can become peer surveillance".'],
    fixes={'Also watch for the daily signs.': 'Also watch for the daily signs of founderism.'},
    changed={
        "Remember, it's not an override unless": ('changed today', [
            'Now: "then there\'s no real way for the community to override the founder, no matter how many meetings it holds."',
            'Pangram: Human alone (59 words, 06:03:23 UTC, 277g).']),
        'Also watch for the daily signs of founderism.': ('changed today', [
            'Pangram: Human alone (52 words, 06:03:34 UTC, 277g).'])},
    proposals=[
        {'after': P2_11, 'label': 'PROPOSAL · question 22a (my pick)',
         'text': para(P2_11) + ' When that influence goes unchecked, I call it founderism.',
         'notes': ['Six cold reads said the heading\'s word is never explained. This fits your own "founderism is a problem in every community" further down, and the four questions test exactly that.',
                   'Pangram: Human beside P3 (87 words, 06:10:41 UTC, 279g). With P1 it read AI (277g), and so do P1 and P2 as they are now (279g, a control). In the section it moves an AI window onto P4\'s questions (281g).']},
        {'after': P2_11, 'label': 'PROPOSAL · question 22b',
         'text': para(P2_11) + ' That influence is what I mean by founderism.',
         'notes': ['The influence itself, unchecked or not.', NOT_YET]},
        {'after': 'A few things help keep that in check', 'label': 'PROPOSAL · question 23, P4, wording 1',
         'text': draft('E-S11P4f'),
         'notes': ['Eleven cold reads asked whose prediction. This names it, and drops "Can it replace the founder?", which the four questions ask again three paragraphs down (the repeats check).',
                   'Pangram: Human alone (147 words, 06:02:59 UTC, 277g); in the section, an AI window on these questions (06:03:47 UTC).']},
        {'after': 'A few things help keep that in check', 'label': 'PROPOSAL · question 23, P4, wording 2',
         'text': draft('E-S11P4f-V2'),
         'notes': ['Pangram: Human alone (140 words, 06:18:37 UTC, 280g); in the section, the same AI window (06:18:50 UTC). With P4 and P6 as they are now and P2\'s definition in, the window is there too (281g); so the run of questions itself is what Pangram reads. My pick: your own wording of P4\'s questions; if you\'d rather not, P2, P4 and P6 stay as they are, and the section reads 100% Human that way.']},
        {'after': 'Here are the four questions about the founder', 'label': 'PROPOSAL · question 23, P6',
         'text': 'The questions so far have been about the method. These four are about the founder:',
         'notes': ['Three cold reads couldn\'t tell these four from P4\'s questions.',
                   'Pangram: Human beside P5 and the four questions (93 words, 06:11:06 UTC, 279g); in the section with P4\'s fix, the AI window on P4 again (06:21:36 UTC, 282g).']},
        {'after': 'Then follow the practical power.', 'label': 'PROPOSAL · question 23, P8 (my pick)',
         'text': swap('Then follow the practical power.', 'who picks the reviewers?', 'who picks the people who review the founder?'),
         'notes': ['Nine cold reads asked: reviewers of whom? These are the next paragraph\'s own words. A meaning trace read this wording, and "the people who handle complaints", as narrower than the published "chooses reviewers", so it isn\'t in.', NOT_YET]},
        {'after': 'Peer counseling can become peer surveillance', 'label': 'PROPOSAL · question 26 (my pick: yes)',
         'text': swap('Peer counseling can become peer surveillance', ' There are pros and cons to each extreme, and again, a living balance must be struck.', ''),
         'notes': ['The repeats check: "a dynamic, living, always re-assessed balance" before it and "But again, balance" after it say it too; the third gives its own reason.', NOT_YET]}],
    drop_blocks=(2,)),
    'community-section11-side-by-side.html'))

# Section 12
PAGES.append((build('ic12-v5.json', 'ic12-v4.json',
    'Community article · section 12 · v13, 2026-10-14 · your rewrite, in the article so far as a candidate',
    [FIRST,
     'What changed: your P2 and P3 from your W1 answer ("i prefer this version"), as you wrote them.',
     'Pangram\'s web app: each reads Human alone and as a pair, and the section 100% Human (950 words, 04:30:41 UTC, batch 274g), on the first try.',
     'Question 26 (two repeats in your words) is on P3\'s row; my pick for both is to keep them.'],
    fixes={'This does not surprise me': "This doesn't surprise me",
           'So the question isn’t whether': 'So then a lot of people'},
    changed={
        "This doesn't surprise me": ('changed today', [
            'Your W1 P2, as you wrote it.',
            'Pangram: Human alone (62 words, 04:30:09 UTC, 274g); with P3, Human (155 words, 04:30:30 UTC).']),
        'So then a lot of people': ('changed today', [
            'Your W1 P3, as you wrote it (the ")" after it closed your note).',
            'Pangram: Human alone (93 words, 04:30:19 UTC, 274g).',
            'Question 26: "it\'s more about what fits where & when than good or bad" here and the list\'s "This doesn\'t mean you\'re bad or doomed, it\'s about timing" further down. My pick: keep both; the first is about labels, the second reassures the reader right when the list says they may not fit. And "free resource/capacity" comes four paragraphs before "free resource" is defined, as it did before; my pick is to leave it.'])}),
    'community-section12-side-by-side.html'))

if __name__ == '__main__':
    for mp, out in PAGES:
        r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'render_in_context.py'), str(mp),
                            str(CAND / out), '--article', str(CAND / 'HUMANIZED-SO-FAR.md'),
                            '--source', str(CAND.parent / 'original.md'), '--since', SINCE],
                           capture_output=True, text=True)
        print(mp.name, '->', out, 'exit', r.returncode)
        print('  ' + (r.stdout + r.stderr).strip().replace('\n', '\n  '))
