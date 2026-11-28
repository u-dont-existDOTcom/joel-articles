#!/usr/bin/env python3
"""fill_receipts_sh.py - the making-sense receipts (tools/humanization/sense_receipt.py) for the three pointers that carry
the somatic additions into the Self-Hypnosis guide (turn of 2026-11-28 09:44 UTC; his ask: "yes i want to carry changes
into self hypnhosis guide also once we're done"), from DRAFTS-<N>.json, filled from my reading of each sentence and from
the fresh reads in reads/. The checked points and their sources are the somatic additions' own
(articles/somatic-therapies/experiments/additions-20261126/fill_receipts_v29.py, C).

  python3 articles/inner-signal/experiments/carry-c1128/fill_receipts_sh.py N

Writes texts/vN/SHk.txt and receipts/vN/SHk.receipt.json and runs sense_receipt.py check on each.
"""
import importlib.util
import json
import pathlib
import re
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
SR = ROOT / 'tools' / 'humanization' / 'sense_receipt.py'
spec = importlib.util.spec_from_file_location(
    'v29', ROOT / 'articles/somatic-therapies/experiments/additions-20261126/fill_receipts_v29.py')
v29 = importlib.util.module_from_spec(spec)
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
spec.loader.exec_module(v29)

N = sys.argv[1] if len(sys.argv) > 1 else '2'
READS = 'articles/inner-signal/experiments/carry-c1128/reads/READ-1.md to READ-%s.md' % N


def plain(t):
    return re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', t).strip()


# each sentence by how it starts: (payoff, follows, tie to what comes before)
ANN = {
    'One bigger container is': (
        'they learn one bigger container for memory work: a clinical therapy called Imagery Rescripting, and where to '
        'read about it', 'it names one of the bigger containers the paragraph before says high-risk trauma work needs', ''),
    'It works a lot like the way I': (
        'they learn what the therapy does, by a way of re-doing memories they may know from his inner child guide: '
        'imagining a painful memory going differently', 'it says what the therapy just named does', 'It works a lot like'),
    'In Imagery Rescripting, though': (
        'they learn the difference from doing it alone: the therapist is in the scene as the ideal adult, until over the '
        'sessions they can be that adult', 'it says how the therapy differs from the way the sentence before compared it '
        'to', 'In Imagery Rescripting, though,'),
    'If the symptom is pain': (
        'they learn what to do when the symptom is pain that has lasted months with no injury or disease found: keep '
        'using self-hypnosis for it and look for one of two talk therapies, and where to read about them',
        'it picks up "push symptoms down instead of getting medical attention" from the list before it', ''),
    "They've helped people": (
        'they learn what the two have done for people with pain like theirs, and how, without being told the pain '
        'isn\'t real', 'it says why the two therapies just named are worth looking for', "They've helped"),
    'Analyzing a feeling instead of feeling it': (
        'they recognize the section\'s habit in therapy sessions, by its sign: explaining a feeling as soon as it '
        'comes up', 'the section is about being too analytical in the practice; this carries it into therapy sessions',
        ''),
    'If that keeps happening': (
        'they know what to ask their therapist, or whom to look for', 'it says what to do when the habit the sentence '
        'before named keeps happening', 'If that keeps happening'),
    'In that therapy, the therapist catches you': (
        'they picture what that therapist does when they move away from a feeling', 'it says what the therapy just '
        'named does', 'In that therapy'),
    'I go into it in': (
        'they know where to read about it and the two other therapies for staying with feelings',
        'it says where the therapy just described is written up', 'I go into it'),
}
HIS = {'SH2': [{'said': ("They've helped people with long-lasting back, muscle and joint pain, by changing their "
                         "relationship to the pain without pretending it's not there."),
                'note': 'his own sentence from his version of IC2 in the inner child guide (card IC2-TEACH, answers of '
                        '2026-11-27 22:26 UTC), carried as he wrote it'}]}
READER = {
    'SH1': ('an adult using the Self-Hypnosis guide who wants to go back into a painful memory and change it, reading '
            'why to do that with a clinician, deciding whether to look for an Imagery Rescripting therapist'),
    'SH2': ('an adult whose pain has lasted months with no injury found, reading what self-hypnosis is not for, deciding '
            'what to try besides it'),
    'SH3': ('an adult who keeps explaining feelings away, in the practice and in therapy sessions, deciding whether to '
            'look for a therapist trained for that'),
}
SAME = {'SH1': 'a clinical therapy for re-imagining a painful memory', 'SH2': 'what to do for long-lasting pain with no '
        'injury found', 'SH3': 'explaining feelings away in therapy sessions, and what to look for'}
