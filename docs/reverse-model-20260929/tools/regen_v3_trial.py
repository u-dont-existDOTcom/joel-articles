"""Bounded, resumable 40-passage structural regeneration trial; no training writes."""
import argparse
import hashlib
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
from generate_pairs import JUDGE, MODEL, REVISION, SEED, SOURCE_SHA256, append, parse_judge, sha
from regen_v3_policy import copy_guard, parse_chinese_notes, parse_slots_notes, POLICY
from request_cache import RequestCache, complete_lines


OLD_FAILURES = ('H0002 H0003 H0008 H0009 H0014 H0015 H0020 H0021 H0023 H0026 '
                'H0027 H0029 H0030 H0032 H0033 H0035 H0036 H0038 H0041 H0042 '
                'H0044 H0045 H0047 H0048 H0050 H0051 H0053 H0054 H0059 H0060').split()
NEW = 'H0063 H0065 H0066 H0068 H0069 H0071 H0072 H0074'.split()
TRIAL_IDS = sorted(OLD_FAILURES + ['H0012', 'H0062'] + NEW)
assert len(TRIAL_IDS) == len(set(TRIAL_IDS)) == 40
TECHNICAL_IDS = 'H0002 H0009 H0020 H0021 H0030 H0033 H0035 H0053 H0068 H0071'.split()
REQUESTS = ['Turn these notes into polished prose.', 'Write this up properly.',
            'Draft this from my notes.', 'Improve this into clear writing.',
            'Write a short piece using these points.']
NOTES_PROMPT = '''Read the licensed English passage and extract complete content without carrying its English prose into the notes.
Output exactly these three sections:
FORM: one English line stating the document form and speaker perspective.
KEEP:
- one exact source string per line for every person, place, organization, product, work title, technical term, number with units, date, or fixed form line that must survive exactly. Copy those strings only from the passage.
NOTES:
1. A complete numbered content list in Simplified Chinese. Include every fact, example, qualification, hedge, negation, cause, comparison, opinion, relationship, and who said what. Keep each KEEP string and direct quotation in English exactly as in the source, with direct quotations in quotation marks. Otherwise write Chinese, not English sentences copied from the passage. Do not invent information.

PASSAGE:
'''
SLOTS_PROMPT = '''Extract every fact and relationship from the licensed English passage into short atomic slots. Output only one JSON object with FORM (a string giving document form and speaker perspective), KEEP (an array of exact source strings that must survive: names, titles, technical terms, numbers with units, dates, direct quotes, and fixed form lines), and FACTS (a complete array of objects). Each FACTS object has subject, relation, object, qualifier (strings of at most five words each) and negated (boolean). Split complex facts into several slots. Include every example, hedge, qualification, cause, comparison, opinion, and who said what. Preserve uncertainty, perspective, and negation. Do not copy sentences or invent facts. Put long direct quotes in KEEP and refer to them briefly in the slots.

PASSAGE:
'''
DRAFT_SUFFIX = '''Write in English. Keep the form and perspective on the FORM line. Write flowing prose, not a list and not one sentence per note. Preserve every point, including names, numbers, qualifications, negations and relationships. Use the English names, terms and quotations exactly as they appear in the notes. Add no facts. Output only the prose.

'''
JUDGE_V3 = JUDGE.replace('Only stylistic changes are acceptable.',
    'Only stylistic changes are acceptable. Treat a change of speaker, perspective or form, such as first person turned into third person, as unsupported.')


def trial_rows(source, old_audit):
    by_id = {row['id']: row for row in source}
    audit = {row['id']: row for row in old_audit}
    assert len(by_id) == 1200 and len(audit) >= 62
    assert set(OLD_FAILURES) == {identifier for identifier, row in audit.items()
                                  if row['method'] == 'notes_regeneration' and
                                  'copy_guard_failed_after_single_fresh_retry' in row.get('rejection_reasons', [])}
    assert all(by_id[identifier]['split'] == 'train' and
               by_id[identifier]['method'] == 'notes_regeneration' for identifier in TRIAL_IDS)
    assert all(identifier not in audit for identifier in NEW)
    assert len(TECHNICAL_IDS) == 10 and set(TECHNICAL_IDS) <= set(TRIAL_IDS)
    assert all(by_id[identifier]['genre'] == 'technical' for identifier in TECHNICAL_IDS)
    return [by_id[identifier] for identifier in TRIAL_IDS]


