"""Exercise real child termination using isolated non-model subprocess fixtures."""
import json
from pathlib import Path
import signal
import subprocess
import sys
import tempfile
import time
import unittest

WRAPPER = Path(__file__).with_name('run_generation_batch.py').resolve()


class GenerationBound(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='reverse-pilot-bound-')
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.repo = self.root / 'repo'
        tools = self.repo / 'docs/reverse-model-20260929/tools'
        tools.mkdir(parents=True)
        self.child_source = tools / 'generate_pairs.py'
        data = tools.parent / 'data'
        data.mkdir()
        (data / 'human-passages.jsonl').write_text('{}\n')
        (self.root / 'generated').mkdir()
        (self.root / 'generated/pairs-audit.jsonl').write_text('{"id":"fixture_only"}\n')
        subprocess.run(['git', 'init', '-q', str(self.repo)], check=True)
        subprocess.run(['git', '-C', str(self.repo), 'add', '.'], check=True)
        subprocess.run(['git', '-C', str(self.repo), '-c', 'user.name=Isolated fixture',
                        '-c', 'user.email=fixture@example.invalid', 'commit', '-qm', 'fixture'], check=True)

    def start(self, seconds=10):
        return subprocess.Popen([sys.executable, str(WRAPPER), '--root', str(self.root),
                                 '--batch-size', '1', '--new-passages', '1', '--seconds', str(seconds),
                                 '--python', sys.executable], stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)

    def receipt(self):
        return json.loads(next((self.root/'generated/run-history').glob('*/run-receipt.json')).read_text())

    def assert_child_ended(self):
        pid = int((self.root/'child.pid').read_text())
        stat = Path(f'/proc/{pid}/stat')
        self.assertTrue(not stat.exists() or stat.read_text().split()[2] == 'Z')

    def sleeper(self):
        self.child_source.write_text('import os,time\nfrom pathlib import Path\n'
                                    f'Path({str(self.root / "child.pid")!r}).write_text(str(os.getpid()))\n'
                                    'time.sleep(30)\n')

    def test_deadline_reaps_real_child_and_records_partial_state(self):
        self.sleeper()
        process = self.start(seconds=1)
        _, error = process.communicate(timeout=5)
        self.assertEqual(process.returncode, 0, error)
        self.assertEqual(self.receipt()['status'], 'DEADLINE_SAVED_PARTIAL_EVIDENCE')
        self.assert_child_ended()

    def test_supervisor_stop_does_not_leave_child_running(self):
        self.sleeper()
        process = self.start()
        limit = time.monotonic()+3
        while not (self.root/'child.pid').exists() and time.monotonic() < limit:
            time.sleep(0.02)
        self.assertTrue((self.root/'child.pid').exists())
        process.send_signal(signal.SIGTERM)
        _, error = process.communicate(timeout=5)
        self.assertEqual(process.returncode, 0, error)
        self.assertEqual(self.receipt()['status'], 'STOP_REQUESTED_SAVED_PARTIAL_EVIDENCE')
        self.assert_child_ended()

    def test_child_failure_is_preserved_as_failure(self):
        self.child_source.write_text('raise SystemExit(7)\n')
        process = self.start()
        _, error = process.communicate(timeout=5)
        self.assertEqual(process.returncode, 7, error)
        self.assertEqual(self.receipt()['status'], 'FAILED')


if __name__ == '__main__':
    unittest.main()
