"""Disposable memory/gradient check. Random token IDs never enter the dataset."""
import os
os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")
os.environ.setdefault("HF_HOME", "/workspace/.hf_home")
import json
import pathlib
import time
import traceback
import unsloth
import torch
import bitsandbytes as bnb
from unsloth import FastLanguageModel

ROOT = pathlib.Path("/workspace/reverse-pilot-20260929")
MODEL = "Qwen/Qwen3-30B-A3B-Instruct-2507"
REVISION = "0d7cf23991f47feeb3a57ecb4c9cee8ea4a17bfe"
result = {"model": MODEL, "revision": REVISION, "status": "RUNNING",
          "started_unix": time.time(), "sequence_length": 1024,
          "rank": 64, "probe_data": "seeded random token IDs, discarded"}

def save():
    (ROOT / "gpu-fit.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result), flush=True)

def memory():
    torch.cuda.synchronize()
    return {"allocated_gib": torch.cuda.memory_allocated() / 2**30,
            "reserved_gib": torch.cuda.memory_reserved() / 2**30,
            "peak_gib": torch.cuda.max_memory_allocated() / 2**30}

try:
    transfer = json.loads((ROOT / "repo/docs/reverse-model-20260929/environment/download-manifest-instruct.json").read_text())
    assert transfer["status"] == "COMPLETE" and transfer["revision"] == REVISION
    assert sum(f["filename"].endswith(".safetensors") and f["verified"] for f in transfer["files"]) == 16
    # Earlier interrupted Unsloth downloaders left suspect partials in this one
    # model's cache. Preserve them outside the Hub blobs directory so the loader's
    # unsafe-partial watchdog cannot discard the newly verified complete weights.
    blobs = pathlib.Path(os.environ["HF_HOME"]) / "hub" / ("models--" + MODEL.replace("/", "--")) / "blobs"
    abandoned = ROOT / "abandoned-public-model-parts" / "instruct"
    abandoned.mkdir(parents=True, exist_ok=True)
    retired = []
    for partial in blobs.glob("*.incomplete"):
        assert partial.is_file() and not partial.is_symlink()
        destination = abandoned / partial.name
        assert not destination.exists(), "Abandoned partial already preserved; diagnose collision"
        retired.append({"filename": partial.name, "bytes": partial.stat().st_size})
        partial.rename(destination)
    result["preserved_abandoned_download_parts"] = retired
    torch.manual_seed(3407)
    torch.set_num_threads(8)
    save()
    model, tokenizer = FastLanguageModel.from_pretrained(
        model_name=MODEL, revision=REVISION, use_exact_model_name=True,
        max_seq_length=1024, dtype=torch.bfloat16, load_in_4bit=True,
        device_map="sequential", use_gradient_checkpointing="unsloth",
        trust_remote_code=False)
    result["loaded_memory"] = memory()
    result["loaded_model_class"] = str(type(model))
    result["loaded_device_map"] = {n: str(d) for n, d in getattr(model, "hf_device_map", {}).items()}
    result["quantization_config"] = model.config.to_dict().get("quantization_config")
    result["expert_weight_layout"] = [(n, list(p.shape), str(p.dtype), type(p).__name__)
                                     for n, p in model.named_parameters()
                                     if "layers.0.mlp.experts" in n]
    save()
    model = FastLanguageModel.get_peft_model(
        model, r=64, lora_alpha=64, lora_dropout=0, bias="none",
        target_modules=["q_proj", "k_proj", "v_proj", "o_proj",
                        "gate_proj", "up_proj", "down_proj"],
        use_gradient_checkpointing="unsloth", random_state=3407)
    params = [(n, p) for n, p in model.named_parameters() if p.requires_grad]
    # Both experimental arms use BF16 adapters and computation, with an 8-bit
    # paged optimizer. This choice preserves rank and layer coverage on 40 GB.
    for _, parameter in params:
        parameter.data = parameter.data.to(torch.bfloat16)
    result["adapter_precision"] = "bfloat16"
    result["trainable_count"] = sum(p.numel() for _, p in params)
    result["trainable_dtypes"] = {str(d): sum(p.numel() for _, p in params if p.dtype == d)
                                  for d in set(p.dtype for _, p in params)}
    result["lora_config"] = model.peft_config["default"].to_dict()
    targets = result["lora_config"]["target_modules"]
    if not isinstance(targets, str):
        result["lora_config"]["target_modules"] = sorted(targets)
    result["first_layer_parameters"] = [(n, list(p.shape), str(p.dtype))
                                         for n, p in params if "layers.0." in n]
    result["adapter_parameters_by_layer"] = {
        str(i): {part: [(n, list(p.shape)) for n, p in params
                        if f"layers.{i}." in n and f".{part}." in n]
                 for part in ["self_attn", "mlp"]} for i in range(48)}
    result["attached_memory"] = memory()
    assert all(any(f"layers.{i}." in n and ".mlp." in n for n, _ in params)
               for i in range(48)), "Expert adapters missing from a layer"
    assert all(any(f"layers.{i}." in n and ".self_attn." in n for n, _ in params)
               for i in range(48)), "Attention adapters missing from a layer"
    save()
    FastLanguageModel.for_training(model)
    model.config.use_cache = False
    optimizer = bnb.optim.PagedAdamW8bit([p for _, p in params], lr=2e-4)
    ids = torch.randint(1000, min(140000, model.config.vocab_size), (1, 1024), device="cuda")
    labels = ids.clone()
    labels[:, :512] = -100
    result["steps"] = []
    for step in range(2):
        started = time.perf_counter()
        optimizer.zero_grad(set_to_none=True)
        with torch.autocast("cuda", dtype=torch.bfloat16):
            loss = model(input_ids=ids, attention_mask=torch.ones_like(ids), labels=labels).loss
        assert torch.isfinite(loss).item(), "Non-finite probe loss"
        loss.backward()
        gradient_layers = {}
        for part in ["self_attn", "mlp"]:
            gradient_layers[part] = [i for i in range(48) if any(
                f"layers.{i}." in n and f".{part}." in n and p.grad is not None
                and torch.isfinite(p.grad).all().item() and p.grad.abs().max().item() > 0
                for n, p in params)]
            assert len(gradient_layers[part]) == 48, f"Missing {part} gradients"
        before_step = memory()
        # LoRA A is initially zero-gradient because B starts at zero. After the
        # first update, every attached adapter tensor must receive finite signal;
        # checking one tensor per layer alone could conceal an omitted projection.
        adapter_gradients = []
        if step == 1:
            for name, parameter in params:
                assert parameter.grad is not None, f"Missing adapter gradient: {name}"
                assert torch.isfinite(parameter.grad).all().item(), f"Non-finite gradient: {name}"
                maximum = parameter.grad.abs().max().item()
                assert maximum > 0, f"Zero adapter gradient after first update: {name}"
                adapter_gradients.append({"name": name, "shape": list(parameter.shape),
                                          "max_abs_gradient": maximum})
        optimizer.step()
        result["steps"].append({"step": step, "loss": loss.item(),
                                "seconds": time.perf_counter() - started,
                                "gradient_layers": gradient_layers,
                                "all_adapter_gradients": adapter_gradients,
                                "before_optimizer": before_step,
                                "after_optimizer": memory()})
        save()
    result["status"] = "PASS"
except Exception as exc:
    result["status"] = "FAIL"
    result["error"] = repr(exc)
    result["traceback"] = traceback.format_exc()
    if torch.cuda.is_available():
        result["failure_memory"] = memory()
finally:
    result["ended_unix"] = time.time()
    save()
if result["status"] != "PASS":
    raise SystemExit(1)
