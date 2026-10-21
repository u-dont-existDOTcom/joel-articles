"""Batch 467g's texts and gate records (2026-10-20/21), then the in-page batch through the gate.

The texts are part 1's (HG12, HG15: ./drafts.json) and part 2's (HG33, HG35: ./part2/drafts.json). Each edit's record
cites its reviews: the march read of the installed paragraph and the edit (march.json of the round named), the cold read
of its section (SENSE-*.md), the meaning check (VERIFY*.md), the stance check (STANCE.md) and, for a section, the
repeats check (REPEATS.md). Where a reviewer's finding is answered rather than fixed, the answer is in the record.

  python3 articles/inner-signal/humanize/fix-20261020/b467/make_gate_b467.py   (from the repo root)

Then: python3 tools/humanization/pangram_gate.py batch/drafts.json batch/GATE.json batch/b467.js --name B467log
      --lint-article articles/inner-signal/humanize/HUMANIZED-SO-FAR.md KEY ...   (this script runs it)
"""
import json, pathlib, subprocess, sys

REPO = pathlib.Path(__file__).resolve().parents[5]
B = pathlib.Path(__file__).resolve().parent
P2 = B / 'part2'
OUT = B / 'batch'
FEED_A = 'https://www.pangram.com/feed/fd91cf34-925f-48ca-8100-5fee8d5766c4'
FEED_B = 'https://www.pangram.com/feed/6a48b3ce-6631-4c99-aec3-b127409dc2f8'
HIST = 'https://www.pangram.com/history/'


def rel(p):
    return str(pathlib.Path(p).resolve().relative_to(REPO))


