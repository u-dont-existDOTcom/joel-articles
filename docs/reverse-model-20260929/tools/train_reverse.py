"""Comparable two-epoch, target-only LoRA training; private resumable checkpoints."""
import argparse
import hashlib
import importlib.metadata
import json
import math
import os
import random
import time
from pathlib import Path
os.environ.setdefault('HF_HOME', '/workspace/.hf_home')
os.environ.setdefault('TOKENIZERS_PARALLELISM', 'false')
os.environ.setdefault('HF_HUB_DISABLE_XET', '1')
from unsloth import FastLanguageModel
import torch
import bitsandbytes as bnb

MODELS = {
    'base': ('Qwen/Qwen3-30B-A3B-Base', '1b75feb79f60b8dc6c5bc769a898c206a1c6a4f9'),
    'instruct': ('Qwen/Qwen3-30B-A3B-Instruct-2507', '0d7cf23991f47feeb3a57ecb4c9cee8ea4a17bfe')}
INSTRUCTION = 'Rewrite this so it reads like a person wrote it. Keep every fact.'
SEED = 3407
TARGETS = ['q_proj', 'k_proj', 'v_proj', 'o_proj', 'gate_proj', 'up_proj', 'down_proj']

def prefix(text):
    return INSTRUCTION + '\n\n' + text + '\n\nRewritten paragraph:\n'

def append(path, record):
    with path.open('a') as f:
        f.write(json.dumps(record)+'\n'); f.flush(); os.fsync(f.fileno())

def memory():
    torch.cuda.synchronize()
    return {'allocated_gib': torch.cuda.memory_allocated()/2**30,
            'reserved_gib': torch.cuda.memory_reserved()/2**30,
            'peak_gib': torch.cuda.max_memory_allocated()/2**30}

def validate_complete_generation(data_path, originals, rows):
    audit_path = data_path.parent / 'pairs-audit.jsonl'
    audit = [json.loads(line) for line in audit_path.read_text().splitlines()]
    assert len(audit) == len(originals) == 1200, 'Complete all 1,200 counterparts before either training'
    assert len({r['id'] for r in audit}) == 1200 and {r['id'] for r in audit} == set(originals)
    accepted = {r['id']: r for r in audit if r['accepted'] and r['split'] == 'train'}
    assert len(rows) == len(accepted) and {r['id'] for r in rows} == set(accepted)
    assert all(row == accepted[row['id']] for row in rows), 'Train on the exact open-judge-accepted rows'
    return hashlib.sha256(audit_path.read_bytes()).hexdigest()

