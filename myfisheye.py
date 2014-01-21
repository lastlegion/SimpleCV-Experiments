import SimpleCV
import numpy as np
import math
from PIL import Image
def myfisheye(I,k):
    newXs = np.zeros((I.size()))
    newYs = np.zeros((I.size()))
    midX = I.width/2
    midY = I.height/2
    rmax = math.sqrt((midX)^2 + (midY)^2)
    i = 0
    j = 0
    FishEye = SimpleCV.Image(Image.fromarray(np.zeros((I.size()[1], I.size()[0]))))
    print FishEye.size()
    for i in range(0,I.width):
        for j in range(0, I.height):
            r = math.sqrt(((midX - i)**2) + ((midY - j)**2))
            #print r
            newXs[i,j] = min( midX+ ((i-midX)/(1+k*(r/rmax))  ),I.width-1)
            newYs[i,j] = min( midY + ((j-midY)/(1+k*(r/rmax))),I.height-1)
    for i in range(0, I.width):
        for j in range(0, I.height):
            FishEye[newXs[i,j],newYs[i,j]] = I[i,j]
    FishEye.show()
    a = raw_input("test")
    print newXs
    print newYs

I = SimpleCV.Image("1.jpg")
myfisheye(I,0.1)
