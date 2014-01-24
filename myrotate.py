import SimpleCV
import numpy as np
import math
import Image
def bilinear(x,y,Inp):
    InpWidth = Inp.shape[0]
    InpHeight = Inp.shape[1]
    x1 = min(math.floor(x), InpWidth - 1)
    x2 = min(math.ceil(x), InpWidth - 1)
    if(x2 == 0):
        x2=1
    xint = x%1
    y1 = min(math.floor(y), InpHeight - 1)
    y2 = min(math.ceil(y), InpHeight -1)

    if(y2 == 0):
        y2=1

    #Clipping
    if(x1 == InpWidth -1 and x2 == InpWidth-1):
        return np.matrix([0,0,0])
    if(y1 == InpHeight -1 and y2 == InpHeight - 1):
        return np.matrix([0,0,0])
    if(math.floor(x) < 0):
        return np.matrix([0,0,0])
    if(math.floor(y) < 0):
        return np.matrix([0,0,0])

    BL = Inp[x1,y1]
    TL = Inp[x1,y2]
    BR = Inp[x2,y1]
    TR = Inp[x2,y2]
    
    yint = y%1

    R1 = BR*yint + BL*(1-yint)
    R2 = TR*yint + TL*(1-yint)
    
    return  (R1*xint + R2*(1-xint))


def myrotate(I, angle):
    angle = angle/180.0*math.pi
    cosx = math.cos(angle)
    sinx = math.sin(angle)
    nx,ny = x,y = [I.size()[0]/2, I.size()[1]/2]
    a = cosx
    b = sinx
    c = x-nx*a-ny*b
    d = -sinx
    e = cosx
    f = y-nx*d-ny*e
    T = np.matrix([[a,b,c],[d,e,f],[0,0,1]]) 

    Xs = np.linspace(0,I.width-1,num=I.width)
    Ys = np.linspace(0,I.height-1,num=I.height)

    Inp = I.getNumpy()
    Rotated = np.zeros(Inp.shape)
    for i in range(0,I.width -1):
        for j in range(0, I.height -1):
            P = np.matrix([Xs[i], Ys[j], 1])
            P_ = np.linalg.inv(T)*P.transpose()
            x = P_[0].min()
            y = P_[1].min()
            Rotated[i,j] = bilinear(x,y,Inp)
    print Rotated    
    return Rotated.transpose([1,0,2])


'''
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
'''

I = SimpleCV.Image("1.jpg")
#I.rotate(40).show()
Image.fromarray(np.uint8(myrotate(I,40))).save("newrot.jpg")
#myrotate(I,40).save("images/rotate40.jpg")
