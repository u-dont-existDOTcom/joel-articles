"""Mechanical admission for the last, whole-passage Chinese round-trip trial."""
import re

from regen_v3_policy import copy_guard, qualified_keep

LATIN_RUN = re.compile(r"[A-Za-z0-9][A-Za-z0-9'’._:/-]*(?:[ \t]+[A-Za-z0-9][A-Za-z0-9'’._:/-]*)*")
WORD_IN_RUN = re.compile(r"[A-Za-z0-9]+(?:['’][A-Za-z0-9]+)*")


def source_latin_runs(source, translation):
    """Find contiguous English runs in the translation that occur in the source."""
    source_words = [word.casefold() for word in WORD_IN_RUN.findall(source)]
    found = []
    for match in LATIN_RUN.finditer(translation):
        words = [word.casefold() for word in WORD_IN_RUN.findall(match.group())]
        if not words:
            continue
        width = len(words)
        if any(source_words[i:i+width] == words for i in range(len(source_words)-width+1)):
            found.append((match.start(), match.end(), match.group()))
    return found


def chinese_fraction(source, translation):
    """Remove source-matching Latin runs, then count all remaining letters."""
    parts, cursor = [], 0
    matches = source_latin_runs(source, translation)
    for start, end, _ in matches:
        parts.append(translation[cursor:start])
        cursor = end
    parts.append(translation[cursor:])
    remaining = ''.join(parts)
    letters = [char for char in remaining if char.isalpha()]
    chinese = sum('\u4e00' <= char <= '\u9fff' for char in letters)
    return {'chinese_fraction': chinese/len(letters) if letters else 0.0,
            'chinese_letters': chinese, 'remaining_letters': len(letters),
            'removed_source_latin_runs': [run for _, _, run in matches],
            'passed': bool(letters) and chinese/len(letters) >= 0.90}


def roundtrip_guard(source, translation, draft):
    runs = [run for _, _, run in source_latin_runs(source, translation)]
    guard = copy_guard(source, translation, draft, runs)
    guard['translation_longest_run'] = guard.pop('notes_longest_run')
    guard['protected_source_runs'] = guard.pop('qualified_keep')
    guard['rejected_source_runs'] = guard.pop('rejected_keep')
    return guard
