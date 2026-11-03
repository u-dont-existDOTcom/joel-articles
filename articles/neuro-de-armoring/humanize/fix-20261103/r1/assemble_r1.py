"""Round 1 of the neuro de-armoring rewrite, after Joel's answer to question 1 (2026-11-03, after his message of 15:22
UTC: "Freely, in your voice"): each section rewritten in his voice, every compound, dose, unit, timing and warning kept
(FIDELITY-KEYS.json, fidelity_keys.py check), nothing added that he hasn't said, his Human (High) stretches word for word
(the introduction, and the D-serine paragraph in Part 4).

sections/SNN.md is a section's new Markdown, from its heading in master.md to the line before the next section's heading
(SECTIONS below, the baseline's ten sections). This script puts every section file there is into master.md's place for
it (CANDIDATE.md), runs the fidelity check on the whole, and cuts each rewritten section into the stretches the API may
check (gate E325: at most six paragraphs of eight words or more, and 1,200 words; a cut goes before a heading when it
can), the text as the post reads it (no Markdown marks, link text kept, images and the video's placeholder left out).

  python3 articles/neuro-de-armoring/humanize/fix-20261103/r1/assemble_r1.py [--only S02 S06 ...]
Writes CANDIDATE.md, STRETCHES.json (every stretch, with its section and blocks) and TEXTS.json (the stretches of the
sections named by --only, or of every rewritten section) here; exits 1 when the fidelity check fails.
"""
import argparse
import hashlib
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parents[1]
ART = H.parent
ROOT = ART.parents[1]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import suggestion_review as sr  # noqa: E402

MASTER_SHA = 'a4b4e05ae5b6930519e79708f0d7dbedf5cb4f9c6158bf2efd60121501fdef0f'
SECTIONS = [
    ('S01', '# Introduction'),
    ('S02', '## Psychology is the Software; Biology is the Hardware.'),
    ('S03', '### Part 1: THE SCIENCE (Why We Do This)'),
    ('S04', '#### C. The “Hardened” Circuit: Dynorphin & DeltaFosB'),
    ('S05', '## Part 2: Reducing Anxiety & Depression'),
    ('S06', '### Dopamine Receptor Burnout / DAWS Pattern: Uridine Monophosphate'),
    ('S07', '### Serotonin Bottleneck Pattern: 5-HTP + Low-Dose P5P'),
    ('S08', '## Part 3: THE SHIELD (Flu-Proofing & Voltage Control)'),
    ('S09', '## Part 4: THE JAMMER (Acute Symptom Management)'),
    ('S10', '## Part 5: THE TIMELINE (The 8-Week Path)'),
]
SKIP = {'Double click to interact with video'}
# His paragraphs that read Human (High) in the baseline (../../fix-20261102/baseline/API-ROUND1.log) and stay word for
# word: they aren't in the stretches, so a stretch's result is about the rewritten text around them (a known-Human
# paragraph isn't used to carry a rewritten one, SKILL.md's owner-delivery admission).
KNOWN_HUMAN = ('Introduction', 'When people tell me they have trauma', 'This protocol is partly theoretical',
               'Recent neuroscience (Tian-Ming Gao', 'Advanced tactic: The D-Serine Memory Re-consolidator.',
               'D-serine has shown efficacy', 'The Stack: Microdose Iboga Nasal Spray', 'Fun with fungi:',
               'Phosphatidylserine 300–600 mg earlier in the day only if', 'Transition: Consider moving to Strategy B')
MAX_P, MAX_W = 6, 1200


def segments(md):
    lines = md.split('\n')
    idx = []
    for key, head in SECTIONS:
        hits = [n for n, l in enumerate(lines) if l == head]
        assert len(hits) == 1, (key, head, hits)
        idx.append(hits[0])
    assert idx == sorted(idx)
    return lines, idx


def readable(block):
    return not (block['kind'] == 'image' or block['text'].startswith('image ') and len(block['text'].split()) <= 2) \
        and block['text'] not in SKIP


