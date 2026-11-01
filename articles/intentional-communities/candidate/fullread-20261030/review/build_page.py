"""Joel's marking page for the community article's full read by the lead model (REVIEW-FULLREAD.json, .html,
.artifact.html, .md).

His message of 2026-10-30 20:15 UTC, after the hypnosis guide's own full read: "i guess we need to go back and re-read the
community article as well after this then". I read the live post (master.md, "Updated: Oct 25 2026") beside his published
version (original.md), ten parts, sentence by sentence (../READER-1..10.md, ../FINDINGS.json: 66 findings). Then every
finding was checked against how its words got there and how a lost point left (../READ.md, ../DISPOSITIONS.json):
his edits of 20 October (his and GPT's), his rulings in the owner-edits ledger, and his answers to 59, 64, 65 and 66. A
point he cut stays out (gates E298, E301); light snags in words he chose stay as they are. What is left is here, as
cards on the article as it is live, in the marking page's form (tools/humanization/suggestion_review.py, gate E265):
- the sentences a cut of 24 October (question 64, as I advised) left hanging, fixed without bringing the cut back;
- commas and small slips;
- suggestions for his own words;
- one fix to my words (the anomie paragraph, my draft of his thesis of 17 October).
The post is live, so nothing changes until he answers; then each approved card is an old/new pair for Substack's editor.

  python3 articles/intentional-communities/candidate/fullread-20261030/review/build_page.py
"""
import collections
import datetime
import hashlib
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parents[2]
ROOT = ART.parents[1]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import suggestion_review as sr  # noqa: E402

BLOB = 'https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/community-joel-1018/'
ARTICLE = 'articles/intentional-communities/master.md'
GIT_FILE = 'articles/intentional-communities/candidate/fullread-20261030/review/REVIEW-FULLREAD.html'
MD_FILE = 'articles/intentional-communities/candidate/fullread-20261030/review/REVIEW-FULLREAD.md'
MD = (ART / 'master.md').read_text(encoding='utf-8')
BL = sr.blocks(MD)
FOUND = 'My read of the whole article beside your published version (30 October)'

TYPES = {
    'hanging': {'label': 'Left hanging by a cut',
                'about': 'A sentence that leaned on words you cut on 24 October (question 64, as I advised), and now '
                         'hangs. The fix keeps your cut. Approve, Reject or Revise.'},
    'typo': {'label': 'Commas and slips',
             'about': 'A comma or a small slip in the words as they are. Approve, Reject or Revise.'},
    'yours': {'label': 'Your own words',
              'about': 'A suggestion for words you wrote yourself, or in your edits of 20 October. Approve uses the '
                       'suggestion; Reject keeps your words; Revise lets you write your own.'},
    'mine': {'label': 'My words',
             'about': 'A fix to words I wrote. Approve, Reject or Revise.'},
    'ask': {'label': 'A question for you',
            'about': 'A sentence of yours that can be read two ways. Tell me which you meant in the answer box; it stays '
                     'as it is until you do.'},
}

