from pathlib import Path
import re, json, hashlib, html

ROOT=Path('/workspace/scratch/4845c4a6c885')
WORK=ROOT/'odt_work'
WORK.mkdir(exist_ok=True)
raw=(ROOT/'upload/Pasted markdown(8).md').read_text()
assert hashlib.sha256(raw.encode()).hexdigest()=='81c0e31546deefc2ae17b5aa0e5159143618a7d5e94770cb07c6cd36e20520b1'
chunks=re.split(r'(?m)^(#{1,4}) (.+)\n',raw)
sections={}; all_blocks=[]
for i in range(1,len(chunks),3):
    level=len(chunks[i]); title=html.unescape(chunks[i+1]).strip()
    blocks=[]
    for p in re.split(r'\n\s*\n',chunks[i+2].strip()):
        if not p.strip(): continue
        b={'id':f'P{len(all_blocks)+1:03d}','source_heading':title,'original':p.strip(),'text':p.strip(),'edits':[]}
        blocks.append(b); all_blocks.append(b)
    sections[title]={'level':level,'blocks':blocks}
def get(name):
    matches=[s for t,s in sections.items() if t.replace('\xa0',' ')==name]
    assert len(matches)==1,(name,list(sections))
    return matches[0]['blocks']
def edit(b,before,after,reason,kind='approved transition/trim'):
    assert b['text'].count(before)==1,(b['id'],before)
    b['text']=b['text'].replace(before,after,1)
    b['edits'].append({'before':before,'after':after,'reason':reason,'kind':kind})

opening=get('Borrowed Adulthood in Relationship')
play=get('Play Is Part of the Work')
survival=get('From Survival to Experimental Play')
beginner=get('Let the Child Be Bad at Things')
bargains=get('Untangling the Belonging Bargains')
pairs=get('Four Pairs That Commonly Hook the Child')
diff=get('Differentiation')
happy=get('When Being Happy Feels Like Abandoning Someone')
people=get('People ? Where are the people?')
first=get('First Social Connections, Done Right')
disclose=get('Opening up honestly to the right people at the right pace')
hard=get('Before You Tell the Hardest Stuff')
ask=get('Ask What Kind of Company They Want')
hearth=get('Hearthwork: Taking Turns')
dating=get('Dating While You Heal')
threat=get("If they've actually hurt or threatened you")
speak=get('Speak Toward What You Are Building')
write=get("Write It. Don't Send It Yet.")
repair=get('If you really did hurt them')
hooks=get('Other Folks Also Have Hooks')
change=get('Can they change?')
unsafe=get('If a relationship keeps making you feel less safe')
endings=get('When One Life Has Ended and the Next Hasn’t Begun')
missing=get('Missing Someone')
love=get('The Love Has to Move')

# Three exact trims authorized by the accepted plan.
edit(bargains[0],'Most groups expect some conformity. ','','Repeated generalization; the surrounding examples retain the point.','approved cut')
edit(bargains[2],' In the process of self-differentiation, we learn to notice when we’re making the trade, and we begin keeping our ground more when feasible.','','The adjacent differentiation teaching and daily-practice list supply this function.','approved cut')
edit(speak[0],'also isn’t realistic nor ideal, and ','','The opening supplies balanced reliance; retain the distinct reaction-to-dependence observation.','approved cut')

# Local referent repairs required by the approved moves.
doctor=first[-1]
assert doctor['text'].startswith('The same goes for doctors.')
edit(doctor,'The same goes for doctors. ','','The new doctors heading supplies a self-contained context; remove the old backward reference.','approved lead deletion')
edit(threat[0],'old stuff or not','whether or not it brings up old stuff','Make the prior-experience qualification explicit after moving this branch to the section opening.')

edit(dating[0],'Maybe you’d rather that your support person were a lover, as well.','Maybe you’d rather that your support came from a lover, as well.','Refer to receiving support in romance, without implying that the Hearthwork peer should become a lover.')
# Keep the original First Social Connections opening: the previous paragraph now
# names places where the reader can meet people, supplying its Then reference.

# Only unambiguous copy slips; no style or claim changes.
edit(opening[0],'it’s might','it might','Remove an accidental grammatical extra.','P1 typo')
edit(first[1],'mind,but','mind, but','Restore a missing space.','P1 spacing')
edit(first[1],'hildhood','childhood','Restore the missing initial letter.','P1 typo')
edit(first[2],'they’re you’re  reassurance machine','they’re your reassurance machine','Correct the possessive and duplicated space.','P1 grammar')
edit(endings[1],'autopilot.Ask','autopilot. Ask','Restore the sentence space.','P1 spacing')

chameleon=survival[2]
break_para=next(b for b in diff if b['text'].startswith('Differentiation is slow'))
attribution=next(b for b in diff if b['text'].startswith('Key developed'))
note=next(b for b in change if 'An embedded note of yours:' in b['text'])

nodes=[]
def head(level,title): nodes.append({'type':'heading','level':level,'text':title})
def put(blocks):
    for b in blocks:
        assert not any(n.get('source_id')==b['id'] for n in nodes), b['id']
        nodes.append({'type':'body','source_id':b['id'],'text':b['text']})
