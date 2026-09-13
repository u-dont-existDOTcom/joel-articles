from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "scripts" / "somatic_activation_steering.py"
SPEC = importlib.util.spec_from_file_location("somatic_activation_steering", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


@unittest.skipUnless(importlib.util.find_spec("torch"), "torch is required for hook tests")
class ResidualHookTests(unittest.TestCase):
    def setUp(self) -> None:
        import torch

        self.torch = torch

    def test_tuple_preservation_and_targeted_batch(self) -> None:
        hidden = self.torch.zeros((2, 4, 3), dtype=self.torch.float32)
        aux = {"cache": "kept"}
        vector = self.torch.tensor([1.0, 0.0, 0.0])
        hook = MODULE.ResidualAdditionHook(vector, 2.0, start_position=2, steered_batch_index=1)
        result = hook(None, (), (hidden, aux))
        self.assertIs(result[1], aux)
        self.assertTrue(self.torch.equal(result[0][0], hidden[0]))
        self.assertTrue(self.torch.equal(result[0][1, :2], hidden[1, :2]))
        self.assertTrue(self.torch.equal(result[0][1, 2:, 0], self.torch.tensor([2.0, 2.0])))

    def test_alpha_zero_is_bit_identical(self) -> None:
        hidden = self.torch.randn((2, 5, 7), generator=self.torch.Generator().manual_seed(5))
        vector = self.torch.randn((7,), generator=self.torch.Generator().manual_seed(6))
        hook = MODULE.ResidualAdditionHook(vector, 0.0, start_position=1, steered_batch_index=1)
        result = hook(None, (), hidden)
        self.assertTrue(self.torch.equal(result, hidden))
        self.assertEqual(hook.records[-1].projection_delta_last, 0.0)

    def test_sign_reversal_changes_projection_oppositely(self) -> None:
        hidden = self.torch.randn((2, 3, 5), generator=self.torch.Generator().manual_seed(10))
        vector = self.torch.randn((5,), generator=self.torch.Generator().manual_seed(11))
        negative = MODULE.ResidualAdditionHook(vector, -1.0, 1, 1)
        positive = MODULE.ResidualAdditionHook(vector, 1.0, 1, 1)
        negative(None, (), hidden)
        positive(None, (), hidden)
        neg_delta = negative.records[-1].projection_delta_last
        pos_delta = positive.records[-1].projection_delta_last
        self.assertLess(neg_delta, 0)
        self.assertGreater(pos_delta, 0)
        self.assertAlmostEqual(abs(neg_delta), abs(pos_delta), places=5)


class ManifestTests(unittest.TestCase):
    def test_condition_grid_is_predeclared_and_unique(self) -> None:
        config = json.loads(
            (
                ROOT
                / "tasks"
                / "somatic-r15-clean-continuation-20260830"
                / "activation-steering-20260902"
                / "experiment_config.json"
            ).read_text(encoding="utf-8")
        )
        conditions = list(MODULE.condition_grid(config))
        self.assertEqual(len(conditions), 63)
        self.assertEqual(len({MODULE.canonical_json(item) for item in conditions}), 63)
        self.assertEqual(sum(item["direction_kind"] == "baseline" for item in conditions), 3)
        self.assertEqual(sum(item["direction_kind"] == "random_matched_norm" for item in conditions), 6)

    def test_hash_is_exact_utf8(self) -> None:
        self.assertEqual(
            MODULE.sha256_text("afterward"),
            "d1e9283f4b919a7237426077216c1a2661290707981ebec558c4f8ef45b315a9",
        )

    def test_opaque_ids_change_with_condition(self) -> None:
        config = {"blinding": {"opaque_id_salt": "x"}}
        first = {"prompt_id": "H01", "layer": 6, "alpha": 1.0, "direction_kind": "contrastive"}
        second = {"prompt_id": "H01", "layer": 6, "alpha": -1.0, "direction_kind": "contrastive"}
        self.assertNotEqual(MODULE.opaque_id(config, first), MODULE.opaque_id(config, second))

    def test_manifest_reverification_preserves_pre_experiment_head(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            output_dir = Path(temp_dir)
            original_head = "d" * 40
            MODULE.write_json(
                output_dir / "RUN-MANIFEST.json",
                {"repository_head_before_experiment_commit": original_head},
            )
            manifest = MODULE.write_run_manifest(
                {"experiment_id": "test-fixed-head"}, output_dir
            )
            self.assertEqual(
                manifest["repository_head_before_experiment_commit"], original_head
            )


if __name__ == "__main__":
    unittest.main()
