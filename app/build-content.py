import json
from pathlib import Path
cards=[]
def add(unit, key, name, desc, clue='', action='', scene='', source='', objective='', aliases=None, region=''):
 cards.append(dict(id=key,unit=unit,name=name,description=desc,clue=clue,action=action,scene=scene,source=source,objective=objective or f'Unit {unit}: listed vocabulary and identification objective',aliases=aliases or [],region=region))
muscles=[
('orbicularis_oculi','Orbicularis oculi','Head and neck','Circular muscle surrounding the eye.','Look for the ring around the eyelids.','Closes the eyelids.','pp. 6–8 · Figures 10.2–10.3'),
('orbicularis_oris','Orbicularis oris','Head and neck','Circular muscle surrounding the mouth.','The muscle encircles the lips.','Closes and purses the lips.','p. 8 · Figures 10.2–10.3'),
('masseter','Masseter','Head and neck','Thick muscle on the lateral jaw.','Find it over the mandibular ramus, just in front of the ear.','Elevates the mandible to close the jaw.','pp. 8–9 · Figure 10.3'),
('sternocleidomastoid','Sternocleidomastoid','Head and neck','Oblique strap along the side of the neck.','Runs from the sternum/clavicle toward the mastoid region behind the ear.','Together: flex the neck. One side: tilts the head to the same side and rotates the face to the opposite side.','pp. 8–9 · Figure 10.3'),
('trapezius','Trapezius','Head and neck','Broad superficial muscle of the posterior neck and upper back.','Together the two sides form a large diamond.','Extends the head/neck; elevates, retracts, depresses and upwardly rotates the scapula through different fiber regions.','pp. 9, 14 · Figure 10.9'),
('rectus_abdominis','Rectus abdominis','Trunk','Paired vertical muscles on the anterior abdomen.','The segmented “six-pack” on either side of the midline.','Flexes the trunk and compresses the abdomen.','pp. 11–12 · Figure 10.7'),
('external_oblique','External oblique','Trunk','Superficial lateral abdominal muscle.','Fibers run downward and toward the midline.','Flexes and laterally bends the trunk; rotates it to the opposite side; compresses the abdomen.','pp. 11–12 · Figures 10.7–10.8'),
('internal_oblique','Internal oblique','Trunk','Abdominal muscle deep to the external oblique.','Its upper fibers generally run upward and toward the midline.','Flexes and laterally bends the trunk; rotates it to the same side; compresses the abdomen.','pp. 11–12 · Figures 10.7–10.8'),
('erector_spinae','Erector spinae group','Trunk','Long columns of muscle along the posterior vertebral column.','Includes iliocostalis, longissimus and spinalis; study them as this listed group.','Extends and laterally bends the vertebral column; helps maintain upright posture.','pp. 12–14 · Figure 10.9'),
('deltoid','Deltoid','Trunk','Triangular muscle forming the shoulder cap.','Covers the lateral shoulder.','Abducts the arm. Anterior fibers assist flexion and posterior fibers assist extension.','pp. 15–17 · Figures 10.10–10.11'),
('pectoralis_major','Pectoralis major','Trunk','Large fan-shaped muscle on the anterior chest.','Broad on the chest and narrows toward the upper arm.','Flexes, adducts and medially rotates the arm.','pp. 15–16 · Figure 10.10'),
('latissimus_dorsi','Latissimus dorsi','Trunk','Broad superficial muscle over the lower posterior trunk.','Sweeps from the lower back toward the upper arm.','Extends, adducts and medially rotates the arm.','pp. 14–15 · Figure 10.9'),
('biceps_brachii','Biceps brachii','Upper limb','Superficial two-headed muscle on the anterior upper arm.','Anterior to the humerus and superficial to brachialis.','Flexes the forearm at the elbow and supinates the forearm.','pp. 16–17 · Figure 10.10'),
('triceps_brachii','Triceps brachii','Upper limb','Three-headed muscle on the posterior upper arm.','Look on the back of the arm, opposite biceps.','Extends the forearm at the elbow.','p. 17 · Figure 10.11'),
('brachialis','Brachialis','Upper limb','Elbow flexor deep to biceps on the anterior humerus.','Visible beside and beneath the distal biceps; use deep view.','Flexes the forearm at the elbow.','pp. 16–17 · Figure 10.10'),
('brachioradialis','Brachioradialis','Upper limb','Superficial muscle along the lateral, thumb-side forearm.','Crosses the lateral elbow and runs toward the distal radius.','Flexes the forearm at the elbow, especially with the thumb pointing upward.','pp. 16–20 · Figures 10.10, 10.14'),
('iliopsoas','Iliopsoas','Lower limb','Deep hip-flexor group formed by iliacus and psoas major.','Seen inside the pelvis and beside the lumbar spine; use deep view.','Flexes the thigh at the hip.','pp. 21–23 · Figure 10.17'),
('gluteus_maximus','Gluteus maximus','Lower limb','Large superficial buttock muscle.','Forms most of the posterior buttock contour.','Extends and laterally rotates the thigh.','pp. 20–21 · Figure 10.15'),
('gluteus_medius','Gluteus medius','Lower limb','Fan-shaped muscle on the lateral hip, partly deep to gluteus maximus.','Find it above and lateral to gluteus maximus.','Abducts the thigh and helps stabilize the pelvis during walking.','pp. 20–21 · Figure 10.15'),
('sartorius','Sartorius','Lower limb','Long superficial strap crossing the anterior thigh diagonally.','Runs from the lateral hip to the medial knee.','Flexes, abducts and laterally rotates the thigh; flexes the knee.','pp. 23–24 · Figure 10.17'),
('quadriceps','Quadriceps femoris group','Lower limb','Anterior thigh group: rectus femoris and the three vastus muscles.','Includes the central rectus femoris, lateral/medial masses and deeper vastus intermedius.','Extends the leg at the knee. Rectus femoris also flexes the thigh at the hip.','pp. 23–24 · Figure 10.17'),
('biceps_femoris','Biceps femoris','Lower limb','Lateral hamstring on the posterior thigh.','Its distal tendon runs toward the lateral knee.','Flexes the knee; its long head also extends the thigh.','pp. 24–25 · Figure 10.18'),
('semitendinosus','Semitendinosus','Lower limb','Superficial medial hamstring.','Recognize the long, narrow distal tendon.','Extends the thigh and flexes the knee.','pp. 24–25 · Figure 10.18'),
('semimembranosus','Semimembranosus','Lower limb','Broad medial hamstring deep to semitendinosus.','Has a broad, flattened proximal tendon; use deep view.','Extends the thigh and flexes the knee.','pp. 24–25 · Figure 10.18'),
('gastrocnemius','Gastrocnemius','Lower limb','Two-headed superficial calf muscle.','Forms the prominent upper posterior calf.','Plantarflexes the foot and assists knee flexion.','pp. 25–26 · Figure 10.18'),
('tibialis_anterior','Tibialis anterior','Lower limb','Muscle along the front-lateral side of the tibia.','Anterior shin muscle whose tendon crosses the front of the ankle.','Dorsiflexes and inverts the foot.','pp. 26–28 · Figures 10.20–10.21')]
for key,name,region,desc,clue,action,src in muscles:
 add(10,key,name,desc,clue,action,'muscle','Unit 10 in-lab · '+src,'Unit 10: identify listed muscles and describe their actions',region=region)
