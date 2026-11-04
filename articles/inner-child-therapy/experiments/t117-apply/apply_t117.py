#!/usr/bin/env python3
"""Turn 117: Joel's answers on the turn-116 marking page, put into his own reorganized guide, with the links and the post's
pictures and videos back.

  python3 articles/inner-child-therapy/experiments/t117-apply/apply_t117.py

In:  experiments/t116-joel/JOEL-GUIDE-20261103.md (his ODT of 2026-11-03 21:00 UTC as Markdown, his characters),
     experiments/t116-review/REVIEW.json (the 44 cards as the page showed them), experiments/t117-answers/
     ANSWERS-20261103-2332.json (his export of 23:32 UTC), experiments/t116-review/RELINK.json (where each lost link goes),
     experiments/t116-gate/G1..G6/FOR-JOEL.txt (the few words P1 to P6 add, admitted by the owner-delivery gate).
Out: GUIDE-APPLIED.md, installed as articles/inner-child-therapy/HUMANIZED-ARTICLE-SO-FAR.md, and CHANGES.json (every
     change: which card, the old and new text). verify_t117.py then checks each card's fate in the result.

Each change is an exact string of his file, found once and replaced once; the build stops otherwise. In order:
  1. the typos (T1 to T9, the 62 the cards listed, located by the words around each, the way the page found them);
  2. the cards he approved and his answers to the questions (P12 "on purpose", P13 his re-do in his words, A1 "change
     the other Xandria to X", A5 "fix it", F6 "libreoffice didn't have h5 available");
  3. the post's eleven pictures and videos, from the live post as it is today (L2 "yes keep all the embeds"; F2 "i hope
     you're not losing other embeds from the original"), his own two videos and six pictures (L3: the uncropped one), as
     notes on their own lines (IMAGE for a picture, EMBED for a video, an audio or a post card: article_images.py), so
     Pangram's text and the paragraph numbers skip them;
  4. the links (L1 "yes"): his typed ones made real, the fixes the card named, and the last guide's links back where his
     words and their sentence still are;
  5. Q1 "yes": English quote marks, and no space before ! ? : ; (a smiley's " :)" keeps its space);
  6. the standard typographic swap, in every article since 2026-11-03 (gate E337 (gut); Joel, 22:02 UTC: "yes make that
     swapping standard"): every curly quote mark straight, each em dash his spaced en dash (typography_swap.py).
"""
import difflib
import json
import pathlib
import re
import subprocess
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[4] / 'tools' / 'humanization'))
import typography_swap  # noqa: E402

HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parents[1]
ROOT = HERE.parents[3]
EXP = ART / 'experiments'
SRC = EXP / 't116-joel' / 'JOEL-GUIDE-20261103.md'
REVIEW = json.loads((EXP / 't116-review' / 'REVIEW.json').read_text(encoding='utf-8'))
ANSWERS = json.loads((EXP / 't117-answers' / 'ANSWERS-20261103-2332.json').read_text(encoding='utf-8'))
RELINK = json.loads((EXP / 't116-review' / 'RELINK.json').read_text(encoding='utf-8'))
CARDS = {s['id']: s for s in REVIEW['suggestions']}
HIS = {a['id']: a for a in ANSWERS['items']}
LAST_COMMIT = 'b3a1f54c'   # turn 114, the last guide before his reorganization (its dog paragraph, in his characters)
LAST = subprocess.run(['git', '-C', str(ROOT), 'show', LAST_COMMIT + ':articles/inner-child-therapy/HUMANIZED-ARTICLE-SO-FAR.md'],
                      capture_output=True, text=True, check=True).stdout


def typo_list():
    """The (words around it, old, new) list the T cards showed, from the page's build script."""
    src = (EXP / 't116-review' / 'build_review.py').read_text(encoding='utf-8')
    i = src.index('TYPOS = [')
    ns = {}
    exec(src[i:src.index('\n]\n', i) + 3], ns)
    return ns['TYPOS']


