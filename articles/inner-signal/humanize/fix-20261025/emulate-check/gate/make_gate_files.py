#!/usr/bin/env python3
"""The owner-delivery gate's files (docs/HUMANIZATION-OWNER-DELIVERY-GATE.md, main's of 2026-10-25 17:44 UTC) for the new
model-written words on the two Emulate-check marking pages: the hypnosis guide's (../REVIEW-EMULATE.json) and the
community article's (articles/intentional-communities/candidate/joel-20261025/emulate-check/REVIEW-EMULATE.json). Main's
Inner Child lane put its review sheet's new sentences through the gate the same day (its turn 110), one sentence at a
time; this does the same. Cards that only put back his own words, or change one word to his, stay outside the gate,
which is for generated prose, not owner-authored prose; GATE.md lists them.

Each NAME gets DRAFT.txt (the exact new sentence or sentences, as the page shows them), CONTEXT.txt (its section as it
would read with the change, holding the draft once) and SOURCE.txt (the sentence it replaces and his own published line),
then `owner_delivery_gate.py init` writes ADMISSION.json. GATE-INPUTS.json gives the reviewers each NAME's folder,
change and hashes.

Round 1 (GATE-INPUTS-ROUND1.json) had sixteen drafts. Where a reviewer failed one, the card now shows his own words and the
draft is WITHDRAWN below; it stays out of GATE-INPUTS.json. A draft whose CONTEXT.txt changed because a withdrawn draft
in the same card did (C-E3a, after C-E3b) gets new files and a new manifest; its round-1 manifest and reviews move to
superseded/, since they carry the old context's hash.

  python3 articles/inner-signal/humanize/fix-20261025/emulate-check/gate/make_gate_files.py
"""
import datetime
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[5]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import suggestion_review as sr  # noqa: E402

