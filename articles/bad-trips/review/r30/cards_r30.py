# The cards of round 30, read by build_r30.py (which defines P, PALL, T, whole, span_of, cut_block, cut_words,
# replace_words and card). Round 30 answers his round-28 comments of 2026-11-09 17:22 UTC: the table of contents first
# (HELPER-NOW: "make sure the ToC is optimized then we can make sure the stuff in each section is what belongs there
# rather than merging or moving?"), shown as each option would really look, with how sure I am (METHOD-WHERE: "keep in
# mind how confident you are ... make sure i'm able to see the options and how theyh would really look"), and his Syrian
# rue oil and relaxing-herbs notes put where they belong (RUE-SAFETY: "Make sure that is in the sections it needs to be
# in."). What the contents reads found: articles/bad-trips/humanize/h39-20261109/toc/RESULTS.md. What I could check of
# the Syrian rue points: articles/bad-trips/humanize/h39-20261109/RUE.md.

import pathlib as _pl
import re as _re

BUILT = '2026-11-09'
H39 = BLOB + 'articles/bad-trips/humanize/h39-20261109/'
TOCDIR = REPO / 'articles/bad-trips/humanize/h39-20261109/toc'
COMMENT = 'his own: his RUE-SAFETY comment on round 28 (2026-11-09 17:16 UTC)'
NB = '\u00a0'

RUE_P1 = ("Syrian rue (*Peganum harmala*) can be mixed into warm/hot oil (like coconut oil), just enough to cover it, then "
          "squeezed out thru cheese cloth. Within some minutes of the seeds soaking in oil (if it's hot, or maybe an hour if "
          "it's warm), the oil contains the oil-soluble harmalas, not harmine, harmaline, or THH in quantities that could "
          "make it a potent MAOI. In my experience there's no MAOI effect in Syrian rue extracted with oil (it won't "
          "activate DMT, rather it reduces DMT's effects). These oil-soluble harmalas have no effect when eaten, but when "
          "absorbed thru mucous membranes or vaped, they chill out psychedelic trip intensity, making them more gentle and "
          "sweet. On their own, they have some mild psychedelic properties though (like I felt like half of my head was "
          "sort of transparent), and significant mood boosting properties.")
RUE_P2 = ("I have a friend with schizophrenia who would use about 1-2mL of this oil rectally when he was in psychosis, which "
          "helped at least as much as niacin and DMSO, equally effective as Geodon, an antipsychotic his doctors prescribed "
          "which makes him feel like a zombie.")
RUE_P3 = ("Another option is vaping the whole Syrian rue seeds, as it seems that these oil soluble harmalas are concentrated "
          "on the outside of the seeds. Once ground up, vaping the powder is more stimulating, less relaxing (but variable "
          "since all is mixed together). However, if vaping the whole seeds, I would not assume there's no MAOI effect "
          "(even though it still seems to reduce DMT effects) since depending maybe on temperature and time, you might also "
          "vaporize the harmine and harmaline.")
RUE_WARN = (REPO / 'articles/bad-trips/review/r30/RUE-WARN.txt').read_text(encoding='utf-8').strip()
OILS_P = ("If you don't have the Metta NMT sniffer, just use AUTHENTIC natural calming essential oils to smell, like rose "
          "geranium, jasmine, lemon/lime oils. Most of these oils are fake on Amazon so buy only directly from trusted "
          "essential oil vendors. It should not smell like a perfume. Even just taking a lime and scratch & sniff the peel "
          "can be relaxing.")
HERBS_OLD = "I'd still go for my trusty relaxing herbs and natural antipsychotics listed above first."
HERBS_NEW = ("I'd still go for my trusty relaxing herbs first, like beach morning glory, Syrian rue oil or the Metta NMT "
             "sniffer, and natural antipsychotics like DMSO and niacin.")
TOC_RESULT = ("On the contents as it is, the two readers guessed on 6 and 5 of the 16, and both would have stopped at beach "
              "morning glory and missed niacin when they wanted the trip to end. On A, a third reader guessed on 4, and its "
              "first pick was right for all 16")
