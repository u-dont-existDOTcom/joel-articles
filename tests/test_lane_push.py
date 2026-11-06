"""Tests for tools/humanization/lane_push.py's arguments (2026-10-23: "--add TOOL --add TEST" committed only the test, so
the tool change it tests stayed out of the commit, and the checks, which run on the working tree, passed anyway)."""
import pathlib
import sys
import os
import subprocess
import unittest
from unittest import mock

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / 'tools' / 'humanization'))
import lane_push as P  # noqa: E402


class Arguments(unittest.TestCase):
    def test_each_add_adds_to_the_list(self):
        a = P.parser().parse_args(['subject', '--add', 'tools/x.py', '--add', 'tests/test_x.py', 'docs/y.md'])
        self.assertEqual(a.add, ['tools/x.py', 'tests/test_x.py', 'docs/y.md'])

    def test_no_add_is_an_empty_list(self):
        self.assertEqual(P.parser().parse_args(['subject']).add, [])


class LaneIntegration(unittest.TestCase):
    """Gate E339 (Joel, 2026-11-04 00:37 UTC: "make sure no other lane can make the same mistake you made next time"):
    the gut lane never merged main, opened no pull request and changed a shared test another open pull request changed."""

    def test_shared_files_are_the_rules_and_tools_not_an_articles_folder(self):
        self.assertEqual(P.shared(['tools/humanization/x.py', 'docs/GATE.md', 'articles/gut/a.md', 'AGENTS.md',
                                   'state/MAILBOX.json', 'articles/INDEX.json', 'tests/test_x.py']),
                         ['AGENTS.md', 'docs/GATE.md', 'tests/test_x.py', 'tools/humanization/x.py'])

    def test_overlaps_name_each_other_pull_request_and_the_files(self):
        mine = ['tools/humanization/suggestion_review_browser_test.py', 'articles/gut/a.md', 'state/MAILBOX.json']
        others = {280: ('claude/bad-trips-20261103', ['tools/humanization/suggestion_review_browser_test.py',
                                                      'state/MAILBOX.json']),
                  278: ('chat/inner-child', ['state/tasks/x.md'])}
        self.assertEqual(P.overlaps(mine, others), {280: ['tools/humanization/suggestion_review_browser_test.py']})

    def fake(self, behind):
        def run(cmd, check=True, timeout=600):
            rc, out = 0, ''
            if cmd[:3] == ['git', 'merge-base', '--is-ancestor']:
                rc = 1 if behind else 0
            elif cmd[:2] == ['git', 'log']:
                out = 'abc one\ndef two\n'
            elif cmd[:2] == ['git', 'diff']:
                out = 'docs/HUMANIZATION-GATE.md\narticles/x/a.md\n'
            elif cmd[:3] == ['git', 'rev-parse', '--abbrev-ref']:
                out = 'claude/lane\n'
            return subprocess.CompletedProcess(cmd, rc, out, '')
        return run

    def test_main_not_merged_refuses_and_names_the_shared_files(self):
        with mock.patch.object(P, 'run', self.fake(behind=True)):
            with self.assertRaises(SystemExit) as e:
                P.main_gate()
        self.assertIn('git merge origin/main', str(e.exception))
        self.assertIn('docs/HUMANIZATION-GATE.md', str(e.exception))

    def test_main_merged_passes(self):
        with mock.patch.object(P, 'run', self.fake(behind=False)):
            self.assertEqual(P.main_gate(), '')

    def test_main_is_fetched_into_origin_main_whatever_the_clone_fetches(self):
        """A clone whose fetch refspec names only its lane branch kept a weeks-old origin/main after "git fetch origin
        main" (2026-11-04, the Inner Child lane's laptop clone): the fetch has to name refs/remotes/origin/main."""
        calls = []
        fake = self.fake(behind=False)

        def run(cmd, check=True, timeout=600):
            calls.append(cmd)
            return fake(cmd, check, timeout)
        with mock.patch.object(P, 'run', run):
            P.main_gate()
        fetches = [c for c in calls if c[:2] == ['git', 'fetch']]
        self.assertEqual(len(fetches), 1)
        self.assertIn('+refs/heads/main:refs/remotes/origin/main', fetches[0])

    def test_a_narrow_clone_sees_the_main_on_github(self):
        """The same with real repositories: a bare origin whose main moves on, and a clone that fetches only its lane."""
        import tempfile
        with tempfile.TemporaryDirectory() as d:
            env = {k: v for k, v in os.environ.items() if not k.startswith('GIT_')}
            env.update(GIT_AUTHOR_NAME='t', GIT_AUTHOR_EMAIL='t@t', GIT_COMMITTER_NAME='t', GIT_COMMITTER_EMAIL='t@t')
            g = lambda *a, cwd=d: subprocess.run(['git', *a], cwd=cwd, env=env, check=True, capture_output=True, text=True).stdout.strip()
            g('init', '-q', '--bare', 'origin.git')
            g('clone', '-q', 'origin.git', 'seed')
            seed = os.path.join(d, 'seed')
            g('checkout', '-q', '-b', 'main', cwd=seed)
            g('commit', '-q', '--allow-empty', '-m', 'one', cwd=seed)
            g('push', '-q', 'origin', 'main', cwd=seed)
            g('checkout', '-q', '-b', 'lane', cwd=seed)
            g('push', '-q', 'origin', 'lane', cwd=seed)
            g('clone', '-q', '--single-branch', '--branch', 'lane', 'origin.git', 'lane')
            lane = os.path.join(d, 'lane')
            g('fetch', '-q', 'origin', '+refs/heads/main:refs/remotes/origin/main', cwd=lane)
            g('checkout', '-q', 'main', cwd=seed)
            g('commit', '-q', '--allow-empty', '-m', 'two', cwd=seed)
            g('push', '-q', 'origin', 'main', cwd=seed)
            new_main = g('rev-parse', 'HEAD', cwd=seed)
            g('fetch', '-q', 'origin', 'main', cwd=lane)        # what the gate did before: origin/main stays put
            self.assertNotEqual(g('rev-parse', 'origin/main', cwd=lane), new_main)

            def run(cmd, check=True, timeout=600):
                return subprocess.run(cmd, cwd=lane, env=env, capture_output=True, text=True, timeout=timeout)
            with mock.patch.object(P, 'run', run):
                with self.assertRaises(SystemExit) as e:
                    P.main_gate()                                # now: it sees main moved and refuses
            self.assertIn('git merge origin/main', str(e.exception))
            self.assertEqual(g('rev-parse', 'origin/main', cwd=lane), new_main)

    def test_no_pull_request_and_no_pr_option_refuses(self):
        a = P.parser().parse_args(['subject'])
        with mock.patch.object(P, 'run', self.fake(behind=False)), \
                mock.patch.object(P, 'open_pulls', return_value={280: ('claude/other', ['docs/x.md'])}):
            with self.assertRaises(SystemExit) as e:
                P.integration_gate(a)
        self.assertIn('no open pull request', str(e.exception))

    def test_an_overlap_refuses_until_it_says_how_it_builds_on_theirs(self):
        pulls = {280: ('claude/other', ['docs/HUMANIZATION-GATE.md']), 282: ('claude/lane', ['articles/x/a.md'])}
        with mock.patch.object(P, 'run', self.fake(behind=False)), mock.patch.object(P, 'open_pulls', return_value=pulls):
            with self.assertRaises(SystemExit) as e:
                P.integration_gate(P.parser().parse_args(['subject']))
            self.assertIn('#280', str(e.exception))
            notes = P.integration_gate(P.parser().parse_args(['subject', '--overlap-ok', '#280: adds a line after theirs']))
        self.assertTrue(any('#280' in n for n in notes))

    def test_github_unreachable_warns_and_does_not_stop(self):
        with mock.patch.object(P, 'run', self.fake(behind=False)), mock.patch.object(P, 'open_pulls', return_value=None):
            notes = P.integration_gate(P.parser().parse_args(['subject']))
        self.assertTrue(any('could not be read' in n for n in notes))

    def test_files_are_paged_by_number_not_by_paginate(self):
        # 2026-11-04: gh api --paginate follows next-page links by numeric repository id, which the session proxy
        # refuses, so two pull requests over 100 files made the whole overlap check blind
        calls = []

        def run(cmd, check=True, timeout=600):
            calls.append(cmd)
            page = int(cmd[2].rsplit('page=', 1)[1])
            out = '\n'.join('f%d_%d' % (page, i) for i in range(100 if page < 3 else 7))
            return subprocess.CompletedProcess(cmd, 0, out, '')
        with mock.patch.object(P, 'run', run):
            files = P.pull_files('o', 'r', 199)
        self.assertEqual(len(files), 207)
        self.assertFalse(any('--paginate' in c for c in calls))

    def test_one_unreadable_pull_request_does_not_blind_the_others(self):
        pulls = {199: ('chat/big', None), 280: ('claude/other', ['docs/HUMANIZATION-GATE.md']),
                 282: ('claude/lane', ['articles/x/a.md'])}
        with mock.patch.object(P, 'run', self.fake(behind=False)), mock.patch.object(P, 'open_pulls', return_value=pulls):
            with self.assertRaises(SystemExit) as e:
                P.integration_gate(P.parser().parse_args(['subject']))
            self.assertIn('#280', str(e.exception))
            notes = P.integration_gate(P.parser().parse_args(['subject', '--overlap-ok', '#280: after theirs']))
        self.assertTrue(any('#199' in n and 'could not be read' in n for n in notes))

    def test_an_overlap_reason_names_each_pull_request_it_answers_for(self):
        # 2026-11-04: a reason written for #280 let a push through beside #285, opened an hour later on the same file
        pulls = {280: ('claude/other', ['docs/HUMANIZATION-GATE.md']), 285: ('handoff/ic', ['docs/HUMANIZATION-GATE.md']),
                 286: ('claude/lane', ['articles/x/a.md'])}
        with mock.patch.object(P, 'run', self.fake(behind=False)), mock.patch.object(P, 'open_pulls', return_value=pulls):
            with self.assertRaises(SystemExit) as e:
                P.integration_gate(P.parser().parse_args(['subject', '--overlap-ok', '#280: lines apart']))
            self.assertIn('#285', str(e.exception))
            self.assertNotIn('#280 (', str(e.exception))
            notes = P.integration_gate(P.parser().parse_args(['subject', '--overlap-ok', '#280 and #285: lines apart']))
        self.assertTrue(any('#285' in n for n in notes))


