"""Pure parsing and copy admission for Claude's regeneration v3 trial."""
import json
import re
from copy_check import MAX_SHARED_WORDS, WORD, quote_spans


POLICY = 'normalized-word-runs-source-quotes-and-bounded-keep-v2'
LIST_MARKER = re.compile(r'(?m)^\s*(?:[-*•]|\d+[.)])\s+')
KEEP_ITEM = re.compile(r'^\s*(?:[-*•]\s*)?(.+?)\s*$')


def parse_chinese_notes(text):
    """Require the three separate sections; drafting receives FORM and NOTES only."""
    match = re.search(r'(?ms)^FORM:\s*(.+?)\nKEEP:\s*\n(.*?)\nNOTES:\s*\n(.+)$', text.strip())
    if not match:
        return None, 'missing_form_keep_or_notes_section'
    form, keep_block, notes = (part.strip() for part in match.groups())
    keep = [KEEP_ITEM.fullmatch(line).group(1).strip() for line in keep_block.splitlines()
            if line.strip() and KEEP_ITEM.fullmatch(line)]
    if not form or not keep or not notes:
        return None, 'empty_form_keep_or_notes'
    if len(re.findall(r'[\u4e00-\u9fff]', notes)) < 20:
        return None, 'notes_not_substantially_chinese'
    return {'form': form, 'keep': keep, 'notes': notes}, None


def parse_slots_notes(text):
    raw = text.strip()
    if raw.startswith('```'):
        raw = raw.split('\n', 1)[-1].rsplit('```', 1)[0].strip()
    try:
        data = json.loads(raw)
    except (ValueError, TypeError):
        return None, 'slots_invalid_json'
    if not isinstance(data, dict) or not isinstance(data.get('FORM'), str) or not data['FORM'].strip():
        return None, 'slots_invalid_form'
    if not isinstance(data.get('KEEP'), list) or not all(isinstance(x, str) for x in data['KEEP']):
        return None, 'slots_invalid_keep'
    facts = data.get('FACTS')
    if not isinstance(facts, list) or not facts:
        return None, 'slots_missing_facts'
    for index, fact in enumerate(facts):
        if not isinstance(fact, dict) or not isinstance(fact.get('negated'), bool):
            return None, f'slots_invalid_fact_{index}'
        for field in ('subject', 'relation', 'object', 'qualifier'):
            value = fact.get(field)
            if not isinstance(value, str) or len(WORD.findall(value)) > 5:
                return None, f'slots_invalid_{field}_{index}'
        if not any(fact[field].strip() for field in ('subject', 'relation', 'object')):
            return None, f'slots_empty_fact_{index}'
    return {'form': data['FORM'].strip(), 'keep': [x.strip() for x in data['KEEP']],
            'facts': facts, 'notes': render_slots_table(facts)}, None


def render_slots_table(facts):
    columns = ('subject', 'relation', 'object', 'qualifier', 'negated')
    lines = ['| ' + ' | '.join(columns) + ' |', '| ' + ' | '.join(['---']*len(columns)) + ' |']
    for fact in facts:
        lines.append('| ' + ' | '.join(str(fact[col]).replace('|', '/') for col in columns) + ' |')
    return '\n'.join(lines)


def _tokens(text):
    return [(match.group().casefold(), match.start(), match.end()) for match in WORD.finditer(text)]


def _occurrences(tokens, words):
    n = len(words)
    return [(tokens[i][1], tokens[i+n-1][2], tuple(range(i, i+n)))
            for i in range(len(tokens)-n+1)
            if [token[0] for token in tokens[i:i+n]] == words]


def qualified_keep(source, keep):
    """Apply exact membership, per-item length, and the combined 30% ceiling."""
    tokens = _tokens(source)
    chosen, covered, rejected = [], set(), []
    for raw in keep:
        item = raw.strip().strip('"“”')
        words = [token[0] for token in _tokens(item)]
        if not words:
            rejected.append({'item': raw, 'reason': 'no_words'})
            continue
        limit = 8 if any(char.isupper() or char.isdigit() for char in item) else 3
        if len(words) > limit:
            rejected.append({'item': raw, 'reason': 'too_long'})
            continue
        found = _occurrences(tokens, words)
        if not found:
            rejected.append({'item': raw, 'reason': 'not_in_source'})
            continue
        new_covered = covered | {i for _, _, indexes in found for i in indexes}
        if len(new_covered) > 0.30 * len(tokens):
            rejected.append({'item': raw, 'reason': 'combined_share_exceeded'})
            continue
        if words not in [entry['words'] for entry in chosen]:
            chosen.append({'text': item, 'words': words})
        covered = new_covered
    return chosen, len(covered) / max(len(tokens), 1), rejected


def _segments(text, source_quotes, protected):
    spans = [(start, end) for start, end, _ in quote_spans(text)
             if text[start+1:end-1].strip() in source_quotes]
    tokens = _tokens(text)
    for entry in protected:
        spans.extend((start, end) for start, end, _ in _occurrences(tokens, entry['words']))
    merged = []
    for start, end in sorted(spans):
        if merged and start <= merged[-1][1]:
            merged[-1] = (merged[-1][0], max(end, merged[-1][1]))
        else:
            merged.append((start, end))
    parts, last = [], 0
    for start, end in merged:
        parts.append([token[0] for token in _tokens(text[last:start])])
        last = end
    parts.append([token[0] for token in _tokens(text[last:])])
    return parts


def _longest(left, right):
    best = 0
    for a in left:
        for b in right:
            previous = [0] * (len(b) + 1)
            for word in a:
                current = [0] * (len(b) + 1)
                for j, other in enumerate(b, 1):
                    if word == other:
                        current[j] = previous[j-1] + 1
                        best = max(best, current[j])
                previous = current
    return best


def copy_guard(source, notes, draft, keep):
    protected, share, rejected = qualified_keep(source, keep)
    source_quotes = {quote for _, _, quote in quote_spans(source)}
    original = _segments(source, source_quotes, protected)
    runs = {key: _longest(original, _segments(value, source_quotes, protected))
            for key, value in [('notes', notes), ('draft', draft)]}
    return {'policy': POLICY, 'notes_longest_run': runs['notes'],
            'draft_longest_run': runs['draft'], 'maximum_allowed_shared_words': MAX_SHARED_WORDS,
            'exempt_source_word_share': share, 'qualified_keep': [item['text'] for item in protected],
            'rejected_keep': rejected, 'draft_has_list_markers': bool(LIST_MARKER.search(draft)),
            'passed': max(runs.values()) <= MAX_SHARED_WORDS and not LIST_MARKER.search(draft)}
