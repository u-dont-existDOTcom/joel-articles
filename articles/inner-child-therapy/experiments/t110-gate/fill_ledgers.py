#!/usr/bin/env python3
"""Turn 110: the writer's half of each gate manifest (docs/HUMANIZATION-OWNER-DELIVERY-GATE.md): who wrote it, a literal
T/C judgment for every inventory row (docs/HUMANIZATION-TELL-INVENTORY.md), a reason for each linter REVIEW finding, and
where the three reviewers' reports go. The reviews are done by three fresh subagents, one per role, each reading only the
files (REVIEW-BRIEF.md). Run after init; it refuses a manifest whose hashes don't match its files."""
import hashlib
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
ME = {'name': 'Claude Opus 5.5, the Inner Child lane writer', 'context_id': 'session_01NbUfhcTaRT8sbjyYV1wEFq'}
GPT = {'name': 'GPT, in Joel\'s review of the turn-109 sheet (experiments/t110-answers/GPT-REVIEW-20261025.md), adopted with "I\'d" kept by Claude Opus 5.5',
       'context_id': 'chatgpt-review-20261025 (GPT-REVIEW-20261025.md sha256 2ecd1b53576b9a0349641c3755072001c45f13c418aafbd12f079dc58aeac687)'}
REVIEWS = {'preservation': 'REVIEW-preservation.json', 'cold_read_1': 'REVIEW-cold_read_1.json', 'cold_read_2': 'REVIEW-cold_read_2.json'}

A = 'ABSENT'


def rows(draft, said):
    """Every row ABSENT with a literal note unless SAID gives (status, evidence[, reason])."""
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
        'T12': 'no matched pair or closed list in %s' % q,
        'T13': 'the passage around %s keeps its reasons, asides and callbacks; the change adds none of its own and removes none' % q,
        'T14': 'no material moved to dodge a detector: the change in %s is a referent or readability fix both reviews asked for' % q,
        'T15': '%s changes words to say what the old ones left unclear, not to swap in less likely words' % q,
        'T16': 'no "not X, it\'s Y" in %s' % q,
        'T17': 'no compressed thesis or aphorism in %s' % q,
        'T18': 'no premise flipped by a short sentence in %s' % q,
        'T19': '%s does not announce what comes next' % q,
        'T20': '%s is not a polished paragraph-ending line' % q,
        'T21': '%s does one job, not several coordinated argumentative jobs' % q,
        'T22': '%s carries a stance or a reason from its passage, not reassurance alone' % q,
        'T23': 'no generic scenery in %s' % q,
        'T24': 'no faux-insight setup or self-answered question in %s' % q,
        'T25': 'no colon reveal in %s' % q,
        'T26': 'no distinctive word or phrase in %s repeated within three paragraphs without a job' % q,
        'T27': 'none of the tic words ("doing some work", "load-bearing", "digest", "clean", vague "work") in %s' % q,
        'T28': '%s is not the end of its section' % q,
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


