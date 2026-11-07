#!/usr/bin/env python3
"""r04's predictions, written before the checks (pangram_ledger.py predict, one per text in texts.py)."""
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[5]
LEDGER = ROOT / 'articles' / 'romance' / 'humanize' / 'pangram-ledger.jsonl'
REL = 'articles/romance/humanize/fix-20261107/r04/checks/'
DET = 'pangram 4.1, the web app (Joel\'s account, GUI credits)'
PANEL = 'articles/romance/humanize/fix-20261107/r03/panel-s2/PANEL.md'
BACK = ('the r02 try rewrote his sentences into new set pieces and read worse than the live post; this try goes back to '
        'the live post\'s words and changes only the sentences in its windows, so most of r02\'s words go')
P = {
    'r04-s2e': dict(lineage='romance-s2', scope='pair', call='AI', chance=0.4,
                    tells='a colon before the West example; "it’s free food, a roof and respect" is still three things',
                    human='his "Venerable Somebody", "Why wouldn’t it?", his closing pair as the live post has it; "a guy '
                          'who was a nobody", "hold down a job"',
                    diag='Try 3 (#15) read AI Medium on the poor-country sentence and AI High on the West sentence for the '
                         'third time: every version so far told the West case as a hypothetical guy in three escalating '
                         'steps ("shave his head, become Venerable Somebody, and suddenly people are bowing"), and listed '
                         'the poor-country perks in a "you get" frame. My closing pair read AI Medium and Low, no better '
                         'than his (AI Low twice). The tell panel (on try 2) called the West picture human; Pangram read it '
                         'AI High each time, so this try changes how the West case is told.',
                    first='payoff: each case says what it is about first ("it’s free food ...", "it’s more about the '
                          'respect"); join: the West case and its picture in one sentence with a colon; plain: "a roof", '
                          '"hold down a job", "a guy who was a nobody as a layman is now Venerable Somebody"',
                    hum='the West case is a plain before-and-after, with no three-step escalation; the perks are said the '
                        'way he talks ("it’s free food, a roof and respect"); his closing pair back as he wrote it',
                    big='three tries kept the West sentence’s three-step escalation, which read AI High each time; this '
                        'one says it as a plain before-and-after and rebuilds the perks sentence, so most of try 3’s '
                        'words change',
                    panel=True),
    'r04-s6': dict(lineage='romance-s6', scope='pair', call='Human', chance=0.7,
                   tells='"I just think we need ..." states a need',
                   human='his first paragraph; "didn’t exactly solve the problem"; the 30–40 percent figure',
                   diag='Try 2 (#16) read Human, with one Low window: "So it wasn’t a very reliable way to keep courtship '
                        'nonsexual." (12 words) on its own after the figure it follows from.',
                   first='payoff: the figure leads and its consequence follows in the same sentence; join: "so it wasn’t" '
                         'joins the figure; plain: unchanged',
                   hum='the consequence joined to the figure it follows from, as he joins his own sentences'),
    'r04-s7': dict(lineage='romance-s7', scope='pair', call='Human', chance=0.5,
                   tells='a run of questions',
                   human='his questions, with the friends-and-exes one added in their form; "you shut down"',
                   diag='Try 2 (#17) read AI on my friends-and-exes sentences (a general reason tacked on, which repeats '
                        'his paragraph before) and on the staged shut-down lead-in; his questions read Human Low to Medium. '
                        'The tell panel (r04/panel-s7) agreed on my reason sentence ("Nobody’s a great judge ..., me '
                        'included") and on his question list; his questions read Human in the live post and stay.',
                   first='payoff: the friends-and-exes question goes into his list as its last question; join: the two '
                         'shut-down questions become one; plain: "if you tell me you shut down", as his questions say "you"',
                   hum='the tacked-on reason cut as a repeat; the lead-in asks his question directly, in the "you" his list '
                       'uses',
                   panel='articles/romance/humanize/fix-20261107/r04/panel-s7/PANEL.md',
                   big='try 2 kept the reason and the staged lead-in; this one cuts the reason and folds both changed '
                       'paragraphs into his question form'),
    'r04-s10': dict(lineage='romance-s10', scope='pair', call='Human', chance=0.5,
                    tells='"as just part of how we live" could read as a soft tag',
                    human='Toft’s sentence and his reply, unchanged; his outburst told as he would tell it',
                    diag='Try 2 (#19) read worse than the live post: a bare 10-word point (AI Medium), then an Otherwise '
                         'run-on (AI High). The tell panel on it (r04/panel-s10) agreed on my point sentence, a slogan in a '
                         'therapy register ("make alone time normal"), and on the hedge "it can easily sound like". The '
                         'link to Toft’s idea before it was missing too.',
                    first='payoff: "So I’d rather take time alone regularly from the beginning" says what he does and why '
                          'it follows; join: the reason in one if-sentence; plain: "take time alone regularly" for "make '
                          'alone time normal", "she’s likely to hear it as" for "it can easily sound like"',
                    hum='the slogan said as what he would do; the hedge said as what she would hear; "So" ties it to '
                        'Toft’s sources',
                    big='the panel agreed on the wording of both my sentences, so both are rebuilt; his paragraph before '
                        'them is unchanged',
                    panel='articles/romance/humanize/fix-20261107/r04/panel-s10/PANEL.md'),
    'r04-s11': dict(lineage='romance-s11', scope='pair', call='Human', chance=0.5,
                    tells='"and on top of that" could read as a stock turn',
                    human='his sentences about the role; "It can run the other way too."; "made her Mom"; "keep me '
                          'functional", which a panel reader called human',
                    diag='Try 2 (#20) read AI Low (better than the live post’s AI Medium) with the four-item list still in '
                         'it. The tell panel (r04/panel-s11) agreed on that list of four therapy verbs, with "regulate me" '
                         'as clinical words in a personal voice and "soothe every wound" as a generic, overblown phrase. '
                         'It also agreed on his sentences before it, which read Human in the live post and stay.',
                    first='payoff: the if-clause says what she has to do, then that it makes her Mom; join: the practical '
                          'pair joined by "and on top of that"; plain: "calm me down every time I’m upset" for "regulate '
                          'me, soothe every wound"',
                    hum='the clinical word and the overblown phrase said as one plain thing; the list of four is now one '
                        'emotional job and a practical pair',
                    big='the panel agreed on the words of my sentence, the list and its clinical and overblown items, so '
                        'the sentence is rebuilt; his paragraph before it is unchanged',
                    panel='articles/romance/humanize/fix-20261107/r04/panel-s11/PANEL.md'),
    'r04-s15': dict(lineage='romance-s15', scope='pair', call='Human', chance=0.5,
                    tells='a long joined sentence',
                    human='his next paragraph, unchanged, which echoes the list on purpose',
                    diag='Try 1 (#22) read AI Medium: "something’s already fake, because then ..." stayed abstract, and '
                         'cutting the list broke his callback in the next paragraph.',
                    first='payoff: having to prove it comes first, then what that does; join: one sentence with "and"; '
                          'plain: "being the man has already become an act" for "something has already become fake"',
                    hum='the abstract "something" named (being the man) and made concrete (an act); his list back for his '
                        'callback'),
    'r04-s17': dict(lineage='romance-s17', scope='pair', call='AI', chance=0.45,
                    tells='a list of five in the students’ sentence',
                    human='"a ton of stories"; his jade-egg sentence, unchanged',
                    diag='Try 1 (#24) read AI Generated, 100%, his jade-egg sentence included (Human in the live post): '
                         'Anami’s sentence is a summary of a person’s views in nouns ("goes further and treats ... as a '
                         'path to healing and spiritual awakening").',
                    first='payoff: what she says comes first; join: "goes even further:" joins it; plain: "can heal you and '
                          'wake you up spiritually" for "a path to healing and spiritual awakening", "spilled out of the '
                          'bedroom" for "didn’t stay in the bedroom and spilled over"',
                    hum='her view in verbs, as what she says, not a summary in nouns; the students’ list ends the way he '
                        'ended it, with "the rest of their lives" and no "and"'),
    'r04-s19': dict(lineage='romance-s19', scope='pair', call='Human', chance=0.6,
                    tells='a long sentence ending in its advice',
                    human='his paragraph before it; "Take what they say with a grain of salt"',
                    diag='Try 1 (#26) read Human with my sentence in a Low window: the advice came first and three reasons '
                         'trailed after "since".',
                    first='payoff: the reasons lead to the advice (his move: the context first); join: one sentence with '
                          '"so"; plain: unchanged',
                    hum='the reasons first, then "so take what they say with a grain of salt"'),
    'r04-s21': dict(lineage='romance-s21', scope='pair', call='Human', chance=0.5,
                    tells='a rhetorical question at the end',
                    human='his Ecclesiastes paragraph and his verses, unchanged; his closing question',
                    diag='Try 1 (#28) read AI Medium on my two sentences and pulled his verses to AI Low: the paragraph '
                         'never says the link it rests on, that a wedding vow is the extra promise the verses warn about.',
                    first='payoff: the missing link is said first ("A wedding vow is exactly that kind of extra '
                          'promise"); join: his conclusion joins it with "and"; plain: his closing question back as he '
                          'wrote it',
                    hum='the unsaid link between the verses and vows said in plain words; his question back at the end'),
}
for key, p in P.items():
    if sys.argv[1:] and key not in sys.argv[1:]:
        continue
    cmd = [sys.executable, str(ROOT / 'tools' / 'humanization' / 'pangram_ledger.py'), 'predict', str(LEDGER),
           '--lineage', p['lineage'], '--scope', p['scope'], '--text', REL + 'CHECK-%s.txt' % key, '--call', p['call'],
           '--chance', str(p['chance']), '--tells', p['tells'], '--human-tells', p['human'], '--diagnosis', p['diag'],
           '--decides', 'whether the %s window reads Human' % p['lineage'].split('-')[1].upper(), '--key', key,
           '--batch', 'romance-r04', '--detector', DET, '--receipt', REL + 'RECEIPT-%s.json' % key,
           '--first-fix', p['first'], '--humanized', p['hum']]
    if p.get('big'):
        cmd += ['--big-change', p['big']]
    if p.get('panel'):
        cmd += ['--panel', PANEL if p['panel'] is True else p['panel']]
    r = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    print(key, r.returncode, (r.stdout + r.stderr).strip()[:600])