TOC_ADVICE = ("A. How sure I am of each part: sure of the remedies part and of who to call being in one place at the top, "
              "since both readers found those on their own; fairly sure of splitting the psychological part and giving the "
              "days after and the next session parts of their own, since one reader proposed them and the other's guesses "
              "point the same way; least sure of moving the brain section to the end of the medical part, since leading with "
              "it may be your choice (say \"A, but keep the brain section first\" if so). The guesses left on A come from "
              "three headings, not the order: \"Give the Session a Beginning and an End\" doesn't say it's for planning, "
              "\"Hang up the phone\" says nothing until you read the section, and harm is answered in three places. A later "
              "card can rename those, if you want.")


NOTES_A = {
    'Who to Contact, and When': 'moved here from Get One Human Anchor',
    'Active Seizure': 'the emergencies come first now',
    'If Someone Says "My Brain Feels Damaged": DMSO + Humic Acid First': 'moved to the end of the medical part, '
                                                                          'leading into the remedies',
    'My Acute Rescue Hierarchy of Remedies': '"of Remedies" added',
    'How I label the evidence': 'no longer the parent of every remedy',
    'Some Remedies Require More Caution': 'moved before the remedies',
    'Gut-Toxin and Parasite-Die-Off Tools': 'each remedy group one level up',
    'Authentic Calming Essential Oils (or a Lime Peel)': 'new: your notes, card OILS',
    'DMSO': 'moved next to humic acid',
    'Syrian Rue Oil Makes the Trip Gentle & Sweet': 'new: your notes, card RUE-OIL',
    'When the Goal Is to Stop a Psychedelic Trip': 'now after the stabilizers, gentlest to strongest',
    'A Final Trip Killer: Niacin (a Form of Vitamin B3)': 'your two headings joined',
    'Tripsitting Yourself or Others': 'your part heading split in two; your greeting still opens it',
    'Grounding Menu: Choose One or Two Things': 'moved up, next to first aid',
    'Shadow Work': 'the other half of your part heading',
    'Dealing With Sorrow: Missing Versus Sending Love': 'the hard-content sections, before the reflective ones',
    '(Re)defining "Bad Trip"': 'the reflective sections, after the hard content',
    'After the Storm': 'a part of its own',
    'Bring in mental-health support when:': 'moved here from the top, right after the aftermath list',
    'Hang up the phone, get off the Healing Treadmill': 'moved here',
    'Give the Session a Beginning and an End': 'a part of its own, for next time',
}
NOTES_B = {k: NOTES_A[k] for k in ('Who to Contact, and When', 'My Acute Rescue Hierarchy of Remedies',
                                   'How I label the evidence', 'Some Remedies Require More Caution',
                                   'Gut-Toxin and Parasite-Die-Off Tools', 'When the Goal Is to Stop a Psychedelic Trip',
                                   'A Final Trip Killer: Niacin (a Form of Vitamin B3)')}


def contents(name, notes, upto=None):
    """The contents file as he'd see it: each heading indented by its level, with what changed beside it."""
    out = []
    for line in (TOCDIR / name).read_text(encoding='utf-8').splitlines():
        m = _re.match(r'^ *(#+) (.*?)  \(\d+ words?\)$', line)
        if not m:
            continue
        t = m.group(2).replace('*', '')
        if upto and t == upto:
            out.append('(the rest as it is now)')
            break
        note = notes.get(t)
        out.append(NB * 4 * (len(m.group(1)) - 1) + t + ('   [%s]' % note if note else ''))
    return '\n'.join(out)


INTRO = [
    'Round 30 (2026-11-09). Rounds 28 and 29 are in: both typos fixed, the three terms explained in your aftermath list '
    'with Somatic Experiencing linked to your guide, and the Fear/Panic Loop section cut as you meant in round 27, its '
    'picture moved with the loop into your first five minutes. "MAOI" is now explained where the guide first uses it, in '
    'the call-medics list.',
    'You asked for the contents first, so the first card is the table of contents, with each option shown as it would '
    'read. Where your aftermath kinds go and what the helper section is for both follow from it, and your method in the '
    'parts people use in trouble comes once the contents is settled, one card per place, each shown in place. The other '
    'four cards put your Syrian rue oil and relaxing-herbs notes where they belong: your words in two new entries and in '
    'your aftermath line, and one caution of mine to approve or reject.',
]

