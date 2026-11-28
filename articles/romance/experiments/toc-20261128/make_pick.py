#!/usr/bin/env python3
"""The proposed contents (the pick) for the romance article: every heading of CONTENTS-NOW.json at its current level and
place, named by one rule, read against tools/humanization/headings_brief.md and the readers of his contents and of
Fable's (SCORES.json, the reads' HARD lines):

  - his heading stays (capitals only, AP title case) when the sidebar shows it whole with room (not cut, not "tight")
    and no reader of its situation missed it and no more than one reader marked it hard;
  - otherwise it gets his own words cut down to fit, or, where that still hides the point or readers missed it, the
    question a reader comes with, in his words where the section has them.

Levels and places don't change here: those are questions for him on the page (PAGE-OPTIONS.json).

  python3 make_pick.py [PICK|PICK2|PICK3]   # PICK2: the second proposal, after the first one's readers; PICK3: the final

Writes PROPOSAL-PICK.json ([{id, level, heading, was, kind, why}] in the post's order, for the page and score_reads.py),
TOC-PICK-SIDEBAR.md and LINES-PICK.json (what fresh readers see). The readers' contents shows question 1's recommended
answer: the card-game link kept as a heading of its own above the opening, which gets "Who This Guide Is For" (line
"S002cta" in LINES-PICK.json, not a section of CONTENTS-NOW.json).
"""
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', '..', '..', '..', 'tools', 'humanization'))
import toc_sidebar as ts
from make_files import render

