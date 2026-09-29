"""Start the first production batch once the managed fit has truly exited cleanly."""
import argparse
import json
import os
import subprocess
import time
from pathlib import Path
os.environ.setdefault('HF_HUB_DISABLE_XET','1')
ROOT=Path('/workspace/reverse-pilot-20260929')

def main(args):
    while True:
        status=subprocess.check_output(['supervisorctl','status','reverse-pilot-fit'],text=True).strip()
        report=json.loads((ROOT/'gpu-fit.json').read_text()) if (ROOT/'gpu-fit.json').exists() else {}
        if report.get('status')=='FAIL':
            raise SystemExit('Fit failed; benchmark not started. Diagnose the recorded failure.')
        if 'EXITED' in status:
            assert report.get('status')=='PASS' and len(report.get('steps',[]))==2,status
            break
        if 'FATAL' in status or 'STOPPED' in status:
            raise SystemExit('Fit is not running; benchmark not started.')
        time.sleep(10)
    repo=ROOT/'repo';data=repo/'docs/reverse-model-20260929/data'
    tools=repo/'docs/reverse-model-20260929/tools'
    # A bounded production batch measures throughput and acceptance before scaling.
    result=subprocess.run(['/venv/main/bin/python','-u',str(tools/'generate_pairs.py'),
        '--input',str(data/'human-passages.jsonl'),'--output',str(data/'generated'),
        '--batch-size','4','--limit','12','--deadline-unix',str(time.time()+3600)],check=False)
    raise SystemExit(result.returncode)

if __name__=='__main__':
    main(argparse.ArgumentParser().parse_args())
