from __future__ import division
import SimpleCV 
import numpy as np
import math
import sys
def myresize(I,M,N):
    Inp = I.getNumpy()
    InpWidth = Inp.shape[0]
    InpHeight = Inp.shape[1]
    x_ratio = float(InpWidth/M)
    y_ratio = float(InpHeight/N)
    Resize = np.zeros((M,N,3))
    print Resize.shape
    print InpHeight
    print InpWidth
    print x_ratio
    print y_ratio
    
    for x in range(0,M):
        for y in range(0,N):
            px = min(math.floor(x*x_ratio), InpWidth-1)
            py = min(math.floor(y*y_ratio), InpHeight-1)
            Resize[x,y] = Inp[px,py]
    '''
    for x in range(0, N):
        for y in range(0, M):
            px = min(math.floor(x*x_ratio), InpHeight-1)
            py = min(math.floor(y*y_ratio), InpWidth-1)
            print str(x) + " "+ str(y) + " "+ str(px) + " " +str(py)
            Resize[x,y] = Inp[px,py]
    '''
    return Resize
'''
def myresize(I, M,N):
    x_ratio = I.width/M
    y_ratio = I.height/N
    Resized = np.zeros((M,N,3))
    Iarr = I.getNumpy()
    for i in range(0, M-1):
        for j in range(0, N-1):
            px = math.floor(i*(x_ratio+1))
            py = math.floor(j*(y_ratio+1))  
            print str(i) + " " + str(j) + " " +str(px) + " "+ str(py) + " "+ str(I.width) + " " + str(I.height)
            Iarr
            Resized[i,j] = Iarr[px,py] 
    return Resized
'''
if(len(sys.argv)!=4):
    print "Usage: myresize.py <image> <width> <height>"
    exit(0)

I = SimpleCV.Image(sys.argv[1])
print sys.argv[2]
print sys.argv[3]
x = SimpleCV.Image((myresize(I,int(sys.argv[2]), int(sys.argv[3]))))
I.show()
x.show()
x.save("resized.jpg")
wait = input("press any key to exit")