def run(args):
    args.output.mkdir(parents=True, exist_ok=True)
    assert sha(args.input.read_text()) == SOURCE_SHA256
    source = [json.loads(line) for line in args.input.read_text().splitlines()]
    old = [json.loads(line) for line in args.old_audit.read_text().splitlines()]
    rows = trial_rows(source, old)
    if args.method == 'slots':
        assert args.primary_summary and args.primary_summary.is_file(), 'Fallback needs completed primary evidence'
        primary = json.loads(args.primary_summary.read_text())
        assert primary['status'] in {'COMPLETE', 'EARLY_STOP_THRESHOLD_IMPOSSIBLE'} and not primary['thresholds_met'], 'Fallback only after a measured primary miss'
    else:
        assert args.method == 'chinese'
    requests = args.output / 'model-requests.jsonl'
    results = args.output / 'trial-results.jsonl'
    cache = RequestCache(requests, args.output / 'request-reservations.jsonl')
    prior = {row['id']: row for row in complete_lines(results)}
    assert len(prior) == len(complete_lines(results))
    started = time.time()
    manifest = {'method': args.method, 'pipeline_revision': 3, 'ids': TRIAL_IDS,
                'technical_ids': TECHNICAL_IDS, 'old_failures': OLD_FAILURES,
                'new_ids': NEW, 'source_sha256': SOURCE_SHA256, 'model': MODEL,
                'model_revision': REVISION, 'seed': SEED, 'copy_policy': POLICY,
                'maximum_shared_words': MAX_SHARED_WORDS,
                'prompt_notes': NOTES_PROMPT if args.method == 'chinese' else SLOTS_PROMPT,
                'prompt_draft_suffix': DRAFT_SUFFIX, 'requests': REQUESTS,
                'judge': JUDGE_V3, 'max_gpu_seconds': args.max_seconds,
                'global_deadline_unix': args.global_deadline_unix,
                'fresh_context': 'Every call contains one user message; draft contains FORM and NOTES only.'}
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
        note_prompt = NOTES_PROMPT if args.method == 'chinese' else SLOTS_PROMPT
        notes = generate(ids, f'v3_{args.method}_notes_{number}',
                         [note_prompt + row['human'] for row in batch], 1024, True)
        parser = parse_chinese_notes if args.method == 'chinese' else parse_slots_notes
        parsed = [parser(answer['text']) for answer in notes]
        draft_indexes = [i for i, (value, issue) in enumerate(parsed) if value and not notes[i]['truncated']]
        drafts = {}
        if draft_indexes:
            prompts = []
            for i in draft_indexes:
                content = 'FORM: '+parsed[i][0]['form']+'\n'
                if args.method == 'slots':
                    content += 'KEEP:\n' + '\n'.join('- '+item for item in parsed[i][0]['keep']) + '\nSLOTS:\n'
                else:
                    content += 'NOTES:\n'
                content += parsed[i][0]['notes']
                prompts.append(REQUESTS[(int(ids[i][1:])-1) % len(REQUESTS)]+'\n'+DRAFT_SUFFIX+content)
            drafts = dict(zip(draft_indexes, generate([ids[i] for i in draft_indexes],
                         f'v3_{args.method}_draft_{number}', prompts, 512, True)))
        guards = {i: copy_guard(batch[i]['human'], parsed[i][0]['notes'], drafts[i]['text'],
                               parsed[i][0]['keep']) for i in drafts}
        judge_indexes = [i for i in draft_indexes if not drafts[i]['truncated'] and
                         drafts[i]['text'] and guards[i]['passed']]
        judges = {}
        for direction in ('human_claims_in_ai', 'ai_claims_in_human'):
            if judge_indexes:
                prompts = [JUDGE_V3.format(source=batch[i]['human'] if direction == 'human_claims_in_ai' else drafts[i]['text'],
                           candidate=drafts[i]['text'] if direction == 'human_claims_in_ai' else batch[i]['human'])
                           for i in judge_indexes]
                judges[direction] = dict(zip(judge_indexes, generate([ids[i] for i in judge_indexes],
                                   f'v3_{args.method}_{direction}_{number}', prompts, 768, False)))
        outputs = []
        for i, row in enumerate(batch):
            issues = []
            if notes[i]['truncated']:
                issues.append('notes_truncated')
            if parsed[i][1]:
                issues.append(parsed[i][1])
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
            outputs.append({'id': row['id'], 'method': args.method, 'attempt': number,
                            'notes': notes[i], 'parsed_notes': parsed[i][0],
                            'draft': drafts.get(i), 'copy_guard': guards.get(i),
                            'judgments': judgments, 'accepted': not issues, 'rejection_reasons': issues})
        return outputs

    todo = [row for row in rows if row['id'] not in prior]
    stopped_early = False
    for offset in range(0, len(todo), args.batch_size):
        if time.time() - started > args.max_seconds - 180 or (
            args.global_deadline_unix and time.time() >= args.global_deadline_unix - 180):
            break
        batch = todo[offset:offset+args.batch_size]
        first = attempt(batch, 1)
        failed = [row for row, result in zip(batch, first) if not result['accepted']]
        second = {result['id']: result for result in attempt(failed, 2)} if failed and time.time()-started < args.max_seconds-180 else {}
        for row, result in zip(batch, first):
            final = dict(second.get(row['id'], result))
            final['first_attempt'] = result
            final['pipeline_revision'] = 3
            final['source_split'] = row['split']
            final['source_genre'] = row.get('genre')
            append(results, final)
            prior[row['id']] = final
        print(json.dumps({'completed': len(prior), 'accepted': sum(x['accepted'] for x in prior.values()),
                          'elapsed_seconds': time.time()-started}), flush=True)
        remaining = set(TRIAL_IDS) - set(prior)
        accepted = sum(x['accepted'] for x in prior.values())
        old_accepted = sum(prior[i]['accepted'] for i in OLD_FAILURES if i in prior)
        technical_accepted = sum(prior[i]['accepted'] for i in TECHNICAL_IDS if i in prior)
        if (accepted + len(remaining) < 28 or
            old_accepted + len(remaining & set(OLD_FAILURES)) < 18 or
            technical_accepted + len(remaining & set(TECHNICAL_IDS)) < 5):
            stopped_early = True
            print('EARLY_STOP_THRESHOLD_IMPOSSIBLE', flush=True)
            break
    technical = sum(prior[i]['accepted'] for i in TECHNICAL_IDS if i in prior)
    summary = {'status': 'COMPLETE' if len(prior)==40 else
               'EARLY_STOP_THRESHOLD_IMPOSSIBLE' if stopped_early else 'INCOMPLETE_DEADLINE',
               'processed': len(prior), 'accepted': sum(x['accepted'] for x in prior.values()),
               'old_failure_accepted': sum(prior[i]['accepted'] for i in OLD_FAILURES if i in prior),
               'technical_accepted': technical,
               'thresholds_met': len(prior)==40 and sum(x['accepted'] for x in prior.values())>=28 and
                       sum(prior[i]['accepted'] for i in OLD_FAILURES if i in prior)>=18 and technical>=5,
               'elapsed_seconds': time.time()-started, 'raw_requests': request_number}
    (args.output/'trial-summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(summary), flush=True)


if __name__ == '__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--input', type=Path, required=True)
    p.add_argument('--old-audit', type=Path, required=True)
    p.add_argument('--output', type=Path, required=True)
    p.add_argument('--method', choices=['chinese','slots'], default='chinese')
    p.add_argument('--primary-summary', type=Path)
    p.add_argument('--batch-size', type=int, default=8)
    p.add_argument('--max-seconds', type=int, default=5400)
    p.add_argument('--global-deadline-unix', type=float)
    run(p.parse_args())
