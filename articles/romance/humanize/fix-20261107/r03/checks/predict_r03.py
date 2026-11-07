#!/usr/bin/env python3
"""r03's predictions, written before the checks (pangram_ledger.py predict, one per text in texts.py)."""
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[5]
LEDGER = ROOT / 'articles' / 'romance' / 'humanize' / 'pangram-ledger.jsonl'
REL = 'articles/romance/humanize/fix-20261107/r03/checks/'
DET = 'pangram 4.1, the web app (Joel\'s account, GUI credits)'
PANEL = 'articles/romance/humanize/fix-20261107/r03/panel-s2/PANEL.md'
BACK = ('the r02 try rewrote his sentences into new set pieces and read worse than the live post; this try goes back to '
        'the live post\'s words and changes only the sentences in its windows, so most of r02\'s words go')
P = {
    'r03-s2b': dict(lineage='romance-s2', scope='pair', call='AI', chance=0.4,
                    tells='the robes as the subject of "get you"; a closing general line ("Most of us have more than one '
                          'reason ...")',
                    human='his "Venerable Somebody", "Why wouldn’t it?", the bowing picture; "free room and board", '
                          '"nobody expects you to"',
                    diag='Tries 1 and 2 (#2, #6) read AI High on the perks and West sentences; both readers of the tell '
                         'panel agreed on the four-item perks list and on the balanced closing pair ("He can still ... He '
                         'can also ..."). Every try so far kept the list "free food, a place to live, status, and a way out '
                         'of ordinary responsibilities".',
                    first='payoff: the opener says why people choose robes before the perks; join: room and board joined, '
                          'and the West sentence keeps its "but"; plain: "free room and board", "status", "nobody expects '
                          'you to earn a living or raise a family" for "escape from ordinary responsibilities"',
                    hum='the perks list broken into a pair of things you get and a thing nobody expects of you; the closing '
                        'pair no longer mirrors itself (a concession, then the general point said about big choices)',
                    big='both earlier tries kept the four-item list the panel agreed on; this one rebuilds the perks '
                        'sentence and the closing pair, so most of try 2\'s words change',
                    panel=True),
    'r03-s2c': dict(lineage='romance-s2', scope='pair', call='AI', chance=0.4,
                    tells='a concession opener ("Of course, plenty of monks ..."); the robes as the subject of "get you"',
                    human='his "Venerable Somebody", "Why wouldn’t it?", "People can want several things at once", the '
                          'bowing picture',
                    diag='As for 2b: the perks list and the balanced closing pair, agreed by the panel. 2c tests the other '
                         'cause the panel named, the build (claim, list, example, balanced closer): the concession goes '
                         'first and the paragraph ends on his picture.',
                    first='payoff: the concession and his general point come first, so the perks read as the other half; '
                          'join: his two closing sentences become one paragraph with the perks; plain: as in 2b',
                    hum='the closing pair is gone: the concession leads, and the paragraph ends on "suddenly people are bowing to him"',
                    big='the closing pair moves to the front and the perks sentence is rebuilt, so most of try 2\'s words '
                        'change',
                    panel=True),
    'r03-s6': dict(lineage='romance-s6', scope='pair', call='Human', chance=0.5,
                   tells='"I just think we need some stage that ..." still states a need in general terms',
                   human='his whole first paragraph; "didn’t exactly solve the problem"; the 30–40 percent figure',
                   diag='Try 1 (#7) read AI on every sentence of my second paragraph (High on the quip "So much for keeping '
                        'courtship nonsexual." and on the need sentence); the live post read AI Low on "It sounds a lot '
                        'like the missing middle" and on "It also didn’t exactly solve the problem", Medium on the '
                        '"coexisted with" sentence and High on the last two.',
                   first='payoff: the missing middle joins the sentence that describes it; join: that sentence; plain: '
                         '"where lots of couples bundled" for "coexisted with", "moving in together" for "cohabitation", '
                         '"some stage that everybody recognizes" for "some socially recognized way"',
                   hum='"Well," opens the turn; the need is said as what he thinks, after he says he isn’t asking for '
                       'bundling back, with no "but we do need"',
                   big=BACK),
    'r03-s7': dict(lineage='romance-s7', scope='pair', call='Human', chance=0.5,
                   tells='three short questions after a statement',
                   human='his questions about the last conflict; "me included"; his two questions about shutting down',
                   diag='Try 1 (#8) read AI Medium on the friends-and-exes sentence (a general truth tacked on as a '
                        'reason) and AI on the shut-down questions (High on "okay, but what does that look like?"); the '
                        'live post read AI High on the friends sentence and Medium on "okay, what does that mean?".',
                   first='payoff: the reason now says he is one of the people it is about; join: none needed; plain: '
                         '"Nobody’s a great judge of their own progress" for "people aren’t always the best judges"',
                   hum='the reason is its own sentence and includes him ("me included"); "I ask what that means" says what '
                       'he does instead of acting out the question',
                   big=BACK),
    'r03-s8': dict(lineage='romance-s8', scope='pair', call='Human', chance=0.55,
                   tells='three thoughts in a row after "like"',
                   human='his first sentence, unchanged (Human in the live post); "lost in the sauce"',
                   diag='Try 1 (#9) changed his first sentence (it fell from Human to Human Low) and kept the dashed aside '
                        '(AI Medium). In the live post only the dashed sentence read AI (Low): an aside of three thoughts '
                        'sits between "once you start identifying" and what happens then.',
                   first='payoff: "You’re already lost in the sauce" comes first; join: the three thoughts follow with '
                         '"like" instead of standing between dashes; plain: his words',
                   hum='his first sentence back as the live post has it; the aside moved after the point, as self-talk',
                   big=BACK),
    'r03-s10': dict(lineage='romance-s10', scope='pair', call='Human', chance=0.5,
                    tells='"Otherwise I end up ..." could read as a stock turn',
                    human='Toft’s sentence and his reply; the quoted outburst; "it can easily sound like"',
                    diag='Try 1 (#11) read AI Medium on my contrast frame ("not something I suddenly announce when ..."); '
                         'the live post read AI Low on "I’d rather make alone time normal than wait until ...", a '
                         'comparison frame of 35 words.',
                    first='payoff: "I’d rather make alone time normal from the start" is said first, by itself; join: the '
                          'outburst and what it sounds like become one sentence with "and by then"; plain: his words',
                    hum='the comparison frame split into what he would do and what happens otherwise, in his words',
                    big=BACK),
    'r03-s11': dict(lineage='romance-s11', scope='pair', call='AI', chance=0.45,
                    tells='the four-item list of what she would do for him',
                    human='his sentences about the role; "It can run the other way too."; "made her Mom"',
                    diag='Try 1 (#12) read AI Low on my if-sentence (three jobs in an if-then); the live post read AI '
                         'Medium on his if-then with four jobs. This try tests the point-first fix alone.',
                    first='payoff: "I make her Mom" comes first; join: none; plain: his words',
                    hum='the if-then turned so the point leads and the conditions follow',
                    big=BACK),
    'r03-s14': dict(lineage='romance-s14', scope='pair', call='Human', chance=0.6,
                    tells='a closing question',
                    human='his two paragraphs before it, unchanged; "tale as old as time"',
                    diag='The live post read AI Low on "The real question is whether polarity stays alive inside the '
                         'safety." (11 words): a staging frame ("The real question is") ahead of the point.',
                    first='payoff: the question itself, with no frame before it; join: "So" ties it to what came before; '
                          'plain: "can a couple keep the polarity alive" for "whether polarity stays alive"',
                    hum='the staging frame becomes the question the section has been asking'),
    'r03-s15': dict(lineage='romance-s15', scope='pair', call='Human', chance=0.55,
                    tells='a because-clause carrying the consequence',
                    human='his next paragraph, unchanged ("I cry, I need help, I get things wrong", Bee’s "wife")',
                    diag='The live post read AI Low on "The moment I have to prove that I’m the man, something has already '
                         'become fake." and AI Medium on "Then I have to defend the identity every time I hesitate, cry, '
                         'need help, or get something wrong.", a stock "The moment X" opener and a list his next paragraph '
                         'says again.',
                    first='payoff: the point stays first ("If I have to prove I’m the man, something’s already fake"); '
                          'join: the two sentences become one with "because then"; plain: "If I have to" for "The moment I '
                          'have to", "slip up" for the list his next paragraph repeats',
                    hum='the stock opener gone; the repeated list cut to what the next paragraph doesn’t say'),
    'r03-s16': dict(lineage='romance-s16', scope='stretch', call='Human', chance=0.5,
                    tells='"So someone with ..." could read as a tidy example; a "not X" turn in the last sentence',
                    human='Perel’s distinction as he put it; "the actual woman and the actual experience"',
                    diag='The live post read AI Low on "A rape fantasy is not a request to be raped in real life.", AI High '
                         'on "The couple can leave it in imagination or agree to bring some part of it into the room." and '
                         'AI Low on "Fantasy should also add to arousal rather than become the only possible route to it.": '
                         'a definition restated, abstract verbs ("leave it in imagination", "bring ... into the room"), and '
                         'a rather-than frame.',
                    first='payoff: the rape-fantasy line becomes what the distinction means ("So"); join: the arousal '
                          'sentence and his reason become one with "because"; plain: "keep a fantasy in their heads", "act '
                          'some part of it out", "isn’t asking to actually be raped"',
                    hum='abstract verbs replaced by what a couple does; the rather-than frame gone'),
    'r03-s17': dict(lineage='romance-s17', scope='pair', call='AI', chance=0.45,
                    tells='a list of five in the students’ sentence',
                    human='"a ton of stories"; "didn’t stay in the bedroom"; the jade-egg sentence, unchanged',
                    diag='The live post read AI Medium on "Kim Anami goes further and treats sexual energy itself as a path '
                         'into healing, creativity, worldly action, and spiritual awakening." and AI Low on the students’ '
                         'sentence: two lists in a row that name creativity and work twice.',
                    first='payoff: what Anami does stays first; join: none; plain: "didn’t stay in the bedroom and '
                          'spilled over into" for "spill out of sex into", "everything else" for "the rest of life"',
                    hum='creativity and work said once, in the students’ sentence; Anami’s sentence keeps healing and '
                        'awakening'),
    'r03-s18': dict(lineage='romance-s18', scope='paragraph', call='Human', chance=0.65,
                    tells='a list of five at the end of a sentence',
                    human='his whole paragraph around it, unchanged',
                    diag='The live post read AI Low on "Housing, money, children, health, emotional crises—if one person '
                         'goes down, the other becomes the whole backup system.": a list fronted before the dash and the '
                         'point.',
                    first='payoff: "If one person goes down, the other becomes the whole backup system" comes first; join: '
                          'the list joins it with "for"; plain: his words',
                    hum='the fronted list moved after the point'),
    'r03-s19': dict(lineage='romance-s19', scope='pair', call='Human', chance=0.55,
                    tells='a long joined sentence with three reasons',
                    human='his paragraph before it; "Take what they say with a grain of salt"',
                    diag='The live post read AI Low on "They are hearing a partial story, usually while you’re upset, and '
                         'they may be trying to protect you rather than understand the relationship fairly.": a '
                         'rather-than frame that repeats the paragraph’s "biased toward you".',
                    first='payoff: the grain of salt comes first and the reasons follow; join: the reasons join it with '
                          '"since"; plain: "they’re only hearing your side" for "a partial story"',
                    hum='the rather-than frame cut as a repeat of "biased toward you"; contractions as he talks'),
    'r03-s20': dict(lineage='romance-s20', scope='pair', call='Human', chance=0.5,
                    tells='a run of four questions',
                    human='his first paragraph of questions, unchanged; "And the biggie"',
                    diag='The live post read AI Low on "What counts as betrayal, and what just means we need a serious '
                         'conversation?", AI Medium on "If our lives change, can we revisit the agreement honestly?" and AI '
                         'Low on "If we separate, what do we still owe each other, and what do we owe any children '
                         'involved?": formal words in his question voice ("revisit the agreement honestly", "any children '
                         'involved").',
                    first='payoff: each question already asks first; join: none; plain: "a serious talk", "honestly sit '
                          'down and rethink the agreement", "split up", "our kids, if we have any"',
                    hum='the formal words in three questions replaced by how he talks in the questions before them'),
    'r03-s21': dict(lineage='romance-s21', scope='pair', call='Human', chance=0.55,
                    tells='a rhetorical question',
                    human='his Ecclesiastes paragraph, unchanged; the verses as he quotes them',
                    diag='The live post read AI Low on "To me, the extra promise itself starts to look suspicious." and on '
                         '"If your yes is trustworthy, why does it need another layer?": a "To me," frame ahead of his '
                         'conclusion, then the question that leads to it.',
                    first='payoff: the question comes first and his conclusion follows from it; join: none; plain: "The '
                          'extra promise actually starts to make me suspicious" for "To me, the extra promise itself '
                          'starts to look suspicious"',
                    hum='the "To me," frame gone; the question before the conclusion it leads to'),
}
for key, p in P.items():
    if sys.argv[1:] and key not in sys.argv[1:]:
        continue
    cmd = [sys.executable, str(ROOT / 'tools' / 'humanization' / 'pangram_ledger.py'), 'predict', str(LEDGER),
           '--lineage', p['lineage'], '--scope', p['scope'], '--text', REL + 'CHECK-%s.txt' % key, '--call', p['call'],
           '--chance', str(p['chance']), '--tells', p['tells'], '--human-tells', p['human'], '--diagnosis', p['diag'],
           '--decides', 'whether the %s window reads Human' % p['lineage'].split('-')[1].upper(), '--key', key,
           '--batch', 'romance-r03', '--detector', DET, '--receipt', REL + 'RECEIPT-%s.json' % key,
           '--first-fix', p['first'], '--humanized', p['hum']]
    if p.get('big'):
        cmd += ['--big-change', p['big']]
    if p.get('panel'):
        cmd += ['--panel', PANEL]
    r = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    print(key, r.returncode, (r.stdout + r.stderr).strip()[:600])