md = SRC.read_text(encoding='utf-8')
LOG = []


def N(s):
    """No-break spaces as spaces: one character for one, so offsets stay."""
    return s.replace('\xa0', ' ')


def rep(old, new, why, count=1):
    global md
    n = md.count(old)
    assert n == count, (why, old[:90], n)
    md = md.replace(old, new)
    LOG.append((why, old, new))


def gated(gid):
    return (EXP / 't116-gate' / gid / 'FOR-JOEL.txt').read_text(encoding='utf-8').strip()


# ---------------------------------------------------------------- 1. typos

def typos():
    global md
    for find, old, new in typo_list():
        mdn = N(md)
        if mdn.count(N(find)) == 1:
            # the old words are in the words around them, or just after ("borrowed adulthood trick" then "».,  The new")
            i = mdn.index(N(find))
            ws, we = max(0, i - 40), i + len(find) + len(old) + 40
            win = N(md[ws:we])
            assert win.count(N(old)) == 1, (find, old, win.count(N(old)))
            s = ws + win.index(N(old))
            md = md[:s] + new + md[s + len(old):]
        else:   # the page's words had a link inside them ("(along with spirituality) , but")
            assert md.count(old) == 1, ('typo not found once', find, old)
            md = md.replace(old, new)
        LOG.append(('typo (T1-T9)', old, new))
    rep('heal\xa0itself', 'heal itself', 'typo (T1: of its no-break space and space, a plain space)')
    rep('A**n** old', 'An old', 'typo (T1: the bold "n" its card named)')
    rep('free as a bird.** **And', 'free as a bird. And', 'typo (T1: the bold space its card named)')
    # one more of the kind T4 and T8 fixed, an opening quote mark the wrong way round, which the cards missed
    rep('On ne change pas—”we don’t change.”', 'On ne change pas—“we don’t change.”', 'typo (the kind T4 and T8 fixed; the cards missed this one)')


# ---------------------------------------------------------------- 2. the cards he approved, and his answers

DOG = re.search(r'\nSometimes it\'s not that you can\'t love in general\.[^\n]*\n', LAST).group(0).strip()
P13 = re.sub(r'^\s*oops\. ok it should say:\s*', '', HIS['P13']['comment']).rstrip()


