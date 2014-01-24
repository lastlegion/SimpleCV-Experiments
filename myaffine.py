#Usage:
#   python myaffine.py
#Applies tranformation on image: 1.jpg
#Points P0(x0,y0), P1(x1,y1), P2(x2,y2) can be specified in funciton myaffine()#
#Output: newtrans.jpg 

import SimpleCV
import numpy as np
from PIL import Image
import math
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


def myaffine(In, po0,po1,po2):
    dim = I.size()
    x0,y0 =0,0
    x1,y1 = I.width, 0
    x2,y2 = I.width, I.height
    A = np.matrix([[x0,y0,1],[x1,y1,1], [x2,y2,1]])
    
    delta = np.linalg.det(A)    #Find determinant

    #Solve a,b,c using x coordinates
    u1,u2,u3 = po0[0], po1[0], po2[0]   

    #Now U=AX where X = (a,b,c)
    #Solving for a,b,c using cramer's rule

    aMat = np.matrix([[u1,y0,1],[u2,y1,1],[u3,y2,1]])
    a = np.linalg.det(aMat)/delta
    bMat = np.matrix([[x0, u1, 1], [x1,u2,1], [x2,u3,1]])
    b = np.linalg.det(bMat)/delta
    cMat = np.matrix([[x0,y0,u1],[x1,y1,u2], [x2,y2,u3]])
    c = np.linalg.det(cMat)/delta
    
    #Solve e,f,g using y coordinates
    v1,v2,v3 = po0[1],po1[1],po2[1]
    eMat = np.matrix([[v1,y0,1],[v2,y1,1],[v3,y2,1]])
    d = np.linalg.det(eMat)/delta
    fMat = np.matrix([[x0, v1, 1], [x1,v2,1], [x2,v3,1]])
    e = np.linalg.det(fMat)/delta
    gMat = np.matrix([[x0,y0,v1],[x1,y1,v2], [x2,y2,v3]])
    f = np.linalg.det(gMat)/delta
    
    print a,b,c,d,e,f
    return np.matrix([[a,b,c],[d,e,f],[0,0,1]])

def affineTransform(I,T):
    Xs = np.linspace(0,I.width-1,num=I.width)
    Ys = np.linspace(0,I.height-1,num=I.height)
    Inp = I.getNumpy()
    Transformed = np.zeros(Inp.shape)
    for i in range(0,I.width -1):
        for j in range(0, I.height -1):
            P = np.matrix([Xs[i], Ys[j], 1])
            P_ = np.linalg.inv(T)*P.transpose()
            print P_.shape
            x = P_[0].min()
            y = P_[1].min()
            Transformed[i,j] = bilinear(x,y,Inp)
            print bilinear(x,y,Inp).shape
    Transformed = Transformed.transpose([1,0,2]) #Transpose for PIL Image
    return np.uint8(Transformed)
    #return Inp


I = SimpleCV.Image("1.jpg")
T = myaffine(I, [0,0], [I.width*2, 0], [I.width*2,I.height*2])
It = affineTransform(I,T)
print It.shape
Image.fromarray(It).save("newtrans.jpg")

