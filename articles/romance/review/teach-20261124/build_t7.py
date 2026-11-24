#!/usr/bin/env python3
"""The seventh marking page (2026-11-24): the whole fixed article (whole/FIXED.md) with the Medium pass's fixes that
change his versions from the fourth page, or a line he kept there, each tested in its section (r37/CARDS-T7.json,
r37/medium/), and the two sections still below High as questions. His message of 2026-11-23 23:49 UTC: "actually i don't
like the medium windows ... i often find the medium windows indicate other issues also" (lesson romance-2026-11-23i). The
fixes of model text went in without a card (r37/MINE-R37.json).

  python3 build_t7.py   ->  REVIEW-T7.json, REVIEW-T7.html, REVIEW-T7.artifact.html, REVIEW-T7.md
"""
import hashlib
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import suggestion_review as R  # noqa: E402

FIX = 'articles/romance/humanize/fix-20261107'
ART = FIX + '/whole/FIXED.md'
md = (ROOT / ART).read_text(encoding='utf-8')
sha = hashlib.sha256(md.encode('utf-8')).hexdigest()
bl = R.blocks(md, whole=True)
CHANGES = json.loads((ROOT / FIX / 'r37' / 'CARDS-T7.json').read_text(encoding='utf-8'))
RECEIPTS = json.loads((ROOT / FIX / 'r37' / 'medium' / 'para' / 'INDEX.json').read_text(encoding='utf-8'))
H = 'https://www.pangram.com/history/'


def find_block(text):
    hits = [b['i'] for b in bl if b['kind'] not in ('embed', 'cut') and b['text'] == text]
    assert len(hits) == 1, (text[:60], hits)
    return hits[0]


def find_words(words):
    hits = [(b['i'], b['text'].find(words)) for b in bl if b['kind'] not in ('embed', 'cut') and words in b['text']]
    assert len(hits) == 1, (words[:60], hits)
    i, s = hits[0]
    return {'block': i, 'start': s, 'end': s + len(words)}


def span(i, words):
    t = bl[i]['text']
    s = t.find(words)
    assert s >= 0 and t.find(words, s + 1) < 0, (i, words)
    return {'block': i, 'start': s, 'end': s + len(words)}


FOUND = ('the Medium pass of 2026-11-24 (r37/medium/): the sentences in each Medium window, and the ones beside them '
         'that read the same way, changed the ways your fix of "Talk about making love" did, then the section checked by itself')