def cards():
    global md
    rep('(as described in Noticing Counts)', '(%s)' % gated('G1'), 'P1')
    rep('avoidance of differentiation.', 'avoidance of differentiation %s.' % gated('G2'), 'P2')
    rep('that guard’s trust', gated('G3') + ' trust', 'P3')
    rep('That future you probably', gated('G4') + ' probably', 'P4')
    rep('future characters in your mind', 'future characters %s in your mind' % gated('G5'), 'P5')
    rep('stay curious about its motivations', 'stay curious about %s motivations' % gated('G6'), 'P6')
    # P7: the explanation, and its link, at the first mention
    rep('properly. Re-evaluation counseling always ends',
        'properly. [Re-evaluation Counseling](https://rc.org), a global movement of peer counseling, always ends', 'P7')
    rep('[Re-evaluation Counseling ](https://rc.org), a global movement of peer counseling, counts', 'Re-evaluation Counseling counts', 'P7')
    rep('I call it pl/ork\xa0!', 'I call it pl/ork (play + work)\xa0!', 'P8')
    rep('the deeper therapy pl/ork, play + work.', 'the deeper therapy pl/ork.', 'P8')
    rep('we ask the Adult Protector to start', 'we ask the Protector to start', 'P9')
    m = re.search(r'\n(#+ Borrow Your Love For Someone Else\n\n)(Or put somebody you care about)', md)
    assert m
    md = md[:m.start(2)] + DOG + '\n\n' + md[m.start(2):]
    LOG.append(('P10 (his paragraph from the last guide, %s, his straight apostrophes)' % LAST_COMMIT, '', DOG))
    rep('so my section, “meet the protector first,” would fit', 'so “meet the protector first” would fit', 'P12 (his answer: "on purpose")')
    rep('\nWhatever the situation was, we will contrast it with the corrected version.\n', '\n' + P13 + '\n', 'P13 (his words)')
    nairobi = ' She led a guided inner-child meditation in Nairobi in January 2026 for twenty people, and it’s up on YouTube.'
    rep(' Key developed the Guide’s sense of direction, and the identity and differentiation work from Bowen I mentioned earlier.'
        + nairobi, '', 'R1')
    rep('she added The Guide to make the 3 parental modes.', 'she added The Guide to make the 3 parental modes.' + nairobi, 'R1')
    rep(' So warmth and safety come first for a while, and the direction can grow once there’s a clear little one in there to guide.', '', 'R2')
    rep('never problems at all from up there, and', 'never problems at all, and', 'R3')
    rep('«\xa0punishment hug.\xa0» (which is called «\xa0therapeutic holding\xa0» in the literature) and I feel',
        '«\xa0punishment hug\xa0», and I feel', 'C1')
    rep('My ex, Xandria, taught me', 'My ex, X, taught me', 'A1 (his answer)')
    rep('like what century Pharaoh', 'like what year Pharaoh', 'A5 (his answer)')
    rep('\n### What to Make of a Passing Feeling\n', '\n## What to Make of a Passing Feeling\n', 'F3')
    rumi = CARDS['F4']['inserts'][0]['text']
    m = re.search(r'\n### Jelaluddin Rumi wrote: ‘The most secure place[^\n]*\n', md)
    assert m and md.count('Jelaluddin') == 1
    md = md[:m.start()] + ('\n<!-- PULL QUOTE: in Substack the next paragraph is a pull quote block (Joel, 2026-11-03 23:32 UTC, '
                           'on F4: "we can also add a \'pull quotes\' substack block code to quotes like this") -->\n\n'
                           + rumi + '\n') + md[m.end():]
    LOG.append(('F4 (the quote as the section\'s first paragraph, its quote marks closed; his pull quote)', m.group(0), rumi))
    rep('\n## 3. Finding People', '\n## Finding People', 'F5')
    rep('\n## 5. When One Life', '\n## When One Life', 'F5')
    rep('\n## 6. The Love Has to Move', '\n## The Love Has to Move', 'F5')
    rep('\nMo’ Money, Mo’ Problems\n', '\n##### Mo’ Money, Mo’ Problems\n', 'F6 (his answer: an h5)')
    rep('come along.\n\n## \n\n# Discovering', 'come along.\n\n# Discovering', 'the empty heading line (no words; it was on F2 with the video)')


# ---------------------------------------------------------------- 3. pictures and videos

S3 = 'https://substack-post-media.s3.amazonaws.com/public/images/'


def image(url, desc):
    return '<!-- IMAGE %s : %s -->' % (url, desc)


def embed(url, desc):
    return '<!-- EMBED %s : %s -->' % (url, desc)


