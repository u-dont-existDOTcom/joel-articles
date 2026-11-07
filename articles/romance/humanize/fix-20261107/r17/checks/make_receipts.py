#!/usr/bin/env python3
"""Making-sense receipts (gate E365) for r17's checks (texts.py). Every sentence has its row: the live post's sentences
as well as mine (gate E373). A sentence an earlier receipt in this article already has a row for keeps that row (the
spots' best tries, S11, S12, S13 and S20, and "Situationships"); the rest are written here, in the order the text has them.
Writes CHECK-<name>.txt and RECEIPT-<name>.json and checks each; exits 1 if one fails."""
import glob
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[5]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import sense_receipt as S  # noqa: E402
from texts import TEXTS  # noqa: E402

OLD = {}
for f in sorted(glob.glob(str(ROOT / 'articles' / 'romance' / 'humanize' / '**' / 'RECEIPT-*.json'), recursive=True)):
    if '/r17/' in f:
        continue
    for s in json.load(open(f, encoding='utf-8')).get('sentences', []):
        if s.get('s') and s.get('payoff'):
            OLD[s['s'].strip()] = (s['payoff'], s['follows'], s.get('link'))

NEW = {
    'r17-babies': [
        ('some gap in maturity is normal, but the extremes get out of hand', 'opens the section', None),
        ('when one is always the child and the other always the helper, it is too unequal and swings back',
         'what the extremes look like', 'What I noticed in all of my most intimate relationships'),
        ('always being the responsible one made him to blame for everything, with clinginess and jealousy on top',
         'his own case of it', 'When I became consistently the responsible one'),
        ('Toft warns she is neither a girl nor his mother', 'another voice on it', 'Toft says'),
        ('he agrees but qualifies "she’s not a girl"', 'his view of Toft', 'I agree with the warning'),
        ('many women enjoy a daddy/little-girl side with a man they trust, and he wouldn’t deny them it',
         'why he qualifies it', 'A lot of women enjoy'),
        ('that side can be affectionate, erotic, comforting or playful', 'what it can be like', 'It can be affectionate'),
        None, None, None, None, None,
        ('all three women said they felt like his patient, and he couldn’t argue', 'what happened in his case',
         'All three women told me'),
        ('they asked him about nearly every kind of problem', 'why they felt that way', 'They asked me about almost every'),
        ('one kind of question was about being sick', 'an example of it', 'I’m sick'),
        ('they wanted him to say what to take', 'the question they asked', 'What should I take'),
        ('another kind was about being sad', 'a second example', 'I’m sad'),
        ('they wanted him to say what to do', 'the question they asked', 'What should I do'),
        ('he usually answered, but enough moments like that become a pattern', 'what he did and what it led to',
         'I usually had some idea'),
        ('Key once asked him to be her guru', 'a story about it', 'Key at first asked me'),
        ('he declined and offered to learn from each other instead', 'his answer to her', 'I told her'),
        ('months later she said she was far more advanced than him', 'what came next', 'A few months later'),
        ('he reminded her she had asked him to be her guru', 'his reply to that', 'I asked'),
        ('she said she must have been confused back then', 'her answer, the swing back', 'She said'),
        None, None, None, None, None, None, None,
    ],
    'r17-levels': [
        ('by his own account he was ahead of Bee, Key and H. in maturity and self-awareness', 'opens the section', None),
        ('he also had a happier childhood and more money', 'his other advantages', 'I also had advantages'),
        ('all of that tilted the balance between them', 'what it did to them', 'all of that affected the balance'),
        ('they were ahead in wonder and intuition, which attracted him', 'where they were ahead', 'They were all ahead of me'),
        ('their intuition was sometimes wrong, but he loved it, being analytical himself', 'his view of it',
         'Sometimes their intuition was wrong'),
        ('they were all more social than him', 'another way they were ahead', 'They were also all more social'),
        ('they could easily gather people for a ceremony', 'what that looked like', 'They could organize people'),
        ('he felt he needed that for a commune, being introverted', 'why it mattered to him', 'I felt like I needed that'),
        ('he talks well with people when there is a purpose', 'what he can do', 'I’m good at talking to people'),
        ('he is worse at rousing people, since he thinks everyone should do as they please', 'what he does less well',
         'I’m not as good at rousing'),
        ('so he believes partners can coach and complete each other', 'what he concludes', 'So I do believe'),
        None, None, None,
        ('bring in other support once one partner is the caregiver and that is taken for granted, or the romance may '
         'collapse', 'when it stops being healthy', 'It’s time to bring in other support'),
        ('then the romance may need less intensity, become friendship, or end', 'what may follow',
         'Maybe the romance actually does need'),
        ('asking that question out loud is where it starts, though he can’t answer it for others', 'where to begin',
         'Asking the question out loud'),
    ],
    'r17-choosing': [
        ('much romantic pain starts when a couple enters a big arrangement without talking it over', 'opens the section',
         None),
        ('"we’re together" can mean many things', 'an example of it', 'what does that mean exactly'),
        ('he hears a whole future in those two words', 'what he hears in it', 'I can hear a whole future'),
        ('she might only mean "let’s see what happens"', 'what she might mean', 'She might mean'),
        ('he likes leaving parts unnamed; the trouble is the same words for two futures', 'where the problem is',
         'but the problem is when'),
        ('sometimes a couple wants something practical', 'another kind of couple', 'Sometimes what two people want'),
        ('they want a home, children and support without pretending it rests on overwhelming love', 'what they want',
         'They want to share a home'),
        ('he calls that a practical partnership', 'what he calls it', 'I’d call that'),
        ('that is fine if both of them know it', 'his view of it', 'if both people know'),
        ('he suspects they have never been in love', 'his doubt about it', 'But I suspect'),
        ('that becomes a problem if one of them falls for someone', 'when it goes wrong', 'if they ever do fall for someone'),
        ('another honest option is a romance with humility', 'a third option', 'Another honest option'),
        ('a couple in love can build a life together as long as nobody pretends to guarantee future feelings',
         'what that looks like', 'Two people really are in love'),
        None, None, None, None, None, None, None, None,
        ('these questions are a start, and the reader can add their own', 'what to do with the questions',
         'These are just a few questions'),
        ('they can make a card game of it', 'a way to use them', 'You can make a card game'),
        ('real love survives some honest curiosity', 'why not to fear it', 'If there’s real love'),
        ('community makes all of this less scary', 'a last reassurance', 'community can make all of this'),
    ],
    'r17-artificial': [
        ('he admits all this sounds artificial', 'opens the section', None),
        ('he asks whether anyone will really do all these practices', 'why it sounds artificial',
         'Is anyone actually going to do'),
        ('he answers his own question', 'his answer to it', 'Well, yeah'),
        ('it is painfully artificial', 'what he concedes', 'It is painfully artificial'),
        ('a communal society would give the couple witnesses, elders and outlets', 'why it is artificial',
         'In a healthy communal society'),
        ('without that, we rebuild some of it clumsily, with a checklist', 'what we do instead', 'Most of us these days'),
        ('the article is mostly about what to do before falling in', 'a turn to those already in', 'Most of this article'),
        ('for the married with children, advice about slowing down comes late', 'who it doesn’t help',
         'But if you’re already married'),
        ('he has no special method for that', 'what he can offer', 'I wish I had a special method'),
        ('one person can’t fix the relationship unless they are its main problem', 'what he learned', 'Mostly I learned'),
        ('with Bee and Key the core issue was trust', 'his own case', 'With Bee and Key'),
        ('they said they trusted him but trusted no one', 'what the trust problem was', 'They wanted to be with me'),
        ('their trust was all or nothing', 'the shape of it', 'It was all or nothing'),
        ('he kept saying a relationship needs trust', 'what he said to them', 'I kept saying'),
        ('he thinks the rigidity came from trauma', 'where it came from', 'I think that rigidity'),
        ('even dishonesty was hard to define with them', 'a related problem', 'Even dishonesty was sometimes hard'),
        ('Bee once denied opening a door a second after she did', 'an example of it', 'Bee once opened a door'),
        ('that drove him crazy', 'his reaction to it', 'That drove me crazy'),
        ('he couldn’t see why she would lie', 'his question about it', 'Why would she lie'),
        ('"she lied" named only the moment', 'what the word missed', 'only named the momentary behavior'),
        ('there was no strategy, and she was usually honest', 'why the word missed it', 'There was no strategy behind it'),
        ('he could have seen it as illness rather than strategy', 'what he sees now', 'Looking back'),
        ('they acted as if trust was fine because they wanted the relationship', 'a plainer kind of it',
         'Some things were less mysterious'),
        ('attractions went unsaid, or got imagined', 'another thing kept hidden', 'Attractions to other people'),
        ('some keep such a relationship going for years by hiding everything', 'how long it can last',
         'Some people keep a relationship'),
        ('he was sometimes more honest than his partner could handle', 'the other side of it', 'On the other hand'),
        ('ask first whether both want radical honesty', 'what to do about it', 'Ask whether both of you'),
        ('"not now" forever won’t save the relationship', 'the limit on that', 'But the other person also'),
        ('agape may mean letting go of the pattern they first committed to', 'what love asks then',
         'This is the time for agape'),
        ('he asks when the couple last danced', 'a test of it', 'When did you two last dance'),
        ('he means real dancing, not dancing around problems', 'what he means by it', 'we dance around our problems'),
        ('if they only dance around problems, the trust is gone', 'what that means', 'the trust is out the window'),
        ('that hurts', 'his reaction to it', 'Ouch'),
        ('he knows it from his first two wives and K', 'his experience of it', 'I know that one from experience'),
        ('that marks the point of no return, so don’t wait for it', 'why it matters', 'the point of no return'),
        ('past it, resentment snowballs and they feel colder together than alone', 'why there is no return',
         'Because once you’re there'),
        ('then they start looking at other people', 'what comes next', 'Pretty soon'),
    ],
    'r17-gaslight': [
        ('he asks whether the reader has memories that can’t be reconciled', 'opens the section', None),
        ('he did, with his first two wives', 'his own case', 'I did with both'),
        ('he took Ann to two counselors', 'what he tried', 'I took my first wife'),
        ('one counselor told them to split for six months', 'what came of it', 'The male counselor'),
        ('opposite memories of the same event can’t be resolved', 'why it couldn’t be fixed', 'There’s no way to resolve'),
        ('they had no neutral friends to corroborate', 'what was missing', 'We also didn’t have mutual friends'),
        ('he disagrees with keeping it private', 'his view on it', 'Many say it’s best'),
        ('without friends who can help, you are stuck', 'why he disagrees', 'If you don’t have friends'),
        ('involve friends honestly, to help, not to win approval', 'how to do it', 'But do it honestly'),
        ('both should get to speak, and friends should hear both first', 'what fairness takes',
         'Both people should get a chance'),
        ('he can believe a friend and still admit he can’t know', 'his own practice', 'I can believe a friend’s experience'),
        ('he trusts people more who admit they lack evidence', 'why he does that', 'I trust their thinking more'),
        ('community helps because friends would hear more than two stories', 'what would help',
         'Living in community would help'),
        ('friends would see how the couple argue', 'what they would see', 'Sometimes they would actually see'),
        ('don’t abandon someone in a crisis, except in three cases', 'a limit on leaving', 'don’t abandon them in a crisis'),
        ('arranging other care is no reason to pretend the romance has a future', 'what staying means',
         'You may need to arrange other care'),
    ],
}
# Sentences whose old rows opened a check by themselves and so had no link, now inside the section: a whole row, or the
# link alone (the old row's payoff and follows kept).
OVERRIDE = {'It can go either way': ('either side can keep it undefined, but often it is the man, since she risks pregnancy',
                                     'who keeps it undefined', 'often the man wants to keep it undefined'),
            'The problem is when the role takes over': 'The problem is when the role takes over',
            'I also have to admit, I can become condescending': 'I also have to admit',
            'I could teach these women': 'I could teach these women',
            'Then the questions change for me.': 'Then the questions change',
            'I had something sort of like that with H.': ('he had something like it with H., deeper than most but painfully '
                                                          'uneven', 'his own case of it', 'something sort of like that')}
