import json,base64,io,subprocess,csv
from pathlib import Path
from PIL import Image,ImageDraw
import fitz
imgs={};Path('tmp/clean').mkdir(exist_ok=True)
import numpy as np
from scipy import ndimage as ndi
# Retain the colored anatomical specimens, excluding surrounding printed labels.
# Fill enclosed regions so pale internal tissue and cavities remain unchanged.
def anatomical_crop(im):
 a=np.asarray(im).astype(float);saturation=(a.max(2)-a.min(2))/np.maximum(a.max(2),1)
 mask=(saturation>.12)&(a.max(2)<253)
 mask=ndi.binary_closing(mask,iterations=3)
 lab,num=ndi.label(mask);sizes=np.bincount(lab.ravel());sizes[0]=0
 keep=np.where(sizes>max(2000,sizes.max()*.18))[0]
 mask=np.isin(lab,keep);mask=ndi.binary_fill_holes(mask);mask=ndi.binary_dilation(mask,iterations=2)
 out=np.array(im);out[~mask]=255
 return Image.fromarray(out)
for key in ['brain','brain_model','sheep','cranial']:
 p=next(Path('tmp/figures').glob(key+'.*'));imgs[key]=anatomical_crop(Image.open(p).convert('RGB'))
d=fitz.open('upload/13_ In-Lab _ Top Hat.pdf');b=d.extract_image(52);p=Path('tmp/figures/brain_lateral.png');p.write_bytes(b['image'])
imgs['brain_lateral']=anatomical_crop(Image.open(p).convert('RGB'))
crops={'skeletal':[(160,30,545,440),(690,60,1080,410)],'cardiac':[(180,50,940,465),(230,210,800,470)],'smooth':[(270,45,900,190),(280,200,890,320)]}
for key,boxes in crops.items():
 im=Image.open(next(Path('tmp/figures').glob(key+'.*'))).convert('RGB')
 for i,box in enumerate(boxes):imgs[key+('2' if i else '')]=im.crop(box)
# Course images are included for this user's private study; keep them out of public release builds.
for key,im in imgs.items():
 im.thumbnail((1000,850));im.save('tmp/clean/'+key+'.jpg',quality=90)
 b=io.BytesIO();im.save(b,format='WEBP',quality=88);imgs[key]='data:image/webp;base64,'+base64.b64encode(b.getvalue()).decode()
Path('app/images.json').write_text(json.dumps(imgs))
print('images',len(imgs),'bytes',Path('app/images.json').stat().st_size)
