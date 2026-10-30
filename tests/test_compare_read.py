"""tools/humanization/compare_read.py: a rewrite read beside Joel's own version, part by part (Joel, 2026-10-28 15:20
UTC, on the hypnosis guide after Emulate's rewrites: "the guide itself is now too incomprehensible, we went wrong
somewhere"; gate E284)."""
import json
import pathlib
import sys
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import compare_read as C  # noqa: E402

ORIGINAL = '''# Protecting yourself

Conscious agreement is one thing. Unconscious receptivity is another. Emotional compliance is another.

A line associated with the Silva Mind Control tradition says it plainly:

## Finding a hypnotist

Ask what they intend and how they handle surprises.
'''

REWRITE = '''# Protecting yourself

Conscious agreement, unconscious receptivity, emotional compliance. Can people be influenced?

As associated with the Silva Mind Control method:

## A new heading only the rewrite has

This part is new, and it is clear.

## Finding a hypnotist

Ask what they intend and how they handle surprises.
'''

READER = '''## F1.1
NOW: Conscious agreement, unconscious receptivity, emotional compliance. Can people be influenced?
PUBLISHED: Conscious agreement is one thing. Unconscious receptivity is another. Emotional compliance is another.
KIND: garbled
SEVERITY: 3
WHY: A list with no verb, where his text said they differ.

## F1.2
NOW: As associated with the “Silva Mind Control” method:
PUBLISHED: A line associated with the Silva Mind Control tradition says it plainly:
KIND: garbled
SEVERITY: 2
WHY: "As associated" doesn't parse.

## F1.3
NOW: Ask what they intend and how they handle surprises.
PUBLISHED: Ask what they intend and how they handle surprises.
KIND: unclear
SEVERITY: 1
WHY: A reader flagged his own sentence.

TOTAL: 3
'''


class CompareReadTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.d = pathlib.Path(self.tmp.name)
        (self.d / 'rewrite.md').write_text(REWRITE, encoding='utf-8')
        (self.d / 'original.md').write_text(ORIGINAL, encoding='utf-8')

    def tearDown(self):
        self.tmp.cleanup()

    def test_make_pairs_each_part_with_its_published_part(self):
        meta = C.make(self.d / 'rewrite.md', self.d / 'original.md', self.d / 'read', target=1)
        self.assertEqual([m['first'] for m in meta], ['Protecting yourself', 'A new heading only the rewrite has',
                                                      'Finding a hypnotist'])
        part2 = (self.d / 'read' / 'PART-2.txt').read_text(encoding='utf-8')
        # a heading only the rewrite has goes with the shared heading before it
        self.assertIn('Conscious agreement is one thing.', part2)
        self.assertIn('This part is new', part2)
        brief = (self.d / 'read' / 'BRIEF-1.txt').read_text(encoding='utf-8')
        self.assertIn(str(self.d / 'read' / 'READER-1.md'), brief)
        self.assertIn('## F1.1', brief)
        self.assertIn(str(self.d / 'read' / 'PART-1.txt'), brief)

    def test_a_numbered_item_keeps_its_number_for_the_reader(self):
        # the hypnosis guide's countdown line starts "5." as a list number; a reader given the bare text reported the
        # count starting at 4 (2026-10-28, F4b.18), and the fix writer added a second "5." (lesson E290)
        countdown = '# Sober induction\n\nCount 5 to 1.\n\n5. Let your attention come back. 4. Leave a little space.\n\n- one\n'
        (self.d / 'rewrite.md').write_text(countdown, encoding='utf-8')
        (self.d / 'original.md').write_text(countdown, encoding='utf-8')
        C.make(self.d / 'rewrite.md', self.d / 'original.md', self.d / 'read', target=10 ** 6)
        part = (self.d / 'read' / 'PART-1.txt').read_text(encoding='utf-8')
        self.assertIn('5. Let your attention come back. 4.', part)
        self.assertIn('- one', part)

    def test_collect_finds_quotes_and_drops_his_own_sentences(self):
        C.make(self.d / 'rewrite.md', self.d / 'original.md', self.d / 'read', target=10 ** 6)
        (self.d / 'read' / 'READER-1.md').write_text(READER, encoding='utf-8')
        (self.d / 'his.txt').write_text('Ask what they intend and how they handle surprises.', encoding='utf-8')
        s = C.collect(self.d / 'read', owner=[str(self.d / 'his.txt')])
        f = {r['id']: r for r in json.loads((self.d / 'read' / 'FINDINGS.json').read_text())['findings']}
        self.assertEqual(f['F1.1']['now_found'], 1.0)
        self.assertEqual(f['F1.1']['pub_found'], 1.0)
        # quote marks a reader added or dropped don't stop a quote being found
        self.assertEqual(f['F1.2']['now_found'], 1.0)
        self.assertTrue(f['F1.3']['same_as_original'])
        self.assertEqual(s['findings'], 2)
        self.assertEqual(s['same_as_original'], ['F1.3'])
        self.assertEqual(s['by_severity'], {3: 1, 2: 1})
        self.assertEqual(s['paragraphs_hit'][3], 1)

    def gate_files(self, rewrite_text):
        (self.d / 'rewrite.md').write_text(rewrite_text, encoding='utf-8')
        (self.d / 'answers.json').write_text(json.dumps({'items': [{'your_version': 'This part is new, and it is clear.'}]}),
                                             encoding='utf-8')
        (self.d / 'gate.json').write_text(json.dumps({
            'article': 'rewrite.md', 'original': 'original.md', 'records': ['read/READ-RECORD.json'],
            'owner': ['answers.json']}), encoding='utf-8')

    def test_gate_needs_every_rewritten_paragraph_read_and_every_finding_settled(self):
        self.gate_files(REWRITE)
        C.make(self.d / 'rewrite.md', self.d / 'original.md', self.d / 'read', target=10 ** 6)
        (self.d / 'read' / 'READER-1.md').write_text(READER, encoding='utf-8')
        C.collect(self.d / 'read')
        C.record(self.d / 'read')
        probs = C.gate(self.d / 'gate.json', self.d)
        # read, but the two findings at severity 2 and 3 have no fate yet (F1.3 is his published sentence)
        self.assertEqual(sorted(p[0] for p in probs), ['OPEN', 'OPEN'])
        (self.d / 'read' / 'DISPOSITIONS.json').write_text(json.dumps({
            'F1.1': ['his', 'his own version replaces it'], 'F1.2': ['fixed', 'his published line back']}), encoding='utf-8')
        C.record(self.d / 'read')
        probs = C.gate(self.d / 'gate.json', self.d)
        # "fixed" while the words are still in the article is still open
        self.assertEqual([(p[0], 'F1.2' in p[3]) for p in probs], [('OPEN', True)])
        # the fix goes in: its words are new, so the paragraph is unread until someone reads it beside his
        self.gate_files(REWRITE.replace('As associated with the Silva Mind Control method:',
                                        'A line associated with the Silva Mind Control method says it plainly, I guess:'))
        probs = C.gate(self.d / 'gate.json', self.d)
        self.assertEqual([p[0] for p in probs], ['UNREAD'])
        self.assertIn('Silva', probs[0][3])

    def test_a_garbled_sentence_is_never_simply_kept(self):
        self.gate_files(REWRITE)
        C.make(self.d / 'rewrite.md', self.d / 'original.md', self.d / 'read', target=10 ** 6)
        (self.d / 'read' / 'READER-1.md').write_text(READER, encoding='utf-8')
        C.collect(self.d / 'read')
        settled = {'F1.1': ['his', 'his own version replaces it']}
        (self.d / 'read' / 'DISPOSITIONS.json').write_text(json.dumps(dict(settled, **{
            'F1.2': ['kept', 'fixing it would cost the Pangram reading']})), encoding='utf-8')
        C.record(self.d / 'read')
        probs = C.gate(self.d / 'gate.json', self.d)
        self.assertEqual(len(probs), 1)
        self.assertIn('F1.2 is garbled and kept', probs[0][3])
        # a snag my check put at severity 1 may stay, with that on record
        (self.d / 'read' / 'DISPOSITIONS.json').write_text(json.dumps(dict(settled, **{
            'F1.2': ['kept', 'reads as casual speech', 1]})), encoding='utf-8')
        C.record(self.d / 'read')
        self.assertEqual(C.gate(self.d / 'gate.json', self.d), [])

    def test_gate_passes_his_published_text_and_his_own_versions(self):
        self.gate_files(ORIGINAL + '\nThis part is new, and it is clear.\n')
        (self.d / 'read').mkdir()
        (self.d / 'read' / 'READ-RECORD.json').write_text(json.dumps({'coverage': [], 'findings': []}), encoding='utf-8')
        self.assertEqual(C.gate(self.d / 'gate.json', self.d), [])

    def test_reader_fields_parse_across_lines(self):
        recs, total = C.parse_reader('## F2.1\nNOW: one line\nand another\nPUBLISHED: none\nKIND: Lost (a point)\n'
                                     'SEVERITY: 2 (most readers)\nWHY: because.\n\nTOTAL: 1\n', 2)
        self.assertEqual(total, 1)
        self.assertEqual(recs[0]['now'], 'one line\nand another')
        self.assertEqual(recs[0]['kind'], 'lost')
        self.assertEqual(recs[0]['severity'], 2)

    def test_changes_show_the_card_that_cut_a_point(self):
        # gate E301: the hypnosis guide's forces line, cut by his card RP-1.4 on 25 October, brought back on 30 October
        cut = 'As you know there are many forces at work in the world that are already training your mind.'
        rest = 'With self-hypnosis you can do much of the same thing from the inside, by befriending your mind.'
        later = 'With self-hypnosis you can train your own mind from the inside, by befriending your mind.'
        back = 'Ads, screens, fear and cravings are already training your mind.'
        hist = [('a' * 40, '2026-10-21T00:00:00', 'installed', '', [cut + ' ' + rest, 'Another paragraph entirely.']),
                ('b' * 40, '2026-10-25T00:00:00', 'his answers in (RP-1.4)', '', [rest, 'Another paragraph entirely.']),
                ('c' * 40, '2026-10-29T00:00:00', 'comprehension fixes', '', [later, 'Another paragraph entirely.'])]
        ch = C.changes(back + ' ' + later, hist)
        self.assertEqual([c['subject'] for c in ch], ['comprehension fixes', 'his answers in (RP-1.4)', 'installed'])
        self.assertEqual(ch[1]['dropped'], [cut])
        self.assertTrue(ch[-1]['first_seen'])
        # a paragraph that shares too few words with any older one has no history before it
        self.assertEqual(C.changes('Nothing like any of these at all, really.', hist), [])


if __name__ == '__main__':
    unittest.main()
