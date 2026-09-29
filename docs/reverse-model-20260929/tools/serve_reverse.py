"""Local LoRA-capable generation server with the exact training serialization."""
import argparse
import hashlib
import json
import os
import time
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
os.environ.setdefault('HF_HOME', '/workspace/.hf_home')
os.environ.setdefault('TOKENIZERS_PARALLELISM', 'false')
os.environ.setdefault('HF_HUB_DISABLE_XET', '1')
from unsloth import FastLanguageModel
import torch
from peft import PeftModel
from train_reverse import MODELS, prefix

def run(args):
    model_id, revision = MODELS[args.condition]
    manifest = json.loads((args.adapter / 'adapter_config.json').read_text())
    assert manifest['r'] == 64
    assert manifest['base_model_name_or_path'] == model_id
    assert manifest.get('revision') == revision
    model, tokenizer = FastLanguageModel.from_pretrained(
        model_name=model_id, revision=revision, use_exact_model_name=True,
        max_seq_length=4096, dtype=torch.bfloat16, load_in_4bit=True,
        device_map='sequential', trust_remote_code=False)
    model = PeftModel.from_pretrained(model, args.adapter, is_trainable=False)
    FastLanguageModel.for_inference(model)
    model.eval()
    args.cache_directory.mkdir(parents=True, exist_ok=True)
    class Handler(BaseHTTPRequestHandler):
        def send(self, code, value):
            body=json.dumps(value,ensure_ascii=False).encode()
            self.send_response(code);self.send_header('Content-Type','application/json')
            self.send_header('Content-Length',str(len(body)));self.end_headers();self.wfile.write(body)
        def do_GET(self):
            if self.path == '/health':
                self.send(200, {'ready':True,'condition':args.condition,'model':model_id,'revision':revision})
            else:
                self.send(404, {'error':'unknown path'})
        def do_POST(self):
            if self.path != '/generate':
                self.send(404, {'error':'unknown path'});return
            request=json.loads(self.rfile.read(int(self.headers['Content-Length'])))
            assert isinstance(request['text'],str) and request['text']
            assert float(request.get('temperature',0.8)) == 0.8
            identifier=request['id']
            assert identifier and all(c.isalnum() or c in '_-' for c in identifier)
            cache_path=args.cache_directory/(identifier+'.json')
            input_hash=hashlib.sha256(request['text'].encode()).hexdigest()
            if cache_path.exists():
                cached=json.loads(cache_path.read_text())
                assert cached['input_sha256']==input_hash
                assert cached['seed']==int(request.get('seed',3407))
                self.send(200,cached);return
            torch.manual_seed(int(request.get('seed',3407)))
            encoded=tokenizer(prefix(request['text']),return_tensors='pt',add_special_tokens=False).to('cuda')
            assert encoded.input_ids.shape[1] + 1024 <= 4096
            torch.cuda.synchronize();begin=time.perf_counter()
            with torch.inference_mode():
                output=model.generate(**encoded,do_sample=True,temperature=0.8,top_p=1.0,
                                      max_new_tokens=1024,use_cache=True,pad_token_id=tokenizer.eos_token_id)
            torch.cuda.synchronize();seconds=time.perf_counter()-begin
            tokens=output[0,encoded.input_ids.shape[1]:].tolist()
            ended=tokenizer.eos_token_id in tokens
            if ended:
                tokens=tokens[:tokens.index(tokenizer.eos_token_id)]
            text=tokenizer.decode(tokens,skip_special_tokens=True).strip()
            words=len(text.split())
            result={'id':identifier,'input_sha256':input_hash,
                            'condition':args.condition,'text':text,'seconds':seconds,
                            'words':words,'seconds_per_300_words':seconds*300/words if words else None,
                            'output_tokens':len(tokens),'truncated':not ended and len(tokens)>=1024,
                            'seed':int(request.get('seed',3407)),'temperature':0.8,
                            'model':model_id,'revision':revision}
            cache_path.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
            self.send(200,result)
    print(json.dumps({'event':'ready','bind':'127.0.0.1','port':args.port,'condition':args.condition}),flush=True)
    HTTPServer(('127.0.0.1',args.port),Handler).serve_forever()

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--condition',choices=list(MODELS),required=True)
    p.add_argument('--adapter',type=Path,required=True);p.add_argument('--port',type=int,default=18001)
    p.add_argument('--cache-directory',type=Path,required=True)
    run(p.parse_args())
