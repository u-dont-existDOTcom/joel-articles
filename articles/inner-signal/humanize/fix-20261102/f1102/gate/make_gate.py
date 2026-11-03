"""The owner-delivery gate for batch f1102's two card suggestions on Joel's own words (docs/HUMANIZATION-OWNER-DELIVERY-GATE.md;
tools/humanization/owner_delivery_gate.py): G-92, his inner child guide's rent line with its joke in brackets (C-92, the
c1102-92b wording), and G-480, his Core prompts caveat joined to the sentence before it (C-480). Each folder gets DRAFT.txt
(the new words), CONTEXT.txt (its paragraph's section as it would read) and SOURCE.txt (the words it replaces and the
meaning to keep); then init, the writer's ledger (every inventory row, a reason for each linter finding), GATE-INPUTS.json
and the three briefs, made from ../../w1102fix/gate/'s. The reviewers are fresh agents with only their brief and files.

  python3 articles/inner-signal/humanize/fix-20261102/f1102/gate/make_gate.py
"""
import hashlib
import json
import pathlib
import re
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
F = HERE.parent
H = F.parents[1]
ROOT = H.parents[2]
GATE = ROOT / 'tools' / 'humanization' / 'owner_delivery_gate.py'
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
sys.path.insert(0, str(F))
import make_f1102 as mf  # noqa: E402
import suggestion_review as sr  # noqa: E402

sha = lambda p: hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
ME = {'name': 'Claude Opus 5.5, the hypnosis guide lane\'s writer (the suggestions on his cards C-92 and C-480)',
      'context_id': 'session_01Mxpoi6tFT3FgKmBvtGjRtS'}
OLD92 = ("That’s one grown-up doing three jobs, not three more people moving in to help with the rent, and each job keeps the "
         "others in balance.")
OLD480 = ("Used together properly, the subconscious can feel safer in giving its response. That doesn't make the answers any more "
          "true, though.")
NEW480 = ("Used together properly, the subconscious can feel safer in giving its response, though that doesn't make the answers "
          "any more true.")
