"""Freeze A/B inputs and chronological first Emulate outputs; never access E."""
import hashlib
import json
import subprocess
from pathlib import Path

COMMIT='45caa139a94bc5919e26a7026dca05118acc2229'
ROOT='articles/inner-child-therapy/experiments/emulate-20260929/'
OUT=Path('docs/reverse-model-20260929/evaluation')

def read(path):
    assert path.startswith(('inputs/learning/A_joelfixes/','inputs/learning/B_protector/','runs/'))
    return subprocess.check_output(['git','show',COMMIT+':'+ROOT+path],text=True)

def sha(text):
    return hashlib.sha256(text.encode()).hexdigest()

def main():
    inventory=json.loads(read('runs/input-inventory.json'))['learning']
    inputs=[r for r in inventory if r['file'].startswith(('inputs/learning/A_joelfixes/','inputs/learning/B_protector/'))
            and not r.get('reference_only')]
    assert len(inputs)==53
    histories=[json.loads(l) for l in read('runs/emulate.jsonl').splitlines()]
    grades=[json.loads(l) for l in read('runs/pangram.jsonl').splitlines()]
    histories=sorted(enumerate(histories),key=lambda x:(x[1].get('started_utc',''),x[0]))
    cases=[]
    for item in inputs:
        text=read(item['file'])
        assert sha(text)==item['sha256'],item['id']
        first=next((r for _,r in histories if r.get('input_file')==item['file']
                    and r.get('output_file') and r.get('status','completed')=='completed'),None)
        row={'id':item['id'],'set':item['id'][0],'input':text,'input_sha256':sha(text),
             'source_file':ROOT+item['file'],'source_commit':COMMIT,'input_words':len(text.split()),
             'emulate':None,'cached_pangram':[]}
        if first:
            output=read(first['output_file'])
            if first.get('output_sha256'):
                assert sha(output)==first['output_sha256'],first['run_id']
            row['emulate']={'text':output,'sha256':sha(output),'run_id':first['run_id'],
                            'source_file':ROOT+first['output_file'],'started_utc':first.get('started_utc'),
                            'seconds':first.get('elapsed'),'via':first.get('via',first.get('style',{})),
                            'selection':'earliest recorded completed version; file order breaks timestamp ties'}
            for grade in grades:
                if grade.get('text_file')==first['output_file']:
                    if grade.get('text_sha256'):
                        assert grade['text_sha256']==sha(output)
                    row['cached_pangram'].append(grade)
        else:
            row['missing_emulate_reason']='No completed version in the frozen overnight ledger'
        cases.append(row)
    OUT.mkdir(parents=True,exist_ok=True)
    p=OUT/'learning-cases.jsonl'
    p.write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in cases))
    summary={'source_commit':COMMIT,'inputs':len(cases),
             'first_emulate_outputs':sum(r['emulate'] is not None for r in cases),
             'missing_emulate':[r['id'] for r in cases if r['emulate'] is None],
             'outputs_with_cached_pangram':sum(bool(r['cached_pangram']) for r in cases),
             'manifest_sha256':sha(p.read_text()),'E_holdout_accessed':False,
             'scope':'evaluation only; never training data or filter labels'}
    (OUT/'learning-manifest.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(summary,indent=2))

if __name__=='__main__':
    main()
