#!/usr/bin/env python3
"""tell_panel.py - fresh readers list a paragraph's AI tells before I name a tell, or ask Joel's help (turn 104).

Joel, 2026-10-23 23:21 UTC. My help request on 97.8 said "I can't find any more AI tells here" and named the
"(dissociating)" gloss as the paragraph's one human tell. The three readers he sent it to (Codex, ChatGPT and Haiku)
each listed several tells, and all three named the gloss as one: "so why don't you fix your process before asking for
help". The turn before had the same failure on a metaphor of mine (E251, Inner Child): I graded my own sentences with
the judgment that wrote them. The lesson is E253 (Inner Child) in docs/HUMANIZATION-GATE.md.

  python3 tools/humanization/tell_panel.py prompt TEXT.txt [--out PROMPT.txt]
      the panel's one fixed question (reviewer/tell_panel.txt) with the paragraph. Every reader gets the same prompt.
  python3 tools/humanization/tell_panel.py summarize DIR
      DIR holds TEXT.txt (the paragraph) and one reply per reader (codex.md, sonnet.md, haiku.md, or a reader Joel
      asked, by name). Writes DIR/PANEL.md and DIR/PANEL.json: each sentence with the readers who quoted its words as
      AI-made, AGREED where two or more did, what each reader said about the paragraph as a whole (its WHOLE: line and
      any point that quotes nothing), and the words readers called human that no reader flagged as AI.
  python3 tools/humanization/tell_panel.py rewrite-prompt DIR --points POINTS.txt --before B.txt --after A.txt
          [--voice VOICE.txt] [--out REWRITE-PROMPT.txt]
      the second writer's brief (reviewer/rewrite_with_tells.txt): the paragraph, its neighbours, the points it has to
      keep, every reader's notes from DIR and lines of Joel's own. For a paragraph two of my drafts couldn't fix.

The readers, each fresh, given PROMPT.txt and nothing else:
- Codex, from Joel's laptop (OpenAI's model, so it doesn't share the habits of the Anthropic models that write here):
    codex exec --skip-git-repo-check --ephemeral -s read-only -C DIR -o DIR/codex.md - < DIR/PROMPT.txt
- a Sonnet agent and a Haiku agent, told to answer from the prompt alone, their replies saved as sonnet.md and haiku.md.

What the panel decides (E253 and E256 (Inner Child)):
- every sentence AGREED, and every WHOLE: point two readers share, gets a fix in the next draft, and the draft goes
  through the panel again before its Pangram try. A flag on one of the guide's own instructions is about how it is said:
  the instruction stays and its wording changes (E256: I had stopped there on 97.8, and GPT fixed it on its first try);
- when two of my drafts have failed after the panel, the next draft comes from a writer of another family (Codex, given
  `rewrite-prompt`), and the panel reads it before its check;
- a help request comes only after that, and links its PANEL.md (pangram_links_check.py fails a help request without one);
- a human tell I name is Joel's words, a fact he gave, or a rough edge (E251). Words the readers called human don't make
  one: ChatGPT called "I'd count the milder stuff too" human, and Joel hears it as "that same habit of being overly
  careful".
"""
import argparse
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
PROMPT = HERE / 'reviewer' / 'tell_panel.txt'
SKIP = {'TEXT', 'PROMPT', 'PANEL', 'README', 'NOTES'}


def norm(s):
    """Lowercase, straight quotes and apostrophes, one space: how quotes are matched against the paragraph."""
    s = s.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')
    s = s.replace('—', '-').replace('–', '-')
    return re.sub(r'\s+', ' ', s).strip().lower()


def clip(s, n=1500):
    """A reader's point, whole unless it runs past n characters, and then cut with a mark (a cut at 400 dropped the end of
    Sonnet's note on the whole paragraph on 2026-10-24)."""
    return s if len(s) <= n else s[:n].rstrip() + ' [cut]'


def sentences(text):
    """The paragraph's sentences, cut after . ! ? or … (with any closing quote or bracket) before a space."""
    text = text.strip()
    out, start = [], 0
    for m in re.finditer(r'[.!?…]+["”’)\]]*(?=\s)', text):
        out.append(text[start:m.end()].strip())
        start = m.end()
    if text[start:].strip():
        out.append(text[start:].strip())
    return [s for s in out if s]


def prompt_for(text):
    body = re.sub(r'<!--.*?-->\n?', '', PROMPT.read_text(encoding='utf-8'), flags=re.S)
    return body.replace('{text}', text.strip())


WHOLE_LINE = re.compile(r'^[\s#*>_-]*\**\s*WHOLE\b', re.I)
HUMAN_LINE = re.compile(r'^[\s#*>_-]*(?:\d+[.)]\s*)?\**\s*(?:HUMAN\b|what (?:sounds|reads|feels) (?:\w+ )?human'
                        r'|human[- ](?:sounding|written|tells?)\b)', re.I)
