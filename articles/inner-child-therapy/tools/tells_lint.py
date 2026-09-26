#!/usr/bin/env python3
"""tells_lint.py - run the written tells audit mechanically before any Pangram check.

Usage:
  python3 tells_lint.py DRAFT [--source SOURCE] [--owner OWNER] [--quiet]

DRAFT, SOURCE and OWNER are plain-text or markdown files.
  --source  the AI source section. Enables a review note (D9) when my paragraphs
            walk through the source's points in the source's order. That's not a
            failure by itself: organization is fine when the prose notices things.
  --owner   the owner's own lines, one per line. They're excluded from the
            sentence checks (they're his, not mine) but still counted in the metrics.
There is deliberately no check against phrases from failed drafts (Joel, 2026-09-26):
an old phrase is judged like any other, on whether it looks AI. Swapping phrases
between rounds while the structure stays is what humanizer bots do.
Exit code: 2 = FAIL, 1 = REVIEW, 0 = CLEAR.
A CLEAR only means no mechanical tells were found. The judgment checks
(D2 disparity, A1 meaning and safety, referents) still have to be written by hand.
"""
import re, sys, argparse, math
from statistics import mean, pstdev

def clean(t):
    t = re.sub(r'<!--.*?-->', '', t, flags=re.S)
    t = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', t)
    t = re.sub(r'^#+\s.*$', '', t, flags=re.M)          # drop headings
    t = t.replace('*', '')
    return t.strip()

def paragraphs(t):
    ps = [p.strip() for p in re.split(r'\n\s*\n', t) if p.strip()]
    # drop heading-like lines: short and without sentence punctuation at the end
    return [p for p in ps if not (len(p.split()) <= 12 and not p.rstrip().endswith(('.', '?', '!', '"', '”', ':')))]

ABBREVIATIONS = ('Mr.', 'Mrs.', 'Ms.', 'Dr.', 'St.', 'vs.', 'e.g.', 'i.e.')

def sentences(p):
    p = re.sub(r'\s+', ' ', p)
    parts = re.split(r'(?<=[.!?])["”]?\s+(?=["“]?[A-Z0-9])', p)
    # Rejoin splits after an abbreviation: "Mr. Rogers" was read as two sentences,
    # which produced false short-landing and announcing flags (2026-09-26).
    out = []
    for s in (x.strip() for x in parts if x.strip()):
        if out and out[-1].endswith(ABBREVIATIONS):
            out[-1] = out[-1] + ' ' + s
        else:
            out.append(s)
    return out

def words(s): return re.findall(r"[A-Za-z']+", s)

TICS = [r"doing some work", r"load-bearing", r"tells on itself", r"metaboli[sz]", r"\bdigest", r"\bclean\b",
        r"does its work", r"\b(That's|It's|This is) not [^.?!]{1,60}[.?!] (It's|That's|This is)\b"]
CONTRAST = [r"\b(isn't|is not|wasn't|aren't|not)\b[^.?!]{0,50}\b(it's|it is|they're|but)\b",
            r"\brather than\b", r"\binstead of\b", r"doesn't mean[^.?!]*\bmeans?\b", r"\bIt's tempting\b",
            r"\bnot the same as\b", r"\bis still a long way from\b", r"\bthe difference between\b"]
THESIS = [r"\band (still|yet)\b", r"\beven if\b", r"\beven though\b", r"\benough to\b[^.?!]*\b(but|not)\b",
          r"\bnot necessarily\b", r"\bstill counts\b", r"\banyway[.!]", r"\bonly gets you\b",
          r"^(Most|Nobody|Everyone|Everybody|People|Kids|Children|No one|Plenty of|Anybody who)\b"]
COACH = [r"\byou can\b", r"\byou might\b", r"\byou'll (want|need|probably)\b", r"\bat some point\b",
         r"\bthat's (fine|okay|ok|normal|all right)\b", r"\bit helps( to)?\b", r"\bstart (by|with)\b",
         r"\bthe next step\b", r"\bdon't be surprised\b", r"\bit's tempting\b", r"\byou don't (have|need) to\b",
         r"\bkeep in mind\b", r"\bremember (that|to)\b", r"\bgive yourself\b", r"\bit's okay to\b",
         r"\bthe goal is\b", r"\bthe point is\b", r"\bin other words\b", r"\bgo easy\b"]
