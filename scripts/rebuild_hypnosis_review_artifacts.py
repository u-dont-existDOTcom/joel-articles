#!/usr/bin/env python3
"""Reproduce the exact tested review bytes using canonical generators.

The freeze timestamp is presentation metadata, not a new review/test claim.
Article content, row alignment, comments and controls remain generator-owned.
"""
from pathlib import Path
import argparse, importlib.util, importlib.machinery, json, re, hashlib, sys


def load(path):
    loader = importlib.machinery.SourceFileLoader('canonical_interactive_review', str(path))
    spec = importlib.util.spec_from_loader(loader.name, loader)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    loader.exec_module(module)
    return module


def rebuild(root):
    root = root.resolve()
    a = root / 'articles/inner-signal'
    recipe = json.loads((a / 'sync-r03/REVIEW-REBUILD.json').read_text())
    mod = load(root / 'project-sources/interactive_review.py.txt')
    template = (root / 'project-sources/review_interface_template.html.txt').read_text()
    revised = mod.extract_blocks((a/'master.html').read_text())
    original = mod.extract_blocks((a/'source/owner-editor-20260911.html').read_text())
    for name, item in recipe['reviews'].items():
        meta = item['metadata']
        rows = mod.full_draft_rows(revised, {}) if meta['view_mode']=='full-draft' else [x for x in mod.align_blocks(original,revised,{}) if x['state']!='equal']
        keys=['title','artifact_id','baseline_type','row_scope','source_label','new_label','source_filename','revised_filename','source_version','new_version','export_basename','audience_contract','view_mode']
        args={k:meta[k] for k in keys}
        args.update(source_sha=meta['source_sha256'],revised_sha=meta['revised_sha256'],rows=rows)
        output=mod.build_document(template,**args)
        output,count=re.subn(r'"generated_utc": "[^"]+"', '"generated_utc": '+json.dumps(meta['generated_utc']),output)
        if count!=1 or hashlib.sha256(output.encode()).hexdigest()!=item['sha256']:
            raise ValueError(f'Canonical review reproduction differs: {name}')
        (a/'sync-r03'/name).write_text(output)
    return len(recipe['reviews'])

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--root',type=Path,default=Path('.'));args=p.parse_args()
    print(f'Reproduced {rebuild(args.root)} exact canonical reviews')
