#!/usr/bin/env python3
"""r32 = r31 with Joel's news about Pooyan, as one more sub-item of "Years of accumulated shit in your guts", after the
"However, while we don't know if Pooyan has diverticulosis ..." item and before the CAUTION. His words, 2026-11-07, in
answer to my question about updating his post: "Oh, one change. Pooyan is actually all better from his gut issues now
that nobody could fix. Apparently he didn't need the insane treatments he was doing on himself. What worked was some
Bombax ceiba flower i sent him. It's sold on amazon cheap. AskRigor is what told me about this when doing
ethnobotanical research. My other friend, Acacea, is also benefitting from this flower".

An answer that explains something to me is his content, not the line (gate E261): the item keeps his facts and his
phrases ("all better", "nobody could fix", "the insane treatments he was doing on himself", "sold on amazon cheap",
"ethnobotanical research", and his last sentence word for word), with three changes of mine: "now" moved so "now that"
can't read as "since"; "AskRigor, my research tool," because this is now where the reader first meets the name (the
leaky gut list introduces it the same way further down); and a gloss for Bombax ceiba, "from the red silk-cotton tree"
(Flora of Qatar, https://www.floraofqatar.com/bombax_ceiba.htm: "Kapok, red cotton tree, red silk-cotton").
Writes r32.md and CHANGES.json."""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
md = (HERE.parent / 'r31' / 'r31.md').read_text(encoding='utf-8')
after = ('  - However, while we don\'t know if Pooyan has diverticulosis, what we now do know is that his peak health '
         'disappeared 3 days later after eating some bread with A1 dairy, the regular cow\'s milk that has the A1 type of '
         'casein protein.\n')
assert md.count(after) == 1
NEW = ('Update: Pooyan is actually all better now from his gut issues that nobody could fix. Apparently he didn\'t need '
       'the insane treatments he was doing on himself. What worked was some Bombax ceiba flower, from the red silk-cotton '
       'tree, that I sent him. It\'s sold on Amazon, cheap. AskRigor, my research tool, is what told me about it when I '
       'was doing ethnobotanical research. My other friend, Acacea, is also benefitting from this flower.')
md = md.replace(after, after + '\n  - ' + NEW + '\n')
CHANGES = [{'new': NEW, 'kind': 'his', 'after': after.strip(),
            'why': 'Joel, 2026-11-07, answering whether to update his post: "Oh, one change. Pooyan is actually all better '
                   '..."; his facts and phrases, with "now" moved, AskRigor introduced where the reader first meets it, '
                   'and a gloss for Bombax ceiba',
            'source': 'https://www.floraofqatar.com/bombax_ceiba.htm (the gloss: "Kapok, red cotton tree, red silk-cotton")'}]
(HERE / 'r32.md').write_text(md, encoding='utf-8')
(HERE / 'CHANGES.json').write_text(json.dumps(CHANGES, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print(len(md.split()), 'words')
