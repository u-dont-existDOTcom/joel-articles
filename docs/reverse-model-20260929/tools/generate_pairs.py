"""Resumable Qwen-only counterparts and two fresh, directional judgments."""
import argparse
import hashlib
import json
import os
import random
import time
from pathlib import Path
os.environ.setdefault('HF_HOME', '/workspace/.hf_home')
os.environ.setdefault('TOKENIZERS_PARALLELISM', 'false')
from unsloth import FastLanguageModel
import torch

MODEL = 'Qwen/Qwen3-30B-A3B-Instruct-2507'
REVISION = '0d7cf23991f47feeb3a57ecb4c9cee8ea4a17bfe'
SEED = 3407
PARAPHRASE = 'Rewrite this paragraph to be clearer and more polished.'
NOTES = ('Extract a complete numbered list of the content of the passage below. '
         'Include every fact, example, number, name, qualification, negation, cause, '
         'comparison, opinion and relationship. Preserve uncertainty and who said what. '
         'Do not summarize away details or add facts. Output only the notes.\n\nPASSAGE:\n')
REGEN = ['Write this up as a blog paragraph.', 'Turn these notes into a section.',
         'Improve this into a clear paragraph.', 'Draft a paragraph from these notes.',
         'Write a short explanatory paragraph using these points.']
REGEN_SUFFIX = (' Preserve every point, including names, numbers, qualifications, '
                'negations and relationships. Add no facts. Output only the prose.\n\nNOTES:\n')
JUDGE = ('Check whether every claim in SOURCE is supported by CANDIDATE. '
         'Treat each fact, example, number, name, qualification, negation, opinion, '
         'causal direction, comparison and relationship as a claim. '
         'Only stylistic changes are acceptable. Do not reward plausible new information. '
         'Return only a JSON object with keys all_supported (boolean), '
         'source_claim_count (integer), and issues (array). Each issue must have '
         'type (dropped, changed, or invented), source_claim, candidate_evidence, and reason. '
         'all_supported may be true only if issues is empty and every source claim is preserved.\n\nSOURCE:\n{source}\n\nCANDIDATE:\n{candidate}')

def sha(text):
    return hashlib.sha256(text.encode()).hexdigest()

def append(path, value):
    with path.open('a') as handle:
        handle.write(json.dumps(value, ensure_ascii=False) + '\n')
        handle.flush()
        os.fsync(handle.fileno())

def parse_judge(text):
    try:
        raw = text.strip()
        if raw.startswith('```'):
            raw = raw.split('\n', 1)[1].rsplit('```', 1)[0]
        result = json.loads(raw)
        assert isinstance(result['all_supported'], bool)
        assert type(result['source_claim_count']) is int and result['source_claim_count'] > 0
        assert isinstance(result['issues'], list)
        assert not result['all_supported'] or not result['issues']
        return result
    except (ValueError, KeyError, TypeError, AssertionError):
        return {'all_supported': False, 'issues': [{'type': 'invalid_judge_response', 'raw': text}]}

