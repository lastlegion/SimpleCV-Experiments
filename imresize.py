from __future__ import division
import SimpleCV 
import numpy as np
import math
import sys
def myresize(I,M,N,method):
    Inp = I.getNumpy()
    InpWidth = Inp.shape[0]
    InpHeight = Inp.shape[1]
    x_ratio = float(InpWidth/M)
    y_ratio = float(InpHeight/N)
    Resize = np.zeros((M,N,3))
    if method=="pixelrep":
        for x in range(0,M):
            for y in range(0,N):
                px = min(math.floor(x*x_ratio), InpWidth-1)
                py = min(math.floor(y*y_ratio), InpHeight-1)
                Resize[x,y] = Inp[px,py]
    elif method == "bilinear":
        '''
        for i in range(1,M):
            for j in range(1,N):
                x = i*x_ratio
                y = j*y_ratio
                y2 = int(max(math.ceil(x), 1))
                x2 = int(max(math.ceil(y), 1))
                y1 = int(min(math.floor(x), InpWidth -1))
                x1 = int(min(math.floor(y), InpHeight -1))
                print str(x) +"\t"+ str(y) +"\t"+str(x1) +"\t"+str(y1) +"\t"+str(x2) +"\t"+ str(y2) 
                Irval = (1/float((x2-x1)*(y2-y1)))*\
                        ((I[x1,y1][0]*float(x2-x)*float(y2-y)) + \
                        (I[x2,y1][0]*(x-x1)(y2-y1)) + \
                        (I[x1,y2][0]*(x2-x)*(y-y1)) + \
                        (I[x2,y2][0]*(x-x1)*(y-y1)))
                Igval = (1/(x2-x1)*(y2-y1))*\
                        (
                        (I[x1,y1][1]*(x2-x)*(y2-y)) + \
                        I[x2,y1][1]*(x-x1)(y2-y1) + \
                        I[x1,y2][1]*(x2-x)*(y-y1) + \
                        I[x2,y2][1]*(x-x1)*(y-y1))
                Ibval = (1/(x2-x1)*(y2-y1))*\
                        (
                        (I[x1,y1][2]*(x2-x)*(y2-y)) + \
                        I[x2,y1][2]*(x-x1)(y2-y1) + \
                        I[x1,y2][2]*(x2-x)*(y-y1) + \
                        I[x2,y2][2]*(x-x1)*(y-y1))
                Resized[i,j] = [Irval, Igval, Ibval]
            '''
        Inp = I.getNumpy()
        for i in range(0,M):
            x = i*x_ratio
            x1 = min(math.floor(x), InpWidth - 1)
            x2 = min(math.ceil(x), InpWidth - 1)
            if(x2 == 0):
                x2=1
            xint = x%1
            for j in range(0,N):
                y = j*y_ratio
                y1 = min(math.floor(y), InpHeight - 1)
                y2 = min(math.ceil(y), InpHeight -1)
                if(y2 == 0):
                    y2=1
                BL = Inp[x1,y1]
                TL = Inp[x1,y2]
                BR = Inp[x2,y1]
                TR = Inp[x2,y2]
                
                yint = y%1

                R1 = BR*yint + BL*(1-yint)
                R2 = TR*yint + TL*(1-yint)
                
                Resize[i,j] = R1*xint + R2*(1-xint)

    return Resize

if(len(sys.argv)!=4):
    print "Usage: myresize.py <image> <width> <height>"
    exit(0)

I = SimpleCV.Image(sys.argv[1])
print sys.argv[2]
print sys.argv[3]
a = SimpleCV.Image((myresize(I,int(sys.argv[2]), int(sys.argv[3]), "bilinear")))
I.show()
a.show()
a.save("images/resized.jpg")
wait = input("press any key to exit")
