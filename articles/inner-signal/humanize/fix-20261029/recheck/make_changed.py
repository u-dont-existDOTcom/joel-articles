"""CHANGED-A.json and CHANGED-B.json for the recheck of 2026-10-29 (part_forecast.py make), written before the paste.

The last check of both parts is batch 481's recheck (fix-20261026/b481/recheck/read/RESULT-A.json and RESULT-B.json), which
read batch 481's candidate master. Since then: Joel's six answers of 28 October (his four versions, and HG-S11 and HG-S12
approved), batch 481's other 22 spots back to the words batch 480's recheck read (he never approved them), the 114
comprehension fixes he approved on 29 October and my advised wording on four cards in his own words. Every paragraph
(a line of the checked text) that the last check didn't read is a part here, whole, with my chance that it reads red and
that it reads Human at High confidence, from one stated rule:

- back to words batch 480's recheck read Human: red 0.03, High 0.4;
- his own words (his versions of 28 October, in his answers file): red 0.04, High 0.5;
- otherwise by its new words: up to 5 new words red 0.03, High 0.55; 6 to 15, red 0.05, High 0.45; 16 to 40, red 0.08,
  High 0.35; more, red 0.12, High 0.3;
- and when 8 or more of its new words in a row are his published version's (the AI-written one, whose sentences the fixes
  bring back where the rewrite lost a point), red plus 0.12 (0.2 at 16 words in a row or more) and High at most 0.25: the
  fixes put his published sentences back, and those are what Pangram read as AI before the humanizing began.

  python3 articles/inner-signal/humanize/fix-20261029/recheck/make_changed.py
"""
import difflib
import json
import pathlib
import re
import sys

X = pathlib.Path(__file__).resolve().parent
H = X.parents[1]
ROOT = H.parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import suggestion_review as sr  # noqa: E402

LAST = H / 'fix-20261026' / 'b481' / 'recheck' / 'read'
B480 = H / 'fix-20261026' / 'b480' / 'recheck'
FLAT = str.maketrans({'“': '"', '”': '"', '‘': "'", '’': "'"})
AUDIT_FIRST, AUDIT_LAST = 'Before accepting a recording or live suggestion, ask:', 'change the method, or leave.'


def words(s):
    return re.findall(r"[\w’']+", s.translate(FLAT).lower())


def grams(ws, n):
    return {tuple(ws[i:i + n]) for i in range(len(ws) - n + 1)}


def longest_pub_run(new_words, pub8):
    """The longest run of NEW_WORDS whose every 8 words in a row are in his published text (0 if under 8)."""
    best = run = 0
    for i in range(len(new_words) - 7):
        if tuple(new_words[i:i + 8]) in pub8:
            run = run + 1 if run else 8
            best = max(best, run)
        else:
            run = 0
    return best


def his_texts():
    """His own versions of 28 October (the answers file's your_version texts), as plain words."""
    ans = json.loads((H / 'fix-20261028' / 'ANSWERS-20261028-1519.json').read_text(encoding='utf-8'))
    return [' '.join(words(x['your_version'])) for x in ans['items'] if x.get('your_version', '').strip()]


