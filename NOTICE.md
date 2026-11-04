# Sources and attribution

## Exam content

Scope: the user's Bio270 Fall 26 Study Guide for Practical 2, Units 10–14. Supporting explanations, model inventories, and images come from the supplied Top Hat workbook chapters. Individual study cards retain their unit, source reference, and objective. Small supporting sarcomere structures are drawn from the workbook's muscle model inventories.

Basic muscle-action and autonomic-effect wording was cross-checked with OpenStax Anatomy and Physiology 2e:

- https://openstax.org/books/anatomy-and-physiology-2e/pages/11-6-appendicular-muscles-of-the-pelvic-girdle-and-lower-limbs
- https://openstax.org/books/anatomy-and-physiology-2e/pages/15-1-divisions-of-the-autonomic-nervous-system

## 3D anatomy

Z-Anatomy, models by Gauthier Kervyn and contributors. FBX distribution by Lluís Vinent Juanico. Derived from BodyParts3D, The Database Center for Life Science (DBCLS).

- Project: https://github.com/Z-Anatomy/Models-of-human-anatomy
- FBX distribution: https://github.com/LluisV/Z-Anatomy
- Source file: https://raw.githubusercontent.com/LluisV/Z-Anatomy/PC-Version/Resources/Models/FBX/MuscularSystem100.fbx
- Model and adaptation license: Creative Commons Attribution-ShareAlike 4.0 International, https://creativecommons.org/licenses/by-sa/4.0/
- Legacy BodyParts3D attribution: Creative Commons Attribution-ShareAlike 2.1 Japan, https://creativecommons.org/licenses/by-sa/2.1/jp/

The Z-Anatomy geometry and its adaptations remain under CC BY-SA 4.0. Modifications: applied world-space transforms; omitted broad investing fascia and bursae; retained tendons, aponeuroses and retinacula as reference context; simplified meshes; rounded coordinates to 0.01 source units; applied study colors and lighting; mapped geometry to the 26 required muscle entries/groups. The combined adapted model has 575 mesh objects and 528,789 triangles. No endorsement by the original creators is implied.

### Additional BodyParts3D reference anatomy

BodyParts3D, © The Database Center for Life Science, licensed under Creative Commons Attribution-ShareAlike 2.1 Japan. Source archive: `isa_BP3D_4.0_obj_99.zip`, compatibility version 4.0, with the supplied `isa_element_parts.txt` mapping. Source license notice: http://dbarchive.biosciencedbc.jp/en/bodyparts3d/lic.html. License: https://creativecommons.org/licenses/by-sa/2.1/jp/.

Added 203 bone surfaces, 28 teeth, 37 cartilage surfaces, two sclerae and two irises. These source parts are merged into five non-selectable rendering groups. A rigid registration to 16 corresponding bilateral muscle surfaces aligns the reference anatomy with the Z-Anatomy muscle model without individually stretching bones. Meshes were simplified, coordinates rounded, and illustrative material colors applied. These adapted BodyParts3D surfaces retain their CC BY-SA 2.1 Japan attribution and license. The combined fallback views include both sources.

This surrounding anatomy is for orientation only, is not selectable or assessed, and does not expand the exam topics. Registration is approximate; the added surfaces are not a guide to precise muscle attachment locations.

## Workbook visuals

Muscle photomicrographs: Unit 11, Figures 11.7 and 11.15. Brain views and specimens: Unit 13, Figures 13.6, 13.8 and 13.15. Cranial nerves: Unit 14, Figure 14.3. Surrounding printed labels were cropped or masked, and quiz pins were added. Original schematic study diagrams supplement these figures.

These excerpts are provided for the user's personal study. This notice does not grant public redistribution rights in the workbook figures. Replace them with appropriately licensed assets before a public release.

## Three.js

The runtime bundles Three.js and its OrbitControls add-on. The full MIT license is included below and in the standalone HTML file.

The MIT License

Copyright © 2010-2026 three.js authors

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

Build-only dependencies include esbuild (MIT) and meshoptimizer (MIT). Their package distributions contain their respective license notices. They are not bundled into the study app runtime.
