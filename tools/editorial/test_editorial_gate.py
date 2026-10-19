"""Regression tests use copied fixtures. They are not fabricated live review receipts."""
from pathlib import Path
import copy, json, tempfile, shutil, unittest, threading, http.client
from editorial_gate import assess, package, RegisteredService, handler_for, digest, GateError, ThreadingHTTPServer
BASE=Path(__file__).resolve().parents[2]/'articles/intentional-communities/candidate/finalization-20261019'
FILES=['Owner-Source-1454.html','Community-Article-r03-candidate.html','OWNER-ANSWERS.json','ASSEMBLY-LEDGER.json','STRUCTURE-MAP.json','READ-REVIEW.json','BOUNDARY-AUDIT.json','CLUSTER-INVENTORY.json','GATE-CONTRACT.json']
class EditorialGateTests(unittest.TestCase):
 def setUp(self):
  self.tmp=tempfile.TemporaryDirectory();self.root=Path(self.tmp.name)/'bundle';self.root.mkdir();self.out=Path(self.tmp.name)/'output'
  for f in FILES:shutil.copyfile(BASE/f,self.root/f)
  # A fixture-only transfer receipt permits testing package control flow, not real clipboard conversion.
  c=self.read('GATE-CONTRACT.json');self.write('TRANSFER-RECEIPT.json',{'candidate_sha256':c['candidate_sha256'],'canonical_verify':'PASS','destination_result':'UNTESTED','scope':'SYNTHETIC UNIT FIXTURE ONLY'})
  (self.root/'fixture.txt').write_text('Unit-test artifact, not byline text.')
  c['navigation_artifacts']=[]
  c['artifacts']=[{'path':'fixture.txt','sha256':digest((self.root/'fixture.txt').read_bytes())}];self.write('GATE-CONTRACT.json',c)
 def tearDown(self):self.tmp.cleanup()
 def read(self,n):return json.loads((self.root/n).read_text())
 def write(self,n,x):(self.root/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
 def bad(self,phrase):
  r=assess(self.root,'delivery');self.assertEqual(r['status'],'NOT_READY');self.assertTrue(any(phrase in s for s in r['issues']),r['issues'])
 def test_valid_actual_editorial_fixture(self):self.assertEqual(assess(self.root)['status'],'REVIEW_ELIGIBLE')
 def test_valid_package_route(self):self.assertEqual(package(self.root,self.out/'valid.zip')['status'],'REVIEW_PACKAGE_READY')
 def test_source_revision_drift(self):
  with (self.root/'Owner-Source-1454.html').open('ab') as f:f.write(b' ')
  self.bad('exact source')
 def test_candidate_drift(self):
  p=self.root/'Community-Article-r03-candidate.html';p.write_text(p.read_text().replace('The New Age May Dawn Suddenly','Changed title',1));self.bad('exact candidate')
 def test_owner_answer_drift(self):
  x=self.read('OWNER-ANSWERS.json');x['answers']['E19.decision']='Reject';self.write('OWNER-ANSWERS.json',x);self.bad('exact owner answer file')
 def test_stale_reader(self):
  x=self.read('READ-REVIEW.json');x['candidate_sha256']='0'*64;self.write('READ-REVIEW.json',x);self.bad('review record binds candidate')
 def test_missing_known_overlap_occurrence(self):
  x=self.read('STRUCTURE-MAP.json');del x['clusters'][0]['dispositions']['T184'];self.write('STRUCTURE-MAP.json',x);self.bad('full-cluster coverage C-practice')
 def test_shrinking_inventory_not_a_workaround(self):
  x=self.read('CLUSTER-INVENTORY.json');x['clusters']['C-practice'].remove('T184');self.write('CLUSTER-INVENTORY.json',x);self.bad('cluster inventory identity')
 def test_missing_whole_cluster(self):
  x=self.read('STRUCTURE-MAP.json');x['clusters']=x['clusters'][1:];self.write('STRUCTURE-MAP.json',x);self.bad('every discovered cluster')
 def test_missing_map_heading(self):
  x=self.read('STRUCTURE-MAP.json');x['nodes']=[n for n in x['nodes'] if n['id']!='T184'];self.write('STRUCTURE-MAP.json',x);self.bad('outline matches')
 def test_wrong_founder_movement_adjacency(self):
  c=self.read('GATE-CONTRACT.json');c['constraints'][0]['after']='T193';self.write('GATE-CONTRACT.json',c);self.bad('adjacent_h1')
 def test_lost_native_island(self):
  x=self.read('ASSEMBLY-LEDGER.json');x['blocks'][0]['raw']='<p>Missing native object</p>';self.write('ASSEMBLY-LEDGER.json',x);self.bad('native islands preserved')
 def test_missing_two_site_audit(self):
  x=self.read('BOUNDARY-AUDIT.json');del x['moves']['M01']['old_location'];self.write('BOUNDARY-AUDIT.json',x);self.bad('boundary review M01')
 def test_dangling_pointer(self):
  x=self.read('BOUNDARY-AUDIT.json');x['pointers'][0]['to']='NO_SUCH_HEADING';self.write('BOUNDARY-AUDIT.json',x);self.bad('resolved article pointer P01')
 def test_confirmed_blocking_finding(self):
  x=self.read('READ-REVIEW.json');x['unresolved_blocking_findings']=['a real source loss'];self.write('READ-REVIEW.json',x);self.bad('no unresolved')
 def test_changed_output_refuses_package(self):
  (self.root/'fixture.txt').write_text('Tampered artifact');self.bad('delivered artifact');p=self.out/'bad.zip'
  with self.assertRaises(GateError):package(self.root,p)
  self.assertFalse(p.exists())
 def test_no_claimed_publication_authority(self):
  x=self.read('GATE-CONTRACT.json');x['publication_authority']='GRANTED_BY_MODEL';self.write('GATE-CONTRACT.json',x);self.bad('does not silently promote')
 def test_server_rejects_client_pass(self):
  srv=RegisteredService({'task':self.root},self.out);c=self.read('GATE-CONTRACT.json');status,_=srv.request({'task_id':'task','candidate_sha256':c['candidate_sha256'],'approved':True});self.assertEqual(status,400)
 def test_unknown_task_and_no_path_argument(self):
  srv=RegisteredService({'task':self.root},self.out);self.assertEqual(srv.request({'task_id':'../bundle','candidate_sha256':'0'*64})[0],404)
 def test_server_stale_expected_candidate(self):
  srv=RegisteredService({'task':self.root},self.out);self.assertEqual(srv.request({'task_id':'task','candidate_sha256':'0'*64})[0],409)
 def test_server_enrollment_contract_changed(self):
  srv=RegisteredService({'task':self.root},self.out);c=self.read('GATE-CONTRACT.json');c['review_status']='ALTERED';self.write('GATE-CONTRACT.json',c);self.assertEqual(srv.request({'task_id':'task','candidate_sha256':c['candidate_sha256']})[1]['status'],'STALE_ENROLLMENT')
 def test_server_checks_disk_bytes_again(self):
  srv=RegisteredService({'task':self.root},self.out);(self.root/'fixture.txt').write_text('Changed after enrollment');c=self.read('GATE-CONTRACT.json');self.assertEqual(srv.request({'task_id':'task','candidate_sha256':c['candidate_sha256']})[0],409)
 def test_unresolved_review_anchor_is_blocked(self):
  (self.root/'navigation.html').write_text('<a href="destination.html#missing">Source</a>')
  (self.root/'destination.html').write_text('<p id="real">Original</p>')
  c=self.read('GATE-CONTRACT.json');c['navigation_artifacts']=['navigation.html'];self.write('GATE-CONTRACT.json',c);self.bad('review navigation')
 def test_legitimate_review_anchor_is_accepted(self):
  (self.root/'navigation.html').write_text('<a href="destination.html#real">Source</a>')
  (self.root/'destination.html').write_text('<p id="real">Original</p>')
  c=self.read('GATE-CONTRACT.json');c['navigation_artifacts']=['navigation.html'];self.write('GATE-CONTRACT.json',c);self.assertEqual(assess(self.root,'delivery')['status'],'REVIEW_ELIGIBLE')
 def test_traversal_output_artifact(self):
  c=self.read('GATE-CONTRACT.json');c['artifacts'][0]['path']='../outside.txt';self.write('GATE-CONTRACT.json',c);self.bad('Traversal')
 def test_legitimate_empty_spacer_omission_is_not_blocked(self):
  from article_edit import parse
  L=self.read('ASSEMBLY-LEDGER.json');L['new_order'].remove('T106');L['blocks']=[b for b in L['blocks'] if b['id']!='T106'];op,_=parse((self.root/'Owner-Source-1454.html').read_text());raw=op+''.join(b['raw'] for b in L['blocks'])+'</div>';p=self.root/'Community-Article-r03-candidate.html';p.write_text(raw);h=digest(p.read_bytes());L['candidate_sha256']=h;self.write('ASSEMBLY-LEDGER.json',L)
  for name in ['STRUCTURE-MAP.json','READ-REVIEW.json','BOUNDARY-AUDIT.json']:
   x=self.read(name);x['candidate_sha256']=h;self.write(name,x)
  c=self.read('GATE-CONTRACT.json');c['candidate_sha256']=h;c['allowed_omissions']={'T106':{'kind':'EMPTY_SPACER','reason':'An empty spacing paragraph, no content','authority_ref':'SYNTHETIC_TEST_SCOPE'}};self.write('GATE-CONTRACT.json',c)
  self.assertEqual(assess(self.root)['status'],'REVIEW_ELIGIBLE')
 def test_service_rejects_wrong_value_types(self):
  srv=RegisteredService({'task':self.root},self.out);self.assertEqual(srv.request({'task_id':[],'candidate_sha256':'0'*64})[0],400)
 def test_loopback_http_positive_and_hostile_requests(self):
  srv=RegisteredService({'task':self.root},self.out);server=ThreadingHTTPServer(('127.0.0.1',0),handler_for(srv));t=threading.Thread(target=server.serve_forever,daemon=True);t.start();c=self.read('GATE-CONTRACT.json')
  try:
   for payload,expected in [({'task_id':'task','candidate_sha256':c['candidate_sha256']},200),({'task_id':'task','candidate_sha256':'0'*64},409),({'task_id':'task','candidate_sha256':c['candidate_sha256'],'PASS':True},400)]:
    conn=http.client.HTTPConnection('127.0.0.1',server.server_port,timeout=5);body=json.dumps(payload);conn.request('POST','/review-package',body,{'Content-Type':'application/json'});r=conn.getresponse();r.read();self.assertEqual(r.status,expected);conn.close()
  finally:server.shutdown();server.server_close();t.join(3)
if __name__=='__main__':unittest.main(verbosity=2)
