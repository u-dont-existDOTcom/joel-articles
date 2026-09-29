"""Focused guard and actual orchestration tests with model-call fixture responses."""
import argparse
import ast
import hashlib
import json
from pathlib import Path
import tempfile
import types
import unittest
from copy_check import overlap, longest_unquoted_run
from prepare_copy_repair import prepare
from request_cache import RequestCache


HUMAN = 'one two three four five six seven eight nine ten eleven twelve'


class CopyBoundary(unittest.TestCase):
    def test_threshold_and_punctuation(self):
        self.assertTrue(overlap(HUMAN, 'one two three four five six seven eight nine ten')['passed'])
        self.assertFalse(overlap(HUMAN, 'ONE, two three four five six seven eight nine ten eleven')['passed'])

    def test_quotes_and_contractions(self):
        for opening, closing in [('"', '"'), ('“', '”'), ("'", "'"), ('‘', '’')]:
            self.assertEqual(longest_unquoted_run('He said '+opening+HUMAN+closing, opening+HUMAN+closing), 0)
            self.assertEqual(longest_unquoted_run(HUMAN, opening+HUMAN+closing), 12)
        self.assertEqual(longest_unquoted_run(HUMAN, '"'+HUMAN), 12)
        self.assertEqual(longest_unquoted_run("don't repeat these words", "don't repeat these words"), 4)
        self.assertEqual(longest_unquoted_run(HUMAN, 'one two three four five "quoted" six seven eight nine ten eleven twelve'), 7)

    def test_existing_migration_and_recovery(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp)
            row = {'id':'H0001','human':HUMAN,'notes':HUMAN,'ai':HUMAN,
                   'accepted':True,'method':'notes_regeneration','split':'train'}
            para = dict(row, id='H0002', method='paraphrase')
            original = ''.join(json.dumps(x)+'\n' for x in [row, para])
            (p/'pairs-audit.jsonl').write_text(original)
            first = prepare(p)
            self.assertEqual(first['queued_once_for_fresh_notes_and_draft'], ['H0001'])
            actual = [json.loads(line) for line in (p/'pairs-audit.jsonl').read_text().splitlines()]
            self.assertEqual(actual[1], para)
            self.assertEqual((p/'run-history/pre-copy-repair-v2/pairs-audit.jsonl').read_text(), original)
            self.assertEqual(prepare(p), first)
            # Interrupted receipt publication replays the immutable original.
            (p/'run-history/pre-copy-repair-v2/repair-admission.json').unlink()
            self.assertEqual(prepare(p), first)


def load_orchestration(fake):
    tree = ast.parse(Path(__file__).with_name('generate_pairs.py').read_text())
    tree.body = [node for node in tree.body if not (
        isinstance(node, ast.ImportFrom) and node.module == 'unsloth' or
        isinstance(node, ast.Import) and any(alias.name == 'torch' for alias in node.names) or
        isinstance(node, ast.If) and isinstance(node.test, ast.Compare))]
    class ReplaceModelBoundary(ast.NodeTransformer):
        def visit_FunctionDef(self, node):
            if node.name == 'generate_uncached':
                node.body = ast.parse('return _fake_generate(ids, phase, prompts, max_new, sample)').body
                return node
            return self.generic_visit(node)
    tree = ast.fix_missing_locations(ReplaceModelBoundary().visit(tree))
    tokenizer = types.SimpleNamespace(pad_token_id=0)
    factory = types.SimpleNamespace(from_pretrained=lambda **kw:(object(),tokenizer), for_inference=lambda m:None)
    namespace = {'FastLanguageModel':factory, 'torch':types.SimpleNamespace(manual_seed=lambda n:None,bfloat16='fixture'), '_fake_generate':fake}
    exec(compile(tree, 'generate_pairs.py', 'exec'), namespace)
    return namespace


