"""Section 14 draft v1 (2026-10-16): Emulate round a's call A of the whole section (emu-a/out/s01-emuA.txt, byte for byte from
the laptop, sha256 2c0f528a...), with the preservation keys (preservation-keys.json) and Emulate's meaning slips put back.
Call A kept more of the published meaning than call B, which turned his father's foundation and film into the author's own
("the foundation I started, the film I made") and lost American Commune. Each fix is an exact old -> new pair on one Emulate
paragraph; everything else is Emulate's. The heading stays Joel's. Writes v1.md and v1-fixes.json.
Run from this folder: python3 make_v1.py"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent
emu = [b.strip() for b in re.split(r'\n\s*\n', (HERE / 'emu-a' / 'out' / 's01-emuA.txt').read_text(encoding='utf-8')) if b.strip()]
assert emu[0] == 'Dissolution and Exit' and len(emu) == 8, len(emu)
IDS = ['P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7']
EMU = dict(zip(IDS, emu[1:]))

FIX = {
 'P1': [
  ("It’s something the founders of any institution probably don’t want to talk about while they’re naming it and looking "
   "forward to its harvests, but it needs to be talked about.",
   "Dissolution is something founders probably don’t want to talk about while they’re picking a name for their community "
   "and looking forward to its first harvest, but that’s exactly when it needs to be talked about.",
   'key U1 "dissolution" (the section opens on its subject, not "It", the opener rule of 2026-10-16), "harvest"; '
   '"founders of any institution" widened the published founders of a community; key U2: the published "That is when the '
   'discussion needs to happen" (the timing) was lost in "it needs to be talked about"')],
 'P2': [
  ("If the commune/intentional community/co-op dissolves, what happens to the land, any outside debts, any other property "
   "(buildings, equipment, stores, funds, etc.)? What are the rights of each person at this time?",
   "If the commune dissolves, what happens to the land and any outside debts? What about its buildings, equipment, common "
   "stores or funds? What happens to each member’s agreed rights?",
   'key U3 "agreed": the published "each member\'s agreed rights"; "etc." opened the published closed list; the slashes '
   'named three kinds of group where the article means the commune; split in two so the sentence has no two lists of '
   'three (linter E125, Joel 2026-10-03)'),
  ("Who is responsible for ensuring that everyone has a place to live and food to eat?",
   "More immediately, who is responsible for ensuring that everyone has a place to live and food to eat?",
   'key U4 "immediately": the published "More immediately" puts these duties first'),
  ("Who takes responsibility for making sure people get their meds and/or other care they need? Who makes sure the kids are "
   "taken care of and continue to go to school?",
   "Who takes responsibility for making sure people get their medications and the other care they need? Who keeps childcare "
   "going and makes sure the kids continue to go to school?",
   'key U4 "medications", "childcare"'),
  ("Who takes responsibility for transportation, for record-keeping, for helping people stay in touch with family, for the "
   "animals, for ensuring obligations to the land are met, for other claims on the group’s time/attention/etc., if applicable?",
   "Who takes responsibility for transportation, for the records, for family contact, for the animals, for ensuring "
   "obligations to the land are met, and for any unresolved claims?",
   'key U4 "records", "family contact", "claims": the published "handles unresolved claims"; "claims on the group\'s '
   'time/attention" changed what the claims are')],
 'P3': [
  ("assign a bridge/successor for each function in advance. The institution may not be salvageable, but people’s lives need "
   "to go on.",
   "assign a bridge/successor for each critical function in advance. The institution may not be salvageable, but people "
   "still need breakfast, and basic life shouldn’t depend on reviving the commune.",
   'key U6 "critical"; key U7 "breakfast" (the published "the people still need breakfast", without its "Tuesday", the '
   'weekday tell O11); key U8 "basic", "reviving": the published "continuity of basic life should not depend on resurrecting '
   'the commune"')],
 'P4': [
  ("It’s also a way for a group to end without destroying all the friendships involved, or without people losing their "
   "dignity.",
   "Dissolution terms are also a way for a group to end without turning every friendship into evidence. People may leave "
   "hurt, but they keep the transition support they agreed on, and their dignity. And they can tell a coherent story of what "
   "happened.",
   'key U9 "dissolution terms", "evidence" (the published "without turning every friendship into evidence"; "destroying" '
   'lost the picture of friendships turned into a case file); key U10 "hurt", "support", "story". The published list of '
   'three (support, dignity, story) is split the way Joel splits his: the third item in its own sentence')],
 'P5': [
  ("Institutions and the relationships that make them up don’t have to die together.",
   "Institutions and the relationships that make them up don’t have to die at the same time.",
   'key U11 "same time"'),
  ("American Commune recently ran an article about two sisters who grew up on The Farm. One of them recently became ill, and "
   "even though the economic institution they were born into had changed dramatically over the years, former members who "
   "hadn’t seen her in years still rallied around her.",
   "American Commune follows two sisters who grew up on The Farm. When one of them later became ill, former members who "
   "hadn’t seen her in years reached out with support. The communal economy they were born into had changed dramatically, "
   "but the bonds hadn’t vanished.",
   'American Commune is a film that follows the sisters, not an article (the published "American Commune follows two '
   'sisters raised at The Farm"); "recently" for the published "later"; key U13 "support"; key U14 "economy", "bonds"')],
 'P6': [
  ("The Bruderhof still impacts my father’s life, the foundation he started, the movie he made, and the places he’s brought "
   "me to, and me, in ways I’m only starting to comprehend.",
   "My father carried the Bruderhof with him long after he left it. It shaped the foundation he started, the film he made, "
   "the places he took me, and the questions I’m still asking.",
   'Joel\'s own lines about his father, his published words back: Emulate made the Bruderhof shape his father\'s life now and '
   'added "in ways I\'m only starting to comprehend"; keys U15 "long after", U16 "film", "questions"')],
 'P7': [
  ("Even if the legal entity dies, the rest of it doesn’t have to.",
   "Even if the legal entity dies, some of what people learned to give one another can go on.",
   'key U17 "learned", "give", "go on": "the rest of it" left a reader asking the rest of what')],
}
log, new = [], {}
for pid in IDS:
    t = EMU[pid]
    for old, new_s, why in FIX.get(pid, []):
        assert t.count(old) == 1, (pid, old)
        t = t.replace(old, new_s)
        log.append({'id': pid, 'source': 'emu-a/out/s01-emuA.txt', 'old': old, 'new': new_s, 'why': why})
    new[pid] = t
out = ['# Dissolution and Exit', '[image 18](https://substackcdn.com/image/fetch/$s_!9Q3c!,f_auto,q_auto:good,fl_progressive:steep/'
       'https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fddd2a051-9ac5-4630-868b-5a37226707f9_1536x1024.png)']
out += [new[p] for p in IDS]
(HERE / 'v1.md').write_text('\n\n'.join(out) + '\n', encoding='utf-8')
(HERE / 'v1-fixes.json').write_text(json.dumps(log, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
for p in IDS:
    print('%s %3d words | %s' % (p, len(new[p].split()), new[p]))
    print()
print(len(log), 'fixes')