# (card, finding, type, old, new, why, advice note)
CARDS = [
    ('C-1', 'F1.2', 'typo', 'At the time that meant a lot of boredom', 'At the time, that meant a lot of boredom',
     'Without a comma after "At the time", the sentence first reads as "the time that meant a lot of boredom", and the '
     'reader has to start it again.',
     'Approve: one comma, nothing else changes.'),
    ('C-2', 'F1.3', 'typo', 'computer bug which some folks like my dad especially, felt',
     'computer bug which some folks, like my dad especially, felt',
     'The one comma after "especially" splits "some folks" from "felt", so the sentence reads as broken. A comma on '
     'each side of "like my dad especially" puts it back together.',
     'Approve: one comma, nothing else changes.'),
    ('C-3', 'F1.7', 'typo', 'the longing to escape loneliness which inspired my father’s movie, is everywhere again',
     'the longing to escape loneliness, which inspired my father’s movie, is everywhere again',
     'The comma after "movie", with none before "which", splits the subject from its verb. These are your words of 18 '
     'October, the opening you checked in Pangram yourself.',
     'Approve: one comma. A comma rarely moves a Pangram reading, but these are the words you checked, so it\'s your '
     'call.'),
    ('C-4', 'F1.9', 'mine',
     'In a large society the shared norms and close ties that held those groups together fall apart, and that’s how '
     'large societies end up run by psychopaths.',
     'In a large society, the shared norms and close ties that held those groups together fall apart, and nobody knows '
     'anybody well enough to see what they’re really like. That’s how large societies end up run by psychopaths.',
     '"That\'s how" claims a reason the sentence never gives: it doesn\'t say why the ties falling apart lets '
     'psychopaths rise. This is my paragraph, written on 17 October from your thesis ("large societies breed anomie and '
     'capture by psychopaths"), and the bridge I\'ve added is my guess at your reason.',
     'Approve if that\'s your reason; if it isn\'t, Revise with yours. The comma after "In a large society" goes in '
     'either way.'),
    ('C-5', 'F2.3', 'yours',
     'does not make everyone less passive, selfish, thieving, nor suddenly unlearning learned helplessness.',
     'does not make everyone less passive, selfish or thieving, or suddenly unlearn their learned helplessness.',
     'As it is, the sentence doesn\'t parse: the list switches from "passive, selfish, thieving" to "unlearning", and '
     '"nor" has no verb of its own. Your sentence of 14 October; this keeps all four things.',
     'Your call. I\'d use it: it keeps your words and your point, and a reader gets through it in one go.'),
    ('C-6', 'F2.5', 'yours', 'for outer freedom (secular, nondogmatic, political).',
     'for outer freedom (secular, nondogmatic, political), or the other way around.',
     'The sentence says most communes gave up inner freedom for outer freedom, which is only the secular half. The next '
     'sentence\'s "two pendulum ends", and the two sections after it (the secular communes, then the spiritual ones), '
     'are about both ways. Your words of 20 October.',
     'Your call. I\'d use it: five words, and the paragraph says what the sections after it show.'),
    ('C-7', 'F3.1', 'yours', 'where do you find these people?', 'where do you find people for a practice group?',
     '"These people" points back to nobody. The section before is about the values to list before visiting, and the '
     'practice group is only named in the next section ("Call it a practice group"). This ties the question to your '
     'heading.',
     'Your call. I\'d use it: it keeps your "Uh, but wait" and the heading, and says who.'),
    ('C-8', 'F3.2', 'yours', 'Fun and nice things first give incentive.',
     'Do the fun and nice things first, to give people an incentive.',
     'As it is, it reads like a note to yourself: the reader has to work out that it means "start with the fun and nice '
     'things, because they give people a reason to keep coming". Your words of 20 October.',
     'Your call. I\'d use it: same words, put in order.'),
    ('C-10', 'F3.7', 'typo',
     'The exit terms in “Leaving, Removal, and Dissolution” section after that would also help for thinking about '
     'those agreements.',
     'The exit terms in the “Leaving, Removal, and Dissolution” section after that would also help with thinking about '
     'those agreements.',
     '"In “Leaving, Removal, and Dissolution” section" is missing "the", and "help for thinking about" wants "help with".',
     'Approve: two words, nothing else changes.'),
    ('C-11', 'F4.3', 'hanging', 'But it means that people building', 'That means people building',
     'On 24 October you cut "Does this prove there\'s a universal formula? No." (64.4, as I advised), and I left the '
     '"But" that answered it. Now it contrasts with nothing, and "it" has nothing to point to.',
     'Approve: it keeps your cut, and the sentence makes sense again.'),
    ('C-12', 'F5.6', 'yours',
     'make sure that the person caring about you and listening to you shouldn’t translate that information into '
     'administration over your life',
     'make sure that the person caring about you and listening to you doesn’t turn what you tell them into '
     'administration over your life',
     '"Make sure that ... shouldn\'t translate" doesn\'t parse, and "that information" has nothing before it: it means '
     'what you tell the person while they listen. Your words; "administration over your life" stays.',
     'Your call. I\'d use it: it fixes the grammar and keeps your point.'),
    ('C-13', 'F6.6', 'yours', 'They’re right though that modern folk',
     'The lineages are right, though, that modern folk',
     '"They" comes right after the Huni Kuin shamans and the shamans they accuse, so the reader can\'t tell who is right. '
     'It means the traditional lineages your section starts with. Your words.',
     'Your call. I\'d use it: otherwise a reader may think you\'re siding with the cancer claim.'),
    ('C-14', 'F7.3', 'yours', 'especially when they are fond of each other',
     'especially when an adult and a child are fond of each other',
     '"They" can be read as the adults. Your published version said it plainly: a warm relationship between an '
     'unrelated adult and a child. Your words of 20 October.',
     'Your call. I\'d use it: in this paragraph above all, the reader should know exactly who is meant.'),
    ('C-16', 'F8.5', 'hanging', 'If several are present, they are worth paying attention to',
     'If several of these point to one person or clique, they are worth paying attention to',
     'On 24 October you cut "Presence of one of these alone isn\'t proof of abuse, but" (64.23, as I advised, with your '
     'note that "isn\'t proof of" is a high-frequency AI pattern), and "several" lost the "these" it counted. This keeps '
     'your cut and doesn\'t bring "proof" back.',
     'Approve: it keeps your cut, and the reader knows several of what.'),
    ('C-17', 'F8.6', 'typo', 'over time as I’m describing may happen in my case',
     'over time, as I’ve said may happen in my case',
     '"Which form naturally over time as I\'m describing may happen in my case" doesn\'t parse; it means "as I\'ve said '
     'may happen in my case".',
     'Approve: a comma and one word.'),
    ('C-18', 'F8.8', 'hanging', 'But some practices go too far against the communal spirit.',
     'But some private practices go too far against the communal spirit.',
     'On 24 October you cut "In general, people can have their own private practices, of course." (64.24, as I '
     'advised). That sentence told the reader that "some practices" meant a member\'s own; without it, coming after '
     '"Every practice in this article can be turned against the people using it", it reads as the community\'s '
     'practices.',
     'Approve: one word, and it keeps your cut.'),
    ('C-19', 'F8.10', 'hanging', 'Sometimes it really is their wounded ego projection',
     'Sometimes it really is the dissenter’s wounded ego projecting',
     'On 24 October you cut "That doesn\'t mean everything everyone says is equally valid, though." (64.25, as I '
     'advised), and "their" lost the people it pointed to.',
     'Approve: it keeps your cut and your point.'),
]