class RetryBoundary(unittest.TestCase):
    def test_resume_reuses_first_attempt_and_completed_retry_notes(self):
        calls = []
        def boundary(ids, phase, prompts, max_new, sample):
            calls.append(phase)
            text = (json.dumps({'all_supported':True,'source_claim_count':1,'issues':[]})
                    if phase.endswith('in_ai') or phase.endswith('in_human')
                    else 'distinct fragments convey the preserved source content')
            return [{'text':text,'truncated':False,'request':10+len(calls)} for _ in ids]
        env = load_orchestration(boundary)
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp); out=root/'generated'; out.mkdir(); source=root/'human.jsonl'
            row={'id':'H0001','human':HUMAN,'document_id':'doc1','method':'notes_regeneration','split':'train'}
            source.write_text(json.dumps(row)+'\n'); env['SOURCE_SHA256']=hashlib.sha256(source.read_bytes()).hexdigest()
            (out/'pairs-audit.jsonl').write_text('')
            phases=[('paraphrase_or_notes', env['NOTES']+HUMAN, HUMAN),
                    ('fresh_notes_regeneration', env['REGEN'][0]+env['REGEN_SUFFIX']+HUMAN, HUMAN),
                    ('fresh_retry_notes', env['NOTES']+HUMAN, 'distinct fragments convey the preserved source content')]
            raw=[{'id':'H0001','phase':phase,'messages':[{'role':'user','content':prompt}],
                  'response':text,'truncated':False,'request':i+1} for i,(phase,prompt,text) in enumerate(phases)]
            (out/'model-requests.jsonl').write_text(''.join(json.dumps(r)+'\n' for r in raw))
            (out/'pair-attempt-history.jsonl').write_text(json.dumps({'id':'H0001','outcome':'COPY_FAILURE_SINGLE_FRESH_RETRY'})+'\n')
            env['run'](argparse.Namespace(input=source,output=out,limit=0,batch_size=1,deadline_unix=0))
            self.assertEqual(calls, ['fresh_retry_regeneration','human_claims_in_ai','ai_claims_in_human'])
            result=json.loads((out/'pairs-audit.jsonl').read_text())
            self.assertTrue(result['accepted']); self.assertEqual(result['copy_retry_count'], 1)

    def test_interrupted_reservation_never_resamples(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp); requests=root/'requests.jsonl'; reservations=root/'reservations.jsonl'
            cache=RequestCache(requests,reservations)
            cache.reserve('H0001','fresh_retry_notes','prompt')
            recovered=RequestCache(requests,reservations)
            with self.assertRaisesRegex(RuntimeError,'do not resample'):
                recovered.lookup('H0001','fresh_retry_notes','prompt')
            requests.write_text(json.dumps({'id':'H0001','phase':'fresh_retry_notes',
                'messages':[{'role':'user','content':'prompt'}],'response':'saved',
                'truncated':False,'request':1})+'\n')
            self.assertEqual(RequestCache(requests,reservations).lookup('H0001','fresh_retry_notes','prompt')['text'],'saved')
            with reservations.open('ab') as handle:
                handle.write(b'{"key":')
            with self.assertRaisesRegex(AssertionError, 'Incomplete journal tail'):
                RequestCache(requests,reservations)

    def execute(self, second_copies, prior_repair=False):
        calls = []
        def model_call(ids, phase, prompts, max_new, sample):
            calls.append((phase, prompts, sample))
            if phase in ['human_claims_in_ai','ai_claims_in_human']:
                text = json.dumps({'all_supported':True,'source_claim_count':1,'issues':[]})
            elif phase.startswith('fresh_retry') and not second_copies:
                text = 'distinct fragments convey the preserved source content'
            else:
                text = HUMAN
            return [{'text':text,'truncated':False,'request':len(calls)} for _ in ids]
        env = load_orchestration(model_call)
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); source = root/'human.jsonl'; output = root/'generated'; output.mkdir()
            row = {'id':'H0001','human':HUMAN,'document_id':'doc1','method':'notes_regeneration','split':'train'}
            source.write_text(json.dumps(row)+'\n'); env['SOURCE_SHA256'] = hashlib.sha256(source.read_bytes()).hexdigest()
            existing = dict(row, accepted=False,copy_repair_pending=True) if prior_repair else None
            (output/'pairs-audit.jsonl').write_text(json.dumps(existing)+'\n' if existing else '')
            env['run'](argparse.Namespace(input=source,output=output,limit=0,batch_size=1,deadline_unix=0))
            result = json.loads((output/'pairs-audit.jsonl').read_text())
            return calls, result

    def test_one_retry_then_fidelity(self):
        calls, result = self.execute(False)
        self.assertTrue(result['accepted'])
        self.assertEqual(result['copy_retry_count'], 1)
        self.assertEqual([x[0] for x in calls], ['paraphrase_or_notes','fresh_notes_regeneration',
            'fresh_retry_notes','fresh_retry_regeneration','human_claims_in_ai','ai_claims_in_human'])
        self.assertNotIn(HUMAN, calls[3][1][0])
        self.assertTrue(all(x[2] for x in calls[:4]))

    def test_second_failure_is_dropped_without_judging(self):
        calls, result = self.execute(True)
        self.assertEqual(len(calls), 4)
        self.assertFalse(result['accepted'])
        self.assertIn('copy_guard_failed_after_single_fresh_retry', result['rejection_reasons'])

    def test_existing_failure_gets_only_its_one_fresh_retry(self):
        calls, result = self.execute(True, True)
        self.assertEqual(len(calls), 2)
        self.assertFalse(result['accepted'])
        self.assertEqual(result['copy_retry_count'], 1)


if __name__ == '__main__':
    unittest.main()
