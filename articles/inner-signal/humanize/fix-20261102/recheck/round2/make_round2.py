"""Batch r1102b: tested fixes for the windows batch r1102 found (gate E306: a window that reads AI or Human (Low) gets
fixed now), with predictions written before the run. Nothing goes on Joel's cards page untested (his note on W-605,
2 November: "you didn't check if your changes passed.. they didn't. don't waste my time"), and every result has its
public link (on W-274: "always give me the links").

The sections themselves used their two checks (lineages HG1101-15 and HG1101-40), so each fix is checked with the
paragraph before or after it, as it stands and as it would read, in a lineage of its own (cap 6), the base first:

- A. The inner child, the guards (section 15): "That's one grown-up doing three jobs, not three more people moving in to
  help with the rent, ..." read AI (High) in the section. It's his inner child guide's line (W-92), which there goes on
  to his party example; A1 brings the example along, his words from his inner child guide, word for word.
- B. Stay awake / Make the hypnosis more alert (section 40) read AI Detected: the script (W-283, the card's version he
  approved) AI (High) twice, and his own rewrite above it AI (Low) in five places. B0 is the passage he checked himself
  ("now it's human high conf"), from "Once you've got your bearings", which starts in the section before; B1 his
  paragraph and the script as they are; B2 and B3 the script with its list of three echoes said as three things you might
  notice, B3 with the escalation said plainly too.
- C. Working with your guards (section 23): our sentence "So before you decide where it's coming from, ask it what it's
  trying to stop, or what it wants." read Human (Low); C1 asks the two questions as questions.
- D. Pattern 10 (section 69): our two paragraphs read Human (Low); D1 brings back his published verbs ("To 'Milton Model'
  is to open things up"), and D2 also says the Meta Model's questions as you'd ask them, not as a list.

  python3 articles/inner-signal/humanize/fix-20261102/recheck/round2/make_round2.py [--round 2|3] [--ledger]
Writes TEXTS.json, CANDIDATES.json and PREDICTIONS.md / .json; with --ledger, adds each prediction to the ledger.
"""
import argparse
import hashlib
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parents[2]
ROOT = H.parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import suggestion_review as sr  # noqa: E402

LEDGER = H / 'pangram-ledger.jsonl'
BATCH = 'r1102b'
DETECTOR = 'pangram 4.1, the API (Joel\'s key, run on his laptop; E218)'

STARTS = {90: 'The inner child, the guards, and the inner adult', 91: 'Your inner child won’t trust you right away',
          92: 'Here I’m going to talk about what you develop', 140: 'Instead, you might feel numb', 141: 'Talk to the guard',
          274: 'Once you’ve got your bearings, make your first wish', 636: 'How do you know which it is?',
          637: 'If it is helping you, then simply ask', 638: 'If it is taking you away from life',
          639: 'Then ask yourself what it is that you need to do', 281: 'Aside from focusing on things',
          282: '“Starting with your eyes open', 527: 'Pattern 10: Meta Model questions', 528: 'Milton Model language opens',
          529: 'When something sounds true but vague', 530: 'So when someone is starting to tense up'}

RENT = 'That’s one grown-up doing three jobs, not three more people moving in to help with the rent, and each job keeps the others in balance.'
PARTY = (' Say a party gets to be too much for your little one. The Protector gets you both out of there, and on the way '
         'home the Nurturer tells them they did great, even though mostly they hid in the bathroom. And the Guide helps '
         'them think twice about the next weird party they might go to, avoiding another cycle of bathroom vacationing. 🙈')
ECHO = ('In the first second after you stop, notice if there’s any echo of the pressing in your fingers, in your '
        'breathing, in your attention, or nowhere at all.')
ECHO2 = ('In the first second after you stop, see if the pressing is still echoing somewhere. Maybe your fingers still '
         'tingle, or your breath is keeping the rhythm, or your attention is waiting for the next press. Or maybe there’s '
         'no echo at all.')
RISE = ('As you do, you begin to bring yourself into a place of clearer awareness… Press and let go again, and you’re '
        'clearer still. And once more, into the clearest state of awareness yet.')
RISE3 = ('Each time you do, you get a little more awake… Press and let go again, a bit clearer. And once more, and now '
         'you’re clearer than when you started.')
ECHO4 = ('In the first second after you stop, is the pressing still echoing somewhere? Start with your fingers, which may '
         'still be tingling. Next, see if your breath kept the rhythm going. Then check whether your attention is still '
         'waiting for the next press. Or maybe there’s no echo at all.')
SAY = ' Say something like,'
PRAYER = (' Simply say to yourself, “Dear subconscious, thank you for showing me images. If what you are showing me is '
          'helpful, then please also show me the guidance in it. If what you are showing me is a way of avoiding dealing '
          'with life, then please show me in a gentle but structured way how to deal with life as it is right now.”')
