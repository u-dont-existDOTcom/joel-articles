"""Nibbāna, batch n1 (2026-10-23): the High and Medium windows of the Pangram 4.1 check of 2026-10-20, each fixed inside
its own sentences in Joel's editor HTML of 2026-10-22 (source/substack-editor-20261022.html, the text the check read).

Of the check's 22 AI windows ([his result](https://www.pangram.com/feed/1ffe8aed-a00a-4273-846c-635ae22b2917)), the six High
and five Medium ones are here, in nine paragraphs. They are explanations, evidence and disclaimers around his story,
not the story (RED-WINDOWS-20261020.md, "First look"), and each fix keeps every claim, citation and link and changes only
the shape the window sits on. His own lines stay as they are, the distinctive ones above all ("Matter weighs what its
binding weighs. Light weighs nothing.", "More like a driverless car.", "That's my own CYA showing. 😇"). The eleven Low
windows wait for the whole-article recheck: a Low window read Human unchanged when checked on its own pair (the hypnosis
guide's E226), so the API can't show whether a fix there helps.

Each fixed paragraph (with the next one where the window runs into it) goes through the API first (E218; the hypnosis
lane's laptop folder, pangram-api/hg-b472/), then a reader checks meaning and sense, and the passing ones go into the
working copy, HUMANIZED-SO-FAR.html; the post itself is Joel's to update.

  python3 articles/nibbana/humanize/fix-20261023/n1/make_n1.py   (from the repo root)
      -> EDITS.json, TEXTS.json, texts/*.txt, DRAFTS.md
"""
import json, pathlib, sys

N = pathlib.Path(__file__).resolve().parent
H = N.parents[1]
REPO = H.parents[2]
sys.path.insert(0, str(REPO / 'tools' / 'humanization'))
import substack_check_text as C  # noqa: E402

SRC = H / 'source' / 'substack-editor-20261022.html'
RESULT = 'https://www.pangram.com/feed/1ffe8aed-a00a-4273-846c-635ae22b2917'
A_SN2222 = '<a target="_blank" rel="noopener noreferrer nofollow" href="https://suttacentral.net/sn22.22/en/sujato">SN 22.22</a>'
A_CERN = '<a target="_blank" rel="noopener noreferrer nofollow" href="https://home.cern/news/news/physics/other-99">'
A_DIAMOND = ('<a target="_blank" rel="noopener noreferrer nofollow" href="https://read.84000.co/translation/toh16.html">'
             '<em>Diamond Sutra</em></a>')
A_SN2295 = '<a target="_blank" rel="noopener noreferrer nofollow" href="https://suttacentral.net/sn22.95/en/sujato">SN 22.95</a>'
A_DHP170 = '<a target="_blank" rel="noopener noreferrer nofollow" href="https://suttacentral.net/dhp170/en/sujato">Dhammapada 170</a>'