NATIVES = [   # (the words just before, the note, why): the live post's eleven, in its order
    (None, image(S3 + '40c24f21-070c-4bc5-9333-c838b20d46dd_1122x1402.png',
                 'The post\'s top chart, "Inner Child Reparenting: Connect Today, Nurture Today, Heal Tomorrow" ("The child does '
                 'not heal itself. The present-day adult learns to relate, protect, and guide, when it is safe to do so."): what it '
                 'is, the goal, a practical healing path in five steps (orient and witness, borrow one adult function, adult '
                 'apprentice, build the inner adult, adult and child in relationship), practices that help, the adult functions '
                 'you build (Nurturer, Protector, Guide), when the adult is not yet safe, realistic reminders, a simple daily '
                 'practice, and a note on spiritual support'), 'the top chart, above the first line'),
    ('relaxing, and playing.\n\n', embed('substack-video:f302980e-0c6a-40c5-b6db-1e89ab887e3d',
                 'Céline Dion, "On ne change pas" (We don\'t change), the video Joel subtitled in English and uploaded to the post'),
     'the Céline Dion video, which "Céline’s right up there" points at'),
    ('desperate to be chosen.\n\n', embed('https://www.youtube.com/watch?v=4PxC3zZ2Mus',
                 'Rosey Grier, "It\'s All Right to Cry" (Free to Be... You and Me)'),
     'the Rosey Grier video, which "a little further down" points at'),
    ('as best as I can fit:\n\n.\n\n', image(S3 + '718d0e76-1acb-4c3c-8076-b9253317f15d_1122x1402.png',
                 'The study chart, "Inner Child Reparenting: The Study Chart" (practices, processes and supports for deep healing '
                 'and adult integration): practical tools that help (gentle self-hypnosis and meditation, journaling and dialogue, '
                 'somatic and trauma therapies, altered states and plant medicines, professional and relational support), '
                 'learning to feel love, when you can\'t feel like the adult yet, on forgiveness, enough adult capacity before '
                 'going deep, an adult-first safety gate, no clear child yet, catch the hook before you interpret it, also look '
                 'outward, and closing tenets'), 'the study chart, where his file had a lone "." (F1)'),
    ('Here’s a map of what to try when:\n\n', embed('https://ibogaqueen.substack.com/p/somatic-modalities-strategic-sequencing',
                 'Post card: "Somatic Therapy Modalities Map & Free Intro Sessions!"'), 'the somatic map post card'),
    ('#### Your Loan is PRE-APPROVED!\n\n', embed('https://www.youtube.com/shorts/4TYvq-d0-XM',
                 'A short from EndSickness.org, "Gratitude heals nervous system"'), 'the gratitude short, under its heading'),
    ('Inner Child’s Gift.\n\n', embed('https://ibogaqueen.substack.com/p/treasuring-the-inner-childs-gift',
                 'Post card: "Treasuring the Inner Child\'s Gift"'), 'the Treasuring post card (the L2 card missed it)'),
    ('For the Benefit of All Beings:\n\n', embed('https://www.youtube.com/watch?v=foHCbX0xjAU&t=58s',
                 'The Om Mani Padme Hum mantra from the Garchen Rinpoche documentary For the Benefit of All Beings, from 0:58'),
     'the mantra video (the L2 card missed it; the address is the one Joel gave on F2)'),
    ('open the envelope to find it!\n\n', image(S3 + 'c4ab39d5-554a-45ce-bc95-fa5f9846b58f_1122x1402.png',
                 'The "Cosmic Jackpot" picture: a slot machine reading HUMAN BIRTH (Dhamma available, can understand, free to '
                 'practice, potential awakening; incredibly rare), with too much pleasure (distraction and complacency) above, too '
                 'much suffering (fear, pain and confusion, no space to practice) below, and "just right" in the middle (a man on a '
                 'bench with his phone), the Buddha pointing up the path to Nibbana: "This human birth is like finding a tiny, '
                 'fertile island between two vast oceans. Don\'t waste the treasure."'), 'the Cosmic Jackpot picture (the L2 card missed it)'),
    ('into the core of my being.\n\n', image(S3 + '969adf28-c95f-4c96-bea8-3505a29137cc_638x786.jpeg',
                 'A dark black-and-white drawing of a gaunt, long-limbed creature crouched over a person asleep in bed ("Jinn Al '
                 'Kaboos, that attacks you while sleeping")'), 'the sleep-paralysis drawing, which "Yep. Exactly like that." answers'),
    ('and it’s up on YouTube.\n\n', embed('substack-audio:bc40d36b-6d3d-470d-a25d-14eb7eb067fb',
                 'Key\'s guided inner-child meditation in Nairobi, the audio uploaded to the post (41:56); in the post it followed '
                 'a line of the old intro that his guide no longer has, so it goes after Key\'s paragraph, which says it is up'),
     'Key\'s meditation, the post\'s audio (the L2 card missed it; its place is my choice)'),
]
HIS_PICTURES = [   # (his file's line, the note)
    ('[image 1](Pictures/10000000000006000000040091DBA79B.png)', image('odt:Pictures/10000000000006000000040091DBA79B.png',
        '"TL;DR: Don\'t Be Ashamed of Shame, a nuanced modern guide", seven panels (what shame is, shame can be healthy, but we '
        'can get stuck, the hidden weight, opening up helps, what doesn\'t help, healing is possible) and the bottom line: keep '
        'the moral signal, drop the self-condemnation')),
    ('[image 2](Pictures/10000001000002400000026F6724EE68.png)', image('laptop:/home/joel/Images/uncropped%20study%20on%20pain.png',
        'A screenshot, "Changing a threatening belief can produce unusually large pain improvements": a randomized trial of 151 '
        'people with primary chronic back pain testing Pain Reprocessing Therapy, and a bar chart of those reporting no or almost '
        'no pain at four weeks: 33 of 50 with pain reprocessing, 10 of 51 with open-label placebo, 5 of 50 with usual care '
        '(Joel\'s uncropped screenshot, 2026-11-03, in place of the cropped one)')),
    ('[image 3](Pictures/10000000000003B100000467B56DB2E6.jpg)', image('odt:Pictures/10000000000003B100000467B56DB2E6.jpg',
        'A meme: a man in an attic looking up at a small light, his hand on his heart, "Feeling relief when you realize the weird '
        'house noises are ghosts... and not something expensive you can\'t afford to fix is a different level of adulthood."')),
    ('[image 4](Pictures/10000000000004620000057A4F9C5370.png)  ', image('odt:Pictures/10000000000004620000057A4F9C5370.png',
        '"How This Reparenting Guide Differs From: Lucia Capacchione", six rows (the inner critic and the Critical Parent, the '
        'parts model, the Inner Adult, where to begin, the child\'s wisdom, emotion and illness) and the similarities: nurturing, '
        'protection, creativity, and an ongoing relationship with the inner child')),
    ('[image 5](Pictures/10000000000004620000057A5F00102A.png)', image('odt:Pictures/10000000000004620000057A5F00102A.png',
        '"How This Reparenting Guide Differs From: Schema Therapy", six rows (the inner critic, guards and coping modes, the '
        'Inner Adult and the Healthy Adult, where to begin, experience and interpretation, critic work) and the overlap: '
        'childhood wounds, reparenting, and helping a wiser adult self lead')),
    ('[image 6](Pictures/10000000000004620000057A547F4F79.png)', image('odt:Pictures/10000000000004620000057A547F4F79.png',
        '"How This Reparenting Guide Differs From: IFS", six rows (the inner critic, the Inner Parent and the Self, parts '
        'language, the Guide, everyday transfer, the spiritual level) and the overlap: compassion, curiosity, inner dialogue, '
        'and healing protective parts')),
]


