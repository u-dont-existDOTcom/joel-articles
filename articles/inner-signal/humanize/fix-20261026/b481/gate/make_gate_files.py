#!/usr/bin/env python3
"""The owner-delivery gate's files (docs/HUMANIZATION-OWNER-DELIVERY-GATE.md) for batch 481's Emulate splices
(../CANDIDATES.json, S11 to S36), the same files and steps as batch 480's gate (../../gate/make_gate_files.py): Emulate's
words are model-written words in his byline, so each passes the gate before his page shows it as a proposed change.

Each NAME gets DRAFT.txt (the exact new words, as the page shows them), CONTEXT.txt (its section as it would read with
every candidate in, from ../CANDIDATE-MASTER.md, holding the draft once) and SOURCE.txt (the words it replaces and the
line the meaning comes from), then `owner_delivery_gate.py init` writes ADMISSION.json. GATE-INPUTS.json gives the
reviewers each NAME's folder, change and hashes.

  python3 articles/inner-signal/humanize/fix-20261026/b481/gate/make_gate_files.py [NAME ...]   (from the repo root)
"""
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[5]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import suggestion_review as sr  # noqa: E402

GATE = ROOT / 'tools' / 'humanization' / 'owner_delivery_gate.py'
MASTER = HERE.parent / 'CANDIDATE-MASTER.md'
CANDS = HERE.parent / 'CANDIDATES.json'
# NAME: (spot, the change in words)
DRAFTS = {
    'G-S11': ('S11', 'Emulate\'s "read some of the stuff in the daily and weekly sections" (sample co) for "look at the daily and '
                     'weekly sections", with the sentence\'s own ending kept ("to make the practice your own") and "Also" for '
                     '"You can also" (the linter\'s coach register).'),
    'G-S12': ('S12', 'Emulate\'s sentence (sample cm) in place of his own "On a guide this long, that little hidden menu is your '
                     'friend.": the hidden table of contents helps because the guide is long.'),
    'G-S14': ('S14', 'Emulate\'s first and third sentences (sample co) around his own second one, which stays: there are many ways '
                     'to influence people without the conscious mind, and the FTC\'s report on dark patterns, with his "designs that '
                     'trick or manipulate consumers" put back (the first draft\'s "their", "used to" and "trick and manipulate" '
                     'failed preservation).'),
    'G-S15': ('S15', 'Emulate\'s version (sample co): the four kinds of agreement joined to the question with a dash.'),
    'G-S16': ('S16', 'Emulate\'s "So each can correct the other." (sample cm) for "So these modes can correct each other."'),
    'G-S17': ('S17', 'The line without its "And", as all three samples gave it.'),
    'G-S18': ('S18', 'Emulate\'s two sentences (sample cm) for the two that read Medium and Low, ending on his own "trust and '
                     'precision"; "One reason was" made "One reason might have been" (his "Maybe part of that").'),
    'G-S19': ('S19', 'Emulate\'s sentence (sample co): the body\'s no noticed before the conscious mind can twist it into a yes.'),
    'G-S20': ('S20', 'Emulate\'s sentence (sample cm) for the paragraph\'s last one, without its quote marks around "social".'),
    'G-S21': ('S21', 'Emulate\'s "When you\'re done, make sure to come back the other way." (sample cm) for "And when you\'re done, '
                     'come back the other way."'),
    'G-S22': ('S22', 'Emulate\'s three sentences (sample cn): "And then read it out loud as you write it. Long, elegant sentences '
                     'are NOT going to help you when you’re trying to induce. It’s all soup to you at that point."'),
    'G-S23': ('S23', 'Emulate\'s first two sentences of the paragraph (sample cn): what you want to do, and what you don\'t want to '
                     'do today.'),
    'G-S24': ('S24', 'Emulate\'s "Make sure you\'re in a safe place to do this." (samples cm and co, word for word).'),
    'G-S25': ('S25', 'Emulate\'s version (sample cn) of the paragraph\'s first eight sentences: decide to do it, how to coax '
                     'yourself, preview the session; the old "this" kept in the second. The stop lines after them are card '
                     'S3b\'s and stay.'),
    'G-S26': ('S26', 'Emulate\'s "What is one next thing I can do?" (sample co) for "Give me one next action!"'),
    'G-S27': ('S27', 'Emulate\'s end of the first sentence ("if it has to do with trauma or memories", sample co of the next item) '
                     'and last sentence ("So take it as an image and get some outside help!", sample co); the middle sentence '
                     'stays.'),
    'G-S28': ('S28', 'Emulate\'s "Could you try it on a smaller scale?" (sample co), with the old sentence\'s "this" for "it".'),
    'G-S29': ('S29', 'Emulate\'s words (sample co) in place of his own three requests, ending on his own "today is for listening '
                     'or resting" (the sample\'s "listening to something" made it something outside you); the third ask is its own '
                     'sentence (the linter\'s list of three).'),
    'G-S30': ('S30', 'Emulate\'s "Have you got any sense of what it is that\'s making it feel fake?" (sample co).'),
    'G-S31': ('S31', 'Emulate\'s start (sample co), "You may have fooled yourself in the past", for his inner child guide\'s "Maybe '
                     'you\'ve fooled yourself before", ending on his own "and that part remembers"; his next sentence stays. (The '
                     'first draft, Emulate\'s two sentences, failed preservation: "this part knows it" lost his "remembers", and '
                     '"Try" lost his "works well here".)'),
    'G-S32': ('S32', 'Emulate\'s sentence (sample cn) in place of his own "An ethical one offers two genuinely safe routes.", with his '
                     '"genuinely" put back (the first draft dropped it and failed preservation).'),
    'G-S33': ('S33', 'Emulate\'s "Here is a little script you could use:" (sample cm); the heading says it is for anxiety.'),
    'G-S34': ('S34', 'Emulate\'s "Let’s see if I can find my body parts." (sample cn, its "Lets" typo fixed with the section\'s '
                     'curly apostrophe; the first draft\'s straight one failed all three reviewers) for the script\'s first question.'),
    'G-S36': ('S36', 'Emulate\'s "What’s theirs and what’s mine?" (sample cm) for "What is theirs? What is mine?". (The first draft also '
                     'had Emulate\'s "What boundaries do I need to set as a result?", which failed preservation; that question stays as '
                     'the working copy has it.)'),
}


