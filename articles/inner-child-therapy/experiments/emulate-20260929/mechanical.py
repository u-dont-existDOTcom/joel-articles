"""Exact-source sentence alignment and splice materialization; no provider calls."""
import argparse
import difflib
import hashlib
import json
import re
from pathlib import Path


def digest(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def spans(text):
    # Include every separator in its preceding unit so untouched text is lossless.
    result = []
    start = 0
    for match in re.finditer(r'[.!?][\"”’\')]*\s+|\n\s*\n', text):
        end = match.end()
        if text[start:end].strip():
            result.append({'start': start, 'end': end, 'text': text[start:end]})
            start = end
    if start < len(text):
        result.append({'start': start, 'end': len(text), 'text': text[start:]})
    assert ''.join(item['text'] for item in result) == text
    return result


def overlap(left, right):
    tokens = lambda t: re.findall(r'\w+', t.casefold())
    return difflib.SequenceMatcher(None, tokens(left), tokens(right), autojunk=False).ratio()


def paragraph_spans(text):
    result, start = [], 0
    for match in re.finditer(r'\n[ \t]*\n(?:[ \t]*\n)*', text):
        end = match.end()
        if text[start:end].strip():
            result.append({'start': start, 'end': end, 'text': text[start:end]})
            start = end
    if start < len(text):
        result.append({'start': start, 'end': len(text), 'text': text[start:]})
    assert ''.join(item['text'] for item in result) == text
    return result


def align(source, output, unit_kind='sentence'):
    assert unit_kind in ('sentence', 'paragraph')
    segmenter = spans if unit_kind == 'sentence' else paragraph_spans
    a, b = segmenter(source), segmenter(output)
    n, m = len(a), len(b)
    cost = {(0, 0): 0.0}
    back = {}
    for i in range(n + 1):
        for j in range(m + 1):
            if (i, j) not in cost:
                continue
            for da, db in [(1, 1), (1, 2), (2, 1), (1, 0), (0, 1)]:
                ni, nj = i + da, j + db
                if ni > n or nj > m:
                    continue
                left = ''.join(x['text'] for x in a[i:ni])
                right = ''.join(x['text'] for x in b[j:nj])
                score = overlap(left, right) if da and db else 0.0
                step = 1 - score + 0.12 * (da + db - 2) if da and db else 0.68
                candidate = cost[(i, j)] + step
                if candidate < cost.get((ni, nj), float('inf')):
                    cost[(ni, nj)] = candidate
                    back[(ni, nj)] = (i, j, score)
    units = []
    i, j = n, m
    while (i, j) != (0, 0):
        pi, pj, score = back[(i, j)]
        aa, bb = a[pi:i], b[pj:j]
        units.append({'source_sentences': list(range(pi, i)), 'output_sentences': list(range(pj, j)),
                      'source_start': a[pi]['start'] if aa else (a[pi]['start'] if pi < n else len(source)),
                      'source_end': aa[-1]['end'] if aa else (a[pi]['start'] if pi < n else len(source)),
                      'output_start': b[pj]['start'] if bb else (b[pj]['start'] if pj < m else len(output)),
                      'output_end': bb[-1]['end'] if bb else (b[pj]['start'] if pj < m else len(output)),
                      'source_text': ''.join(x['text'] for x in aa), 'output_text': ''.join(x['text'] for x in bb),
                      'word_overlap': score, 'semantic_disposition': 'UNREVIEWED_BY_PRO'})
        i, j = pi, pj
    units.reverse()
    assert ''.join(u['source_text'] for u in units) == source
    assert ''.join(u['output_text'] for u in units) == output
    if unit_kind == 'paragraph':
        for unit in units:
            unit['source_paragraphs'] = unit.pop('source_sentences')
            unit['output_paragraphs'] = unit.pop('output_sentences')
    return {'source_sha256': digest(source), 'output_sha256': digest(output),
            f'source_{unit_kind}_count': n, f'output_{unit_kind}_count': m,
            'unit_kind': unit_kind,
            'method': 'monotone word-overlap difflib; heuristic, not semantic proof', 'units': units}


def splice(alignment, selected, backward=False):
    selected = set(selected)
    return ''.join(u['source_text' if (backward == (i in selected)) else 'output_text']
                   for i, u in enumerate(alignment['units']))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input')
    parser.add_argument('output')
    parser.add_argument('alignment_file')
    args = parser.parse_args()
    # Reading and writing bytes avoids implicit CR/LF normalization.
    source = Path(args.input).read_bytes().decode('utf-8')
    output = Path(args.output).read_bytes().decode('utf-8')
    result = align(source, output)
    Path(args.alignment_file).parent.mkdir(parents=True, exist_ok=True)
    Path(args.alignment_file).write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')


if __name__ == '__main__':
    main()