META = {
    'r17-sit': ('Situationships',
                'Someone in a relationship that is mostly sex and has no name, deciding whether to ask what it is.',
                'It tells the reader what a situationship is, the kind they may be in.'),
    'r17-babies': ('Some babies grow up faster',
                   'Someone whose partner keeps turning to them as a parent or a doctor, wondering when that is too much.',
                   'It tells the reader when a gap in maturity gets out of hand.'),
    'r17-levels': ('Different levels in different domains can be complementary',
                   'Someone whose partner is ahead in some things and behind in others, wondering whether that can work.',
                   'It tells the reader a gap can be complementary, and when it stops being healthy.'),
    'r17-choosing': ('What are you actually choosing together?',
                     'A couple about to commit or move in, who haven’t said what each of them means by it.',
                     'It tells the reader to say what "together" means before committing.'),
    'r17-artificial': ('Why all of this sounds artificial',
                       'Someone already married with children, wondering whether any of this still applies to them.',
                       'It tells the reader why this feels artificial, and what is left if they are already in.'),
    'r17-gaslight': ('Gaslighting in the dark',
                     'Someone whose memory of key events contradicts their partner’s, with nobody neutral to ask.',
                     'It tells the reader what to do when two memories can’t be reconciled.'),
}
Q = {
    'Q1': 'PASS: each changed sentence gives its point first, in plain words',
    'Q2': 'N/A: these sections tell and ask; the advice in them is unchanged',
    'Q3': 'PASS: the people, places, numbers and things are named as in the live post',
    'Q4': 'PASS: no new term; "practical partnership" and "agape" are used as the live post uses them',
    'Q5': 'PASS: each sentence’s tie is in its words (the links field), or the link says why it needs none',
    'Q6': 'PASS: the order is the live post’s; the joins named in texts.py keep it',
    'Q7': 'PASS: each change keeps what the section tells the reader about their own case',
    'Q8': 'PASS: no item moved between groups',
    'Q9': 'PASS: one step per sentence in the changed paragraphs',
}
LOW = [{'point': 'the Low windows’ points', 'found': 'the live post (../../live-check/LOW-WINDOWS.json) and the last part’s '
        'check (#47, ../../r07/checks/RESULTS-r07.json)', 'still_needed': 'yes: the section needs them', 'fate': 'changed'}]