card(id='TOC', type='structure', advice='ask', title='1. The table of contents: which one?',
     question=('Three fresh readers read only the contents, with 16 situations a reader comes with (a friend shaking and '
               'not responding, a week later the world still feels unreal, planning a ceremony), and said where they\'d '
               'look first. %s ([what each reader found](%stoc/RESULTS.md)).\n\n'
               'A (my pick):\n%s\n\n'
               'Pro: who to call is in one place at the top; the emergencies come first; the remedies run from the evidence '
               'key and the cautions to the gentlest and then the strongest; the psychological part is two short parts, what '
               'to do in the moment and the shadow work; the days after and the next session each have a part of their own. '
               'Con: the biggest change to the order your post has, and the brain section no longer leads the medical part.'
               '\n\nB (only what both readers found broken):\n%s\n\n'
               'Pro: fixes the remedies part and who to call, and nothing else moves. Con: the psychological part stays one '
               'run of 17 sections with the days after at the end of it, and "Bring in mental-health support when:" stays '
               'at the top, away from the aftermath list.\n\n'
               'C: leave the contents as it is.') % (TOC_RESULT, H39, contents('TOC-A.md', NOTES_A),
                                                      contents('TOC-B.md', NOTES_B, upto='Shadow Work and Tripsitting Yourself or Others')),
     why=('You asked to settle the contents before anything else moves. Two of round 28\'s questions, where the aftermath '
          'kinds go and what the helper section is for, depend on it: with A, "Bring in mental-health support when:" sits '
          'right after the aftermath list, which you said would make moving paranoia and derealization there an easy choice.'),
     stays=('The guide keeps its order until you answer; the other cards work with A, B or C. Nothing in any section is '
            'reworded: A and B move sections and change heading levels, and every heading is the guide\'s own but for "of '
            'Remedies", "A Final Trip Killer" joined with "Niacin", and your part heading split in two.'),
     advice_note=TOC_ADVICE,
     spans=[whole(P('B65'))])

card(id='RUE-OIL', type='notes', advice='approve', title='Syrian rue oil: your notes as a new entry under Mental Stabilizers',
     whose=COMMENT,
     owner_text=('his own: his RUE-SAFETY comment and the Syrian rue sentence of his AFT-HOW-MUCH comment (2026-11-09), with '
                 'typos fixed and the hexane aside left out; the heading in his style, from his "more gentle and sweet"'),
     what=('A new entry after DMSO, in your words from your comment: what the oil is and how you make it, what it does, your '
           'friend\'s experience, and vaping the whole seeds. Typos fixed ("would would", "an DMSO", "MAOi"); "(*Peganum '
           'harmala*)" added after the first "Syrian rue", so a reader knows the plant; and from your comment on the '
           'aftermath card, "In my experience there\'s no MAOI effect in Syrian rue extracted with oil (it won\'t activate '
           'DMT, rather it reduces DMT\'s effects)." Left out: "(unless one extracts with hexane and then eats a 1-2tbsp of '
           'that extract)".'),
     why=('Your aftermath list names "syrian rue OIL" among the natural antipsychotics "mentioned in this guide", and the '
          'guide never said what it is. After DMSO, because DMSO\'s interactions already talk about harmalas. The hexane '
          'aside is a method and an amount for a strong MAOI extract, which a reader looking for a calming oil doesn\'t '
          'need; the next card says what to keep away from instead.'),
     stays='Everything else under Mental Stabilizers, and your paranoia line, which now has the oil it names.',
     deciding='Approve puts the entry in; Revise to change any of it, or to put the hexane aside back.',
     advice_note='Approve.',
     ask_because='his own: your comment on round 28, placed as a new entry',
     found_by='your answer on round 28\'s RUE-SAFETY card',
     inserts=[{'before': P('B208'), 'kind': 'h4', 'seq': 1, 'text': 'Syrian Rue Oil Makes the Trip Gentle & Sweet',
               'whose': 'in your style, from your words "more gentle and sweet"'},
              {'before': P('B208'), 'kind': 'p', 'seq': 2, 'text': RUE_P1},
              {'before': P('B208'), 'kind': 'p', 'seq': 3, 'text': RUE_P2},
              {'before': P('B208'), 'kind': 'p', 'seq': 4, 'text': RUE_P3}],
     spans=[whole(P('B207', 1))])