CANDIDATES = {
    'S1-nurturer': (ME, {
        'T01': (A, '"I\'d" is the source\'s ("I\'d still keep it the same."), and the reason for the Nurturer voice is the exchange just before: "It puts you into the role of the Nurturer, which alleviates the instinct to argue back."'),
        'T12': (A, 'the contrast "A harder voice can seem more fitting ... I\'d still keep the Nurturer voice." answers a temptation the reader really has; it is not a balanced pair for coverage'),
        'T18': ('PRESENT', 'premise "A harder voice can seem more fitting for something that\'s been in your way." then the short "I\'d still keep the Nurturer voice."',
                'The structure is the source\'s, which Joel approved in turn 27 ("I\'d still keep it the same."); the premise is a real temptation, the reason is the exchange right before, and the next sentence turns it into a step ("borrow it from someone who\'s been safe for you"). The change only names which voice.'),
        'T26': (A, '"the Nurturer voice" repeats "the same Nurturer voice" of the section\'s first sentence, and the repetition is the fix: it says which voice "the same" meant (GPT\'s P8 point)'),
        'C02': (A, '"the Nurturer voice" names the referent, so "that voice" in the next sentence can only be it; before, "the same" and "that voice" could point at the harder voice'),
    }, {
        'B7 short landing at paragraph end': 'The linter sees the sentence alone as a paragraph. In the article it is the middle of three: "If that voice isn\'t there in you yet, borrow it from someone who\'s been safe for you." follows it, so it lands nothing.',
    }),
    'S1-watch': (ME, {
        'T01': (A, '"I think" is the source\'s ("and I think watching is what it wants anyway"): a reading of the part\'s motive the reader can test'),
        'T08': (A, '"I think watching is what it wants anyway, to find out if there\'s a grown-up here now who could call it all off" adds the part\'s reason, a new consideration, not a translation of "It can keep watch"'),
        'T10': (A, '"It can keep watch while you take one small step" is the part\'s permission inside this case (it doesn\'t have to move out), not a reusable counseling formula'),
        'T15': (A, '"call it off" became "call it all off": one word so "it" can\'t be read as the guard (the cold read), and ", and I think" became ". I think" (GPT\'s readability fix)'),
        'T21': (A, 'split in two, each sentence does one job: the permission ("It can keep watch ...") and the motive ("I think watching is what it wants anyway ...")'),
        'T26': (A, '"keep watch" then "watching" ties the permission to the motive; the repeat is the link'),
        'C02': (A, '"It" and "it wants" are the guard, named as "That part" two sentences before; "call it all off" now means the whole step, which "call it off" left open'),
    }, {
        'D9 follows the source order': 'It is the source sentence split in two with one word added, so it follows the source\'s order by design; the passage keeps its asides ("way longer than the grown-up you", the blinds) and its callback.',
    }),
    'S1-protective': (ME, {
        'T03': (A, 'the paragraph before it shows a part doing a protective job (calling all this stupid because it is "scared of getting its hopes up"), and "too" ties the self-blame case to it'),
        'T06': (A, '"a protective job" is the article\'s own term for what its protective parts do (the section opens "Whichever protective part showed up"), and the next sentences say what it protects against'),
        'T11': (A, 'it states a claim the paragraph then tests ("might be your parent\'s line", "Then again, if it\'s your fault, maybe you can fix it before they leave")'),
        'T15': (A, '"a job like that" became "a protective job": the cold read couldn\'t tell which job, and GPT asked to tie self-blame to a part\'s protective job explicitly'),
        'T17': (A, 'it opens a possibility the paragraph examines with "might" and "Then again", not a finished principle'),
        'T26': (A, '"protective" calls back to the section\'s first sentence six paragraphs up; the callback is what ties self-blame to the guards'),
        'T27': (A, '"doing a protective job" names the job, and the paragraph says what it does; not the vague "doing some work" tic'),
        'C02': (A, '"a protective job" needs no antecedent, which is the fix; "they" later points at "your parent"'),
    }, {
        'B7 short landing at paragraph end': 'The linter sees it alone. In the article it opens its paragraph, and four sentences follow it, so it ends nothing.',
        'D9 follows the source order': 'It is the source sentence with one phrase replaced, so it follows the source by design; the paragraph keeps its own turns ("Then again", "either way").',
    }),
    'P2': (GPT, {
        'T01': (A, '"I\'d" is the source\'s ("I\'d keep whatever you feel around them"); it is the step that answers "How do you check that?"'),
        'T02': (A, 'one step between the question "How do you check that?" and the concrete questions "Do they respect a no, or keep pushing on it"'),
        'T15': (A, '"keep whatever you feel" became "keep what you feel ... in mind": it says what to do with the feeling, which GPT found ambiguous ("Keep feeling it? Remember it? Trust it?")'),
        'T22': (A, 'it pairs the reader\'s felt sense with a check of behavior, and the questions after it make the check concrete'),
    }, {
        'D9 follows the source order': 'It is the source sentence with its meaning made plain, so it follows the source\'s order by design.',
        'E36/E41 heavy second person': 'One "you" in a 16-word sentence that answers "How do you check that?"; the second person is the reader running the check, and the paragraph has no run of coaching lines.',
    }),
    'P5': (ME, {
        'T01': (A, 'the first person is his own experience: "My son did that for me" is his "I actually used my son ... to reconnect with my inner child"'),
        'T03': (A, 'the sentence before it says a child or a pet "can also act as a companion that brings out the relationship with your own inner child"; "did that for me" is that case'),
        'T22': (A, 'it is a fact of his and his impression, not reassurance'),
        'C03': (A, 'his answer of 2026-10-02 00:16 UTC supplies it: "I actually used my son (i shouldn\'t say "used") to reconnect with my inner child, and I think that\'s very common for parents."'),
        'C04': (A, '"I think that\'s very common for parents" is his stated impression, hedged as his ("I think"), as he said it'),
    }, {
        'D9 follows the source order': 'It is his answer as one article sentence, in his order (his son, then his impression); nothing is reordered.',
    }),
    'P6': (ME, {
        'T01': (A, '"I\'d" is the source\'s ("I\'d leave out forgiving them and picturing their childhood.")'),
        'T15': (A, 'one word, "here", so the line limits this exercise and can\'t be read as advice against forgiving them at all (GPT\'s P6)'),
        'T28': (A, 'it is the paragraph\'s and exercise\'s own limit, not a lesson or uplift'),
        'T29': (A, 'the sentence before it ("Whoever hurt you might come to mind, too.") raises the case and this one says what to do with it; it is a new step, not a restatement'),
        'C02': (A, '"them" and "their" are "Whoever hurt you", named in the sentence before; "here" is this exercise'),
    }, {
        'D9 follows the source order': 'It is the source sentence with "here" added, so it follows the source by design.',
    }),
}


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


for name, (writer, said, lint_reasons) in CANDIDATES.items():
    d = HERE / name
    m = json.loads((d / 'ADMISSION.json').read_text(encoding='utf-8'))
    assert m['candidate_sha256'] == sha(d / 'DRAFT.txt') and m['context_sha256'] == sha(d / 'CONTEXT.txt'), name
    draft = (d / 'DRAFT.txt').read_text(encoding='utf-8')
    m['writer'] = writer
    m['tell_ledger'] = rows(draft, said)
    labels = [f['label'] for f in m['lint']['findings']]
    assert set(labels) == set(lint_reasons), (name, labels)
    for f in m['lint']['findings']:
        f['disposition'] = 'JUSTIFIED_KEEP'
        f['reason'] = lint_reasons[f['label']]
    m['review_files'] = dict(REVIEWS)
    m['status'] = 'READY_FOR_CHECK'
    (d / 'ADMISSION.json').write_text(json.dumps(m, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    present = [r['id'] for r in m['tell_ledger'] if r['status'] == 'PRESENT']
    print('%-14s ledger %d rows, present %s, lint %s' % (name, len(m['tell_ledger']), present, labels))