def natives():
    global md
    for before, note, why in NATIVES:
        if before is None:
            assert md.startswith('# Understanding Reparenting\n')
            md = note + '\n\n' + md
            LOG.append(('L2: ' + why, '', note))
        elif before.endswith('\n\n.\n\n'):
            rep(before, before[:-3] + note + '\n\n', 'L2 and F1: ' + why)
        else:
            rep(before, before + note + '\n\n', 'L2: ' + why)
    rep('\nhttps://www.youtube.com/watch?v=qLfqA2igdUI&list=RDqLfqA2igdUI&start_radio=1\n',
        '\n' + embed('https://www.youtube.com/watch?v=qLfqA2igdUI', 'Eurythmics, "Sweet Dreams (Are Made of This)"') + '\n',
        'his video (the address without its playlist part)')
    rep('\n## https://www.youtube.com/watch?v=JQs2watlFws\n',
        '\n' + embed('https://www.youtube.com/watch?v=JQs2watlFws', '"Mantra healing practice is key for most people to heal"') + '\n',
        'his video where he put it, a line and not a heading (his answer on F2: "it\'s not a heading")')
    for line, note in HIS_PICTURES:
        rep('\n' + line + '\n', '\n' + note + '\n', 'his picture' + (' (L3: his uncropped screenshot)' if 'uncropped' in note else ''))