DRAFTS = {
    'G-92': {'block': 92, 'section': range(90, 94), 'old': OLD92, 'new': mf.C92B, 'card': 'C-92',
             'the_change': ('In his inner child guide\'s line in The inner child, the guards, and the inner adult\'s three jobs, "That’s one '
                            'grown-up doing three jobs, not three more people moving in to help with the rent, and each job keeps the '
                            'others in balance." becomes "It’s still one grown-up doing three jobs (nobody new is moving in to help with the '
                            'rent), and each job keeps the others in balance." His "That\'s X, not Y" line read AI (Low) in the first free '
                            'check of the whole guide and Human (Low) in the second; with the joke in brackets, its stretch read Human '
                            'Written, one window, High (c1102-92b, https://www.pangram.com/history/a1aff5ea-da51-415b-a4eb-cc3aef09e8e3).'),
             'source': ('THE WORDS IT REPLACES (his inner child guide\'s line, kept as he wrote it in this guide):\n' + OLD92 + '\n\n'
                        'THE MEANING TO KEEP: the three jobs are one grown-up, the reader, not three extra people (his joke: nobody '
                        'moves in to help with the rent), and each job keeps the others in balance. His party example right after it '
                        'shows the three jobs at work. Source: his inner child guide (articles/inner-signal/humanize/fix-20261025/'
                        'ic-align/IC-GUIDE.txt) and this guide as it stands.\n')},
    'G-480': {'block': 480, 'section': range(476, 481), 'old': OLD480, 'new': NEW480, 'card': 'C-480',
              'the_change': ('In Core prompts, his two sentences "Used together properly, the subconscious can feel safer in giving its '
                             'response. That doesn\'t make the answers any more true, though." become one: "Used together properly, the '
                             'subconscious can feel safer in giving its response, though that doesn\'t make the answers any more true." '
                             'His short last line read Human (Low) by itself in both free checks of the whole guide; joined, its stretch '
                             'read Human Written, the joined sentence in a High window (c1102-480, '
                             'https://www.pangram.com/history/99c37345-2641-4db2-be55-e4324087321d).'),
              'source': ('THE WORDS IT REPLACES (his own, from his answers of 2 November):\n' + OLD480 + '\n\n'
                         'THE MEANING TO KEEP: used together properly (the prompt and the NLP of Appendix B), the subconscious can feel '
                         'safer giving its answer, and that safety does not make the answers more true. Only the join changes: the '
                         'caveat becomes the sentence\'s last clause, every word of his kept but "That" (now "that") and the closing '
                         '"though" (moved to the front of the clause).\n')},
}
ROWS = ['T%02d' % i for i in range(1, 30)] + ['C01', 'C02', 'C03', 'C04']
NOTES = {
    'G-92': {
        'T01': 'no first person in the change', 'T02': 'one sentence inside a paragraph of explanation and example',
        'T03': 'nothing new arrives; his point and his joke are kept', 'T04': 'no scene in the change; his party example follows unchanged',
        'T05': 'no new prop; the rent is his', 'T06': 'no therapy abstraction added', 'T07': 'no filler; "still" carries the real turn (three named jobs, one person)',
        'T08': 'no explanation after an image', 'T09': 'one sentence', 'T10': 'no permission formula', 'T11': 'no bridge phrase',
        'T12': 'his "X, not Y" contrast is gone; nothing balanced is added', 'T13': 'his joke stays inside the line, in brackets',
        'T14': 'nothing moved', 'T15': 'the words are his but "It’s still" and "nobody new is"; the shape changes, the reveal is gone',
        'T16': 'the reflex negative reveal ("not three more people") is what the change removes', 'T17': 'his clause "each job keeps the others in balance" is kept as he wrote it',
        'T18': 'no premise and knock-down', 'T19': 'it announces nothing', 'T20': 'not a paragraph end; the party example follows',
        'T21': 'one claim and his joke', 'T22': 'no coach phrase', 'T23': 'no generic scenery', 'T24': 'no question', 'T25': 'no colon',
        'T26': '"three jobs" repeats the sentence before it, as his line did', 'T27': 'none of his tic words', 'T28': 'not a section end',
        'T29': 'not the paragraph\'s last sentence', 'C01': 'the inner child is not named in the change', 'C02': '"It" is the grown-up doing the jobs, as his "That" was',
        'C03': 'no first-person fact', 'C04': 'no named entity'},
    'G-480': {
        'T01': 'no first person', 'T02': 'one sentence, not a run of commands', 'T03': 'his caveat, nothing new',
        'T04': 'no scene', 'T05': 'no prop', 'T06': 'no therapy abstraction added', 'T07': 'no filler', 'T08': 'no image',
        'T09': 'one sentence', 'T10': 'no permission formula', 'T11': '"though" is his own word, moved to join the clause',
        'T12': 'no balanced pair', 'T13': 'his caveat is the thing noticed', 'T14': 'nothing moved but the clause join',
        'T15': 'his words, re-joined; no synonyms', 'T16': 'not a "not X, it\'s Y"', 'T17': 'his caveat, not a new principle',
        'T18': 'no knock-down sentence: the short flip is what the join removes', 'T19': 'announces nothing', 'T20': 'no short landing left: the caveat is a clause now',
        'T21': 'two of his points in one sentence, the second qualifying the first', 'T22': 'no coach phrase', 'T23': 'no scenery',
        'T24': 'no question', 'T25': 'no colon', 'T26': 'no repetition added', 'T27': 'none of his tic words', 'T28': 'his section ends on a caveat, not uplift',
        'T29': 'a new consideration (safety is not truth), not a restatement', 'C01': 'no naming', 'C02': '"that" is the subconscious feeling safer; "Used together properly" is his opening, unchanged',
        'C03': 'no first-person fact', 'C04': 'no named entity'},
}
LINT = {
    'E36/E41 heavy second person': 'The guide speaks to the reader as "you" throughout; the change adds no "you".',
    'O15 unusual spelling or hyphenation, his lines included (Joel 2026-10-07: "unusual spellings should help pass pangram, but that\'s also cheating"); a coinage or a rare word stays, a misspelling gets fixed: reparent': '"reparent" is his word for the whole practice, in his paragraph before the change; it is not in the change.',
    'B1 finished principle': 'His party example in the paragraph, unchanged, not the change.',
    'B4/E15 list or packed sentence': 'His two sentences joined: one claim and its caveat, nothing listed.',
    'D9 follows the source order': 'It replaces his line in place, so it follows that line\'s order by design.',
}