ASK = 'So before you decide where it\'s coming from, ask it what it\'s trying to stop, or what it wants.'
ASK1 = 'So before you decide where it\'s coming from, ask it. What is it trying to stop? What does it want from you?'
P528 = ('Milton Model language opens things up, and Meta Model questions ask what exactly someone means. If you want to be '
        'ethical with people, you need both.')
P528D = ('To \'Milton Model\' is to open things up, so the listener can fill in what fits for them. To \'Meta Model\' is '
         'to stop and ask, "What do you mean by that?" In order to be ethical with people, you need to do both.')
P529 = ('When something sounds true but vague, ask: "What do you mean, specifically? According to who? Compared to '
        'what? Always, or never? What exactly would happen if you did? How do you know that, and what evidence would '
        'change your mind?"')
P529D = ('When something sounds true but vague, ask, "What do you mean, specifically?" Then find out according to who, and '
         'compared to what. If you hear "always" or "never," check whether it\'s really every time. If someone\'s afraid '
         'of doing something, ask what exactly would happen if they did. And ask how they know, and what evidence would '
         'change their mind.')

# key: (lineage, scope, [(block, replacement or None)], call, chance, why, card, author)
TRIES = {
    'r1102b-A0': ('HG1102-15-P12', 'pair', [(91, None), (92, None)], 'AI', 0.4,
                  'the two paragraphs as they stand; in the section the rent line read AI (High)', 'W-92', 'his'),
    'r1102b-A1': ('HG1102-15-P12', 'pair', [(91, None), (92, (RENT, RENT + PARTY))], 'Human', 0.6,
                  'his inner child guide\'s party example after the rent line, as it goes there (his words; specifics)',
                  'W-92', 'his'),
    'r1102b-B0': ('HG1102-W282', 'stretch', [(i, None) for i in range(274, 283)], 'Human', 0.55,
                  'the passage he checked himself ("now it\'s human high conf"), from "Once you\'ve got your bearings" to '
                  'the end of the script, as it stands', 'W-282', 'his'),
    'r1102b-B1': ('HG1102-40-S', 'pair', [(281, None), (282, None)], 'AI', 0.35,
                  'his paragraph and the script as they stand; in the section the script read AI (High) twice',
                  'W-283', 'his'),
    'r1102b-B2': ('HG1102-40-S', 'pair', [(281, None), (282, (ECHO, ECHO2))], 'AI', 0.45,
                  'the list of three echoes said as three things you might notice; the rising part unchanged',
                  'W-283', 'ours'),
    'r1102b-B3': ('HG1102-40-S', 'pair', [(281, None), (282, (ECHO, ECHO2)), (282, (RISE, RISE3))], 'Human', 0.5,
                  'B2, and the "clearer, clearer still, clearest yet" climb said plainly', 'W-283', 'ours'),
    'r1102b-B4': ('HG1102-40-S', 'pair', [(281, None), (282, (ECHO, ECHO4)), (282, (RISE, RISE3))], 'Human', 0.55,
                  'B3\'s climb (it read Human, Medium and Low), and the three echoes as three steps, each its own verb '
                  '(his fix for W-589 and W-605: a sequence, not a list)', 'W-283', 'ours'),
    'r1102b-B5': ('HG1102-40-C', 'pair', [(280, None), (281, (SAY, ''))], 'Human', 0.6,
                  'the script cut: his paragraph above it already says each of its steps (eyes open, the small hand '
                  'movement with each suggestion of clarity, then stop and see where your mind is at)', 'W-283', 'his'),
    'r1102b-B6': ('HG1102-W282', 'stretch', [(i, None) for i in range(274, 281)] + [(281, (SAY, ''))], 'Human', 0.55,
                  'the passage he checked himself, from "Once you\'ve got your bearings", with the script cut', 'W-283',
                  'his'),
    'r1102b-E1': ('HG1102-AppE-P3', 'stretch', [(636, None), (637, None), (638, (PRAYER, '')), (639, None)], 'Human',
                  0.6, 'Appendix E\'s prayer cut: it says what the prayer in Stay awake when your mind likes to escape '
                  'says (his rewrite, W-282), and "ask your subconscious to help you" stays', None, 'his'),
    'r1102b-C0': ('HG1102-23-P34', 'pair', [(140, None), (141, None)], 'Human', 0.55,
                  'the two paragraphs as they stand; in the section the last sentence of the first read Human (Low)',
                  None, 'ours'),
    'r1102b-C1': ('HG1102-23-P34', 'pair', [(140, (ASK, ASK1)), (141, None)], 'Human', 0.6,
                  'the two questions asked as questions', None, 'ours'),
    'r1102b-D0': ('HG1102-69-P10', 'stretch', [(527, None), (528, None), (529, None), (530, None)], 'Human', 0.5,
                  'Pattern 10 as it stands; in the section its first 63 words read Human (Low)', None, 'ours'),
    'r1102b-D1': ('HG1102-69-P10', 'stretch', [(527, None), (528, (P528, P528D)), (529, None), (530, None)], 'Human',
                  0.55, 'his published verbs back ("To \'Milton Model\' is to open things up"), said a little more fully',
                  None, 'ours'),
    'r1102b-D2': ('HG1102-69-P10', 'stretch', [(527, None), (528, (P528, P528D)), (529, (P529, P529D)), (530, None)],
                  'Human', 0.6, 'D1, and the Meta Model\'s questions said as you\'d ask them, not as a list of seven',
                  None, 'ours'),
}


