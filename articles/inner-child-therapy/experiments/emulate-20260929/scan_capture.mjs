// Exact browser-UI scan capture. No downloads, internal app state, or network shortcuts.
import fs from 'node:fs/promises';
import crypto from 'node:crypto';
const index=(state,re)=>Number(state.split('\n').find(l=>re.test(l))?.trim().match(/^\d+/)?.[0]);
export async function startScan(tab,root,item){
 const rows=(await fs.readFile(root+'/runs/pangram.jsonl','utf8')).trim().split('\n').map(JSON.parse);
 if(rows.some(r=>r.check_id===item.check_id))return {error:'completed identity: reuse saved result'};
 if(/E_holdout|REFERENCE_ONLY|\.\./.test(item.text_file))return {error:'excluded source'};
 let state=await tab.getAXState({emit:false,disableDiffing:true});
 if(/button New scan/.test(state)){await tab.click(index(state,/button New scan/));state=await tab.getAXState({emit:false,disableDiffing:true});}
 const record={...item,credits_before:Number(state.match(/text (\d+) left/)?.[1])};
 if(!record.credits_before||record.credits_before<300)return {error:'credit boundary'};
 const input=await fs.readFile(root+'/'+item.text_file,'utf8');record.input_words=input.trim().split(/\s+/).length;
 const boxIndex=index(state,/text entry area/);
 await tab.pressKey(boxIndex,'Control+a');await tab.paste(boxIndex,input,{format:'text'});
 state=await tab.getAXState({emit:false,disableDiffing:true});
 const box=await tab.playwright.getByRole('textbox').evaluate(el=>el.value);
 const uiWords=Number(state.match(/text (\d+)  word/)?.[1]);
 const button=state.split('\n').find(l=>/button.*Check for AI/.test(l));
 if(box!==input||!uiWords||Math.abs(uiWords-record.input_words)/record.input_words>0.080001||/disabled/.test(button))return {error:'paste or minimum gate; not submitted',box_exact:box===input,ui_words:uiWords,input_words:record.input_words};
 record.input_verification={box_exact:true,input_ui_words:uiWords,first10:box.trim().split(/\s+/).slice(0,10).join(' '),last10:box.trim().split(/\s+/).slice(-10).join(' ')};
 record.text_sha256=crypto.createHash('sha256').update(input).digest('hex');
 await fs.appendFile(root+'/runs/admission-events.jsonl',JSON.stringify({...record,event:'verified_before_paid_scan',utc:new Date().toISOString()})+'\n');
 await tab.click(Number(button.trim().match(/^\d+/)[0]));await tab.getAXState({emit:false});
 return {record,input};
}
export async function finishScan(tab,root,pending){
 if(!pending?.record)return {error:'no submitted identity'};
 const overview=await tab.playwright.domSnapshot();const panel=overview.split('- tabpanel "Overview":')[1]?.split('- tabpanel "Notes"')[0];
 if(!panel||!/words scanned/.test(panel))return {error:'unread: wait10seconds, never resubmit'};
 const record={...pending.record,checked_utc:new Date().toISOString(),words_scanned:Number(panel.match(/(\d+) words scanned/)[1]),model:panel.match(/Detection model: ([^"]+)/)?.[1],label:panel.match(/^\s*- generic: ([^\n]+)/)?.[1],percent:{},confidence:panel.match(/- generic: (Confidence[^\n]+)/)?.[1]??null};
 for(const m of panel.matchAll(/- generic: "?(\d+(?:\.\d+)?)"?\n\s*- generic: "?%"?\n\s*- generic: of this text is ?([^\n]*)\n?(?:\s*- generic: ([^\n]+))?/g))record.percent[(m[2]||m[3]).replace(/"$/,'')]=Number(m[1]);
 record.flagged_spans=await tab.playwright.evaluate(()=>Array.from(document.querySelectorAll('span')).filter(el=>getComputedStyle(el).backgroundColor==='rgba(255, 86, 48, 0.1)').map(el=>el.textContent));
 const state=await tab.getAXState({emit:false,disableDiffing:true});record.credits_after=Number(state.match(/text (\d+) left/)[1]);record.credits_cost=record.credits_before-record.credits_after;
 record.input_verification.result_words_within_8_percent=Math.abs(record.words_scanned-record.input_words)/record.input_words<=0.080001;
 await tab.playwright.getByRole('tab',{name:'Details',exact:true}).click();const detailState=await tab.getAXState({emit:false,disableDiffing:true});if(!/tab \(selected[^\n]*Details/.test(detailState))return {error:'detail view unread; preserve result before any repeat'};const details=await tab.playwright.domSnapshot();
 record.segment_confidences=Array.from(details.matchAll(/generic "Confidence level":\n\s*- text: ([^\n]+)/g),m=>m[1]);
 record.pdf_status='omitted: native Save As interrupts owner; downloads disabled';
 await fs.writeFile(root+'/runs/pangram/'+record.check_id+'.overview.txt',overview);await fs.writeFile(root+'/runs/pangram/'+record.check_id+'.details.txt',details);
 await fs.appendFile(root+'/runs/pangram.jsonl',JSON.stringify(record)+'\n');
 return {saved:record.check_id,label:record.label,percent:record.percent,words:record.words_scanned,credits:record.credits_after,segments:record.segment_confidences,highlights:record.flagged_spans.length};
}
