"""Batch 468g's gate records (2026-10-21), then the in-page batch through the gate.

The texts are ./drafts.json (make_b468.py). Each record cites its reviews: the march read of the installed paragraph and
the edit (march-labels.txt, decoded here into march.json by march-map.json), the cold read of its section (SENSE-*.md),
the meaning check (VERIFY.md) and the stance check (STANCE.md). A reviewer's finding that is answered rather than fixed
is answered in gate-answers.json, which fills or overrides these records. Only the paragraph texts go in this batch: each
section's recheck (its one recheck, the budget rule) waits until its paragraphs read Human.

  python3 articles/inner-signal/humanize/fix-20261020/b468/make_gate_b468.py   (from the repo root)
"""
import json, pathlib, re, subprocess, sys

REPO = pathlib.Path(__file__).resolve().parents[5]
B = pathlib.Path(__file__).resolve().parent
OUT = B / 'batch'
FEED_A = 'https://www.pangram.com/feed/fd91cf34-925f-48ca-8100-5fee8d5766c4'
FEED_B = 'https://www.pangram.com/feed/6a48b3ce-6631-4c99-aec3-b127409dc2f8'
HIST = 'https://www.pangram.com/history/'
KEYS = ['HG15-p9e2', 'HG35-forgive-e3', 'HG35-quote-e', 'HG35-selfforgive-e']


def rel(p):
    return str(pathlib.Path(p).resolve().relative_to(REPO))


def march_reads():
    """march.json from the reader's labels: {key: {'was': [labels per paragraph], 'new': [...]}}."""
    labels = dict(re.findall(r'^\s*T(\d+):\s*([SB ]+?)\s*$', (B / 'march-labels.txt').read_text(encoding='utf-8'), re.M))
    out = {}
    for m in json.loads((B / 'march-map.json').read_text(encoding='utf-8')):
        seq = [labels[str(m['start'] + j + 1)] for j in range(m['n'])]
        out.setdefault(m['key'], {})[m['ver']] = seq
    (B / 'march.json').write_text(json.dumps(out, indent=1) + '\n', encoding='utf-8')
    return out


def main():
    OUT.mkdir(exist_ok=True)
    drafts = json.loads((B / 'drafts.json').read_text(encoding='utf-8'))
    meta = json.loads((B / 'meta.json').read_text(encoding='utf-8'))['texts']
    mr = march_reads()
    hg35_40 = '453g HG35-rfix (Pangram 4.0), 100%% Human: %s0bbc85f4-a5d1-4383-b09d-447f3a7d7f30' % HIST
    rec = {
        'HG15-p9e2': {
            'was': '455g HG15-smp (Pangram 4.0), 100%% Human: %s1ced6e80-dfa7-4825-ba6e-e7e00c8a0b5e; Pangram 4.1, the whole '
                   'guide: its last two sentences read AI, low (windows 53 and 54, %s); try 1, 467g HG15-p9e: AI, medium '
                   '(%s6e97d63f-765f-4e8d-aecc-39ca783c05fa)' % (HIST, FEED_A, HIST),
            'was_kind': 'emulate', 'lint_was': 'REVIEW'},
        'HG35-forgive-e3': {
            'was': '%s; Pangram 4.1, part B: the question and the colon list read AI, low and high (windows 19 and 20, %s); '
                   'try 1, 467g HG35-forgive-e2: AI, medium and high (%s25833096-c587-4602-b24d-ba7affdfbcf3)'
                   % (hg35_40, FEED_B, HIST),
            'was_kind': 'emulate', 'lint_was': 'FAIL'},
        'HG35-quote-e': {
            'was': '%s; Pangram 4.1, the section check 467g HG35-w467: its first two sentences read AI, low '
                   '(%s74763536-ab88-4ec2-b347-0e186b0208ad); light green in part B (%s)' % (hg35_40, HIST, FEED_B),
            'was_kind': 'emulate', 'lint_was': 'REVIEW'},
        'HG35-selfforgive-e': {
            'was': '%s; Pangram 4.1, the section check 467g HG35-w467: the paragraph read AI, low '
                   '(%s74763536-ab88-4ec2-b347-0e186b0208ad); light green in part B (%s)' % (hg35_40, HIST, FEED_B),
            'was_kind': 'emulate', 'lint_was': 'FAIL'},
    }
    for k, r in rec.items():
        r.update({'kind': 'edit', 'march_was': mr[k]['was'], 'march': mr[k]['new'], 'march_reads': rel(B / 'march.json'),
                  'cold': None, 'cold_read': rel(B / ('SENSE-%s.md' % meta[k]['section'])),
                  'grounding': None, 'grounding_note': rel(B / 'VERIFY.md'),
                  'stance': None, 'stance_note': rel(B / 'STANCE.md'), 'missing': [], 'words': meta[k]['words']})
    over = B / 'gate-answers.json'
    if over.exists():
        for k, v in json.loads(over.read_text(encoding='utf-8')).items():
            rec[k].update(v)
    (OUT / 'drafts.json').write_text(json.dumps({k: drafts[k] for k in KEYS}, ensure_ascii=False, indent=1) + '\n',
                                     encoding='utf-8')
    (OUT / 'GATE.json').write_text(json.dumps(rec, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    r = subprocess.run([sys.executable, str(REPO / 'tools' / 'humanization' / 'pangram_gate.py'), str(OUT / 'drafts.json'),
                        str(OUT / 'GATE.json'), str(OUT / 'b468.js'), '--name', 'B468log', '--lint-article',
                        str(REPO / 'articles' / 'inner-signal' / 'humanize' / 'HUMANIZED-SO-FAR.md')] + KEYS,
                       capture_output=True, text=True, cwd=REPO)
    print(r.stdout[-3000:], r.stderr[-2000:])
    return r.returncode


if __name__ == '__main__':
    sys.exit(main())
