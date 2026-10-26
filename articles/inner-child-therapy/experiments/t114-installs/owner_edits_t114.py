#!/usr/bin/env python3
"""Turn 114: OWNER-EDITS.json after his answers from the turn-113 review sheet (apply_t114.py). The fifteen entries whose
strings his approved cards changed get their current strings, each with a history line, and one new entry records the
turn: every case heading line with its level, the paragraphs the splits start, the moved sentence in its place, his 109 A
and his "you", and what must be gone. Applied once; it refuses to run again."""
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
P = HERE.parents[1] / 'OWNER-EDITS.json'
SEC = json.loads((HERE.parent / 't113-shape' / 'SECTIONS.json').read_text(encoding='utf-8'))['sections']
data = json.loads(P.read_text(encoding='utf-8'))
assert not any(e['id'] == 'joel-114-20261026' for e in data['entries']), 'already applied'
E = {e['id']: e for e in data['entries']}
WHEN = 'Turn 114 (his answers of 2026-10-26 00:52 UTC, experiments/t114-answers/ANSWERS-20261026-0052.json)'

# each failing string, as the article has it now (a lifted heading's words left the paragraph; a split made two)
SAFE = "Even once, old stuff or not, get safe first, which is not a small thing at all, I know."
CHANGES = {
    'tf12-test-line-pending-20261018': ('Q-me answered "you"', [
        ("But they can know things you don't and still be wrong about you. The test is whether the relationship makes me more grounded, truthful, and free.",
         ["But they can know things you don't and still be wrong about you. The test is whether the relationship makes you more grounded, truthful, and free."])]),
    'rel-meditate-moved': ('H-hooks approved: the paragraph starts after its heading, his "If a relationship keeps making you feel less safe"', [
        ('If a relationship keeps making you feel less safe, meditate on why it makes you feel unsafe, and what keeps you in it.',
         ['Meditate on why it makes you feel unsafe, and what keeps you in it.']),
        ('If you really did hurt them, repair it.', ['Repair it. Easier said than done, but'])]),
    'rel-danger-line': ('H-hooks approved: the danger line is its own paragraph under his "If they\'ve actually hurt or threatened you"', [
        ("But if they've actually hurt or threatened you, even once, old stuff or not, get safe first, which is not a small thing at all, I know.", [SAFE])]),
    'guide-update-20261003-covered': ('H-borrow approved: the warmth paragraph starts after its heading, his "For warmth"', [
        ('For warmth, think of someone you remember fondly.', ['Think of someone you remember fondly.'])]),
    'sws-p3-p5-joel': ('H-start approved: "If nothing comes," became the heading "If no answer comes", "Or if you do get an answer," and "If '
                       'it tells you to do something," are headings, and "How you picture all that is up to you ..." moved up to the end '
                       'of the answer paragraph', [
        ("If nothing comes, that's fine for now. No need to answer for that part just because you'd set this up as a healing session. Even without the answer, you can notice what sets the reaction off, and you can understand what the reaction is propelling you toward, and away from.",
         ["That's fine for now. No need to answer for that part just because you'd set this up as a healing session. Even without the answer, you can notice what sets the reaction off, and you can understand what the reaction is propelling you toward, and away from."]),
        ("Or if you do get an answer, it could come in different forms, like as a voice or just a hunch. It's often more like a feeling. Maybe grief or anger. If so just listen and be present for it if that's what it wants. If it tells you to do something, I'd only do it if it's loving and leaves you free. It should make sense, too. Even then, anything big or hard to undo can wait until you're calm and you've checked it against what you actually know.",
         ["It could come in different forms, like as a voice or just a hunch. It's often more like a feeling. Maybe grief or anger. If so just listen and be present for it if that's what it wants. How you picture all that is up to you, as long as it helps, and the simpler the better.",
          "I'd only do it if it's loving and leaves you free. It should make sense, too. Even then, anything big or hard to undo can wait until you're calm and you've checked it against what you actually know."])]),
    'adultfake-altered-states-joel': ('H-fake approved: his first clause is the heading "For some people it only stops feeling fake in an altered state"', [
        ("For some people it only stops feeling fake in an altered state, like on MDMA or deep in meditation. All of a sudden your little one is right there! Oh my gosh! And the love or grief that sounded like therapy talk is just obvious. Old memories might come up too. They can feel totally real, but that alone doesn't prove they happened. I'd still hang on to what you felt, even once it's gone, and try to bring a little of it into your normal life. You've felt that your little one is real now, so talking to them afterward isn't just pretending.",
         ["Like on MDMA or deep in meditation. All of a sudden your little one is right there! Oh my gosh! And the love or grief that sounded like therapy talk is just obvious. Old memories might come up too. They can feel totally real, but that alone doesn't prove they happened. I'd still hang on to what you felt, even once it's gone, and try to bring a little of it into your normal life. You've felt that your little one is real now, so talking to them afterward isn't just pretending."])]),
    'bus-h3': ('H-guard approved: his "If it\'s been calling all this stupid" is the heading', [
        ("If it's been calling all this stupid, it might turn out to be scared of getting its hopes up. I wouldn't want to get mine up either. I'd tell it something like, \"You don't have to hope yet, I'll keep coming back even when I mess up.\" Sometimes it doesn't say anything back for a while.",
         ["It might turn out to be scared of getting its hopes up. I wouldn't want to get mine up either. I'd tell it something like, \"You don't have to hope yet, I'll keep coming back even when I mess up.\" Sometimes it doesn't say anything back for a while."])]),
    'pgq-004-anxiety': ('H-start approved: the stop rule\'s condition is its heading', [
        ("If a part hesitates about being touched or about sex, or says no to going deeper in this work or to an altered state, I'd stop there and not test it, even when it sounds like a prediction.",
         ["If a part hesitates about being touched or about sex, or says no to going deeper in this work or to an altered state",
          "I'd stop there and not test it, even when it sounds like a prediction."])]),
    '5meo-before-history-20261011': ('H-escape approved: "Your own drug history matters too." left for the heading "If a past trip went badly"', [
        ('Your own drug history matters too', ['If a past trip went badly'])]),
    'q4b-caution-signs-20261011b': ('H-escape approved: the spaced-out paragraph starts under the heading "If you keep coming back from trips confused or spaced out"', [
        ('Say you keep coming back from trips', ['If you keep coming back from trips'])]),
    'finding-a-therapist-joel-20261019': ('H-therapist approved: "Before choosing a therapist," and "Regarding AI therapy," became headings', [
        ("Before choosing a therapist, get to know the strengths and pitfalls of their approach, including any modifications they make to the standard protocol. I'd especially want to interview them regarding how they treat spiritual experiences. You want someone who won't tell you what yours really mean, downplay them, force them, or treat them as a symptom. I'd also want one who doesn't put ideas in your head, and who understands dissociation. What have they found too challenging to deal with so far, and where have they seen the best results? A good therapist won't charge you an arm and a leg just for this kind of interview, and they should already have this information on their website to avoid wasting too much time. A certificate on the wall can't tell you any of that.",
         ["Get to know the strengths and pitfalls of their approach, including any modifications they make to the standard protocol. I'd especially want to interview them regarding how they treat spiritual experiences. You want someone who won't tell you what yours really mean, downplay them, force them, or treat them as a symptom. I'd also want one who doesn't put ideas in your head, and who understands dissociation. What have they found too challenging to deal with so far, and where have they seen the best results? A good therapist won't charge you an arm and a leg just for this kind of interview, and they should already have this information on their website to avoid wasting too much time. A certificate on the wall can't tell you any of that."]),
        ("Regarding AI therapy, I've tried all the top AI therapy apps, and they're all pretty bad. I'm trying to make my own based on this guide, but I'm becoming more convinced that unsupervised AI therapy is just a toss up. That doesn't mean you can't get a lot of great insights sometimes when talking to AI, though, but just expect it to go sideways sometimes.",
         ["I've tried all the top AI therapy apps, and they're all pretty bad. I'm trying to make my own based on this guide, but I'm becoming more convinced that unsupervised AI therapy is just a toss up. That doesn't mean you can't get a lot of great insights sometimes when talking to AI, though, but just expect it to go sideways sometimes."])]),
    'joel-101-20261023': ('H-borrow approved: "For warmth," and "For protecting," became headings', [
        ('For warmth, think of someone you remember fondly.', ['Think of someone you remember fondly.']),
        ('For protecting, ask what a minimally competent adult', ['Ask what a minimally competent adult'])]),
    'joel-105-20261024': ('H-escape approved: his first sentence became the heading "If you keep coming back from trips confused or spaced out", and the '
                          'paragraph splits before the medication warning, whose "And" goes', [
        ("Say you keep coming back from trips confused or spaced out. Maybe nothing worse happens, but after several trips like that I'd be concerned. If you're having episodes when you're sober, or any of them are severe, see a psychiatrist. And don't suddenly stop a medication just because you suspect it's involved. Talk to the doctor who prescribed it. Benzos can be dangerous to quit cold turkey. Alcohol withdrawal can be dangerous if you're physically dependent.",
         ["Maybe nothing worse happens, but after several trips like that I'd be concerned. If you're having episodes when you're sober, or any of them are severe, see a psychiatrist.",
          "Don't suddenly stop a medication just because you suspect it's involved. Talk to the doctor who prescribed it. Benzos can be dangerous to quit cold turkey. Alcohol withdrawal can be dangerous if you're physically dependent."])]),
    'joel-106-20261024-sections': ('H-change approved: the last paragraph splits before his condition, which is its heading', [
        ("Not wanting to do it anymore might be reason enough, but if that “nope” sounds like a part of you that’s trying to protect you, I’d hear it out first to get a better understanding. And if you keep following the reparenting steps correctly without getting the expected results, consider if you have a unique case these steps don’t match yet. Maybe you’ll find something that works better for you, or you can ask me what I’d do for this case, or ask a therapist you work with. Either way, I’d like to hear about it!",
         ["Not wanting to do it anymore might be reason enough, but if that “nope” sounds like a part of you that’s trying to protect you, I’d hear it out first to get a better understanding.",
          "Consider if you have a unique case these steps don’t match yet. Maybe you’ll find something that works better for you, or you can ask me what I’d do for this case, or ask a therapist you work with. Either way, I’d like to hear about it!"])]),
    'joel-112-20261025': ('W-solomon approved, his 109 A', [
        ("This [psychological trick](https://pubmed.ncbi.nlm.nih.gov/21728454/) has a rich history around it, and even has a name, [Solomon’s paradox](https://pubmed.ncbi.nlm.nih.gov/24916084/)",
         ["This [psychological trick](https://pubmed.ncbi.nlm.nih.gov/21728454/) has a rich history around it, and the blind spot behind it even has a name, [Solomon’s paradox](https://pubmed.ncbi.nlm.nih.gov/24916084/)"])]),
}