# one try per lineage per round (the ledger takes a lineage's next try only after its last one has a result); the
# section checks of batch r1102 are the base, so each lineage starts with its best candidate. Round 3 comes after round
# 2's results (RESULTS.md here): B3 and D2 read AI, so B4 and D1 are the lineages' second tries; its files are in r3/.
# Round 4 (r4/), after B4 read AI too: the script cut, since his paragraph above it says each of its steps (a redundancy,
# his note on W-685), checked with that paragraph and in the passage he checked himself. Round 5 (r5/): the one other
# repeat the redundancy read found worth a card (../../redundancy/REPEATS.md), Appendix E's prayer.
ROUNDS = {2: ['r1102b-A1', 'r1102b-B0', 'r1102b-B3', 'r1102b-C1', 'r1102b-D2'], 3: ['r1102b-B4', 'r1102b-D1'],
          4: ['r1102b-B5', 'r1102b-B6'],
          5: ['r1102b-E1']}


def build(bl, parts):
    out = {}
    order = []
    for i, rep in parts:
        if i not in out:
            out[i] = bl[i]['text']
            order.append(i)
        if rep:
            old, new = rep
            assert out[i].count(old) == 1, (i, old[:40])
            out[i] = out[i].replace(old, new)
    return '\n\n'.join(out[i] for i in order), {i: out[i] for i in order if out[i] != bl[i]['text']}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--ledger', action='store_true')
    ap.add_argument('--round', type=int, default=2)
    a = ap.parse_args()
    ROUND = ROUNDS[a.round]
    OUT = HERE if a.round == 2 else HERE / ('r%d' % a.round)
    OUT.mkdir(exist_ok=True)
    bl = sr.blocks((H / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8'))
    for i, s in STARTS.items():
        assert bl[i]['text'].startswith(s), (i, bl[i]['text'][:50])
    texts, rows, cands = {}, [], {}
    for k, (lineage, scope, parts, call, chance, why, card, author) in TRIES.items():
        if k not in ROUND:
            continue
        text, changed = build(bl, parts)
        texts[k] = text
        cands[k] = {'card': card, 'author': author, 'blocks': [i for i, _ in parts], 'changed': changed}
        rows.append({'key': k, 'lineage': lineage, 'scope': scope, 'words': len(text.split()), 'call': call,
                     'chance': chance, 'why': why, 'card': card,
                     'sha256': hashlib.sha256(text.encode('utf-8')).hexdigest()})
    (OUT / 'TEXTS.json').write_text(json.dumps(texts, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    (OUT / 'CANDIDATES.json').write_text(json.dumps(cands, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    out = ['# Batch r1102b: the fixes for batch r1102\'s windows, checked before they reach Joel (predictions, before the '
           'run)', '', 'Chance = my chance of a 100% Human result. The Pangram column is filled after the run.', '',
           '| text | lineage | words | mine | chance | why | Pangram |', '|---|---|---|---|---|---|---|']
    for r in rows:
        out.append('| %s | %s | %d | %s | %.2f | %s | |' % (r['key'], r['lineage'], r['words'], r['call'], r['chance'],
                                                         r['why']))
    (OUT / 'PREDICTIONS.md').write_text('\n'.join(out) + '\n', encoding='utf-8')
    (OUT / 'PREDICTIONS.json').write_text(json.dumps(rows, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print(len(rows), 'texts:', [(r['key'], r['words']) for r in rows])
    if not a.ledger:
        return
    td = OUT / 'texts'
    td.mkdir(exist_ok=True)
    for r in rows:
        f = td / (r['key'] + '.txt')
        f.write_text(texts[r['key']], encoding='utf-8')
        cmd = [sys.executable, str(ROOT / 'tools' / 'humanization' / 'pangram_ledger.py'), 'predict', str(LEDGER),
               '--lineage', r['lineage'], '--scope', r['scope'], '--text', str(f), '--call', r['call'],
               '--chance', str(r['chance']), '--key', r['key'], '--batch', BATCH, '--detector', DETECTOR,
               '--tells', 'batch r1102 (2 November): the window this fixes read AI or Human (Low) in its section',
               '--human-tells', 'his words, or a fix said from his published version',
               '--diagnosis', r['why'],
               '--decides', 'whether this fix reads Human before it goes on his cards page or into the guide (E306, E315)']
        p = subprocess.run(cmd, capture_output=True, text=True)
        if p.returncode:
            sys.exit('%s: %s%s' % (r['key'], p.stdout, p.stderr))
    print('ledger: %d predictions added' % len(rows))


if __name__ == '__main__':
    main()
