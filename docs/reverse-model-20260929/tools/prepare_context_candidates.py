"""Trace real article slots for evaluation only; never alter article source files."""
import argparse
import hashlib
import json
import re
import subprocess
from pathlib import Path

ROOT = 'articles/inner-child-therapy/experiments/emulate-20260929/'
OVERNIGHT = '45caa139a94bc5919e26a7026dca05118acc2229'

def sha(text):
    return hashlib.sha256(text.encode()).hexdigest()

def clean_markdown(text):
    text = re.sub(r'<!--.*?-->', '', text, flags=re.S)
    text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', text)
    return text.replace('**', '').replace('*', '')

def normalize_with_offsets(text):
    chars, offsets = [], []
    for index, char in enumerate(text):
        if char.isspace():
            if chars and chars[-1] != ' ':
                chars.append(' '); offsets.append(index)
        else:
            chars.append(char); offsets.append(index)
    return ''.join(chars).strip(), offsets

def main(args):
    cases = [json.loads(l) for l in args.cases.read_text().splitlines()]
    article_paths = [Path('articles/inner-child-therapy/HUMANIZED-ARTICLE-SO-FAR.md'),
                     Path('articles/romance/master.md')]
    sources = [(p, p.read_text(), clean_markdown(p.read_text())) for p in article_paths]
    reference_directory = Path(ROOT + 'inputs/learning/A_joelfixes')
    contexts = []
    for case in cases:
        if case['set'] != 'A' or case.get('emulate') is None:
            continue
        number = case['id'].split('_')[0]
        # A02 and A03 are successive versions of the same Dangerous Adult P1,
        # documented in the input manifest. The current installed P1 is A03.
        anchor = 'A03' if number == 'A02' else number
        reference_path = reference_directory / (anchor + '_joel_after_REFERENCE_ONLY.txt')
        reference = reference_path.read_text().strip()
        needle = re.sub(r'\s+', ' ', reference).strip()
        matches = []
        for source_path, original, text in sources:
            normalized, offsets = normalize_with_offsets(text)
            where = normalized.find(needle)
            if where < 0:
                continue
            assert normalized.find(needle, where + 1) < 0, 'Ambiguous article slot: ' + case['id']
            start = offsets[where]; end = offsets[where + len(needle) - 1] + 1
            headings = list(re.finditer(r'^(#{1,6})\s+(.+)$', text, re.M))
            previous = [h for h in headings if h.start() < start]
            assert previous, 'Article slot has no section heading'
            heading = previous[-1]
            level = len(heading.group(1))
            following = next((h for h in headings if h.start() > end and len(h.group(1)) <= level), None)
            section_end = following.start() if following else len(text)
            prefix, suffix = text[heading.start():start], text[end:section_end]
            matches.append({'id': case['id'], 'input_sha256': case['input_sha256'],
                            'source_file': str(source_path), 'source_sha256': sha(original),
                            'source_role': 'frozen article assembly/master for experiment; no new publication authority',
                            'section_heading': heading.group(2), 'section_heading_level': level,
                            'anchor_reference_file': str(reference_path), 'anchor_sha256': sha(reference),
                            'anchor_alias': None if anchor == number else
                                'A02 earlier Dangerous Adult P1 -> A03 current P1 slot; input manifest identifies same destination',
                            'prefix': prefix, 'suffix': suffix,
                            'context_words_excluding_output': len((prefix + suffix).split()),
                            'construction': 'replace the exact reference slot inside its full real Markdown section; preserve all other section text',
                            'training_use': 'FORBIDDEN'})
        assert len(matches) <= 1
        contexts.extend(matches)
    b01 = next(c for c in cases if c['id'] == 'B01_m34')
    path = ROOT + 'inputs/learning/CONTEXT_section_so_far.txt'
    text = subprocess.check_output(['git', 'show', OVERNIGHT + ':' + path], text=True)
    contexts.append({'id': b01['id'], 'input_sha256': b01['input_sha256'],
                     'source_file': path, 'source_commit': OVERNIGHT, 'source_sha256': sha(text),
                     'section_heading': text.splitlines()[0], 'prefix': text + '\n\n', 'suffix': '',
                     'context_words_excluding_output': len(text.split()),
                     'construction': 'exact prescribed section-so-far bytes, two LF, exact raw output',
                     'training_use': 'FORBIDDEN'})
    contexts.sort(key=lambda r: r['id'])
    assert len({c['id'] for c in contexts}) == len(contexts)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(''.join(json.dumps(c, ensure_ascii=False) + '\n' for c in contexts))
    print(json.dumps({'traceable_candidates': len(contexts), 'ids': [c['id'] for c in contexts],
                      'fixed_context_words': sum(c['context_words_excluding_output'] for c in contexts),
                      'candidates_sha256': sha(args.output.read_text()),
                      'selection_basis': 'exact real article slot available before model scoring; A02 same-P1 alias documented',
                      'paid_scans': 0, 'E_holdout_accessed': False}))

if __name__ == '__main__':
    p = argparse.ArgumentParser(); p.add_argument('--cases', type=Path, required=True)
    p.add_argument('--output', type=Path, required=True)
    main(p.parse_args())