def swap(lst, old, news):
    out, hit = [], 0
    for s in lst:
        if s == old:
            out += news
            hit += 1
        elif old in s and len(news) == 1:
            out.append(s.replace(old, news[0]))
            hit += 1
        else:
            out.append(s)
    return out, hit


for eid, (why, pairs) in CHANGES.items():
    e = E[eid]
    for old, news in pairs:
        hits = 0
        for f in ('must_contain', 'must_contain_exact', 'order'):
            if f in e:
                e[f], h = swap(e[f], old, news)
                hits += h
        sp = e.get('span')
        if sp:
            for f in ('from', 'to'):
                if sp[f] == old:
                    sp[f] = news[0]
                    hits += 1
        assert hits, (eid, old[:60])
    e.setdefault('history', []).append('%s: %s, so the strings are the current ones (entry joel-114-20261026).' % (WHEN, why))

# the new entry: every case heading at its level, the paragraphs the splits start, the moved sentence, 109 A, his "you"
heads = ['#' * int(x['kind'][1]) + ' ' + x['md'] for r in SEC for x in r['new'] if x['kind'] != 'p']
assert len(heads) == 36, len(heads)
starts = [
    "Feeling calmer or having deeper insights or explanations for the trauma response are some possible signs of initial progress, but if that's the endgame, it's just a cope. Real healing is ultimately measured by reduced need for the therapy.",
    "It's like real parenting: you might start out reading parenting books and thinking hard about what to say or do, but after a while you get into the groove and a lot of it becomes natural. Inner parenting can be like that too. You don't need to keep checking this guide or planning every conversation with your little one; the nurturing, protecting and guiding become more automatic. You might still turn to therapy when you need it, and life will keep offering chances to grow wiser and more compassionate.",
    "And if the therapy is actually working, it should improve your daily life, and especially the health of the inner child-inner adult relationship. Going at it harder isn't as useful as going at it with more wisdom and compassion. Take the parts that work, and innovate on the rest.",
    "So a boundary can still be right. So can the law, if it comes to that, or telling them plainly it was wrong (or telling yourself, if they'd never hear it). Keeping away from them for good can be right too, and you can still forgive them from over there. Understanding somebody's limitations should make my expectations more realistic, not make those limitations less consequential. \"I understand how you became this way\" can sit right next to \"I now understand why I shouldn't rely on you for this.\"",
    "If you can’t clearly understand what happened yourself, get someone qualified to help. And if you have an idea of what happened but aren’t sure, ask someone who knows you well.",
    SAFE,
]
data['entries'].append({
    'id': 'joel-114-20261026',
    'status': 'applied',
    'what': 'His answers from the turn-113 review sheet: all eleven cards approved, each section as the sheet showed it (case headings, '
            'every one a ####; the first words a heading now says dropped; the splits; the one move in Start With Whatever Showed Up; '
            'his 109 A), and Q-me answered "you". Installed by experiments/t114-installs/apply_t114.py, which checks that the article '
            'without its notes is experiments/t113-shape/PROPOSAL-ARTICLE.md with his "you".',
    'joel': '2026-10-26 00:52 UTC (experiments/t114-answers/ANSWERS-20261026-0052.json; his message, experiments/t114-answers/JOEL-20261026-0053.md)',
    'where': ', '.join(r['heading'].lstrip('# ') for r in SEC) + "; Don't Give the Inner Adult Away",
    'must_have_line': heads + starts,
    'must_contain': [
        "If so just listen and be present for it if that's what it wants. How you picture all that is up to you, as long as it helps, and the simpler the better.",
        'has a rich history around it, and the blind spot behind it even has a name',
        'The test is whether the relationship makes you more grounded, truthful, and free.',
        'Repair it. Easier said than done, but',
    ],
    'must_not_contain': [
        "If nothing comes, that's fine for now", 'Your own drug history matters too', 'Say you keep coming back from trips',
        'Also easier said than done', 'makes me more grounded, truthful, and free', 'and even has a name, Solomon',
        'Regarding AI therapy,', 'And picturing one ideal parent', 'For warmth, think of someone', 'For protecting, ask what',
        'And don\'t suddenly stop a medication',
    ],
})
P.write_text(json.dumps(data, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('updated %d entries; added joel-114-20261026 (%d lines)' % (len(CHANGES), len(heads) + len(starts)))
if '--check' in sys.argv:
    pass