# (card, finding, the words it's about, question, why, my advice)
QUESTIONS = [
    ('C-9', 'F3.3', 'you can all meet in a rented or borrowed space, or at each other’s houses',
     'Did you mean that the group keeps meeting in rented or borrowed places, or at each other\'s houses, until it '
     'really needs land, or that it can try living together there before anyone buys land?',
     'After the phases, the next step is "meet in a rented or borrowed space, or at each other\'s houses", which the '
     'group has been doing all along, so the reader can\'t tell what changes once they\'re past the phases. Your version '
     'of 18 October had it the other way round ("Until that\'s happened ... That\'s okay! You can all meet in a rented '
     'or borrowed space ..."); when you made it the step after the phases on 20 October, "meet" stayed.',
     'Tell me which. If it\'s meeting: "you can keep meeting in a rented or borrowed space, or at each other\'s houses, '
     'long before anyone needs a land surveyor". If it\'s living together: "you can all live together in a rented or '
     'borrowed space first, long before anyone needs a land surveyor". My guess is the second, since the sentence starts '
     '"if you still want to live together".'),
    ('C-15', 'F7.5', 'but that’s something which varies a lot in every society also.',
     'What varies: what counts as acceptable physical discipline, from one society to another, or how much of it goes '
     'on, in every society, so that it isn\'t special to communes?',
     '"That\'s something which varies a lot in every society also" doesn\'t say what varies, so a reader can take it as '
     'saying abuse is relative, and has to reread to see what you mean. Your words of 20 October.',
     'Tell me which and I\'ll put it plainly. For the first: "but what counts as acceptable physical discipline varies '
     'a lot from one society to another". For the second: "but that goes on, more or less, in every society, not only '
     'in communes".'),
]