AI_LINE = re.compile(r'^[\s#*>_-]*\**\s*(?:AI\b|what (?:sounds|reads|feels) (?:more )?AI)', re.I)
QUOTE = re.compile(r'“([^”]{1,400})”|"([^"\n]{1,400})"')


def reader_quotes(reply):
    """[(mode, quote, line)] from one reader's reply: quotes after a HUMAN line are words it calls human, the rest AI tells."""
    mode, out = 'AI', []
    for line in reply.split('\n'):
        if HUMAN_LINE.match(line):
            mode = 'HUMAN'
        elif WHOLE_LINE.match(line):
            mode = 'WHOLE'
        elif AI_LINE.match(line):
            mode = 'AI'
        if mode == 'WHOLE':
            continue
        for m in QUOTE.finditer(line):
            out.append((mode, m.group(1) or m.group(2), line.strip()))
    return out


def whole_points(reply):
    """What a reader says about the paragraph as a whole: its WHOLE: lines, and any AI-list point that quotes nothing."""
    mode, out = 'AI', []
    for line in reply.split('\n'):
        s = line.strip()
        if HUMAN_LINE.match(line):
            mode = 'HUMAN'
            continue
        if WHOLE_LINE.match(line):
            mode = 'WHOLE'
            rest = re.sub(r'^[\s#*>_-]*\**\s*WHOLE\s*:?\**\s*', '', s, flags=re.I)
            if rest and rest.lower() != 'none':
                out.append(rest)
            continue
        if AI_LINE.match(line):
            mode = 'AI'
            continue
        if not s or s.lower() in ('none', '"none"') or s.startswith('<!--'):
            continue
        if mode == 'WHOLE':
            out.append(s)
        elif mode == 'AI' and re.match(r'^(?:[-*]|\d+[.)])\s', s) and not QUOTE.search(s):
            out.append(s)
    return out


def locate(quote, joined, bounds):
    """Spans of the quote's pieces (split at ellipses) in the joined paragraph, and the sentences they touch."""
    spans, sents = [], set()
    for piece in re.split(r'\.\.\.|…', quote):
        p = norm(piece).strip(' ,;:.')
        # A short quote is found only when it has no letters or digits (an emoji such as the 🤗 Haiku and Sonnet flagged
        # on 2026-10-24); a short word would match inside other words.
        if not p or (len(p) < 4 and re.search(r'[a-z0-9]', p)):
            continue
        i = joined.find(p)
        if i < 0:
            continue
        spans.append((i, i + len(p)))
        sents.update(k for k, (a, b) in enumerate(bounds) if a < i + len(p) and i < b)
    return spans, sorted(sents)