def main():
    pub_words = words(' '.join(b['text'] for b in sr.blocks((H / 'source' / 'published-20260928.md')
                                                             .read_text(encoding='utf-8'))))
    pub8 = grams(pub_words, 8)
    his = his_texts()
    for part in ('A', 'B'):
        # a line either part of the last check read counts as read: part B starts a section earlier this time (the
        # guide grew), so its first section was read last time in part A
        last = '\n'.join(json.loads((LAST / ('RESULT-%s.json' % q)).read_text(encoding='utf-8'))['text'] for q in 'AB')
        new = (X / ('TEXT-%s.txt' % part)).read_text(encoding='utf-8')
        b480 = '\n'.join((B480 / ('TEXT-%s.txt' % q)).read_text(encoding='utf-8') for q in 'AB')
        old_lines = [ln.strip() for ln in last.split('\n') if ln.strip()]
        old_set = {ln.translate(FLAT) for ln in old_lines}
        b480_set = {ln.strip().translate(FLAT) for ln in b480.split('\n') if ln.strip()}
        changed, n = [], 0
        for ln in [ln.strip() for ln in new.split('\n') if ln.strip()]:
            if ln.translate(FLAT) in old_set:
                continue
            n += 1
            if new.count(ln) != 1 or len(ln) < 12:
                continue   # a short or repeated line: its paragraph's neighbours and the rest's chance cover it
            # the closest line the last check read (its words give the new words); quick ratios pick the likely ones
            short = sorted(old_lines, key=lambda o: -difflib.SequenceMatcher(a=o, b=ln).quick_ratio())[:40]
            best = max(short, key=lambda o: difflib.SequenceMatcher(a=o, b=ln, autojunk=False).ratio())
            ow, nw = words(best), words(ln)
            sm = difflib.SequenceMatcher(a=ow, b=nw, autojunk=False)
            added = [w for op, _a1, _a2, b1, b2 in sm.get_opcodes() if op in ('replace', 'insert') for w in nw[b1:b2]]
            run = longest_pub_run(nw, pub8) if added else 0
            # only a published run that the change brought in counts: it must overlap the new words
            new_runs = [nw[b1:b2] for op, _a1, _a2, b1, b2 in sm.get_opcodes() if op in ('replace', 'insert')]
            run_new = max([longest_pub_run(r, pub8) for r in new_runs] or [0])
            k = len(added)
            if ln.translate(FLAT) in b480_set:
                red, high, why = 0.03, 0.4, 'back to the words batch 480\'s recheck read Human (a batch 481 spot he never approved)'
            elif any(' '.join(nw) in h or (len(nw) > 8 and ' '.join(nw[:8]) in h) for h in his):
                red, high, why = 0.04, 0.5, 'his own version of 28 October'
            else:
                if k <= 5:
                    red, high = 0.03, 0.55
                elif k <= 15:
                    red, high = 0.05, 0.45
                elif k <= 40:
                    red, high = 0.08, 0.35
                else:
                    red, high = 0.12, 0.3
                why = '%d new words' % k
                if run_new >= 8:
                    red += 0.2 if run_new >= 16 else 0.12
                    high = min(high, 0.25)
                    why += ', %d of them in a row from his published version' % run_new
            changed.append({'name': 'P%d (%s)' % (len(changed) + 1, ln[:48].rstrip() + '...'), 'text': ln,
                            'chance_red': round(red, 2), 'chance_high': high, 'why': why, 'kind': 'changed'})
        if part == 'B':
            # his hypnosis audit, kept as a list by his answer 2c and unchanged, as one part (as batch 481's forecast had it)
            a = new.find(AUDIT_FIRST)
            b = new.find(AUDIT_LAST, a) + len(AUDIT_LAST)
            assert a >= 0 and b > a and new.count(AUDIT_FIRST) == 1
            changed = [c for c in changed if not (new.find(c['text']) < b and new.find(c['text']) + len(c['text']) > a)]
            changed.append({'name': 'the hypnosis audit (kept, 2c)', 'text': new[a:b], 'chance_red': 0.95, 'chance_high': 0.0,
                            'why': 'his list, kept by his answer 2c, unchanged: read AI (High, 120 words) in the last two '
                                   'checks (batches 480 and 481)', 'kind': 'changed'})
        (X / ('CHANGED-%s.json' % part)).write_text(json.dumps(changed, ensure_ascii=False, indent=1) + '\n',
                                                     encoding='utf-8')
        exp = sum(c['chance_red'] for c in changed)
        print('part %s: %d paragraphs the last check didn\'t read, %d as parts; expected red parts %.2f; '
              'with a published run %d' % (part, n, len(changed), exp, sum('published' in c['why'] for c in changed)))


if __name__ == '__main__':
    main()