ANNOUNCE = [r"^(Or maybe|For [a-z]+,|Here's|That's where|The next step|Now,|First,|Second,|Finally,|So the next)",
            r"^[A-Z][a-z]+ (is|are|can be|works like) [^.]{0,30}\.$"]
IMPER = set("""think picture imagine ask try put start leave borrow skip write take let keep stop find notice make give go
use pick tell say be do don't dont notice consider remember breathe turn stay come look call eat sleep sit""".split())
STOP = set("""a an the and or but if so to of in on at for with by from as is are was were be been being it its it's this that
these those you your yours i me my we our they them their he she his her not no do does did done have has had can could
would should will just about into than then there here what which who whom when where why how all any some more most very
up out over under again also too even still yet only own same such own each few other get got""".split())

def content(s): return [w.lower() for w in words(s) if w.lower() not in STOP and len(w) > 2]

def cos(a, b):
    from collections import Counter
    A, B = Counter(a), Counter(b)
    num = sum(A[k]*B[k] for k in A)
    den = math.sqrt(sum(v*v for v in A.values()))*math.sqrt(sum(v*v for v in B.values()))
    return num/den if den else 0.0

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('draft'); ap.add_argument('--source')
    ap.add_argument('--owner'); ap.add_argument('--quiet', action='store_true')
    a = ap.parse_args()
    text = clean(open(a.draft, encoding='utf-8').read())
    owner = set()
    if a.owner:
        owner = {re.sub(r'\s+', ' ', l.strip()) for l in open(a.owner, encoding='utf-8') if l.strip()}
    ps = paragraphs(text)
    allw = words(text); nw = len(allw) or 1
    flags = []   # (severity, rule, sentence)
    def flag(sev, rule, s): flags.append((sev, rule, s))
    mine_words = 0; coach_hits = 0; you_hits = 0
    para_final_short = 0; imper_heavy = 0
    openers = []
    sent_lens = []
    for p in ps:
        ss = sentences(p)
        openers.append(' '.join(words(ss[0])[:1]).lower() if ss else '')
        imps = 0
        for i, s in enumerate(ss):
            mine = re.sub(r'\s+', ' ', s) not in owner
            w = words(s); sent_lens.append(len(w))
            if not mine: continue
            mine_words += len(w)
            for r in TICS:
                if re.search(r, s, re.I): flag('FAIL', 'B11 tic', s)
            for r in CONTRAST:
                if re.search(r, s, re.I): flag('REVIEW', 'B2 contrast', s); break
            for r in THESIS:
                if re.search(r, s, re.I if not r.startswith('^') else 0): flag('REVIEW', 'B1 finished principle', s); break
            for r in ANNOUNCE:
                if re.search(r, s): flag('REVIEW', 'B5 announces the paragraph', s); break
            hits = sum(len(re.findall(r, s, re.I)) for r in COACH)
            coach_hits += hits
            if hits: flag('REVIEW', 'E41 coach phrase', s)
            you_hits += len(re.findall(r"\byou(r|'re|'ll|'d|'ve)?\b", s, re.I))
            if re.search(r"\bthe kid\b|\bkids?\b", s, re.I): flag('REVIEW', 'E1 kid', s)
            first = (w[0].lower() if w else '')
            if first in IMPER: imps += 1
            if s.count(',') >= 3 or len(re.findall(r'\b(or|and)\b', s)) >= 3:
                flag('REVIEW', 'B4/E15 list or packed sentence', s)
            if i > 0 and len(w) <= 6 and len(words(ss[i-1])) >= 12 and re.match(r"(But|That|It|So|And|Which|They)\b", s):
                flag('REVIEW', 'B3 short knock-down', s)
        if ss and len(words(ss[-1])) <= 9 and re.sub(r'\s+', ' ', ss[-1]) not in owner:
            para_final_short += 1; flag('REVIEW', 'B7 short landing at paragraph end', ss[-1])
        if imps >= 2: imper_heavy += 1; flag('REVIEW', 'E23 paragraph of instructions', p[:90] + '...')
    # paragraph-level metrics
    plen = [len(words(p)) for p in ps]
    cv_p = (pstdev(plen)/mean(plen)) if len(plen) > 1 and mean(plen) else 1
    cv_s = (pstdev(sent_lens)/mean(sent_lens)) if len(sent_lens) > 1 else 1
    coach_density = 100*coach_hits/max(mine_words, 1)
    you_density = 100*you_hits/max(mine_words, 1)
    landing_rate = para_final_short/max(len(ps), 1)
    from collections import Counter
    oc = Counter(o for o in openers if o)
    rep_openers = {k: v for k, v in oc.items() if v >= 3}
    metrics = dict(words=nw, my_words=mine_words, paragraphs=len(ps), coach_per_100=round(coach_density, 2),
                   you_per_100=round(you_density, 1), landing_rate=round(landing_rate, 2),
                   instruction_paragraphs=imper_heavy, para_len_cv=round(cv_p, 2), sent_len_cv=round(cv_s, 2),
                   repeated_openers=rep_openers)
    hard = []
    if coach_density > 2.0: hard.append(f'E41 coach register: {coach_density:.1f} coach phrases per 100 of my words (limit 2.0)')
    if landing_rate >= 0.5 and len(ps) >= 3: hard.append(f'B7/B13 landings: {para_final_short}/{len(ps)} paragraphs end on a short line')
    if imper_heavy >= 2: hard.append(f'E23 listicle: {imper_heavy} paragraphs are strings of instructions')
    if rep_openers: hard.append(f'B13 repeated paragraph openers: {rep_openers}')
    if you_density >= 9.0 and mine_words >= 60:
        hard.append(f'E36/E41 second-person coaching: {you_density:.1f} "you" per 100 of my words (limit 9)')
    elif you_density > 6.0:
        flag('REVIEW', 'E36/E41 heavy second person', f'{you_density:.1f} "you" per 100 of my words')
    # AI marching order: do my paragraphs walk through the source's points in the source's order?
    if a.source:
        src = clean(open(a.source, encoding='utf-8').read())
        spts = [q for q in re.split(r'\n\s*\n|\n- ', src) if len(q.split()) >= 8]
        mapping = []
        for p in ps:
            sims = [cos(content(p), content(q)) for q in spts]
            j = max(range(len(sims)), key=lambda k: sims[k]) if sims else -1
            mapping.append((j, round(sims[j], 2) if j >= 0 else 0))
        matched = [j for j, s in mapping if s >= 0.15]
        inversions = sum(1 for x in range(len(matched)) for y in range(x+1, len(matched)) if matched[x] > matched[y])
        pairs = len(matched)*(len(matched)-1)/2 or 1
        order = 1 - inversions/pairs
        coverage = len(matched)/max(len(ps), 1)
        metrics['source_map'] = mapping; metrics['source_order_agreement'] = round(order, 2)
        metrics['paragraphs_mapped_to_source'] = round(coverage, 2)
        if coverage >= 0.6 and order >= 0.8 and len(set(matched)) >= 0.6*len(matched):
            # Review note, not a hard fail (Joel, 2026-09-26): following the source's order is fine when the
            # sentences notice things along the way. The tell is nothing noticed (inventory T13) or equal weight (T09).
            flag('REVIEW', 'D9 follows the source order',
                 f"{len(matched)}/{len(ps)} paragraphs follow the source's points in its order (agreement {order:.2f}); "
                 f"fine if each part notices something; check T13 and T09 in the tell ledger")
    fails = [f for f in flags if f[0] == 'FAIL']
    verdict = 'FAIL' if (hard or fails) else ('REVIEW' if flags else 'CLEAR')
    print(f'== tells_lint: {a.draft}')
    print('verdict:', verdict)
    for h in hard: print('  HARD:', h)
    print('metrics:', metrics)
    if not a.quiet:
        from collections import defaultdict
        by = defaultdict(list)
        for sev, rule, s in flags: by[rule].append(s)
        for rule in sorted(by):
            print(f'-- {rule} ({len(by[rule])})')
            for s in by[rule]: print('   *', s[:160])
    sys.exit(2 if verdict == 'FAIL' else 1 if verdict == 'REVIEW' else 0)

if __name__ == '__main__':
    main()
