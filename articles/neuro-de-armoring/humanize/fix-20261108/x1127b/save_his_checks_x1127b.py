#!/usr/bin/env python3
"""Write HIS-CHECKS-X1127B.json: his own Pangram checks of his versions on cards W-SW19 and W-SW23 (answered 2026-11-27
22:59 UTC: ANSWERS-X1127B-20261127-2259.json), read back from his account's history
(web.pangram.com/api/history/<uuid>/) in the desktop app's browser pane, tab "seed", 2026-11-27 after 23:00 UTC.

Four checks: the three he linked in his comments and one he didn't (75361775, "20" as a numeral without "something
like", which he described: "you forgot not to spell out twenty ... but that didn't help"). Each prompt is written here
as Pangram returned it and asserted against the SHA-256 the browser computed of the stored prompt, so a slip in copying
fails the script.

  python3 articles/neuro-de-armoring/humanize/fix-20261108/x1127b/save_his_checks_x1127b.py
"""
import hashlib
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE / 'HIS-CHECKS-X1127B.json'

PRACTICE_HEAD = ("The Anti-Breakthrough (Micro-Dosing): A brain stuck in alarm can often take in healing work for only a few "
                 "seconds at a time, Perry finds. So for now we have to give up on the hour-long breakthrough that therapy "
                 "aims for, since an hour spent working on the trauma itself overwhelms an armored nervous system more than "
                 "it heals it. Instead, this protocol works in doses of a few seconds, which is another dimension of "
                 "micro-dosing.\n\n")

CHECKS = [
    {'card': 'W-SW19', 'step': 'his version ("people you\'re close to and who you hang with on most days")',
     'link': 'https://www.pangram.com/history/51ceffa5-98f3-4fd5-b160-e438f540d9d8',
     'uuid': '51ceffa5-98f3-4fd5-b160-e438f540d9d8', 'at': '2026-11-27T22:51:56Z',
     'sha256': '929024b7029528a93690b4091bce90ff4bbf2038c94e266dbec1219dfe5bb5e5',
     'headline': 'Human Written', 'ai': 0, 'words': 94,
     'windows': [['Human', 'High', 94, 'the whole paragraph']],
     'prompt': ("That works out to about one-sixteenth of the grown-ups per child that our brains evolved with (Perry, "
                "2023). So the emptiness you feel (the \"Void\") is real, since it's what that missing company feels like. "
                "Once you've de-armored, going back to a lonely life will tend to feel worse than it did with the armor "
                "on. So gather a tribe of people you're close to and who you hang with on most days, or you'll eventually "
                "put the armor back on just to get through the loneliness.")},
    {'card': 'W-SW23', 'step': '1: "which is another dimension of micro-dosing" (the practice line still mine, "twenty")',
     'link': 'https://www.pangram.com/history/dd157d47-19a1-40a5-95af-1d5d6a9440e3',
     'uuid': 'dd157d47-19a1-40a5-95af-1d5d6a9440e3', 'at': '2026-11-27T22:55:57Z',
     'sha256': '3390c163f3d82e07ff757e8f0e7fcac627558467bea64edca4fb816eb448652b',
     'headline': 'Human Written', 'ai': 3.353711811112135e-16, 'words': 93,
     'windows': [['Human', 'High', 79, 'the Anti-Breakthrough'],
                 ['Human', 'Medium', 14, "In practice, I'd do 30 seconds of slow breathing, twenty times a day."]],
     'prompt': PRACTICE_HEAD + "In practice, I'd do 30 seconds of slow breathing, twenty times a day."},
    {'card': 'W-SW23', 'step': '2: "20" for "twenty" (not linked; his comment: "that didn\'t help")',
     'link': 'https://www.pangram.com/history/75361775-0680-4db9-835b-5d71b387ce59',
     'uuid': '75361775-0680-4db9-835b-5d71b387ce59', 'at': '2026-11-27T22:57:09Z',
     'sha256': '2585bf4e71c74ed94ff9825123528ae3b6dad37ac16f52b8d16716f124bccd8c',
     'headline': 'Human Written', 'ai': 8.510433835617534e-17, 'words': 93,
     'windows': [['Human', 'High', 79, 'the Anti-Breakthrough'],
                 ['Human', 'Medium', 14, "In practice, I'd do 30 seconds of slow breathing, 20 times a day."]],
     'prompt': PRACTICE_HEAD + "In practice, I'd do 30 seconds of slow breathing, 20 times a day."},
    {'card': 'W-SW23', 'step': '3: "something like" (his version)',
     'link': 'https://www.pangram.com/history/6bdc6163-1943-4de6-87d1-d398f4431bee',
     'uuid': '6bdc6163-1943-4de6-87d1-d398f4431bee', 'at': '2026-11-27T22:57:27Z',
     'sha256': '6eb93937c5eae77a7b04f2bd232a226917354dcc80b7a2d7ed0c35d4751c04b0',
     'headline': 'Human Written', 'ai': 9.412769179339898e-25, 'words': 95,
     'windows': [['Human', 'High', 95, 'the whole pair']],
     'prompt': PRACTICE_HEAD + "In practice, I'd do something like 30 seconds of slow breathing, 20 times a day."},
]

for c in CHECKS:
    got = hashlib.sha256(c['prompt'].encode('utf-8')).hexdigest()
    assert got == c['sha256'], (c['uuid'], got)
    c['text_sha256'] = got

OUT.write_text(json.dumps({
    'about': ("His own Pangram checks of his two card versions (cards W-SW19 and W-SW23, answered 2026-11-27 22:59 UTC: "
              "ANSWERS-X1127B-20261127-2259.json), read back from his account's history (web.pangram.com/api/history/<uuid>/) "
              "in the desktop app's browser pane, 2026-11-27 after 23:00 UTC. Each prompt is the text as he typed it. Each "
              "check has the fields coverage.py reads (uuid, at, text_sha256 of the prompt, windows as [label, confidence, "
              "words, where]). The W-SW23 checks are a lineage of his: step 2 is the one he described without a link."),
    'checks': CHECKS}, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
print('written', OUT.name, len(CHECKS), 'checks, every SHA-256 as Pangram stored it')