def stretches(blocks):
    """Cut a section's blocks into the fewest stretches the API takes, about equal in paragraphs, each cut moved to just
    before a heading when one is within a paragraph of it (a heading goes with what it heads)."""
    def size(bs):
        # pangram_api.py's count: every block of eight words or more, a long heading included
        return sum(1 for b in bs if len(b['text'].split()) >= 8), sum(len(b['text'].split()) for b in bs)

    paras, words = size(blocks)
    n = max(1, -(-paras // MAX_P), -(-words // MAX_W))
    while True:
        target = paras / n
        cuts, count = [], 0
        for i, b in enumerate(blocks):
            if len(b['text'].split()) >= 8:
                count += 1
            if len(cuts) < n - 1 and count >= target * (len(cuts) + 1) and i + 1 < len(blocks):
                c = i + 1
                for j in (c - 1, c + 1):     # a heading within one block of the cut: cut before it
                    if 0 < j < len(blocks) and blocks[j]['level']:
                        c = j
                        break
                cuts.append(c)
        bounds = [0] + sorted(set(cuts)) + [len(blocks)]
        out = [blocks[bounds[k]:bounds[k + 1]] for k in range(len(bounds) - 1) if bounds[k] < bounds[k + 1]]
        # a stretch may not end on a heading
        for k in range(len(out) - 1):
            while out[k] and out[k][-1]['level']:
                out[k + 1].insert(0, out[k].pop())
        out = [s for s in out if s]
        if all(size(s)[0] <= MAX_P and size(s)[1] <= MAX_W for s in out):
            return out
        n += 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--only', nargs='*')
    a = ap.parse_args()
    md = (ART / 'master.md').read_text(encoding='utf-8')
    assert hashlib.sha256(md.encode('utf-8')).hexdigest() == MASTER_SHA
    lines, idx = segments(md)
    out, done = lines[:idx[0]], []
    for n, (key, head) in enumerate(SECTIONS):
        end = idx[n + 1] if n + 1 < len(idx) else len(lines)
        f = HERE / 'sections' / (key + '.md')
        if f.exists():
            new = f.read_text(encoding='utf-8').rstrip('\n').split('\n')
            out += new + ['']
            done.append(key)
        else:
            out += lines[idx[n]:end]
    cand = '\n'.join(out).rstrip('\n') + '\n'
    (HERE / 'CANDIDATE.md').write_text(cand, encoding='utf-8')
    fk = subprocess.run([sys.executable, str(ROOT / 'tools' / 'humanization' / 'fidelity_keys.py'), 'check',
                         str(H / 'FIDELITY-KEYS.json'), str(HERE / 'CANDIDATE.md')], capture_output=True, text=True)
    print(fk.stdout.strip()[-3000:])
    # the stretches, from the candidate's blocks section by section
    cl, cidx = segments_candidate(cand, done)
    rows, texts = [], {}
    for key in done:
        sec = [b for b in cl[key] if readable(b) and not (b['text'] == 'Introduction' or b['text'].startswith(KNOWN_HUMAN[1:]))]
        for k, s in enumerate(stretches(sec)):
            name = 'r1-%s%s' % (key, 'abcdefgh'[k])
            t = '\n\n'.join(b['text'] for b in s)
            rows.append({'key': name, 'section': key, 'blocks': [s[0]['i'], s[-1]['i']], 'words': len(t.split()),
                         'paragraphs': sum(1 for b in s if len(b['text'].split()) >= 8),
                         'sha256': hashlib.sha256(t.encode('utf-8')).hexdigest(), 'first': s[0]['text'][:80]})
            if not a.only or key in a.only:
                texts[name] = t
    (HERE / 'STRETCHES.json').write_text(json.dumps(rows, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    (HERE / 'TEXTS.json').write_text(json.dumps(texts, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print('candidate', hashlib.sha256(cand.encode('utf-8')).hexdigest()[:12], '| rewritten:', ' '.join(done))
    for r in rows:
        print(' ', r['key'], r['paragraphs'], 'paragraphs', r['words'], 'words |', r['first'][:60],
              '| in TEXTS' if r['key'] in texts else '')
    return fk.returncode


def segments_candidate(cand, done):
    """The candidate's blocks for each rewritten section: from the section file's first heading to the next section's."""
    bl = sr.blocks(cand)
    lines = cand.split('\n')
    heads = {}
    for key, head in SECTIONS:
        f = HERE / 'sections' / (key + '.md')
        h = f.read_text(encoding='utf-8').split('\n')[0] if f.exists() else head
        heads[key] = h.lstrip('#').strip()
    order = [k for k, _ in SECTIONS]
    pos = {}
    for key in order:
        hits = [b['i'] for b in bl if b['level'] and b['text'] == heads[key]]
        assert hits, (key, heads[key])
        pos[key] = hits[0]
    res = {}
    for n, key in enumerate(order):
        end = pos[order[n + 1]] if n + 1 < len(order) else len(bl)
        res[key] = bl[pos[key]:end]
    return res, pos


if __name__ == '__main__':
    sys.exit(main())