GATE = ROOT / 'tools' / 'humanization' / 'owner_delivery_gate.py'
PAGES = {
    'guide': (HERE.parent / 'REVIEW-EMULATE.json', HERE),
    'community': (ROOT / 'articles/intentional-communities/candidate/joel-20261025/emulate-check/REVIEW-EMULATE.json',
                  ROOT / 'articles/intentional-communities/candidate/joel-20261025/emulate-check/gate'),
}
# NAME: (page, card, the new words as on the page, the old words they replace, his own line, the change in words)
DRAFTS = {
    'G-EM2': ('guide', 'EM-2', 'It’s built from familiar practices like modeling and supported action, but I’m not suggesting that the whole sequence has been formally tested and proven as one treatment.',
              'It is important to note here that I’m not suggesting that all of the steps in this process have been formally tested and proven.',
              'It combines familiar practices—witnessing, modeling, supported action, and gradual transfer of responsibility—without claiming that the complete sequence has been validated as one treatment.',
              'Emulate\'s sentence said "not all of the steps ... have been tested"; this puts back his two points: the steps are familiar practices, and only the whole sequence is untested as one treatment.'),
    'G-EM5': ('guide', 'EM-5', 'You were too busy avoiding pain, reading what was dangerous and what you had to do to stay in a good bond, etc.',
              'You were too occupied in not being in pain, reading out what was dangerous and what you had to do to stay in a good bond, etc.',
              'A useful developmental explanation is that when childhood is organized around avoiding pain and preserving attachment, attention goes into reading danger, meeting expectations, and keeping the bond.',
              'Mends Emulate\'s "too occupied in not being in pain, reading out what was dangerous" with his "avoiding pain" and "reading danger".'),
    'G-EM9': ('guide', 'EM-9', None, 'to help me know what I need to know in a form and at a level that will be useful',
              'please help me understand what I need to know, only in the form and timing that is useful, kind, stabilizing, and real.',
              'Puts back his "only" and his timing in the invocation: "only in a form and at a time that will be useful".'),
    'G-EM11': ('guide', 'EM-11', 'DO NOT: Attempt to force memories, to use trance to prove something happened to you, or to force down medical symptoms with hypnosis instead of getting them looked at.',
               'DO NOT: Attempt to “force” memories, to use trance to “prove” something happened to you, or to skip medical attention for symptoms just because you can “force” them down using hypnosis.',
               'Do not force memory recovery, use trance to prove what happened, or suppress medical symptoms.',
               'Puts back his rule against suppressing medical symptoms, which Emulate had narrowed to skipping medical attention, and takes off Emulate\'s quote marks.'),
    'G-EM13': ('guide', 'EM-13', 'Ethical Double Bind Questions give you two choices that are both genuinely safe.',
               'Ethical Double Bind Questions might be:',
               'A manipulative double bind traps every answer inside the speaker’s agenda. An ethical one offers two genuinely safe routes.',
               'Adds his definition of an ethical double bind, which Emulate dropped, before the examples.'),
    'G-EM14': ('guide', 'EM-14', "Nominalizations are words that turn a process into a noun, like 'healing', 'safety', 'trust', 'integration', 'communion', 'clarity', 'rest', etc.",
               "Nominalizations are words like 'healing', 'safety', 'trust', 'integration', 'communion', 'clarity', 'rest', etc.",
               'Nominalizations turn processes into nouns: healing, safety, trust, integration, communion, clarity, rest.',
               'Adds his definition of a nominalization, which Emulate dropped, in front of the examples.'),
    'G-EM15': ('guide', 'EM-15', 'I do not tell people to override their fear before asking what it’s protecting.',
               'I do not tell people to override their fear.',
               'To override fear before asking what the fear protects.',
               'Puts back his condition: he won\'t override fear before asking what it protects.'),
    'G-EM16': ('guide', 'EM-16', 'What matters is whether the way you’re responding helps you get steadier and less hooked.',
               'but whether warmth or distance helps, that doesn’t prove what it is.',
               'Neither response establishes its origin. A protective part needn’t reveal its fear quickly; a comforting response doesn’t prove an interpretation either. The useful question is whether this way of responding helps you become clearer, steadier, and less hooked.',
               'Puts back his test for a response in place of Emulate\'s broken sentence ("but whether warmth or distance helps, that doesn\'t prove what it is").'),
    'G-EMS2': ('guide', 'EM-S2', None, "Also, Adam Eason's work with Benjamin Parris in the International Society of Hypnosis, specifically his article about self hypnosis, should be a useful thing to read",
               'Adam Eason and Benjamin Parris’s ISH article on self-hypnosis discusses self-directed learning and its relationship to another hypnotist and recordings.',
               'Gives the article back to both its authors; Emulate gave it to Eason alone and made the two "work in" the society.'),
    'G-EMS3a': ('guide', 'EM-S3', 'Chapter 7 of Trauma and Memory, by Peter Levine, 2015, is useful on the difference between a compelling experience and what really happened.',
                'Chapter 7 of Trauma and Memory, by Peter Levine, 2015, contains useful information on this.',
                'Levine’s Trauma and Memory (2015), chapter 7, is useful on the difference between compelling experience and historical verification.',
                'Says what the chapter is about, from his line; Emulate\'s "useful information on this" said nothing.'),
    'G-EMS3b': ('guide', 'EM-S3', 'Links are available for these and other useful groups in the evidence and specialist sections, but each one backs up only its own claim.',
                'Links are available for these and other useful groups in the evidence and specialist sections, but they point to their particular claims, not every use of hypnosis.',
                'The existing links in the evidence and specialist sections point to their particular claims rather than validating every use of hypnosis.',
                'Says what the links back up, from his line; Emulate\'s "point to their particular claims, not every use of hypnosis" lost it.'),
    'C-E2': ('community', 'IC-E2', 'It’s already a real piece of community, and it can still make a difference when people are going through a divorce, an illness or grief.',
             'It can still make a difference when people are going through a divorce, an illness or grief.',
             'A weekly group that has practiced together for two years already contains a real piece of community. It may never own land.',
             'Puts back his point that a practice group already is community, which Emulate dropped.'),
    'C-E3a': ('community', 'IC-E3', 'Who has to step aside because they’re too close to it?', '',
              'Decide the process before the name: what conduct triggers immediate protective action, who preserves evidence, who is recused, who decides temporary restrictions, how the person replies, what review or appeal is possible without endangering others',
              'Puts back his "who is recused" as a question in the list.'),
    'C-E3b': ('community', 'IC-E3', 'What review or appeal can you safely give them?', '',
              'Decide the process before the name: what conduct triggers immediate protective action, who preserves evidence, who is recused, who decides temporary restrictions, how the person replies, what review or appeal is possible without endangering others',
              'Puts back his "what review or appeal is possible without endangering others" as a question in the list.'),
    'C-E4': ('community', 'IC-E4', 'And a community’s autonomy doesn’t let it take away rights a person can’t sign away, or make the law outside disappear.', '',
             'But autonomy is not permission to erase non-waivable individual rights, and it does not make outside jurisdiction disappear.',
             'Puts back his limit on autonomy, which Emulate dropped.'),
    'C-T1': ('community', 'IC-T1', 'Just because taking part in the ceremonies is optional doesn’t mean people don’t have to work with the other parts.',
             'Just because it’s optional participating in the ceremonies doesn’t mean they don’t have to work with the other parts.',
             '(He kept this sentence on 2026-10-24, answer 65.14 B.)',
             'Grammar only: the sentence didn\'t parse ("it\'s optional participating").'),
}

