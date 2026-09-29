"""Budgeted single-call evaluation client. Credentials never enter evidence."""
import argparse
import hashlib
import json
import os
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

def main(args):
    rows=[json.loads(l) for l in args.cases.read_text().splitlines()]
    case=next(r for r in rows if r['id']==args.id)
    assert not case.get('emulate'), 'Existing Emulate output must be reused'
    text=case.get('ai',case.get('input'))
    assert isinstance(text,str) and text
    words=len(text.split())
    assert 1<=words<=3000
    args.output.mkdir(parents=True,exist_ok=True)
    reservations=list(args.output.glob('*.reservation.json'))
    used=0
    for path in reservations:
        entry=json.loads(path.read_text())
        # Pending/ambiguous work consumes the full reservation until recovered.
        used+=entry.get('words_charged',entry['reserved_words'])
    assert used+words<=3000, f'Word cap: {used}+{words}>3000'
    destination=args.output/(args.id+'.reservation.json')
    assert not destination.exists(), 'Reservation exists: recover; never resubmit'
    key=os.environ.get('EMULATE_API_KEY')
    if not key:
        assert args.credential_file is not None
        key=args.credential_file.read_text().strip()
    def request(path,body=None):
        data=None if body is None else json.dumps(body,ensure_ascii=False).encode()
        req=urllib.request.Request('https://www.tryemulate.ai'+path,data=data,
            headers={'Authorization':'Bearer '+key,'Content-Type':'application/json'})
        with urllib.request.urlopen(req,timeout=90) as r:
            return json.load(r)
    before=request('/v1/me')['words_left']
    assert before>=words
    reservation={'id':args.id,'input_sha256':hashlib.sha256(text.encode()).hexdigest(),
                 'reserved_words':words,'started_utc':datetime.now(timezone.utc).isoformat(),
                 'status':'reserved_before_POST','balance_before':before,'task_word_cap':3000}
    destination.write_text(json.dumps(reservation,indent=2)+'\n')
    started=time.perf_counter()
    try:
        response=request('/v1/humanize',{'text':text})
    except urllib.error.HTTPError as e:
        raw=e.read().decode(errors='replace')
        reservation.update(status='http_error_no_resubmit',http_status=e.code,
                           error_body=raw,seconds=time.perf_counter()-started)
        after=request('/v1/me')['words_left']
        reservation.update(balance_after=after,words_charged=max(0,before-after))
        destination.write_text(json.dumps(reservation,indent=2)+'\n')
        print(json.dumps({'id':args.id,'http_status':e.code,'words_charged':reservation['words_charged'],
                          'message':raw[:500]}),flush=True)
        return
    elapsed=time.perf_counter()-started
    assert isinstance(response.get('text'),str)
    after=request('/v1/me')['words_left']
    charged=response['words']['charged']
    record={**reservation,'status':'completed','text':response['text'],
            'output_sha256':hashlib.sha256(response['text'].encode()).hexdigest(),
            'output_words':len(response['text'].split()),'words_charged':charged,
            'provider_id':response['id'],'seconds':elapsed,'balance_after':after,
            'provider_reads_human_claim':response.get('reads_human'),
            'style':'API defaults; no style settings exposed','source':'Emulate API first output'}
    (args.output/(args.id+'.json')).write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
    reservation.update(status='completed',words_charged=charged,balance_after=after,
                       output_sha256=record['output_sha256'])
    destination.write_text(json.dumps(reservation,indent=2)+'\n')
    assert used+charged<=3000, 'Provider charge exceeded reserved budget; stop all further calls'
    print(json.dumps({'id':args.id,'status':'completed','charged':charged,
                      'output_words':record['output_words'],'seconds':elapsed,'total_used':used+charged}),flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--cases',type=Path,required=True)
    p.add_argument('--id',required=True);p.add_argument('--output',type=Path,required=True)
    p.add_argument('--credential-file',type=Path)
    main(p.parse_args())