CARDS = {
    'M-07': dict(
        title='“Then what? You block her?”',
        highlight=['she’s gonna call you. Then what? You block her? Agree to child support?'],
        what='“Then what?” carries on from the sentence before (“she’s gonna call you, and then what?”), and the next two '
             'questions become one, joined with “or”.',
        why='The section’s one Medium window was these five words, “Then what? You block her?”: two short questions '
            'standing alone. Run on into the sentence they answer, the whole section read Human High.',
        stays='Every question and its order, and the rest of the paragraph word for word.',
        deciding='whether the questions can run together like this',
        ask_because='downside: it changes your version from the fourth page (M-28), which read High in your own check; '
                    'my brief on your fixes also counts “Then what? You block her?” as a question in a '
                    'story, which it doesn’t count as a short line',
        reading='The section before this pass: Human, one Medium window on “Then what? You block her?” '
                '(%sb95881ab-afe0-4a76-adc1-d3cf789b1391).' % H,
        tested='The section with this change: Human High in every window (%sd29e7a30-b543-45c9-a1af-c0eeeb7b3caf).' % H),
    'M-16': dict(
        title='Sex appeal “isn’t the basis anymore”',
        highlight=['sex appeal stops being the basis of the relationship'],
        what='“sex appeal stops being the basis of the relationship” becomes “sex appeal isn’t the basis of the '
             'relationship anymore”.',
        why='The section read Medium on “Nobody is owed that as proof of love.” My fix of that line is in the article '
            '(“Or maybe they don’t, and you can’t make giving you that freedom a test of whether they love you”), and '
            'with it this sentence read Medium. With both, the section read Human High.',
        stays='The rest of the paragraph, word for word.',
        deciding='whether “isn’t ... anymore” says what “stops being” said',
        ask_because='downside: it changes your version from the fourth page (M-76); without it, the section as the '
                    'article has it now reads Medium on this sentence',
        reading='The section as the article has it now, my other fix in: Human, one Medium window on this sentence '
                '(%sa5204466-f4d1-4f62-9b73-652a5ce5aef7). Before this pass: Medium on “Nobody is owed that as proof '
                'of love.” (%s1341b0eb-afce-42e0-8631-91b1da228be6).' % (H, H),
        tested='The section with this change: Human High in every window (%s0b928214-0ed5-43e5-b495-f68bfc7028b9).' % H),
    'M-26': dict(
        title='“How well we actually handle our own issues”',
        highlight=['how effective we actually are at handling our own issues'],
        what='“how effective we actually are at handling our own issues” becomes “how well we actually handle our own '
             'issues”.',
        why='This sentence was the section’s one Medium window (20 words). Said plainly, the section read Human High.',
        stays='The two questions after it and the last line, word for word.',
        deciding='whether “how well we handle” says what “how effective we are at handling” said',
        ask_because='downside: it changes your version from the fourth page (M-125)',
        reading='The section before this pass: Human, one Medium window on this sentence '
                '(%sdd319996-2440-46c1-8d80-73e1e132add4).' % H,
        tested='The section with this change: Human High in every window (%s39e78fb6-8b3e-4692-bec6-4cc4f261b23f).' % H),
    'M-28': dict(
        title='“Because if somebody starts with enough trauma”',
        highlight=['when a relationship got ugly. If somebody starts with enough trauma'],
        what='The trauma line joins the sentence before it with “because”: you couldn’t know how either woman would act '
             'when a relationship got ugly, because huge progress can still leave a lot unresolved.',
        why='The section read Medium on the trauma line and the blind-spot line after it, and on the fawning line. My '
            'fixes of the blind-spot and fawning lines are in the article; with them, the trauma line standing alone '
            'still read Medium (14 words). Joined, the section read Human High.',
        stays='“We see what we want to see.” and every word of both sentences.',
        deciding='whether the trauma line is the reason you couldn’t know',
        ask_because='meaning: “because” makes the trauma line the reason you couldn’t tell how either woman would act; '
                    'it changes your version from the fourth page (M-135)',
        reading='The section as the article has it now, my two other fixes in: Human, one Medium window on the trauma '
                'line (%s940ea290-9326-4ac7-9d4e-dfd610d43dea). Before this pass: two Medium windows '
                '(%sc6cf2ba9-446a-407b-996e-d4ed9087ab9e).' % (H, H),
        tested='The section with this change: Human High in every window (%sbd788843-ff5f-417c-9242-5aeee7123f33).' % H),
    'M-31': dict(
        title='Twin flames, and the women you still love',
        highlight=['"We’re twin flames!" "I’m Lord Krishna and she\'s Radha!"',
                   'Sometimes I talk about them... because I’m thinking about them, and I don\'t want to hide it. I’m not '
                   'trying to make my current partner jealous.'],
        what='The two quotes run together with “or”. In the next paragraph, the three lines about talking of past '
             'loves become one sentence: you talk about them, with no intention of making your partner jealous, just '
             'because you’re thinking about them and don’t want to hide it.',
        why='The section read Medium in three short windows: “You know how it goes: "We’re twin flames!"” (9 words), '
            '“Sometimes I talk about them...” (5) and “I’m not trying to make my current partner jealous.” (10). '
            'Joined, the section read Human High.',
        stays='“Okay, maybe I really am way better...”, the test of finding all of me, and “If she can’t handle the '
              'truth that I still love them, she isn’t ready for me.”',
        deciding='whether the one sentence keeps what the three said',
        ask_because='downside: it changes your versions from the fourth page (M-149 and M-150), and the pause after '
                    '“Sometimes I talk about them...” goes',
        reading='The section before this pass: Human, three Medium windows (%sbefa2e14-7078-4cf7-8e5c-a40a61fa2cc2).' % H,
        tested='The section with these changes: Human High in every window (%s8d070089-ca59-4476-a372-f3fbe75cb711).' % H),
    'M-35': dict(
        title='“Much stronger barriers than these”',
        highlight=['much stronger barriers around'],
        what='“than these” goes in: “much stronger barriers than these around a man and woman being alone”, so '
             '“stronger” says what it is stronger than (the phone, video and meeting among other people just named).',
        why='This sentence read Medium before this pass. My fix of the section’s other Medium line is in the article, '
            'and with it the last 52 words read Medium. With “than these”, the section read Human High.',
        stays='Everything else in the paragraph.',
        deciding='whether “than these” points at the right things',
        ask_because='downside: it changes your version from the fourth page (M-171), which read High in your own check',
        reading='The section as the article has it now, my other fix in: Human, its last 52 words Medium '
                '(%s61a92d63-622e-4f94-b441-a6d00ed3e67a). Before this pass: two Medium windows '
                '(%s75e83ed7-2549-476a-9ad4-49000e7fa17a).' % (H, H),
        tested='The section with this change: Human High in every window (%s1867a533-baa4-4926-af33-d26bf54676fb).' % H),
    'M-54': dict(
        title='“But woops, I came too fast”',
        highlight=['but I came too fast. Woops...'],
        what='“Woops” moves into the punchline: “but woops, I came too fast.”',
        why='The one Medium window here was the single word “Woops...”. On the fourth page you kept it and called that '
            'window a Pangram bug (M-264). Inside the sentence, the section read Human High.',
        stays='The story and the joke.',
        deciding='whether the joke lands as well with “woops” before the punchline',
        ask_because='downside: you kept this line on the fourth page, calling its one-word window a Pangram bug '
                    '(M-264), and the joke’s timing changes',
        reading='The section before this pass: Human, one Medium window on “Woops...” '
                '(%s71ded138-9e16-4494-842b-222da81cbe90).' % H,
        tested='The section with this change: Human High in every window (%s1b906fcb-7099-4a0e-8948-7d0db749969b).' % H),
    'M-68': dict(
        title='“With H., I learned”',
        highlight=['H. taught me another part of the same dyad problem. I learned not to treat',
                   'The accusations couldn’t have survived among people who knew us both.'],
        what='“H. taught me another part of the same dyad problem. I learned not to treat...” becomes “With H., I '
             'learned another part of the same dyad problem: not to treat...”, and the last sentence, “The accusations '
             'couldn’t have survived among people who knew us both.”, goes.',
        why='The window that read Medium was the single word “H.”, which Pangram reads as a sentence by itself. On the '
            'fourth page you kept it and called that a Pangram bug (M-338). Inside the sentence, the section read '
            'Human High. The cut line says again what the section’s first paragraph says (“Baseless accusations only '
            'work with friends who only know one side.”).',
        stays='Everything else in the paragraph.',
        deciding='whether the paragraph can end on her friends affirming her truth',
        ask_because='meaning: the paragraph loses its last line, which the section’s first paragraph already says; you '
                    'kept “H. taught me” on the fourth page (M-338)',
        reading='The section as the article has it now, my fix of the Meetups paragraph in: Human, one Medium window on '
                '“H.” (%s5da10762-3b06-49c5-8659-a483974b66f1). Before this pass the same '
                '(%s61152dd2-3c32-40b3-8e4a-8ebbb9343631).' % (H, H),
        tested='The section with these changes: Human High in every window (%s231c824d-3dbe-44c5-be5d-3fe52fc88574).' % H),
    'M-82': dict(
        title='“That drove me crazy, because”',
        highlight=['That drove me crazy! I mean, why would she lie like that?'],
        what='“That drove me crazy! I mean, why would she lie like that?” becomes “That drove me crazy, because why '
             'would she lie like that?”',
        why='The section’s one Medium window was “That drove me crazy!” (4 words). Joined to its reason, the section '
            'read Human High.',
        stays='The door story, the lying, and the last line about seeing it as an illness.',
        deciding='whether “because why would she” sounds the way you talk',
        ask_because='downside: it changes your version (M-409, from the fourth and fifth pages)',
        reading='The section before this pass: Human, one Medium window on “That drove me crazy!” '
                '(%s63b3104d-ee5d-486b-be0d-acea98e0c980).' % H,
        tested='The section with this change: Human High in every window (%s7a6a097c-d8a6-4c63-af8b-afd18d8193d8).' % H),
}
ASKS = [
    {'id': 'Q-42', 'title': 'What does “without manipulating ... all that expert management” mean?',
     'highlight': [('All that works wonderfully until', 'without manipulating her with all that expert “management.”')],
     'question': 'In the last sentence of “From flow to nitty gritty”, what is the “expert management”, and who would '
                 'be manipulating whom? It said “without manipulating based on all that expert “management,”” and a '
                 'fresh reader found that clause can’t be parsed; the sentence is the section’s last Medium window. My '
                 'guess: she expects me to read her mind and check in all the time, and to manage her feelings like an '
                 'expert without it turning into manipulation. If that’s it, I’ll write it that way and test it.',
     'why': 'Every try read Medium or worse on this sentence: as it was (Medium, %s23715e47-56f7-45d8-a6a4-664613be4e35; '
            'Low in two other checks, %sa21945ec-e22b-45a3-be08-465dbfc7462c and %sa9a6e65c-d1a4-4f89-8ac6-1dcff26c56fc), '
            'my rewrite (AI High, %seb7c696e-ffa6-4506-97d8-a2db36af128a) and two phrases made plain (Medium, '
            '%sf38b40b6-a828-4341-b2d1-4f125588379e). That last try is in the article now, its opening joined to the '
            'bed example (High).' % (H, H, H, H, H),
     'stays': 'The sentence as it reads now, until your answer.',
     'advice_note': 'A line on what you meant is enough; I’ll do the rewrite and test it.'},
    {'id': 'Q-67', 'title': 'What’s off in these three places?',
     'highlight': [(None, 'If one person goes down, the other becomes the whole backup system for housing, money, children, health, and emotional crises.'),
                   (None, 'Sometimes you need privacy from your partner and somewhere else to say what you’re feeling.'),
                   (None, 'They’re only hearing your side, usually while you’re upset, and they may just be trying to protect you, so take what they say with a grain of salt.')],
     'question': 'The first part of “Two Pillars Don’t Hold The Roof Up” reads Medium in three places (highlighted), '
                 'and all three of my tries read worse. A reader could stumble on three things: “That’s a pretty '
                 'terrible time to be trying to run the rest of life with two people” runs the falling-out into the '
                 'point that two people alone have no backup; “Separate confidants can be helpful and harmful” is a line '
                 'the next two sentences say again; and “take what they say with a grain of salt” says again what the '
                 'sentence before says (they’re biased toward you). Is it one of these, or something else?',
     'why': 'Before this pass: Human, three Medium windows (%sb6427065-aaad-4e21-a31b-3ee2f7d5249d). My tries: a word or '
            'two (Low windows, %sa3e48bae-3eaf-48c1-bd33-6e1f169956c5); the helpful-and-harmful line folded into the next '
            'and the last two sentences joined (a Low window and two Medium, %s3e4993ed-d619-4715-904a-cd3e33bf3cf1); the blind writer’s '
            'rewrite of the first and last windows (14%% AI, %sd8299b57-d9d7-4b96-9b4f-6413f0b6c912).' % (H, H, H, H),
     'stays': 'The section as it is, until your answer.',
     'advice_note': 'A line on what’s off is enough; I’ll do the rewrite and test it.'},
]
review = {
    'format': R.FORMAT, 'review_id': 'romance-t7', 'built': '2026-11-24',
    'title': 'Romance Advice I Wish My Parents Taught Me: the Medium windows',
    'intro': ['The whole article as it reads now. You said you don’t like the Medium windows, so I took on the 21 '
              'sections that had one, the way your fix of “Talk about making love before you do it” did (your fix is '
              'in). With my fixes, 19 read Human High in every window, each section checked by itself. Ten of them are in '
              'the article, the fixes of its model text; the other nine change your versions from the fourth page, or a '
              'line you kept there, so they are the cards below, each needing your decision. Two sections still read Medium or worse, and are here as questions: a line '
              'from you on each helps. Every paragraph, picture and video is here in order: nothing is left out.'],
    'git_file': 'articles/romance/review/teach-20261124/REVIEW-T7.html',
    'article': {'file': ART, 'sha256': sha}, 'whole': {'file': ART, 'sha256': sha},
    'links': {'guide': 'https://ibogaqueen.substack.com/p/romance-advice-i-wish-my-parents', 'guide_label': 'your live post',
              'review': 'https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/romance-20261108/articles/romance/review/teach-20261124/REVIEW-T7.md'},
    'types': {'medium': {'label': 'Read Medium', 'about': 'a window of its section read Human at Medium; my fix, tested in its section'},
              'still': {'label': 'Still Medium', 'about': 'every try so far read Medium or worse; a line from you helps'}},
    'suggestions': [],
}
order = []
for cid, spec in CARDS.items():
    chs = CHANGES[cid]
    blocks = [find_block(ch['before']) for ch in chs]
    order.append((min(blocks), cid, spec, chs, blocks))