add(10,'origin','Origin','The usually more stationary attachment of a muscle; often the proximal attachment.','Distinguish the attachment that usually remains relatively fixed.',scene='terms',source='Unit 10 in-lab · p. 2',objective='Unit 10 vocabulary: origin')
add(10,'insertion','Insertion','The usually more movable attachment of a muscle; often the distal attachment.','During many contractions it moves toward the origin.',scene='terms',source='Unit 10 in-lab · p. 2',objective='Unit 10 vocabulary: insertion')
rows11=[
('epimysium','Epimysium','Connective tissue sheath surrounding the entire muscle.','Epi = outside the whole muscle.','bundle'),
('perimysium','Perimysium','Connective tissue surrounding a fascicle, or bundle of muscle fibers.','Look around one bundle inside the muscle.','bundle'),
('endomysium','Endomysium','Fine connective tissue around an individual muscle fiber.','Look between individual fibers inside a fascicle.','bundle'),
('muscle_fascicle','Fascicle (muscle)','A bundle of skeletal muscle fibers.','A bundle inside the whole muscle; its covering is perimysium.','bundle'),
('muscle_fiber','Skeletal muscle fiber','One long skeletal muscle cell containing many myofibrils.','A fiber is a cell; a fascicle contains many fibers.','bundle'),
('sarcolemma','Sarcolemma','The plasma membrane surrounding a muscle fiber.','The cell membrane, not a connective tissue sheath.','fiber'),
('myofibrils','Myofibrils','Long contractile organelles within a muscle fiber, made of repeating sarcomeres.','Many parallel rods fit inside one muscle fiber.','fiber'),
('myofilaments','Myofilaments','Protein filaments within myofibrils; thick filaments contain myosin and thin filaments contain actin.','Smaller than a myofibril.','sarcomere'),
('sr','Sarcoplasmic reticulum','Membrane network surrounding myofibrils that stores calcium ions.','Weblike network wrapped around the myofibrils.','fiber'),
('t_tubules','T-tubules','Inward extensions of the sarcolemma into the muscle fiber.','A transverse tube runs into the cell.','fiber'),
('motor_end_plate','Motor end plate','Specialized folded region of muscle sarcolemma facing a motor neuron terminal.','The muscle side of the neuromuscular junction.','nmj'),
('muscle_myelin','Myelin sheath','Insulating wrapping around a motor neuron axon approaching a muscle.','Wraps the axon; the terminal itself is unmyelinated.','neuron'),
('skeletal_tissue','Skeletal muscle tissue','Long, parallel, striated fibers with multiple peripheral nuclei.','Look for striations and nuclei at the fiber edges.','skeletal'),
('cardiac_tissue','Cardiac muscle tissue','Striated, branching cells with central nuclei and intercalated discs.','Branches and intercalated discs distinguish it from skeletal muscle.','cardiac'),
('smooth_tissue','Smooth muscle tissue','Spindle-shaped cells with a central nucleus and no striations.','Look for tapered cells and absence of banding.','smooth'),
('sarcomere','Sarcomere','Repeating unit within a myofibril, extending from one Z disc to the next.','Boundaries are the two Z discs.','sarcomere'),
('a_band','A band','Region spanning the full length of thick filaments.','The central dark band.','sarcomere'),
('i_band','I band','Region containing thin filaments without thick filaments.','The lighter band on either side of a Z disc.','sarcomere'),
('z_disc','Z disc','Boundary of a sarcomere where thin filaments are anchored.','A boundary line, not the middle line.','sarcomere'),
('h_zone','H zone','Central region of the A band containing thick filaments without thin filaments.','Central thick-only zone.','sarcomere'),
('m_line','M line','Proteins supporting thick filaments at the center of a sarcomere.','The midline.','sarcomere'),
('nmj_terminal','Axon terminal (NMJ)','Swollen ending of a motor neuron that faces a muscle fiber.','The neuron side of the neuromuscular junction.','nmj'),
('nmj_vesicles','Synaptic vesicles (NMJ)','Small sacs inside a motor neuron terminal that contain acetylcholine.','Small spheres inside the terminal.','nmj'),
('nmj_cleft','Synaptic cleft (NMJ)','Narrow space between the neuron terminal and motor end plate.','The gap between the two cells.','nmj')]
for key,name,desc,clue,scene in rows11:
 src='pp. 5–11 · Figures 11.4–11.6'
 if scene=='nmj':src='pp. 14–16 · Figure 11.8'
 if scene in ('skeletal','cardiac','smooth'):src='pp. 12, 30–31 · Figures 11.7, 11.15'
 add(11,key,name,desc,clue,scene=scene,source='Unit 11 in-lab · '+src,objective='Unit 11: '+('distinguish skeletal, cardiac and smooth muscle' if 'tissue' in key else 'identify skeletal muscle microanatomy / neuromuscular junction structures'))
