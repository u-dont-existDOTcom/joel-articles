#!/usr/bin/env python3
"""Fail-closed integrity and recorded-review gate for a registered editorial package.

This verifies bytes, coverage and recorded judgments. It does not decide whether a
semantic judgment is right, identify its author, or intercept unrelated chat output.
The HTTP adapter accepts only a registered task ID and an expected candidate hash.
"""
from __future__ import annotations
import argparse, hashlib, json, os, re, tempfile, zipfile
from pathlib import Path
from typing import Any
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from bs4 import BeautifulSoup
from article_edit import parse

class GateError(ValueError):
    """A package is not eligible for the requested operation."""

def digest(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()

def safe_file(root: Path, name: str) -> Path:
    if not isinstance(name,str) or not name or Path(name).is_absolute():
        raise GateError('File must be a nonempty registered relative path')
    p=root/name
    if '..' in Path(name).parts:
        raise GateError('Traversal is not a registered file')
    for parent in [p,*p.parents]:
        if parent==root:break
        if parent.is_symlink():raise GateError('Symlinks are not permitted in a review bundle')
    if not p.resolve().is_relative_to(root.resolve()) or not p.is_file():
        raise GateError('Missing or outside-bundle file: '+name)
    return p

def load(root: Path, name: str) -> Any:
    return json.loads(safe_file(root,name).read_text(encoding='utf-8'))

def assess(root: Path, phase: str='editorial', expected_contract: str|None=None) -> dict[str,Any]:
    root=root.resolve();checks=[];problems=[]
    def require(name: str, predicate: bool, detail: str='') -> None:
        checks.append({'check':name,'passed':bool(predicate),'detail':detail})
        if not predicate:problems.append(name+(': '+detail if detail else ''))
    try:
        cfile=safe_file(root,'GATE-CONTRACT.json');chash=digest(cfile.read_bytes())
        if expected_contract is not None:
            require('registered contract unchanged',chash==expected_contract)
        c=json.loads(cfile.read_text());require('contract version',c.get('format')=='joel-editorial-gate-contract-v1')
        src=safe_file(root,c['source_file']).read_bytes();cand=safe_file(root,c['candidate_file']).read_bytes();ans=safe_file(root,c['answers_file']).read_bytes()
        require('exact source',digest(src)==c['source_sha256']);require('exact candidate',digest(cand)==c['candidate_sha256']);require('exact owner answer file',digest(ans)==c['owner_answers_sha256'])
        a=json.loads(ans);require('source matches owner-selected revision',a.get(c['owner_source_hash_field'])==digest(src))
        L=load(root,c['ledger_file']);M=load(root,c['map_file']);R=load(root,c['review_file']);A=load(root,c['boundary_audit_file'])
        for label,obj in [('assembly ledger',L),('structure map',M),('review record',R),('boundary audit',A)]:
            require(label+' binds candidate',obj.get('candidate_sha256')==digest(cand));require(label+' binds source',obj.get('source_sha256')==digest(src));require(label+' binds owner answers',obj.get('owner_answers_sha256')==digest(ans))
        opening,source_blocks=parse(src.decode());_,candidate_blocks=parse(cand.decode())
        old={x['id']:x for x in source_blocks};nodes=L['blocks'];new={x['id']:x for x in nodes};order=L['new_order']
        require('no duplicate block IDs',len(new)==len(nodes)==len(order)==len(set(order)))
        missing=set(old)-set(new);allowed=c.get('allowed_omissions',{})
        require('source block coverage or exact allowed disposition',missing==set(allowed))
        for i,disposition in allowed.items():
            require('omission has source and rationale '+i,i in old and bool(disposition.get('reason')) and bool(disposition.get('authority_ref')))
            if disposition.get('kind')=='EMPTY_SPACER':
                require('omitted spacer really is empty '+i,old[i]['tag'] in ['p','hr'] and not old[i]['text'].strip() and not old[i].get('classes'))
            else:
                require('substantive omission has recorded review '+i,disposition.get('kind') in ['OWNER_APPROVED','DUPLICATE_FUNCTION_REVIEWED'] and R.get('reviewed_omission_ids',{}).get(i)==disposition.get('authority_ref'))
                require('omission destinations exist '+i,all(d in new for d in disposition.get('destinations',[])))
        require('order covers all ledger blocks',set(order)==set(new))
        require('literal reconstruction equals candidate',opening+''.join(new[i]['raw'] for i in order)+'</div>'==cand.decode())
        current={i:x['raw'] for i,x in old.items() if i not in missing};seen=[]
        for edit in L['edits']:
            i=edit['block'];before=edit['before_html'];after=edit['after_html']
            require('edit has explanation '+edit['id'],bool(edit.get('reason','').strip()))
            if i not in current:
                require('addition has no hidden source '+edit['id'],before=='' and edit['kind']=='addition')
            else:require('exact edit chain '+edit['id'],current[i]==before)
            current[i]=after;seen.append(i)
        require('all changed text has an edit record',set(current)==set(new) and all(current[i]==new[i]['raw'] for i in current))
        # Native islands are taken directly from raw source blocks, not rebuilt from a model.
        kinds={'captioned-image-container','digest-post-embed','youtube-wrap','button-wrapper'}
        protected=[b for b in source_blocks if kinds.intersection(b.get('classes',[]))]
        require('native islands preserved byte-for-byte',all(new.get(b['id'],{}).get('raw')==b['raw'] for b in protected),f'{len(protected)} source objects; global order may intentionally change')
        source_links=[a.get('href') for a in BeautifulSoup(src,'html.parser').find_all('a',href=True)]
        candidate_links=[a.get('href') for a in BeautifulSoup(cand,'html.parser').find_all('a',href=True)]
        from collections import Counter
        require('link destinations and occurrence counts preserved',Counter(source_links)==Counter(candidate_links))
        actual=[];stack=[]
        for i in order:
            b=new[i];soup=BeautifulSoup(b['raw'],'html.parser');tag=soup.find()
            if tag and re.fullmatch(r'h[1-6]',tag.name):
                level=int(tag.name[1]);title=tag.get_text(' ',strip=True)
                while stack and stack[-1][1]>=level:stack.pop()
                actual.append((i,title,level,stack[-1][0] if stack else None));stack.append((i,level))
        mapped=[(n['id'],n['title'],n['level'],n['parent']) for n in M['nodes']]
        require('outline matches literal headings and parents',actual==mapped)
        require('every mapped heading has purpose and reader question',all(n.get('purpose','').strip() and n.get('reader_question','').strip() for n in M['nodes']))
        md={n['id']:n for n in M['nodes']};h1=[i for i,_,lev,_ in actual if lev==1]
        require('all dependency endpoints exist',all(e['from'] in md and e['to'] in md and e.get('why') for e in M['edges']))
        for n,k in enumerate(c['constraints'],1):
            kind=k['type'];ok=False
            if kind=='adjacent_h1':ok=k['before'] in h1 and k['after'] in h1 and h1.index(k['after'])==h1.index(k['before'])+1
            elif kind=='same_parent':ok=all(md.get(i,{}).get('parent')==k['parent'] for i in k['nodes'])
            elif kind=='before':ok=k['before'] in order and k['after'] in order and order.index(k['before'])<order.index(k['after'])
            elif kind=='heading':ok=md.get(k['node'],{}).get('title')==k['title']
            require(f'owner/route constraint {n} ({kind})',ok,k.get('authority',''))
        require('cluster inventory identity',digest(safe_file(root,c['cluster_inventory_file']).read_bytes())==c['cluster_inventory_sha256'])
        inventory=load(root,c['cluster_inventory_file']);require('cluster inventory source binding',inventory.get('source_sha256')==digest(src));clusters={x['id']:x for x in M['clusters']}
        require('every discovered cluster dispositioned',set(clusters)==set(inventory['clusters']))
        for k,expected in inventory['clusters'].items():
            group=clusters.get(k,{})
            require('full-cluster coverage '+k,set(group.get('dispositions',{}))==set(expected)==set(group.get('occurrences',[])))
            require('cluster has meaningful disposition '+k,group.get('result') in ['RESOLVED','RETAINED_DISTINCT_FUNCTIONS','RETAINED_PENDING_OWNER'] and bool(group.get('why')))
        require('every move has both-site audit',set(A['moves'])=={m['id'] for m in M['moves']})
        for k,v in A['moves'].items():require('boundary review '+k,bool(v.get('old_location')) and bool(v.get('new_location')) and bool(v.get('disposition')))
        for pointer in A['pointers']:
            f,t=pointer['from'],pointer['to'];ok=f in new and t in new and pointer['required_text'] in new[f]['text']
            if pointer.get('direction')=='forward':ok=ok and order.index(f)<order.index(t)
            require('resolved article pointer '+pointer['id'],ok)
        require('recorded editorial verdict is eligible',R.get('status') in ['PASS','PASS_WITH_OWNER_CHOICES'])
        require('no unresolved confirmed blocking finding',not R.get('unresolved_blocking_findings'))
        require('review names actual scope and limits',bool(R.get('scope')) and bool(R.get('limitations')) and bool(R.get('evidence')))
        require('pending independent content retained',all(new[i]['raw']==old[i]['raw'] for q in M['questions'] for i in q['blocks']))
        if phase=='delivery':
            require('artifact inventory exists','artifacts' in c and len(c['artifacts'])>0)
            for x in c.get('artifacts',[]):require('delivered artifact '+x['path'],digest(safe_file(root,x['path']).read_bytes())==x['sha256'])
            # Check only the registered review navigation surfaces, not archival native-host paths.
            navigation = c.get('navigation_artifacts', [])
            parsed = {}
            for name in navigation:
                page = BeautifulSoup(safe_file(root,name).read_text(encoding='utf-8'),'html.parser')
                parsed[name] = page
                for anchor in page.find_all('a',href=True):
                    href = anchor['href']
                    if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:',href) or href.startswith(('//','%%')):
                        continue
                    path, _, fragment = href.partition('#')
                    target_name = path or name
                    try:
                        target_path = safe_file(root,target_name)
                        ok = True
                        if fragment and target_path.suffix.lower()=='.html':
                            target_page = parsed.get(target_name)
                            if target_page is None:
                                target_page=BeautifulSoup(target_path.read_text(encoding='utf-8'),'html.parser')
                                parsed[target_name]=target_page
                            ok = target_page.find(id=fragment) is not None
                    except (GateError,OSError,ValueError):
                        ok = False
                    require('review navigation '+name+' -> '+href,ok)
            T=load(root,c['transfer_receipt_file'])
            require('canonical transfer verified for exact candidate',T.get('candidate_sha256')==digest(cand) and T.get('canonical_verify')=='PASS' and T.get('destination_result') in ['UNTESTED','PASS','FAIL'])
        require('stage does not silently promote publication',c.get('publication_authority')=='NOT_GRANTED')
    except (KeyError,TypeError,ValueError,OSError,AssertionError) as exc:
        problems.append(type(exc).__name__+': '+str(exc))
    return {'format':'joel-editorial-admission-result-v1','phase':phase,'status':'REVIEW_ELIGIBLE' if not problems else 'NOT_READY','issues':problems,'checks':checks,'semantic_truth_proved':False,'owner_approval_proved':False,'publication_authorized':False}

def package(root: Path, output: Path, expected_contract: str|None=None) -> dict[str,Any]:
    result=assess(root,'delivery',expected_contract)
    if result['status']!='REVIEW_ELIGIBLE':raise GateError('; '.join(result['issues']))
    c=load(root,'GATE-CONTRACT.json');output.parent.mkdir(parents=True,exist_ok=True)
    with tempfile.NamedTemporaryFile(dir=output.parent,suffix='.zip',delete=False) as t:tmp=Path(t.name)
    try:
        with zipfile.ZipFile(tmp,'w',zipfile.ZIP_DEFLATED) as z:
            for item in c['artifacts']:z.write(safe_file(root,item['path']),item['path'])
            z.writestr('GATE-RESULT.json',json.dumps(result,indent=2)+'\n')
            z.write(root/'GATE-CONTRACT.json','GATE-CONTRACT.json')
        with zipfile.ZipFile(tmp) as z:
            if z.testzip() is not None:raise GateError('ZIP integrity failed')
            for item in c['artifacts']:
                if digest(z.read(item['path']))!=item['sha256']:raise GateError('ZIP identity mismatch')
        os.replace(tmp,output)
    finally:
        if tmp.exists():tmp.unlink()
    return {'status':'REVIEW_PACKAGE_READY','path':output.name,'sha256':digest(output.read_bytes()),'publication_authorized':False}

class RegisteredService:
    """Server-owned task enrollment. Caller-supplied PASS, paths or receipts are rejected.

    Enrollment and bundle-write permissions are trust boundaries. Running this under
    the same OS user as a writer does not make the stored semantic records independent.
    """
    def __init__(self, tasks: dict[str,Path], output_dir: Path):
        self.tasks={k:(v.resolve(),digest(safe_file(v.resolve(),'GATE-CONTRACT.json').read_bytes())) for k,v in tasks.items()}
        self.output_dir=output_dir.resolve()
    def request(self, data: dict[str,Any]) -> tuple[int,dict[str,Any]]:
        if not isinstance(data,dict) or set(data)!={'task_id','candidate_sha256'} or not isinstance(data.get('task_id'),str) or not isinstance(data.get('candidate_sha256'),str) or not re.fullmatch('[0-9a-f]{64}',data.get('candidate_sha256','')):
            return 400,{'status':'INVALID_REQUEST','reason':'Only task_id and candidate_sha256 are accepted; no paths, approvals or PASS fields.'}
        item=self.tasks.get(data['task_id'])
        if item is None:return 404,{'status':'UNKNOWN_TASK'}
        root,chash=item
        if digest(safe_file(root,'GATE-CONTRACT.json').read_bytes())!=chash:return 409,{'status':'STALE_ENROLLMENT'}
        contract=load(root,'GATE-CONTRACT.json')
        if data['candidate_sha256']!=contract['candidate_sha256']:return 409,{'status':'STALE_CANDIDATE'}
        try:
            return 200,package(root,self.output_dir/(re.sub('[^a-zA-Z0-9_-]','_',data['task_id'])+'.zip'),chash)
        except GateError as exc:return 409,{'status':'NOT_READY','reason':str(exc)}

def handler_for(service: RegisteredService):
    class Handler(BaseHTTPRequestHandler):
        def do_POST(self):
            if self.path!='/review-package':self.send_error(404);return
            try:
                length=int(self.headers.get('Content-Length','0'))
                if not 0<length<=8192:raise ValueError('Request size')
                code,obj=service.request(json.loads(self.rfile.read(length)))
            except (ValueError,TypeError,OSError) as exc:code,obj=400,{'status':'INVALID_REQUEST','reason':str(exc)}
            body=json.dumps(obj).encode();self.send_response(code);self.send_header('Content-Type','application/json');self.send_header('Content-Length',str(len(body)));self.end_headers();self.wfile.write(body)
        def log_message(self,*args):pass
    return Handler

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('command',choices=['check','package']);p.add_argument('--bundle',type=Path,required=True);p.add_argument('--phase',choices=['editorial','delivery'],default='editorial');p.add_argument('--out',type=Path);a=p.parse_args()
    try:
        if a.command=='package':
            if a.out is None:p.error('--out is required for package')
            r=package(a.bundle,a.out)
        else:r=assess(a.bundle,a.phase)
        s=json.dumps(r,indent=2)+'\n'
        if a.command=='check' and a.out:a.out.write_text(s)
        print(s);return 0 if r['status'] in ['REVIEW_ELIGIBLE','REVIEW_PACKAGE_READY'] else 2
    except GateError as exc:print(json.dumps({'status':'NOT_READY','error':str(exc)}));return 2
if __name__=='__main__':raise SystemExit(main())