def main():
    OUT.mkdir(exist_ok=True)
    d1 = json.loads((B / 'drafts.json').read_text(encoding='utf-8'))
    d2 = json.loads((P2 / 'drafts.json').read_text(encoding='utf-8'))
    m1 = json.loads((B / 'meta.json').read_text(encoding='utf-8'))
    m2 = json.loads((P2 / 'meta.json').read_text(encoding='utf-8'))
    drafts = dict(d1, **d2)
    meta = dict(m1['texts'], **m2['texts'])
    plain = lambda md: __import__('re').sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', md).replace('*', '').strip()
    stance_1 = ('0: STANCE.md (round 1, the whole published essay) found no conflict in the edited sentences; its six '
                'findings are in installed text these edits keep (the edit it flagged, HG12-p1e, was dropped)')
    rec = {
        'HG12-p3c': {
            'kind': 'edit', 'was': '434g HG12-fix (Pangram 4.0), 100%% Human: %s781080d2-867c-4e50-9250-c8a6899036b8; Pangram 4.1, '
                                   'the whole guide: this sentence read AI, medium (window 22, %s)' % (HIST, FEED_A),
            'was_kind': 'emulate', 'lint_was': 'FAIL', 'cut_of': plain(meta['HG12-p3c']['was_md']),
            'march_was': ['S B S'], 'march': ['S B'], 'march_reads': rel(B / 'r1' / 'march.json'),
            'cold': 'OK', 'cold_read': rel(B / 'SENSE-HG12.md') + ' (P3 OK)',
            'grounding': 'OK',
            'grounding_note': 'r1/VERIFY.md pair 2 calls the cut sentence LOST; it is the restatement itself: the first sentence '
                              'says a hypnotist outside can\'t get that feedback since they aren\'t IN my mind, the same point '
                              'from the other side (AGENTS.md: a cut with genuine semantic equivalence). Round 2 kept the "But" '
                              'by putting the concession first, and lost the paragraph\'s break (r2/march.json)',
            'stance': 0, 'stance_note': stance_1, 'missing': []},
        'HG12-p7e': {
            'kind': 'edit', 'was': '434g HG12-fix (Pangram 4.0), 100%% Human: %s781080d2-867c-4e50-9250-c8a6899036b8; Pangram 4.1, '
                                   'the whole guide: its last sentence read AI, high (window 28, %s)' % (HIST, FEED_A),
            'was_kind': 'emulate', 'lint_was': 'FAIL',
            'march_was': ['S S B S S B B'], 'march': ['S S B S S B B'], 'march_reads': rel(B / 'r2' / 'march.json'),
            'cold': 'OK', 'cold_read': rel(B / 'SENSE-HG12.md') + ' (P6: "when the desire is sincere" is the installed phrase, '
                                                                 'and the reader\'s best reading is the meant one)',
            'grounding': 'OK',
            'grounding_note': 'r2/VERIFY.md pair 2: every point kept; "made it wear off" for "dissolved the state" and "with '
                              'people" (whom the interaction is with; the next paragraph says he had to talk to people) are '
                              'the same in context',
            'stance': 0, 'stance_note': stance_1, 'missing': []},
        'HG15-p9e': {
            'kind': 'edit', 'was': '455g HG15-smp (Pangram 4.0), 100%% Human: %s1ced6e80-dfa7-4825-ba6e-e7e00c8a0b5e; Pangram 4.1, '
                                   'the whole guide: its last two sentences read AI, low (windows 53 and 54, %s)' % (HIST, FEED_A),
            'was_kind': 'emulate', 'lint_was': 'FAIL',
            'march_was': ['B S B S'], 'march': ['B S S'], 'march_reads': rel(B / 'r2' / 'march.json'),
            'cold': 'OK', 'cold_read': rel(B / 'SENSE-HG15.md') + ' (P12 OK)',
            'grounding': 'OK', 'grounding_note': 'r2/VERIFY.md pair 3: OK',
            'stance': 0, 'stance_note': stance_1, 'missing': []},
        'HG15-p11t': {
            'kind': 'edit', 'was': '455g HG15-smp (Pangram 4.0), 100%% Human: %s1ced6e80-dfa7-4825-ba6e-e7e00c8a0b5e; Pangram 4.1, '
                                   'the whole guide: this paragraph read Human (high, the adult\'s line low; windows 55-57, %s)'
                                   % (HIST, FEED_A),
            'was_kind': 'emulate', 'lint_was': 'FAIL',
            'march_was': ['S S S S S S'], 'march': ['S S S S S S'],
            'march_reads': rel(B / 'r1' / 'march.json') + ' (HG15-p11e "was": the installed paragraph; the term fix changes one '
                                                       'word and no sentence\'s job)',
            'cold': None, 'cold_read': rel(B / 'SENSE-HG15.md'),
            'grounding': None, 'grounding_note': rel(B / 'VERIFY-p11t.md'),
            'stance': 0, 'stance_note': 'resolves STANCE.md finding 6 (round 1): "inner parent" for the voice the guide calls '
                                        'the inherited parent', 'missing': []},
        'HG33-buteyko-e': {
            'kind': 'edit', 'was': '455g HG33-rfix2 (Pangram 4.0), 100%% Human: %s52ded84a-c50d-440f-8e4d-68df4cb3835e; Pangram 4.1, '
                                   'part B: this sentence read AI, low (window 12, %s)' % (HIST, FEED_B),
            'was_kind': 'emulate', 'lint_was': 'FAIL',
            'march_was': ['S S S S S B S'], 'march': ['S S S S S S B S'], 'march_reads': rel(P2 / 'march.json'),
            'cold': 'OK', 'cold_read': rel(P2 / 'SENSE-HG33.md') + ' (P4\'s note is the installed "Then")',
            'grounding': 'OK', 'grounding_note': rel(P2 / 'r1' / 'VERIFY.md') + ' pair 1: OK',
            'stance': None, 'stance_note': rel(P2 / 'STANCE.md'), 'missing': []},
        'HG35-forgive-e2': {
            'kind': 'edit', 'was': '453g HG35-rfix (Pangram 4.0), 100%% Human: %s0bbc85f4-a5d1-4383-b09d-447f3a7d7f30; Pangram 4.1, '
                                   'part B: the question and the colon list read AI, low and high (windows 19 and 20, %s)'
                                   % (HIST, FEED_B),
            'was_kind': 'emulate', 'lint_was': 'FAIL',
            'march_was': ['S S B S'], 'march': ['S S B S S S'], 'march_reads': rel(P2 / 'march.json'),
            'cold': None, 'cold_read': rel(P2 / 'SENSE-HG35-e2.md'),
            'grounding': None, 'grounding_note': rel(P2 / 'VERIFY.md'),
            'stance': None, 'stance_note': rel(P2 / 'STANCE.md'), 'missing': []},
    }
    repeats_answer = None   # gate-answers.json gives each section's answer to its repeats check
    rec['HG12-w467'] = {'kind': 'section', 'parts': ['HG12-p3c', 'HG12-p7e', 'installed'], 'repeats': repeats_answer,
                        'repeats_read': rel(B / 'REPEATS.md')}
    rec['HG15-w467'] = {'kind': 'section', 'parts': ['HG15-p9e', 'HG15-p11t', 'installed'], 'repeats': repeats_answer,
                        'repeats_read': rel(B / 'REPEATS.md')}
    rec['HG33-w467'] = {'kind': 'section', 'parts': ['HG33-buteyko-e', 'installed'], 'repeats': None,
                        'repeats_read': rel(P2 / 'REPEATS.md')}
    rec['HG35-w467'] = {'kind': 'section', 'parts': ['HG35-forgive-e2', 'installed'], 'repeats': None,
                        'repeats_read': rel(P2 / 'REPEATS.md')}
    over = B / 'gate-answers.json'   # the answers filled in once the pending reviews are read
    if over.exists():
        for k, v in json.loads(over.read_text(encoding='utf-8')).items():
            rec[k].update(v)
    for k, r in rec.items():
        if k in meta:
            r['words'] = meta[k]['words']
    keys = list(rec)
    (OUT / 'drafts.json').write_text(json.dumps({k: drafts[k] for k in keys}, ensure_ascii=False, indent=1) + '\n',
                                     encoding='utf-8')
    (OUT / 'GATE.json').write_text(json.dumps(rec, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'pangram_gate.py'), str(OUT / 'drafts.json'),
                        str(OUT / 'GATE.json'), str(OUT / 'b467.js'), '--name', 'B467log', '--lint-article',
                        str(REPO / 'articles' / 'inner-signal' / 'humanize' / 'HUMANIZED-SO-FAR.md')] + keys,
                       capture_output=True, text=True, cwd=REPO)
    print(r.stdout[-3000:], r.stderr[-2000:])
    return r.returncode


if __name__ == '__main__':
    sys.exit(main())