# key: (windows, the shape the window sits on, [(old, new), ...]) -- old and new are the editor HTML's
E = {
    'n1-unification': (
        '12 (Medium)', 'a definition with a balanced list of four ("I use X for the functional coordination through which a '
                       'person speaks, crosses a road, recognizes a friend, and answers a message")',
        [('I use “unification” for the functional coordination through which a person speaks, crosses a road, recognizes a '
          'friend, and answers a message, even with no separate knower.',
          'When I say “unification”, I mean whatever pulls everything together so that a person can talk, cross a road, '
          'recognize a friend and answer a text, and it works even when there’s no separate knower in there.')]),
    'n1-nde': (
        '31 (Low), 32 (High)', '"They aren\'t proof of ..., but they could help explain ..." (the "not proof" frame the gate '
                               'lists, E193) and the evidence as a tidy list ("See this X, the Y, and a recent Z.")',
        [('Those cases had an externally verifiable target, which was not part of my room experience, since I was not '
          'floating around to notice any specific details. They aren’t proof of my own event, but they could help explain '
          'what I mean by an experience that was no longer limited by the body’s vantage point. See this ',
          'Those cases had a target that other people could check, and my room experience didn’t, since I wasn’t floating '
          'around noticing specific details. So they can’t vouch for my event, but they help show what I mean by an '
          'experience that wasn’t stuck at the body’s vantage point anymore. If you want to dig in, there’s this ')]),
    'n1-percentages': (
        '51 (Medium)', 'a colon definition with two semicolon halves in parallel, then a closer ("Partial untying isn\'t '
                       'limited to that range.")',
        [('My percentages are playful shorthand for how much binding has dissolved: around <strong>1%</strong>, a person '
          'remains fully functional; by roughly <strong>5%</strong>, function is barely possible. Partial untying isn’t '
          'limited to that range.',
          'My percentages are just playful shorthand for how much binding has dissolved, and partial untying isn’t limited '
          'to the range I give: at around <strong>1%</strong> a person can still do everything fine, and by roughly '
          '<strong>5%</strong> they can barely function.')]),
    'n1-burden': (
        '80 (High), 81 (Medium), 82 (Low)', 'two colon-and-semicolon splits in a row ("splits the accounting cleanly in SN '
                                             '22.22: X; Y", "Physics agrees that ...: X; Y") with an aside between dashes',
        [('The Buddha splits the accounting cleanly in ' + A_SN2222 + ': the five aggregates are the burden; craving is '
          'picking it up. The tangle is heavy by nature – even an arahant feels the first dart – and craving keeps us '
          'carrying it. Physics agrees that binding is literally heavy: ' + A_CERN + 'quarks supply less than 1% of a '
          'proton’s mass; roughly 99% comes from gluon-binding energy</a>.',
          'In ' + A_SN2222 + ' the Buddha keeps two things apart: the five aggregates are the burden, and craving is what '
          'picks it up. The tangle is heavy all by itself (even an arahant still feels the first dart), and craving is why '
          'we keep carrying it. Physics actually agrees that binding is heavy, literally: ' + A_CERN + 'quarks supply less '
          'than 1% of a proton’s mass, and roughly 99% comes from gluon-binding energy</a>.')]),
    'n1-last-test': (
        '120 (Low), 121 (High), 122 (Low)', 'significance-staging ("That last test matters because ...") and "does not turn '
                                            'somebody into X, let alone Y"',
        [('That last test matters because a stream-enterer still has most fetters. They still need to do reparenting like '
          'other folks, and even a genuine breakthrough does not turn somebody into a therapist, let alone a saint.',
          'I’m asking that last one because a stream-enterer still has most of the fetters. They still need to do '
          'reparenting like other folks, and even a real breakthrough won’t turn somebody into a therapist, let alone a '
          'saint.')]),
    'n1-rebirth': (
        '126 (Medium)', 'a definition with a colon and a chain ("Rebirth is causal continuity without a traveler, often '
                        'called a mind-stream: ...")',
        [('Rebirth is causal continuity without a traveler, often called a mind-stream: craving and clinging condition '
          'becoming, and becoming becomes birth.',
          'What continues is a chain of causes with no traveler riding along, often called a mind-stream: craving and '
          'clinging condition becoming, and becoming becomes birth.')]),
    'n1-diamond': (
        '129 (High)', 'a concession ("although the early Pāli texts offer closely related images") and the sources as a '
                      'tidy list of two parallel sentences',
        [('The famous stanza I loved actually comes from the later Mahāyāna ' + A_DIAMOND + ', which puts some words in his '
          'mouth, although the early Pāli texts offer closely related images. ' + A_SN2295 + ' compares form to foam, '
          'feeling to a bubble, perception to a mirage, and consciousness to a magic trick. ' + A_DHP170 + ' asks us to see '
          'the world as a bubble and mirage.',
          'Turns out the famous stanza I loved comes from the later Mahāyāna ' + A_DIAMOND + ', which puts some words in his '
          'mouth. The early Pāli texts do have images that are pretty close, though: ' + A_SN2295 + ' compares form to '
          'foam, feeling to a bubble, perception to a mirage and consciousness to a magic trick, and ' + A_DHP170 + ' asks '
          'us to see the world as a bubble and a mirage.')]),
    'n1-science': (
        '133 (High)', 'four findings as a colon list in parallel ("Science circles consciousness\'s edges: X, Y, Z, and W")',
        [('Science circles consciousness’s edges: people can function with no felt controller, several things can be '
          'cognized at once, split-brain patients can resemble two knowers sharing a skull, and one recent theory models '
          'minds as nested parallel observers.',
          'Science only gets to circle the edges of consciousness, though it finds some wild stuff out there: people '
          'functioning with no felt controller, several things cognized at once, split-brain patients who can seem like two '
          'knowers sharing a skull, and one recent theory that models minds as nested parallel observers.')]),
    'n1-driving': (
        '164 (High), 165 (Medium)', 'possibilities as a list ("X is one possibility; so is A, B, a combination, or God only '
                                    'knows"), a hedge ("Whatever the explanation, to be safe") and a disclaimer in a '
                                    'policy\'s voice ("Anyone having comparable episodes should stop operating machinery '
                                    '...")',
        [('Luck is one possibility; so is a misunderstanding of what was happening, some feature of how these states '
          'operate, a combination, or God only knows.',
          'Maybe he was just lucky, or he misunderstood what was happening, or there’s something about how these states '
          'work, or some mix of those, or God only knows.'),
         ('Whatever the explanation, to be safe, I wouldn’t keep driving through that. Anyone having comparable episodes '
          'should stop operating machinery until they understand them better.',
          'Either way, I wouldn’t keep driving through that myself. If you’re having episodes like that, I’d stay away from '
          'driving or running machinery until you understand them better.')]),
}


