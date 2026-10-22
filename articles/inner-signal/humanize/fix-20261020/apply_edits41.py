"""The guide's Pangram 4.1 edits, kept as a list and applied to the working copy (2026-10-21).

The sections installed in the 4.0 work are rebuilt from the published text and their fixed files
(tools/install_fixed.py, fix-20261018/installed.json). The 4.1 edits are small changes made after that, sentence by
sentence, so they are kept here as exact replacements (EDITS41.json: key, section, old, new, batch, and the check that
passed) and applied on top: after any rebuild, run this again.

  python3 articles/inner-signal/humanize/fix-20261020/apply_edits41.py                 apply every edit (idempotent)
  python3 articles/inner-signal/humanize/fix-20261020/apply_edits41.py --check         say which are in, without writing
  python3 articles/inner-signal/humanize/fix-20261020/apply_edits41.py --add EDITS.json  add a batch's passed edits to the list

An edit whose "old" text is gone and whose "new" text is there counts as applied; one whose old text isn't found and new
text isn't there either stops the run (the working copy changed under it).
"""
import argparse, json, pathlib, sys

H = pathlib.Path(__file__).resolve().parents[1]
LIST = pathlib.Path(__file__).resolve().parent / 'EDITS41.json'
WORKING = H / 'HUMANIZED-SO-FAR.md'


def load():
    return json.loads(LIST.read_text(encoding='utf-8')) if LIST.exists() else []


def superseded(e, later, md):
    """Later edits of the same sentence carried e's new text on, and the result is in. 2026-10-21: Joel's own edit of
    "Because often your inherited parent ..." came after HG15-p11t, which had put "inherited parent" there, so a later
    edit's old text held e's new text whole. 2026-10-22: batch 470g's rename ("your inherited inner parent tells" to "your
    inherited parent script tells") changed a few words inside his edit's new text, so a later edit's old text can also be
    a part of e's. So e's new text is carried through every later edit in order, taken over whole by one whose old text
    holds it, or changed in place by one whose old text it holds, and what comes out must be in the working copy."""
    if not e['new']:
        return False
    text, moved = e['new'], False
    for l in later:
        if l['old'] and text in l['old']:
            text, moved = l['new'], True
        elif l['old'] and l['old'] in text:
            text, moved = text.replace(l['old'], l['new']), True
    return moved and bool(text) and text in md


def is_in(md, e):
    """The edit is already in MD. When its new text contains its old text (an addition after an installed sentence:
    2026-10-21, b469-HG18-stopped-press), the old text is still there after the edit, so only the new text decides; when its
    new text is part of the old (a cut), the old text must be gone too."""
    old, new = e['old'], e['new']
    if not new:
        return old not in md
    if old and old in new:
        return md.count(new) == 1
    if new in old:
        return new in md and old not in md
    return new in md


def apply(md, edits):
    done, applied = [], []
    for i, e in enumerate(edits):
        if is_in(md, e) or superseded(e, edits[i + 1:], md):
            done.append(e['key'])
        elif e['old'] and md.count(e['old']) == 1:
            md = md.replace(e['old'], e['new'])
            applied.append(e['key'])
        else:
            raise SystemExit('%s: neither its old text (%d times) nor its new text is in the working copy'
                             % (e['key'], md.count(e['old'])))
    return md, applied, done


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('--check', action='store_true')
    ap.add_argument('--add')
    a = ap.parse_args(argv)
    edits = load()
    if a.add:
        new = json.loads(pathlib.Path(a.add).read_text(encoding='utf-8'))
        have = {e['key'] for e in edits}
        edits += [e for e in new if e['key'] not in have]
        LIST.write_text(json.dumps(edits, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
        print('%d edits in the list' % len(edits))
    md = WORKING.read_text(encoding='utf-8')
    out, applied, done = apply(md, edits)
    if not a.check and applied:
        WORKING.write_text(out, encoding='utf-8')
    print('applied now: %s; already in: %s' % (', '.join(applied) or 'none', ', '.join(done) or 'none'))
    return 0


if __name__ == '__main__':
    sys.exit(main())
