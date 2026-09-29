"""Post-training, fresh open-Qwen judgments; invalid judgments stay unscored."""
import argparse
import hashlib
import json
import os
import time
from pathlib import Path
os.environ.setdefault('HF_HOME', '/workspace/.hf_home')
os.environ.setdefault('HF_HUB_DISABLE_XET', '1')
os.environ.setdefault('TOKENIZERS_PARALLELISM', 'false')
from unsloth import FastLanguageModel
import torch
from generate_pairs import MODEL, REVISION, JUDGE, append, parse_judge

def sha(text):
    return hashlib.sha256(text.encode()).hexdigest()

def main(args):
    # This evaluation cannot run before both experimental trainings finish.
    training = [json.loads(p.read_text()) for p in args.training_manifests]
    assert {m['condition'] for m in training} == {'base', 'instruct'}
    assert all(m['status'] == 'COMPLETE' and m['epochs'] == 2 and m['rank'] == 64 for m in training)
    assert len({m['dataset_sha256'] for m in training}) == 1
    cases = [json.loads(l) for l in args.cases.read_text().splitlines()]
    tasks = []
    args.output.mkdir(parents=True, exist_ok=True)
    path = args.output / 'meaning-judgments.jsonl'
    existing = [json.loads(l) for l in path.read_text().splitlines()] if path.exists() else []
    done = {(r['id'], r['system'], r['direction']): r for r in existing}
    for case in cases:
        original = case.get('input', case.get('ai'))
        assert isinstance(original, str) and original
        for system, result in case['outputs'].items():
            assert system in {'base', 'instruct', 'emulate'}
            output = result['text']
            for direction, source, candidate in [('input_claims_in_output', original, output),
                                                 ('output_claims_in_input', output, original)]:
                identity = (case['id'], system, direction)
                if identity in done:
                    assert done[identity]['source_sha256'] == sha(source)
                    assert done[identity]['candidate_sha256'] == sha(candidate)
                    continue
                tasks.append({'id': case['id'], 'system': system, 'direction': direction,
                              'source': source, 'candidate': candidate})
    if not tasks:
        print('All exact judgments already recorded'); return
    model, tokenizer = FastLanguageModel.from_pretrained(
        model_name=MODEL, revision=REVISION, use_exact_model_name=True,
        max_seq_length=8192, dtype=torch.bfloat16, load_in_4bit=True,
        device_map='sequential', trust_remote_code=False)
    assert not hasattr(model, 'peft_config'), 'Judge must be the original open model, without reverse adapters'
    FastLanguageModel.for_inference(model); model.eval(); tokenizer.padding_side = 'left'
    if tokenizer.pad_token_id is None:
        tokenizer.pad_token = tokenizer.eos_token
    for offset in range(0, len(tasks), args.batch_size):
        if args.deadline_unix and time.time() >= args.deadline_unix:
            print('DEADLINE_REACHED: recorded judgments retained'); break
        batch = tasks[offset:offset + args.batch_size]
        prompts = [JUDGE.format(source=t['source'], candidate=t['candidate']) for t in batch]
        messages = [[{'role': 'user', 'content': p}] for p in prompts]
        rendered = [tokenizer.apply_chat_template(m, tokenize=False, add_generation_prompt=True,
                                                  enable_thinking=False) for m in messages]
        encoded = tokenizer(rendered, return_tensors='pt', padding=True, truncation=False).to('cuda')
        width = encoded.input_ids.shape[1]
        assert width + 2048 <= 8192
        torch.cuda.synchronize(); started = time.perf_counter()
        with torch.inference_mode():
            output = model.generate(**encoded, do_sample=False, max_new_tokens=2048,
                                    use_cache=True, pad_token_id=tokenizer.pad_token_id)
        torch.cuda.synchronize(); elapsed = time.perf_counter() - started
        for task, prompt, tokens in zip(batch, prompts, output[:, width:]):
            ids = tokens.tolist(); ended = tokenizer.eos_token_id in ids
            if ended: ids = ids[:ids.index(tokenizer.eos_token_id)]
            raw = tokenizer.decode(ids, skip_special_tokens=True).strip()
            judgment = parse_judge(raw)
            valid = ended and 'source_claim_count' in judgment
            issues = judgment.get('issues', [])
            valid = valid and all(isinstance(i, dict) and i.get('type') in {'dropped', 'changed', 'invented'}
                                  and all(k in i for k in ['source_claim', 'candidate_evidence', 'reason'])
                                  for i in issues)
            append(path, {'id': task['id'], 'system': task['system'], 'direction': task['direction'],
                          'source_sha256': sha(task['source']), 'candidate_sha256': sha(task['candidate']),
                          'model': MODEL, 'revision': REVISION, 'adapter': None,
                          'messages': [{'role': 'user', 'content': prompt}], 'raw_response': raw,
                          'judgment': judgment, 'valid': bool(valid), 'truncated': not ended,
                          'seconds_allocated': elapsed / len(batch), 'batch_seconds': elapsed,
                          'interpretation': ('Forward dropped/changed points; reverse unsupported output '
                                             'claims are additions or inventions. Keep directions separate; '
                                             'do not sum both changed counts as distinct facts.')})
        print(json.dumps({'completed_new_judgments': offset + len(batch), 'new_judgments': len(tasks),
                          'batch_seconds': elapsed}), flush=True)

if __name__ == '__main__':
    p = argparse.ArgumentParser(); p.add_argument('--cases', type=Path, required=True)
    p.add_argument('--training-manifests', type=Path, nargs=2, required=True)
    p.add_argument('--output', type=Path, required=True)
    p.add_argument('--batch-size', type=int, default=4); p.add_argument('--deadline-unix', type=float, default=0)
    main(p.parse_args())
