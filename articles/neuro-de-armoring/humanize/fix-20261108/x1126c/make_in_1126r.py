"""IN.json for batch x1126r: each fold of 72a checked by itself (the Cognitive Warning, under 50 words, with the
paragraph after it), from the receipts' texts."""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
R = HERE / 'receipts'
SEC = 'https://www.pangram.com/history/b0684e96-0fc7-45a7-9a84-6ce66bc9958b'
MID = 'https://www.pangram.com/history/7b98691f-cf13-4576-8979-1362f2e6009e'
OFF = 'https://www.pangram.com/history/b9f4952c-eb3b-456d-a757-9b9ed17a259f'
WHY = ('checked as a section the warnings read Mostly Human (6%%, %s); the five in the middle read AI together (90%%, %s), '
       '28%% with their labels off (%s): a run of "Label: claim" paragraphs reads as a generated list of tips. 72a folds '
       'each label into its first sentence, opening on the subject. ' % (SEC, MID, OFF))
DECIDES = ('whether the fold goes in; below High, the next try starts from it and changes a word or two a reader could '
           'take two ways')
FF = ('payoff: with the label gone the first sentence opens on the warning\'s subject and what it means for the reader '
      '(%s); join: none, the sentences after the first are unchanged; plain: none, no paraphrase in it')
HISV = ('only the label folded into the first sentence (72a)%s; every other word is his own card version')
MINEV = ('only the label folded into the first sentence (72a); every other word is my version that read Human High')

ITEMS = {
    'dmso-f1': dict(lineage='W-DMSO', receipt='DMSO-F1', name='DMSO Safety, its label folded in', chance=0.8,
                    first='"This protocol has you smell DMSO for anxiety and brain fog."',
                    stood='https://www.pangram.com/history/00c16a93-c037-4131-be4a-92e08639fcf8',
                    human="his line \"(I've never had a bad batch)\""),
    'elec-f1': dict(lineage='W-ELEC', receipt='ELEC-F1', name='Electrolytes, its label folded in', chance=0.8,
                    first='"You\'ll also be eating a lot more potassium than most people get"',
                    stood='https://www.pangram.com/history/107fdac9-c18d-4518-a639-09950f338556', human='',
                    tells='"consult a doctor first if you have kidney disease or heart conditions" (a stock medical '
                    'caution)'),
    'ethno-f1': dict(lineage='W-ETHNO', receipt='ETHNO-F1', name='Ethnobotanicals, its label folded in', chance=0.8,
                     first='"The plant medicines in this protocol are iboga ... and psilocybin mushrooms."',
                     stood='https://www.pangram.com/history/c6b0ce3a-3677-45aa-bf26-0b425cb58b3f',
                     human='his line "since AI is pretty good at that"'),
    'iso-f1': dict(lineage='W-ISO-his', receipt='ISO-F1', name='Behavioral Warning, its label folded in, "the isolation '
                   'trap" kept in its third sentence', chance=0.75, his=True,
                   first='"This neural de-armoring protocol demands starving your brain of Phasic Dopamine"',
                   stood='https://www.pangram.com/history/364ba0a6-ea20-4584-85e8-5d8ca2c733d0',
                   human='his own card version: "The easiest way for most folks to take a break from that is to hole up '
                         'alone"', extra=', and his nickname "the isolation trap" kept in the third ("But don\'t fall '
                   'into the isolation trap of cutting yourself off completely")'),
    'rule-f1': dict(lineage='W-RULE', receipt='RULE-F1', name='The Rule, its label folded in', chance=0.7,
                    first='"My rule for now is to seek Boring Love, meaning parallel play ..."',
                    stood='https://www.pangram.com/history/f981a309-164a-4f7d-a198-c470b773ebdc',
                    human='his post\'s "Boring Love" and "Exciting Love"', tells='"My rule for now is to seek" (a rule '
                    'statement opening the paragraph)'),
    'cog-faces-f1': dict(lineage='PAIR-COG-FACES', scope='pair', receipt='PAIR-COG-FACES-F1', name='Cognitive Warning '
                         '(30 words), its label folded in, with the paragraph after it', chance=0.7,
                         first='"As you de-armor, you will feel naked and exposed."',
                         stood='https://www.pangram.com/history/aeb0115a-dadf-489b-a096-828677f55f06',
                         human='his post\'s "you will feel naked and exposed"'),
    'lma-f1': dict(lineage='W-LMA-his', receipt='LMA-F1', name='Lion\'s Mane & Ashwagandha, its label folded in',
                   chance=0.75, his=True, first='"I\'m not advising lion\'s mane or ashwagandha, even though ..."',
                   stood='https://www.pangram.com/history/37022ca4-704b-48af-a7d3-150d3700c3c2',
                   human='his own card version: "Post-ashwa and post-lion\'s mane syndrome are rare"',
                   extra=', "either of these" named as the two herbs'),
    'agm-f1': dict(lineage='W-AGMINTRO-his', receipt='AGM-F1', name='Agmatine Warning, its label folded in, "the voltage '
                   'regulator" kept in its first sentence', chance=0.7, his=True,
                   first='"Agmatine, the voltage regulator, acts like a brake on NMDA/glutamate signaling"',
                   stood='https://www.pangram.com/history/2d5f8c39-9e62-4301-ab59-5e416a8c26d5',
                   human='his own card version: "People may think it\'s pretty safe, since it\'s a common health '
                         'supplement"', tells='the appositive nickname right after the subject ("Agmatine, the '
                   '\'voltage regulator\', acts like")', extra=', his nickname kept as an appositive'),
    'prec-f1': dict(lineage='W015-his', receipt='PREC-F1', name='Precautions, its label folded in, agmatine named',
                    chance=0.75, his=True, first='"Do not use agmatine concurrently with opioids and/or kratom ..."',
                    stood='https://www.pangram.com/history/afc40e25-fc20-4db8-a220-5c1fb41419d6',
                    human='his own paragraph: "Not recommended for use in pregnancy or breast-feeding."',
                    extra=', agmatine named where the label said what it was about'),
    'htp-f1': dict(lineage='W-HTPTOP-his', receipt='HTP-F1', name='The warning for psychedelic users, its label folded '
                   'in, "it" named as 5-HTP', chance=0.75, his=True,
                   first='"Uridine and 5-HTP are in this protocol for repairing neural signaling"',
                   stood='https://www.pangram.com/history/bc1f203e-34da-44e7-99db-6e4140130364',
                   human='his own card version: "That\'s how folks end up with serotonin syndrome"',
                   extra=', and "it" named as 5-HTP in the last sentence, which a fresh reader of the fold took as the '
                   'list\'s drugs'),
}

out = {}
for k, v in ITEMS.items():
    t = (R / (v['receipt'] + '.txt')).read_text(encoding='utf-8').rstrip('\n')
    d = {'lineage': 'neuro-de-armoring/' + v['lineage'], 'scope': v.get('scope', 'paragraph'), 'name': v['name'],
         'text': t, 'chance': v['chance'], 'receipt': str(R / (v['receipt'] + '.receipt.json')),
         'diagnosis': WHY + 'As it stood it read Human High by itself (%s)%s.' % (
             v['stood'], ', his own check of his version' if v.get('his') else ''),
         'decides': DECIDES, 'first_fix': FF % v['first'],
         'humanized': HISV % v.get('extra', '') if v.get('his') else MINEV}
    if v.get('human'):
        d['human_tells'] = v['human']
    if v.get('tells'):
        d['tells'] = v['tells']
    out[k] = d
(HERE / 'checks-1126r' / 'IN.json').write_text(json.dumps(out, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
print(len(out), 'items')