def main(names):
    inputs_path = HERE / 'GATE-INPUTS.json'
    inputs = json.loads(inputs_path.read_text(encoding='utf-8')) if inputs_path.exists() else {}
    md = MASTER.read_text(encoding='utf-8')
    bl = sr.blocks(md)
    by = {sr.where(bl, b['i']): b['i'] for b in bl}
    cands = json.loads(CANDS.read_text(encoding='utf-8'))['spots']
    for name in names or list(DRAFTS):
        spot, change = DRAFTS[name]
        c = cands[spot]
        draft = c['new']
        i = by[c['where']]
        assert draft in bl[i]['text'], name
        h = max(b['i'] for b in bl[:i + 1] if b['level'])
        paras = []
        for b in bl[h + 1:]:
            if b['level']:
                break
            paras.append(b['text'])
        context = '\n\n'.join([bl[h]['text']] + paras)
        assert context.count(draft) == 1, name
        d = HERE / name
        d.mkdir(parents=True, exist_ok=True)
        (d / 'DRAFT.txt').write_text(draft, encoding='utf-8')
        (d / 'CONTEXT.txt').write_text(context + '\n', encoding='utf-8')
        (d / 'SOURCE.txt').write_text('The words it replaces: ' + c['old'] + '\n\nThe meaning to keep, and where it comes from: '
                                      + c['published'] + '\n', encoding='utf-8')
        if not (d / 'ADMISSION.json').exists():
            r = subprocess.run([sys.executable, str(GATE), 'init', '--draft', str(d / 'DRAFT.txt'), '--context', str(d / 'CONTEXT.txt'),
                                '--source', str(d / 'SOURCE.txt'), '--manifest', str(d / 'ADMISSION.json')], capture_output=True, text=True)
            if r.returncode not in (0, 1):
                print(name, 'init:', r.stdout[-400:], r.stderr[-400:])
        m = json.loads((d / 'ADMISSION.json').read_text(encoding='utf-8'))
        inputs[name] = {'folder': str(d), 'spot': spot, 'his': c['his'], 'the_change': change,
                        'candidate_sha256': m['candidate_sha256'], 'context_sha256': m['context_sha256'],
                        'source_sha256': m['source_sha256'], 'lint_verdict': m['lint']['verdict_at_init'],
                        'lint_findings': [{'label': f['label'], 'examples': f['examples']} for f in m['lint']['findings']]}
        print('%-6s lint %-6s %s | %s' % (name, m['lint']['verdict_at_init'], [f['label'][:40] for f in m['lint']['findings']], draft[:60]))
    inputs_path.write_text(json.dumps(inputs, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')


if __name__ == '__main__':
    main(sys.argv[1:])
