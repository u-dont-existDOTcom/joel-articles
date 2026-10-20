"""Verify committed package bytes and exact included article/review identities."""
from pathlib import Path
from zipfile import ZipFile
import hashlib,json
T=Path(__file__).resolve().parent
R=T.parents[2]
D=T/'delivery'
sha=lambda b:hashlib.sha256(b).hexdigest()
m=json.loads((D/'DELIVERY-MANIFEST.json').read_text())
for name,digest in m['files'].items():
    assert Path(name).name==name,name
    assert sha((D/name).read_bytes())==digest,name
pairs=[('Community-r04-Approved.zip','Community-Article-r04-approved.html','articles/intentional-communities/master.html',m['community_article_sha256']),('Inner-Child-r03-Editorial-Review.zip','Inner-Child-r03-candidate.html','articles/inner-child-therapy/candidate/editorial-20261020/Inner-Child-r03-candidate.html',m['innerchild_candidate_sha256'])]
for archive,name,source,digest in pairs:
    with ZipFile(D/archive) as z:
        assert z.testzip() is None
        assert sha(z.read('article/'+name))==digest
        assert z.read(name)==z.read('article/'+name)==(R/source).read_bytes()
        for member in z.namelist():
            p=Path(member)
            assert not p.is_absolute() and '..' not in p.parts
        manifests=json.loads(z.read('project/MANIFEST.json'))
        for member in manifests['members']:
            assert sha(z.read(member['path']))==member['sha256'],member['path']
print('PASS: both committed canonical packages, exact source articles, all member hashes and safe paths.')