head(1,'Bringing Reparenting Into Real Life');put(opening)
head(2,'1. Rediscover Play and Your Own Preferences')
head(3,'Play Is Part of the Work');put(play)
head(3,'From Survival to Experimental Play');put(survival[:2])
head(3,'Let the Child Be Bad at Things');put(beginner)
head(2,'2. Differentiation: Keeping Your Own Ground')
head(3,'Untangling the Belonging Bargains');put(bargains)
head(4,'Four Pairs That Commonly Hook the Child');put(pairs)
head(3,'Practicing Differentiation');put([diff[0],chameleon]);put([b for b in diff[1:] if b not in [break_para,attribution]]);put([attribution])
head(3,'When Being Happy Feels Like Abandoning Someone');put(happy)
head(2,'3. Finding People and Building Trust')
head(3,'People? Where Are the People?');put(people)
head(3,'First Social Connections, Done Right');put(first[:-1])
head(3,'Opening Up Honestly to the Right People at the Right Pace');put(disclose)
head(4,'Before You Tell the Hardest Stuff');put(hard)
head(3,'Ask What Kind of Company They Want');put(ask)
head(3,'Hearthwork: Taking Turns');put(hearth)
head(3,'Dating While You Heal');put(dating)
head(2,'4. Speaking Up and Handling Conflict')
head(3,'If Someone Has Actually Hurt or Threatened You');put(threat)
head(3,'Speak Toward What You Are Building');put(speak)
head(3,'Being Your Own Advocate With Doctors');put([doctor])
head(3,"Write It. Don't Send It Yet.");put(write)
head(3,'If You Really Did Hurt Them');put(repair)
head(3,'Other Folks Also Have Hooks');put(hooks)
head(4,'Can They Change?');put([b for b in change if b is not note])
nodes[-1]['comment_source_id']=note['id']
head(4,'If a Relationship Keeps Making You Feel Less Safe');put(unsafe)
head(3,'Taking a Break From a Family, Group, or Relationship');put([break_para])
head(2,"5. When One Life Has Ended and the Next Hasn't Begun");put(endings)
head(3,'Missing Someone');put(missing)
head(2,'6. The Love Has to Move');put(love)

def render_md(s):
    s=html.unescape(s).strip()
    s=re.sub(r'(?m)^\s*\\- ', '- ',s)
    s=re.sub(r'\\\n','\n',s)
    s=s.replace('\\(https\\://ibogaqueen.substack.com/p/i-ate-loveyhuasca-every-day-for-90)', '(https://ibogaqueen.substack.com/p/i-ate-loveyhuasca-every-day-for-90)')
    return s
for n in nodes: n['rendered_text']=render_md(n['text'])
md='\n\n'.join(('#'*n['level']+' '+n['rendered_text']) if n['type']=='heading' else n['rendered_text'] for n in nodes)+'\n'
(WORK/'revised.md').write_text(md)
note_plain=render_md(note['text']).strip('*')
(WORK/'editorial-note.txt').write_text(note_plain+'\n')
ledger={'source_sha256':hashlib.sha256(raw.encode()).hexdigest(),'accepted_plan_sha256':hashlib.sha256((ROOT/'upload/Inner_child_real_life_TOC_and_move_map.md').read_bytes()).hexdigest(),'source_blocks':all_blocks,'nodes':nodes,'comment':{'source_id':note['id'],'exact_raw':note['original'],'visible_text':note_plain},'output_md_sha256':hashlib.sha256(md.encode()).hexdigest()}
assert len([n for n in nodes if n['type']=='body'])==len(all_blocks)-1
assert set(n['source_id'] for n in nodes if n['type']=='body')|{note['id']}==set(b['id'] for b in all_blocks)
(WORK/'preservation-ledger.json').write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n')
# The only newly composed prose is a minimal source-referent repair. Its exact
# full local unit is reviewed through the repository's owner-delivery gate.
gate=WORK/'gate_r2';gate.mkdir(exist_ok=True)
original_heading="If they've actually hurt or threatened you"
new_heading='If Someone Has Actually Hurt or Threatened You'
(gate/'source.txt').write_text('### '+original_heading+'\n\n'+threat[0]['original']+'\n')
(gate/'candidate.txt').write_text('### '+new_heading+'\n\n'+threat[0]['text']+'\n')
(gate/'context.txt').write_text(md)
dategate=WORK/'dating_gate';dategate.mkdir(exist_ok=True)
(dategate/'source.txt').write_text('Maybe you’d rather that your support person were a lover, as well.')
(dategate/'candidate.txt').write_text('Maybe you’d rather that your support came from a lover, as well.')
(dategate/'context.txt').write_text(md)
print(json.dumps({'source_blocks':len(all_blocks),'body_blocks':len(all_blocks)-1,'comments':1,'changed_blocks':sum(bool(b['edits']) for b in all_blocks),'edits':[{'id':b['id'],'changes':b['edits']} for b in all_blocks if b['edits']],'md_sha256':ledger['output_md_sha256']},ensure_ascii=False,indent=2))
