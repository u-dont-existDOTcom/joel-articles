#!/usr/bin/env python3
"""Turn 132's two tests, scored by code into RESULTS.md (AGENTS.md: numbers Joel comes back to are computed in the repo).

  python3 score_t132.py            # rewrites RESULTS.md beside this file

Order test: every outline in order-test/out/ against his own reorganization (order/score_order.py, his 20 re-parentings
and 15 level changes). Heading test: the three fresh runs with RULES-HEADINGS.md in heading-test/out/, against his picks
(HIS-PICKS-RESOLVED.json): exact matches, and a blind judge's same/close/different (heading-judge/, a Sonnet reader that
saw the candidates shuffled as A, B and C, never the run names; KEY-do-not-show-judge.json unblinds them)."""
import collections
import json
import pathlib
import re
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / 'order'))
import score_order  # noqa: E402


def norm(s):
    s = str(s).translate(str.maketrans({'’': "'", '‘': "'", '“': '"', '”': '"'}))
    return re.sub(r'\s+', ' ', s).strip()


def order_rows():
    rows = []
    base = score_order.score(score_order.BASE)
    rows.append(('4 November order, unchanged', base))
    for p in sorted((HERE / 'order-test' / 'out').glob('*.json')):
        if p.name.startswith('GPT-plain') or p.name.startswith('GPT-rules'):
            continue  # the same answers as GPT-gpt-*-OUTLINE.json, under a second name
        ok = subprocess.run([sys.executable, str(HERE / 'order-test' / 'validate.py'), str(p)], capture_output=True, text=True)
        if ok.returncode:
            rows.append((p.stem + ' (invalid: ' + ok.stdout.strip()[:60] + ')', None))
            continue
        rows.append((p.stem, score_order.score(json.load(open(p)))))
    return rows


def heading_rows():
    ids = json.load(open(HERE / 'heading-test' / 'ids.json'))
    his = {h['id']: h['heading'] for h in json.load(open(HERE / 'HIS-PICKS-RESOLVED.json'))}
    scope = [i for i in ids if i in his]
    judge = json.load(open(HERE / 'heading-judge' / 'JUDGE-OUTPUT.json'))
    key = json.load(open(HERE / 'heading-judge' / 'KEY-do-not-show-judge.json'))
    runs = ['SONNET-1', 'FABLE-1', 'GPT-1']
    out, labels = {}, collections.defaultdict(dict)
    for i, lab in judge.items():
        for L, v in lab.items():
            labels[key[i][L]][i] = v
    heads = {r: json.load(open(HERE / 'heading-test' / 'out' / (r + '.json')))['headings'] for r in runs}
    for r in runs:
        h = heads[r]
        c = collections.Counter(labels[r].get(i) for i in scope)
        out[r] = {'exact': sum(norm(h.get(i, '')) == norm(his[i]) for i in scope),
                  'nocase': sum(norm(h.get(i, '')).lower() == norm(his[i]).lower() for i in scope),
                  'same': c['same'], 'close': c['close'], 'different': c['different']}
    all_diff = [(i, his[i], [heads[r].get(i, '') for r in runs]) for i in scope
                if all(labels[r].get(i) == 'different' for r in runs)]
    return len(scope), out, all_diff


def main():
    L = ['# Turn 132: which model gets closest to his contents', '',
         'Made by `score_t132.py` from the files beside it; run it again to check every number.', '',
         '## Order: outlines against his own reorganization of 4 to 14 November', '',
         'His version re-parents 20 of the 148 units and changes the level of 15. "His moves" counts the units an outline gives'
         ' his new parent; "other moves" the units it re-parents that he left alone; tau is Kendall\'s tau against his order;'
         ' "in his place" counts units with his parent and his preceding unit.', '',
         '| Outline | His moves (of 20) | Other moves | His level changes (of 15) | Other level changes | Tau | In his place (of 148) |',
         '|---|---|---|---|---|---|---|']
    for name, s in order_rows():
        if s is None:
            L.append('| %s | | | | | | |' % name)
            continue
        L.append('| %s | %d | %d | %d | %d | %.3f | %d |' % (name, s['reparented_same'], s['reparented_extra'], s['levels_same'],
                                                            s['levels_extra'], s['tau_vs_his'], s['same_place']))
    L += ['', '"plain" outlines had only the task; "rules" had RULES-ORGANIZE.md (v1), "rules2" RULES-ORGANIZE-2.md (v2).',
          'GPT-gpt-* came from his laptop.', '',
          '**What it shows.** No model, with or without either version of the rules, comes near his order. The best tau'
          ' (Fable, no rules, 0.930) barely beats leaving the 4 November order alone (0.923), and the outlines closest to'
          ' his order make almost none of his moves. The GPT outlines with rules v1 make the most of his moves (9 and 8 of 20)'
          ' and also the most moves he didn\'t make (16 and 23). Rules v2, the four-pass version, did not help any model.'
          ' A model\'s reorganization of his article is a proposal to put to him move by move, never a reorganization.', '',
          '## Headings: fresh runs with RULES-HEADINGS.md against his picks', '']
    n, h, all_diff = heading_rows()
    L += ['| Run | Exact (of %d) | Exact ignoring case | Judge: same | Judge: close | Judge: different |' % n,
          '|---|---|---|---|---|---|']
    for r, s in h.items():
        L.append('| %s | %d | %d | %d | %d | %d |' % (r, s['exact'], s['nocase'], s['same'], s['close'], s['different']))
    L += ['', 'The judge (a Sonnet reader, blind to which run wrote what) called a candidate "same" when it differs from his'
          ' heading at most in capitals, punctuation or an article, "close" when a reader would expect the same section, and'
          ' "different" otherwise. The earlier counts in HANDOFF.md (Opus t130 132, Fable t131 121, and so on) were the lists'
          ' he picked from, so they are not comparable with these.', '',
          '**What it shows.** Fable with the heading rules came closest: the same or close on %d of %d, different on %d.'
          % (h['FABLE-1']['same'] + h['FABLE-1']['close'], n, h['FABLE-1']['different']), '',
          'Where all three runs missed his meaning (the judge said "different" for each):', '']
    for i, mine, cands in all_diff:
        L.append('- %s: his "%s"; the runs: %s' % (i, mine, '; '.join('"%s"' % c for c in cands)))
    (HERE / 'RESULTS.md').write_text('\n'.join(L) + '\n')
    print('\n'.join(L))


if __name__ == '__main__':
    main()
