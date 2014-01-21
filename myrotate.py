import SimpleCV
from PIL import Image
import math
def myrotate(I, angle):
    angle = -angle/180.0*math.pi
    cosx = math.cos(angle)
    sinx = math.sin(angle)
    nx,ny = x,y = [I.size[0]/2, I.size[1]/2]
    a = cosx
    b = sinx
    c = x-nx*a-ny*b
    d = -sinx
    e = cosx
    f = y-nx*d-ny*e
    T = I.transform(I.size, Image.AFFINE, (a,b,c,d,e,f), resample=Image.BICUBIC)
    return T
I = Image.open("1.jpg")
I.rotate(40).show()
myrotate(I,40).show()
