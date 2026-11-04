import * as THREE from 'three';
import {OrbitControls} from 'three/addons/controls/OrbitControls.js';
let dataPromise, viewer;
export async function modelData(){
 if(!dataPromise)dataPromise=(async()=>{const b64=document.getElementById('mesh-data').textContent.trim();const bytes=Uint8Array.from(atob(b64),c=>c.charCodeAt(0));const stream=new Blob([bytes]).stream().pipeThrough(new DecompressionStream('gzip'));return JSON.parse(await new Response(stream).text())})();
 return dataPromise;
}
const posterior=new Set(['trapezius','latissimus_dorsi','erector_spinae','gluteus_maximus','gluteus_medius','biceps_femoris','semitendinosus','semimembranosus','gastrocnemius','triceps_brachii']);
const deep=new Set(['brachialis','internal_oblique','iliopsoas','erector_spinae','semimembranosus']);
const contextColors={bone:0xe9ddc3,tooth:0xf5edda,cartilage:0xc6d9d5,tendon:0xdbcdb5,eye:0xf1eee4,iris:0x415a56};
export async function mountViewer(host,opts={}){
 if(!host)return null;
 host.innerHTML='<div class="loading">Preparing the anatomy model…</div>';
 try{
 if(!viewer){const data=await modelData();if(!host.isConnected)return null;if(!viewer)viewer=new AnatomyViewer(data)}
 viewer.attach(host,opts);return viewer;
 }catch(e){host.innerHTML='<div class="fallback"><strong>3D is unavailable in this browser.</strong><p>The image reference and all study modes remain available.</p></div>';if(opts.fallback){const im=new Image();im.src=opts.fallback;im.alt='Anatomical reference';host.prepend(im)}host.closest('.study-card,.quiz-visual')?.querySelectorAll('.viewer-tools button').forEach(b=>b.disabled=true);console.warn('3D unavailable',e);return null}
}
export function disposeView(){if(viewer)viewer.host=null}
export function currentViewer(){return viewer}
class AnatomyViewer{
 constructor(data){
 this.scene=new THREE.Scene();this.scene.background=new THREE.Color('#edf3f2');
 this.camera=new THREE.PerspectiveCamera(33,1,.1,2000);this.camera.position.set(0,95,350);
 this.renderer=new THREE.WebGLRenderer({antialias:true,alpha:false,preserveDrawingBuffer:true});this.renderer.setPixelRatio(Math.min(devicePixelRatio,1.5));this.renderer.setClearColor('#edf3f2');this.renderer.outputColorSpace=THREE.SRGBColorSpace;
 this.renderer.domElement.setAttribute('aria-label','Interactive 3D anatomy. Only study-guide muscles can be selected. Surrounding anatomy is reference only. Use the buttons for keyboard view control.');this.renderer.domElement.setAttribute('tabindex','0');
 this.controls=new OrbitControls(this.camera,this.renderer.domElement);this.controls.target.set(0,88,0);this.controls.enableDamping=false;this.controls.minDistance=8;this.controls.maxDistance=600;this.controls.addEventListener('change',()=>this.draw());
 this.scene.add(new THREE.HemisphereLight(0xffffff,0x79838b,2.5));const key=new THREE.DirectionalLight(0xfff7eb,2.4);key.position.set(-130,230,210);this.scene.add(key);const rim=new THREE.DirectionalLight(0xb7dbef,1.7);rim.position.set(100,140,-150);this.scene.add(rim);
 this.meshes=[];this.coverage=data.coverage;this.bounds={};
 for(const m of data.meshes){const g=new THREE.BufferGeometry();g.setAttribute('position',new THREE.Float32BufferAttribute(m.p,3));g.setIndex(m.i);g.computeVertexNormals();const baseColor=m.id?0xb8736b:(contextColors[m.kind]??0xb09891);const mat=new THREE.MeshStandardMaterial({color:baseColor,roughness:m.kind==='eye'?.4:.8,metalness:0,side:THREE.DoubleSide});const mesh=new THREE.Mesh(g,mat);mesh.userData={id:m.id,sourceName:m.name,kind:m.kind||'muscle',baseColor};mesh.frustumCulled=true;this.scene.add(mesh);this.meshes.push(mesh);if(m.id){if(!this.bounds[m.id])this.bounds[m.id]=new THREE.Box3();this.bounds[m.id].expandByObject(mesh)}}
 this.fullBounds=new THREE.Box3();this.meshes.forEach(m=>this.fullBounds.expandByObject(m));
 this.raycaster=new THREE.Raycaster();this.pointer=new THREE.Vector2();this.down=null;
 this.renderer.domElement.addEventListener('pointerdown',e=>this.down={x:e.clientX,y:e.clientY});
 this.renderer.domElement.addEventListener('pointerup',e=>{if(!this.down||Math.hypot(e.clientX-this.down.x,e.clientY-this.down.y)>7)return;const b=this.renderer.domElement.getBoundingClientRect();this.pointer.set((e.clientX-b.left)/b.width*2-1,-(e.clientY-b.top)/b.height*2+1);this.raycaster.setFromCamera(this.pointer,this.camera);const pool=this.meshes.filter(m=>m.visible&&(!this.isDeep||m.userData.id===this.selected));const hits=this.raycaster.intersectObjects(pool,false);if(hits[0]?.object.userData.id&&this.opts.onPick){this.preserveNextAttach=!!this.opts.preserveOnPick;this.opts.onPick(hits[0].object.userData.id)}});
 this.renderer.domElement.addEventListener('keydown',e=>{if(['ArrowLeft','ArrowRight','ArrowUp','ArrowDown'].includes(e.key)){e.preventDefault();const v=this.camera.position.clone().sub(this.controls.target),s=new THREE.Spherical().setFromVector3(v);s.theta+=(e.key==='ArrowLeft'?.15:e.key==='ArrowRight'?-.15:0);s.phi=Math.max(.1,Math.min(Math.PI-.1,s.phi+(e.key==='ArrowUp'?-.1:e.key==='ArrowDown'?.1:0)));this.camera.position.copy(this.controls.target).add(new THREE.Vector3().setFromSpherical(s));this.controls.update();this.draw()}});
 this.ro=new ResizeObserver(()=>this.resize());
 }
 attach(host,opts){const preserve=this.preserveNextAttach||(!!opts.viewKey&&opts.viewKey===this.opts?.viewKey&&opts.preserveView!==false);this.preserveNextAttach=false;this.ro.disconnect();this.host=host;this.opts=opts;host.innerHTML='';host.append(this.renderer.domElement);this.ro.observe(host);this.selected=opts.selected||null;if(!preserve){this.isolate=false;this.isDeep=opts.deep??deep.has(this.selected)}this.highlight=opts.highlight!==false;this.apply();if(!preserve)this.focus(this.selected,opts.overview);this.resize()}
 apply(){for(const [act,on] of [['deep',this.isDeep],['isolate',this.isolate]]){const b=document.querySelector('[data-act="'+act+'"]');if(b){b.classList.toggle('active',!!on);b.setAttribute('aria-pressed',String(!!on));b.disabled=!this.selected}}const focusButton=document.querySelector('[data-act="focus-muscle"]');if(focusButton)focusButton.disabled=!this.selected;for(const m of this.meshes){const id=m.userData.id,isSel=id&&id===this.selected;m.visible=!(this.isolate&&!isSel);m.material.color.setHex(isSel&&this.highlight?0x127d72:m.userData.baseColor);m.material.emissive.setHex(isSel&&this.highlight?0x003d31:0);m.material.emissiveIntensity=.16;m.material.transparent=this.isDeep&&!isSel;m.material.opacity=this.isDeep&&!isSel?.08:1;m.material.depthWrite=!(this.isDeep&&!isSel)}this.draw()}
 select(id,focus=false){this.selected=id;this.apply();if(focus)this.focusSelection()}
 focusSelection(){const b=this.bounds[this.selected];if(!b)return;const direction=this.camera.position.clone().sub(this.controls.target).normalize(),center=b.getCenter(new THREE.Vector3()),span=Math.max(b.getSize(new THREE.Vector3()).length()*1.7,40);this.controls.target.copy(center);this.camera.position.copy(center).addScaledVector(direction,span);this.controls.update();this.draw()}
 focus(id,overview=false){const b=id&&this.bounds[id]&&!overview?this.bounds[id]:this.fullBounds;const center=b.getCenter(new THREE.Vector3());let span=b.getSize(new THREE.Vector3()).length();if(!id||overview)span=345;else span=Math.max(span*1.7,40);this.controls.target.copy(center);const angle=posterior.has(id)?Math.PI:0;this.camera.position.copy(center).add(new THREE.Vector3(Math.sin(angle)*span,.03*span,Math.cos(angle)*span));this.controls.update();this.draw()}
 preset(view){if(view==='full'){this.focus(null,true);return}const dist=this.camera.position.distanceTo(this.controls.target);const angle={front:0,back:Math.PI,left:Math.PI/2,right:-Math.PI/2}[view];if(view==='reset'){this.selected=this.opts.selected||null;this.isolate=false;this.isDeep=deep.has(this.selected);this.apply();this.focus(this.selected,this.opts.overview);return}this.camera.position.copy(this.controls.target).add(new THREE.Vector3(Math.sin(angle)*dist,0,Math.cos(angle)*dist));this.controls.update();this.draw()}
 toggleDeep(){this.isDeep=!this.isDeep;this.isolate=false;this.apply();return this.isDeep}
 toggleIsolate(){if(!this.selected)return false;this.isolate=!this.isolate;this.apply();return this.isolate}
 zoom(f){this.camera.position.sub(this.controls.target).multiplyScalar(f).add(this.controls.target);this.controls.update();this.draw()}
 resize(){if(!this.host?.isConnected)return;const w=this.host.clientWidth,h=this.host.clientHeight;if(w<1||h<1)return;this.camera.aspect=w/h;this.camera.updateProjectionMatrix();this.renderer.setSize(w,h);this.draw()}
 draw(){if(!this.host?.isConnected||this.frame)return;this.frame=requestAnimationFrame(()=>{this.frame=null;this.controls.update();this.renderer.render(this.scene,this.camera)})}
 snapshot(){this.renderer.render(this.scene,this.camera);return this.renderer.domElement.toDataURL('image/webp',.85)}
}
