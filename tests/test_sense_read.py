"""tools/humanization/sense_read.py: the word-for-sense read with planted errors (Joel, 2026-11-03 13:46 UTC: "the tag
questions part above says "oily" instead of old. do we have more nonsense in here?"; lesson E331)."""
import contextlib
import io
import json
import pathlib
import sys
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import sense_read as S  # noqa: E402
import suggestion_review as sr  # noqa: E402

ARTICLE = '''# The quiet room

We start with a short appointment with yourself. Find a quiet place and notice your breath without any effort at all.

If you can't find any warmth today, that is fine. Stay with what you feel and be gentle with yourself for a while.

Some people trust the process quickly. Others need more time than they expected, and that is normal for everyone.

## Listening in

Sit down and listen to the room. A calm mind is not a closed mind, and it will accept what comes along without a fight.

Good advice is to remove the pressure, not the feeling. Your old habits will loosen when you stop pushing against them.

The specific words matter less than the tone you use, so keep a steady and gentle voice from start to finish.

## Coming back

Take your time returning. Notice the weight of your body and the sounds in the room before you open your eyes again.

A compliment to yourself helps here: you did something kind today, and it was an act of real principle for you.

Peace is not the absence of noise. It comes when you stop trying to control which thoughts arrive and which ones leave.

Write down one thing you noticed, then close the notebook and carry on with your day in a gentle way as before.

Come back to this practice tomorrow, and the day after, and see whether the old patterns shift even a little bit.
'''


def run(*args):
    out, err = io.StringIO(), io.StringIO()
    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
        code = S.main([str(a) for a in args])
    return code, out.getvalue(), err.getvalue()