# id: (heading, kind, why). kind: fit = his is cut off or only just fits in the sidebar; reader = renamed for what
# readers look for (they missed it, or two of them marked it hard); case = capitals only; kept = his, as it is;
# retest = changed in the second proposal after the first one's readers.
PICK = {
    'S001': ('Ask an AI About This Guide', 'fit', "Yours is cut off and doesn't say it's a link to a chat about the guide. Fable's name. Question 1 asks whether it stays a heading."),
    'S002': ('Who This Guide Is For', 'reader', "This heading sits over your opening (your dad's answer, why you wrote it, who it's for), so the sidebar files the opening under the card game, and no reader looking for who the advice is for, or how sure you are of it, found it (0 of 5). With question 1's answer the card-game link stays a heading of its own just above, as you have it now."),
    'S003': ('What We Mean by "Love" ❤️', 'case', 'Capitals only.'),
    'S004': ('Talk Before You Make Love', 'fit', "Yours is cut off; the same advice, short enough. Fable's name."),
    'S005': ('Affection and the Simmer', 'case', 'Capitals only. Readers of the long-marriage situation found it.'),
    'S006': ('Is Casual Sex Honest?', 'fit', "Yours is cut off. \"Can Casual Sex Be Honest?\" only just fits, so it would likely lose its last letters in your browser. Fable's name."),
    'S007': ('Situationships', 'kept', ''),
    'S008': ('Labels Only Describe', 'fit', "Yours is cut off; your claim in three words. Fable's. Question 3 is about its last two paragraphs."),
    'S009': ('Should You Date at All?', 'fit', "Yours is cut off; your question, with \"date\" from your first lines (\"I would tell most of my friends not to date yet\")."),
    'S010': ('Not Ready, but Lucky', 'fit', "Yours is cut off; your words, shorter. Fable's name."),
    'S011': ('Spiritual Bypassing', 'fit', "Yours is cut off. Your \"spirituality\" and \"bypass\", as the name readers know for it."),
    'S012': ('Practical Partnerships', 'case', 'Capitals only.'),
    'S013': ('Loved, or Just Useful?', 'reader', "Two readers of yours said \"It always goes deeper\" names no subject. The section's question in your words: \"how much does she love me vs how much does she love what I can do for her?\" Fable's name."),
    'S014': ('Beyond Sex Appeal', 'reader', "No reader of yours found it when the partner is ill and sex is no longer possible (0 of 3); both readers of Fable's did. From your line \"sex appeal isn't the basis of the relationship anymore\". Readers of the proposals often clicked its parent first, then it; the reader's question itself, if you'd rather (fits, not tested): \"Love Without Sex?\"."),
    'S015': ('How to Find a Partner', 'case', 'Capitals only.'),
    'S016': ('Long Distance', 'case', 'Capitals only.'),
    'S017': ('Dating App Horror Show', 'kept', ''),
    'S018': ('Meet in Community', 'fit', "Yours is cut off; \"Community Makes Matches\" is too. Fable's name."),
    'S019': ('The Missing Middle', 'kept', "Kept: your coinage, which the section's own text uses (\"the missing middle I'm talking about\"), and 4 of 5 readers found it. Fable's other idea: \"Between Interest and Sex\". Question 5 is about where it sits."),
    'S020': ('Starting on the Right Foot', 'case', 'Capitals only.'),
    'S021': ('The Window of Clarity', 'fit', "Yours is cut off; your phrase, which the next sections pick up (\"Before the window of clarity closes\"). Fable's name."),
    'S022': ('Are You Compatible?', 'fit', "Yours only just fits, so it would likely lose its last letters in your browser. Your first line's question (\"find out whether you are actually compatible\"). Fable's name."),
    'S023': ('The Flaws Conversation', 'fit', 'Yours is cut off; your words, turned round to fit.'),
    'S024': ('My Flaws', 'case', 'Capitals only.'),
    'S025': ('Keep an Outside View', 'reader', "A reader said \"Things get tricky fast\" doesn't say what gets tricky, and all three readers of yours looking for whether to move in together clicked it. The section's point: couples withdraw just when they need a view from outside. Fable's name."),
    'S026': ('Beware Idealization', 'fit', 'Yours is cut off; without "in either direction" it fits.'),
    'S027': ('Anti-PTSD Is Risky Too', 'fit', "Yours is cut off before its point shows. Keeps your coinage and your claim. Fable's name."),
    'S028': ('Seeing Idealization Right', 'case', "Capitals only. \"De-ontologizing\" names it in its text (\"what I said in Seeing idealization right\"), so the name staying saves a change there."),
    'S029': ('If Slow Isn\'t Realistic', 'fit', 'Yours only just fits; without "for You" it fits with room.'),
    'S030': ('Birth Control for Men', 'reader', "A reader said \"Just in case\" doesn't say in case of what. The section is about a contraceptive herb for men. Fable's name."),
    'S031': ('Wait to Move In Together', 'reader', "No reader of yours found it when the person you've slept with for a few weeks suggests moving in (0 of 3: all three went to \"Things get tricky fast\"); both readers of Fable's did. Fable's name."),
    'S032': ('What if the Sex Is Bad?', 'fit', "Yours is cut off after \"Slow & steady may…\", and its child started the same way. The section's question. Fable's (capitals: AP lower-cases \"if\")."),
    'S033': ('Sexual Fit Can Grow', 'fit', "Yours is cut off, and read the same as its parent once cut. The section's answer (Bee: \"You're going to get a lot better at sex\"). Fable's name."),
    'S034': ('The Relationship as Crucible', 'case', 'Capitals only.'),
    'S035': ('From Flow to Nitty Gritty', 'case', 'Capitals only.'),
    'S036': ('Reverting to Babyhood', 'case', 'Capitals only.'),
    'S037': ('Not Your Whole World', 'fit', 'Yours is cut off; your words, shorter.'),
    'S038': ('Disconnect to Connect', 'case', 'Capitals only.'),
    'S039': ('Growing Up Again', 'reader', "Readers said \"Reverting to babyhood\" and \"Babies growing up again\" blur together. Your words without \"Babies\". Fable's name."),
    'S040': ('Lover or Therapist?', 'reader', "No reader found it, with yours or with Fable's \"When One Is the Adult\", when the girlfriend says she feels like his patient (0 of 5: all went to \"Reverting to babyhood\"). The section is about one partner always being \"the therapist, guru, doctor, or dad\"."),
    'S041': ('Ahead in Different Ways', 'fit', 'Yours is cut off; your claim (different levels in different domains) in four words.'),
    'S042': ('Primal Attraction & Polarity', 'fit', "Yours is cut off before its point. Keeps \"Primal Attraction\", the words your opening uses for it (\"The Primal Attraction section is the exception\"). Fable's name."),
    'S043': ('Muses & Directors', 'kept', ''),
    'S044': ('His Desire, Her Desire', 'fit', "Yours is cut off. Fable's name."),
    'S045': ('No Need to Prove It', 'reader', "Yours is cut off, and a reader called \"Adjudicated\" jargon. Your point: \"The moment I have to prove that I'm the man, something has already become fake\", and women shouldn't have to prove their femininity either. Fable's: \"Invite Roles, Don't Demand\"."),
    'S046': ('Fantasy', 'kept', ''),
    'S047': ('The Queen of Orgasms', 'kept', ''),
    'S048': ('Is Making Love Spiritual?', 'fit', "Yours is cut off. Your question with \"making love\", the words you define at the start (Fable's \"Sex as a Spiritual Practice?\" uses \"sex\", which you keep for the physical act)."),
    'S049': ('Twin Flames?', 'kept', ''),
    'S050': ('My Two Twin Flames', 'fit', "Yours is cut off; your words, shorter. Fable's \"What My Two Taught Me\" didn't say two what."),
    'S051': ('De-ontologizing FTW 💗', 'fit', "Yours is cut off; your coinage, without \"Twin Flames\", which its parent says. Readers found it either way. Fable's other idea: \"An Energy, Not a Person\"."),
    'S052': ('Who Holds a Couple Up?', 'reader', "Three readers said \"Two Pillars\" doesn't say pillars of what, and it's cut off. Your roof, as the question the section answers: a couple needs other people around it. Fable's \"A Couple Needs Community\" echoed \"Meet in Community\"."),
    'S053': ('What "Together" Means', 'fit', "Yours is cut off. Your first lines' question (\"When we say, 'We're together,' what does that mean exactly?\"). Fable's \"What Are You Choosing?\" was too open for both its readers."),
    'S054': ('Which Vows Are Honest?', 'fit', "Yours is cut off. Fable's name."),
    'S055': ('Attraction and Exclusivity', 'case', 'Capitals only.'),
    'S056': ('Jealousy on Trial', 'case', 'Capitals only. Question 4 is about its second half.'),
    'S057': ('Conscious Tools 🧭', 'reader', "Readers said \"Doing it consciously\" doesn't say what \"it\" is or what's under it: imagining the hard parts, psychedelics, the objection that it's artificial. Keeps your \"consciously\" and your compass."),
    'S058': ('Imagine the Hard Parts', 'fit', 'Yours is cut off; what the exercise is.'),
    'S059': ('Psychedelic Timing', 'kept', ''),
    'S060': ('Getting Unstuck', 'fit', 'Yours is cut off; your words.'),
    'S061': ('Did the Therapy Work?', 'reader', "A reader asked \"benefits of what?\". Your test: \"I would say the therapy worked if a week or two later...\""),
    'S062': ('Why This Sounds Artificial', 'fit', 'Yours is cut off; without "all of".'),
    'S063': ('If You\'re Already in It', 'case', 'Capitals only.'),
    'S064': ('Get Outside Help Early', 'fit', "Yours is cut off. Your point: \"don't think of outside help as a formal last resort\". Fable's name."),
    'S065': ('What Will Honesty Do?', 'fit', "Yours only just fits, so it would likely lose its last letters in your browser. The same question. Fable's name."),
    'S066': ('Children', 'kept', ''),
    'S067': ('Should You Leave?', 'reader', "Readers of yours and of Fable's \"Ending Consciously\" looking for whether to leave or try counseling went to \"If you're already in it\" first (4 of 5). Your first line: \"settle whether you're leaving, and whether counseling is worth trying first\"."),
    'S068': ('Gaslighting in the Dark', 'case', 'Capitals only. All three readers of yours found it.'),
    'S069': ('After Leaving', 'case', 'Capitals only.'),
    'S070': ('What I Gained From Loss', 'case', 'Capitals only.'),
    'S071': ('Tough Love', 'kept', "Kept: every reader looking for why a marriage ending isn't a private failure found it (5 of 5), though they all said the name doesn't say what's in it. Fable's other idea, which avoids the idiom's meaning (being strict for someone's good): \"Love Is Tough\"."),
}
# The second proposal: four headings changed after both readers of the first marked each one hard (reads/READ-PICK-1.md,
# READ-PICK-2.md), each with the readers' words.
PICK2 = {
    'S039': ('Reparent Yourself', 'retest', "Both readers of the first proposal couldn't tell \"Growing Up Again\" from \"Reverting to Babyhood\" (nor could readers of yours and Fable's). Your point: \"Inner-child reparenting means parenting the child part instead of surreptitiously hiring the partner for the job.\""),
    'S050': ('Can You Have Two?', 'retest', "\"My Two Twin Flames\" (first proposal) repeated its parent \"Twin Flames?\" on the line above, a reader said. Your own question in the section: \"How could it be possible to fall in love with a different woman? I thought Bee was my forever, only Twin.\""),
    'S052': ('A Couple Needs a Village', 'retest', "Both readers of the first proposal said \"Who Holds a Couple Up?\" could be about friends, community, kids or money; three readers of yours said \"Two Pillars\" doesn't say pillars of what. Your point: a couple is \"left alone inside something that needed other people around it\". Fable's \"A Couple Needs Community\" echoed \"Meet in Community\"."),
    'S057': ('Psychedelics & Other Tools', 'retest', "Both readers of the first proposal said \"Conscious Tools 🧭\" hides what's in it, as readers of yours and of Fable's said of theirs; one said psychedelics show nowhere at the top level. Your compass doesn't fit with these words."),
}
CTA = {'id': 'S002cta', 'level': 1, 'heading': 'Try My Couples Card Game', 'words': 0}   # question 1's recommended answer


