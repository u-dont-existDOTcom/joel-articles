"""Tests for tools/humanization/repo_links.py: a document or message for Joel links the files it points to (Joel,
2026-10-25 00:24 UTC, on ENGAGING.md: "i have no idea where the 3 files are that i'm supposed to read...")."""
import pathlib
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import pangram_links_check as P  # noqa: E402
import repo_links as R  # noqa: E402

DOC = ROOT / 'articles' / 'inner-child-therapy' / 'experiments' / 't105-readers-edit' / 'ENGAGING.md'


class Paths(unittest.TestCase):
    def written(self, text):
        return [w for _, _, _, w in R.paths(text)]

    def test_engaging_md_paths_are_found(self):
        # the four references he couldn't open, as turn 106 sent them
        text = ("Safety is in one place (`../t102-safety/BOOKS.md`). The hedge read (`caveats/`) looked for those "
                "(32 of 41 lines; `IDEAS.md`). The reader's edit (`edit/`) looks for where the doing can come sooner.")
        self.assertEqual(self.written(text), ['`../t102-safety/BOOKS.md`', '`caveats/`', '`IDEAS.md`', '`edit/`'])

    def test_a_bare_file_name_is_found(self):
        self.assertEqual(self.written('Each one before and after is in ../t106-installs/OLD-SECTIONS.json.'),
                         ['../t106-installs/OLD-SECTIONS.json'])

    def test_links_commands_addresses_and_words_pass(self):
        text = ('Read [IDEAS.md](https://github.com/x/blob/b/IDEAS.md) and https://example.com/a/b.md. Run '
                '`python3 tools/humanization/repo_links.py check FILE`. He wrote "he/she" and "he/zhe/she/they/them". '
                'The batch is `t106-api` and the rule E257.\n\n```\nexperiments/t106-api/API-CHECKS.md\n```\n'
                '<!-- experiments/t106-api/API-CHECKS.md -->')
        self.assertEqual(self.written(text), [])

    def test_a_quote_is_someones_words(self):
        # his question quoted on the questions page, with the link right after it
        self.assertEqual(self.written('- "parked.md is where?": it\'s on GitHub, [here](https://github.com/x/PARKED.md).'), [])

    def test_fix_links_each_path_from_the_documents_folder(self):
        text = 'Safety is in one place (`../t102-safety/BOOKS.md`); the hedge read is `caveats/`, and the gate is `docs/HUMANIZATION-GATE.md`.'
        fixed = R.fix(text, DOC, branch='b')
        self.assertEqual(R.paths(fixed), [])
        self.assertIn('[t102-safety/BOOKS.md](https://github.com/u-dont-existDOTcom/joel-articles/blob/b/articles/'
                      'inner-child-therapy/experiments/t102-safety/BOOKS.md)', fixed)
        self.assertIn('[caveats/](https://github.com/u-dont-existDOTcom/joel-articles/tree/b/articles/inner-child-therapy/'
                      'experiments/t105-readers-edit/caveats)', fixed)
        self.assertIn('[docs/HUMANIZATION-GATE.md](https://github.com/u-dont-existDOTcom/joel-articles/blob/b/docs/'
                      'HUMANIZATION-GATE.md)', fixed)

    def test_fix_leaves_a_path_it_cant_find(self):
        text = 'His messages are in `tNNN-answers/`.'
        self.assertEqual(R.fix(text, DOC), text)
        self.assertEqual(self.written(text), ['`tNNN-answers/`'])


class ChatAndQuestionsPage(unittest.TestCase):
    def test_chat_check_refuses_a_path(self, ):
        import io
        import contextlib
        import tempfile
        with tempfile.NamedTemporaryFile('w', suffix='.md', delete=False, encoding='utf-8') as f:
            f.write('The readers\' notes are in `caveats/`.\n')
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            code = P.main(['--chat', f.name])
        pathlib.Path(f.name).unlink()
        self.assertEqual(code, 1)
        self.assertIn("a path Joel can't open", out.getvalue())

    def test_questions_page_finds_paths_in_open_questions_only(self):
        sys.path.insert(0, str(ROOT / 'articles' / 'inner-child-therapy' / 'tools'))
        import questions_page as Q
        md = ('# Q\n\n## Open questions\n\n### 🟣 104. A thing\n\nSee `experiments/t107-answers/LESSONS.md`.\n\n'
              '## For you to do (no decision needed)\n\nNothing.\n\n## Decided\n\n### 🟢 103\n\nIn `tools/questions_page.py`.\n')
        self.assertEqual(Q.unlinked_paths(md), ['`experiments/t107-answers/LESSONS.md`'])


if __name__ == '__main__':
    unittest.main()