# ---------------------------------------------------------------- 4. links

FIX = {   # the card's fixes (relink.py's FIX)
    'shame.innerself.lovehttps://ibogaqueen.substack.com/p/dont-be-ashamed-of-shame-a-nuanced':
        'https://ibogaqueen.substack.com/p/dont-be-ashamed-of-shame-a-nuanced?utm_source=publication-search',
    '@KeyGoddess11': 'https://substack.com/@keygoddess11',
    'https://onlinelibrary.wiley.com/doi/10.1111/jftr.70049?af=R&utm_source=chatgpt.com': 'https://onlinelibrary.wiley.com/doi/10.1111/jftr.70049',
    'https://pmc.ncbi.nlm.nih.gov/articles/PMC12311821/?utm_source=chatgpt.com': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC12311821/',
    'https://www.youtube.com/watch?v=FyZI-VaVg2g&list=RDFyZI-VaVg2g&start_radio=1': 'https://www.youtube.com/watch?v=FyZI-VaVg2g',
}
URL_OF = {'spiritual bypassing': 'https://bypassing.u-dont-exist.com',   # the card: "gets your bypassing link"
          'Key': 'https://substack.com/@keygoddess11'}                     # the card: "Key goes to her Substack"
LINK_TARGET = re.compile(r'\]\((<?[^()\s]+(?:\([^()\s]*\))?[^()\s]*>?)\)')


def links():
    global md
    # his four typed in a form Markdown can't read
    rep('[[her institute still trains therapists](https://luciac.com/instructors.php)] (https://luciac.com/instructors.php)',
        '[her institute still trains therapists](https://luciac.com/instructors.php)', 'L1: the doubled link')
    n = 0
    for m in list(re.finditer(r'\[([^\[\]]+)\] \(<?([^()<>\s]+)>?\)', md))[::-1]:
        url = m.group(2) if re.match(r'https?://', m.group(2)) else 'https://' + m.group(2)
        md = md[:m.start()] + '[%s](%s)' % (m.group(1), url) + md[m.end():]
        LOG.append(('L1: a link typed with a space', m.group(0), '[%s](%s)' % (m.group(1), url)))
        n += 1
    assert n == 3, n

    def target(m):   # the fixes, and https:// on his bare addresses
        t = m.group(1).strip('<>')
        new = FIX.get(t, t)
        if not re.match(r'https?://|#|mailto:', new) and re.match(r'[a-z0-9-]+(\.[a-z0-9-]+)+(/|$)', new):
            new = 'https://' + new
        if new != m.group(1):
            LOG.append(('L1: ' + ('the card\'s fix' if t in FIX else 'https:// in front'), m.group(1), new))
        return '](%s)' % new
    md = LINK_TARGET.sub(target, md)
    # the last guide's links, where his words and their sentence still are
    back, skipped = 0, []
    for r in RELINK['base_links']:
        if r['action'] != 'restore':
            continue
        a, sent = r['text'], r.get('his_sentence') or ''
        url = URL_OF.get(a) or FIX.get(r['url'], r['url'])
        if not re.match(r'https?://', url):
            url = 'https://' + url
        cands = []
        for m in re.finditer(r'(?<!\w)%s(?!\w)' % re.escape(a), md):
            ls = md.rfind('\n', 0, m.start()) + 1
            le = md.find('\n', m.end())
            le = len(md) if le < 0 else le
            line = md[ls:le]
            if line.startswith(('#', '<!--')):
                continue
            pre = md[ls:m.start()]
            if pre.count('[') > pre.count(']') or re.search(r'\]\([^)]*$', pre) or md[m.end():m.end() + 2] == '](':
                continue   # inside a link already
            w = N(md[max(ls, m.start() - 2 * len(sent)):min(le, m.end() + 2 * len(sent))])
            w = re.sub(r'\]\([^)]*\)', '', w).replace('[', '')   # the links already back in the sentence
            sm = difflib.SequenceMatcher(None, N(sent), w, autojunk=False)
            score = sum(b.size for b in sm.get_matching_blocks()) / max(1, len(sent))
            cands.append((score, m.start(), m.end()))
        cands.sort(reverse=True)
        if not cands or cands[0][0] < 0.6:
            if '[%s](%s)' % (a, url) in md:
                LOG.append(('L1: already a link', a, url))
            else:
                skipped.append((a, url, sent, round(cands[0][0], 2) if cands else None))
            continue
        assert len(cands) == 1 or cands[0][0] - cands[1][0] >= 0.1, ('two places for a link', a, cands[:3])
        _, s0, e0 = cands[0]
        md = md[:s0] + '[%s](%s)' % (a, url) + md[e0:]
        LOG.append(('L1: the last guide\'s link back', a, url))
        back += 1
    return back, skipped