rows12=[
('cell_body','Cell body','The part of a neuron containing its nucleus and most organelles.','The enlarged central portion.','neuron'),
('dendrite','Dendrite','Branching process extending from the cell body, typically receiving input.','Short, branching extensions near the cell body.','neuron'),
('axon_hillock','Axon hillock','Tapered region where the axon joins the cell body.','The cone-shaped transition into the axon.','neuron'),
('axon','Axon','Long neuron process that carries signals toward axon terminals.','One main long process leaves the cell body.','neuron'),
('myelin','Myelin sheath','Insulating wrapping around portions of an axon.','Separate segments wrapped around the axon.','neuron'),
('node','Node of Ranvier','Gap between adjacent segments of myelin.','Find an exposed gap, not a myelinated segment.','neuron'),
('axon_terminal','Axon terminal','End branch of an axon that communicates with another cell.','Small ending at the far end of the axon.','neuron'),
('synapse','Synapse','Junction where a neuron communicates with another cell.','Includes the sending ending, gap and receiving region.','synapse'),
('synaptic_vesicle','Synaptic vesicle','Membrane-bound sac containing neurotransmitter in a terminal.','Small sphere inside the presynaptic ending.','synapse'),
('synaptic_cleft','Synaptic cleft','Narrow extracellular gap between the sending and receiving cells.','Space between the membranes.','synapse'),
('presynaptic','Presynaptic neuron','The neuron on the sending side of a synapse.','Its terminal contains synaptic vesicles.','synapse'),
('postsynaptic','Postsynaptic cell','The receiving cell at a synapse.','The receiving membrane lies across the cleft.','synapse')]
for key,name,desc,clue,scene in rows12:
 add(12,key,name,desc,clue,scene=scene,source='Unit 12 in-lab · '+('pp. 18–20 · Figure 12.11' if scene=='synapse' else 'pp. 3–11 · Figures 12.2, 12.5–12.7'),objective='Unit 12: identify neuron structures and describe nervous tissue / synapse microanatomy')
