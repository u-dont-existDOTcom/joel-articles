"""Final bounded whole-passage Chinese round-trip trial; no training writes."""
import argparse
import json
import os
import time
from pathlib import Path

os.environ.setdefault('HF_HOME', '/workspace/.hf_home')
os.environ.setdefault('TOKENIZERS_PARALLELISM', 'false')
os.environ.setdefault('HF_HUB_DISABLE_XET', '1')
from unsloth import FastLanguageModel
import torch

from copy_check import MAX_SHARED_WORDS
from generate_pairs import MODEL, REVISION, SEED, SOURCE_SHA256, append, parse_judge, sha
from regen_v3_trial import OLD_FAILURES, NEW, TRIAL_IDS, TECHNICAL_IDS, JUDGE_V3, trial_rows
from regen_v4_policy import chinese_fraction, roundtrip_guard
from request_cache import RequestCache, complete_lines

TRANSLATE_PROMPT = ("Translate this passage into Simplified Chinese. Translate everything, including "
    "hedges, qualifications, tone and who is speaking. Keep names, titles, technical terms, "
    "numbers, units, links and direct quotations in English exactly as written, with quotations "
    "in quotation marks. Output only the translation.\n\nPASSAGE:\n")
REQUESTS = ["Here's a draft I wrote. Turn it into polished English.",
            "Write this up in English for my blog.",
            "Rewrite this in clear, natural English.",
            "Improve this and put it in English.",
            "Make this read well in English."]
DRAFT_SUFFIX = ("Keep the form, the perspective and every point, including hedges, "
    "qualifications and who said what. Keep the English names, terms and quotations exactly "
    "as they are. Add nothing. Output only the English text.\n\n")
GENRE_MINIMUM = {'essays_journal': 9, 'technical': 5, 'practical': 4, 'letters': 2}


def trial_admission(chinese, slots):
    for path in (chinese, slots):
        assert path and path.is_file(), 'Version 4 requires both completed version 3 trial summaries'
    a, b = json.loads(chinese.read_text()), json.loads(slots.read_text())
    assert a['status'] == b['status'] == 'COMPLETE'
    assert a['processed'] == b['processed'] == 40
    assert not a['thresholds_met'] and not b['thresholds_met']
    return a, b