# a paragraph before the edited one, where the window's reading leans on it (window 120, "Can you still recognize trauma
# without floating above it?", read AI just before window 121)
CONTEXT_BEFORE = {'n1-last-test': 1}


# Try 2 (after the API round of 02:24 UTC: the five below read AI on their own, n1-percentages and n1-driving with the
# changed sentence High): each keeps every claim, citation and link, and changes the paragraph's frame rather than its
# words (the hypnosis guide's E223), without inventing anything of his
T2 = {
    'n1-nde': [
        ('The closest comparison that’s worth mentioning is the out-of-body perception in some near-death experiences. People '
         'sometimes report seeing things from impossible angles, and a controversial subset of those reports were verified by '
         'others in the room. Those cases had an externally verifiable target, which was not part of my room experience, since '
         'I was not floating around to notice any specific details. They aren’t proof of my own event, but they could help '
         'explain what I mean by an experience that was no longer limited by the body’s vantage point. See this ',
         'The closest thing I can compare it to is the out-of-body part of some near-death experiences. People sometimes '
         'report seeing things from impossible angles, and some of those reports (controversially) were verified by others in '
         'the room. My room event had nothing like that to check, though, since I wasn’t floating around noticing any details. '
         'So those cases can’t back mine up. They just help me show what I mean by an experience that wasn’t stuck at the '
         'body’s vantage point anymore. If you want to go down that rabbit hole, there’s this ')],
    'n1-percentages': [
        ('My percentages are playful shorthand for how much binding has dissolved: around <strong>1%</strong>, a person '
         'remains fully functional; by roughly <strong>5%</strong>, function is barely possible. Partial untying isn’t '
         'limited to that range.',
         'My percentages are just a playful way of saying how much binding has dissolved. Around <strong>1%</strong>, a '
         'person can still do everything fine. Around <strong>5%</strong>, they can hardly do anything. (And partial untying '
         'goes beyond that range too.)')],
    'n1-burden': [
        ('The Buddha splits the accounting cleanly in ' + A_SN2222 + ': the five aggregates are the burden; craving is '
         'picking it up. The tangle is heavy by nature – even an arahant feels the first dart – and craving keeps us '
         'carrying it. Physics agrees that binding is literally heavy: ' + A_CERN + 'quarks supply less than 1% of a '
         'proton’s mass; roughly 99% comes from gluon-binding energy</a>.',
         'In ' + A_SN2222 + ' the Buddha puts the weight in one place and the carrying in another. The five aggregates are '
         'the burden, and craving is what picks it up. The tangle is heavy all by itself (even an arahant still feels the '
         'first dart), and craving is why we keep lugging it around. Physics backs this up, and I mean literally: ' + A_CERN +
         'quarks supply less than 1% of a proton’s mass, and roughly 99% comes from gluon-binding energy</a>.')],
    'n1-diamond': [
        ('The famous stanza I loved actually comes from the later Mahāyāna ' + A_DIAMOND + ', which puts some words in his '
         'mouth, although the early Pāli texts offer closely related images. ' + A_SN2295 + ' compares form to foam, '
         'feeling to a bubble, perception to a mirage, and consciousness to a magic trick. ' + A_DHP170 + ' asks us to see '
         'the world as a bubble and mirage.',
         'The famous stanza I loved is actually from the later Mahāyāna ' + A_DIAMOND + ', which puts some words in his mouth. '
         'The early Pāli texts were already reaching for the same kind of pictures, though. In ' + A_SN2295 + ' form is like '
         'foam, feeling is like a bubble, perception is a mirage and consciousness is a magic trick, and ' + A_DHP170 + ' '
         'tells us to look at the world like a bubble, or a mirage.')],
    'n1-driving': [
        ('Luck is one possibility; so is a misunderstanding of what was happening, some feature of how these states '
         'operate, a combination, or God only knows.',
         'Whether that was luck, or he got it wrong about what was happening, or it’s something about how these states work, '
         'or some mix of those, God only knows.'),
        ('Whatever the explanation, to be safe, I wouldn’t keep driving through that. Anyone having comparable episodes '
         'should stop operating machinery until they understand them better.',
         'Either way, I wouldn’t keep driving through that myself. If you’re having episodes like that, I’d stay away from '
         'driving or running machinery until you understand them better.')],
    # n1-science read Human on try 1, but the reader's check (REVIEW.md, item 4) found two additions a reader would take
    # as claims: "only gets to" (a stated limit on science) and "some wild stuff" (a reaction of his the original doesn't
    # have). Try 2 is the reader's own fix of that frame, the rest of try 1 unchanged.
    'n1-science': [
        ('Science circles consciousness’s edges: people can function with no felt controller, several things can be '
         'cognized at once, split-brain patients can resemble two knowers sharing a skull, and one recent theory models '
         'minds as nested parallel observers.',
         'Science circles the edges of consciousness, and here’s some of what it finds out there: people functioning with no '
         'felt controller, several things cognized at once, split-brain patients who can seem like two knowers sharing a '
         'skull, and one recent theory that models minds as nested parallel observers.')],
}


