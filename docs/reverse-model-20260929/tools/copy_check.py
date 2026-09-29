"""Mechanical regeneration copy guard; no detector or model-derived labels."""
import difflib
import re

MAX_SHARED_WORDS = 10
POLICY = 'normalized-word-runs-outside-balanced-quotes-v1'
WORD = re.compile(r"\w+(?:['’]\w+)*", re.UNICODE)


def unquoted_segments(text):
    """Exclude balanced speech quotes, retaining a boundary across each exclusion.

    Apostrophes inside words do not start/end single-quoted speech. Unbalanced
    quotes exempt nothing; exact names/numbers alone do not bypass this guard.
    """
    pairs = {'"': '"', '“': '”', '‘': '’', "'": "'"}
    segments, begin, i = [], 0, 0
    while i < len(text):
        opener = text[i]
        if opener not in pairs or (opener in "'‘" and i and text[i-1].isalnum()):
            i += 1
            continue
        close = pairs[opener]
        j = i + 1
        while j < len(text):
            if text[j] == close and not (close in "'’" and j+1 < len(text) and text[j+1].isalnum()):
                break
            j += 1
        if j == len(text):
            i += 1
            continue
        segments.append(text[begin:i])
        begin = j + 1
        i = begin
    segments.append(text[begin:])
    return [[word.casefold() for word in WORD.findall(part)] for part in segments]


def longest_unquoted_run(source, candidate):
    best = 0
    for left in unquoted_segments(source):
        for right in unquoted_segments(candidate):
            previous = [0] * (len(right) + 1)
            for word in left:
                current = [0] * (len(right) + 1)
                for j, other in enumerate(right, 1):
                    if word == other:
                        current[j] = previous[j-1] + 1
                        best = max(best, current[j])
                previous = current
    return best


def overlap(source, candidate):
    run = longest_unquoted_run(source, candidate)
    return {'policy': POLICY, 'maximum_allowed_shared_words': MAX_SHARED_WORDS,
            'longest_unquoted_shared_words': run, 'passed': run <= MAX_SHARED_WORDS,
            'whitespace_sequence_similarity': difflib.SequenceMatcher(
                None, source.split(), candidate.split(), autojunk=False).ratio()}


def regeneration_guard(human, notes, draft):
    result = {'notes': overlap(human, notes), 'draft': overlap(human, draft)}
    result['passed'] = all(result[key]['passed'] for key in ['notes', 'draft'])
    return result
