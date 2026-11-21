You are checking an answer key for a test of a guide's table of contents. You will not see the guide's headings.

Read only these two files:
- /home/claude/joel-articles/articles/bad-trips/humanize/h64-20261121/toc/ARTICLE-NO-HEADINGS.md (the guide, section by
  section, each with an id and its text, headings taken out)
- /home/claude/joel-articles/articles/bad-trips/humanize/h64-20261121/toc/SITUATIONS.json (32 situations readers bring,
  each with the sections someone listed as answering it, best first)

For each situation, read the guide for any other section that answers it just as directly: a reader who opened that section
first, in that situation, would get what they need there. List only those the key is missing; leave out sections that only
touch the topic. Also say if a listed section doesn't really answer it.

Write /home/claude/joel-articles/articles/bad-trips/humanize/h64-20261121/toc/KEY-CHECK.json as:
{"add": [{"n": 1, "ids": ["..."], "why": "one line"}], "doubt": [{"n": 1, "id": "...", "why": "one line"}]}
Then reply with one line: how many additions and doubts.