if __name__ == '__main__':
    unittest.main()


class MergeLessons(unittest.TestCase):
    """Joel, 2026-11-05 15:15 UTC: "make sure you merge lessons with main branch so everyone is sharing always". A branch
    that changes shared rules or tools merges into main the turn it is pushed, once its checks pass."""

    def args(self, *extra):
        return P.parser().parse_args(['subject', '--article', 'bad-trips'] + list(extra))

    def test_shared_changes_without_merge_or_reason_refuse(self):
        with self.assertRaises(SystemExit) as e:
            P.merge_gate(self.args(), ['docs/MAKING-SENSE.md'], robot=False)
        self.assertIn('--merge', str(e.exception))
        self.assertIn('docs/MAKING-SENSE.md', str(e.exception))

    def test_merge_or_a_reason_lets_it_through(self):
        P.merge_gate(self.args('--merge'), ['docs/MAKING-SENSE.md'], robot=False)
        P.merge_gate(self.args('--no-merge', 'its tests fail until the gut lane merges'), ['docs/MAKING-SENSE.md'],
                     robot=False)

    def test_article_work_alone_needs_neither(self):
        P.merge_gate(self.args(), [], robot=False)

    def test_merge_and_no_merge_together_refuse(self):
        with self.assertRaises(SystemExit):
            P.merge_gate(self.args('--merge', '--no-merge', 'why'), ['docs/x.md'], robot=False)

    def test_with_the_auto_merge_workflow_on_main_shared_changes_need_neither(self):
        """Gate E379 (Joel, 2026-11-06: every lane's pull request merges itself once its checks pass)."""
        P.merge_gate(self.args(), ['docs/MAKING-SENSE.md'], robot=True)
        with self.assertRaises(SystemExit):
            P.merge_gate(self.args(), ['docs/MAKING-SENSE.md'], robot=False)

    def test_a_lesson_number_main_already_gave_out_refuses(self):
        """Gate E379: on 2026-11-06 the neuro lane's pull request 314 numbered its lessons E374 to E377 while the gut
        lane's branch had its own E374; the gut lane's became E378, and then E379 when the bad trips lane's 316 gave
        out E378 first."""
        main = '- **E373. Old.** text\n- **E374. Neuro.** text\n'
        branch = main + '- **E374. Gut.** text\n'
        self.assertEqual(P.new_duplicate_lessons(branch, main), (['374'], 375))
        shared_before = '- **E362. Gut.** a\n- **E362. Bad trips.** b\n'
        self.assertEqual(P.new_duplicate_lessons(shared_before + '- **E363. New.** c\n', shared_before)[0], [])

    def test_no_merge_with_the_workflow_labels_the_pull_request_hold(self):
        calls = []

        def run(cmd, **kw):
            calls.append(cmd)
            out = {'rev-parse': 'claude/gut-r16\n'}.get(cmd[1], '308\n' if 'pulls?state=open' in ' '.join(cmd) else '')
            return mock.Mock(returncode=0, stdout=out, stderr='')
        with mock.patch.object(P, 'run', run), mock.patch.object(P, 'owner_repo', lambda: ('o', 'r')):
            msg = P.hold('his answers are still out')
        self.assertIn('labelled "hold"', msg)
        self.assertTrue(any('issues/308/labels' in ' '.join(c) and 'labels[]=hold' in c for c in calls))

    def fake(self, checks, merged=True, pull='301'):
        calls = []

        def run(cmd, check=True, timeout=600):
            calls.append(cmd)
            rc, out, err = 0, '', ''
            if cmd[:2] == ['git', 'rev-parse'] and '--abbrev-ref' in cmd:
                out = 'claude/bad-trips-20261105\n'
            elif cmd[:2] == ['git', 'rev-parse']:
                out = 'abcdef1234567890\n'
            elif cmd[:3] == ['git', 'remote', 'get-url']:
                out = 'https://github.com/owner/joel-articles.git\n'
            elif cmd[:2] == ['gh', 'api'] and 'pulls?state=open' in cmd[2]:
                out = pull + '\n'
            elif cmd[:2] == ['gh', 'api'] and cmd[2].endswith('/check-runs'):
                out = '\n'.join('\t'.join(c) for c in checks) + '\n'
            elif cmd[:4] == ['gh', 'api', '-X', 'PUT']:
                if merged:
                    out = '0123456789abcdef\n'
                else:
                    rc, err = 1, 'Pull Request is not mergeable'
            return subprocess.CompletedProcess(cmd, rc, out, err)
        return run, calls

    def test_green_checks_merge_with_a_merge_commit_at_the_pushed_commit(self):
        run, calls = self.fake([('content-integrity', 'completed', 'success')])
        with mock.patch.object(P, 'run', run):
            msg = P.merge_now(wait=1)
        self.assertIn('merged pull request 301 into main', msg)
        put = [c for c in calls if c[:4] == ['gh', 'api', '-X', 'PUT']][0]
        self.assertIn('merge_method=merge', put)
        self.assertIn('sha=abcdef1234567890', put)

    def test_a_failed_check_does_not_merge(self):
        run, calls = self.fake([('content-integrity', 'completed', 'failure')])
        with mock.patch.object(P, 'run', run):
            msg = P.merge_now(wait=1)
        self.assertTrue(msg.startswith('NOT MERGED'))
        self.assertIn('content-integrity', msg)
        self.assertFalse([c for c in calls if c[:4] == ['gh', 'api', '-X', 'PUT']])

    def test_no_pull_request_says_so(self):
        run, _ = self.fake([], pull='')
        with mock.patch.object(P, 'run', run):
            self.assertIn('no open pull request', P.merge_now(wait=1))

    def test_github_refusing_the_merge_is_reported_not_hidden(self):
        run, _ = self.fake([('content-integrity', 'completed', 'success')], merged=False)
        with mock.patch.object(P, 'run', run):
            msg = P.merge_now(wait=1)
        self.assertIn('NOT MERGED', msg)
        self.assertIn('not mergeable', msg)
