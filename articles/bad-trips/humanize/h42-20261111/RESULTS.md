# The guide as it stands after round 33, in Pangram (2026-11-11, batch h42a)

Pangram's web app on his account (Pangram Professional), each unit typed as its text file in `pass/units/` (SHA-256 checked before each click), its prediction in `../pangram-ledger.jsonl` first (`pass/write_predictions.py`). A unit is a section, or a run of one (at most about six paragraphs). Each window: its label, Pangram's confidence (High, Medium or Low) and its words.

**Totals:** 50 units, 49 checked; 8 read Human High in every window, 5 have a Medium window, 3 a Low window, 33 an AI window.

| unit | section | words | result | windows (label, confidence, words) | link |
|---|---|---|---|---|---|
| h42-01 | Inner Signal App to the Rescue! | 73 | Human Written, 0% AI | Human High 80 | [fe0670df](https://www.pangram.com/history/fe0670df-012c-4688-930a-1bc8ffbfbe65) |
| h42-02 | When to Bring In Outside Help / Call medics for: | 184 | AI Generated, 100% AI | AI-Generated High 187 | [a491b633](https://www.pangram.com/history/a491b633-dc0d-44b6-bdf1-7584860063b4) |
| h42-03 | Risk of Harm: When Peer Support Isn't Enough | 138 | AI Generated, 100% AI | AI-Generated High 141 | [44d2df44](https://www.pangram.com/history/44d2df44-70d3-40a7-95ec-b59dc7743cd7) |
| h42-04 | Who to Contact, and When | 201 | AI Detected, 96% AI | AI-Generated High 60, AI-Generated Medium 4, AI-Generated Low 2, AI-Generated High 62, AI-Generated Medium 2, AI-Generated High 10, AI-Generated Medium 31, AI-Generated Low 18, AI-Generated Low 29 | [eaea5237](https://www.pangram.com/history/eaea5237-3875-4885-bf38-ce7f596d0301) |
| h42-05 | Acute Medical and Neurological Rescue | 150 | AI Generated, 100% AI | AI-Generated Low 10, AI-Generated Medium 15, AI-Generated High 130 | [0df121e8](https://www.pangram.com/history/0df121e8-abda-428e-aa4f-a93887e4bf18) |
| h42-06 | If Someone Says "My Brain Feels Damaged": DMSO + Humic Acid First | 480 | AI Detected, 65% AI | AI-Generated High 57, Human Medium 14, Human High 35, AI-Generated Low 26, AI-Generated Medium 8, AI-Generated High 37, Human Low 20, AI-Generated High 55, AI-Generated Medium 14, AI-Generated High 40, Human High 75, Human Medium 2, Human High 24, Human Medium 12, AI-Generated Low 7, Human Low 13, AI-Generated High 53 | [4076db14](https://www.pangram.com/history/4076db14-325a-4854-88b1-fc3c82da040a) |
| h42-07 | Active Seizure (1 of 2) | 451 | AI Detected, 31% AI | AI-Generated Low 5, AI-Generated High 54, AI-Generated Medium 11, AI-Generated High 62, Human Medium 44, Human High 300 | [6280b126](https://www.pangram.com/history/6280b126-8af7-4def-9ae2-f8d11b722990) |
| h42-08 | Active Seizure (2 of 2) | 219 | Human Written, 0% AI | Human High 208, Human Low 20 | [a9e74179](https://www.pangram.com/history/a9e74179-83f2-4805-be65-b8057c632bbc) |
| h42-09 | MDMA: Jaw Tension Is the Magnesium Alarm | 424 | AI Detected, 96% AI | AI-Generated High 66, AI-Generated Medium 7, AI-Generated Low 31, AI-Generated Low 39, AI-Generated Low 15, AI-Generated High 50, AI-Assisted Low 37, AI-Generated High 187 | [08beb99e](https://www.pangram.com/history/08beb99e-4d7b-45b4-ac6f-32c9bfe3823a) |
| h42-10 | Chest Pain and Injury | 162 | AI Detected, 78% AI | Human Low 42, AI-Generated Medium 7, AI-Generated High 118 | [ce00d5dc](https://www.pangram.com/history/ce00d5dc-1e58-4c03-9b82-628409d40764) |
| h42-11 | Recent Oral Toxic Ingestion | 142 | AI Generated, 100% AI | AI-Generated High 142 | [bb092688](https://www.pangram.com/history/bb092688-faa8-46b1-9b14-b124951061eb) |
| h42-12 | Suspected Serotonin Syndrome (SS) | 500 | AI Generated, 100% AI | AI-Generated High 512 | [4a5da2d5](https://www.pangram.com/history/4a5da2d5-a8b4-44f4-87d1-b86df0781db3) |
| h42-13 | My Acute Rescue Hierarchy of Remedies | 172 | AI Detected, 78% AI | Human High 39, AI-Generated Low 9, AI-Generated High 49, AI-Generated Medium 8, AI-Generated High 74 | [6a03a533](https://www.pangram.com/history/6a03a533-0f18-4bc3-9048-75089ac30fd3) |
| h42-14 | Some Remedies Require More Caution | 175 | AI Detected, 85% AI | Human Low 16, AI-Generated Low 29, AI-Generated Low 46, AI-Generated Medium 16, AI-Generated Low 36, AI-Generated Medium 9, AI-Generated Low 11, AI-Generated Low 19 | [495edcec](https://www.pangram.com/history/495edcec-8d7a-4798-b2bb-c9fd2af8da8f) |
| h42-15 | Gut-Toxin and Parasite-Die-Off Tools (1 of 2) | 278 | AI Detected, 77% AI | AI-Generated High 36, AI-Assisted Low 40, AI-Assisted Medium 12, AI-Assisted Low 44, AI-Generated Low 9, AI-Generated High 15, AI-Generated Medium 30, AI-Generated Low 18, AI-Generated Medium 10, AI-Generated Low 11, AI-Assisted Medium 24, AI-Assisted Low 8, AI-Generated Low 19, AI-Generated High 15 | [4b5386d5](https://www.pangram.com/history/4b5386d5-d1c3-4b5c-9755-c2a13f9e80d3) |
| h42-16 | Gut-Toxin and Parasite-Die-Off Tools (2 of 2) | 139 | AI Detected, 98% AI | AI-Generated High 39, AI-Generated Medium 9, AI-Generated Low 13, AI-Generated Low 6, AI-Generated High 75 | [d059a498](https://www.pangram.com/history/d059a498-054a-41a0-aa91-cca1e3df74b5) |
| h42-17 | Nausea Smoothers When the Person Wants to Preserve the Trip | 101 | Human Written, 0% AI | Human High 76, Human Medium 6, Human Low 22 | [1c9fc7f4](https://www.pangram.com/history/1c9fc7f4-9af7-44f1-9892-8f51bcd71352) |
| h42-18 | Mental Stabilizers That Don't Abort the Trip (1 of 6) | 212 | Human Written, 0% AI | Human High 218 | [02a81218](https://www.pangram.com/history/02a81218-6e32-4d9f-aaa2-d721517a85ce) |
| h42-19 | Mental Stabilizers That Don't Abort the Trip (2 of 6) | 332 | AI Detected, 36% AI | Human High 91, AI-Generated Medium 27, AI-Generated High 15, AI-Generated Medium 14, AI-Generated Low 14, Human Low 19, Human High 49, Human Medium 28, AI-Generated Low 2, AI-Generated Low 37, AI-Generated Low 7, Human Low 16, Human Low 11, Human Medium 10 | [793cb8f9](https://www.pangram.com/history/793cb8f9-1fd7-4398-9c9f-dda17f7a9f86) |
| h42-20 | Mental Stabilizers That Don't Abort the Trip (3 of 6) | 159 | AI Detected, 25% AI | Human High 102, AI-Generated Medium 15, AI-Generated High 20, Human High 32 | [d7a8b41d](https://www.pangram.com/history/d7a8b41d-bd9c-4c20-b19d-8e3eeea26add) |
| h42-21 | Mental Stabilizers That Don't Abort the Trip (4 of 6) | 276 | Human Written, 0% AI | Human High 285 | [32203fed](https://www.pangram.com/history/32203fed-6434-4ff0-bfc9-c2b0bf832aca) |
| h42-22 | Mental Stabilizers That Don't Abort the Trip (5 of 6) | 287 | AI Detected, 16% AI | Human High 21, Human Medium 7, Human High 54, Human Medium 10, Human Low 18, AI-Generated Low 19, AI-Generated Low 6, AI-Generated Medium 17, Human High 134, Human Medium 11 | [ba7e33a5](https://www.pangram.com/history/ba7e33a5-23c2-4c86-b9e7-fb7299be8dc7) |
| h42-23 | Mental Stabilizers That Don't Abort the Trip (6 of 6) | 234 | AI Detected, 79% AI | AI-Generated Low 29, AI-Generated High 13, AI-Generated Medium 7, AI-Generated Low 6, AI-Generated Medium 37, AI-Generated High 38, AI-Generated Low 17, AI-Generated Medium 27, AI-Generated High 16, Human Low 33, Human Low 20 | [dbfabf7b](https://www.pangram.com/history/dbfabf7b-4a9c-401d-9469-006de717378b) |
| h42-24 | When the Goal Is to Stop a Psychedelic Trip (1 of 2) | 234 | AI Detected, 73% AI | Human High 31, AI-Generated Low 39, AI-Assisted Low 46, AI-Generated Low 38, AI-Generated Medium 9, AI-Generated Low 23, AI-Assisted Low 17, AI-Generated Low 26, AI-Generated Low 12 | [6d2b162d](https://www.pangram.com/history/6d2b162d-1b31-4462-bf03-6dea64df89ef) |
| h42-25 | When the Goal Is to Stop a Psychedelic Trip (2 of 2) | 228 | AI Detected, 13% AI | Human High 12, Human Medium 18, Human High 94, Human Medium 23, Human Low 6, Human Low 17, Human Medium 22, Human Low 11, AI-Generated High 32 | [523d93cd](https://www.pangram.com/history/523d93cd-4dd9-4c48-8c46-bcd434e9d3af) |
| h42-26 | Tripsitting Yourself or Others | 76 | Human Written, 0% AI | Human High 77 | [7a02f9c5](https://www.pangram.com/history/7a02f9c5-c07c-42e2-b0de-d3c067124f02) |
| h42-27 | Psychological First Aid: The First Five Minutes (1 of 2) | 322 | Human Written, 0% AI | Human High 78, Human Medium 11, Human High 240 | [71e9dd23](https://www.pangram.com/history/71e9dd23-ae2b-48bc-a606-78f33f1e5c1e) |
| h42-28 | Psychological First Aid: The First Five Minutes (2 of 2) | 275 | Human Written, 0% AI | Human High 286 | [afed525e](https://www.pangram.com/history/afed525e-73c5-4d0d-b8ab-29570f172b51) |
| h42-29 | Grounding Menu: Choose One or Two Things (1 of 2) | 198 | AI Generated, 100% AI | AI-Generated High 137, AI-Generated Medium 26, AI-Generated High 33 | [9025d2b1](https://www.pangram.com/history/9025d2b1-52b3-4656-86d2-d843a7d970c7) |
| h42-30 | Grounding Menu: Choose One or Two Things (2 of 2) | 144 | Human Written, 0% AI | Human Medium 6, Human High 83, Human Medium 8, Human High 12, Human Medium 11, Human Low 29 | [ea7a2215](https://www.pangram.com/history/ea7a2215-f9de-4b7c-b35b-dc5091ec7037) |
| h42-31 | Get One Human Anchor | 228 | AI Generated, 100% AI | AI-Generated High 50, AI-Generated Medium 8, AI-Generated High 104, AI-Generated Medium 1, AI-Generated High 75 | [5732b48d](https://www.pangram.com/history/5732b48d-9efb-4ff1-9c06-db5edcdb22f4) |
| h42-32 | For the Person Helping: Calm Anchor, Not Guru (1 of 2) | 194 | AI Generated, 100% AI | AI-Generated High 104, AI-Generated Medium 2, AI-Generated High 59, AI-Generated Medium 1, AI-Generated High 35 | [96ae4fdc](https://www.pangram.com/history/96ae4fdc-a0dd-4ef1-9a7a-dbfab8db5048) |
| h42-33 | For the Person Helping: Calm Anchor, Not Guru (2 of 2) | 246 | AI Generated, 100% AI | AI-Generated High 258 | [b37b776e](https://www.pangram.com/history/b37b776e-bbda-46e4-8ecb-e5f82130d88e) |
| h42-34 | No Rash Actions: Visions Are Not Commands | 246 | AI Generated, 100% AI | AI-Generated High 89, AI-Generated Low 29, AI-Generated High 138 | [0e72d245](https://www.pangram.com/history/0e72d245-bd64-4325-83b9-9648e45bc722) |
| h42-35 | When the Trip Feels Amazing: Euphoric Certainty | 87 | AI Generated, 100% AI | AI-Generated High 87 | [b6755001](https://www.pangram.com/history/b6755001-0369-4870-803f-ffc37a6c73f0) |
| h42-36 | Shadow Work | 84 | Human Written, 0% AI | Human High 32, Human Medium 5, Human High 52 | [236a3091](https://www.pangram.com/history/236a3091-6841-4e3a-a5fc-9642b12637e1) |
| h42-37 | Dealing With Sorrow: Missing Versus Sending Love | 213 | AI Detected, 65% AI | Human High 41, Human Medium 2, Human High 4, Human Medium 22, AI-Generated Low 5, AI-Generated High 28, AI-Generated Low 4, AI-Generated Low 40, AI-Generated Low 36, AI-Generated High 25, AI-Generated Low 11 | [8d71284e](https://www.pangram.com/history/8d71284e-ebc1-438b-bc33-dd8e81787a21) |
| h42-38 | Hand on Heart and Gratitude 🫶🏿 | 211 | AI Generated, 100% AI | AI-Generated High 70, AI-Generated Medium 6, AI-Generated High 33, AI-Generated Medium 7, AI-Generated High 22, AI-Generated Medium 8, AI-Generated High 68 | [64194b97](https://www.pangram.com/history/64194b97-a5dc-4765-9fef-db8717a55b89) |
| h42-39 | Demons, Jinn, Entities, and Shadow Forces | 294 | AI Generated, 100% AI | AI-Generated High 31, AI-Generated Low 3, AI-Generated Medium 60, AI-Generated High 204 | [c00df5c7](https://www.pangram.com/history/c00df5c7-b129-47a7-9c16-a30ebfb3eae4) |
| h42-40 | Abuse Memories, Recovered Memories, and Certainty | 125 | AI Generated, 100% AI | AI-Generated High 132 | [0fa4603f](https://www.pangram.com/history/0fa4603f-d3a0-43f8-80eb-c7a3f9631679) |
| h42-41 | Dealing With Shadow Thoughts | 610 | Mostly Human Written, 8% AI | Human Low 65, Human Low 7, Human Low 19, Human High 21, Human Medium 30, Human Low 13, AI-Generated Low 23, AI-Generated Low 20, Human Medium 9, Human High 415, Human Medium 1 | [a9528123](https://www.pangram.com/history/a9528123-9665-4a17-bef1-4a5c2d172908) |
| h42-42 | (Re)defining "Bad Trip" | 221 | Human Written, 0% AI | Human High 158, Human Medium 17, Human High 16, Human Medium 9, Human High 17, Human Medium 10 | [4972cd65](https://www.pangram.com/history/4972cd65-cf59-4a3c-878d-0a877f11d012) |
| h42-43 | Spiritual ≠ "Getting Your Ass Kicked" | 120 | AI Generated, 100% AI | AI-Generated High 113, AI-Generated Medium 10 | [185ae3d5](https://www.pangram.com/history/185ae3d5-3056-4e5e-a41f-eb3fc5d1f8a1) |
| h42-44 | The Other Bypass: Feeling Good Forever | 193 | Human Written, 0% AI | Human High 200 | [6ab5dc24](https://www.pangram.com/history/6ab5dc24-1554-4c0e-8df7-f1d734c0acfd) |
| h42-45 | After the Storm | 215 | AI Detected, 78% AI | AI-Generated High 35, AI-Generated Medium 9, AI-Generated Low 18, Human Low 25, Human Low 18, AI-Generated Medium 7, AI-Generated High 41, AI-Generated Medium 26, AI-Generated High 40 | [53464de3](https://www.pangram.com/history/53464de3-daea-4cf1-8ef3-191f1c48d0d8) |
| h42-46 | What Kind of Aftermath Is This? | 567 | Human Written, 0% AI | Human Medium 6, Human High 584 | [78353445](https://www.pangram.com/history/78353445-3765-4e63-9119-00ab5f8f562a) |
| h42-47 | Bring in mental-health support when: | 37 | not checked: 37 words, under the web app's 50-word minimum (its prediction voided; it gets checked with a neighbour after the humanize edits) | | |
| h42-48 | Trip After Trip? Hang up the phone, get off the Healing Treadmill | 605 | Human Written, 0% AI | Human High 620 | [3421bf44](https://www.pangram.com/history/3421bf44-a90b-4a7f-96d6-8c7ca7d52ccf) |
| h42-49 | Planning a Trip or Ceremony? Give It a Beginning and an End | 469 | Human Written, 0% AI | Human High 482 | [de2fd87c](https://www.pangram.com/history/de2fd87c-b98c-466b-ae11-cbdca76fffa5) |
| h42-50 | Appendix: Additional Resources | 266 | Human Written, 0% AI | Human High 31, Human Medium 2, Human High 239 | [eeba7d60](https://www.pangram.com/history/eeba7d60-3ed4-499e-9432-61b828931b46) |

## Every window that isn't Human High

### h42-02, When to Bring In Outside Help / Call medics for: ([result](https://www.pangram.com/history/a491b633-dc0d-44b6-bdf1-7584860063b4))

- AI-Generated (187 words): When to Bring In Outside Help
Call medics for:
Trouble breathing, blue or gray lips, or respiratory depression
A convulsive seizure lasting about five minutes, repeated seizures without normal recovery, or a first or substantially different seizure
Collapse, inability to wake normally, or rapidly worsening consciousness
Dangerous overheating, severe rigidity, or clonus with fever
Sudden one-sided weakness, loss of speech, inability to walk normally, or loss of control of bodily functions
A report that the brain feels damaged when the person cannot complete a basic neurological check or is rapidly worsening
Severe, worsening, radiating, or exertional chest pain--or chest pain with breathlessness, sweating, faintness, neurological changes, or collapse
Serious injury, uncontrolled bleeding, or a possible head or spinal injury
Repeated vomiting, severe dehydration, blood, or severe abdominal pain
Violence, self-harm, or a situation the sitter cannot physically contain
Concerning symptoms after an MAOI, which slows the breakdown of serotonin (some older antidepressants, and the harmalas in ayahuasca and Syrian rue seeds), plus a serotonergic substance, one that raises serotonin, like MDMA or most antidepressants
The remedies below can begin while help is being arranged.

### h42-03, Risk of Harm: When Peer Support Isn't Enough ([result](https://www.pangram.com/history/44d2df44-70d3-40a7-95ec-b59dc7743cd7))

- AI-Generated (141 words): Risk of Harm: When Peer Support Isn't Enough
Get urgent help when somebody may harm themselves or another person, cannot be kept physically safe, is moving toward roads, water, or heights, has command voices or fixed terrifying beliefs driving action, becomes violent, is severely confused and unreachable, has dangerous physical symptoms, has lost enough sleep that judgment is collapsing, or exceeds what the sitter can safely contain.
Use local emergency services for immediate danger or a medical emergency. In the United States, 988 can provide mental-health crisis guidance, de-escalation, and connection to local resources when no immediate physical emergency exists. Call 911 for immediate danger, a crime in progress, medical emergency, weapon, violence underway, or a situation you cannot safely contain. Outside the United States, identify the local emergency number and crisis line before you ever need them.

### h42-04, Who to Contact, and When ([result](https://www.pangram.com/history/eaea5237-3875-4885-bf38-ce7f596d0301))

- AI-Generated (60 words): Who to Contact, and When
Save the relevant links and local numbers before you need them. Their hours and services change, and some only work in one country.
During or soon after a psychedelic experience
Fireside Project: U.S.-only according to its current FAQ; phone or text psychedelic peer support at 623-473-7433, daily from 11 a.m.
- AI-Generated (4 words): to 11 p.m.
- AI-Generated (2 words): Pacific Time.
- AI-Generated (62 words): TripSit live chat: a harm-reduction chat you open in your browser, for people using drugs and for whoever's looking after them.
Global crisis and emotional-support directories
Find A Helpline: a global directory of free helplines, many offering phone, text, online chat, or WhatsApp. It is not psychedelic-specific, but it can put a human on the other end quickly.
- AI-Generated (2 words): U.S.
- AI-Generated (10 words): crisis chat and text
988 Suicide & Crisis Lifeline: U.S.
- AI-Generated (31 words): call, text, and chat for suicidal or mental-health crises.
Crisis Text Line: U.S. text, chat, and WhatsApp support, with partner text lines listed for Canada, the UK, and Ireland.
- AI-Generated (18 words): Integration and post-experience support
ICEERS Support Center: up to five free online integration sessions for challenging experiences.
- AI-Generated (29 words): CPEP online peer group: a free confidential monthly group for post-psychedelic difficulties.
Cheetah House: resources, consultations, and support groups for meditation-related difficulties, including chat-based peer support.

### h42-05, Acute Medical and Neurological Rescue ([result](https://www.pangram.com/history/0df121e8-abda-428e-aa4f-a93887e4bf18))

- AI-Generated (10 words): Acute Medical and Neurological Rescue
An emergency means act now.
- AI-Generated (15 words): It does not always mean that an ambulance is the first or only useful action.
- AI-Generated (130 words): Some severe but physically stable altered states may respond faster to field rescue than to hours in an emergency room.
When the person is breathing normally, not dangerously hot, not seizing, has no neurological-injury concern, remains conscious enough to cooperate, and can be kept physically safe, calming and stabilizing the trip may be enough.
The emergency room is not magic, and for a physiologically stable psychedelic or practice-induced crisis it may be a poor environment. A scared, psychotic-feeling person often receives a benzodiazepine; those drugs don't reliably address psychosis and can cause paradoxical agitation or fear in some people. Antipsychotics may work better for psychosis, but they carry their own risks and interactions, often administered by someone who doesn't know what was taken, if anything.

### h42-06, If Someone Says "My Brain Feels Damaged": DMSO + Humic Acid First ([result](https://www.pangram.com/history/4076db14-325a-4854-88b1-fc3c82da040a))

- AI-Generated (57 words): If Someone Says "My Brain Feels Damaged": DMSO + Humic Acid First
Do not dismiss that report because the person is high or cannot explain it in clinical language. It may be anxiety or excessive psychedelic intensity. It may also be acute neurological dysfunction, and the person experiencing it may be the least able to describe it neatly.
- AI-Generated (26 words): While using DMSO, check wakefulness, breathing, temperature, speech, facial symmetry, both arms, balance, walking, bodily control, seizure activity, severe headache, repeated vomiting, chest pain, and vision.
- AI-Generated (8 words): These checks include several recognized stroke warning signs.
- AI-Generated (37 words): A person who cannot answer or cooperate has not passed the screen; their neurological status is still unknown. If the screen is reassuring but the brain-damage feeling remains, continue the DMSO-first route and reassess promptly.
- AI-Generated (55 words): That judgment is stronger than the clinical evidence, but the evidence is not empty: a preliminary human ischemic-stroke trial reported possible neurological benefit; a small human series used DMSO for intracranial hypertension; and animal stroke research found substantial infarct reduction even when treatment began after ischemia. DMSO also suppresses NMDA- and AMPA-mediated excitotoxicity.
- AI-Generated (14 words): For objective stroke-like signs, I would use DMSO immediately while someone calls medics.
- AI-Generated (40 words): DMSO cannot identify whether the problem is a clot, a hemorrhage, low oxygen, an electrolyte crisis, or something else. The larger adjacent risk is losing a treatment window or missing a bleed because the symptoms improved enough to feel reassuring.
- AI-Generated (7 words): Do not manufacture reassurance from missing information.
- AI-Generated (53 words): At this point safety matters more than preserving the experience.
If this is MDMA, move to magnesium chloride and the broader electrolyte branch instead.
Bring in medical help in parallel for objective neurological signs, dangerous heat, prolonged or repeated seizure, breathing trouble, severe chest pain, collapse, or when basic stability cannot be established.
- Human Medium (14 words): DMSO is my first immediate remedy while I ask what the symptoms actually are.
- Human Low (20 words): I believe DMSO works better for stroke and most acute brain damage than anything else readily available to ordinary people.
- Human Medium (2 words): DMSO immediately.
- Human Medium (12 words): Ask what the symptoms actually are while the DMSO is being used.
- Human Low (13 words): If this is a psychedelic, use Ipomoea pes-caprae to stop the trip.

### h42-07, Active Seizure (1 of 2) ([result](https://www.pangram.com/history/6280b126-8af7-4def-9ae2-f8d11b722990))

- AI-Generated (5 words): Active Seizure
Time the seizure.
- AI-Generated (54 words): Protect the person from injury, clear dangerous objects, loosen tight clothing, and place them on their side when practical. Don't restrain them and don't put anything in their mouth while they are convulsing or not fully conscious.
If an appropriate rapid seizure-rescue benzodiazepine is available, use it by its intended route.
- AI-Generated (11 words): Benzodiazepines are the established first-line drug class for status epilepticus.
- AI-Generated (62 words): An ordinary pill is not the same thing as a nasal, buccal, rectal, intramuscular, or intravenous rescue preparation, and respiratory depressants in the mix change the risk.
Call medics for a convulsive seizure lasting about five minutes, repeated seizures without normal recovery, trouble breathing, dangerous heat, serious injury, a first seizure, or a seizure substantially different from the person's known pattern.
- Human Medium (44 words): What Else May Help: At the Aura, and Alongside Rescue Medicine
Some people get a warning before a seizure takes hold, which is called an aura. That's when the things people report can still stop it, depending on what sets their seizures off.

### h42-09, MDMA: Jaw Tension Is the Magnesium Alarm ([result](https://www.pangram.com/history/08beb99e-4d7b-45b4-ac6f-32c9bfe3823a))

- AI-Generated (66 words): MDMA: Jaw Tension Is the Magnesium Alarm
With MDMA, I treat meaningful jaw tension as the earliest warning that the body needs more magnesium. This comes from repeated field experience rather than a direct clinical trial. Everyone I know who has taken enough magnesium chloride to make the jaw tension fully release has avoided the other complications I have seen when people let that tension continue.
- AI-Generated (7 words): A token dose may not be enough.
- AI-Generated (31 words): On multiple occasions, I have dissolved Dead Sea magnesium chloride hexahydrate flakes in water and taken approximately one gram per minute orally for around twenty minutes before my jaw fully released.
- AI-Generated (39 words): I have tolerated around twenty grams without diarrhea; for me, diarrhea has appeared only above roughly forty grams. Magnesium chloride is also generally less likely to cause diarrhea than several other replacement salts, including forms deliberately used as laxatives.
- AI-Generated (15 words): Interestingly, magnesium taken before the MDMA peak also makes the peak less euphoric for me.
- AI-Generated (50 words): That suggests it may both meet a rapidly increasing magnesium need and directly moderate part of MDMA's excitatory effect. For harm reduction, slightly less euphoria is a reasonable price for a relaxed jaw and what appears in my experience to be a much lower risk of the state escalating.
- AI-Assisted (37 words): My second wife had severe convulsions after an MDMA overdose. At the hospital, her potassium was found to be critically low--described to me as essentially zero--and IV potassium was the only treatment they gave her.
- AI-Generated (187 words): That experience is why I treat serious MDMA toxicity as a broader electrolyte emergency, even though magnesium is the first and most useful early intervention when jaw tension appears.
Jaw tension should also mean no more MDMA, less exertion and heat, and closer monitoring. Worsening headache, confusion, vomiting, weakness, palpitations, collapse, or seizure raises concern about sodium, potassium, temperature, hydration, kidneys, and broader toxicity. MDMA is documented to cause acute kidney injury through several pathways, and controlled research confirms that hyponatremia can occur after a single dose.
People with impaired kidneys do need to be more cautious with large, rapid magnesium doses because they may not clear magnesium normally. But they should be far more worried about the MDMA. MDMA can cause overheating, rhabdomyolysis, dangerous electrolyte shifts, and acute kidney injury. Kidney impairment is a strong reason not to take MDMA--not a reason to sit there with worsening jaw tension after taking it. I would not tell somebody with serious kidney impairment to copy my one-gram-per-minute approach blindly; I would tell them to treat the situation as higher-risk and get help sooner.

### h42-10, Chest Pain and Injury ([result](https://www.pangram.com/history/ce00d5dc-1e58-4c03-9b82-628409d40764))

- AI-Generated (7 words): The cardiovascular science is preclinical but relevant.
- AI-Generated (118 words): In rats, DMSO pretreatment reduced myocardial infarct size by about three quarters and sharply reduced cardiac injury markers. Other work found inhibition of tissue factor, platelet activation, and arterial thrombus formation. Myocardial-ischemia study; tissue-factor and thrombosis study; human platelet study.
Mild, familiar, non-progressive discomfort in a fully alert person is different from new, severe, persistent, worsening, radiating, or exertional pain--or pain with breathlessness, sweating, faintness, neurological changes, or collapse. In the second branch, I would use DMSO while arranging medical evaluation. If you're not sure which branch it is, treat it as the second. DMSO can also block pain signals, so pain relief alone does not prove that the underlying problem has ended.
- Human Low (42 words): Chest Pain and Injury
DMSO is also my first remedy for many injuries and some chest pain. After I overused erythritol, I developed angina that lasted for days. I took DMSO, the pain disappeared within about a minute, and it never returned.

### h42-11, Recent Oral Toxic Ingestion ([result](https://www.pangram.com/history/bb092688-faa8-46b1-9b14-b124951061eb))

- AI-Generated (142 words): Recent Oral Toxic Ingestion
"Overdose" is too vague to choose a remedy. Ask what was swallowed, how much, when, and what the body is actually doing: respiratory depression, stimulant toxicity, serotonin toxicity, seizure, dangerous overheating, cardiovascular symptoms, severe agitation, objective neurological dysfunction, vomiting, diarrhea, or something else.
Activated charcoal may help after some recent oral ingestions when the substance binds to it and the person is fully alert enough to swallow safely. It does not bind every toxin, can adsorb necessary medication, and creates aspiration risk in somebody who is vomiting, sedated, seizing, or unable to protect the airway. Clinical review.
Poison control may be useful when the substance, combination, delayed risk, or value of charcoal is unclear. I do not treat it as a mandatory ritual; usefulness varies by country and by whoever answers. It is decision support, not first aid.

### h42-12, Suspected Serotonin Syndrome (SS) ([result](https://www.pangram.com/history/4a5da2d5-a8b4-44f4-87d1-b86df0781db3))

- AI-Generated (512 words): Suspected Serotonin Syndrome (SS)
Serotonin syndrome overlaps with several symptoms above, but the rescue measures in the other branches do not necessarily treat it. It can follow serotonergic medication changes, combinations, or excessive exposure. Ayahuasca and other MAOI brews, MDMA, DXM, many antidepressants, tramadol, linezolid, other MAOIs, and some opioids can contribute, especially in combinations.
Recognizing serotonin toxicity
Clinicians often use the Hunter criteria. One or more of the following patterns makes serotonin toxicity more likely:
Spontaneous clonus: involuntary rhythmic muscle contractions and relaxations occurring without stimulation.
Inducible clonus plus agitation or sweating.
Ocular clonus plus agitation or sweating: rapid rhythmic involuntary eye movements.
Tremor plus hyperreflexia: shaking together with abnormally brisk reflexes.
Hypertonia plus fever: rigidity with temperature above 38°C (100.4°F), together with ocular or inducible clonus.
This is a recognition aid rather than a command to wait for every criterion before acting. Dangerous heat, rigidity, clonus, confusion, or rapid worsening deserves medical help.
Do this immediately when serotonin toxicity is reasonably suspected:
Stop all suspected serotonergic substances. No more SSRI, SNRI, MAOI, tramadol, MDMA, DXM cough syrup, 5-HTP, St John's wort, SAM-e, linezolid, stimulant redoses, or harmala/ayahuasca-type MAOI exposure.
If the person is fully alert and able to swallow, I would give cyproheptadine early. It antagonizes serotonin receptors. Case reports describe rapid improvement, including complete resolution within two hours in a small series, while a recent systematic review found the evidence for major outcomes inconclusive. Case series; systematic review. I would not wait to see whether it works before cooling, stopping serotonergic substances, and arranging help for moderate or severe signs.
Call emergency help and arrange transport for moderate or severe signs. Don't drive yourself. Poison control may help when the combination is unclear, but it is not the treatment.
Cool the person without delaying transport. Move to a cool room, remove excess clothing, use a fan and cool damp cloths, and place ice packs wrapped in cloth at the neck, armpits, or groin when the person is hot. Don't put a confused, seizing, or very weak person in a bath. Fever reducers do not solve heat generated by extreme muscle activity.
Keep stimulation low and prevent exertion. No pacing to "burn it off," exercise, crowds, or arguments. Akathisia can create a strong urge to move, but muscle activity can worsen heat and rhabdomyolysis risk.
Hydrate only when fully alert and not vomiting. Small sips of an appropriate oral rehydration drink are reasonable. Don't force fluids, food, pills, or charcoal when someone is confused, vomiting, sleepy, or at seizure risk.
Gather the evidence for the ER. Bring pill bottles and packages. Write down exact substances, dose, timing, last dose, recent increases, supplements, recreational drugs, temperature, pulse, and blood pressure when available.
Hospitals may use benzodiazepines, external cooling, IV fluids, monitoring, and intensive supportive care. Niacin is unsafe for serotonin syndrome. DMSO is also not part of this branch. I would consider oral magnesium chloride when the person is fully alert, especially with MDMA-related jaw tension or muscle activity.

### h42-13, My Acute Rescue Hierarchy of Remedies ([result](https://www.pangram.com/history/6a03a533-0f18-4bc3-9048-75089ac30fd3))

- AI-Generated (9 words): Sometimes the mind isn't in a metaphysical crisis.
- AI-Generated (49 words): The body feels awful and the altered mind writes cosmic horror to explain it. Nausea, heat, exhaustion, dehydration, overstimulation, and sleep loss all become spiritual content very quickly.
A horrible thought isn't automatically a revelation. The body may need quiet, water, cooling, warmth, rest, or a calmer room.
- AI-Generated (8 words): The body is part of the spiritual field.
- AI-Generated (74 words): The hierarchy appears before the mystical sections because love doesn't require us to ignore the body.
A trip with diarrhea, nausea, toxic heaviness, a dirty body-feeling, loss of bodily control, jaw tension, neurological disorganization, or the sense that the mind is going crazy because the gut or brain is going crazy belongs in a different branch from a mainly emotional crisis. A gut-driven mental hell is often mistaken as shadow work.

### h42-14, Some Remedies Require More Caution ([result](https://www.pangram.com/history/495edcec-8d7a-4798-b2bb-c9fd2af8da8f))

- AI-Generated (29 words): From the outside that may look manic, and it could destabilize somebody prone to mania or without meditation training. I wouldn't use it casually during a bad trip.
- AI-Generated (46 words): Smelling it does not produce that hyperintelligent state but does feel relaxing and very beneficial for brain health, so I'd start with that.
Cinnamon can produce an intense "brain surgery" or "brain scraping" effect, especially the first time it combines with an ayahuasca-like state.
- AI-Generated (16 words): That may be therapeutic in the right context, but it is not a casual rescue tool.
- AI-Generated (36 words): I would also be extremely careful with Acacia confusa eaten with Mimosa hostilis. For me, that combination produced hellishly intense psychosis-like and autism-like states before transforming into a week of extraordinary creativity and joy.
- AI-Generated (9 words): The later benefit did not make the crisis recommendable.
- AI-Generated (11 words): Iboga--especially male iboga--potentiates many drugs and can be dangerous.
- AI-Generated (19 words): A low amount combined well for me; doubling it became dangerously intense. I include that only as a warning.
- Human Low (16 words): Some Remedies Require More Caution
Humic acid when eaten, can produce a hyperintelligent state for me.

### h42-15, Gut-Toxin and Parasite-Die-Off Tools (1 of 2) ([result](https://www.pangram.com/history/4b5386d5-d1c3-4b5c-9755-c2a13f9e80d3))

- AI-Generated (36 words): Gut-Toxin and Parasite-Die-Off Tools
These are the first things I would use, even preventively on the come-up, because I want to address possible toxins before assigning the distress to something more mysterious.
- AI-Assisted (40 words): Zeolite and Ferment in ZHoly3O
When the trip feels like sick stomach, nausea, diarrhea, toxic heaviness, a dirty body-feeling, parasite die-off, or mental hell driven by gut hell, zeolite and the ZHoly3O ferment are often my first thoughts.
- AI-Assisted (12 words): Many ferments help to different degrees, including kombucha, kimchi, and apple vinegar.
- AI-Assisted (44 words): I prefer fermented beet juice made with apple vinegar and salt. Smelling the ferment helps a lot. Drinking a spoonful can also help, although it may cause itching in somebody who breaks down histamine poorly, which then requires activated charcoal to reduce gut histamine.
- AI-Generated (9 words): Most sober people don't feel much from zeolite.
- AI-Generated (15 words): Its effect becomes more obvious when a trip has a toxic or gut-driven component.
- AI-Generated (30 words): I put a spoonful into water--some people need a teaspoon, others a tablespoon--and sip slowly. Rubbing it on the body or simply holding the jar also helps me.
- AI-Generated (18 words): In my experiments, zeolite has to be prepared correctly. I use powdered zeolite rather than nano-liquid zeolite.
- AI-Generated (10 words): Many products did nothing for me, and quality mattered enormously.
- AI-Generated (11 words): Most zeolites have clogged pores because they haven't been cleaned.
- AI-Assisted (24 words): For my ozonated zeolite, I mix the powder into water and use an ozone-water purifier in a glass vessel because ozone destroys plastic.
- AI-Assisted (8 words): I mean ozonating water, never inhaling ozone gas.
- AI-Generated (19 words): With a machine producing about two grams of ozone per hour, ten minutes produced a working zeolite for me.
- AI-Generated (15 words): Less time did not work as well, and more time did not noticeably improve it.

### h42-16, Gut-Toxin and Parasite-Die-Off Tools (2 of 2) ([result](https://www.pangram.com/history/d059a498-054a-41a0-aa91-cca1e3df74b5))

- AI-Generated (39 words): I also keep zeolite away from metal during preparation. Zeolite adsorbs metals, which is part of why it is used for heavy-metal removal, and I don't want it sitting against a metal vessel or utensil before ingestion.
- AI-Generated (9 words): I use glass for ozonation and storage whenever possible.
- AI-Generated (13 words): Actual Activated Charcoal
Activated charcoal can help gut toxicity, but it adsorbs drugs.
- AI-Generated (6 words): Sometimes that is exactly the point.
- AI-Generated (75 words): It can also flatten or reduce a trip, so I don't treat charcoal and zeolite as interchangeable.
When the goal is to reduce drug absorption or stop a toxic gut situation, charcoal may be relevant. When I want to preserve the trip while improving the gut feeling, I prefer zeolite.
Charcoal can also adsorb medications somebody depends on. I would use it cautiously around necessary medicines and tell the medics if charcoal was taken.

### h42-19, Mental Stabilizers That Don't Abort the Trip (2 of 6) ([result](https://www.pangram.com/history/793cb8f9-1fd7-4398-9c9f-dda17f7a9f86))

- AI-Generated (27 words): It is also my primary emergency neuroprotectant when the problem feels like acute neurological damage, altered consciousness, loss of bodily control, or severe drug-related brain dysfunction.
- AI-Generated (15 words): It overlaps with aged ozonated-charcoal water, but the two don't always work equally.
- AI-Generated (14 words): Sometimes DMSO works better; sometimes the water does. I don't yet know why.
- AI-Generated (14 words): In my experience there is generally no harm in taking both or mixing them.
- AI-Generated (2 words): Sensitivity varies.
- AI-Generated (37 words): Reduced sleep: DMSO reduces how long I sleep when I take too much, take it too late, or use it over too many consecutive days. It builds up past a threshold that seems to differ between people.
- AI-Generated (7 words): In rats, higher doses made sleep lighter.
- Human Low (19 words): Ozonated-charcoal water has what I consider a perfect safety profile; DMSO is a close second in my experience.
- Human Medium (28 words): DMSO can also burn dry mouth tissue, so the mouth should be moist first.
Nausea: when drinking DMSO, dilute it in water, juice, or milk and sip gradually.
- Human Low (16 words): Some people sleep better with DMSO because it reduces whatever symptom had been keeping them awake.
- Human Low (11 words): Body odor: above a certain dose you may smell like sulfur.
- Human Medium (10 words): I don't smell when I put it into milk.

### h42-20, Mental Stabilizers That Don't Abort the Trip (3 of 6) ([result](https://www.pangram.com/history/d7a8b41d-bd9c-4c20-b19d-8e3eeea26add))

- AI-Generated (15 words): Contraindications:
DMSO has produced both anticonvulsant and proconvulsant effects depending on dose and seizure model.
- AI-Generated (20 words): I consider it a plausible adjunct for excitotoxic or temporal-lobe-type seizure activity, not a proven universal seizure rescue.

### h42-22, Mental Stabilizers That Don't Abort the Trip (5 of 6) ([result](https://www.pangram.com/history/ba7e33a5-23c2-4c86-b9e7-fb7299be8dc7))

- AI-Generated (19 words): It has a grounding, cooling, organizing effect different from DMSO, aged ozonated-charcoal water, zeolite, or beach morning glory.
- AI-Generated (6 words): I don't understand the mechanism.
- AI-Generated (17 words): I only know that it has repeatedly felt like a powerful natural remedy for excessive psychedelic intensity.
- Human Medium (7 words): I noticed it in Kenya and Florida.
- Human Medium (10 words): Touching the outside of a bottle doesn't do it.
- Human Low (18 words): Direct contact with the water seems to matter, even when the water has been stored in a bottle.
- Human Medium (11 words): That water doesn't fix the gut the way zeolite does.

### h42-23, Mental Stabilizers That Don't Abort the Trip (6 of 6) ([result](https://www.pangram.com/history/dbfabf7b-4a9c-401d-9469-006de717378b))

- AI-Generated (29 words): Aged ozonated-charcoal water acts more on the crazy or excessively intense mental feeling: too much psychedelic energy, the wrong environment, anxiety, high EMF, or a generally overloaded mind.
- AI-Generated (13 words): It can shift "too much" into calm release without necessarily aborting the trip.
- AI-Generated (7 words): Zeolite usually feels subtle to sober people.
- AI-Generated (6 words): Aged ozonated-charcoal water does not.
- AI-Generated (37 words): Most people I have given it to find it relaxing even while sober, whether they smell it, touch it, or drink the water portion.
I have even watched the water calm a crying baby through touch alone.
- AI-Generated (38 words): No ozone gas was present; this was contact with the water after ozonation had ended and the residual ozone had dissipated. I include that because it suggested the relaxing effect was not only adult expectation or psychedelic context.
- AI-Generated (17 words): Earlier in my experiments, I made the mistake of directly smelling ozone gas during a psychedelic state.
- AI-Generated (27 words): It intensified the experience and became mentally alarming. DMSO didn't help that situation, while aged ozonated-charcoal water helped rapidly. I don't recommend inhaling ozone.
- AI-Generated (16 words): The mistake showed me that DMSO and aged ozonated-charcoal water address different kinds of overload.
- Human Low (33 words): Without an ozone-water purifier--which can cost around $20 on Amazon--boiling water with charcoal gives some of the benefit. Touching or holding shungite can also feel similar to holding cleaned zeolite.
- Human Low (20 words): Shungite pendants are sold on Amazon. Shungite should not be drunk unless it has been properly washed of heavy metals.

### h42-24, When the Goal Is to Stop a Psychedelic Trip (1 of 2) ([result](https://www.pangram.com/history/6d2b162d-1b31-4462-bf03-6dea64df89ef))

- AI-Generated (39 words): The distinction matters. I have tried many related plants and cousins, and they did not work the same way. As far as I know, nobody else sells it.
Its primary role in this guide is not ordinary nausea control.
- AI-Assisted (46 words): In my experience, Ipomoea pes-caprae is the ultimate sledgehammer for stopping a psychedelic trip cold and fast.
A tiny nibble can sometimes smooth psychedelic nausea and improve the trip without killing it, but the difference between that amount and a trip-aborting amount is narrow.
- AI-Generated (38 words): I use it for nausea only when the person is comfortable with the possibility that the trip may end.
Even picking a leaf can affect me when the broken juicy part touches sensitive skin, especially under the fingernails.
- AI-Generated (9 words): Avoiding contact with the broken portion prevents that effect.
- AI-Generated (23 words): A whole leaf can easily end the trip and, in my experience, may prevent tripping for days afterward.
This was not only personal.
- AI-Assisted (17 words): I once gave beach morning glory to a woman experiencing nausea and dysphoria during a psychedelic state.
- AI-Generated (26 words): I was rushing to help and may have given more than I would now. Within a couple of minutes she shifted from miserable to very happy.
- AI-Generated (12 words): That helped convince me the effect wasn't limited to my body.

### h42-25, When the Goal Is to Stop a Psychedelic Trip (2 of 2) ([result](https://www.pangram.com/history/523d93cd-4dd9-4c48-8c46-bcd434e9d3af))

- AI-Generated (32 words): Once the body is stable and those tools have done what they can, fear, grief, memory, certainty, and whatever else the altered mind has opened still need somebody to sit with them.
- Human Medium (18 words): MDMA remains a separate branch centered on magnesium, temperature, sodium, potassium, hydration, serotonin toxicity, seizure, and cardiovascular symptoms.
- Human Medium (23 words): This is normal, although some people find it intolerable and others enjoy it.
Heartburn in sensitive stomachs or after too much at once.
- Human Low (6 words): Drowsiness, usually with terrible sleep quality.
- Human Low (17 words): Higher or repeated doses can create real risk, especially with liver problems, alcohol, medications, or sensitive physiology.
- Human Medium (22 words): Other forms of vitamin B3 seem less reliable for relaxation. Niacinamide sometimes relaxes people and sometimes creates hyperfocus, depending on their state.
- Human Low (11 words): Avoid sustained-release niacin and the useless non-flush hexanicotinate form.

### h42-29, Grounding Menu: Choose One or Two Things (1 of 2) ([result](https://www.pangram.com/history/9025d2b1-52b3-4656-86d2-d843a7d970c7))

- AI-Generated (137 words): Grounding Menu: Choose One or Two Things
Grounding is love becoming practical. Choose one or two options rather than all of them.
A useful order is room → body → human → time → meaning. Most people begin with meaning because the experience feels cosmic.
Body
Put one hand on the heart and one on the solar plexus.
Smell
Scratch & sniff a lime peel, or smell an authentic calming essential oil, the Metta NMT sniffer or humic acid powder (see Mental Stabilizers That Don't Abort the Trip).
Breath
Exhale longer than you inhale for ten breaths.
Or try Buteyko reduced breathing: breathe softly and slowly through the nose, taking in slightly less air than desired until there is faint air hunger.
Systema continuous partial breathing in coordination with relaxed movement and muscular detensioning is excellent for entering a flow state.
- AI-Generated (26 words): It helps to watch a video on how to do it prior though, as it's a bit tricky to understand compared to simple reduced breathing.
- AI-Generated (33 words): Never force breath-holds while intoxicated or panicked. Stop for increased fear, dizziness, chest pain, or medical concern.
Whisper: "This is a wave. I can love the part of me that feels it."

### h42-31, Get One Human Anchor ([result](https://www.pangram.com/history/5732b48d-9efb-4ff1-9c06-db5edcdb22f4))

- AI-Generated (50 words): Get One Human Anchor
Many bad trips get worse because somebody is alone with a frightened or over-certain mind. Other times it's the opposite: too many people crowd in and start advising, arguing, spiritualizing, or panicking.
So one calm person should be the anchor and take the lead.
- AI-Generated (8 words): One person can only handle so much, though.
- AI-Generated (104 words): When fatigue or logistics get to be too much, or keeping them safe does, or there's a risk of violence or self-harm, bring in one more calm adult or a crisis professional to back them up.
Script for the person in the altered state:
I'm in an intense psychedelic or altered state and I need grounding. I don't need you to solve my life. Please stay with me, speak slowly, remind me where I am, and help me not make any big decisions until tomorrow.
Alone at 3 a.m.
The triage app has the stripped-down 3 a.m.
- AI-Generated (1 words): plan.
- AI-Generated (75 words): Once the lamp is on, the keys are away, and "No big actions until morning" is visible, use the phone only to reach a calm person or support service.
Send the human-anchor script.
While you wait, put one hand on your heart and the other on your solar plexus just under your chest, and say to yourself: "This feeling is allowed to move through. I can love the part of me that feels it."

### h42-32, For the Person Helping: Calm Anchor, Not Guru (1 of 2) ([result](https://www.pangram.com/history/96ae4fdc-a0dd-4ef1-9a7a-dbfab8db5048))

- AI-Generated (104 words): For the Person Helping: Calm Anchor, Not Guru
The Zendo Project, a harm-reduction group that offers peer support at festivals and other events to people having a hard time in an altered state, sums up its approach in four principles: creating a safe space, sitting with the person rather than guiding them, talking them through it rather than down from it, and remembering that difficult isn't necessarily bad.
Crying, grieving, remembering, or touching a genuine wound calls for loving awareness. Interrogation, analysis every thirty seconds, and "bro, you're purging ancestral karma" while somebody white-knuckles the carpet are generally less helpful.
- AI-Generated (2 words): Stay present.
- AI-Generated (59 words): If it helps, you can say to yourself: This feeling is allowed to move through. I don't have to become it. I can love the part of me that feels it. Or simply: Can I send love to the one who's suffering?
Do
Ask simple questions: "Would less light help?" "Music or quiet?" "Closer or farther away?"
- AI-Generated (1 words): "Water?"
- AI-Generated (35 words): (in small sips) "Need the bathroom?"
Call for help early when safety is slipping.
Set behavioral boundaries without humiliation: "I won't help anybody hurt themselves or another person. We are keeping every body safe."

### h42-33, For the Person Helping: Calm Anchor, Not Guru (2 of 2) ([result](https://www.pangram.com/history/b37b776e-bbda-46e4-8ecb-e5f82130d88e))

- AI-Generated (258 words): When What They Say Turns Toward Harm
When somebody says, "I am God, so I can kill," leading with "No you're not" or "That's delusional" can turn the encounter into a status fight. Nodding along as though harm is spiritually neutral is also unacceptable. Treat the statement as a safety signal and build a bridge back toward non-harm.
Non-combative philosophical grounding:
I hear how vast and certain this feels. Many traditions say God is in everyone. That makes every body sacred, not disposable. Peace is the godly move tonight. No proof is needed. We protect life and sleep first.
Other useful lines: "Maybe you are touching something divine. Divine doesn't need a violent test." "Tonight the commandment is no harm, no proof, no mission, sleep first."
When talk of harm continues, shift from philosophy to safety. Create distance from potential targets and keep your own exit. Don't block, crowd, threaten, mock, or physically wrestle away a weapon. Quietly remove means only when that can be done without confrontation or turning yourself into the target.
Call crisis or emergency services for a specific target, available means, movement toward action, escalating agitation, a weapon, violence underway, or a situation you can't contain.
Be brief and specific with emergency services: "Someone is in an altered-state or mental-health crisis, has threatened to harm others, may have access to [means if known], and needs a medical or mental-health crisis response with de-escalation support. Please send crisis-trained responders or EMS if available."

### h42-34, No Rash Actions: Visions Are Not Commands ([result](https://www.pangram.com/history/0e72d245-bd64-4325-83b9-9648e45bc722))

- AI-Generated (89 words): No Rash Actions: Visions Are Not Commands
An intense altered state can make everything feel final, cosmic, and urgent, and it might feel like you have to act right now. But more likely the urgency is just part of the state, and acting on it isn't safe.
Put yourself on a 24–72 hour action lock.
Until you have slept and eaten, maybe don't drive, travel, break up, make up, quit your job, confess everything, confront or accuse that list of people you've been meaning to...
- AI-Generated (29 words): Think twice before sending whatever ridiculous message you're planning on to Judge Amos, posting that revelation you'll forget tomorrow, giving away your BMW, buying a new BMW.
- AI-Generated (138 words): After you decide that you are permanently enlightened or permanently damaged, and you explained the whole universe to your parents in 42 seconds, you can still change your mind the next day.
Write it down, get some sleep, and go back over it with one grounded person once your head is clear.
Treat trip content first as experience-content, rather than fact-content. Because you saw it, it might feel like you have to act on it, and because it felt cosmic, obeying it might seem wise. But more likely you had an experience, and it can wait until the state has passed.
No revelation makes murder, assault, coercion, sexual boundary-crossing, reckless driving, or self-harm safe tonight. Anything requiring violated consent or harm belongs in the notebook until you can review it with a clear head.

### h42-35, When the Trip Feels Amazing: Euphoric Certainty ([result](https://www.pangram.com/history/b6755001-0369-4870-803f-ffc37a6c73f0))

- AI-Generated (87 words): When the Trip Feels Amazing: Euphoric Certainty
The action lock matters especially when the state feels blissful: I am God. I am chosen. Everybody must hear this tonight. I finally understand everything. Bliss is not proof of safety, and it often makes grounding less welcome.
Two questions while glowing:
Have I slept? Sleep comes before mission.
Has this happened before, and how did it end? A recurring pattern with lost sleep, racing thoughts, pressured speech, or everyone saying you are not yourself needs grounded support before action.

### h42-37, Dealing With Sorrow: Missing Versus Sending Love ([result](https://www.pangram.com/history/8d71284e-ebc1-438b-bc33-dd8e81787a21))

- AI-Generated (5 words): Missing someone is a contraction.
- AI-Generated (28 words): There's hunger and ache in it, it keeps circling back to you, and there's the painful fantasy that loving them means needing them to come back.
- AI-Generated (4 words): Sending love is different.
- AI-Generated (40 words): Sending love is pleasure in itself, even when the person is gone. Love can bless without grabbing.
The difference is enormous.
The mistake people often make in love states is simply enjoying the love--or sending heart emojis to everybody.
- AI-Generated (36 words): That can feel like the whole point, and it's nice.
But the deepest utility is sending love to the places where love is missing.
Send love to the person you miss without demanding their return.
- AI-Generated (25 words): Send love to the part of you still waiting for them.
Send love to the inner child who believed somebody else had to rescue him.
- AI-Generated (11 words): Send love to the ashamed, angry, lonely, terrified, and exiled parts.
- Human Medium (2 words): Missing hurts.
- Human Medium (22 words): This sounds almost embarrassingly obvious, but it took me months of daily loveyhuasca after my ex-wife Bee left to understand it.

### h42-38, Hand on Heart and Gratitude 🫶🏿 ([result](https://www.pangram.com/history/64194b97-a5dc-4765-9fef-db8717a55b89))

- AI-Generated (70 words): Hand on Heart and Gratitude 🫶🏿
A hand on the heart can change the direction of a trip, especially when the problem is emotional contraction, grief, fear, or loneliness. There's no need to manufacture loving thoughts, you're just giving the body one simple signal: love is here.
Put one hand on the heart and the other on the solar plexus just below it, sending love to the inner child.
- AI-Generated (6 words): Sometimes that shifts the whole field.
- AI-Generated (33 words): Once love reaches the inner child, send it toward all beings suffering now. Recognizing that you are not the only one suffering can open awareness in a liberating way, with real heart magic.
- AI-Generated (7 words): Gratitude comes like icing on the cake.
- AI-Generated (22 words): Being thankful for every lesson, difficult experience, reprieve, heart opening, and moment of compassion can create a deep connection with the sacred.
- AI-Generated (8 words): Never force gratitude. Let it bubble up gently.
- AI-Generated (68 words): Touch, Consent, and Compassion
Self-touch is different from somebody else touching you. Compassion does not mean grabbing, hugging, restraining, stroking, or crowding. Ask first: "Would touch help, or would you rather have space?" Good support may be silent presence from six feet away.
When the person says stop, freezes, pulls away, or seems unsure, stop. Touch must remain nonsexual, consensual, and unrelated to the helper's needs.

### h42-39, Demons, Jinn, Entities, and Shadow Forces ([result](https://www.pangram.com/history/c00df5c7-b129-47a7-9c16-a30ebfb3eae4))

- AI-Generated (31 words): Demons, Jinn, Entities, and Shadow Forces
I have faced demons and jinn during psychedelic and exorcism-type situations. The most important thing I discovered was that fighting them did not help.
- AI-Generated (3 words): Sending love did.
- AI-Generated (60 words): In one especially dramatic situation involving another person, the entity seemed to attack both of us psychically. I sent it love, and within a few seconds it left. The other person could not do that immediately. I had to show her, and it took hours of practice before it worked because she had never gone deeply into "Love Thy Enemy."
- AI-Generated (204 words): I don't have to settle whether these things are objectively real or internal formations because the response is mostly the same.
Hatred, fear, shame, pride, and rage make hooks. Love removes hooks.
The common mistake is fighting the terrifying thing with the energy it already consumes. Panic fights panic, hatred fights hatred, pride fights pride, and suddenly a small war is running inside consciousness.
Love is a better move, although it is difficult advice. Almost nobody can authentically love what terrifies them while they are terrified. So train before you need it, sending love to a frightening image, to someone you hate (without approving of what they did), to your shame and your body, to sickness and aging and fear and death, and to the inner child. Practice being the space rather than the storm.
It might look passive, but this is how you become unhookable. A demon can fight your hatred, feed on your fear, argue with your pride or seduce your grandiosity, but there's nothing in love for it to grab.
When somebody is medically, physically, or psychologically too overwhelmed to reach love, stabilize first. Don't teach nondual demonology to somebody who needs the lights down and a doctor.

### h42-40, Abuse Memories, Recovered Memories, and Certainty ([result](https://www.pangram.com/history/0fa4603f-d3a0-43f8-80eb-c7a3f9631679))

- AI-Generated (132 words): Abuse Memories, Recovered Memories, and Certainty
Psychedelics and intense practices can bring up true trauma, symbolic material, distorted fragments, fears, fantasies, archetypes, past-life narratives, and mixtures of all of them. Don't dismiss what arises. Don't treat the certainty you feel in that state as evidence either.
Don't confront tonight
When you see or remember abuse, betrayal, murder, past lives, hidden crimes, or cosmic plots, write it down and get safe. Don't confront anybody while intoxicated or destabilized. Return to it after sleep with a trauma-informed therapist, integration specialist, or grounded person you trust.
The experience may matter deeply. It could be true psychologically, or symbolically, or literally, or only partly true, or false in the form it first took. You don't have to decide tonight.

### h42-41, Dealing With Shadow Thoughts ([result](https://www.pangram.com/history/a9528123-9665-4a17-bef1-4a5c2d172908))

- AI-Generated (23 words): During a trip, don't identify with every shadow thought, suppress it, confess it to everybody, or convert it into a permanent diagnosis.
- AI-Generated (20 words): Notice: "A thought is here. A feeling is here. It is intense, but it is not the whole of me."
- Human Low (65 words): Dealing With Shadow Thoughts
When we try to purify the mind, something natural and frightening may happen: the opposite becomes more visible, almost like Newton's Third Law--every action arrives with an equal and opposite reaction.
Shadow thoughts and feelings are not inherently a problem. They co-arise naturally and do not need to be attached to, like shadows cast by objects in sunlight.
- Human Low (7 words): I also notice them after excessive focus.
- Human Low (19 words): The mind becomes stressed and seeks an exit from the pressure, often in the opposite direction from the focus.
- Human Medium (30 words): I am not repeating the simplistic Hermetic claim that opposites are required to understand anything. A hated baby does not feel love, and a loved baby does not feel hate.
- Human Low (13 words): In the subconscious world of concepts, however, two sides are often considered together.
- Human Medium (9 words): Then return to room, body, human, time, and love.
- Human Medium (1 words): --Unknown

### h42-43, Spiritual ≠ "Getting Your Ass Kicked" ([result](https://www.pangram.com/history/185ae3d5-3056-4e5e-a41f-eb3fc5d1f8a1))

- AI-Generated (113 words): Spiritual ≠ "Getting Your Ass Kicked"
The triage above is meant to make trips useful. Some people believe they deserve suffering because of karma or self-hatred. Suffering by itself fixes nobody. Suffering that yields insight requires enough clarity of mind and heart to learn from it.
This is one side of the difference between spiritual bypassing and spiritual practice:
Bypassing reaches for an ultimate view--"we are all One," "I don't exist," "this is all karma," "everything is Love"--while ignoring the person shaking in the corner.
Practice says love is here, so we make the room safer, call for help when needed, stop pretending, and hold the experience without becoming it.
- AI-Generated (10 words): That is tripsitting, shadow work, and the path becoming practical.

### h42-45, After the Storm ([result](https://www.pangram.com/history/53464de3-daea-4cf1-8ef3-191f1c48d0d8))

- AI-Generated (35 words): After the Storm
Don't make huge decisions or diagnose yourself from an intense night. You don't need to assume every vision was literal, nor that anything you realized is actually true (or false).
- AI-Generated (9 words): Ask your body what it needs from you now.
- AI-Generated (18 words): I'm betting it will tell you: Give me sleep, natural food, pure water, a nice nature walk.
- AI-Generated (7 words): No "another ceremony will fix this" reflex.
- AI-Generated (41 words): Don't take more psychedelics, cannabis or ketamine, do intense breathwork, fast, push kundalini, deprive yourself of sleep, meditate or stretch to extremes, or schedule "another ceremony to fix it" while destabilized. Deep practice can wait until the floor is back.
- AI-Generated (26 words): Then ask what actually happened. What was medical or environmental? What was emotional? What was old trauma? What was fantasy? What was useful? What changed behavior?
- AI-Generated (40 words): What needs therapy, an apology, rest, or plain practical action?
It can feel like the more cosmic the story sounds, the bigger the insight. But the fruit of an insight is whether suffering goes down and love gets more available.
- Human Low (25 words): It helps to integrate the experience via journaling your feelings, and talking with someone grounded (not the 20 chaotic people who are still coming down).
- Human Low (18 words): To prevent your mind from giving spirituality a negative connotation, engage in some calm prayer or gentle meditation.

### h42-08, Active Seizure (2 of 2) ([result](https://www.pangram.com/history/a9e74179-83f2-4805-be65-b8057c632bbc))

- Human Low (20 words): I'd treat it as a plausible experimental adjunct remedy rather than something to wait on while a seizure continues.

### h42-17, Nausea Smoothers When the Person Wants to Preserve the Trip ([result](https://www.pangram.com/history/1c9fc7f4-9af7-44f1-9892-8f51bcd71352))

- Human Medium (6 words): It may also extend the trip.
- Human Low (22 words): That can be useful and healthy when planned, but I wouldn't reach for it first when somebody is already becoming manic.

### h42-30, Grounding Menu: Choose One or Two Things (2 of 2) ([result](https://www.pangram.com/history/ea7a2215-f9de-4b7c-b35b-dc5091ec7037))

- Human Medium (6 words): Music
Use familiar music when possible.
- Human Medium (8 words): Put every big decision into tomorrow's notebook.
- Human Medium (11 words): Walk slowly with a clear-headed person in a safe environment.
- Human Low (29 words): Go outside only away from roads, heights, crowds, and water.
Avoid strenuous exercise with overheating, chest pain, faintness, severe confusion, stimulant use, an unknown mixture, or any medical concern.

### h42-27, Psychological First Aid: The First Five Minutes (1 of 2) ([result](https://www.pangram.com/history/71e9dd23-ae2b-48bc-a606-78f33f1e5c1e))

- Human Medium (11 words): And if they want to leave, have someone go with them.

### h42-36, Shadow Work ([result](https://www.pangram.com/history/236a3091-6841-4e3a-a5fc-9642b12637e1))

- Human Medium (5 words): Inner-child reparenting is central.

### h42-42, (Re)defining "Bad Trip" ([result](https://www.pangram.com/history/4972cd65-cf59-4a3c-878d-0a877f11d012))

- Human Medium (17 words): But if you had no intention of doing shadow work, that explanation might have come too late.
- Human Medium (9 words): Samsara offers no shortage of difficult experiences to process.
- Human Medium (10 words): Sometimes focusing on what we want makes the blockage visible:

### h42-46, What Kind of Aftermath Is This? ([result](https://www.pangram.com/history/78353445-3765-4e63-9119-00ab5f8f562a))

- Human Medium (6 words): What Kind of Aftermath Is This?

### h42-50, Appendix: Additional Resources ([result](https://www.pangram.com/history/eeba7d60-3ed4-499e-9432-61b828931b46))

- Human Medium (2 words): U.C.

