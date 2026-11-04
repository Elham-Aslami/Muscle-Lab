import fs from 'node:fs';
import zlib from 'node:zlib';
import {FBXLoader} from 'three/addons/loaders/FBXLoader.js';
import {mergeVertices} from 'three/addons/utils/BufferGeometryUtils.js';
import {MeshoptSimplifier} from 'meshoptimizer';
await MeshoptSimplifier.ready;
const bytes=fs.readFileSync('../tmp/model/MuscularSystem100.fbx');
const root=new FBXLoader().parse(bytes.buffer.slice(bytes.byteOffset,bytes.byteOffset+bytes.byteLength),'');root.updateMatrixWorld(true);
const matches=[['orbicularis_oculi',/orbicularis_oculi/],['orbicularis_oris',/orbicularis_oris/],['masseter',/part_of_masseter/],['sternocleidomastoid',/sternocleidomastoid_muscle/],['trapezius',/part_of_trapezius/],['rectus_abdominis',/rectus_abdominis/],['external_oblique',/external_abdominal_oblique/],['internal_oblique',/internal_abdominal_oblique/],['erector_spinae',/^(spinalis_|longissimus_|iliocostalis_)/],['deltoid',/part_of_deltoid/],['pectoralis_major',/pectoralis_major/],['latissimus_dorsi',/latissimus_dorsi/],['biceps_brachii',/head_of_biceps_brachii/],['triceps_brachii',/head_of_triceps_brachii/],['brachialis',/^brachialis_/],['brachioradialis',/^brachioradialis_/],['iliopsoas',/^(iliacus_muscle|psoas_major)/],['gluteus_maximus',/^gluteus_maximus_/],['gluteus_medius',/^gluteus_medius_/],['sartorius',/^sartorius_/],['quadriceps',/^(rectus_femoris_|vastus_)/],['biceps_femoris',/head_of_biceps_femoris/],['semitendinosus',/^semitendinosus_muscle/],['semimembranosus',/^semimembranosus_muscle/],['gastrocnemius',/head_of_gastrocnemius/],['tibialis_anterior',/^tibialis_anterior_muscle/]];
const meshes=[];const coverage={};let original=0,final=0;
function compact(g,ratio,error=.008){
 for(const key of Object.keys(g.attributes)){if(key!=='position')g.deleteAttribute(key)}
 g=mergeVertices(g,0.0005);const pos=g.attributes.position.array;let idx=new Uint32Array(g.index.array);
 original+=idx.length/3;
 try{const target=Math.max(120,Math.floor(idx.length*ratio/3)*3);idx=MeshoptSimplifier.simplify(idx,pos,3,target,error,[])[0]}catch{}
 const map=new Map(),verts=[],inds=[];for(const v of idx){if(!map.has(v)){map.set(v,verts.length/3);verts.push(...[pos[v*3],pos[v*3+1],pos[v*3+2]].map(v=>Math.round(v*100)/100))}inds.push(map.get(v))}
 final+=idx.length/3;return {p:verts,i:inds};
}
root.traverse(o=>{
 if(!o.isMesh)return;const name=o.name.toLowerCase();
 // Broad investing fascia would conceal the tested muscles. Retain the real
 // tendons, aponeuroses and retinacula that complete exposed joints and extremities.
 if(/bursa/.test(name)||(/fascia/.test(name)&&!/^tensor_fasciae/.test(name)))return;
 const kind=/sheath|retinaculum|aponeurosis|ligament|raphe|trochlea|tendon|tendinous_arch/.test(name)?'tendon':'muscle';
 const id=kind==='muscle'?(matches.find(([id,re])=>re.test(name))?.[0]||''):'';
 if(id)coverage[id]=(coverage[id]||0)+1;
 const g=o.geometry.clone();g.applyMatrix4(o.matrixWorld);
 meshes.push({id,name:o.name,kind,...compact(g,id?.22:.10)});
});
const {BufferGeometry,Float32BufferAttribute}=await import('three');
const context=JSON.parse(fs.readFileSync('../tmp/model/context-raw.json','utf8')),groups={};
for(const m of context.meshes){
 const g=new BufferGeometry();g.setAttribute('position',new Float32BufferAttribute(m.p,3));g.setIndex(m.i);
 const part=compact(g,.22,.004);const group=groups[m.kind]??={id:'',kind:m.kind,name:'Reference-only '+m.kind,source:'BodyParts3D',sourceParts:[],p:[],i:[]};
 const offset=group.p.length/3;for(const v of part.p)group.p.push(v);for(const i of part.i)group.i.push(i+offset);group.sourceParts.push({name:m.name,sourceId:m.sourceId});
}
meshes.push(...Object.values(groups));
const json=JSON.stringify({meshes,coverage,source:'Z-Anatomy / BodyParts3D',license:'CC BY-SA 4.0; BodyParts3D context CC BY-SA 2.1 Japan',contextRegistration:context.registration,adaptation:'World-space transforms applied; broad investing fascia omitted; tendons and connective tissues retained as context; reference-only skeleton, cartilage, teeth and eye surfaces rigidly registered from BodyParts3D; meshes simplified; coordinates rounded to 0.01 source units.'});
fs.writeFileSync('model.json',json);fs.writeFileSync('model.b64',zlib.gzipSync(json,{level:9}).toString('base64'));
console.log({meshes:meshes.length,original,final,coverage,bytes:json.length,gzip:zlib.gzipSync(json).length});
