import images from './images.json';
export {images};
export const picturePoints={brain:{cerebrum:[.42,.25],frontal_lobe:[.13,.47],parietal_lobe:[.54,.20],occipital_lobe:[.78,.40],cortex:[.50,.12],corpus_callosum:[.37,.425],thalamus:[.425,.54],hypothalamus:[.35,.625],midbrain:[.485,.615],pons:[.52,.70],medulla:[.61,.81],cerebellum:[.755,.665],ventricles:[.28,.50]},brain_model:{epithalamus:[.552,.515]},brain_lateral:{temporal_lobe:[.47,.65]},sheep:{cerebrum:[.52,.31],corpus_callosum:[.51,.47],thalamus:[.59,.54],hypothalamus:[.54,.62],midbrain:[.48,.63],pons:[.42,.68],medulla:[.31,.65],cerebellum:[.27,.39],spinal_cord:[.13,.55]},cranial:{cn1:[.5125,.205],cn2:[.52,.39],cn3:[.5167,.45],cn4:[.4333,.4744],cn5:[.5783,.5674],cn6:[.5142,.5698],cn7:[.425,.600],cn8:[.5675,.6279],cn9:[.432,.647],cn10:[.5683,.6721],cn11:[.4592,.8326],cn12:[.4683,.6814]}};
export const scenePoints={
 bundle:{epimysium:[128,165],perimysium:[179,160],endomysium:[272,198],muscle_fascicle:[235,210],muscle_fiber:[300,225]},
 nerve:{epineurium:[128,165],perineurium:[179,160],endoneurium:[272,198],nerve_fascicle:[235,210]},
 fiber:{sarcolemma:[110,130],myofibrils:[267,188],sr:[355,135],t_tubules:[430,228]},
 neuron:{cell_body:[148,200],dendrite:[77,104],axon_hillock:[216,210],axon:[457,211],myelin:[309,209],muscle_myelin:[309,209],node:[350,210],axon_terminal:[533,164]},
 nmj:{nmj_terminal:[300,150],nmj_vesicles:[330,178],nmj_cleft:[300,242],motor_end_plate:[300,286]},
 synapse:{synapse:[300,240],synaptic_vesicle:[330,178],synaptic_cleft:[300,242],presynaptic:[300,140],postsynaptic:[340,305]},
 sarcomere:{sarcomere:[300,85],myofilaments:[230,165],a_band:[300,290],i_band:[130,290],h_zone:[300,122],m_line:[300,198],z_disc:[80,200]},
 meninges:{meninges:[180,160],dura:[300,97],arachnoid:[300,150],pia:[300,232]},
 spinal:{spinal_cord:[225,168],central_canal:[280,207],dorsal_horn:[250,152],ventral_horn:[248,255],lateral_horn:[325,213],dorsal_root:[392,159],ventral_root:[405,266],dorsal_ganglion:[434,176]},
 reflex:{sensory_neuron:[155,155],interneuron:[300,155],motor_neuron:[445,155],reflex_arc:[300,155]}
};
const esc=s=>String(s).replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('"','&quot;');
function dot(x,y,target,learn,onAll=false){return `<g class="pin ${onAll?'choice-pin':''}" data-pin="${esc(target)}" role="button" tabindex="0" aria-label="${learn?esc(target.replaceAll('_',' ')):'Select structure'}"><circle cx="${x}" cy="${y}" r="13" fill="#0c7c6e" stroke="white" stroke-width="4"/><circle cx="${x}" cy="${y}" r="3" fill="white"/></g>`}
export function pictureVisual(card,opts={}){
 let key=opts.variant==='specimen'&&picturePoints.sheep[card.id]?'sheep':card.scene;
 if(opts.variant==='alternate'&&['skeletal','cardiac','smooth'].includes(key))key+='2';
 let im=images[key];if(!im)return null;
 const points=picturePoints[key]||{},p=points[card.id];
 return `<div class="photo-stage" data-scene="${key}"><img src="${im}" alt="${opts.learn?'Course anatomy reference':'Unlabeled anatomy image'}" draggable="false"/>${opts.find?Object.entries(points).map(([id,xy])=>`<button class="photo-pin choice-pin" data-pin="${id}" style="left:${xy[0]*100}%;top:${xy[1]*100}%" aria-label="Select structure"></button>`).join(''):p?`<span class="photo-pin" style="left:${p[0]*100}%;top:${p[1]*100}%" aria-label="Tagged structure"></span>`:''}</div><p class="visual-caption">${key==='brain_lateral'?'Course diagram · Lateral view':key.includes('brain')||key==='sheep'?'Course specimen / model photograph':key==='cranial'?'Inferior view · brain and cranial nerves':'Course microscope image'} · Labels hidden</p>`
}
export function canVisual(c){return c.scene==='muscle'||!!images[c.scene]||!!scenePoints[c.scene]?.[c.id]}
export function diagram(card,opts={}){
 const pic=pictureVisual(card,opts);if(pic)return pic;
 const kind=card.scene;let shapes='';
 const base=`<svg viewBox="0 0 600 380" class="anatomy-diagram" aria-label="${opts.learn?'Anatomy study diagram':'Unlabeled anatomy diagram'}"><defs><linearGradient id="pink" x2="1" y2="1"><stop stop-color="#f4c0b1"/><stop offset="1" stop-color="#c86e78"/></linearGradient><linearGradient id="blue"><stop stop-color="#a8dedd"/><stop offset="1" stop-color="#398f9d"/></linearGradient></defs>`;
 if(['bundle','nerve'].includes(kind)){
 shapes+=`<ellipse cx="300" cy="195" rx="180" ry="135" fill="${kind==='bundle'?'#f6cdc5':'#e7d5b3'}" stroke="#865d68" stroke-width="13"/>`;
 for(const [x,y]of [[235,185],[370,155],[335,268]]){shapes+=`<ellipse cx="${x}" cy="${y}" rx="64" ry="52" fill="#f9e9db" stroke="#b88e89" stroke-width="9"/>`;for(const[dx,dy]of [[0,0],[-26,-20],[26,-20],[-27,22],[25,22]])shapes+=`<circle cx="${x+dx}" cy="${y+dy}" r="17" fill="${kind==='bundle'?'#ce8590':'#91b6b0'}" stroke="white" stroke-width="4"/>${kind==='nerve'?`<circle cx="${x+dx}" cy="${y+dy}" r="6" fill="#e9b757"/>`:''}`}
 shapes+=`<path d="M285 222 C360 220 445 200 525 220" fill="none" stroke="${kind==='bundle'?'#ce8590':'#e9b757'}" stroke-width="23"/><path d="M285 207 C360 205 445 185 525 205 M285 237 C360 235 445 215 525 235" fill="none" stroke="white" stroke-width="3"/>`;
 }else if(kind==='fiber'){
 shapes+=`<rect x="90" y="105" width="410" height="180" rx="80" fill="#f4d7cf" stroke="#8d5667" stroke-width="6"/>`;
 for(let y=145;y<=245;y+=50)shapes+=`<path d="M130 ${y} L460 ${y}" stroke="#c96e83" stroke-width="24"/>`;
 for(let x=160;x<450;x+=30)shapes+=`<path d="M${x} 120 Q${x+35} 150 ${x} 180 T${x} 270" fill="none" stroke="#d4a742" stroke-width="6" opacity=".85"/>`;
 shapes+='<path d="M430 106V284" stroke="#448f9e" stroke-width="16"/>';
 }else if(kind==='neuron'){
 shapes+=`<path d="M120 170 L70 105 L55 64 M70 105L30 125 M125 240L66 290 L37 305 M66 290L70 332 M143 161L149 83L126 52 M149 83L178 62 M111 207L48 213L20 195 M48 213L27 242" fill="none" stroke="#d1a14c" stroke-width="8" stroke-linecap="round"/><path d="M110 161Q165 139 197 185L230 209 198 234Q161 266 118 239Q88 211 110 161" fill="#f2ce83" stroke="#c29138" stroke-width="3"/><circle cx="150" cy="205" r="25" fill="#9a7cba"/><path d="M218 210H478 M478 210L530 165L552 145 M478 210L530 258L550 275 M478 210L548 210" stroke="#d1a14c" stroke-width="8" fill="none"/>`;
 for(let x=248;x<450;x+=110)shapes+=`<rect x="${x}" y="185" width="92" height="50" rx="20" fill="url(#blue)" opacity=".95" stroke="#4b9299" stroke-width="3"/>`;
 for(const[x,y]of [[552,145],[550,275],[548,210],[533,164]])shapes+=`<circle cx="${x}" cy="${y}" r="10" fill="#e5b14d"/>`;
 }else if(['nmj','synapse'].includes(kind)){
 shapes+=`<path d="M268 30V104 C190 120 180 205 226 220 Q300 235 374 220 C420 205 410 120 332 104 V30" fill="#f3ce81" stroke="#bf964d" stroke-width="4"/>`;
 for(const[x,y]of [[245,160],[280,184],[330,178],[305,136],[355,199]])shapes+=`<circle cx="${x}" cy="${y}" r="12" fill="#db8f95" stroke="#af6477" stroke-width="3"/>`;
 shapes+=`<path d="M150 335V270 Q180 250 210 270 Q220 300 230 270 Q240 250 250 280 Q265 320 275 275 Q285 250 300 280 Q310 320 323 275 Q337 250 347 280 Q360 300 370 270 Q390 250 450 270V335Z" fill="url(#pink)" stroke="#ad6676" stroke-width="4"/>`;
 }else if(kind==='sarcomere'){
 shapes+=`<path d="M80 85V60H520V85" fill="none" stroke="#3a6d75" stroke-width="3"/><path d="M80 110V280 M520 110V280" stroke="#555172" stroke-width="8"/>`;
 for(let y=145;y<260;y+=50){shapes+=`<path d="M80 ${y-10}H260 M340 ${y-10}H520" stroke="#489a9c" stroke-width="7"/><path d="M190 ${y+10}H410" stroke="#c77283" stroke-width="12"/>`;for(let x=195;x<412;x+=22)shapes+=`<path d="M${x} ${y+10}l-8 -12" stroke="#b66275" stroke-width="3"/>`}
 shapes+=`<path d="M300 110V280" stroke="#5d6683" stroke-width="4"/><path d="M190 280V302H410V280 M80 280V302H180V280 M275 120V100H325V120" fill="none" stroke="#738391" stroke-width="3"/>`;
 }else if(kind==='meninges'){
 shapes+=`<rect x="65" y="75" width="470" height="45" rx="10" fill="#c28a94"/><rect x="65" y="139" width="470" height="18" rx="5" fill="#d4b894"/>`;
 for(let x=80;x<530;x+=25)shapes+=`<path d="M${x} 157l12 54m-12 -16l20 -26" fill="none" stroke="#b8c6bf" stroke-width="2"/>`;
 shapes+=`<path d="M65 230Q105 190 140 230T215 230T290 230T365 230T440 230T535 230V320H65Z" fill="#edc4ba" stroke="#348c8b" stroke-width="7"/>`;
 }else if(kind==='spinal'){
 shapes+=`<text x="240" y="47" fill="#6b7788" font-size="14">POSTERIOR</text><text x="243" y="350" fill="#6b7788" font-size="14">ANTERIOR</text><ellipse cx="280" cy="207" rx="133" ry="128" fill="#f4e9c8" stroke="#baaf91" stroke-width="4"/><path d="M280 195 Q256 155 230 112 Q215 165 245 205 Q205 217 225 263 Q248 285 268 245 L280 222 L292 245 Q312 285 335 263 Q355 217 315 205 Q345 165 330 112 Q304 155 280 195" fill="#c9988b" stroke="#a47970" stroke-width="3"/><path d="M320 203l24 10-24 11" fill="#c9988b" stroke="#a47970" stroke-width="2"/><circle cx="280" cy="207" r="7" fill="#fefcf5" stroke="#82775c" stroke-width="2"/><path d="M326 145Q379 130 434 176L510 220 M325 259Q396 293 510 220" fill="none" stroke="#d5aa45" stroke-width="14"/><ellipse cx="434" cy="176" rx="23" ry="16" fill="#e2b64e" stroke="#a8893d" stroke-width="3"/><path d="M510 220H560" stroke="#d5aa45" stroke-width="17"/>`;
 }else if(kind==='reflex'){
 for(const[x,col]of [[155,'#71b6bc'],[300,'#aa98c6'],[445,'#d89aa1']]){shapes+=`<circle cx="${x}" cy="155" r="38" fill="${col}"/><path d="M${x-50} 170l-22 20m22 -20l-20 -18M${x+38} 155h35" fill="none" stroke="${col}" stroke-width="7"/>`}
 shapes+=`<path d="M40 155H105 M205 155H250 M350 155H395 M495 155H555" fill="none" stroke="#617787" stroke-width="3"/><text x="30" y="240" font-size="16" fill="#6b7788">Receptor</text><text x="263" y="240" font-size="16" fill="#6b7788">CNS</text><text x="498" y="240" font-size="16" fill="#6b7788">Effector</text><text x="140" y="300" font-size="13" fill="#6b7788">Example with an interneuron; not every reflex uses one.</text>`;
 }else return `<div class="concept-visual"><span class="concept-symbol">${kind==='ans'?'↔':'Aa'}</span><p>${kind==='ans'?'Sympathetic · Parasympathetic':'Recall the term'}</p></div>`;
 const points=scenePoints[kind]||{},p=points[card.id];
 const pins=opts.find?Object.entries(points).filter(([id])=>!['meninges','reflex_arc','muscle_myelin'].includes(id)).map(([id,xy])=>dot(...xy,id,false,true)).join(''):p?dot(...p,card.id,!!opts.learn):'';
 return base+shapes+pins+'</svg><p class="visual-caption">Schematic study diagram · Not to scale</p>';
}