for _, cid, spec, chs, blocks in sorted(order):
    edits = [{'block': i, 'before': R.block_text(bl, i), 'after': ch['after'][0] if ch['after'] else ''} for i, ch in zip(blocks, chs)]
    spans = []
    for w in spec['highlight']:
        hit = [i for i in blocks if w in bl[i]['text']]
        assert len(hit) == 1, (cid, w)
        spans.append(span(hit[0], w))
    s = {'id': cid, 'type': 'medium', 'title': spec['title'], 'advice': 'approve', 'spans': spans, 'edits': edits,
         'what': spec['what'], 'why': spec['why'], 'stays': spec['stays'], 'deciding': spec['deciding'],
         'advice_note': 'My pick: use it. The section reads Human High with it.' if cid not in ('M-54', 'M-68') else
         'My pick: use it, since its section reads Human High with it; if you’d rather keep %s as it was, Reject it.'
         % ('the beat after the punchline' if cid == 'M-54' else '“H. taught me” and the last line'),
         'found_by': FOUND, 'reading': spec['reading'], 'tested': spec['tested'], 'ask_because': spec['ask_because'],
         'receipt': RECEIPTS[cid]}
    review['suggestions'].append(s)
for a in ASKS:
    spans = []
    for anchor, w in a['highlight']:
        sp = find_words(w)
        spans.append(sp)
    review['suggestions'].append({'id': a['id'], 'type': 'still', 'title': a['title'], 'advice': 'ask',
                                  'question': a['question'], 'why': a['why'], 'stays': a['stays'],
                                  'advice_note': a['advice_note'], 'spans': spans})
