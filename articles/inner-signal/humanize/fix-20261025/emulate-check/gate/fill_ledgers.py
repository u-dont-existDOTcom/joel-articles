#!/usr/bin/env python3
"""The writer's half of each gate manifest (docs/HUMANIZATION-OWNER-DELIVERY-GATE.md): who wrote it, a literal judgment on
every inventory row (docs/HUMANIZATION-TELL-INVENTORY.md, T01 to T29 and C01 to C04), a reason for each linter REVIEW
finding, and where the three reviewers' reports go. The reviewers are three fresh subagents, one per role, each reading
only the files (REVIEW-BRIEF.md); main's Inner Child lane did the same on its turn 110 (its t110-gate/fill_ledgers.py,
whose row wording this follows). Run after make_gate_files.py; it refuses a manifest whose hashes don't match its files.

  python3 articles/inner-signal/humanize/fix-20261025/emulate-check/gate/fill_ledgers.py
"""
import hashlib
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
ME = {'name': 'Claude Opus 5.5, the hypnosis guide and community lanes\' writer',
      'context_id': 'session_01Mxpoi6tFT3FgKmBvtGjRtS'}
REVIEWS = {'preservation': 'REVIEW-preservation.json', 'cold_read_1': 'REVIEW-cold_read_1.json', 'cold_read_2': 'REVIEW-cold_read_2.json'}
A = 'ABSENT'
LINT = {
    'D9 follows the source order': 'It is his own line (SOURCE.txt) put back in place of Emulate\'s wording, so it follows his order by design; the paragraph around it keeps its own order and asides.',
    'E36/E41 heavy second person': 'The guide speaks to the reader as "you" throughout; this sentence uses it to give one step, inside a paragraph that is not a run of coaching lines.',
    'O27 a rough edge in my text: the paragraph ends with no period': 'The draft is the changed part of a longer sentence; in the article the sentence goes on (CONTEXT.txt) and ends with its own full stop.',
    'B2 contrast': 'The contrast is the content, from his line: what the rule forbids against what it replaces (G-EM11), or the chapter\'s topic, a compelling experience against what really happened (G-EMS3a).',
    'B4/E15 list or packed sentence': 'The list is his and was already in the paragraph (the nominalization examples; the chapter, title, author and year of a reference); the change adds one clause to it.',
    'B7 short landing at paragraph end': 'The linter sees the question alone; in the article it is one question in a list of questions in the middle of its paragraph, not its end.',
}


def rows(draft, said):
    q = '"%s"' % (draft if len(draft) < 90 else draft[:87] + '...')
    base = {
        'T01': 'no first-person stake in %s beyond the source\'s own' % q,
        'T02': '%s is one step in its paragraph, not part of a run of compressed commands' % q,
        'T03': 'the sentence before it in the context sets it up; nothing new arrives unprepared in %s' % q,
        'T04': 'no scene in %s' % q,
        'T05': 'no concrete prop in %s' % q,
        'T06': 'no vague healing or process language in %s; its terms are the article\'s own' % q,
        'T07': 'no filler or staged hesitation in %s' % q,
        'T08': 'no image followed by an explanation of it in %s' % q,
        'T09': 'one change in one passage; %s gets the weight its point needs, the rest of the passage is unchanged' % q,
        'T10': 'no "you don\'t have to X before Y" packaging in %s' % q,
        'T11': '%s carries a claim or step, not a bridge between document parts' % q,
        'T12': 'no matched pair or closed list made for symmetry in %s' % q,
        'T13': 'the passage around %s keeps its reasons, asides and callbacks; the change adds none of its own and removes none' % q,
        'T14': 'no material moved to dodge a detector: %s puts back the author\'s own point that Emulate dropped' % q,
        'T15': '%s puts back the author\'s words or meaning, not less likely words for their own sake' % q,
        'T16': 'no "not X, it\'s Y" in %s' % q,
        'T17': 'no compressed thesis or aphorism in %s' % q,
        'T18': 'no premise flipped by a short sentence in %s' % q,
        'T19': '%s does not announce what comes next' % q,
        'T20': '%s is not a polished paragraph-ending line' % q,
        'T21': '%s does one job, not several coordinated argumentative jobs' % q,
        'T22': '%s carries a step, a rule or a reason from his line, not reassurance alone' % q,
        'T23': 'no generic scenery in %s' % q,
        'T24': 'no faux-insight setup or self-answered question in %s' % q,
        'T25': 'no colon reveal in %s' % q,
        'T26': 'no distinctive word or phrase in %s repeated within three paragraphs without a job' % q,
        'T27': 'none of the tic words ("doing some work", "load-bearing", "digest", "clean", vague "work") in %s' % q,
        'T28': '%s is not the end of its section, and adds no lesson or uplift' % q,
        'T29': '%s is not a closing restatement of its paragraph' % q,
        'C01': 'the inner child is not named in %s, and "the kid" appears nowhere in it' % q,
        'C02': 'every pronoun in %s points at something named just before it' % q,
        'C03': 'no first-person fact about Joel\'s life in %s that he didn\'t give' % q,
        'C04': 'no claim about a study, person or product in %s' % q,
    }
    out = []
    for k, ev in base.items():
        if k in said:
            st, ev2, *why = said[k]
            r = {'id': k, 'status': st, 'evidence': ev2, 'resolution': 'JUSTIFIED_KEEP' if st == 'PRESENT' else ''}
            if st == 'PRESENT':
                r['reason'] = why[0]
            out.append(r)
        else:
            out.append({'id': k, 'status': A, 'evidence': ev, 'resolution': ''})
    return out


