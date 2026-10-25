"""Owner delivery gate regression: Joel's rejected metta wording must not reach him."""
from __future__ import annotations

import importlib.util
import json
import pathlib
import subprocess
import sys
from unittest import mock
import tempfile
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "tools" / "humanization" / "owner_delivery_gate.py"
spec = importlib.util.spec_from_file_location("owner_delivery_gate", SCRIPT)
gate = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gate)

REJECTED = (
    "With metta, you can wish for suffering to end without making it your job "
    "to end it. Try to force it, and even that wish can turn desperate—or leave "
    "you afraid you'll fail."
)
POSITIVE = "The ferry arrived late—by then, her friends had left the pier."


class OwnerDeliveryGateTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.folder = pathlib.Path(self.tmp.name)
        self.draft = self.folder / "draft.txt"
        self.context = self.folder / "context.txt"
        self.source = self.folder / "source.txt"
        self.manifest = self.folder / "admission.json"
        self.output = self.folder / "for-owner.txt"
        self.proof = self.folder / "for-owner.proof.json"

    def initialize(self, draft=POSITIVE, source=None, context=None):
        self.draft.write_text(draft, encoding="utf-8")
        self.context.write_text(
            context if context is not None else "Before.\n\n" + draft + "\n\nAfter.",
            encoding="utf-8",
        )
        self.source.write_text(
            source if source is not None else "Original source: " + draft, encoding="utf-8"
        )
        r = self.call("init")
        self.assertEqual(r.returncode, 0, r.stderr)
        return json.loads(self.manifest.read_text(encoding="utf-8"))

    def call(self, action):
        args = [
            sys.executable,
            str(SCRIPT),
            action,
            "--draft", str(self.draft),
            "--context", str(self.context),
            "--source", str(self.source),
            "--manifest", str(self.manifest),
        ]
        if action == "deliver":
            args += ["--out", str(self.output), "--proof", str(self.proof)]
        return subprocess.run(args, capture_output=True, text=True, timeout=45)

    def save_manifest(self, data):
        self.manifest.write_text(
            json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )

    def fill_reviews(self, manifest):
        vals = {
            k: manifest[k]
            for k in ("candidate_sha256", "context_sha256", "source_sha256")
        }
        for i, role in enumerate(gate.ROLES):
            review = {
                "schema": gate.REVIEW_SCHEMA,
                "role": role,
                **vals,
                "verdict": "PASS",
                "unresolved": [],
                "reviewer": {
                    "name": f"Independent test critic {i}",
                    "context_id": f"critic-example-context-{i}",
                    "origin": "unittest fixture only; not real authorial evidence",
                },
                "evidence": (
                    "Unittest-only source and literal candidate comparison; "
                    "the ferry-arrival relation and timing remain unchanged."
                ),
                "resolved_tell_ids": ["T12"],
                "resolved_lint_labels": [
                    finding["label"] for finding in manifest["lint"]["findings"]
                ],
            }
            fn = self.folder / f"{role}.review.json"
            fn.write_text(json.dumps(review), encoding="utf-8")
            manifest["review_files"][role] = fn.name

    def ready(self, draft=POSITIVE):
        manifest = self.initialize(draft)
        manifest["status"] = "READY_FOR_CHECK"
        manifest["writer"] = {"name": "GPT test writer", "context_id": "writer-test"}
        for row in manifest["tell_ledger"]:
            row.update({
                "status": "ABSENT",
                "evidence": "No such operation in these literal source words.",
                "resolution": "NONE",
            })
        for finding in manifest["lint"]["findings"]:
            finding["disposition"] = "JUSTIFIED_KEEP"
            finding["reason"] = (
                "No actual AI-shaped operation at this point; exact source "
                "and cold-reader evidence supports keeping the syntax."
            )
        self.fill_reviews(manifest)
        self.save_manifest(manifest)
        return manifest

    def test_pending_manifest_denies_delivery_even_with_clear_lint(self):
        manifest = self.initialize()
        self.assertIn(manifest["lint"]["verdict_at_init"], ("CLEAR", "REVIEW"))
        result = self.call("deliver")
        self.assertEqual(result.returncode, 2, result.stderr)
        self.assertIn("READY_FOR_CHECK", result.stderr)
        self.assertFalse(self.output.exists())
        self.assertFalse(self.proof.exists())

    def test_joels_exact_rejected_metta_draft_fails_mechanically(self):
        m = self.ready(REJECTED)
        self.assertEqual(m["lint"]["verdict_at_init"], "FAIL")
        self.assertIn("E186", [x["label"][:4] for x in m["lint"]["findings"]])
        # Even with forged all-ABSENT dispositions and separate PASS reviews,
        # the linter must remain a blocking independent computation.
        result = self.call("deliver")
        self.assertEqual(result.returncode, 2)
        self.assertIn("mechanical tells_lint verdict FAIL", result.stderr)
        self.assertFalse(self.output.exists())
        self.assertFalse(self.proof.exists())

    def test_properly_reviewed_natural_dash_passes_without_blanket_ban(self):
        self.ready()
        result = self.call("deliver")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(self.output.read_bytes(), self.draft.read_bytes())
        proof = json.loads(self.proof.read_text(encoding="utf-8"))
        self.assertIn(proof["lint_verdict"], ("CLEAR", "REVIEW"))
        self.assertNotIn("dash", " ".join(f["label"] for f in json.loads(
            self.manifest.read_text())["lint"]["findings"]).lower())
        self.assertEqual(proof["candidate_sha256"], gate.sha(self.draft.read_bytes()))
        self.assertEqual(set(proof["reviews"]), set(gate.ROLES))

    def test_genuine_contrast_tell_can_be_explicitly_justified(self):
        manifest = self.ready()
        row = next(row for row in manifest["tell_ledger"] if row["id"] == "T12")
        row.update({
            "status": "PRESENT",
            "resolution": "JUSTIFIED_KEEP",
            "reason": (
                "The after-the-dash contrast is a causal time relation, "
                "not a symmetrical therapy maxim."
            ),
            "evidence": "By then her friends had already left the pier.",
        })
        self.save_manifest(manifest)
        self.assertEqual(self.call("check").returncode, 0)

    def test_present_tell_requires_independent_review_and_reason(self):
        manifest = self.ready()
        t12 = next(x for x in manifest["tell_ledger"] if x["id"] == "T12")
        t12["status"] = "PRESENT"
        t12["resolution"] = "JUSTIFIED_KEEP"
        t12["reason"] = "A real sequence caused by the ferry arriving after friends left."
        self.save_manifest(manifest)
        for role in gate.ROLES:
            p = self.folder / (role + ".review.json")
            review = json.loads(p.read_text())
            review["resolved_tell_ids"] = []
            p.write_text(json.dumps(review))
        result = self.call("deliver")
        self.assertEqual(result.returncode, 2)
        self.assertIn("did not explicitly review justified tells", result.stderr)
        self.assertFalse(self.output.exists())

    def test_unknown_or_duplicate_tell_id_cannot_pass(self):
        manifest = self.ready()
        manifest["tell_ledger"][0]["id"] = "T42"
        self.save_manifest(manifest)
        result = self.call("check")
        self.assertEqual(result.returncode, 2)
        self.assertIn("tell inventory incomplete or stale", result.stderr)

    def test_uncertain_tell_blocks(self):
        manifest = self.ready()
        manifest["tell_ledger"][0]["status"] = "UNCERTAIN"
        self.save_manifest(manifest)
        self.assertIn("UNCERTAIN", self.call("check").stderr)

    def test_changed_draft_or_context_invalidates_every_review(self):
        self.ready()
        self.draft.write_text(POSITIVE + "\nIt was raining.", encoding="utf-8")
        self.context.write_text("Before.\n\n" + self.draft.read_text() + "\n\nAfter.")
        result = self.call("deliver")
        self.assertEqual(result.returncode, 2)
        self.assertIn("candidate_sha256", result.stderr)
        self.assertFalse(self.output.exists())

    def test_changed_source_invalidates_every_review(self):
        self.ready()
        self.source.write_text(self.source.read_text() + " Extra claim.")
        result = self.call("deliver")
        self.assertEqual(result.returncode, 2)
        self.assertIn("source_sha256", result.stderr)
        self.assertFalse(self.output.exists())

    def test_changed_review_hash_or_reviewer_context_denies(self):
        self.ready()
        p = self.folder / "cold_read_2.review.json"
        review = json.loads(p.read_text())
        review["reviewer"]["context_id"] = "writer-test"
        p.write_text(json.dumps(review))
        result = self.call("deliver")
        self.assertEqual(result.returncode, 2)
        self.assertIn("writer and reviewer contexts are identical", result.stderr)

    def test_repeated_review_context_denies_freshness_claim(self):
        self.ready()
        p = self.folder / "cold_read_2.review.json"
        review = json.loads(p.read_text())
        review["reviewer"]["context_id"] = "critic-example-context-1"
        p.write_text(json.dumps(review))
        result = self.call("check")
        self.assertEqual(result.returncode, 2)
        self.assertIn("reviewers shared a context", result.stderr)

    def test_draft_not_in_context_denies_init(self):
        self.draft.write_text(POSITIVE)
        self.context.write_text("This is an unrelated passage.")
        self.source.write_text(POSITIVE)
        self.assertIn("context must contain", self.call("init").stderr)
        self.assertFalse(self.manifest.exists())

    def test_candidate_appears_twice_in_context_denies(self):
        self.draft.write_text(POSITIVE)
        self.context.write_text(POSITIVE + "\n\n" + POSITIVE)
        self.source.write_text(POSITIVE)
        self.assertIn("exact draft bytes exactly once", self.call("init").stderr)

    def test_existing_owner_text_and_proof_are_not_overwritten(self):
        self.ready()
        self.output.write_text("owner original; not our candidate")
        result = self.call("deliver")
        self.assertEqual(result.returncode, 2)
        self.assertIn("refusing to replace existing artifact", result.stderr)
        self.assertEqual(self.output.read_text(), "owner original; not our candidate")
        self.assertFalse(self.proof.exists())

    def test_reviews_are_bound_to_exact_candidate(self):
        self.ready()
        p = self.folder / "preservation.review.json"
        review = json.loads(p.read_text())
        review["candidate_sha256"] = "0" * 64
        p.write_text(json.dumps(review))
        r = self.call("deliver")
        self.assertEqual(r.returncode, 2)
        self.assertIn("preservation review", r.stderr)
        self.assertIn("candidate_sha256 mismatch", r.stderr)

    def test_tampering_with_manifest_fingerprint_is_detected(self):
        m = self.ready()
        m["lint"]["stdout_sha256"] = "f" * 64
        self.save_manifest(m)
        result = self.call("check")
        self.assertEqual(result.returncode, 2)
        self.assertIn("linter changed since init", result.stderr)


    def test_lint_review_needs_independent_confirmation(self):
        manifest = self.ready()
        self.assertTrue(manifest["lint"]["findings"])
        p = self.folder / "cold_read_2.review.json"
        review = json.loads(p.read_text())
        review["resolved_lint_labels"] = []
        p.write_text(json.dumps(review))
        r = self.call("deliver")
        self.assertEqual(r.returncode, 2)
        self.assertIn("did not explicitly review lint findings", r.stderr)
        self.assertFalse(self.output.exists())

    def test_linter_unparseable_review_fails_closed(self):
        fake_run = subprocess.CompletedProcess(
            args=["tells_lint"], returncode=1, stdout="verdict: REVIEW\n",
            stderr=""
        )
        with mock.patch.object(gate.subprocess, "run", return_value=fake_run):
            with self.assertRaisesRegex(gate.GateError, "REVIEW without parseable"):
                gate.lint(POSITIVE.encode(), POSITIVE.encode())

    def test_inventory_future_identifier_is_not_silently_dropped(self):
        example = b"**T01 \xe2\x80\x94 First.**\n**T100 \xe2\x80\x94 New.**\n**C04 \xe2\x80\x94 End.**\n"
        self.assertEqual(gate.inventory_ids(example), ["T01", "T100", "C04"])
        broken = example.replace(b"T100 \xe2\x80\x94", b"T100 :")
        with self.assertRaisesRegex(gate.GateError, "unrecognized"):
            gate.inventory_ids(broken)

    def test_unhashable_manifest_id_fails_closed_not_crashes(self):
        m = self.ready()
        m["tell_ledger"][0]["id"] = ["T01"]
        self.save_manifest(m)
        r = self.call("deliver")
        self.assertEqual(r.returncode, 2)
        self.assertIn("tell ID must be a string", r.stderr)
        self.assertFalse(self.output.exists())

    def test_malformed_reviewer_confirmation_is_blocked(self):
        self.ready()
        p = self.folder / "cold_read_1.review.json"
        x = json.loads(p.read_text())
        x["resolved_lint_labels"] = 42
        p.write_text(json.dumps(x))
        r = self.call("deliver")
        self.assertEqual(r.returncode, 2)
        self.assertIn("resolved_lint_labels must contain string IDs", r.stderr)

    def test_unwritable_proof_path_creates_no_owner_draft(self):
        self.ready()
        not_directory = self.folder / "existing-file"
        not_directory.write_text("not a directory")
        fake_proof = not_directory / "proof.json"
        cmd = [
            sys.executable, str(SCRIPT), "deliver",
            "--draft", str(self.draft),
            "--context", str(self.context),
            "--source", str(self.source),
            "--manifest", str(self.manifest),
            "--out", str(self.output),
            "--proof", str(fake_proof),
        ]
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        self.assertEqual(r.returncode, 2)
        self.assertFalse(self.output.exists())
        self.assertFalse(fake_proof.exists())

    def test_second_install_failure_removes_new_proof(self):
        self.ready()
        orig_link = gate.os.link

        def one_link_then_failure(src, dst):
            if pathlib.Path(dst) == self.output:
                raise OSError("simulated exclusive owner export link failure")
            return orig_link(src, dst)

        with mock.patch.object(gate.os, "link", side_effect=one_link_then_failure):
            code = gate.main([
                "deliver", "--draft", str(self.draft),
                "--context", str(self.context),
                "--source", str(self.source),
                "--manifest", str(self.manifest),
                "--out", str(self.output),
                "--proof", str(self.proof),
            ])
        self.assertEqual(code, 2)
        self.assertFalse(self.output.exists())
        self.assertFalse(self.proof.exists())

    def test_export_uses_validated_snapshot_when_draft_changes_after_audit(self):
        self.ready()
        original = self.draft.read_bytes()
        original_validate = gate.validate

        def mutate_after_validating(args):
            proof, snapshot = original_validate(args)
            self.draft.write_text("MUTATED AFTER VALIDATION")
            return proof, snapshot

        with mock.patch.object(gate, "validate", side_effect=mutate_after_validating):
            code = gate.main([
                "deliver", "--draft", str(self.draft),
                "--context", str(self.context),
                "--source", str(self.source),
                "--manifest", str(self.manifest),
                "--out", str(self.output),
                "--proof", str(self.proof),
            ])
        self.assertEqual(code, 0)
        self.assertEqual(self.output.read_bytes(), original)
        receipt = json.loads(self.proof.read_text())
        self.assertEqual(gate.sha(original), receipt["candidate_sha256"])
        self.assertNotEqual(self.output.read_bytes(), self.draft.read_bytes())


if __name__ == "__main__":
    unittest.main()
