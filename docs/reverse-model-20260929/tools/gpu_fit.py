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
    result["lora_config"]["target_modules"] = sorted(result["lora_config"]["target_modules"])
    result["first_layer_parameters"] = [(n, list(p.shape), str(p.dtype))
                                         for n, p in params if "layers.0." in n]
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
        optimizer.step()
        result["steps"].append({"step": step, "loss": loss.item(),
                                "seconds": time.perf_counter() - started,
                                "gradient_layers": gradient_layers,
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
