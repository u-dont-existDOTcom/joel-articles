"""Batch 467g (2026-10-20): the first fixes from the whole guide's Pangram 4.1 reading.

The Substack check of the guide (fix-20261020/substack41/RESULT-41a.json, mapped by fix-20261020/result41/map_windows.py)
read every installed section dark green except two: "Why doing it myself worked better for me" (HG12) and "When “your
voice” is everybody else’s voice" (HG15), each with two sentences red and some light green around them. Each edit names the
4.1 pattern it removes (docs/HUMANIZATION-GATE.md, "What Pangram 4.1 flagged in the community article"): a closer that
restates, sums up or reassures is cut or said plainly, a scripted "not X" contrast becomes two plain sentences, a set-up and
reveal becomes one sentence. Every point of the installed paragraph is kept.

  python3 articles/inner-signal/humanize/fix-20261020/b467/make_b467.py   (from the repo root)

Writes CANDIDATE.md (the working copy with the edits), drafts.json (the texts Pangram reads: each changed paragraph
alone and each section whole), the march draft and map, REWRITE.md (the changed paragraphs, for the stance check) and
VERIFY-PROMPT.txt (the meaning check of each edit against the installed paragraph).
"""
import json, pathlib, sys

REPO = pathlib.Path(__file__).resolve().parents[5]
H = REPO / 'articles' / 'inner-signal' / 'humanize'
OUT = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(H / 'tools'))
sys.path.insert(0, str(REPO / 'tools' / 'humanization' / 'reviewer'))
import sections as S          # noqa: E402
import reviewer as R          # noqa: E402

# HG12-p1e (one sentence for the set-up "that's not even the main reason" and the reveal "The bigger issue was trust and
# precision.", both light green) was dropped before the call: the march read the installed paragraph S B S and the edit
# S S, so the edit took out the paragraph's only break (pangram_gate.py E173); march.json keeps that read.
EDITS = [
    {'key': 'HG12-p3c', 'section': 'HG12', 'kind': 'cut',
     'old': " But doing it myself has one advantage nobody outside can copy: immediate dialogue with my own system.",
     'new': "",
     'window': '22 (AI-Generated, Medium, 17 words)',
     'diagnosis': 'patterns 2 and 3: an aphorism with a colon reveal that restates the paragraph\'s first sentence (the '
                  'hypnotist can\'t get that feedback because they aren\'t IN my mind); cut, as Joel cut the restating '
                  'sentences of the community article'},
    {'key': 'HG12-p7e', 'section': 'HG12', 'kind': 'edit',
     'old': "Ordinary interaction dissolved the state, but for a while it showed me a possibility my mind and heart may permit "
            "when the desire is sincere.",
     'new': "It wore off once I was back around people, but for a while it showed me that my mind and heart may allow this "
            "when the desire is sincere.",
     'window': '28 (AI-Generated, High, 25 words)',
     'diagnosis': 'pattern 2: an abstract summing-up closer ("dissolved the state", "a possibility my mind and heart may permit") '
                  'on a personal story; said plainly, "this" pointing at the state he has just described, the hedge kept'},
    {'key': 'HG15-p9e', 'section': 'HG15', 'kind': 'edit',
     'old': "Those can all be real gifts. They become a bargain for belonging when failing in these areas feels like losing "
            "yourself.",
     'new': "Those can be real gifts, but if failing at one of them feels like losing yourself, you're using it to buy "
            "belonging.",
     'window': '53 (AI-Generated, Low) and 54 (AI-Generated, Low)',
     'diagnosis': 'pattern 3 then 2: a short reassurance ("Those can all be real gifts.") and a balanced aphorism ("They become '
                  'a bargain for belonging when ..."); one plain sentence keeps both points, in the words the section\'s '
                  'own questions use ("buying my sense of belonging")'},
    {'key': 'HG15-p11e', 'section': 'HG15', 'kind': 'edit',
     'old': "The adult in you can answer, “We’re finding out whether we enjoy this, not proving our worth.”",
     'new': "The adult in you can answer, “We’re just finding out if we like this. We don’t have to prove our worth.”",
     'window': '56 (Human, Low, AI likelihood 0.33)',
     'diagnosis': 'pattern 6: a scripted "X, not Y" line (and Joel\'s ban on the "not X, Y" contrast), light green; two plain '
                  'sentences'},
]
SECTIONS = {'HG12': 'Why doing it myself worked better for me', 'HG15': 'When “your voice” is everybody else’s voice'}


