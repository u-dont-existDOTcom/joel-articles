"""One cached output per frozen evaluation input, temperature 0.8."""
import argparse
import hashlib
import json
import time
import urllib.request
from pathlib import Path

def main(args):
    cases=[json.loads(l) for l in args.cases.read_text().splitlines()]
    args.output.mkdir(parents=True,exist_ok=True)
    for index,case in enumerate(cases):
        identifier=case['id'];text=case.get('ai',case.get('input'))
        assert isinstance(text,str) and text
        destination=args.output/(identifier+'.json')
        expected=hashlib.sha256(text.encode()).hexdigest()
        if destination.exists():
            result=json.loads(destination.read_text())
            assert result['input_sha256']==expected and result['condition']==args.condition
            continue
        seed=3407+int(hashlib.sha256(identifier.encode()).hexdigest()[:8],16)%1000000
        request=urllib.request.Request('http://127.0.0.1:18001/generate',
            data=json.dumps({'id':identifier,'text':text,'seed':seed,'temperature':0.8}).encode(),
            headers={'Content-Type':'application/json'})
        with urllib.request.urlopen(request,timeout=600) as response:
            result=json.load(response)
        assert result['input_sha256']==expected and result['condition']==args.condition
        destination.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
        print(json.dumps({'id':identifier,'condition':args.condition,'seconds':result['seconds'],
                          'words':result['words'],'truncated':result['truncated']}),flush=True)
        if args.deadline_unix and time.time()>=args.deadline_unix:
            print('DEADLINE_REACHED: completed outputs retained in server cache',flush=True);break

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--cases',type=Path,required=True)
    p.add_argument('--condition',choices=['base','instruct'],required=True)
    p.add_argument('--output',type=Path,required=True);p.add_argument('--deadline-unix',type=float,default=0)
    main(p.parse_args())