def run(args):
    args.output.mkdir(parents=True, exist_ok=True)
    pairs_path = args.output / 'pairs-audit.jsonl'
    request_path = args.output / 'model-requests.jsonl'
    source = [json.loads(line) for line in args.input.read_text().splitlines()]
    done = {json.loads(line)['id'] for line in pairs_path.read_text().splitlines()} if pairs_path.exists() else set()
    todo = [row for row in source if row['id'] not in done]
    if args.limit:
        todo = todo[:args.limit]
    random.seed(SEED)
    torch.manual_seed(SEED)
    model, tokenizer = FastLanguageModel.from_pretrained(
        model_name=MODEL, revision=REVISION, use_exact_model_name=True,
        max_seq_length=4096, dtype=torch.bfloat16, load_in_4bit=True,
        device_map='sequential', trust_remote_code=False)
    FastLanguageModel.for_inference(model)
    tokenizer.padding_side = 'left'
    if tokenizer.pad_token_id is None:
        tokenizer.pad_token = tokenizer.eos_token
    started = time.time()
    request_number = sum(1 for _ in request_path.open()) if request_path.exists() else 0
    manifest = {'model': MODEL, 'revision': REVISION, 'seed': SEED,
                'input_sha256': sha(args.input.read_text()), 'batch_size': args.batch_size,
                'generation_temperature': 0.7, 'judge_temperature': 0,
                'max_context': 4096, 'thinking': 'non-thinking checkpoint',
                'prompts': {'paraphrase': PARAPHRASE, 'notes': NOTES, 'regeneration': REGEN,
                            'regeneration_suffix': REGEN_SUFFIX, 'judge': JUDGE},
                'fresh_context': 'Every call has exactly one user message; regeneration has notes only.'}
    (args.output / 'generation-manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')

    def generate(ids, phase, prompts, max_new, sample):
        nonlocal request_number
        messages = [[{'role': 'user', 'content': prompt}] for prompt in prompts]
        rendered = [tokenizer.apply_chat_template(m, tokenize=False, add_generation_prompt=True,
                                                  enable_thinking=False) for m in messages]
        encoded = tokenizer(rendered, return_tensors='pt', padding=True, truncation=False).to('cuda')
        width = encoded.input_ids.shape[1]
        if width + max_new > 4096:
            raise RuntimeError(f'Context overflow in {phase}: {width}+{max_new}')
        begin = time.time()
        with torch.inference_mode():
            kwargs = {'do_sample': sample, 'max_new_tokens': max_new, 'use_cache': True,
                      'pad_token_id': tokenizer.pad_token_id}
            if sample:
                kwargs.update(temperature=0.7, top_p=0.9)
            output = model.generate(**encoded, **kwargs)
        torch.cuda.synchronize()
        seconds = time.time() - begin
        answers = []
        for identifier, prompt, tokens in zip(ids, prompts, output[:, width:]):
            token_list = tokens.tolist()
            eos = tokenizer.eos_token_id
            finish = token_list.index(eos) if eos in token_list else len(token_list)
            text = tokenizer.decode(token_list[:finish], skip_special_tokens=True).strip()
            truncated = finish == len(token_list) and finish >= max_new
            request_number += 1
            append(request_path, {'request': request_number, 'id': identifier, 'phase': phase,
                                  'messages': [{'role': 'user', 'content': prompt}],
                                  'response': text, 'response_tokens': finish, 'truncated': truncated,
                                  'batch_seconds': seconds, 'batch_count': len(ids),
                                  'allocated_seconds': seconds / len(ids), 'max_new_tokens': max_new,
                                  'do_sample': sample})
            answers.append({'text': text, 'truncated': truncated, 'request': request_number})
        print(json.dumps({'phase': phase, 'ids': ids, 'seconds': seconds,
                          'output_tokens': sum(len(t) for t in output[:, width:]),
                          'gpu_peak_gib': torch.cuda.max_memory_allocated()/2**30}), flush=True)
        return answers

    for offset in range(0, len(todo), args.batch_size):
        if args.deadline_unix and time.time() >= args.deadline_unix:
            print('DEADLINE_REACHED: saved completed pairs; resume without changing data', flush=True)
            break
        batch = todo[offset:offset+args.batch_size]
        ids = [r['id'] for r in batch]
        phase1 = [PARAPHRASE + '\n\n' + r['human'] if r['method'] == 'paraphrase'
                  else NOTES + r['human'] for r in batch]
        first = generate(ids, 'paraphrase_or_notes', phase1, 1024, True)
        drafts = list(first)
        regenerated = [i for i, r in enumerate(batch) if r['method'] == 'notes_regeneration']
        if regenerated:
            prompts = [REGEN[(int(batch[i]['id'][1:])-1) % len(REGEN)] + REGEN_SUFFIX + first[i]['text']
                       for i in regenerated]
            fresh = generate([ids[i] for i in regenerated], 'fresh_notes_regeneration', prompts, 512, True)
            for i, result in zip(regenerated, fresh):
                drafts[i] = result
        forward = generate(ids, 'human_claims_in_ai',
                           [JUDGE.format(source=r['human'], candidate=d['text']) for r, d in zip(batch, drafts)],
                           768, False)
        backward = generate(ids, 'ai_claims_in_human',
                            [JUDGE.format(source=d['text'], candidate=r['human']) for r, d in zip(batch, drafts)],
                            768, False)
        for row, first_result, draft, f, b in zip(batch, first, drafts, forward, backward):
            judgments = {'human_claims_in_ai': parse_judge(f['text']),
                         'ai_claims_in_human': parse_judge(b['text'])}
            reasons = []
            if any(v['truncated'] for v in [first_result, draft, f, b]):
                reasons.append('truncated_model_response')
            if not draft['text']:
                reasons.append('empty_draft')
            for direction, judgment in judgments.items():
                if not judgment['all_supported']:
                    reasons.append(direction)
            append(pairs_path, {**row, 'ai': draft['text'], 'ai_sha256': sha(draft['text']),
                                'notes': first_result['text'] if row['method'] == 'notes_regeneration' else None,
                                'judgments': judgments, 'accepted': not reasons,
                                'rejection_reasons': reasons, 'open_model': MODEL,
                                'open_model_revision': REVISION})
        print(json.dumps({'completed_this_run': min(offset+len(batch), len(todo)),
                          'run_total': len(todo), 'elapsed_seconds': time.time()-started}), flush=True)
    records = [json.loads(line) for line in pairs_path.read_text().splitlines()] if pairs_path.exists() else []
    for split in ['train', 'dev', 'test']:
        accepted = [r for r in records if r['split'] == split and r['accepted']]
        (args.output / f'{split}-pairs.jsonl').write_text(''.join(json.dumps(r, ensure_ascii=False)+'\n' for r in accepted))
    summary = {'processed': len(records), 'accepted': sum(r['accepted'] for r in records),
               'split_accepted': {s: sum(r['accepted'] and r['split'] == s for r in records) for s in ['train','dev','test']},
               'elapsed_seconds_this_run': time.time()-started, 'requests': request_number}
    (args.output / 'generation-status.json').write_text(json.dumps(summary, indent=2)+'\n')
    print(json.dumps(summary), flush=True)

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--input', type=Path, required=True)
    p.add_argument('--output', type=Path, required=True)
    p.add_argument('--batch-size', type=int, default=4)
    p.add_argument('--limit', type=int, default=0)
    p.add_argument('--deadline-unix', type=float, default=0)
    run(p.parse_args())
