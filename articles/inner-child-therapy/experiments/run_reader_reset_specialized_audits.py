#!/usr/bin/env python3
import hashlib,json,os,time,urllib.request,urllib.error
from pathlib import Path
ROOT=Path(__file__).resolve().parent
packet=json.loads((ROOT/"SOURCE-DELTA-SAFETY-READER-RESET-SPECIALIZED-AUDIT-PACKET-20260923.json").read_text())
base=os.environ["UDA_MODEL_GATEWAY_URL"].rstrip("/")
token=os.environ["UDA_MODEL_GATEWAY_TOKEN"]
model=os.environ.get("UDA_MODEL_GATEWAY_MODEL","openai-gpt-6-sol")
endpoint=base+"/v1/chat/completions"
print(json.dumps({"event":"reader_reset_audit_start","case_count":len(packet["cases"]),"model":model,"packet_sha256":hashlib.sha256((ROOT/"SOURCE-DELTA-SAFETY-READER-RESET-SPECIALIZED-AUDIT-PACKET-20260923.json").read_bytes()).hexdigest(),"candidate_sha256":packet["candidate_artifact_sha256"]}),flush=True)
for c in packet["cases"]:
    prompt=packet["prompts"][c["axis"]]
    msg=prompt+"\n\nPREVIOUS CONTEXT:\n"+c["previous"]+"\n\nTARGET:\n"+c["target"]+"\n\nNEXT CONTEXT:\n"+c["next"]
    started=time.time()
    req=urllib.request.Request(endpoint,data=json.dumps({"model":model,"temperature":0,"messages":[{"role":"user","content":msg}]}).encode(),headers={"Authorization":"Bearer "+token,"Content-Type":"application/json"},method="POST")
    try:
        with urllib.request.urlopen(req,timeout=180) as resp: raw=json.loads(resp.read().decode())
        content=raw["choices"][0]["message"]["content"]
        try: parsed=json.loads(content); err=None
        except Exception as exc: parsed=None; err=f"{type(exc).__name__}: {exc}"
        row={"event":"reader_reset_audit_result","case_id":c["case_id"],"axis":c["axis"],"model":raw.get("model"),"response_id":raw.get("id"),"content":content,"parsed":parsed,"parse_error":err,"usage":raw.get("usage"),"elapsed_seconds":round(time.time()-started,3)}
    except Exception as exc:
        row={"event":"reader_reset_audit_transport_error","case_id":c["case_id"],"axis":c["axis"],"error_type":type(exc).__name__,"error":str(exc)[:1500],"elapsed_seconds":round(time.time()-started,3)}
    print(json.dumps(row,ensure_ascii=False),flush=True)
print(json.dumps({"event":"reader_reset_audit_end"}),flush=True)