def quote_start(t, n=7):
    w = t.strip('“”"').split()
    return '“%s%s”' % (' '.join(w[:n]), ' …' if len(w) > n else '')


def changed_span(before, after):
    """Where BEFORE and AFTER differ, in BEFORE's offsets, widened to whole words."""
    a = 0
    while a < min(len(before), len(after)) and before[a] == after[a]:
        a += 1
    z = 0
    while z < min(len(before), len(after)) - a and before[-1 - z] == after[-1 - z]:
        z += 1
    k, e = a, len(before) - z
    while k > 0 and before[k - 1] not in ' ':
        k -= 1
    while e < len(before) and before[e] not in ' .,;:!?':
        e += 1
    return k, e


def main():
    S = []
    for cid, fid, typ, old, new, why, note in CARDS:
        hits = [b['i'] for b in BL if old in b['text'] and not b['level']]
        assert len(hits) == 1, (cid, hits)
        i = hits[0]
        before = BL[i]['text']
        assert before.count(old) == 1, cid
        after = before.replace(old, new)
        k, e = changed_span(before, after)
        S.append({'id': cid, 'spot': fid, 'type': typ, 'title': quote_start(before[k:]),
                  'where': sr.where(BL, i), 'spans': [{'block': i, 'start': k, 'end': e}],
                  'edits': [{'block': i, 'before': before, 'after': after}], 'inserts': [], 'moves': [],
                  'what': '“%s” becomes “%s”' % (old, new), 'why': why,
                  'stays': 'The rest of the paragraph, word for word.', 'advice': 'approve', 'advice_note': note,
                  'found_by': FOUND,
                  'deciding': 'Approve uses the new words; Reject keeps it as it is; Revise lets you write your own.'})
    for cid, fid, words, q, why, note in QUESTIONS:
        hits = [b['i'] for b in BL if words in b['text'] and not b['level']]
        assert len(hits) == 1, (cid, hits)
        i = hits[0]
        k = BL[i]['text'].find(words)
        S.append({'id': cid, 'spot': fid, 'type': 'ask', 'title': quote_start(words), 'where': sr.where(BL, i),
                  'spans': [{'block': i, 'start': k, 'end': k + len(words)}], 'edits': [], 'inserts': [], 'moves': [],
                  'advice': 'ask', 'question': q, 'why': why, 'stays': 'It stays as it is until you answer.',
                  'advice_note': note, 'found_by': FOUND})
    S.sort(key=lambda s: (s['spans'][0]['block'], s['spans'][0]['start']))
    n = collections.Counter(s['type'] for s in S)
    review = {
        'format': sr.FORMAT, 'review_id': 'intentional-communities-fullread-20261030',
        'title': 'Community Article Cards, 30 October',
        'intro': [
            'Your community article as it is live ("Updated: Oct 25 2026"), read by me sentence by sentence beside your '
            'published version, the way I read the hypnosis guide (not Sonnet).',
            'I checked each thing I found against how its words got there. Points your edits of 20 October, your rulings '
            'or your answers took out stay out: they\'re your cuts. Snags in words you chose that a reader still gets '
            'stay as they are. What\'s left is %d cards:' % len(S),
            '<b>%d sentences a cut of 24 October left hanging</b> (cuts I advised): each fix keeps the cut. <b>%d commas '
            'and slips.</b> <b>%d suggestions for your own words.</b> <b>%d fix to my words.</b> <b>%d questions</b>, '
            'where a sentence of yours can be read two ways: tell me which you meant.' % (
                n['hanging'], n['typo'], n['yours'], n['mine'], n['ask']),
            'The post is live, so nothing changes until you say. Once you\'ve answered, I\'ll give you each approved '
            'change as the exact old and new words to change in Substack\'s editor.',
            'Your answers save as you click. When you\'re done, click <b>Copy my answers</b> (or <b>Save them as a '
            'file</b>) and send them to me.',
        ],
        'git_file': GIT_FILE, 'article': {'file': ARTICLE, 'sha256': hashlib.sha256(MD.encode('utf-8')).hexdigest()},
        'links': {'guide': BLOB + ARTICLE, 'review': BLOB + MD_FILE},
        'built': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M UTC'),
        'types': TYPES, 'suggestions': S,
    }
    probs = sr.check(review, BL)
    for p in probs:
        print('PROBLEM', p)
    (HERE / 'REVIEW-FULLREAD.json').write_text(json.dumps(review, ensure_ascii=False, indent=1) + '\n',
                                               encoding='utf-8')
    if probs:
        sys.exit(1)
    page = sr.page(review, MD, BL)
    (HERE / 'REVIEW-FULLREAD.html').write_text(page, encoding='utf-8')
    (HERE / 'REVIEW-FULLREAD.artifact.html').write_text(sr.artifact_view(page), encoding='utf-8')
    (HERE / 'REVIEW-FULLREAD.md').write_text(cards_md(review), encoding='utf-8')
    print(len(S), 'cards:', dict(n))