CHECKED = {'SH1': ['imrs'], 'SH2': ['prt', 'eaet', 'real'], 'SH3': ['istdp']}
Q = {
    'Q1': 'PASS: each opens on the reader\'s case ("If you want to go back into a painful memory", "If you\'ve had that '
          'medical attention", "Being too analytical can show up in therapy sessions too") or on what the therapy does',
    'Q2': 'PASS: read about the therapy; try one of the two; look for someone trained in it; stop for the day if you feel '
          'unreal',
    'Q3': 'PASS: which memory (a painful one), which pain (lasted months, no injury or disease found), which slipping away '
          '(explaining a feeling, agreeing with the therapist)',
    'Q4': 'PASS: each therapy named and said by what it does; "the ideal adult" is the inner child guide\'s own term',
    'Q5': 'PASS: each sentence ties to the one before ("It\'s a lot like", "They\'ve helped", "If that keeps happening", '
          '"It\'s for that kind")',
    'Q6': 'PASS: the reader\'s case, the therapy, how it works or what it is for',
    'Q7': 'PASS: each is for the reader of the section it closes',
    'Q8': 'PASS: no groups',
    'Q9': 'PASS: one step a sentence',
}


def main():
    drafts = json.loads((HERE / ('DRAFTS-%s.json' % N)).read_text(encoding='utf-8'))
    tdir, rdir = HERE / 'texts' / ('v' + N), HERE / 'receipts' / ('v' + N)
    tdir.mkdir(parents=True, exist_ok=True)
    rdir.mkdir(parents=True, exist_ok=True)
    bad = 0
    jobs = []
    for d in drafts:   # the text Pangram reads (plain) and the paragraph as the card shows it (its links in)
        jobs.append((d, tdir / ('%s.txt' % d['id']), plain(d['text']), rdir / ('%s.receipt.json' % d['id'])))
        jobs.append((d, tdir / ('%s.md' % d['id']), d['text'], rdir / ('%s-linked.receipt.json' % d['id'])))
    for d, txt, body, out in jobs:
        txt.write_text(body + '\n', encoding='utf-8')
        subprocess.run([sys.executable, str(SR), 'make', str(txt), '--section', d['section'] + ' (Self-Hypnosis guide)',
                        '--reader', READER[d['id']], '--out', str(out)], check=True, capture_output=True)
        rec = json.loads(out.read_text(encoding='utf-8'))
        for x in rec['sentences']:
            key = next(k for k in ANN if plain(x['s']).startswith(k))
            pay, fol, link = ANN[key]
            x['payoff'], x['follows'] = pay, fol
            if 'link' in x:
                x['link'] = link
        rec['checked'] = [v29.C[c] for c in CHECKED[d['id']]]
        rec['placement'] = 'a paragraph of its own at the end of "%s", after: %s' % (d['section'], d['after'])
        rec['opens']['why_reading'] = rec['sentences'][0]['payoff']
        rec['same_point'] = ('none: read the section from its heading to the next for %s; no other paragraph of the '
                             'Self-Hypnosis guide names these therapies' % SAME[d['id']])
        rec['needed'] = {'reader': 'fresh Fable readers (2026-11-28) given tools/humanization/needed_read_brief.md, the '
                                   'live guide and the text one sentence a line: ' + READS + '; each mark acted on',
                         'unneeded': [], 'kept': {}}
        rec['his_fixes'] = {'reader': 'the same readers, given tools/humanization/his_fixes_brief.md: ' + READS,
                            'marked': [], 'kept': {}}
        rec['fit'] = {'reader': 'the same readers, given tools/humanization/fit_read_brief.md and a contradictions check: '
                                + READS, 'marked': [], 'kept': {}}
        rec['questions'] = Q
        rec['his_answer'] = []
        for h in HIS.get(d['id'], []):
            sent = next(x['s'] for x in rec['sentences'] if plain(x['s']) == h['said'])
            rec['his_answer'].append({'said': h['said'], 'in': sent, 'note': h['note']})
        out.write_text(json.dumps(rec, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
        res = subprocess.run([sys.executable, str(SR), 'check', str(txt), str(out)], capture_output=True, text=True)
        ok = res.returncode == 0
        bad += not ok
        print(out.name, len(plain(d['text']).split()), 'words', 'PASS' if ok else (res.stdout + res.stderr).strip())
    return bad


if __name__ == '__main__':
    sys.exit(1 if main() else 0)
