#!/usr/bin/env python3
"""Run the frozen Somatic activation-steering mechanism experiment.

This module performs no editorial or detector judgment. It derives paired
residual-stream directions, applies them causally during generation, records
mechanical telemetry, and produces a blinded packet.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import os
import platform
import re
import subprocess
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CONFIG = (
    ROOT
    / "tasks"
    / "somatic-r15-clean-continuation-20260830"
    / "activation-steering-20260902"
    / "experiment_config.json"
)


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def sha256_text(value: str) -> str:
    return sha256_bytes(value.encode("utf-8"))


def file_sha256(path: Path, chunk_size: int = 1024 * 1024) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        while chunk := handle.read(chunk_size):
            digest.update(chunk)
    return digest.hexdigest()


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def resolve_repo_path(value: str) -> Path:
    path = (ROOT / value).resolve()
    path.relative_to(ROOT.resolve())
    return path


def require_ml() -> tuple[Any, Any, Any, Any]:
    try:
        import numpy as np
        import torch
        import transformers
        from huggingface_hub import snapshot_download
    except ImportError as exc:  # pragma: no cover - exercised by runtime setup
        raise SystemExit(
            "Missing experiment dependencies. Install the pinned requirements first."
        ) from exc
    return np, torch, transformers, snapshot_download


def get_hidden(output: Any) -> Any:
    if isinstance(output, tuple):
        return output[0]
    if isinstance(output, list):
        return output[0]
    return output


def replace_hidden(output: Any, hidden: Any) -> Any:
    if isinstance(output, tuple):
        return (hidden,) + output[1:]
    if isinstance(output, list):
        return [hidden] + output[1:]
    return hidden


@dataclass
class HookRecord:
    affected_positions: int
    projection_pre_last: float
    projection_post_last: float
    projection_delta_last: float
    projection_pre_mean: float
    projection_post_mean: float


class ResidualAdditionHook:
    """Tuple-preserving post-block residual addition with telemetry."""

    def __init__(
        self,
        vector: Any,
        alpha: float,
        start_position: int,
        steered_batch_index: int = 1,
    ) -> None:
        self.vector = vector
        self.alpha = float(alpha)
        self.start_position = int(start_position)
        self.steered_batch_index = int(steered_batch_index)
        self.records: list[HookRecord] = []

    def __call__(self, _module: Any, _inputs: tuple[Any, ...], output: Any) -> Any:
        hidden = get_hidden(output)
        if hidden.ndim != 3:
            raise RuntimeError(f"Expected rank-3 block output, received {tuple(hidden.shape)}")
        batch_index = self.steered_batch_index
        if batch_index >= hidden.shape[0]:
            raise RuntimeError("Steered batch index is outside the block output batch.")
        # Prefill uses the configured assistant-cue position. Cached decoding
        # presents exactly one current token, which is always intervention-eligible.
        start = 0 if hidden.shape[1] == 1 else min(max(self.start_position, 0), hidden.shape[1])
        affected = hidden.shape[1] - start
        if affected <= 0:
            raise RuntimeError("No generation positions were available for intervention.")

        vector = self.vector.to(device=hidden.device, dtype=hidden.dtype)
        if vector.ndim != 1 or vector.shape[0] != hidden.shape[-1]:
            raise RuntimeError("Steering vector does not match the residual width.")
        unit = vector / vector.norm().clamp_min(1e-12)
        selected = hidden[batch_index, start:, :]
        pre_projection = selected @ unit

        modified = hidden.clone()
        modified[batch_index, start:, :] = selected + self.alpha * vector
        post_selected = modified[batch_index, start:, :]
        post_projection = post_selected @ unit
        self.records.append(
            HookRecord(
                affected_positions=int(affected),
                projection_pre_last=float(pre_projection[-1].detach().cpu()),
                projection_post_last=float(post_projection[-1].detach().cpu()),
                projection_delta_last=float((post_projection[-1] - pre_projection[-1]).detach().cpu()),
                projection_pre_mean=float(pre_projection.mean().detach().cpu()),
                projection_post_mean=float(post_projection.mean().detach().cpu()),
            )
        )
        return replace_hidden(output, modified)


def decoder_layers(model: Any, expected_count: int) -> Any:
    try:
        layers = model.model.layers
    except AttributeError as exc:
        raise RuntimeError("Pinned Qwen2 decoder surface model.model.layers is unavailable.") from exc
    if len(layers) != expected_count:
        raise RuntimeError(f"Expected {expected_count} decoder blocks, found {len(layers)}.")
    return layers


def set_deterministic_runtime(torch: Any, seed: int) -> None:
    os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")
    torch.manual_seed(seed)
    torch.set_num_threads(min(4, os.cpu_count() or 1))
    try:
        torch.set_num_interop_threads(1)
    except RuntimeError:
        pass
    torch.use_deterministic_algorithms(True)


def load_runtime(config: dict[str, Any], local_files_only: bool = False) -> tuple[Any, Any, dict[str, Any]]:
    np, torch, transformers, snapshot_download = require_ml()
    del np
    model_spec = config["model"]
    if model_spec["device"] != "cpu" or model_spec["dtype"] != "float32":
        raise RuntimeError("The frozen protocol permits only CPU float32 execution.")
    set_deterministic_runtime(torch, config["decoding"]["seed"])
    tokenizer = transformers.AutoTokenizer.from_pretrained(
        model_spec["repo_id"],
        revision=model_spec["revision"],
        trust_remote_code=False,
        local_files_only=local_files_only,
    )
    model = transformers.AutoModelForCausalLM.from_pretrained(
        model_spec["repo_id"],
        revision=model_spec["revision"],
        trust_remote_code=False,
        local_files_only=local_files_only,
        torch_dtype=torch.float32,
    ).to("cpu")
    model.eval()

    architecture = model.config.architectures[0] if model.config.architectures else None
    assertions = {
        "architecture": architecture,
        "num_hidden_layers": int(model.config.num_hidden_layers),
        "hidden_size": int(model.config.hidden_size),
    }
    expected = {
        "architecture": model_spec["architecture"],
        "num_hidden_layers": model_spec["num_hidden_layers"],
        "hidden_size": model_spec["hidden_size"],
    }
    if assertions != expected:
        raise RuntimeError(f"Pinned model identity/geometry mismatch: {assertions} != {expected}")
    decoder_layers(model, expected["num_hidden_layers"])

    snapshot = Path(
        snapshot_download(
            model_spec["repo_id"],
            revision=model_spec["revision"],
            local_files_only=True,
        )
    )
    identity_files = [
        "config.json",
        "generation_config.json",
        "model.safetensors",
        "tokenizer.json",
        "tokenizer_config.json",
        "vocab.json",
        "merges.txt",
    ]
    file_records = []
    for name in identity_files:
        path = snapshot / name
        if not path.is_file():
            raise RuntimeError(f"Pinned runtime file is missing: {name}")
        file_records.append({"name": name, "bytes": path.stat().st_size, "sha256": file_sha256(path)})
    runtime = {
        "repo_id": model_spec["repo_id"],
        "revision": model_spec["revision"],
        "snapshot_path": str(snapshot),
        "architecture": architecture,
        "num_hidden_layers": int(model.config.num_hidden_layers),
        "hidden_size": int(model.config.hidden_size),
        "parameter_count": int(sum(parameter.numel() for parameter in model.parameters())),
        "dtype": str(next(model.parameters()).dtype),
        "device": str(next(model.parameters()).device),
        "torch_version": torch.__version__,
        "transformers_version": transformers.__version__,
        "python_version": platform.python_version(),
        "platform": platform.platform(),
        "files": file_records,
    }
    return model, tokenizer, runtime


def render_chat(tokenizer: Any, system: str, user: str, response: str | None = None) -> Any:
    messages = [{"role": "system", "content": system}, {"role": "user", "content": user}]
    if response is not None:
        messages.append({"role": "assistant", "content": response})
    return tokenizer.apply_chat_template(
        messages,
        tokenize=True,
        add_generation_prompt=response is None,
        return_tensors="pt",
    )


def response_positions(tokenizer: Any, prompt_ids: Any, full_ids: Any) -> list[int]:
    prompt = prompt_ids[0].tolist()
    full = full_ids[0].tolist()
    if full[: len(prompt)] != prompt:
        raise RuntimeError("Native chat template response is not prefixed by the generation prompt.")
    special = set(tokenizer.all_special_ids)
    positions = [index for index in range(len(prompt), len(full)) if full[index] not in special]
    if not positions:
        raise RuntimeError("No non-special response tokens were found for activation pooling.")
    return positions


def capture_side_activations(
    model: Any,
    tokenizer: Any,
    system: str,
    instruction: str,
    response: str,
) -> list[Any]:
    _, torch, _, _ = require_ml()
    prompt_ids = render_chat(tokenizer, system, instruction)
    full_ids = render_chat(tokenizer, system, instruction, response=response)
    positions = response_positions(tokenizer, prompt_ids, full_ids)
    attention_mask = torch.ones_like(full_ids)
    with torch.inference_mode():
        outputs = model(
            input_ids=full_ids,
            attention_mask=attention_mask,
            use_cache=False,
            output_hidden_states=True,
            return_dict=True,
        )
    if len(outputs.hidden_states) != model.config.num_hidden_layers + 1:
        raise RuntimeError("Unexpected hidden-state layer count.")
    return [
        outputs.hidden_states[layer + 1][0, positions, :].mean(dim=0).detach().cpu()
        for layer in range(model.config.num_hidden_layers)
    ]


def derive_vectors(
    model: Any,
    tokenizer: Any,
    config: dict[str, Any],
    pairs_doc: dict[str, Any],
    output_dir: Path,
) -> dict[str, Any]:
    np, torch, _, _ = require_ml()
    system = (
        "Realize the supplied Somatic thought in one compact paragraph. "
        "Preserve its meaning; do not add factual claims."
    )
    pair_records = []
    training_differences: dict[int, list[Any]] = {
        layer: [] for layer in range(model.config.num_hidden_layers)
    }
    calibration_activations = []
    for pair in pairs_doc["pairs"]:
        print(f"[derive] {pair['pair_id']} {pair['split']}", flush=True)
        positive = capture_side_activations(
            model, tokenizer, system, pair["instruction"], pair["positive"]
        )
        negative = capture_side_activations(
            model, tokenizer, system, pair["instruction"], pair["negative"]
        )
        diffs = [pos - neg for pos, neg in zip(positive, negative)]
        if pair["split"] == "train":
            for layer, difference in enumerate(diffs):
                training_differences[layer].append(difference)
        elif pair["split"] == "calibration":
            calibration_activations.append((pair["pair_id"], positive, negative))
        else:
            raise RuntimeError(f"Unsupported pair split: {pair['split']}")
        pair_records.append(
            {
                "pair_id": pair["pair_id"],
                "split": pair["split"],
                "instruction_sha256": sha256_text(pair["instruction"]),
                "positive_sha256": sha256_text(pair["positive"]),
                "negative_sha256": sha256_text(pair["negative"]),
            }
        )

    vectors: dict[int, Any] = {}
    vector_records = []
    for layer, differences in training_differences.items():
        if not differences:
            raise RuntimeError("No training differences were captured.")
        vector = torch.stack(differences).mean(dim=0)
        vectors[layer] = vector
        norm = float(vector.norm())
        if not math.isfinite(norm) or norm <= 0:
            raise RuntimeError(f"Invalid steering-vector norm at layer {layer}: {norm}")
        unit = vector / vector.norm()
        calibration = []
        for pair_id, positive, negative in calibration_activations:
            gap = float(((positive[layer] - negative[layer]) @ unit).item())
            calibration.append({"pair_id": pair_id, "projection_gap": gap})
        vector_records.append(
            {
                "layer": layer,
                "l2_norm": norm,
                "training_pair_count": len(differences),
                "calibration": calibration,
                "calibration_mean_projection_gap": (
                    sum(item["projection_gap"] for item in calibration) / len(calibration)
                ),
            }
        )

    vector_path = output_dir / "vectors.npz"
    output_dir.mkdir(parents=True, exist_ok=True)
    np.savez_compressed(
        vector_path,
        **{f"layer_{layer:02d}": vector.numpy() for layer, vector in vectors.items()},
    )
    metadata = {
        "schema_version": 1,
        "experiment_id": config["experiment_id"],
        "pooling": config["data"]["pooling"],
        "direction": config["data"]["direction"],
        "block_output_hidden_state_offset": 1,
        "pairs": pair_records,
        "vectors": vector_records,
        "vector_file": {
            "path": vector_path.name,
            "sha256": file_sha256(vector_path),
            "bytes": vector_path.stat().st_size,
        },
    }
    write_json(output_dir / "DIRECTION-METADATA.json", metadata)
    return metadata


def load_vectors(output_dir: Path, expected_hash: str | None = None) -> dict[int, Any]:
    np, torch, _, _ = require_ml()
    path = output_dir / "vectors.npz"
    if expected_hash is not None and file_sha256(path) != expected_hash:
        raise RuntimeError("Steering-vector archive hash mismatch.")
    archive = np.load(path)
    return {int(key.split("_")[1]): torch.from_numpy(archive[key]).float() for key in archive.files}


def random_matched_vector(vector: Any, seed: int) -> Any:
    _, torch, _, _ = require_ml()
    generator = torch.Generator(device="cpu").manual_seed(seed)
    random_vector = torch.randn(vector.shape, generator=generator, dtype=vector.dtype)
    return random_vector / random_vector.norm() * vector.norm()


def top_p_sample(logits: Any, temperature: float, top_p: float, generator: Any) -> int:
    _, torch, _, _ = require_ml()
    scaled = logits.float() / temperature
    sorted_logits, sorted_indices = torch.sort(scaled, descending=True)
    probabilities = torch.softmax(sorted_logits, dim=-1)
    cumulative = torch.cumsum(probabilities, dim=-1)
    remove = cumulative > top_p
    remove[1:] = remove[:-1].clone()
    remove[0] = False
    sorted_logits[remove] = -float("inf")
    filtered = torch.full_like(scaled, -float("inf"))
    filtered.scatter_(0, sorted_indices, sorted_logits)
    probabilities = torch.softmax(filtered, dim=-1)
    return int(torch.multinomial(probabilities, num_samples=1, generator=generator).item())


def distribution_telemetry(unsteered_logits: Any, steered_logits: Any) -> dict[str, Any]:
    _, torch, _, _ = require_ml()
    log_unsteered = torch.log_softmax(unsteered_logits.float(), dim=-1)
    log_steered = torch.log_softmax(steered_logits.float(), dim=-1)
    p_steered = log_steered.exp()
    kl = float((p_steered * (log_steered - log_unsteered)).sum().detach().cpu())
    unsteered_top = int(unsteered_logits.argmax().item())
    steered_top = int(steered_logits.argmax().item())
    return {
        "kl_steered_vs_unsteered": max(0.0, kl),
        "unsteered_top_token_id": unsteered_top,
        "steered_top_token_id": steered_top,
        "top_token_changed": unsteered_top != steered_top,
    }


def opaque_id(config: dict[str, Any], condition: dict[str, Any]) -> str:
    source = config["blinding"]["opaque_id_salt"] + "\n" + canonical_json(condition)
    return "K" + sha256_text(source)[:11].upper()


def text_metrics(text: str) -> dict[str, int]:
    words = re.findall(r"\b[\w'-]+\b", text, flags=re.UNICODE)
    sentences = [part for part in re.split(r"(?<=[.!?])\s+", text.strip()) if part]
    return {
        "word_count": len(words),
        "sentence_count": len(sentences) if text.strip() else 0,
        "paragraph_count": len([part for part in re.split(r"\n\s*\n", text.strip()) if part]),
    }


def generate_candidate(
    model: Any,
    tokenizer: Any,
    config: dict[str, Any],
    prompt_spec: dict[str, str],
    condition: dict[str, Any],
    vector: Any | None,
) -> dict[str, Any]:
    _, torch, _, _ = require_ml()
    decoding = config["decoding"]
    user = config["prompt"]["template"].format(fragment=prompt_spec["fragment"])
    prompt_ids = render_chat(tokenizer, config["prompt"]["system"], user)
    prompt_length = int(prompt_ids.shape[1])
    generated_ids: list[int] = []
    step_records = []
    past_key_values = None
    if decoding.get("use_cache") is not True:
        raise RuntimeError("Protocol amendment A1 requires KV-cached paired decoding.")
    generator = torch.Generator(device="cpu").manual_seed(decoding["seed"])
    layers = decoder_layers(model, config["model"]["num_hidden_layers"])
    handle = None
    hook = None
    if vector is not None:
        hook = ResidualAdditionHook(
            vector=vector,
            alpha=condition["alpha"],
            start_position=prompt_length - 1,
            steered_batch_index=1,
        )
        handle = layers[condition["layer"]].register_forward_hook(hook)

    started = time.monotonic()
    stop_reason = "max_new_tokens"
    try:
        for step in range(decoding["max_new_tokens"]):
            if step == 0:
                current = prompt_ids.clone()
            else:
                current = torch.tensor([[generated_ids[-1]]], dtype=torch.long)
            if vector is None:
                total_length = prompt_length + len(generated_ids)
                attention = torch.ones((1, total_length), dtype=torch.long)
                with torch.inference_mode():
                    outputs = model(
                        input_ids=current,
                        attention_mask=attention,
                        past_key_values=past_key_values,
                        use_cache=True,
                        return_dict=True,
                    )
                    logits = outputs.logits[0, -1, :]
                    past_key_values = outputs.past_key_values
                sampled = top_p_sample(
                    logits,
                    decoding["temperature"],
                    decoding["top_p"],
                    generator,
                )
                step_records.append(
                    {
                        "step": step,
                        "sampled_token_id": sampled,
                        "kl_steered_vs_unsteered": 0.0,
                        "top_token_changed": False,
                        "unsteered_top_token_id": int(logits.argmax().item()),
                        "steered_top_token_id": int(logits.argmax().item()),
                        "affected_positions": 0,
                        "projection_pre_last": None,
                        "projection_post_last": None,
                        "projection_delta_last": 0.0,
                    }
                )
            else:
                batched = current.repeat(2, 1)
                total_length = prompt_length + len(generated_ids)
                attention = torch.ones((2, total_length), dtype=torch.long)
                with torch.inference_mode():
                    outputs = model(
                        input_ids=batched,
                        attention_mask=attention,
                        past_key_values=past_key_values,
                        use_cache=True,
                        return_dict=True,
                    )
                    logits = outputs.logits[:, -1, :]
                    past_key_values = outputs.past_key_values
                unsteered_logits = logits[0]
                steered_logits = logits[1]
                distribution = distribution_telemetry(unsteered_logits, steered_logits)
                sampled = top_p_sample(
                    steered_logits,
                    decoding["temperature"],
                    decoding["top_p"],
                    generator,
                )
                if hook is None or not hook.records:
                    raise RuntimeError("Steering hook did not record an intervention.")
                record = hook.records[-1]
                step_records.append(
                    {
                        "step": step,
                        "sampled_token_id": sampled,
                        **distribution,
                        "affected_positions": record.affected_positions,
                        "projection_pre_last": record.projection_pre_last,
                        "projection_post_last": record.projection_post_last,
                        "projection_delta_last": record.projection_delta_last,
                        "projection_pre_mean": record.projection_pre_mean,
                        "projection_post_mean": record.projection_post_mean,
                    }
                )
            generated_ids.append(sampled)
            if sampled in set(tokenizer.eos_token_id if isinstance(tokenizer.eos_token_id, list) else [tokenizer.eos_token_id]):
                stop_reason = "eos"
                break
    finally:
        if handle is not None:
            handle.remove()

    text = tokenizer.decode(generated_ids, skip_special_tokens=True).strip()
    elapsed = time.monotonic() - started
    mean_kl = sum(item["kl_steered_vs_unsteered"] for item in step_records) / len(step_records)
    top_change = sum(bool(item["top_token_changed"]) for item in step_records) / len(step_records)
    mean_projection_delta = sum(item["projection_delta_last"] for item in step_records) / len(step_records)
    candidate = {
        "schema_version": 1,
        "experiment_id": config["experiment_id"],
        "candidate_id": opaque_id(config, condition),
        "prompt_id": prompt_spec["prompt_id"],
        "condition": condition,
        "seed": decoding["seed"],
        "decoding": decoding,
        "generated_token_ids": generated_ids,
        "generated_token_count": len(generated_ids),
        "text": text,
        "candidate_sha256": sha256_text(text),
        "stop_reason": stop_reason,
        "elapsed_seconds": elapsed,
        "telemetry_summary": {
            "mean_kl_steered_vs_unsteered": mean_kl,
            "max_kl_steered_vs_unsteered": max(item["kl_steered_vs_unsteered"] for item in step_records),
            "top_token_change_fraction": top_change,
            "mean_projection_delta_last": mean_projection_delta,
        },
        "text_metrics": text_metrics(text),
        "steps": step_records,
    }
    return candidate


def actual_model_smoke(
    model: Any,
    tokenizer: Any,
    config: dict[str, Any],
    vector: Any,
) -> dict[str, Any]:
    _, torch, _, _ = require_ml()
    prompt_spec = config["prompt"]["held_out"][0]
    user = config["prompt"]["template"].format(fragment=prompt_spec["fragment"])
    prompt_ids = render_chat(tokenizer, config["prompt"]["system"], user)
    batch = prompt_ids.repeat(2, 1)
    attention = torch.ones_like(batch)
    layer = config["sweep"]["negative_control"]["layer"]
    layers = decoder_layers(model, config["model"]["num_hidden_layers"])

    zero_hook = ResidualAdditionHook(vector, 0.0, prompt_ids.shape[1] - 1, 1)
    handle = layers[layer].register_forward_hook(zero_hook)
    try:
        with torch.inference_mode():
            zero_logits = model(input_ids=batch, attention_mask=attention, use_cache=False).logits[:, -1, :]
    finally:
        handle.remove()
    zero_equal = torch.equal(zero_logits[0], zero_logits[1])
    max_abs = float((zero_logits[0] - zero_logits[1]).abs().max().item())
    if not zero_equal:
        raise RuntimeError(f"Alpha-zero logit identity failed (max abs delta {max_abs}).")

    sign_records = {}
    for alpha in (-1.0, 1.0):
        hook = ResidualAdditionHook(vector, alpha, prompt_ids.shape[1] - 1, 1)
        handle = layers[layer].register_forward_hook(hook)
        try:
            with torch.inference_mode():
                model(input_ids=batch, attention_mask=attention, use_cache=False)
        finally:
            handle.remove()
        sign_records[str(alpha)] = hook.records[-1].projection_delta_last
    if not (sign_records["-1.0"] < 0 < sign_records["1.0"]):
        raise RuntimeError(f"Sign reversal failed: {sign_records}")
    if not math.isclose(
        abs(sign_records["-1.0"]), abs(sign_records["1.0"]), rel_tol=1e-5, abs_tol=1e-5
    ):
        raise RuntimeError(f"Sign reversal magnitudes differ unexpectedly: {sign_records}")
    return {
        "alpha_zero_logits_bit_identical": zero_equal,
        "alpha_zero_max_abs_logit_delta": max_abs,
        "sign_reversal_projection_delta": sign_records,
        "layer": layer,
    }


def condition_grid(config: dict[str, Any]) -> Iterable[dict[str, Any]]:
    for prompt in config["prompt"]["held_out"]:
        yield {
            "prompt_id": prompt["prompt_id"],
            "direction_kind": "baseline",
            "layer": None,
            "alpha": 0.0,
        }
        for layer in config["sweep"]["layers"]:
            for alpha in config["sweep"]["alphas"]:
                if alpha == 0:
                    continue
                yield {
                    "prompt_id": prompt["prompt_id"],
                    "direction_kind": "contrastive",
                    "layer": layer,
                    "alpha": float(alpha),
                }
        control = config["sweep"]["negative_control"]
        for alpha in control["alphas"]:
            yield {
                "prompt_id": prompt["prompt_id"],
                "direction_kind": "random_matched_norm",
                "layer": control["layer"],
                "alpha": float(alpha),
            }


def run_sweep(
    model: Any,
    tokenizer: Any,
    config: dict[str, Any],
    vectors: dict[int, Any],
    output_dir: Path,
) -> list[dict[str, Any]]:
    prompt_by_id = {item["prompt_id"]: item for item in config["prompt"]["held_out"]}
    control_spec = config["sweep"]["negative_control"]
    random_control = random_matched_vector(vectors[control_spec["layer"]], control_spec["seed"])
    raw_path = output_dir / "RAW-RESULTS.jsonl"
    candidates = []
    with raw_path.open("w", encoding="utf-8") as raw:
        for index, condition in enumerate(condition_grid(config), start=1):
            if condition["direction_kind"] == "baseline":
                vector = None
            elif condition["direction_kind"] == "contrastive":
                vector = vectors[condition["layer"]]
            else:
                vector = random_control
            print(
                f"[sweep {index:02d}] {condition['prompt_id']} "
                f"{condition['direction_kind']} L={condition['layer']} a={condition['alpha']}",
                flush=True,
            )
            candidate = generate_candidate(
                model,
                tokenizer,
                config,
                prompt_by_id[condition["prompt_id"]],
                condition,
                vector,
            )
            raw.write(json.dumps(candidate, ensure_ascii=False) + "\n")
            raw.flush()
            candidates.append(candidate)
    return candidates


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    records = []
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            if line.strip():
                records.append(json.loads(line))
    return records


def mean(values: list[float]) -> float:
    return sum(values) / len(values) if values else 0.0


def linear_slope(xs: list[float], ys: list[float]) -> float:
    x_mean, y_mean = mean(xs), mean(ys)
    denominator = sum((x - x_mean) ** 2 for x in xs)
    return 0.0 if denominator == 0 else sum((x - x_mean) * (y - y_mean) for x, y in zip(xs, ys)) / denominator


def build_outputs(
    config: dict[str, Any],
    runtime: dict[str, Any],
    direction_metadata: dict[str, Any],
    smoke: dict[str, Any],
    candidates: list[dict[str, Any]],
    output_dir: Path,
) -> dict[str, Any]:
    by_prompt_baseline = {
        item["prompt_id"]: item
        for item in candidates
        if item["condition"]["direction_kind"] == "baseline"
    }
    map_records = []
    blinded_records = []
    for candidate in candidates:
        condition = candidate["condition"]
        baseline = by_prompt_baseline[candidate["prompt_id"]]
        mechanical = {
            "candidate_sha256": candidate["candidate_sha256"],
            "generated_token_count": candidate["generated_token_count"],
            **candidate["text_metrics"],
            **candidate["telemetry_summary"],
            "exact_text_equals_prompt_baseline": candidate["text"] == baseline["text"],
        }
        map_records.append(
            {
                "candidate_id": candidate["candidate_id"],
                "prompt_id": candidate["prompt_id"],
                "condition": condition,
                "candidate_sha256": candidate["candidate_sha256"],
            }
        )
        blinded_records.append(
            {
                "candidate_id": candidate["candidate_id"],
                "text": candidate["text"],
                "metrics": mechanical,
            }
        )
    blinded_records.sort(key=lambda item: item["candidate_id"])

    condition_map = {
        "schema_version": 1,
        "experiment_id": config["experiment_id"],
        "blinding_warning": "Do not provide this mapping to the evaluator before frozen editorial verdicts.",
        "records": map_records,
    }
    write_json(output_dir / "CONDITION-MAP.json", condition_map)
    write_json(
        output_dir / "BLINDED-EVALUATION-PACKET.json",
        {
            "schema_version": 1,
            "experiment_id": config["experiment_id"],
            "instruction": "Evaluate exact texts by opaque ID only. No condition labels are present.",
            "candidates": blinded_records,
        },
    )

    markdown = [
        "# Blinded Somatic activation-steering candidate packet",
        "",
        "Evaluate the exact text under each opaque ID. This packet does not reveal model, layer, alpha, direction, or condition. Pangram has not been run.",
        "",
    ]
    for record in blinded_records:
        markdown.extend([f"## {record['candidate_id']}", "", record["text"] or "[EMPTY OUTPUT]", ""])
    markdown.extend(
        [
            "## Blinded non-editorial outcome table",
            "",
            "| ID | SHA-256 | Tokens | Words | Sentences | Mean KL | Top-token change | Mean projection displacement | Baseline exact |",
            "|---|---|---:|---:|---:|---:|---:|---:|---|",
        ]
    )
    for record in blinded_records:
        metrics = record["metrics"]
        markdown.append(
            "| {id} | `{sha}` | {tokens} | {words} | {sentences} | {kl:.8f} | {top:.6f} | {projection:.6f} | {equal} |".format(
                id=record["candidate_id"],
                sha=metrics["candidate_sha256"],
                tokens=metrics["generated_token_count"],
                words=metrics["word_count"],
                sentences=metrics["sentence_count"],
                kl=metrics["mean_kl_steered_vs_unsteered"],
                top=metrics["top_token_change_fraction"],
                projection=metrics["mean_projection_delta_last"],
                equal=str(metrics["exact_text_equals_prompt_baseline"]).lower(),
            )
        )
    (output_dir / "BLINDED-EVALUATION-PACKET.md").write_text("\n".join(markdown) + "\n", encoding="utf-8")

    with (output_dir / "BLINDED-OUTCOME-TABLE.csv").open("w", encoding="utf-8", newline="") as handle:
        fields = ["candidate_id"] + list(blinded_records[0]["metrics"].keys())
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for record in blinded_records:
            writer.writerow({"candidate_id": record["candidate_id"], **record["metrics"]})

    aggregate = []
    for layer in config["sweep"]["layers"]:
        layer_candidates = [
            item
            for item in candidates
            if item["condition"]["direction_kind"] == "contrastive"
            and item["condition"]["layer"] == layer
        ]
        grouped = []
        for alpha in [value for value in config["sweep"]["alphas"] if value != 0]:
            subset = [item for item in layer_candidates if item["condition"]["alpha"] == alpha]
            grouped.append(
                {
                    "alpha": alpha,
                    "mean_kl": mean([item["telemetry_summary"]["mean_kl_steered_vs_unsteered"] for item in subset]),
                    "mean_top_token_change_fraction": mean([item["telemetry_summary"]["top_token_change_fraction"] for item in subset]),
                    "mean_projection_delta_last": mean([item["telemetry_summary"]["mean_projection_delta_last"] for item in subset]),
                    "exact_baseline_text_count": sum(item["text"] == by_prompt_baseline[item["prompt_id"]]["text"] for item in subset),
                }
            )
        aggregate.append(
            {
                "layer": layer,
                "by_alpha": grouped,
                "projection_delta_slope": linear_slope(
                    [item["alpha"] for item in grouped],
                    [item["mean_projection_delta_last"] for item in grouped],
                ),
                "kl_vs_abs_alpha_slope": linear_slope(
                    [abs(item["alpha"]) for item in grouped],
                    [item["mean_kl"] for item in grouped],
                ),
            }
        )
    analysis = {
        "schema_version": 1,
        "experiment_id": config["experiment_id"],
        "interpretation_boundary": "Mechanical causal telemetry only; no prose-human or editorial PASS/FAIL.",
        "candidate_count": len(candidates),
        "runtime": runtime,
        "smoke": smoke,
        "primary_aggregate": aggregate,
        "random_control": [
            {
                "candidate_id": item["candidate_id"],
                "prompt_id": item["prompt_id"],
                "alpha": item["condition"]["alpha"],
                **item["telemetry_summary"],
            }
            for item in candidates
            if item["condition"]["direction_kind"] == "random_matched_norm"
        ],
        "direction_metadata_sha256": file_sha256(output_dir / "DIRECTION-METADATA.json"),
    }
    write_json(output_dir / "ANALYSIS.json", analysis)
    write_json(output_dir / "RUNTIME-MANIFEST.json", runtime)
    write_json(output_dir / "SMOKE-RESULTS.json", smoke)
    return analysis


def verify_outputs(config: dict[str, Any], output_dir: Path) -> dict[str, Any]:
    candidates = read_jsonl(output_dir / "RAW-RESULTS.jsonl")
    expected = list(condition_grid(config))
    actual_conditions = [item["condition"] for item in candidates]
    if len(candidates) != len(expected) or {canonical_json(item) for item in actual_conditions} != {
        canonical_json(item) for item in expected
    }:
        raise RuntimeError("Raw results do not contain the exact predeclared condition grid.")
    if len({item["candidate_id"] for item in candidates}) != len(candidates):
        raise RuntimeError("Opaque candidate IDs are not unique.")
    for item in candidates:
        if item["candidate_sha256"] != sha256_text(item["text"]):
            raise RuntimeError(f"Candidate text hash mismatch: {item['candidate_id']}")
        if item["candidate_id"] != opaque_id(config, item["condition"]):
            raise RuntimeError(f"Opaque ID mismatch: {item['candidate_id']}")
    packet = load_json(output_dir / "BLINDED-EVALUATION-PACKET.json")
    if len(packet["candidates"]) != len(candidates):
        raise RuntimeError("Blinded packet candidate count mismatch.")
    raw_by_id = {item["candidate_id"]: item for item in candidates}
    for item in packet["candidates"]:
        raw = raw_by_id[item["candidate_id"]]
        if item["text"] != raw["text"] or item["metrics"]["candidate_sha256"] != raw["candidate_sha256"]:
            raise RuntimeError(f"Blinded packet identity mismatch: {item['candidate_id']}")
        forbidden = set(config["blinding"]["packet_excludes"])
        if forbidden.intersection(item):
            raise RuntimeError(f"Blinded packet leaked condition fields: {forbidden.intersection(item)}")
    verification = {
        "status": "PASS",
        "candidate_count": len(candidates),
        "unique_candidate_ids": len(candidates),
        "candidate_hashes_verified": len(candidates),
        "condition_grid_verified": True,
        "blinded_packet_verified": True,
        "pangram_run": False,
        "registered_master_edited": False,
    }
    write_json(output_dir / "VERIFICATION.json", verification)
    write_run_manifest(config, output_dir)
    return verification


def write_run_manifest(config: dict[str, Any], output_dir: Path) -> dict[str, Any]:
    manifest_path = output_dir / "RUN-MANIFEST.json"
    existing_manifest = load_json(manifest_path) if manifest_path.is_file() else {}
    initial_repository_head = existing_manifest.get("repository_head_before_experiment_commit")
    if not initial_repository_head:
        initial_repository_head = subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True
        ).strip()
    artifact_records = []
    for path in sorted(output_dir.iterdir()):
        if not path.is_file() or path.name == "RUN-MANIFEST.json":
            continue
        artifact_records.append(
            {
                "path": path.name,
                "bytes": path.stat().st_size,
                "sha256": file_sha256(path),
            }
        )
    manifest = {
        "schema_version": 1,
        "experiment_id": config["experiment_id"],
        "status": "BOUNDED_SWEEP_COMPLETE_AWAITING_BLINDED_CHAT_EVALUATION",
        "repository": "u-dont-existDOTcom/joel-articles",
        "branch": "task/somatic-r15-clean-continuation-20260830",
        "repository_head_before_experiment_commit": initial_repository_head,
        "config_sha256": file_sha256(DEFAULT_CONFIG),
        "artifacts": artifact_records,
        "candidate_count": 63,
        "pangram_run": False,
        "article_authority_mutation": False,
    }
    write_json(manifest_path, manifest)
    return manifest


def complete_alpha_zero_text_smoke(
    config_path: Path,
    output_dir: Path,
    local_files_only: bool,
) -> dict[str, Any]:
    config = load_json(config_path)
    model, tokenizer, _runtime = load_runtime(config, local_files_only=local_files_only)
    direction_metadata = load_json(output_dir / "DIRECTION-METADATA.json")
    vectors = load_vectors(output_dir, direction_metadata["vector_file"]["sha256"])
    layer = config["sweep"]["negative_control"]["layer"]
    prompt = config["prompt"]["held_out"][0]
    condition = {
        "prompt_id": prompt["prompt_id"],
        "direction_kind": "alpha_zero_text_smoke",
        "layer": layer,
        "alpha": 0.0,
    }
    candidate = generate_candidate(
        model,
        tokenizer,
        config,
        prompt,
        condition,
        vectors[layer],
    )
    baseline = next(
        item
        for item in read_jsonl(output_dir / "RAW-RESULTS.jsonl")
        if item["prompt_id"] == prompt["prompt_id"]
        and item["condition"]["direction_kind"] == "baseline"
    )
    token_ids_equal = candidate["generated_token_ids"] == baseline["generated_token_ids"]
    text_equal = candidate["text"] == baseline["text"]
    if not token_ids_equal or not text_equal:
        raise RuntimeError("Full alpha-zero text/token identity failed against the unsteered baseline.")
    smoke_path = output_dir / "SMOKE-RESULTS.json"
    smoke = load_json(smoke_path)
    smoke.update(
        {
            "alpha_zero_full_generation_token_ids_identical": token_ids_equal,
            "alpha_zero_full_generation_text_identical": text_equal,
            "alpha_zero_full_generation_candidate_sha256": candidate["candidate_sha256"],
            "alpha_zero_full_generation_baseline_sha256": baseline["candidate_sha256"],
            "alpha_zero_full_generation_prompt_id": prompt["prompt_id"],
            "alpha_zero_full_generation_tokens": candidate["generated_token_count"],
        }
    )
    write_json(smoke_path, smoke)
    analysis_path = output_dir / "ANALYSIS.json"
    analysis = load_json(analysis_path)
    analysis["smoke"] = smoke
    write_json(analysis_path, analysis)
    verify_outputs(config, output_dir)
    return smoke


def run_all(config_path: Path, output_dir: Path, local_files_only: bool) -> None:
    config = load_json(config_path)
    pairs_doc = load_json(resolve_repo_path(config["data"]["path"]))
    if pairs_doc["experiment_id"] != config["experiment_id"]:
        raise RuntimeError("Contrastive data experiment identity mismatch.")
    model, tokenizer, runtime = load_runtime(config, local_files_only=local_files_only)
    runtime["config_sha256"] = file_sha256(config_path)
    runtime["contrastive_pairs_sha256"] = file_sha256(resolve_repo_path(config["data"]["path"]))
    direction_metadata = derive_vectors(model, tokenizer, config, pairs_doc, output_dir)
    vectors = load_vectors(output_dir, direction_metadata["vector_file"]["sha256"])
    smoke = actual_model_smoke(
        model,
        tokenizer,
        config,
        vectors[config["sweep"]["negative_control"]["layer"]],
    )
    print(f"[smoke] {canonical_json(smoke)}", flush=True)
    candidates = run_sweep(model, tokenizer, config, vectors, output_dir)
    build_outputs(config, runtime, direction_metadata, smoke, candidates, output_dir)
    verification = verify_outputs(config, output_dir)
    print(f"[verify] {canonical_json(verification)}", flush=True)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=Path, default=DEFAULT_CONFIG)
    parser.add_argument("--output-dir", type=Path)
    parser.add_argument("--local-files-only", action="store_true")
    parser.add_argument("--verify-only", action="store_true")
    parser.add_argument("--complete-alpha-zero-text-smoke", action="store_true")
    args = parser.parse_args()
    config_path = args.config.resolve()
    config = load_json(config_path)
    output_dir = (
        args.output_dir.resolve()
        if args.output_dir
        else config_path.parent / "run-20260902-a"
    )
    if args.complete_alpha_zero_text_smoke:
        print(canonical_json(complete_alpha_zero_text_smoke(config_path, output_dir, args.local_files_only)))
        return 0
    if args.verify_only:
        print(canonical_json(verify_outputs(config, output_dir)))
        return 0
    run_all(config_path, output_dir, args.local_files_only)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