# The third (final) proposal: the second with S039 back to "Growing Up Again". With "Reparent Yourself", both readers
# of the second proposal looking for somewhere else to take a wife's pain (situation 21) went to the wrong section
# first, one of them to "Reparent Yourself"; with "Growing Up Again" both readers of the first proposal went to the
# right one ("Disconnect to Connect"). Readers called "Growing Up Again" hard to tell from "Reverting to Babyhood",
# but none clicked it by mistake.
PICK3 = {k: v for k, v in PICK2.items() if k != 'S039'}


def main(version='PICK'):
    picks = dict(PICK, **{'PICK2': PICK2, 'PICK3': PICK3}.get(version, {}))
    now = json.load(open(os.path.join(HERE, 'CONTENTS-NOW.json'), encoding='utf-8'))
    assert [e['id'] for e in now] == sorted(picks), 'every heading needs a pick'
    out, bad = [], []
    for e in now:
        h, kind, why = picks[e['id']]
        if kind in ('case', 'kept'):
            assert h.lower() == e['heading'].lower() or kind == 'case', (e['id'], h)
        st = ts.status(h, e['level'])
        if st != 'fits':
            bad.append((e['id'], st, h))
        out.append({'id': e['id'], 'level': e['level'], 'heading': h, 'was': e['heading'], 'kind': kind, 'why': why})
    json.dump(out, open(os.path.join(HERE, 'PROPOSAL-%s.json' % version), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    words = {e['id']: e['words'] for e in now}
    read = []
    for e in out:
        if e['id'] == 'S002':
            read.append(dict(CTA))
        read.append({'id': e['id'], 'level': e['level'], 'heading': e['heading'], 'words': words[e['id']]})
    side, nums = render(read, 'Contents as the sidebar shows it', True)
    open(os.path.join(HERE, 'TOC-%s-SIDEBAR.md' % version), 'w', encoding='utf-8').write(side)
    json.dump(nums, open(os.path.join(HERE, 'LINES-%s.json' % version), 'w'), indent=0)
    print(version + ': %d headings, %d changed, %d not fitting with room: %s' % (
        len(out), sum(e['heading'] != e['was'] for e in out), len(bad), bad))


if __name__ == '__main__':
    main(*sys.argv[1:])
