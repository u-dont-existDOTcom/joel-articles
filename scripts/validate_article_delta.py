#!/usr/bin/env python3
"""Run the existing content validator; reject target or newly introduced findings.

Existing failures in unrelated registered article families are reported, not hidden
or repaired under another article's authority. Does not change validator semantics.
"""
import argparse,json
from pathlib import Path
from validate_content_repository import validate_repository

def normalize(findings,root):
    return [{**f,'path':f['path'].replace(str(root.resolve())+'/', '')} for f in findings]
def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--root',type=Path,required=True);p.add_argument('--baseline-root',type=Path,required=True);p.add_argument('--article',required=True);p.add_argument('--out',type=Path,required=True);a=p.parse_args()
    before=normalize(validate_repository(a.baseline_root),a.baseline_root);after=normalize(validate_repository(a.root),a.root)
    target=lambda f:a.article in f['path'] or f"'{a.article}'" in f['message']
    key=lambda f:json.dumps(f,sort_keys=True)
    target_findings=[f for f in after if target(f)]
    old_other={key(f) for f in before if not target(f)}
    new_other=[f for f in after if not target(f) and key(f) not in old_other]
    result={'format':'article-scoped-validation-delta-v1','article':a.article,'baseline_findings':before,'current_findings':after,'target_findings':target_findings,'new_unrelated_findings':new_other,'global_result':'pass' if not after else 'fail-existing-findings','scope_result':'pass' if not target_findings and not new_other else 'fail'}
    a.out.write_text(json.dumps(result,indent=2)+'\n');print(result['scope_result'],len(after),'global findings')
    return int(result['scope_result']!='pass')
if __name__=='__main__':raise SystemExit(main())