# ---------------------------------------------------------------- 5. Q1

def quotes():
    global md
    rep('**White Knight\xa0**:', '**White Knight**:', 'Q1 (the space before the colon was inside the bold)')
    rep('**Silent treatment\xa0**:', '**Silent treatment**:', 'Q1 (the space before the colon was inside the bold)')
    nq = md.count('«')
    md = re.sub(r'«[\xa0 ]?', '“', md)
    md = re.sub(r'[\xa0 ]?»', '”', md)
    ns = len(re.findall(r'\xa0(?=[!?:;])', md))
    md = re.sub(r'\xa0(?=[!?:;])', '', md)
    LOG.append(('Q1', '%d « » pairs' % nq, '%d no-break spaces before ! ? : ; taken out' % ns))
    assert '«' not in md and '»' not in md


def swap():
    global md
    md, n = typography_swap.swap_text(md)
    LOG.append(('the standard swap (E337 (gut))', '%d curly quote marks and em dashes' % n, 'straight marks, spaced en dashes'))


def main():
    typos()
    cards()
    natives()
    back, skipped = links()
    quotes()
    swap()
    head = ('<!-- Inner Child Therapy, humanized: Joel\'s own reorganized guide (his ODT of 2026-11-03 21:00 UTC, as Markdown in '
            'experiments/t116-joel/JOEL-GUIDE-20261103.md), with his answers on the turn-116 marking page put in, the links back, '
            'and the post\'s pictures and videos as notes (experiments/t117-apply/apply_t117.py, turn 117). It replaces the '
            'guide as of turn 114 (commit %s), whose paragraph notes and Pangram records stay in Git there. -->\n\n' % LAST_COMMIT)
    out = head + md.rstrip('\n') + '\n'
    (HERE / 'GUIDE-APPLIED.md').write_text(out, encoding='utf-8')
    inst = ART / 'HUMANIZED-ARTICLE-SO-FAR.md'
    if inst.exists() and "It's four pairs, starting with pleasure and pain" in inst.read_text(encoding='utf-8'):
        print('not installed: the article has moved on since turn 117 (turn 118 put the four pairs back); GUIDE-APPLIED.md written')
    else:
        inst.write_text(out, encoding='utf-8')
    (HERE / 'CHANGES.json').write_text(json.dumps([{'why': w, 'old': o, 'new': n} for w, o, n in LOG], ensure_ascii=False,
                                                  indent=1) + '\n', encoding='utf-8')
    words = len(re.sub(r'<!--.*?-->', '', out, flags=re.S).split())
    print('changes %d | links back %d | not placed %d | words %d' % (len(LOG), back, len(skipped), words))
    for s in skipped:
        print('  NOT PLACED', s)
    return 0


if __name__ == '__main__':
    sys.exit(main())