rows13=[
('cerebrum','Cerebrum','The large cerebral hemispheres forming the upper part of the brain.','The large folded mass above the brainstem.','brain'),
('frontal_lobe','Frontal lobe','Anterior lobe of the cerebrum.','Toward the forehead.','brain'),
('parietal_lobe','Parietal lobe','Superior-posterior part of each cerebral hemisphere, behind the frontal lobe.','On the upper surface behind the frontal lobe.','brain'),
('temporal_lobe','Temporal lobe','Inferolateral cerebral lobe.','On the side of the brain near the temple.','brain_lateral'),
('occipital_lobe','Occipital lobe','Posterior cerebral lobe.','At the back of the cerebral hemisphere.','brain'),
('cortex','Cerebral cortex','Outer layer of gray matter covering the cerebrum.','Follow the outer folded surface.','brain'),
('corpus_callosum','Corpus callosum','Large C-shaped white matter band between the cerebral hemispheres.','The pale arch in a midsagittal section.','brain'),
('thalamus','Thalamus','Paired central masses of the diencephalon.','The oval region below the corpus callosum and above the hypothalamus.','brain'),
('hypothalamus','Hypothalamus','Region of the diencephalon inferior to the thalamus.','Below and anterior to the thalamus.','brain'),
('epithalamus','Epithalamus','Posterior-superior region of the diencephalon, including the pineal gland.','Look posterior to the thalamus; the pineal gland is a landmark within this region.','brain_model'),
('midbrain','Midbrain','Upper part of the brainstem, between the diencephalon and pons.','Above the pons.','brain'),
('pons','Pons','Rounded bulge on the anterior brainstem.','Between the midbrain and medulla.','brain'),
('medulla','Medulla oblongata','Inferior part of the brainstem, continuous with the spinal cord.','Below the pons and above the spinal cord.','brain'),
('cerebellum','Cerebellum','Highly folded structure posterior to the brainstem.','Behind the pons and medulla; smaller folds than the cerebrum.','brain'),
('ventricles','Ventricles','Connected spaces within the brain that contain cerebrospinal fluid.','The lateral, third and fourth ventricles are parts of this cavity system.','brain'),
('meninges','Meninges','The three protective membranes around the brain and spinal cord.','From outer to inner: dura, arachnoid, pia.','meninges'),
('dura','Dura mater','Tough outermost meningeal membrane.','The outer membrane.','meninges'),
('arachnoid','Arachnoid mater','Middle meningeal membrane.','Between dura and pia; spans over surface grooves.','meninges'),
('pia','Pia mater','Thin innermost meningeal membrane closely attached to nervous tissue.','Follows the tissue surface and its contours.','meninges'),
('spinal_cord','Spinal cord','CNS structure continuous with the medulla and located in the vertebral canal.','In cross-section, gray matter forms a central butterfly shape.','spinal'),
('central_canal','Central canal','Small CSF-containing canal at the center of the spinal cord.','Tiny opening at the center of the gray matter.','spinal'),
('dorsal_ganglion','Dorsal root ganglion','Swelling on the dorsal root containing sensory neuron cell bodies.','A swollen region outside the spinal cord on the dorsal root.','spinal'),
('dorsal_root','Dorsal root','Root through which sensory fibers enter the spinal cord.','Connected with the dorsal root ganglion.','spinal'),
('ventral_root','Ventral root','Root through which motor fibers leave the spinal cord.','The root without a dorsal root ganglion.','spinal'),
('dorsal_horn','Dorsal horn','Posterior projection of spinal gray matter.','The narrower, pointed posterior horn.','spinal'),
('ventral_horn','Ventral horn','Anterior projection of spinal gray matter.','The broader, rounded anterior horn.','spinal'),
('lateral_horn','Lateral horn','Lateral projection of spinal gray matter, prominent in thoracic and upper lumbar levels.','Small side projection between dorsal and ventral horns.','spinal')]
for key,name,desc,clue,scene in rows13:
 src='pp. 6–22 · Figures 13.5–13.15'
 if scene=='spinal':src='pp. 23–28 · Figures 13.16–13.18'
 if scene=='meninges':src='pp. 14–16 · Figure 13.11'
 add(13,key,name,desc,clue,scene=scene,source='Unit 13 in-lab · '+src,objective='Unit 13: identify listed brain / spinal cord structures on models and specimens')