SAID = {
    'G-EM2': {'T01': (A, '"I’m not suggesting" is the first person of the sentence it replaces ("I’m not suggesting that all of the steps ..."), his own disclaimer of his method'),
              'T12': (A, '"modeling and supported action" are two of his four familiar practices, kept as examples, not a pair built for balance')},
    'G-EM5': {'T03': (A, '"One way of explaining this is that in your childhood you didn’t spend enough attention ..." sets it up; this sentence says why'),
              'C02': (A, '"You" is the reader of the paragraph\'s first sentence; "what was dangerous" and "a good bond" are from it')},
    'G-EM9': {'C02': (A, '"me" is the speaker of the invocation that the clause belongs to ("I invoke my Higher Self ...")')},
    'G-EM11': {'T16': (A, '"instead of getting them looked at" says what the suppression replaces; it is not a "not X, it\'s Y" reveal'),
               'C02': (A, '"them" is "medical symptoms", named just before')},
    'G-EM13': {'T03': (A, 'the paragraph before says what a manipulative double bind does; this says what makes the ethical one different, then the examples follow')},
    'G-EM14': {'T12': (A, 'the list of examples is his and was already there; the change is the definition in front of it')},
    'G-EM15': {'T01': (A, '"I do not tell people" is the first person of his list "Here is a list of things I do not do with NLP"'),
               'C02': (A, '"it" is "their fear", named just before')},
    'G-EM16': {'T26': (A, '"less hooked" echoes Appendix H\'s opening ("safer, clearer, more loving, more grounded and less hooked"), many paragraphs up; the echo ties the test to that aim'),
               'T22': (A, 'it gives his test for a response, "whether this way of responding helps you become ... less hooked", not reassurance')},
    'G-EMS2': {'C04': (A, 'both authors, the article and the society are from his published line: "Adam Eason and Benjamin Parris’s ISH article on self-hypnosis"')},
    'G-EMS3a': {'C04': (A, 'the book, author, year, chapter and its topic are from his published line: "Levine’s Trauma and Memory (2015), chapter 7, is useful on the difference between compelling experience and historical verification"'),
                'T12': (A, '"a compelling experience and what really happened" is the chapter\'s topic in his words, not a contrast made for balance')},
    'G-EMS3b': {'C02': (A, '"each one" is the links of the sentence\'s own subject, "Links are available for these and other useful groups"')},
    'C-E2': {'C02': (A, '"It" is "A group that practices together weekly for two years", the sentence before; "So what?" sits between them as his')},
    'C-E3a': {'C02': (A, '"they" is whoever would decide; "it" is the removal case the list is about ("This power to remove people")')},
    'C-E3b': {'C02': (A, '"them" is "the person" of the question before ("How will the person be able to reply to the concerns?")')},
    'C-E4': {'C02': (A, '"it" is "a community", named in the same sentence')},
    'C-T1': {'C02': (A, '"people" names who works with the other parts; the old "they" could be read as the ceremonies')},
}


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    inputs = json.loads((HERE / 'GATE-INPUTS.json').read_text(encoding='utf-8'))
    for name, x in inputs.items():
        d = pathlib.Path(x['folder'])
        m = json.loads((d / 'ADMISSION.json').read_text(encoding='utf-8'))
        assert m['candidate_sha256'] == sha(d / 'DRAFT.txt') and m['context_sha256'] == sha(d / 'CONTEXT.txt'), name
        draft = (d / 'DRAFT.txt').read_text(encoding='utf-8')
        m['writer'] = ME
        m['tell_ledger'] = rows(draft, SAID.get(name, {}))
        for f in m['lint']['findings']:
            key = next(k for k in LINT if f['label'].startswith(k))
            f['disposition'] = 'JUSTIFIED_KEEP'
            f['reason'] = LINT[key]
        m['review_files'] = dict(REVIEWS)
        m['status'] = 'READY_FOR_CHECK'
        (d / 'ADMISSION.json').write_text(json.dumps(m, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        print('%-8s ledger %d rows, lint %s' % (name, len(m['tell_ledger']), [f['label'][:30] for f in m['lint']['findings']]))


if __name__ == '__main__':
    main()