probs = R.check(review, bl)
if probs:
    sys.exit('\n'.join(probs))
(HERE / 'REVIEW-T7.json').write_text(json.dumps(review, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
html = R.page(review, md, bl)
(HERE / 'REVIEW-T7.html').write_text(html, encoding='utf-8')
(HERE / 'REVIEW-T7.artifact.html').write_text(R.artifact_view(html), encoding='utf-8')
out = ['# The Medium windows: the cards (2026-11-24)', '',
       'The page shows the whole article ([FIXED.md](../../humanize/fix-20261107/whole/FIXED.md)); these are its cards.', '']
for s in review['suggestions']:
    out += ['## %s. %s' % (s['id'], s['title']), '']
    if s['advice'] == 'ask':
        out += [s['question'], '', s['why'], '', '**' + s['advice_note'] + '**', '']
        continue
    out += ['**Now:**', ''] + ['> ' + e['before'] for e in s['edits']] + ['']
    out += ['**Would read:**', ''] + ['> ' + (e['after'] or '(cut)') for e in s['edits']] + ['']
    out += [s['why'], '', 'Pangram: ' + s['reading'] + ' ' + s['tested'], '', '**' + s['advice_note'] + '**', '']
(HERE / 'REVIEW-T7.md').write_text('\n'.join(out) + '\n', encoding='utf-8')
print('REVIEW-T7: %d blocks, %d cards, %d bytes' % (len(bl), len(review['suggestions']), len(html)))
