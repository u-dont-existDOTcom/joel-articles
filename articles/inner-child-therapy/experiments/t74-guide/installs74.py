# Turn 74 installs (registered with register(name, old, new); see t74.py). Joel's message of 2026-10-19 00:08 UTC
# (experiments/t74-answers/JOEL-20261019-0008.md).

SAID74 = 'his message of 2026-10-19 00:08 UTC (experiments/t74-answers/JOEL-20261019-0008.md)'


def note(text):
    return '<!-- Turn 74 (%s): %s -->\n\n' % (SAID74, text)


def joelfile(stem):
    return (T / (stem + '.txt')).read_text(encoding='utf-8').strip()


def jpara(start):
    """His pasted paragraph (experiments/t74-guide/joel-before-you-try-20261019-0008.txt) that starts with START."""
    return next(b.strip() for b in re.split(r'\n\s*\n', joelfile('joel-before-you-try-20261019-0008')) if b.strip().startswith(start))


def block_with_comment(start):
    """The article's paragraph starting with START, with the install comments right above it and the blank lines
    after it: the exact text to cut when a paragraph goes. None once it's gone."""
    t = ART.read_text(encoding='utf-8')
    p = para(start)
    if p is None:
        return None
    j = t.index(p)
    i = j
    while True:   # take in the comment lines (and the blank lines between them) right above the paragraph
        k = t.rfind('\n\n', 0, i - 1)
        prev = t[k + 2:i].strip() if k >= 0 else ''
        if prev.startswith('<!--') and prev.endswith('-->') and '\n' not in prev:
            i = k + 2
            continue
        break
    end = j + len(p)
    while t[end:end + 1] == '\n':
        end += 1
    return t[i:end]


# --- 62, C ("it's human now, i fixed it, pasted"): his Before You Try to Go Deep, as he pasted it ------------------------
JBG = ('62, C ("it\'s human now, i fixed it, pasted"): his Before You Try to Go Deep as he pasted it at 00:08 UTC; this paragraph is his version (experiments/t74-guide/joel-before-you-try-20261019-0008.txt).')
register('jbg', lambda: para('So how were the next few days?'),
         lambda: note(JBG + ' It is turn 72\'s P5 h, with the guide\'s list of what to change in it and "change several things at once" out (54, 8 and 11). @@JBG@@') + jpara('So how were the next few days?'))
register('jbg', lambda: para('Going back can still matter, since realizations'),
         lambda: note(JBG + ' It has 55, 2, A in fewer words.') + jpara('Going back can still matter'))
register('jbg', lambda: para("And the checking doesn't always stay in your head."),
         lambda: note(JBG + ' His own fix of the opening that kept a 37-word AI window (question 62), word for word, his comma after "Even" included.') + jpara("And the checking doesn't always stay in your head."))

# --- His new h1 before the Appendix, in place of the Appendix's three therapist paragraphs --------------------------------
FAT_H = '# Finding a Therapist to Borrow Adulthood'
FAT = [
    "We all need some support, especially when taking our first steps. First and easiest is to start with finding a somatic therapist, if that resonates, as per my [Somatic Therapies Guide](http://somatic.u-dont-exist.com/).",
    "Inner Child Reparenting therapists do exist, and you can find them, although they often are not licensed, and I don't know of any central directory, nor of any protocol they'd have in common. There are none which work with my guide yet. I can consult, and if you like the guide, you can ask a therapist to check it out and see what they agree with or disagree with as a great way to vet them.",
    "The best licensed, listed therapists you'll find that come close will be doing Internal Family Systems (IFS), or Schema Therapy. I'll talk more about those next, but Schema Therapy comes closest to my approach. [Open Path Collective](https://openpathcollective.org/pricing-and-eligibility-for-affordable-therapy/) (or a similar resource in your country) lists thousands of affordable therapists. You can filter them by Schema or IFS. You can often find [even more Schema therapists at the official site](https://schematherapysociety.org/Search?&tab=1).",
    "Before choosing a therapist, get to know the strengths and pitfalls of their approach, including any modifications they make to the standard protocol. I'd especially want to interview them regarding how they treat spiritual experiences. You want someone who won't tell you what yours really mean, downplay them, force them, or treat them as a symptom. What have they found too challenging to deal with so far, and where have they seen the best results? A good therapist won't charge you an arm and a leg just for this kind of interview, and they should already have this information on their website to avoid wasting too much time. A certificate on the wall can't tell you any of that.",
    "Regarding AI therapy, I've tried all the top AI therapy apps, and they're all pretty bad. I'm trying to make my own based on this guide, but I'm becoming more convinced that unsupervised AI therapy is just a toss up. That doesn't mean you can't get a lot of great insights sometimes when talking to AI, though, but just expect it to go sideways sometimes.",
]
FAT_NOTE = note('his new h1 ("Let\'s combine the 3 appendix paragraphs on finding a therapist into a new h1 before Appendix, called: "Finding a Therapist to Borrow Adulthood""), his five paragraphs word for word. Fitted: his Somatic Therapies Guide link gets its http:// (as everywhere else in the article), and the two links of his 2026-10-18 19:06 text (Open Path Collective, and the official site\'s search) stay on the same words. It replaces the Appendix\'s three therapist paragraphs: How This Relates to Schema Therapy P3 (turn 73), How This Relates to IFS P8 (turn 71) and Teachers and Practice Resources P3 (his of 2026-10-18). @@FAT@@')
register('fat', lambda: '\n# Appendix\n' if FAT_H not in ART.read_text(encoding='utf-8') else None,
         lambda: '\n' + FAT_H + '\n\n' + FAT_NOTE + '\n\n'.join(FAT) + '\n\n# Appendix\n')
register('fat', lambda: block_with_comment('So how do you find a good one?'), '')
register('fat', lambda: block_with_comment('Before choosing a therapist, get to know the strengths and pitfalls of IFS'), '')
register('fat', lambda: block_with_comment("I don't know of a resource to find a perfect inner child therapist"), '')

# --- His IFS cut, and Related Clinical Work as an h2 ---------------------------------------------------------------------
UNB = ' Then there\'s "unburdening," often done after you\'ve witnessed a part\'s origin story. It can be powerful, sure. It can also get dramatic, all memories and plenty of room for suggestion, which can knock you off balance, especially if you tend to dissociate (DID-like fragmentation included) or to spiritually bypass.'
register('unb', lambda: (lambda p: p if p and UNB in p else None)(para('IFS calls these wounded young parts')),
         lambda: note('his cut ("remove this part from the original guide, because it doesn\'t make sense, not clear, not explaining anything exactly, and i don\'t see how unburdening is so diff from my approach aside from the weird terminology and exact protocols"): the unburdening sentences are out.') + para('IFS calls these wounded young parts').replace(UNB, ''))
register('rcw2', lambda: '\n### Related Clinical Work\n' if '\n### Related Clinical Work\n' in ART.read_text(encoding='utf-8') else None,
         '\n## Related Clinical Work\n')
