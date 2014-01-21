import SimpleCV
import math
from PIL import Image
def affinescale(image, scale = None):
    if scale:
        (sx,sy) = scale
    print sx,sy
    a = 1/float(sx)
    b = 0
    c = 0
    d = 0
    e = 1/float(sy)
    f = 0
    return image.transform(image.size, Image.AFFINE, (a,b,c,d,e,f), resample=Image.BICUBIC)

I = Image.open("1.jpg")
affinescale(I, [2,2]).show()
