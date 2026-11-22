#!/usr/bin/env python3
"""build_tests.py - turn 35's tests (2026-11-12): his round-34 version carried (lesson bad-trips-2026-11-12a, the sixth fix
in SKILL.md), each written as a whole section for one Pangram check.

- harm-s1: Risk of Harm as it stands after round 34 (his two paragraphs) with the 911 line fixed: it said the reasons his
  paragraph now says ("violence underway, or a situation you cannot safely contain") and "immediate danger" and "medical
  emergency" twice; what is left says which number, plainly (W003's and W004's keys kept).
- oral-s1: Recent Oral Toxic Ingestion (h42a: AI Generated, 100%, bb092688) with his moves carried: the point and its bar
  first, the list of body states pictured with "etc.", plain words with the term in an aside, the reader's judgment.

  python3 build_tests.py      write TEST-*.txt
"""
import hashlib
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
HIS_P1 = ("You can sit through a lot with someone, but the moment you think they might hurt themselves or anybody else, get "
          "urgent help. It doesn't have to be a proven death wish. They might just start heading out the door and get lost, "
          "hit by a car, drown, fall off a cliff, etc. Another cue to get help is if they start acting delusional.")
HIS_P2 = ("If their body is flashing warning signs like severe overheating (not just regular sweating), severe insomnia, or "
          "trouble breathing, or if for whatever reason you feel like this is more than you can handle, reach out.")
NEW_911 = ("In the United States, call 911 when someone's in immediate danger or it's a medical emergency, and also if "
           "there's a weapon or a crime in progress. If it's a mental-health crisis and nobody's in physical danger right "
           "now, 988 can help you calm things down and find local help. Anywhere else, look up your local emergency services "
           "number and a crisis line before you ever need them.")
OLD_911 = ("Use local emergency services for immediate danger or a medical emergency. In the United States, 988 can provide "
           "mental-health crisis guidance, de-escalation, and connection to local resources when no immediate physical "
           "emergency exists. Call 911 for immediate danger, a crime in progress, medical emergency, weapon, violence "
           "underway, or a situation you cannot safely contain. Outside the United States, identify the local emergency "
           "number and crisis line before you ever need them.")
TESTS = {
    'harm-s1': "Risk of Harm: When Peer Support Isn't Enough\n\n" + HIS_P1 + "\n\n" + HIS_P2 + "\n\n" + NEW_911,
    'oral-s1': ("Recent Oral Toxic Ingestion\n\n"
                "Before you pick a remedy for an \"overdose\", find out what they actually swallowed, how much and when, "
                "because that word alone doesn't tell you much. Then look at what their body is doing. Slow, shallow "
                "breathing (respiratory depression) is a different problem from a racing stimulant high, and both are "
                "different from serotonin toxicity, a seizure, dangerous overheating, etc., so each gets its own remedy.\n\n"
                "Activated charcoal can help if they swallowed something recently that charcoal binds to, as long as "
                "they're awake enough to swallow safely. It won't bind every toxin, and it can soak up medicine they "
                "need. And if they're vomiting, sedated, seizing or too out of it to protect their airway, "
                "there's a real aspiration risk, meaning they could breathe it into their lungs. Clinical review.\n\n"
                "Poison control can be useful when you're not sure what the substance or combination does, or whether "
                "there's a delayed risk, and they can tell you whether charcoal would be of any value. I don't treat "
                "calling them as a "
                "mandatory ritual, though, since how useful they are depends on the country and on whoever picks up. "
                "They're there to help you decide, and the first aid is still yours to do."),
}

if __name__ == '__main__':
    for k, t in TESTS.items():
        (HERE / ('TEST-%s.txt' % k)).write_text(t + '\n', encoding='utf-8')
        print(k, len(t.split()), 'words', hashlib.sha256(t.encode('utf-8')).hexdigest()[:12])
    # the paragraphs by themselves first (E343: a section whose last check read AI is narrowed before it is checked again)
    for k, (unit, a, b) in {'harm-p911': ('harm-s1', 4, 4), 'oral-p1': ('oral-s1', 2, 2), 'oral-p2': ('oral-s1', 3, 3),
                            'oral-p3': ('oral-s1', 4, 4)}.items():
        blocks = TESTS[unit].split('\n\n')
        t = '\n\n'.join(blocks[a - 1:b])
        (HERE / ('TEST-%s.txt' % k)).write_text(t + '\n', encoding='utf-8')
        print(k, len(t.split()), 'words', hashlib.sha256(t.encode('utf-8')).hexdigest()[:12])