def run(args):
    assert args.condition in MODELS
    model_id, revision = MODELS[args.condition]
    rows = [json.loads(l) for l in args.data.read_text().splitlines()]
    assert rows and all(r['split'] == 'train' and r['accepted'] for r in rows)
    from generate_pairs import MODEL as GENERATOR, REVISION as GENERATOR_REVISION, SOURCE_SHA256
    assert hashlib.sha256(args.human_source.read_bytes()).hexdigest() == SOURCE_SHA256
    originals = {r['id']:r for r in (json.loads(l) for l in args.human_source.read_text().splitlines())}
    audit_sha256 = validate_complete_generation(args.data, originals, rows)
    for row in rows:
        assert row['open_model'] == GENERATOR and row['open_model_revision'] == GENERATOR_REVISION
        assert row['human'] == originals[row['id']]['human']
        assert row['document_id'] == originals[row['id']]['document_id']
        assert row['ai_sha256'] == hashlib.sha256(row['ai'].encode()).hexdigest()
    assert len({r['document_id'] for r in rows}) == len(rows)
    args.private_output.mkdir(parents=True, exist_ok=True)
    args.evidence.mkdir(parents=True, exist_ok=True)
    started = time.time()
    torch.manual_seed(SEED); random.seed(SEED); torch.set_num_threads(8)
    model, tokenizer = FastLanguageModel.from_pretrained(
        model_name=model_id, revision=revision, use_exact_model_name=True,
        max_seq_length=args.max_length, dtype=torch.bfloat16, load_in_4bit=True,
        device_map='sequential', use_gradient_checkpointing='unsloth', trust_remote_code=False)
    model = FastLanguageModel.get_peft_model(
        model, r=64, lora_alpha=64, lora_dropout=0, bias='none',
        target_modules=TARGETS, use_gradient_checkpointing='unsloth', random_state=SEED)
    model.peft_config['default'].revision = revision
    actual_targets = model.peft_config['default'].target_modules
    actual_targets = actual_targets if isinstance(actual_targets, str) else sorted(actual_targets)
    actual_parameters = getattr(model.peft_config['default'], 'target_parameters', None)
    if actual_parameters is not None and not isinstance(actual_parameters, str):
        actual_parameters = sorted(actual_parameters)
    parameters = [(n,p) for n,p in model.named_parameters() if p.requires_grad]
    for _, parameter in parameters:
        parameter.data = parameter.data.to(torch.bfloat16)
    for part in ['self_attn', 'mlp']:
        assert all(any(f'layers.{i}.' in n and f'.{part}.' in n for n,_ in parameters) for i in range(48))
    encoded = []
    for row in rows:
        prompt_ids = tokenizer.encode(prefix(row['ai']), add_special_tokens=False)
        target_ids = tokenizer.encode(row['human'], add_special_tokens=False) + [tokenizer.eos_token_id]
        ids = prompt_ids + target_ids
        assert len(ids) <= args.max_length, f"No truncation allowed: {row['id']} needs {len(ids)} tokens"
        encoded.append({'id': row['id'], 'input_ids': ids,
                        'labels': [-100]*len(prompt_ids) + target_ids,
                        'target_tokens': len(target_ids)})
    step_count = math.ceil(len(rows)/8)*2
    warmup = max(1, math.ceil(step_count*0.03))
    optimizer = bnb.optim.PagedAdamW8bit([p for _,p in parameters], lr=2e-4, weight_decay=0.01)
    def multiplier(step):
        if step < warmup:
            return (step+1)/warmup
        ratio = min(1, (step-warmup)/max(1,step_count-warmup))
        return 0.5*(1+math.cos(math.pi*ratio))
    scheduler = torch.optim.lr_scheduler.LambdaLR(optimizer, multiplier)
    manifest = {'condition': args.condition, 'model': model_id, 'revision': revision,
                'dataset_sha256': hashlib.sha256(args.data.read_bytes()).hexdigest(),
                'complete_generation_audit_sha256': audit_sha256,
                'examples': len(rows), 'document_ids': [r['document_id'] for r in rows],
                'instruction': INSTRUCTION, 'serialization': 'identical plain prefix and human target in both conditions',
                'prefix_suffix': '\n\nRewritten paragraph:\n', 'loss': 'human target plus EOS only; prompt labels -100',
                'epochs': 2, 'rank': 64, 'alpha': 64, 'dropout': 0, 'bias': 'none',
                'requested_target_modules': TARGETS, 'target_modules': actual_targets,
                'target_parameters': actual_parameters, 'routers': 'frozen', 'precision': 'bfloat16 adapters and computation',
                'optimizer': 'bitsandbytes PagedAdamW8bit', 'learning_rate': 2e-4,
                'weight_decay': 0.01, 'microbatch': 1, 'gradient_accumulation': 8,
                'gradient_clip_norm': 1.0, 'scheduler': 'cosine', 'warmup_steps': warmup,
                'optimizer_steps': step_count, 'seed': SEED, 'max_length': args.max_length,
                'observed_max_length': max(len(r['input_ids']) for r in encoded),
                'trainable_count': sum(p.numel() for _,p in parameters),
                'checkpoint_every_optimizer_steps': 50, 'keep_checkpoints': 2,
                'packages': {p:importlib.metadata.version(p) for p in ['torch','transformers','peft','trl','bitsandbytes','accelerate','unsloth','unsloth_zoo']},
                'started_unix': started, 'memory_after_setup': memory()}
    (args.evidence / 'training-manifest.json').write_text(json.dumps(manifest, indent=2)+'\n')
    FastLanguageModel.for_training(model); model.config.use_cache = False
    global_step, start_epoch, start_index = 0, 0, 0
    if args.resume:
        state = torch.load(args.resume / 'training-state.pt', map_location='cpu', weights_only=False)
        from safetensors.torch import load_file
        from peft import set_peft_model_state_dict
        set_peft_model_state_dict(model, load_file(str(args.resume / 'adapter_model.safetensors')))
        optimizer.load_state_dict(state['optimizer']); scheduler.load_state_dict(state['scheduler'])
        global_step, start_epoch, start_index = state['step'], state['epoch'], state['next_index']
        torch.set_rng_state(state['torch_rng']); torch.cuda.set_rng_state_all(state['cuda_rng'])
        random.setstate(state['random_rng'])
    def checkpoint(epoch, next_index, final=False):
        destination = args.private_output / ('final' if final else f'checkpoint-{global_step:04d}')
        destination.mkdir(parents=True, exist_ok=True)
        model.save_pretrained(destination); tokenizer.save_pretrained(destination)
        torch.save({'optimizer': optimizer.state_dict(), 'scheduler': scheduler.state_dict(),
                    'step': global_step, 'epoch': epoch, 'next_index': next_index,
                    'torch_rng': torch.get_rng_state(), 'cuda_rng': torch.cuda.get_rng_state_all(),
                    'random_rng': random.getstate()}, destination / 'training-state.pt')
        (args.private_output / 'LATEST.json').write_text(json.dumps({'path': str(destination),
            'step': global_step, 'epoch': epoch, 'next_index': next_index, 'final': final})+'\n')
        # Only remove earlier recoverable checkpoints in this run's private directory.
        # Keep two full copies; the final adapter is retained separately.
        old = sorted(args.private_output.glob('checkpoint-*'))
        for directory in old[:-2]:
            import shutil
            shutil.rmtree(directory)
        append(args.evidence / 'training-log.jsonl', {'event': 'checkpoint', 'step':global_step,
                                                     'epoch':epoch, 'next_index':next_index, 'final':final})
    for epoch in range(start_epoch, 2):
        order = list(range(len(encoded))); random.Random(SEED+epoch).shuffle(order)
        begin_index = start_index if epoch == start_epoch else 0
        for index in range(begin_index, len(order), 8):
            group = order[index:index+8]; optimizer.zero_grad(set_to_none=True)
            step_start = time.time(); total_loss = 0
            for item in group:
                row = encoded[item]
                ids = torch.tensor([row['input_ids']], device='cuda')
                labels = torch.tensor([row['labels']], device='cuda')
                with torch.autocast('cuda', dtype=torch.bfloat16):
                    loss = model(input_ids=ids, attention_mask=torch.ones_like(ids), labels=labels).loss
                assert torch.isfinite(loss).item(), f"Non-finite loss: {row['id']}"
                (loss/len(group)).backward(); total_loss += loss.item()
            norm = torch.nn.utils.clip_grad_norm_([p for _,p in parameters], 1.0)
            assert torch.isfinite(norm).item(), 'Non-finite gradients'
            optimizer.step(); scheduler.step(); global_step += 1
            record = {'step':global_step,'epoch':epoch+1,'next_index':index+len(group),
                      'loss':total_loss/len(group),'gradient_norm':norm.item(),
                      'learning_rate':optimizer.param_groups[0]['lr'], 'seconds':time.time()-step_start,
                      'elapsed_seconds':time.time()-started, **memory()}
            append(args.evidence / 'training-log.jsonl', record); print(json.dumps(record), flush=True)
            if global_step%50 == 0:
                checkpoint(epoch, index+len(group))
            if args.deadline_unix and time.time() >= args.deadline_unix:
                checkpoint(epoch, index+len(group)); print('DEADLINE_REACHED', flush=True); return
    assert global_step == step_count
    checkpoint(2, 0, final=True)
    manifest.update(status='COMPLETE', ended_unix=time.time(), elapsed_seconds=time.time()-started,
                    final_memory=memory(), completed_optimizer_steps=global_step)
    (args.evidence / 'training-manifest.json').write_text(json.dumps(manifest, indent=2)+'\n')
    print(json.dumps({'status':'COMPLETE','condition':args.condition,'seconds':time.time()-started}),flush=True)

if __name__ == '__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--condition', choices=list(MODELS), required=True)
    p.add_argument('--data',type=Path,required=True)
    p.add_argument('--human-source',type=Path,required=True)
    p.add_argument('--private-output',type=Path,required=True)
    p.add_argument('--evidence',type=Path,required=True)
    p.add_argument('--max-length',type=int,default=1536)
    p.add_argument('--resume',type=Path)
    p.add_argument('--deadline-unix',type=float,default=0)
    run(p.parse_args())