# Try 3(after the API round of 02:28 UTC: n1-nde, n1-burden, n1-diamond and n1-driving read AI, High, again, and a pair
# through the API reproduces a High window (the hypnosis guide's E226), so these are real failures, not the alone check's
# harshness). Tries 1 and 2 reworded each paragraph in the same order. Try 3 changes the order and the frame the way Joel's
# own passing text does (his Appendix C opening, and the guide's s1b): the evidence as his kind of bracketed aside after the
# claim it backs, his story or his point first, and the disclaimer as a consequence rather than a closing frame. Every
# claim, citation, link and his own lines stay ("splits the accounting cleanly", "Matter weighs what its binding weighs.
# Light weighs nothing.", "That's my own CYA showing. 😇").
A_NDE1 = '<a target="_blank" rel="noopener noreferrer nofollow" href="https://pmc.ncbi.nlm.nih.gov/articles/PMC10158795/">'
A_NDE2 = '<a target="_blank" rel="noopener noreferrer nofollow" href="https://pubmed.ncbi.nlm.nih.gov/37423492/">'
A_NDE3 = '<a target="_blank" rel="noopener noreferrer nofollow" href="https://pmc.ncbi.nlm.nih.gov/articles/PMC12573288/">'
T3 = {
    'n1-nde': [
        ('a controversial subset of those reports were verified by others in the room. Those cases had an externally '
         'verifiable target, which was not part of my room experience, since I was not floating around to notice any specific '
         'details. They aren’t proof of my own event, but they could help explain what I mean by an experience that was no '
         'longer limited by the body’s vantage point. See this ' + A_NDE1 + 'systematic analysis of near-death reports</a>, '
         'the ' + A_NDE2 + 'AWARE-II cardiac-arrest study</a>, and a recent ' + A_NDE3 + 'veridical-NDE evidence scale</a>.',
         'a controversial subset of those reports were verified by others in the room (see this ' + A_NDE1 + 'systematic '
         'analysis of near-death reports</a>, the ' + A_NDE2 + 'AWARE-II cardiac-arrest study</a>, and a recent ' + A_NDE3 +
         'veridical-NDE evidence scale</a>). Nobody could check anything like that in my room event, since I wasn’t floating '
         'around noticing specific details, so those reports don’t prove anything about mine. They might still help explain '
         'what I mean by an experience that wasn’t limited by the body’s vantage point anymore.')],
    'n1-burden': [
        ('The Buddha splits the accounting cleanly in ' + A_SN2222 + ': the five aggregates are the burden; craving is '
         'picking it up. The tangle is heavy by nature – even an arahant feels the first dart – and craving keeps us '
         'carrying it. Physics agrees that binding is literally heavy: ' + A_CERN + 'quarks supply less than 1% of a '
         'proton’s mass; roughly 99% comes from gluon-binding energy</a>.',
         'In ' + A_SN2222 + ' the five aggregates are the burden and craving is what picks it up, so the Buddha splits the '
         'accounting cleanly. The tangle’s heavy by nature (even an arahant feels the first dart), and craving’s what keeps us '
         'carrying it. And binding is literally heavy in physics too (' + A_CERN + 'quarks supply less than 1% of a proton’s '
         'mass, roughly 99% comes from gluon-binding energy</a>).')],
    'n1-diamond': [
        ('I used to attribute “life is like a dream” directly to the historical Buddha. The famous stanza I loved actually '
         'comes from the later Mahāyāna ' + A_DIAMOND + ', which puts some words in his mouth, although the early Pāli texts '
         'offer closely related images. ' + A_SN2295 + ' compares form to foam, feeling to a bubble, perception to a mirage, '
         'and consciousness to a magic trick. ' + A_DHP170 + ' asks us to see the world as a bubble and mirage.',
         'I used to attribute “life is like a dream” directly to the historical Buddha, until I found out the famous stanza I '
         'loved comes from the later Mahāyāna ' + A_DIAMOND + ', which puts some words in his mouth. The early Pāli texts do '
         'have closely related images (' + A_SN2295 + ' compares form to foam, feeling to a bubble, perception to a mirage '
         'and consciousness to a magic trick, and ' + A_DHP170 + ' asks us to see the world as a bubble and mirage).')],
    'n1-driving': [
        ('He never had an accident either. Luck is one possibility; so is a misunderstanding of what was happening, some '
         'feature of how these states operate, a combination, or God only knows.',
         'He never had an accident either. God only knows why (luck, a misunderstanding of what was happening, something '
         'about how these states work, some mix of those, etc).'),
        ('Whatever the explanation, to be safe, I wouldn’t keep driving through that. Anyone having comparable episodes '
         'should stop operating machinery until they understand them better.',
         'Either way, I wouldn’t keep driving through that myself. If you’re having episodes like that, I’d stay away from '
         'driving or running machinery until you understand them better.')],
}


