#!/usr/bin/env python3
"""Replay an explicit, hash-bound article patch plan; never infer replacement text."""
from __future__ import annotations
import argparse,hashlib,json
from pathlib import Path

def sha(text: str) -> str: return hashlib.sha256(text.encode('utf-8')).hexdigest()
def apply(source: str, plan: dict) -> str:
    if plan.get('format')!='exact-anchor-patches-v1' or sha(source)!=plan.get('baseline_sha256'):
        raise ValueError('Wrong source identity or patch contract')
    out=source
    for p in plan['patches']:
        old,new=p['before'],p['after']
        if sha(old)!=p['before_sha256'] or sha(new)!=p['after_sha256']:
            raise ValueError(f"Patch text hash mismatch: {p['id']}")
        if out.count(old)!=1: raise ValueError(f"Non-unique/missing anchor: {p['id']}")
        start=out.index(old)
        if start!=p['current_start']: raise ValueError(f"Patch position drift: {p['id']}")
        out=out[:start]+new+out[start+len(old):]
    if sha(out)!=plan['candidate_sha256']:raise ValueError('Candidate identity mismatch')
    return out

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('source',type=Path);p.add_argument('plan',type=Path);p.add_argument('--out',type=Path,required=True);a=p.parse_args()
    result=apply(a.source.read_text(encoding='utf-8'),json.loads(a.plan.read_text(encoding='utf-8')))
    a.out.write_text(result,encoding='utf-8');print(sha(result))
if __name__=='__main__':main()
