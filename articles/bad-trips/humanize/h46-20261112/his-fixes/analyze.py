#!/usr/bin/env python3
"""analyze.py - what his fixes change, counted: each pattern's rate in the text a card showed (model text: the guide's
drafted words or my fixes) against its rate in his version, over every pair in PAIRS.json and the final try of each series
in SERIES.json. Writes COUNTS.md.

  python3 analyze.py        (from anywhere)
"""
import json, pathlib, re, statistics
HERE = pathlib.Path(__file__).resolve().parent

P = {
 'different/differs': r"\bdiffer(?:ent|s|ence|ently)?\b",
 '"not X but Y", "X, not Y", "but not", "rather than", "instead of", "not just/only"':
     r"\bnot\b[^.?!;\n]{1,60}\bbut\b|\bbut not\b|,\s*not\s+(?:a|an|the|just|only|to|for|as|in|on|by|because)?\s*\w+[.;]|\brather than\b|\binstead of\b|\bnot (?:just|only|merely|simply)\b|\bisn['’]t\b[^.?!\n]{0,40}\bit['’]s\b",
 'a list of three or more ("A, B, and C")': r"\b[\w-]+(?: [\w-]+){0,3}, [\w-]+(?: [\w-]+){0,3},? (?:and|or) [\w-]+",
 'a term defined after a colon ("Term: what it is")': r"(?:^|\n)\s*[-*]?\s*\**[A-Z][\w -]{1,40}\**:\s+[a-z]",
 'nominalizations (-tion, -ment, -ness, -ity, -ance, -ence)': r"\b\w{3,}(?:tion|sion|ment|ness|ity|ance|ence)s?\b",
 'contractions': r"\b\w+['’](?:s|t|re|ve|ll|d|m)\b",
 'I, me, my, we, us, our': r"\b(?:I|me|my|mine|we|us|our|ours)\b",
 'you, your': r"\b(?:you|your|yours|yourself)\b",
 'may, might, can, could, often, usually': r"\b(?:may|might|can|could|often|usually|typically|generally)\b",
 'brackets': r"\(",
 'semicolons and dashes': r";|—|–|--",
 'questions': r"\?",
 '"etc.", "..." and "like" (examples)': r"\betc\b|\.\.\.|…|\blike\b",
 'model words (key, crucial, essential, ensure, significant, various, process, approach, aspect)':
     r"\b(?:key|crucial|essential|ensure|significant|various|process|approach|aspect|overall|notably|additionally|furthermore|moreover)\b",
}
SENT = re.compile(r'[^.?!\n]+[.?!]*')


def sentences(t):
    return [s.strip() for s in SENT.findall(t) if len(s.split()) >= 2]


def words(t):
    return re.findall(r"[A-Za-z0-9'’]+", t)


def openers(t):
    """Sentences that open the way the one before did (the same first word, or a pointer word: This, That, It, These),
    per 100 words: "this is different. that's different, this other thing is also different"."""
    ss = sentences(t)
    n = 0
    for a, b in zip(ss, ss[1:]):
        wa, wb = words(a.lower())[:1], words(b.lower())[:1]
        if wa and wa == wb:
            n += 1
    n += sum(1 for s in ss if re.match(r"(?:This|That|These|Those|It)\b", s))
    return n


def stats(t):
    w = len(words(t)) or 1
    ss = sentences(t)
    lens = [len(words(s)) for s in ss] or [0]
    out = {k: 100.0 * len(re.findall(v, t)) / w for k, v in P.items()}
    out['sentences that open like the one before, or on This/That/It'] = 100.0 * openers(t) / w
    out['sentences starting So, And, But, Or'] = 100.0 * sum(1 for s in ss if re.match(r"(?:So|And|But|Or)\b", s)) / w
    out['_words'] = w
    out['_mean_sentence'] = statistics.mean(lens)
    out['_sentence_spread'] = (statistics.pstdev(lens) / statistics.mean(lens)) if statistics.mean(lens) else 0
    return out


D = json.loads((HERE / 'PAIRS.json').read_text(encoding='utf-8'))['kept']
S = json.loads((HERE / 'SERIES.json').read_text(encoding='utf-8'))
pairs = [(p['lane'], p['id'], p['before'], p['his']) for p in D]
pairs += [('bad-trips', k, v['before'], v['tries'][-1]['text']) for k, v in S.items()]

keys = list(stats('a b.').keys())
agg = {k: [0.0, 0.0] for k in keys}
moves = {k: [0, 0, 0] for k in keys}
wb = wh = 0
for lane, cid, b, h in pairs:
    sb, sh = stats(b), stats(h)
    wb += sb['_words']; wh += sh['_words']
    for k in keys:
        if k.startswith('_'):
            continue
        agg[k][0] += sb[k] * sb['_words'] / 100.0
        agg[k][1] += sh[k] * sh['_words'] / 100.0
        if sb[k] > sh[k]:
            moves[k][0] += 1
        elif sh[k] > sb[k]:
            moves[k][1] += 1
        else:
            moves[k][2] += 1
mean_b = statistics.mean(stats(b)['_mean_sentence'] for _, _, b, _ in pairs)
mean_h = statistics.mean(stats(h)['_mean_sentence'] for _, _, _, h in pairs)
spr_b = statistics.mean(stats(b)['_sentence_spread'] for _, _, b, _ in pairs)
spr_h = statistics.mean(stats(h)['_sentence_spread'] for _, _, _, h in pairs)

lines = ['# What his fixes change, counted', '',
         '%d pairs: every fix he sent on a review page in this repository (%s) and the last try of his three bad-trips '
         'series read from his Pangram history. "Before" is the text the card showed: model text, the drafted article or '
         'my fixes. %d words before, %d in his versions.' % (len(pairs), ', '.join(sorted({p[0] for p in pairs})), wb, wh), '',
         '| pattern | per 100 words before | in his versions | pairs where he had fewer / more / the same |',
         '|---|---|---|---|']
rows = []
for k in keys:
    if k.startswith('_'):
        continue
    rb, rh = 100.0 * agg[k][0] / wb, 100.0 * agg[k][1] / wh
    rows.append((rh / rb if rb else 9, k, rb, rh, moves[k]))
for ratio, k, rb, rh, m in sorted(rows):
    lines.append('| %s | %.2f | %.2f | %d / %d / %d |' % (k, rb, rh, m[0], m[1], m[2]))
lines += ['', 'Sentence length: %.1f words on average before, %.1f in his versions; spread (standard deviation over mean) '
          '%.2f before, %.2f in his.' % (mean_b, mean_h, spr_b, spr_h), '']
(HERE / 'COUNTS.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')
print('\n'.join(lines))
