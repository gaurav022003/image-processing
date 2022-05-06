from PIL import Image
import glob
import os

def size():
    lh=list()
    lw=list()
    for i in (glob.glob("input/*.jpg") or glob.glob("input/*.png") or glob.glob("input/*.jfif")):
        img=Image.open(i)
        lh.append(img.height)
        lw.append(img.width)
    print((min(lh),min(lw)))
    return (min(lw),min(lh))


s = tuple(size())
for i in (glob.glob("input/*.jpg") or glob.glob("input/*.png") or glob.glob("input/*.jfif")):
    img=Image.open(i)
    fname, ext = os.path.splitext(i)
    fname =fname.split("\\")[1]
    print(fname)
    if img.mode =='RGB':
        img.save('C:/learn/image processing/rgb/{}.jpg'.format(fname))
        img.resize(s).convert(mode='L').save("C:/learn/image processing/output/{}.jpg".format(fname))
    elif(img.mode=='L'):
        img.save('C:/learn/image processing/black and white/{}.jpg'.format(fname))
        img.resize(s).save("C:/learn/image processing/output/{}.jpg".format(fname))
    else:
        img.save('C:/learn/image processing/none/{}.jpg'.format(fname))
        img.resize(s).convert(mode='L').save("C:/learn/image processing/output/{}.jpg".format(fname))
