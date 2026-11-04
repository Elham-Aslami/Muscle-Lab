"""Prepare non-assessed anatomical context from the already supplied BodyParts3D archive.

Run from the project root. A rigid registration uses matching muscle surfaces
to place the older reference anatomy in the Z-Anatomy coordinate system.
"""
import json, re, zipfile, gzip, base64
from pathlib import Path
import numpy as np
from scipy.spatial import cKDTree

folder=Path('tmp/model')
rows=[r.split('\t') for r in (folder/'isa_element_parts.txt').read_text().splitlines()[1:]]
archive=zipfile.ZipFile(folder/'isa_BP3D_4.0_obj_99.zip')
cache={}
def obj(key):
    if key in cache: return cache[key]
    raw=archive.read('isa_BP3D_4.0_obj_99/'+key+'.obj').decode()
    vertices=[]; faces=[]
    for line in raw.splitlines():
        if line.startswith('v '): vertices.append([float(x) for x in line.split()[1:4]])
        elif line.startswith('f '):
            ids=[int(x.split('/')[0])-1 for x in line.split()[1:]]
            for k in range(1,len(ids)-1): faces.extend([ids[0],ids[k],ids[k+1]])
    p=np.asarray(vertices);p=p[:,[0,2,1]]*.1;p[:,2]*=-1
    name=re.search(r'# English name : (.*)',raw).group(1)
    cache[key]=(p,faces,name)
    return cache[key]

model=json.loads(gzip.decompress(base64.b64decode(Path('app/model.b64').read_text())))
pairs=[
 ('FJ1439','Tibialis_anterior_muscler'),('FJ1436','Semitendinosus_muscler'),
 ('FJ1512','Short_head_of_biceps_brachiir'),('FJ1478','Long_head_of_biceps_brachiir'),
 ('FJ1486','Brachialis_muscler'),('FJ1434','Sartorius_muscler'),
 ('FJ1418','Gluteus_maximus_muscler'),('FJ1595','Sternocleidomastoid_muscler')]
pairs+= [(('FJ1573' if key=='FJ1595' else key+'M'),name[:-1]+'l') for key,name in list(pairs)]
clouds=[]
for key,name in pairs:
    p=obj(key)[0];q=np.asarray(next(m['p'] for m in model['meshes'] if m['name']==name)).reshape(-1,3)
    p=p[::max(1,len(p)//1200)]
    clouds.append((key,p,cKDTree(q)))
# One rigid registration for all bones: no independent stretching of structures.
R=np.eye(3);t=np.array([0.,6.5,-10.9])
for _ in range(35):
    src=[];dst=[]
    for key,p,tree in clouds:
        dist,idx=tree.query(p@R+t)
        keep=dist<=np.quantile(dist,.85)
        src.append(p[keep]);dst.append(tree.data[idx[keep]])
    a=np.concatenate(src);b=np.concatenate(dst);ac=a.mean(0);bc=b.mean(0)
    u,s,vt=np.linalg.svd((a-ac).T@(b-bc))
    fix=np.eye(3);fix[-1,-1]=np.linalg.det(u@vt)
    R=u@fix@vt;t=bc-ac@R
registration={'rotation':R.tolist(),'translation_cm':t.tolist(),'method':'Rigid registration to 16 corresponding bilateral muscle surfaces; no per-bone stretching.','surface_residuals_cm':{key:float(np.median(tree.query(p@R+t)[0])) for key,p,tree in clouds}}
selected={}
for concept,kind in [('bone organ','bone'),('tooth','tooth'),('cartilage organ','cartilage'),('sclera','eye'),('iris','iris')]:
    for row in rows:
        if row[1]==concept: selected[row[2]]=kind
meshes=[]
for key,kind in selected.items():
    p,indices,name=obj(key);p=p@R+t
    meshes.append({'id':'','name':name,'kind':kind,'source':'BodyParts3D','sourceId':key,'p':np.round(p,3).reshape(-1).tolist(),'i':indices})
(folder/'context-raw.json').write_text(json.dumps({'meshes':meshes,'registration':registration},separators=(',',':')))
print(json.dumps({'meshes':len(meshes),'kinds':{k:list(selected.values()).count(k) for k in set(selected.values())},'registration':registration},indent=2))
