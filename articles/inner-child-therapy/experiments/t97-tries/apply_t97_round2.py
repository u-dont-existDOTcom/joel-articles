#!/usr/bin/env python3
"""Turn 97, after the second API round (experiments/t97-api/API-CHECKS.md, checks t97b_*):
- How Much Happiness P2 and P3: my tries read worse (High windows where the old text had Low), so the old text is back.
- Related Clinical Work: my wording of Joel's last line reads 100% Human with its section (t97b_related_try). This script
  put it in; the owner-edit check then failed (entry appendix-first-person-pending-20261018 holds his line from his published
  guide), so his line went back the same turn and my wording waits for him (question 89).
- The Parent You Inherited P4 and Stays Shallow: my tries stay (each reads less AI than before), and their notes get the result.
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parents[1] / 'HUMANIZED-ARTICLE-SO-FAR.md'
D = HERE / 'drafts'
import importlib.util  # noqa: E402
spec = importlib.util.spec_from_file_location('t', HERE / 'apply_t97_tries.py'); T = importlib.util.module_from_spec(spec); spec.loader.exec_module(T)
OLD = {draft: old for old, draft, _ in T.TRIES}
REL_OLD = "This framework developed through the teachers and collaborators credited below and my own practice. Later revisions also compare notes with schema therapy, compassion-focused therapy, attachment repair, motivational interviewing, mentalizing, metacognitive therapy, behavioral activation, radically open DBT, emotion-focused therapy and spiritually integrated psychotherapy. I borrow particular distinctions and practices rather than presenting the whole synthesis as their consensus."
R = 'experiments/t97-api/API-CHECKS.md'


def text(draft):
    return (D / draft).read_text(encoding='utf-8').strip()


def main():
    s = ART.read_text(encoding='utf-8')
    def once(old, new):
        nonlocal s
        if s.count(old) != 1:
            sys.exit('not exactly once (%d): %r' % (s.count(old), old[:80]))
        s = s.replace(old, new)
    # How Much Happiness P2 and P3: the old text back, the note says why.
    for draft, why in (('e02-happy-P2.txt', 'Low, Low, Medium and High'), ('e03-happy-P3.txt', 'High, Medium and High')):
        note_start = s.index('Draft %s (experiments/t97-tries/drafts/). Not yet checked in Pangram. -->' % draft[:3])
        once('Draft %s (experiments/t97-tries/drafts/). Not yet checked in Pangram. -->' % draft[:3],
             'Draft %s (experiments/t97-tries/drafts/). Checked in the h1 (%s, check t97b_happy_try): it read %s, worse than the old text\'s Low, so the old text is back. The h1 has used its two checks; it goes to Joel (question 88). -->' % (draft[:3], R, why))
        once('-->\n\n' + text(draft) + '\n', '-->\n\n' + OLD[draft] + '\n')
    # The Parent You Inherited P4 and Stays Shallow: results in their notes.
    once('Draft e01 (experiments/t97-tries/drafts/). Not yet checked in Pangram. -->',
         'Draft e01 (experiments/t97-tries/drafts/). Checked in its section (%s, check t97b_parent, try 1 of 2): Medium 20 on its first sentence, Low 22 on its second, Human on the rap sheet and the comfort, Low 27 on its last; the section read 58%% AI, with windows in every paragraph. My third try, so it goes to Joel (question 88). -->' % R)
    once('Draft e05 (experiments/t97-tries/drafts/). Not yet checked in Pangram. -->',
         'Draft e05 (experiments/t97-tries/drafts/). Checked in its section (%s, check t97b_shallow, try 2 of 2): 27%% AI, down from 59%%; still AI: his night line with my next sentence (Medium 36) and "Then this is probably you." (Low 5); the rest reads Human. The section has used its two checks; it goes to Joel (question 88). -->' % R)
    # Related Clinical Work: my wording of his last line goes in.
    once('\n' + REL_OLD + '\n',
         '\n<!-- Turn 97 (his message of 2026-10-22 23:54 UTC: 87, "you can learn and try"): his last line, "I borrow particular distinctions and practices rather than presenting the whole synthesis as their consensus.", read AI (Low 15) with its section (%s, check t97_related). My wording of it, plain and joking, reads 100%% Human with its section (check t97b_related_try). It is my wording of his line, for him to keep or undo (question 89). Draft e06 (experiments/t97-tries/drafts/). -->\n\n' % R + text('e06-related-P1.txt') + '\n')
    ART.write_text(s, encoding='utf-8')
    print('done: Happiness P2 and P3 back; Related Clinical Work in; notes for P4 and Stays Shallow')


if __name__ == '__main__':
    main()