def main():
    md = (H / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
    installed = md
    paras = {}
    blocks = [b for b in md.split('\n\n')]
    for e in EDITS:
        assert md.count(e['old']) == 1, (e['key'], md.count(e['old']))
        para = next(b for b in blocks if e['old'] in b)
        paras[e['key']] = (para, para.replace(e['old'], e['new']))
        md = md.replace(e['old'], e['new'])
    (OUT / 'CANDIDATE.md').write_text(md, encoding='utf-8')
    editor = H / 'source' / 'substack-editor-20260928.html'
    secs = {h: bl for h, bl in S.sections(md, str(editor))}
    drafts, meta = {}, {}
    for e in EDITS:
        was, new = paras[e['key']]
        drafts[e['key']] = S.plain(new)
        meta[e['key']] = {'section': e['section'], 'words': len(S.plain(new).split()), 'was_md': was, 'new_md': new}
    for key, title in SECTIONS.items():
        bl = secs['# ' + title]
        k = key + '-w467'
        drafts[k] = S.text_of(bl)
        meta[k] = {'section': key, 'words': len(drafts[k].split()), 'parts': [e['key'] for e in EDITS if e['section'] == key]}
        (OUT / ('%s-section.md' % key)).write_text('\n\n'.join(m for m, _ in bl) + '\n', encoding='utf-8')
    (OUT / 'drafts.json').write_text(json.dumps(drafts, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    (OUT / 'meta.json').write_text(json.dumps({'edits': EDITS, 'texts': meta}, ensure_ascii=False, indent=1) + '\n',
                                   encoding='utf-8')
    # the march draft: each edited paragraph as installed and as edited, in turn
    mparas, mp = [], []
    for e in EDITS:
        for ver, p in (('was', paras[e['key']][0]), ('new', paras[e['key']][1])):
            p = S.plain(p)
            n = len(R.march_paragraphs(p))
            if n:
                mparas.append(p)
                mp.append({'key': e['key'], 'ver': ver, 'n': n, 'start': sum(m['n'] for m in mp)})
    # written only when there's no march read yet: the read of 2026-10-20 (march-prompt.txt, march-labels.txt, decoded per
    # key in march.json) saw the five edits with HG12-p1e, so its draft isn't rewritten without it
    if not (OUT / 'march-labels.txt').exists():
        (OUT / 'march-draft.txt').write_text('\n\n'.join(mparas), encoding='utf-8')
        (OUT / 'march-map.json').write_text(json.dumps(mp, indent=1) + '\n', encoding='utf-8')
    # the stance check's rewrite: the edited paragraphs under their headings
    rw = []
    for key, title in SECTIONS.items():
        rw.append('# ' + title)
        rw += [paras[e['key']][1] for e in EDITS if e['section'] == key]
    (OUT / 'REWRITE.md').write_text('\n\n'.join(rw) + '\n', encoding='utf-8')
    # the meaning check
    pairs = []
    for i, e in enumerate(EDITS, 1):
        was, new = paras[e['key']]
        pairs.append('## Pair %d (%s)\n\nINSTALLED:\n%s\n\nEDITED:\n%s\n' % (i, e['key'], S.plain(was), S.plain(new)))
    prompt = (
        "You check that a small edit of a paragraph keeps its meaning. Below are %d pairs from a long self-hypnosis guide by "
        "Joel, written in his first person. In each pair the INSTALLED paragraph is the one in the guide now and the EDITED "
        "one changes or cuts a sentence or two of it.\n\nFor each pair, list every point the installed paragraph makes (a "
        "claim, a fact about Joel, a step, a caution, a condition, a hedge such as \"I suspect\" or \"may\") and say whether "
        "the edited paragraph keeps it: KEPT, CHANGED (how a reader would now understand it differently) or LOST. Then list "
        "anything the edited paragraph says that the installed one doesn't: ADDED. Judge meaning only, not style or which "
        "version is better, and don't suggest rewrites. Keep your reasoning short.\n\nWrite your report with a single Write "
        "call to `%s`, one \"## Pair N\" part per pair, ending each with one line `VERDICT: OK` (every point kept, nothing "
        "added) or `VERDICT: CHANGED` (anything changed, lost or added), then reply with only the verdicts. Don't read any "
        "other file, don't run commands, and don't use the web.\n\n%s" % (len(EDITS), OUT / 'VERIFY.md', '\n'.join(pairs)))
    (OUT / 'VERIFY-PROMPT.txt').write_text(prompt, encoding='utf-8')
    for k, v in drafts.items():
        print(k, len(v.split()), 'words')
    print(len(mp), 'march paragraphs')


if __name__ == '__main__':
    main()