def para_of(html, i):
    a = html.rindex('<p', 0, i)
    return a, html.index('</p>', i) + 4


def main():
    src = SRC.read_text(encoding='utf-8')
    cand, edits, texts, drafts = src, [], {}, ['# Nibbāna, batch n1: each fix in its paragraph', '',
                                                'From [the check of 2026-10-20](%s); `make_n1.py` says why.' % RESULT, '']
    for key, (wins, shape, pairs) in E.items():
        spans = []
        for old, new in pairs:
            assert src.count(old) == 1 and cand.count(old) == 1, (key, old[:40])
            i = cand.index(old)
            cand = cand.replace(old, new)
            spans.append(para_of(cand, i))
            edits.append({'key': key if len(pairs) == 1 else '%s-%d' % (key, len(spans)), 'windows': wins, 'shape': shape,
                          'old': old, 'new': new})
        a, b = min(x[0] for x in spans), max(x[1] for x in spans)
        for _ in range(CONTEXT_BEFORE.get(key, 0)):
            a = cand.rindex('<p', 0, a)
        para_html = cand[a:b]
        texts['n1_' + key[3:].replace('-', '_')] = C.checked_text(para_html)
        drafts += ['## %s (windows %s)' % (key, wins), '', 'The shape: %s.' % shape, '']
        for old, new in pairs:
            drafts += ['Was: %s' % C.checked_text('<p>%s</p>' % old), '', 'Now: %s' % C.checked_text('<p>%s</p>' % new), '']
    # tries 2 and 3's texts, each from the source with only that paragraph's edits of that try
    for suffix, tries in (('_t2', T2), ('_t3', T3)):
        for key, pairs in tries.items():
            c2, spans = src, []
            for old, new in pairs:
                assert c2.count(old) == 1, (key, old[:40])
                i = c2.index(old)
                c2 = c2.replace(old, new)
                spans.append(para_of(c2, i))
            a, b = min(x[0] for x in spans), max(x[1] for x in spans)
            texts['n1_' + key[3:].replace('-', '_') + suffix] = C.checked_text(c2[a:b])
    (N / 'CANDIDATE.html').write_text(cand, encoding='utf-8')
    (N / 'EDITS.json').write_text(json.dumps(edits, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    (N / 'texts').mkdir(exist_ok=True)
    for name, t in texts.items():
        (N / 'texts' / (name + '.txt')).write_text(t, encoding='utf-8')
    (N / 'TEXTS.json').write_text(json.dumps(texts, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    (N / 'DRAFTS.md').write_text('\n'.join(drafts) + '\n', encoding='utf-8')
    for name, t in texts.items():
        print('%-18s %3d words | %s' % (name, len(t.split()), t[:80].replace('\n', ' / ')))


if __name__ == '__main__':
    main()