rows14=[
('epineurium','Epineurium','Connective tissue surrounding an entire peripheral nerve.','The outer covering of the whole nerve.','nerve'),
('perineurium','Perineurium','Connective tissue surrounding a nerve fascicle.','A covering around one bundle of nerve fibers.','nerve'),
('endoneurium','Endoneurium','Fine connective tissue around an individual nerve fiber.','The smallest connective tissue covering inside a fascicle.','nerve'),
('nerve_fascicle','Fascicle (nerve)','A bundle of nerve fibers within a peripheral nerve.','One bundle within the whole nerve.','nerve'),
('cranial_nerves','Cranial nerves','Nerves associated with the brain or brainstem.','There are 12 numbered pairs.','terms'),
('spinal_nerves','Spinal nerves','Nerves connected with the spinal cord; formed where dorsal and ventral roots join.','Contain both sensory and motor fibers.','terms'),
('sensory_neuron','Sensory neuron','Carries sensory information toward the CNS.','Afferent = arriving at the CNS.','reflex'),
('interneuron','Interneuron','Neuron within the CNS that connects and processes information between neurons.','An integrating neuron; not every reflex requires an interneuron in its main pathway.','reflex'),
('motor_neuron','Motor neuron','Carries output from the CNS to an effector.','Efferent = exiting the CNS.','reflex')]
for key,name,desc,clue,scene in rows14:
 add(14,key,name,desc,clue,scene=scene,source='Unit 14 in-lab · '+('p. 27 · Figure 14.11' if scene=='reflex' else 'pp. 2–6 · Figures 14.1–14.2'),objective='Unit 14: listed peripheral nerve / reflex-arc vocabulary')