def run(args):
    trial_admission(args.chinese_summary, args.slots_summary)
    assert args.batch_size <= 32 and args.max_seconds <= 3600
    args.output.mkdir(parents=True, exist_ok=True)
    assert sha(args.input.read_text()) == SOURCE_SHA256
    source = [json.loads(line) for line in args.input.read_text().splitlines()]
    old = [json.loads(line) for line in args.old_audit.read_text().splitlines()]
    rows = trial_rows(source, old)
    requests = args.output / 'model-requests.jsonl'
    results = args.output / 'trial-results.jsonl'
    cache = RequestCache(requests, args.output / 'request-reservations.jsonl')
    prior = {row['id']: row for row in complete_lines(results)}
    assert len(prior) == len(complete_lines(results))
    started = time.time()
    manifest = {'method': 'roundtrip_regeneration', 'pipeline_revision': 4, 'ids': TRIAL_IDS,
                'technical_ids': TECHNICAL_IDS, 'old_failures': OLD_FAILURES, 'new_ids': NEW,
                'source_sha256': SOURCE_SHA256, 'model': MODEL, 'model_revision': REVISION,
                'seed': SEED, 'maximum_shared_words': MAX_SHARED_WORDS,
                'translation_prompt': TRANSLATE_PROMPT, 'draft_suffix': DRAFT_SUFFIX,
                'requests': REQUESTS, 'judge': JUDGE_V3, 'genre_minimum': GENRE_MINIMUM,
                'max_gpu_seconds': args.max_seconds, 'batch_size': args.batch_size,
                'fresh_context': 'Each call has one user message; English draft sees only Chinese translation.'}
    (args.output / 'trial-manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
    torch.manual_seed(SEED)
    model, tokenizer = FastLanguageModel.from_pretrained(
        model_name=MODEL, revision=REVISION, use_exact_model_name=True,
        max_seq_length=4096, dtype=torch.bfloat16, load_in_4bit=True,
        device_map='sequential', trust_remote_code=False)
    FastLanguageModel.for_inference(model)
    tokenizer.padding_side = 'left'
    if tokenizer.pad_token_id is None:
        tokenizer.pad_token = tokenizer.eos_token
    request_number = max((row['request'] for row in complete_lines(requests)), default=0)

    def generate(ids, phase, prompts, max_new, sample):
        nonlocal request_number
        answers = [cache.lookup(identifier, phase, prompt) for identifier, prompt in zip(ids, prompts)]
        missing = [i for i, answer in enumerate(answers) if answer is None]
        if not missing:
            return answers
        selected_ids = [ids[i] for i in missing]
        selected_prompts = [prompts[i] for i in missing]
        rendered = [tokenizer.apply_chat_template([{'role': 'user', 'content': prompt}],
                    tokenize=False, add_generation_prompt=True, enable_thinking=False)
                    for prompt in selected_prompts]
        encoded = tokenizer(rendered, return_tensors='pt', padding=True, truncation=False).to('cuda')
        width = encoded.input_ids.shape[1]
        if width + max_new > 4096:
            raise RuntimeError(f'Context overflow {phase}: {width}+{max_new}')
        for identifier, prompt in zip(selected_ids, selected_prompts):
            cache.reserve(identifier, phase, prompt)
        begin = time.time()
        kwargs = {'do_sample': sample, 'max_new_tokens': max_new, 'use_cache': True,
                  'pad_token_id': tokenizer.pad_token_id}
        if sample:
            kwargs.update(temperature=0.7, top_p=0.9)
        with torch.inference_mode():
            output = model.generate(**encoded, **kwargs)
        torch.cuda.synchronize()
        elapsed = time.time() - begin
        fresh = []
        for identifier, prompt, tokens in zip(selected_ids, selected_prompts, output[:, width:]):
            token_list = tokens.tolist()
            eos = tokenizer.eos_token_id
            finish = token_list.index(eos) if eos in token_list else len(token_list)
            value = tokenizer.decode(token_list[:finish], skip_special_tokens=True).strip()
            request_number += 1
            answer = {'text': value, 'truncated': finish == len(token_list) and finish >= max_new,
                      'request': request_number}
            append(requests, {'request': request_number, 'id': identifier, 'phase': phase,
                   'messages': [{'role': 'user', 'content': prompt}], 'response': value,
                   'truncated': answer['truncated'], 'response_tokens': finish,
                   'batch_seconds': elapsed, 'batch_count': len(selected_ids),
                   'batch_size': args.batch_size,
                   'allocated_seconds': elapsed/len(selected_ids), 'max_new_tokens': max_new,
                   'do_sample': sample})
            cache.remember(identifier, phase, prompt, answer)
            fresh.append(answer)
        for i, answer in zip(missing, fresh):
            answers[i] = answer
        print(json.dumps({'phase': phase, 'ids': selected_ids, 'seconds': elapsed,
                          'gpu_peak_gib': torch.cuda.max_memory_allocated()/2**30}), flush=True)
        return answers

    def attempt(batch, number):
        ids = [row['id'] for row in batch]
        translations = generate(ids, f'v4_translation_{number}',
                [TRANSLATE_PROMPT + row['human'] for row in batch], 1024, True)
        checks = [chinese_fraction(row['human'], answer['text'])
                  for row, answer in zip(batch, translations)]
        draft_indexes = [i for i, answer in enumerate(translations)
                         if not answer['truncated'] and checks[i]['passed']]
        drafts = {}
        if draft_indexes:
            prompts = [REQUESTS[(int(ids[i][1:])-1) % len(REQUESTS)] + '\n' + DRAFT_SUFFIX +
                       translations[i]['text'] for i in draft_indexes]
            drafts = dict(zip(draft_indexes, generate([ids[i] for i in draft_indexes],
                    f'v4_draft_{number}', prompts, 1024, True)))
        guards = {i: roundtrip_guard(batch[i]['human'], translations[i]['text'],
                                    drafts[i]['text']) for i in drafts}
        judge_indexes = [i for i in draft_indexes if not drafts[i]['truncated'] and
                         drafts[i]['text'] and guards[i]['passed']]
        judges = {}
        for direction in ('human_claims_in_ai', 'ai_claims_in_human'):
            if judge_indexes:
                prompts = [JUDGE_V3.format(
                           source=batch[i]['human'] if direction == 'human_claims_in_ai' else drafts[i]['text'],
                           candidate=drafts[i]['text'] if direction == 'human_claims_in_ai' else batch[i]['human'])
                           for i in judge_indexes]
                judges[direction] = dict(zip(judge_indexes, generate([ids[i] for i in judge_indexes],
                    f'v4_{direction}_{number}', prompts, 768, False)))
        outputs = []
        for i, row in enumerate(batch):
            issues = []
            if translations[i]['truncated']:
                issues.append('translation_truncated')
            if not checks[i]['passed']:
                issues.append('translation_not_90_percent_chinese')
            if i not in drafts:
                issues.append('no_draft')
            elif drafts[i]['truncated']:
                issues.append('draft_truncated')
            elif not guards[i]['passed']:
                issues.append('copy_or_list_guard_failed')
            judgments = {}
            for direction in ('human_claims_in_ai', 'ai_claims_in_human'):
                if i in judges.get(direction, {}):
                    answer = judges[direction][i]
                    judgment = parse_judge(answer['text'])
                    judgments[direction] = judgment
                    if answer['truncated'] or not judgment['all_supported']:
                        issues.append(direction)
            outputs.append({'id': row['id'], 'method': 'roundtrip_regeneration',
                            'attempt': number, 'translation': translations[i],
                            'language_check': checks[i], 'draft': drafts.get(i),
                            'copy_guard': guards.get(i), 'judgments': judgments,
                            'accepted': not issues, 'rejection_reasons': issues})
        return outputs

    todo = [row for row in rows if row['id'] not in prior]
    stopped_early = False
    for offset in range(0, len(todo), args.batch_size):
        if time.time()-started > args.max_seconds-180:
            break
        batch = todo[offset:offset+args.batch_size]
        first = attempt(batch, 1)
        failed = [row for row, result in zip(batch, first) if not result['accepted']]
        second = {result['id']: result for result in attempt(failed, 2)} if failed and time.time()-started < args.max_seconds-180 else {}
        if failed and len(second) != len(failed):
            print('INCOMPLETE_RETRY_DEADLINE', flush=True)
            break
        for row, result in zip(batch, first):
            final = dict(second.get(row['id'], result))
            final['first_attempt'] = result
            final['pipeline_revision'] = 4
            final['source_split'] = row['split']
            final['source_genre'] = row['genre']
            append(results, final)
            prior[row['id']] = final
        print(json.dumps({'completed': len(prior),
            'accepted': sum(x['accepted'] for x in prior.values()),
            'elapsed_seconds': time.time()-started}), flush=True)
        remaining = set(TRIAL_IDS)-set(prior)
        if (sum(x['accepted'] for x in prior.values()) + len(remaining) < 28 or
            any(sum(x['accepted'] for x in prior.values() if x['source_genre']==genre) +
                sum(row['genre']==genre for row in rows if row['id'] in remaining) < minimum
                for genre, minimum in GENRE_MINIMUM.items())):
            stopped_early = True
            print('EARLY_STOP_THRESHOLD_IMPOSSIBLE', flush=True)
            break
    counts = {genre: {'processed': sum(x['source_genre']==genre for x in prior.values()),
                      'accepted': sum(x['source_genre']==genre and x['accepted'] for x in prior.values())}
              for genre in GENRE_MINIMUM}
    accepted = sum(x['accepted'] for x in prior.values())
    summary = {'status': 'COMPLETE' if len(prior)==40 else
               'EARLY_STOP_THRESHOLD_IMPOSSIBLE' if stopped_early else 'INCOMPLETE_DEADLINE',
               'processed': len(prior), 'accepted': accepted, 'by_genre': counts,
               'thresholds_met': len(prior)==40 and accepted>=28 and
                    all(counts[g]['accepted']>=n for g,n in GENRE_MINIMUM.items()),
               'elapsed_seconds': time.time()-started, 'raw_requests': request_number}
    (args.output/'trial-summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(summary), flush=True)


if __name__ == '__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--input', type=Path, required=True)
    p.add_argument('--old-audit', type=Path, required=True)
    p.add_argument('--chinese-summary', type=Path, required=True)
    p.add_argument('--slots-summary', type=Path, required=True)
    p.add_argument('--output', type=Path, required=True)
    p.add_argument('--batch-size', type=int, default=32)
    p.add_argument('--max-seconds', type=int, default=3400)
    run(p.parse_args())