# NAME: why the card shows his own words instead (GATE.md)
WITHDRAWN = {
    'G-EM11': 'both reviewers failed "instead of getting them looked at" as a condition his rule lacks; the card uses his "or to suppress medical symptoms"',
    'G-EM13': 'his own two sentences fit the place as they are ("A manipulative double bind ... An ethical one offers two genuinely safe routes."); the card uses his second one',
    'G-EM16': 'both reviewers failed it for dropping "clearer" from his three-part test; the card uses his own sentences',
    'G-EMS3a': 'the preservation reviewer failed "what really happened" for his "historical verification"; the card uses his words',
    'G-EMS3b': 'both reviewers failed it for dropping "every use of hypnosis"; the card uses his "rather than validating every use of hypnosis"',
    'C-E3b': 'the preservation reviewer failed "safely" for losing whose safety ("without endangering others"); the card uses his words',
}


def sentence_with(text, words):
    for a, z in [(a, z) for a, z in sr_sentences(text)]:
        if words in text[a:z]:
            return text[a:z].strip()
    raise ValueError(words)


def sr_sentences(text):
    sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
    import emulate_artifacts as ea
    return ea.sentences(text)


def main():
    inputs = {}
    for name, (page, card, draft, old, his, change) in DRAFTS.items():
        if name in WITHDRAWN:
            continue
        rpath, gdir = PAGES[page]
        review = json.loads(rpath.read_text(encoding='utf-8'))
        md = (ROOT / review['article']['file']).read_text(encoding='utf-8')
        bl = sr.blocks(md)
        s = next(x for x in review['suggestions'] if x['id'] == card)
        e = s['edits'][0]
        after = e['after']
        if draft is None:   # the changed sentence, whole
            k = after.find(s['what'].split('becomes "')[1][:40]) if 'becomes "' in s['what'] else -1
            draft = {'G-EM9': 'to help me know what I need to know, only in a form and at a time that will be useful',
                     'G-EMS2': "Also, Adam Eason and Benjamin Parris's article about self hypnosis for the International Society of Hypnosis should be a useful thing to read"}[name]
        assert after.count(draft) == 1, (name, draft[:60])
        i = e['block']
        h = max(b['i'] for b in bl[:i + 1] if b['level'])
        paras = []
        for b in bl[h + 1:]:
            if b['level']:
                break
            paras.append(b['i'])
        context = '\n\n'.join([bl[h]['text']] + [after if j == i else bl[j]['text'] for j in paras])
        assert context.count(draft) == 1, name
        d = gdir / name
        d.mkdir(parents=True, exist_ok=True)
        if (d / 'CONTEXT.txt').exists() and (d / 'CONTEXT.txt').read_text(encoding='utf-8') != context + '\n':
            old_dir = d / 'superseded' / ('round1-' + datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%MZ'))
            old_dir.mkdir(parents=True)
            for f in ['CONTEXT.txt', 'ADMISSION.json'] + sorted(x.name for x in d.glob('REVIEW-*.json')):
                if (d / f).exists():
                    (d / f).rename(old_dir / f)
            print(name, 'context changed; round-1 files moved to', old_dir.relative_to(ROOT))
        (d / 'DRAFT.txt').write_text(draft, encoding='utf-8')
        (d / 'CONTEXT.txt').write_text(context + '\n', encoding='utf-8')
        src = ('The sentence it replaces: ' + old + '\n\n' if old else 'New words; nothing in the paragraph is replaced.\n\n') + \
              'His own line (his published post, or his answer): ' + his + '\n'
        (d / 'SOURCE.txt').write_text(src, encoding='utf-8')
        if not (d / 'ADMISSION.json').exists():
            run = subprocess.run([sys.executable, str(GATE), 'init', '--draft', str(d / 'DRAFT.txt'), '--context', str(d / 'CONTEXT.txt'),
                                  '--source', str(d / 'SOURCE.txt'), '--manifest', str(d / 'ADMISSION.json')], capture_output=True, text=True)
            if run.returncode not in (0, 1):
                print(name, 'init:', run.stdout[-400:], run.stderr[-400:])
        m = json.loads((d / 'ADMISSION.json').read_text(encoding='utf-8'))
        inputs[name] = {'folder': str(d), 'the_change': change, 'candidate_sha256': m['candidate_sha256'],
                        'context_sha256': m['context_sha256'], 'source_sha256': m['source_sha256'],
                        'lint_verdict': m['lint']['verdict_at_init'],
                        'lint_findings': [{'label': f['label'], 'examples': f['examples']} for f in m['lint']['findings']]}
        print('%-8s lint %-6s %s | %s' % (name, m['lint']['verdict_at_init'], [f['label'] for f in m['lint']['findings']], draft[:60]))
    (HERE / 'GATE-INPUTS.json').write_text(json.dumps(inputs, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')


if __name__ == '__main__':
    main()