class SenseReadTest(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.tmp = pathlib.Path(self._tmp.name)
        self.master = self.tmp / 'master.md'
        self.master.write_text(ARTICLE, encoding='utf-8')
        self.out = self.tmp / 'out'
        code, _, _ = run('make', self.master, self.out, '--parts', 2, '--plant', 2, '--seed', 1)
        self.assertEqual(code, 0)
        self.bl = sr.blocks(ARTICLE)
        self.tasks = json.loads((self.out / 'TASKS.json').read_text())
        self.canaries = json.loads((self.out / 'CANARIES.json').read_text())

    def part_lines(self, k):
        text = (self.out / 'parts' / ('PART-%d.md' % k)).read_text()
        return {int(l[1:l.index(']')]): l[l.index(']') + 2:] for l in text.splitlines() if l.startswith('[')}

    def test_make(self):
        self.assertEqual(sorted(p.name for p in (self.out / 'parts').iterdir()), ['PART-1.md', 'PART-2.md'])
        self.assertFalse((self.out / 'parts' / 'CANARIES.json').exists())
        self.assertTrue((self.out / 'CANARIES.json').exists())
        self.assertEqual(self.master.read_text(encoding='utf-8'), ARTICLE)
        self.assertEqual(len(self.canaries), 4)
        self.assertEqual([sum(1 for c in self.canaries if c['part'] == k) for k in (1, 2)], [2, 2])
        self.assertEqual(len({c['block'] for c in self.canaries}), 4)
        # the parts cover every block once, and their ranges are in TASKS.json
        self.assertEqual(self.tasks[0]['blocks'][0], 0)
        self.assertEqual(self.tasks[0]['blocks'][1] + 1, self.tasks[1]['blocks'][0])
        self.assertEqual(self.tasks[1]['blocks'][1], len(self.bl) - 1)
        for c in self.canaries:
            b = self.bl[c['block']]
            self.assertEqual(b['level'], 0, 'planted in a heading')
            lo, hi = self.tasks[c['part'] - 1]['blocks']
            self.assertTrue(lo <= c['block'] <= hi)
            line = self.part_lines(c['part'])[c['block']]
            self.assertIn(c['planted'], line)
            self.assertIn(c['planted'], c['sentence'])
            self.assertIn(c['original'], b['text'])
            self.assertNotIn(c['original'].lower(), c['sentence'].lower().replace(c['planted'].lower(), ''))
            # the only change to the line is that one word
            self.assertEqual(len(line.split()), len(b['text'].split()))
            diff = [(x, y) for x, y in zip(b['text'].split(), line.split()) if x != y]
            self.assertEqual(len(diff), 1)
            self.assertEqual(c['original'][0].isupper(), c['planted'][0].isupper())
        # headings are untouched
        for k in (1, 2):
            lines = self.part_lines(k)
            for b in self.bl:
                if b['level'] and b['i'] in lines:
                    self.assertEqual(lines[b['i']], '#' * b['level'] + ' ' + b['text'])
        # the brief says nothing of planting
        brief = (self.out / 'BRIEF.md').read_text().lower()
        self.assertNotIn('plant', brief)
        self.assertNotIn('canar', brief)
        self.assertNotIn('{{', brief)
        self.assertIn('no style notes', brief)

    def test_same_seed_same_canaries(self):
        out2 = self.tmp / 'out2'
        run('make', self.master, out2, '--parts', 2, '--plant', 2, '--seed', 1)
        self.assertEqual(self.canaries, json.loads((out2 / 'CANARIES.json').read_text()))
        out3 = self.tmp / 'out3'
        run('make', self.master, out3, '--parts', 2, '--plant', 2, '--seed', 2)
        self.assertTrue(json.loads((out3 / 'CANARIES.json').read_text()))

    def test_style_and_pairs(self):
        style = self.tmp / 'STYLE.md'
        style.write_text('Joel says "kinda" and invents "trancier".', encoding='utf-8')
        pairs = self.tmp / 'pairs.json'
        pairs.write_text('[["mind", "mine"]]', encoding='utf-8')
        out = self.tmp / 'o4'
        code, _, _ = run('make', self.master, out, '--parts', 1, '--plant', 1, '--seed', 3, '--style', style, '--pairs', pairs)
        self.assertEqual(code, 0)
        self.assertIn('trancier', (out / 'BRIEF.md').read_text())
        c = json.loads((out / 'CANARIES.json').read_text())
        self.assertEqual([x['planted'] for x in c], ['mine'])

    def write_reads(self, part2_complete=False):
        canaries = self.canaries
        reads = self.tmp / 'reads_src'
        reads.mkdir(exist_ok=True)
        out = {}
        for t in self.tasks:
            k = t['part']
            allb = list(range(t['blocks'][0], t['blocks'][1] + 1))
            mine = [c for c in canaries if c['part'] == k]
            finds = [{'block': c['block'], 'text': c['planted'] + ' in ' + c['sentence'], 'kind': 'wrong-word',
                      'what': 'x', 'fix': 'y', 'confidence': 'sure'} for c in mine]
            if k == 2 and not part2_complete:
                finds = finds[:1]
                allb = allb[:-1]
            if k == 1:
                finds.append({'block': 2, 'text': 'Find a quiet place', 'kind': 'broken', 'what': 'z', 'fix': 'w', 'confidence': 'likely'})
            out[k] = {'part': k, 'read': allb, 'findings': finds, 'notes': ''}
            (self.out / 'reads' / ('READ-%d.json' % k)).write_text(json.dumps(out[k]))
        return out

    def test_score(self):
        self.write_reads()
        code, text, _ = run('score', self.out)
        self.assertEqual(code, 3, text)
        score = json.loads((self.out / 'SCORE.json').read_text())
        self.assertEqual((score['found'], score['planted']), (3, 4))
        self.assertAlmostEqual(score['recall'], 0.75)
        p2 = score['parts'][1]
        self.assertEqual(p2['missing'], [self.tasks[1]['blocks'][1]])
        self.assertEqual(score['parts'][0]['missing'], [])
        self.assertIn('NOT READ', text)
        raw = json.loads((self.out / 'FINDINGS-RAW.json').read_text())
        self.assertEqual([(r['block'], r['text'], r['readers']) for r in raw], [(2, 'Find a quiet place', [1])])

    def test_complete_reads_pass(self):
        self.write_reads(part2_complete=True)
        code, text, _ = run('score', self.out)
        self.assertEqual(code, 0, text)
        self.assertIn('recall: 4/4', text)

    def test_raw_findings_dedup(self):
        self.write_reads(part2_complete=True)
        # part 2 reports the same real finding as part 1 (as if the parts overlapped): one entry, two readers
        rp = self.out / 'reads' / 'READ-2.json'
        d = json.loads(rp.read_text())
        d['findings'].append({'block': 2, 'text': 'find a QUIET place', 'kind': 'slip', 'what': 'q', 'fix': 'r', 'confidence': 'likely'})
        rp.write_text(json.dumps(d))
        run('score', self.out)
        raw = json.loads((self.out / 'FINDINGS-RAW.json').read_text())
        self.assertEqual(len(raw), 1)
        self.assertEqual(raw[0]['readers'], [1, 2])

    def test_malformed_and_missing(self):
        self.write_reads(part2_complete=True)
        (self.out / 'reads' / 'READ-2.json').write_text('{"part": 2, "read": [1, 2')
        code, _, err = run('score', self.out)
        self.assertEqual(code, 2)
        self.assertIn('READ-2.json', err)
        (self.out / 'reads' / 'READ-2.json').unlink()
        code, _, _ = run('score', self.out)
        self.assertEqual(code, 2)

    def test_nonwords(self):
        try:
            import spellchecker  # noqa: F401
        except ImportError:
            self.skipTest('pyspellchecker is not installed')
        m = self.tmp / 'nw.md'
        m.write_text('# Title\n\nWe walked to Prague with a flurbish friend and a xqzv map.\n', encoding='utf-8')
        code, text, _ = run('nonwords', m)
        self.assertEqual(code, 0)
        self.assertIn('flurbish', text)
        self.assertNotIn('prague', text.lower())
        k = self.tmp / 'known.txt'
        k.write_text('flurbish', encoding='utf-8')
        code, text, _ = run('nonwords', m, '--known', k)
        self.assertNotIn('flurbish', text)
        self.assertIn('xqzv', text)



class SkillWiringTest(unittest.TestCase):
    """Joel, 2026-11-03: "make sure this closer reading is also part of the general joel-articles skill". The skill, the
    agent guide and the fixing checklist name the read and its tool, and the readers' brief never says errors are planted."""

    def test_wired(self):
        root = pathlib.Path(__file__).resolve().parents[1]
        skill = (root / 'SKILL.md').read_text(encoding='utf-8')
        self.assertIn('## Word-for-sense read before publication', skill)
        self.assertIn('tools/humanization/sense_read.py', skill)
        self.assertIn('sense_read_brief.md', skill)
        self.assertIn('Word-for-sense read before publication', (root / 'AGENTS.md').read_text(encoding='utf-8'))
        self.assertIn('tools/humanization/sense_read.py', (root / 'docs' / 'FIXING-AN-ARTICLE.md').read_text(encoding='utf-8'))
        brief = (root / 'tools' / 'humanization' / 'sense_read_brief.md').read_text(encoding='utf-8').lower()
        for word in ('plant', 'canary', 'canaries', 'seeded'):
            self.assertNotIn(word, brief)

if __name__ == '__main__':
    unittest.main()
