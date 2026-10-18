"""triage_apply.py - put a triaged second reading's fixes into a refix section (2026-10-18).

A refix screen that reads Human (Emulate's rewrite of my meaning-fixed text) gets a second reader; its findings are
triaged (fix-20261018/rf-a/TRIAGE-BRIEF.md: only what changes what a reader would do or believe is fixed, in few words)
into KEY.triage.json: {"key", "fixes": [{"block", "problems": [...]}], "let_stand": [...], "resample": [...]}. This writes
the fixes as a review (KEY.review.json, faithful.py's shape), applies them to the refix units (faithful.apply ->
KEY.fixed.json), and reports what didn't fit and the share of the words changed, the number that decides whether the
section stays Human (under 18%: 3 of 3 fixed sections did; above it, 2 of 30).

  python3 tools/triage_apply.py UNITS.json [UNITS.json ...]     (KEY.triage.json next to each)
"""
import difflib, json, pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import faithful as F  # noqa: E402


def changed(a, b):
    a, b = a.split(), b.split()
    sm = difflib.SequenceMatcher(a=a, b=b, autojunk=False)
    return 1 - sum(m.size for m in sm.get_matching_blocks()) / max(len(a), len(b), 1)


def run(units_path):
    units_path = pathlib.Path(units_path)
    key = json.loads(units_path.read_text(encoding='utf-8'))['key']
    tri = json.loads((units_path.parent / ('%s.triage.json' % key)).read_text(encoding='utf-8'))
    review = [{'block': f['block'], 'verdict': 'FIX', 'problems': f['problems']} for f in tri.get('fixes', []) if f.get('problems')]
    rp = units_path.parent / ('%s.review.json' % key)
    rp.write_text(json.dumps(review, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    out = units_path.parent / ('%s.fixed.json' % key)
    bad, redo = F.apply(str(units_path), str(rp), str(out))
    before = '\n\n'.join(p for u in json.loads(units_path.read_text(encoding='utf-8'))['units'] for p in u['paras'])
    after = '\n\n'.join(p for u in json.loads(out.read_text(encoding='utf-8'))['units'] for p in u['paras'])
    share = changed(before, after)
    n = sum(len(f['problems']) for f in review)
    print('%s: %d fixes, %d let stand, resample %s, %d did not fit; %.1f%% of the words changed'
          % (key, n, len(tri.get('let_stand', [])), tri.get('resample') or '-', len(bad), 100 * share))
    return {'key': key, 'fixes': n, 'let_stand': len(tri.get('let_stand', [])), 'resample': tri.get('resample') or [],
            'bad': bad, 'changed': share}


if __name__ == '__main__':
    for p in sys.argv[1:]:
        run(p)