def marked(j, spans):
    t = BL[j]['text']
    for sp in sorted((x for x in spans if x['block'] == j), key=lambda x: -x['start']):
        t = t[:sp['start']] + '**' + t[sp['start']:sp['end']] + '**' + t[sp['end']:]
    return t


def cards_md(review):
    """Every card as a page GitHub renders, in the article's order (the page's readable copy in Git)."""
    types = review['types']
    out = ['# %s: every card' % review['title'], '',
           'The page\'s cards as text, in the order of the article. Built %s from [the article as it is live](%s). To '
           'answer, use the page; or write your answer under a card\'s number in a message to me. What I found and '
           'didn\'t put on the page, and why, is in [the read\'s record](%s).' % (
               review['built'], review['links']['guide'],
               BLOB + 'articles/intentional-communities/candidate/fullread-20261030/READ.md'), '']
    section = None
    for s in review['suggestions']:
        b = s['spans'][0]['block']
        if BL[b]['section'] != section:
            section = BL[b]['section']
            out += ['## %s' % (section or 'The opening'), '']
        out += ['### %s: %s (%s)' % (s['id'], s['title'], types[s['type']]['label']), '']
        if s['advice'] == 'ask':
            out += ['**As it is now** (the words it\'s about in bold):', '', '> %s' % marked(b, s['spans']), '',
                    '**My question:** %s' % s['question'], '', '**Why I ask:** %s' % s['why'], '',
                    '**My advice:** %s' % s['advice_note'], '']
            continue
        for e in s['edits']:
            out += ['**Now** (the words it changes in bold):', '', '> %s' % marked(e['block'], s['spans']), '',
                    '**How it would read:**', '', '> %s' % e['after'], '',
                    '**In Substack\'s editor:** %s' % s['what'], '']
        out += ['**Why:** %s' % s['why'], '', '**My advice:** %s' % s['advice_note'], '']
    return '\n'.join(out).replace('\n\n\n', '\n\n') + '\n'


if __name__ == '__main__':
    main()