card(id='RUE-WARN', type='safety', advice='approve', title='Syrian rue oil: what to keep it away from',
     what='One paragraph of mine after your entry: "%s"' % RUE_WARN,
     why=('Your entry says the oil carries little harmine or harmaline, and that vaped whole seeds might carry more. I '
          'couldn\'t confirm or rule out the oil part: the studies of the seeds\' oil I found measured its fatty acids, not '
          'its alkaloids, and a traditional Syrian rue oil tested in a 2015 trial was "standardized by high-performance '
          'liquid chromatography", which for this plant usually means harmine and harmaline, though I couldn\'t open the '
          'full paper to see how much ([what I checked](%sRUE.md)). Harmine is among the plant\'s volatile compounds too, '
          'which fits your caution about vaping. The guide\'s serotonin section already lists harmala exposure among the '
          'things to stop. And your friend\'s story compares the oil with Geodon, so someone in psychosis who reads it '
          'needs to know not to drop a prescription on its strength.') % H39,
     stays='Your entry as you wrote it; this goes after it.',
     deciding='Approve puts the caution in; Reject leaves your entry to stand alone.',
     advice_note='Approve: it keeps your remedy with what a reader on medication needs to use it safely.',
     ask_because='downside: it says to treat the oil as a possible MAOI, which is more careful than your experience of it',
     found_by='a needed read of the paragraph by a fresh reader (both sentences needed), and my check of the oil point',
     inserts=[{'before': P('B208'), 'kind': 'p', 'seq': 5, 'text': RUE_WARN}],
     spans=[whole(P('B207', 2))],
     receipt='articles/bad-trips/review/r30/RUE-WARN.receipt.json')

card(id='OILS', type='notes', advice='approve', title='Authentic calming essential oils: your notes as a new entry',
     whose=COMMENT,
     owner_text='his own: the essential-oils lines of his RUE-SAFETY comment (2026-11-09), placed after humic acid',
     what=('A new entry after Humic Acid Brings Brain to Optimal Function, in your words: "%s" Changed from your comment: '
           '"if they don\'t have that" to "If you don\'t have the Metta NMT sniffer", so it reads on its own, and "amazon" to '
           '"Amazon".') % OILS_P,
     why=('You named them as relaxing remedies for when there\'s no sniffer, and the guide doesn\'t have them. After humic '
          'acid rather than right after the sniffer, because the sniffer paragraph ends on "it works also very well:", '
          'which your Humic Acid heading completes.'),
     stays='The sniffer and humic acid entries, and the rest of the stabilizers.',
     deciding='Approve puts the entry in; Revise to change it.',
     advice_note='Approve.',
     ask_because='his own: your comment on round 28, placed as a new entry',
     found_by='your answer on round 28\'s RUE-SAFETY card',
     inserts=[{'before': P('B185'), 'kind': 'h4', 'seq': 1, 'text': 'Authentic Calming Essential Oils (or a Lime Peel)',
               'whose': 'in your style, from your words "AUTHENTIC natural calming essential oils" and the lime peel'},
              {'before': P('B185'), 'kind': 'p', 'seq': 2, 'text': OILS_P}],
     spans=[whole(P('B184'))])

card(id='HERBS-NAMED', type='notes', advice='approve',
     title='What Kind of Aftermath Is This?: the relaxing herbs named',
     whose='his own: his aftermath list (round 27) and the herbs he named in his RUE-SAFETY comment (2026-11-09)',
     owner_text='his own: the herbs he named in his RUE-SAFETY comment, in the line of his aftermath list that points to them',
     what=('"I\'d still go for my trusty relaxing herbs and natural antipsychotics listed above first." becomes "%s"'
           % HERBS_NEW),
     why=('No herbs were listed above that line. These are the ones you named, and DMSO and niacin are the natural '
          'antipsychotics your paranoia line names; each has its entry in the remedies part.'),
     stays='The rest of your restlessness line, word for word.',
     deciding='Approve names them; Revise to name them differently.',
     advice_note='Approve.',
     ask_because='his own: your aftermath line, with the herbs from your comment',
     found_by='round 28\'s RUE-SAFETY card, and your answer to it',
     edits=[replace_words(P('B426', 7), HERBS_OLD, HERBS_NEW)],
     spans=[span_of(P('B426', 7), HERBS_OLD)])