nerves=[('I','Olfactory','Smell.','Small fibers on the inferior frontal region.'),('II','Optic','Vision.','Runs toward the optic chiasm.'),('III','Oculomotor','Most eye movements; raises the upper eyelid; constricts the pupil and adjusts the lens for near vision.','Emerges from the ventral midbrain.'),('IV','Trochlear','Controls the superior oblique muscle of the eye.','Slender nerve that emerges dorsally and wraps around the midbrain.'),('V','Trigeminal','Facial sensation and muscles of chewing.','Large nerve attached to the side of the pons.'),('VI','Abducens','Abducts the eye through the lateral rectus muscle.','Near the midline at the pons–medulla junction.'),('VII','Facial','Facial expression; taste from the anterior two-thirds of the tongue; tear and salivary secretion.','At the lateral pons–medulla junction, beside VIII.'),('VIII','Vestibulocochlear','Hearing and balance.','Lateral to VII at the pons–medulla junction.'),('IX','Glossopharyngeal','Taste and sensation from the posterior one-third of the tongue; assists swallowing and salivation.','Upper rootlets on the lateral medulla.'),('X','Vagus','Swallowing and voice; parasympathetic regulation of many thoracic and abdominal organs.','Rootlets on the lateral medulla below IX.'),('XI','Accessory','Moves the head and shoulders through sternocleidomastoid and trapezius.','Long series of rootlets extending toward the upper spinal cord.'),('XII','Hypoglossal','Tongue movement.','Rootlets on the anterior medulla, medial to IX–XI.')]
for i,(roman,name,action,clue) in enumerate(nerves,1):
 add(14,'cn'+str(i),name+' nerve (CN '+roman+')','Cranial nerve '+roman+'.',clue,action,'cranial','Unit 14 in-lab · pp. 8–11 · Figure 14.3','Unit 14: identify and describe the functions of all 12 cranial nerves',aliases=[name,name+' nerve','CN '+roman,'cranial nerve '+str(i)])
add(14,'reflex_arc','Spinal reflex arc','Receptor → sensory neuron → CNS integration → motor neuron → effector.','A simple stretch reflex can have a direct sensory-to-motor synapse; other reflexes involve interneurons.','Receptor detects a stimulus; sensory neuron carries input to the CNS; CNS integrates; motor neuron carries output; effector responds.','reflex','Unit 14 in-lab · pp. 27–28 · Figures 14.11–14.12','Unit 14: describe a simple spinal reflex arc')
ans=[('ans_heart','Heart','Sympathetic: increases heart rate and force. Parasympathetic: decreases heart rate.'),('ans_pupil','Pupils','Sympathetic: dilates pupils. Parasympathetic: constricts pupils.'),('ans_airway','Airways','Sympathetic: dilates bronchioles. Parasympathetic: constricts bronchioles.'),('ans_digest','Digestion','Sympathetic: generally reduces digestive activity and secretions. Parasympathetic: increases digestive activity and secretions.'),('ans_energy','Energy storage and release','Sympathetic: mobilizes glucose and fats. Parasympathetic: favors energy storage during rest and digestion.'),('ans_blood','Blood vessels','Sympathetic activity constricts many skin and abdominal vessels and helps redistribute blood during activity. Most vessels do not have a direct opposing parasympathetic supply.'),('ans_urine','Urinary function','Sympathetic activity generally favors urine retention. Parasympathetic activity supports bladder emptying.'),('ans_lens','Lens for near vision','Parasympathetic activity adjusts the lens for near vision.'),('sympathetic','Sympathetic division','Supports activity and fight-or-flight responses: faster heart rate, larger pupils and airways, and reduced digestion.'),('parasympathetic','Parasympathetic division','Supports rest-and-digest responses: slower heart rate, smaller pupils, and increased digestion.')]
for key,name,action in ans:
 add(14,key,name,'Autonomic nervous system effects.','Compare the effect on the same target organ.',action,'ans','Unit 14 in-lab · pp. 30–31; Unit 14 pre-lab · Table 14.2','Unit 14: describe the effects of both autonomic branches')
for c in cards:
 c['aliases']+= [c['name'].split(' (')[0]]
 if c['id']=='dorsal_ganglion':c['aliases']+=['dorsal ganglion','posterior root ganglion']
 if c['id']=='medulla':c['aliases']+=['medulla']
 if c['id']=='node':c['aliases']+=['nodes of ranvier','myelin sheath gap']
 if c['id']=='sr':c['aliases']+=['SR']
 if c['id']=='t_tubules':c['aliases']+=['transverse tubule','T tubule','transverse tubules']
 if c['id']=='sternocleidomastoid':c['aliases']+=['SCM']
 for a,b in [('dorsal','posterior'),('ventral','anterior')]:
  if a in c['name'].lower():c['aliases'].append(c['name'].lower().replace(a,b))
Path('app/content.json').write_text(json.dumps(cards,ensure_ascii=False,separators=(',',':')))
print('Cards',len(cards),'by unit',{u:sum(c['unit']==u for c in cards) for u in range(10,15)})
