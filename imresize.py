#Usage: python myresize.py <image> <width> <height>
#Output: images/resized.jpg
 

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
#wait = input("press any key to exit")