bad = 0
for name, text in TEXTS.items():
    section, reader, why = META[name]
    r = S.make(text, section, reader)
    new = NEW.get(name, [None] * len(r['sentences']))
    assert len(new) == len(r['sentences']), (name, len(new), len(r['sentences']))
    for s, row in zip(r['sentences'], new):
        if row is None:
            ov = next((v for k, v in OVERRIDE.items() if s['s'].startswith(k)), None)
            row = OLD[s['s'].strip()] if ov is None or isinstance(ov, str) else ov
            if isinstance(ov, str):
                row = (row[0], row[1], ov)
        pay, fol, link = row
        s['payoff'] = pay if pay.startswith('the reader learns ') else 'the reader learns ' + pay
        s['follows'] = fol
        if 'link' in s:
            s['link'] = link
    r['opens']['why_reading'] = why
    r['same_point'] = 'none: read the section from its heading to the next for these points; each is made once, here'
    r['questions'] = dict(Q)
    r['checked'] = LOW
    r['placement'] = 'The whole section, in its place in the live post, its heading left out.'
    (HERE / ('CHECK-%s.txt' % name)).write_text(text, encoding='utf-8')
    (HERE / ('RECEIPT-%s.json' % name)).write_text(json.dumps(r, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    probs = S.check(text, r)
    bad += bool(probs)
    print(name, 'PASS' if not probs else probs)
sys.exit(1 if bad else 0)
