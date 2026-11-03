#!/usr/bin/env python3
"""Turn 116: the writer's half of each gate manifest (docs/HUMANIZATION-OWNER-DELIVERY-GATE.md) for the six few-word
suggestions on Joel's reorganized guide (make_gate_files.py): who wrote it, a literal T/C judgment for every inventory row
(docs/HUMANIZATION-TELL-INVENTORY.md) about my words in their sentence, and where the three reviewers' reports go. Each
draft is a pointer or a noun phrase of two to eight words inside his sentence, so most rows have the same answer; each
item's own rows say what is particular to it. Run after make_gate_files.py; it refuses a manifest whose hashes don't
match its files. Adapted from experiments/t115-gate/fill_ledgers.py."""
import hashlib
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
ME = {'name': 'Claude Opus 5.5, the Inner Child lane writer', 'context_id': 'session_01NbUfhcTaRT8sbjyYV1wEFq'}
REVIEWS = {'preservation': 'REVIEW-preservation.json', 'cold_read_1': 'REVIEW-cold_read_1.json', 'cold_read_2': 'REVIEW-cold_read_2.json'}
A = 'ABSENT'
KIND = {'G1': 'pointer', 'G2': 'pointer', 'G5': 'pointer', 'G3': 'referent', 'G4': 'referent', 'G6': 'referent'}
GENERIC = {
    'T01': 'my words add no first person; the sentence\'s voice is his',
    'T02': 'a few words inside one of his sentences; no run of commands',
    'T03': 'the change adds no concern or distinction; it says what an existing word points at',
    'T04': 'no scene added',
    'T05': 'no prop added',
    'T06': 'no therapy abstraction added; the words name a section or a person in the guide',
    'T07': 'no filler or staged hesitation added',
    'T08': 'no image added, and nothing explained after one',
    'T09': 'the sentence is his, with its own rhythm; my words change no sentence\'s shape',
    'T10': 'no permission packaging',
    'T12': 'no contrast or taxonomy added',
    'T13': 'the sentence is his and notices what it noticed before; my words only fix where it points',
    'T14': 'nothing reordered or moved; the words go where the broken pointer or referent is',
    'T15': 'no rewording of his words: a pointer or referent that his reorganization broke is replaced, nothing else',
    'T16': 'no "not X, it\'s Y"',
    'T17': 'no thesis line added',
    'T18': 'no premise flipped',
    'T20': 'the paragraph ends as he wrote it',
    'T21': 'no clause with another job added',
    'T22': 'no reassurance or coaching added',
    'T23': 'no scenery added',
    'T24': 'no question added',
    'T25': 'no colon added',
    'T27': 'none of the tic words',
    'T28': 'the section\'s ending is his, unchanged',
    'T29': 'the paragraph\'s last sentence is his, unchanged',
    'C01': 'the inner child is not named in my words, and "the kid" appears nowhere',
    'C03': 'no fact about Joel\'s life in my words',
    'C04': 'no claim about a study, person or product in my words',
}
OWN = {
    'G1': {'T11': 'a cross-reference to a named section, in the form he uses for forward references ("further on"), replacing his "as described in" that his move made point the wrong way; not a bridge',
           'T19': 'a pointer inside a parenthesis that was already there, not a sentence announcing what comes next',
           'T26': '"Noticing Counts" stays once, as he had it; "further on" is his phrase from two other places, which is the point of using it',
           'C02': 'the pointer now says where Noticing Counts is (later in the guide); before, "as described in" pointed back at a section the reader hasn\'t reached'},
    'G2': {'T11': 'a cross-reference in his form ("We get deeper into ... further on"), not a bridge',
           'T19': 'a pointer inside a parenthesis, not a sentence announcing what comes next',
           'T26': '"that" picks up "differentiation" without repeating it; "we get deeper into" and "further on" are his own words from Sometimes There Isn\'t a Clear Child Yet',
           'C02': '"that" is "differentiation" just before it; the pointer tells a reader meeting the word for the first time that its section comes later'},
    'G3': {'T11': 'no bridge: a noun phrase in place of "that guard\'s"',
           'T19': 'no announcement',
           'T26': '"your little one" is the guide\'s name for the inner child throughout; once here',
           'C02': 'the fix for a C02: "that guard" pointed at a guard the reader hasn\'t met (the guard image comes later), and his heading "Earning their trust" says it is the little one\'s trust'},
    'G4': {'T11': 'no bridge: "Your future self" in place of "That future you"',
           'T19': 'no announcement',
           'T26': '"Your future self" is his phrase from The Chicken-and-Egg Problem; once in this section',
           'C02': 'the fix for a C02: "That future you" pointed back at a sentence he cut ("It\'s a question borrowed from your future self")'},
    'G5': {'T11': 'a cross-reference to a named section, not a bridge',
           'T19': 'a parenthesis naming where the cast comes from, not a sentence announcing what comes next',
           'T26': '"Borrow Hindsight" once here',
           'C02': '"this cast" pointed at future versions built about 190 lines earlier, after Forgiving Yourself; the parenthesis names the section they come from'},
    'G6': {'T11': 'no bridge: a noun phrase in place of "its"',
           'T19': 'no announcement',
           'T26': '"the critical voice" picks up "a critical voice" in the paragraph before the heading; once here, and his "that voice" two sentences later follows from it',
           'C02': 'the fix for a C02: the first "its" had no noun near it (the Mr. Rogers story comes between)'},
}


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


for name in sorted(KIND):
    d = HERE / name
    m = json.loads((d / 'ADMISSION.json').read_text(encoding='utf-8'))
    assert m['candidate_sha256'] == sha(d / 'DRAFT.txt') and m['context_sha256'] == sha(d / 'CONTEXT.txt'), name
    ledger = []
    for r in m['tell_ledger']:
        k = r['id']
        ev = OWN[name].get(k) or GENERIC.get(k)
        assert ev and len(ev) >= 12, (name, k)
        ledger.append({'id': k, 'status': A, 'evidence': ev, 'resolution': ''})
    m['tell_ledger'] = ledger
    m['writer'] = ME
    assert not m['lint']['findings'], (name, m['lint']['findings'])
    m['review_files'] = dict(REVIEWS)
    m['status'] = 'READY_FOR_CHECK'
    (d / 'ADMISSION.json').write_text(json.dumps(m, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print('%s ledger %d rows, lint %d' % (name, len(ledger), len(m['lint']['findings'])))
