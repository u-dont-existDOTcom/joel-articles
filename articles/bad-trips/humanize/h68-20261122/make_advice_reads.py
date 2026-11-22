#!/usr/bin/env python3
"""make_advice_reads.py - turn 60's read of the guide's medical part for advice that doesn't make sense, after his round-49
marks on step 7 ("i'm not sure how s15 and s16 got into this to begin with but i hope we don't have other nonsensical stuff
in this guide"; lesson bad-trips-2026-11-22c). The fit read's brief (tools/humanization/fit_read_brief.md, its four
questions) with a fifth, RIGHT, for advice a careful reader would doubt is correct or safe for this case. One fresh reader
per part of the medical sections; each flag is then checked against a source and gets a fate (ADVICE-FATES.md).

  python3 make_advice_reads.py      writes advice/prompt-PART.txt for each part
"""
import pathlib, re

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[3]
GUIDE = (REPO / 'articles/bad-trips/GUIDE-SO-FAR.md').read_text(encoding='utf-8').split('\n')
PARTS = {  # 1-based line ranges of GUIDE-SO-FAR.md, by heading
    'outside-help': ('# When to Get Outside Help', '# Medical and Brain Rescue'),
    'brain-seizure': ('# Medical and Brain Rescue', '## MDMA: Magnesium Alarm'),
    'mdma-chest-swallowed': ('## MDMA: Magnesium Alarm', '## Serotonin Syndrome (SS)?'),
    'serotonin': ('## Serotonin Syndrome (SS)?', '# My Acute Rescue Remedies'),
}
WHAT = ('a harm-reduction guide on bad trips and overdoses for people who take psychedelics and other drugs and the friends '
        'who sit with them, by a writer who uses and supplies some of the remedies it describes; this part is its medical '
        'part, what to do when the body is in danger')
MOMENT = ('you are a friend with no medical training sitting with someone in trouble after taking a psychedelic, MDMA or '
          'another drug, at home or at a gathering at night, reading this part to decide what to do right now')
body = (REPO / 'tools/humanization/fit_read_brief.md').read_text(encoding='utf-8').split('\n---\n', 1)[1].strip()
RIGHT = ('- RIGHT: As far as you know, is the advice correct and safe for this case? Mark it if a careful reader would doubt '
         'it: it could hurt the person, it contradicts what you know of first aid or medicine, or it rests on a claim that '
         'needs a source it doesn\'t have. Say what you doubt and why, in a line; the writer will check it against sources.')
body = body.replace("- MISREAD:", RIGHT + "\n- MISREAD:", 1)
body = body.replace('ask four questions', 'ask five questions').replace('/ MISREAD -\n', '/ RIGHT - / MISREAD -\n')


def sentences(lines):
    out = []
    for line in lines:
        line = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', line.replace('**', '')).strip()
        if not line or line == '---':
            continue
        out += [p.strip() for p in re.split(r'(?<=[.!?:])["\')\]]?\s+(?=[A-Z0-9"(\[])', line) if p.strip()]
    return out


(HERE / 'advice').mkdir(exist_ok=True)
for key, (a, b) in PARTS.items():
    i = next(k for k, l in enumerate(GUIDE) if l.strip() == a)
    j = next(k for k, l in enumerate(GUIDE) if l.strip() == b and k > i)
    ss = sentences(GUIDE[i:j])
    n = '\n'.join('S%d: %s' % (k + 1, s) for k, s in enumerate(ss))
    t = body.replace('[one line: what kind of text this is, for whom, about what]', WHAT)
    t = t.replace('[one line: who you are as its reader, and what you are doing or deciding as you read this part]', MOMENT)
    t = t.replace('[the text, one line or sentence a line, numbered S1, S2, ...]', n)
    (HERE / 'advice' / ('prompt-%s.txt' % key)).write_text(t + '\n', encoding='utf-8')
    (HERE / 'advice' / ('text-%s.txt' % key)).write_text(n + '\n', encoding='utf-8')
    print(key, len(ss), 'sentences')