def summarize(d):
    d = pathlib.Path(d)
    text = (d / 'TEXT.txt').read_text(encoding='utf-8').strip()
    sents = sentences(text)
    parts, bounds, pos = [], [], 0
    for s in sents:
        n = norm(s)
        parts.append(n)
        bounds.append((pos, pos + len(n)))
        pos += len(n) + 1
    joined = ' '.join(parts)
    readers = sorted(p for p in d.iterdir() if p.suffix in ('.md', '.txt') and p.stem.upper() not in SKIP)
    if not readers:
        sys.exit('no reader replies in %s (codex.md, sonnet.md, haiku.md ...)' % d)
    flags = {k: {} for k in range(len(sents))}          # sentence -> reader -> [(quote, line)]
    ai_spans, human, lost, whole = [], [], [], {}
    for r in readers:
        name = r.stem
        whole[name] = whole_points(r.read_text(encoding='utf-8'))
        for mode, q, line in reader_quotes(r.read_text(encoding='utf-8')):
            spans, where = locate(q, joined, bounds)
            if not spans:
                if norm(q) not in norm(prompt_for('')):
                    lost.append((name, mode, q))
                continue
            if mode == 'AI':
                ai_spans += spans
                for k in where:
                    seen = flags[k].setdefault(name, [])
                    if line not in [l for _, l in seen]:
                        seen.append((q, line))
            else:
                human.append((name, q, spans))
    agreed = [k for k in flags if len(flags[k]) >= 2]
    clean_human = [(n, q) for n, q, spans in human
                   if not any(a < y and x < b for x, y in spans for a, b in ai_spans)]
    out = ['# Tell panel: %s' % d.name, '',
           'Made by `tools/humanization/tell_panel.py summarize` from the readers\' replies in this folder (E253 (Inner Child)). '
           'Readers: %s.' % ', '.join(r.name for r in readers), '',
           'The paragraph (%d words), as the readers saw it:' % len(text.split()), '', '> ' + text, '',
           '| # | sentence | readers who flagged it as AI |', '|---|---|---|']
    for k, s in enumerate(sents):
        who = ', '.join(sorted(flags[k])) or '-'
        out.append('| S%d%s | %s | %s |' % (k + 1, ' AGREED' if k in agreed else '', s.replace('|', '/'), who))
    out += ['', '## Agreed: two or more readers (each gets a fix in the next draft)', '']
    for k in agreed:
        out.append('- **S%d** "%s"' % (k + 1, sents[k]))
        for name in sorted(flags[k]):
            for q, line in flags[k][name]:
                out.append('  - %s: %s' % (name, clip(line)))
    if not agreed:
        out.append('None.')
    single = [k for k in flags if len(flags[k]) == 1]
    out += ['', '## Named by one reader (weigh them)', '']
    for k in single:
        name = next(iter(flags[k]))
        for q, line in flags[k][name]:
            out.append('- S%d, %s: %s' % (k + 1, name, clip(line)))
    if not single:
        out.append('None.')
    out += ['', '## About the whole paragraph (its rhythm, voice and build; a point two readers share gets a fix too)', '']
    for name in sorted(whole):
        for w in whole[name]:
            out.append('- %s: %s' % (name, clip(w)))
    if not any(whole.values()):
        out.append('None.')
    out += ['', '## Words readers called human, and no reader flagged as AI', '',
            'These are the readers\' calls, not human tells: a human tell is Joel\'s words, a fact he gave, or a rough edge '
            '(E251, E256 (Inner Child)).', '']
    out += ['- %s: "%s"' % (n, q) for n, q in clean_human] or ['None.']
    if lost:
        out += ['', '## Quotes not found in the paragraph (a paraphrase, or another text)', '']
        out += ['- %s (%s): "%s"' % (n, m, q) for n, m, q in lost]
    (d / 'PANEL.md').write_text('\n'.join(out) + '\n', encoding='utf-8')
    (d / 'PANEL.json').write_text(json.dumps({
        'readers': [r.stem for r in readers], 'sentences': sents,
        'flagged': {str(k + 1): sorted(flags[k]) for k in flags},
        'agreed': [k + 1 for k in agreed], 'whole': whole, 'human_clean': [q for _, q in clean_human]},
        indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    print('%s: %d readers, %d sentences, agreed %s' % (d, len(readers), len(sents),
                                                       ', '.join('S%d' % (k + 1) for k in agreed) or 'none'))
    return agreed


REWRITE = HERE / 'reviewer' / 'rewrite_with_tells.txt'


def rewrite_prompt(d, points, before, after, voice=None):
    """The second writer's brief: the paragraph and its neighbours, the points to keep, every reader's notes, his lines."""
    d = pathlib.Path(d)
    read = lambda f: pathlib.Path(f).read_text(encoding='utf-8').strip()
    notes = []
    for r in sorted(p for p in d.iterdir() if p.suffix in ('.md', '.txt') and p.stem.upper() not in SKIP):
        body = re.sub(r'<!--.*?-->', '', r.read_text(encoding='utf-8'), flags=re.S).strip()
        body = re.split(r'(?im)^[\s#*>_-]*\**\s*HUMAN\b', body)[0].strip()
        notes.append('%s:\n%s' % (r.stem, body))
    t = re.sub(r'<!--.*?-->\n?', '', REWRITE.read_text(encoding='utf-8'), flags=re.S)
    return (t.replace('{before}', read(before)).replace('{text}', read(d / 'TEXT.txt')).replace('{after}', read(after))
             .replace('{points}', read(points)).replace('{tells}', '\n\n'.join(notes))
             .replace('{voice}', read(voice) if voice else '(none given)'))


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    sub = ap.add_subparsers(dest='cmd', required=True)
    p = sub.add_parser('prompt')
    p.add_argument('text')
    p.add_argument('--out')
    s = sub.add_parser('summarize')
    s.add_argument('dir', nargs='+')
    w = sub.add_parser('rewrite-prompt')
    w.add_argument('dir')
    w.add_argument('--points', required=True)
    w.add_argument('--before', required=True)
    w.add_argument('--after', required=True)
    w.add_argument('--voice')
    w.add_argument('--out')
    a = ap.parse_args(argv)
    if a.cmd == 'rewrite-prompt':
        body = rewrite_prompt(a.dir, a.points, a.before, a.after, a.voice)
        if a.out:
            pathlib.Path(a.out).write_text(body, encoding='utf-8')
        else:
            sys.stdout.write(body)
        return
    if a.cmd == 'prompt':
        body = prompt_for(pathlib.Path(a.text).read_text(encoding='utf-8'))
        if a.out:
            pathlib.Path(a.out).write_text(body, encoding='utf-8')
        else:
            sys.stdout.write(body)
    else:
        for d in a.dir:
            summarize(d)


if __name__ == '__main__':
    main()
