#!/usr/bin/env python3
"""fill_receipts_sr.py - the making-sense receipts for the two fixes the word-for-sense read of 2026-11-28 found in the
somatic guide's live text (turn of 09:44 UTC): his version of a model's text, so the fix is mine to make and test (gate
E373), each a paragraph as it would read (fixes/SR-A2.md, fixes/SR-A3.md).
  python3 articles/somatic-therapies/experiments/additions-20261126/sense-c1128/fill_receipts_sr.py"""
import importlib.util
import json
import pathlib
import re
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[4]
SR = ROOT / 'tools' / 'humanization' / 'sense_receipt.py'
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
spec = importlib.util.spec_from_file_location('v29', HERE.parent / 'fill_receipts_v29.py')
v29 = importlib.util.module_from_spec(spec); spec.loader.exec_module(v29)
REL = 'articles/somatic-therapies/experiments/additions-20261126/sense-c1128/'
READS = (REL + 'out/ (the word-for-sense read: one fresh Fable reader, three planted errors, all found) and ' + REL +
         'READ-SR.md (a fresh Fable reader of the two fixes)')


def plain(t):
    return re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', t).strip()


ANN = {
    'This therapy is a lot like': ('they connect the therapy to the way of re-doing memories they may know from his inner '
                                   'child guide', 'it opens the section on what the therapy is like', ''),
    "Instead of EMDR's mechanical approach": ('they learn what the therapist does, and how it differs from EMDR in the '
                                              'section before', 'it says how the therapy just compared works',
                                              "Instead of EMDR's"),
    'Then you learn to do that yourself': ('they know it ends with them doing it', 'it says what comes after the '
                                           'therapist\'s part', 'Then'),
    'Because rescripting takes you back': ('they know the same care as for EMDR applies', 'it sets the therapy beside '
                                           'EMDR again, for its risk', 'Because'),
    "I haven't found a trial comparing": ('they know no trial says which of the two is better',
                                          'after both trials, it says what they don\'t show', ''),
    'So if your pain seems tied to stress': ('they know which therapy to start with, by their own pain',
                                             'with no trial to choose by, it says how to choose', 'So'),
    "I'd also ask a therapist where they trained": ('they know how to vet a therapist and track the therapy',
                                                     'it adds what to do once they have chosen', "I'd also"),
}
TEXTS = {
    'SR-A2': dict(section='Imagery Rescripting', checked=['imrs'],
                  reader=('an adult reading the somatic guide\'s memory therapies, deciding whether Imagery Rescripting '
                          'is for them and how it differs from EMDR'),
                  placement='the first paragraph of Imagery Rescripting, live since 27 November; only its second '
                            'sentence changes (a comma for the full stop after "approach")',
                  same='none: read the section from its heading to the next for what the therapy is like and does; each '
                       'is said once'),
    'SR-A3': dict(section="Pain That Won't Quit?", checked=['none', 'prt', 'eaet'],
                  reader=('an adult whose pain has lasted months with no injury found, choosing which of the two '
                          'therapies to start with'),
                  placement='the last paragraph of Pain That Won\'t Quit?, live since 27 November; only its second '
                            'sentence changes ("EAET" and "PRT" for "the second" and "the first")',
                  same='none: read the section from its heading to the next for how to choose between the two; it is '
                       'said once'),
}
Q = {
    'Q1': 'PASS: each sentence opens on what it is about (the therapy, the choice)',
    'Q2': 'PASS: start with one therapy by your own pain; ask where a therapist trained; track how it goes; stop when it\'s '
          'too much and ground yourself',
    'Q3': 'PASS: which therapy (named: "EAET", "PRT"), which therapist (the Imagery Rescripting therapist)',
    'Q4': 'PASS: the short forms were given where each therapy is named in the section',
    'Q5': 'PASS: each sentence ties to the one before ("Instead of", "Then", "Because", "So", "also")',
    'Q6': 'PASS: as the section has it',
    'Q7': 'PASS: each is for the reader of the section',
    'Q8': 'PASS: no groups',
    'Q9': 'PASS: one step a sentence',
}


def main():
    bad = 0
    jobs = []
    for key, t in TEXTS.items():   # the paragraph with its links (the live post) and as Pangram reads it (plain)
        jobs.append((key, t, HERE / 'fixes' / ('%s.md' % key), HERE / 'fixes' / ('%s-linked.receipt.json' % key)))
        jobs.append((key, t, HERE / 'fixes' / ('%s.txt' % key), HERE / 'fixes' / ('%s.receipt.json' % key)))
    for key, t, txt, out in jobs:
        subprocess.run([sys.executable, str(SR), 'make', str(txt), '--section', t['section'], '--reader', t['reader'],
                        '--out', str(out)], check=True, capture_output=True)
        rec = json.loads(out.read_text(encoding='utf-8'))
        for x in rec['sentences']:
            k = next(a for a in ANN if plain(x['s']).startswith(a))
            x['payoff'], x['follows'] = ANN[k][0], ANN[k][1]
            if 'link' in x:
                x['link'] = ANN[k][2]
        rec['checked'] = [v29.C[c] for c in t['checked']]
        rec['placement'] = t['placement']
        rec['opens']['why_reading'] = rec['sentences'][0]['payoff']
        rec['same_point'] = t['same']
        rec['needed'] = {'reader': 'fresh readers (Fable, 2026-11-28): ' + READS + '; nothing a reader needs is lost',
                         'unneeded': [], 'kept': {}}
        rec['his_fixes'] = {'reader': 'a fresh Fable reader given tools/humanization/his_fixes_brief.md: ' + REL +
                                      'READ-SR.md', 'marked': [], 'kept': {}}
        rec['fit'] = {'reader': 'the same reader, given tools/humanization/fit_read_brief.md: ' + REL + 'READ-SR.md',
                      'marked': [], 'kept': {}}
        rec['questions'] = Q
        rec['his_answer'] = []
        out.write_text(json.dumps(rec, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
        res = subprocess.run([sys.executable, str(SR), 'check', str(txt), str(out)], capture_output=True, text=True)
        ok = res.returncode == 0
        bad += not ok
        print(out.name, 'PASS' if ok else (res.stdout + res.stderr).strip())
    return bad


if __name__ == '__main__':
    sys.exit(1 if main() else 0)
