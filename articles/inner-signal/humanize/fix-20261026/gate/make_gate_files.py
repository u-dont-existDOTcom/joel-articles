#!/usr/bin/env python3
"""The owner-delivery gate's files (docs/HUMANIZATION-OWNER-DELIVERY-GATE.md) for the Emulate splices that go on Joel's
next marking page: batch 479's six that read Human in place (../../fix-20261025/b479/CANDIDATES.json: S2, S3a, S3b, S4,
S5, S6) and batch 480's (../b480/CANDIDATES.json: S7 to S10, added once their API checks are in). Emulate's words are
model-written words in his byline, so each passes the gate before the page shows it as a proposed change; his own words
(S1, his inner child guide's whole sentence) are outside it. The same files and steps as the Emulate check pages' gate
(../../fix-20261025/emulate-check/gate/).

Each NAME gets DRAFT.txt (the exact new words, as the page shows them), CONTEXT.txt (its section as it would read with
every candidate in, from ../b480/CANDIDATE-MASTER.md, holding the draft once) and SOURCE.txt (the words it replaces and the
line the meaning comes from), then `owner_delivery_gate.py init` writes ADMISSION.json. GATE-INPUTS.json gives the
reviewers each NAME's folder, change and hashes.

  python3 articles/inner-signal/humanize/fix-20261026/gate/make_gate_files.py [NAME ...]   (from the repo root; no NAME: all)
"""
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
H = ROOT / 'articles/inner-signal/humanize'
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import suggestion_review as sr  # noqa: E402

GATE = ROOT / 'tools' / 'humanization' / 'owner_delivery_gate.py'
MASTER = H / 'fix-20261026' / 'b480' / 'CANDIDATE-MASTER.md'
BATCH = {'b479': H / 'fix-20261025' / 'b479' / 'CANDIDATES.json', 'b480': H / 'fix-20261026' / 'b480' / 'CANDIDATES.json'}
# NAME: (batch, spot, the change in words)
DRAFTS = {
    'G-S2': ('b479', 'S2', 'Emulate\'s borrowed adulthood paragraph (sample ch) in place of the one that read AI, with his two published points '
                          'put back: the practices are familiar ones, and he doesn\'t claim the whole sequence is proven as one treatment.'),
    'G-S3a': ('b480', 'S3a2', 'Emulate\'s pointer to the "Already open? Contain before you deepen" section (batch 479\'s sample ci), with the '
                             'heading\'s own words, his "later" and his "not stable", in place of the one that read AI; "you can" dropped '
                             'for the linter\'s coach register.'),
    'G-S3b': ('b479', 'S3b', 'Emulate\'s three stop lines (sample cg: say \'stop\', \'less\', \'quiet\') in place of the two sentences that '
                            'read AI.'),
    'G-S4': ('b479', 'S4', 'Emulate\'s sentence (sample ci) in place of his own two from his inner child guide, which read AI here: make '
                          'sense, and anything big or hard to undo waits until you\'re calm and checked against what you know.'),
    'G-S5': ('b480', 'S5b', 'Emulate\'s sentence (batch 479\'s sample ch) for the no-warmth fallback the inner child alignment added '
                           'from his inner child guide, which read AI here, ending on his own words from that guide, "no faking '
                           'required" (Emulate\'s "You don\'t have to fake it!" failed the linter; "Don\'t fake it." failed the '
                           'preservation review as a rule).'),
    'G-S6': ('b479', 'S6', 'Emulate\'s question (sample cg) for his published test, with his "this way of responding" in place of '
                          'Emulate\'s "it".'),
    'G-S7': ('b480', 'S7', 'Emulate\'s two sentences (sample cl) for his inner child guide\'s three-jobs sentence, which read AI here; '
                          'the rent joke and the balance kept, and his "keeps" put back for Emulate\'s "helps to keep".'),
    'G-S8': ('b480', 'S8', 'Emulate\'s two sentences (sample ck) in place of the inner child alignment\'s two that read AI: ask what '
                          'it\'s trying to stop or wants before deciding what it is; it may be the child, the script, the day, or a mix. '
                          'Its last words are the approved card\'s ("or a bit of each", for Emulate\'s "or a combination").'),
    'G-S9': ('b480', 'S9', 'Emulate\'s three sentences (samples cj and ck) in place of the two that read AI: what the inherited parent '
                          'script is, that it isn\'t always a voice, and that it isn\'t the inner adult you build. The paragraph\'s '
                          '"This" put back for Emulate\'s "It" in the last one.'),
    'G-S10': ('b480', 'S10', 'Emulate\'s sentence (sample cl) in place of the inner child guide\'s "Borrowed is fine, ...", which read AI '
                            'here.'),
}


def main(names):
    inputs_path = HERE / 'GATE-INPUTS.json'
    inputs = json.loads(inputs_path.read_text(encoding='utf-8')) if inputs_path.exists() else {}
    md = MASTER.read_text(encoding='utf-8')
    bl = sr.blocks(md)
    by = {sr.where(bl, b['i']): b['i'] for b in bl}
    cands = {k: json.loads(p.read_text(encoding='utf-8'))['spots'] for k, p in BATCH.items() if p.exists()}
    for name in names or list(DRAFTS):
        batch, spot, change = DRAFTS[name]
        c = dict(cands[batch][spot])
        if 'published' not in c or not c['published']:
            raise SystemExit(name + ': no meaning source')
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
        inputs[name] = {'folder': str(d), 'the_change': change, 'candidate_sha256': m['candidate_sha256'],
                        'context_sha256': m['context_sha256'], 'source_sha256': m['source_sha256'],
                        'lint_verdict': m['lint']['verdict_at_init'],
                        'lint_findings': [{'label': f['label'], 'examples': f['examples']} for f in m['lint']['findings']]}
        print('%-6s lint %-6s %s | %s' % (name, m['lint']['verdict_at_init'], [f['label'] for f in m['lint']['findings']], draft[:70]))
    inputs_path.write_text(json.dumps(inputs, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')


if __name__ == '__main__':
    main(sys.argv[1:])
