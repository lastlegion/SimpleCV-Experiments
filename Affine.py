import SimpleCV
import math
from PIL import Image
def ScaleRotateTranslate(image, angle, center = None, new_center = None, scale = None,expand=False):
    if center is None:
        return image.rotate(angle)
    angle = -angle/180.0*math.pi
    nx,ny = x,y = center
    sx=sy=1.0
    if new_center:
        (nx,ny) = new_center
    if scale:
        (sx,sy) = scale
    cosine = math.cos(angle)
    sine = math.sin(angle)
    a = cosine/sx
    b = sine/sx
    c =  x-nx*a-ny*b
    d = -sine/sy
    e = cosine/sy
    f = y-nx*d-ny*e
    return image.transform(image.size, Image.AFFINE, (a,b,c,d,e,f), resample=Image.BICUBIC)

angle = 45
I = Image.open("1.jpg")
I.rotate(angle,Image.BICUBIC,0).show()
a = raw_input("yo")
print I.size
ScaleRotateTranslate(I, angle, [I.size[0]/2,I.size[1]/2]).show()