def main():
    md = (H / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
    inputs = {}
    for name, d in DRAFTS.items():
        f = HERE / name
        f.mkdir(exist_ok=True)
        raw = re.split(r'\n\s*\n', md.rstrip('\n'))
        assert raw[d['block']].count(d['old']) == 1, name
        raw[d['block']] = raw[d['block']].replace(d['old'], d['new'])
        bl = sr.blocks('\n\n'.join(raw) + '\n')
        (f / 'DRAFT.txt').write_text(d['new'], encoding='utf-8')
        (f / 'CONTEXT.txt').write_text('\n\n'.join(bl[i]['text'] for i in d['section']) + '\n', encoding='utf-8')
        (f / 'SOURCE.txt').write_text(d['source'], encoding='utf-8')
        args = ['--draft', str(f / 'DRAFT.txt'), '--context', str(f / 'CONTEXT.txt'), '--source', str(f / 'SOURCE.txt'),
                '--manifest', str(f / 'ADMISSION.json')]
        if not (f / 'ADMISSION.json').exists():
            p = subprocess.run([sys.executable, str(GATE), 'init'] + args, capture_output=True, text=True)
            assert p.returncode == 0 or (f / 'ADMISSION.json').exists(), p.stdout + p.stderr
        a = json.loads((f / 'ADMISSION.json').read_text(encoding='utf-8'))
        assert a['candidate_sha256'] == sha(f / 'DRAFT.txt') and a['context_sha256'] == sha(f / 'CONTEXT.txt')
        a['writer'] = ME
        judged = ' (judged: %s)' % d['new']
        a['tell_ledger'] = [{'id': r, 'status': 'ABSENT', 'evidence': NOTES[name][r] + judged, 'resolution': ''} for r in ROWS]
        for x in a['lint'].get('findings', []):
            lab = x['label']
            reason = next((v for k, v in LINT.items() if lab.startswith(k[:40])), None)
            assert reason, (name, lab)
            x['disposition'] = 'JUSTIFIED_KEEP'
            x['reason'] = reason
        a['review_files'] = {'preservation': 'REVIEW-preservation.json', 'cold_read_1': 'REVIEW-cold_read_1.json',
                             'cold_read_2': 'REVIEW-cold_read_2.json'}
        (f / 'ADMISSION.json').write_text(json.dumps(a, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
        inputs[name] = {'folder': str(f.relative_to(ROOT)), 'the_change': d['the_change'],
                        'candidate_sha256': a['candidate_sha256'], 'context_sha256': a['context_sha256'],
                        'source_sha256': a['source_sha256'],
                        'lint_findings': [{'label': x['label'], 'examples': x.get('examples', [])} for x in a['lint'].get('findings', [])]}
    (HERE / 'GATE-INPUTS.json').write_text(json.dumps(inputs, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    prev = F.parent / 'w1102fix' / 'gate'
    for role in ('preservation', 'cold_read_1', 'cold_read_2'):
        b = (prev / ('BRIEF-%s.md' % role)).read_text(encoding='utf-8')
        b = b.replace('/home/claude/ja-community/articles/inner-signal/humanize/fix-20261102/w1102fix/gate/GATE-INPUTS.json',
                      str(HERE / 'GATE-INPUTS.json'))
        b = b.replace('The NAMEs: G-672 (one NAME).', 'The NAMEs: G-92 and G-480 (two NAMEs).')
        b = b.replace('w1102f-gate-%s-subagent-a' % role, 'f1102-gate-%s-subagent-a' % role)
        b = b.replace('which read AI in a check of the whole guide though it read human to him by itself',
                      'which read AI or Human (Low) in a check of the whole guide')
        assert 'G-92 and G-480' in b and str(HERE / 'GATE-INPUTS.json') in b
        (HERE / ('BRIEF-%s.md' % role)).write_text(b, encoding='utf-8')
    print(json.dumps({k: {'candidate': v['candidate_sha256'][:12], 'lint': [x['label'][:40] for x in v['lint_findings']]} for k, v in inputs.items()}, indent=1))


if __name__ == '__main__':
    main()
