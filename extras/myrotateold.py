import SimpleCV 
import numpy as np

def myrotate(I, angle):
    Inp = I.getNumpy()
    Rotx = np.zeros(I.size())
    Roty = np.zeros(I.size())
    i=0
    j=0
    for i in range(0, I.width):    #For each row
        for j in range(0, I.height):
            Rotx[i,j] = i*np.cos(angle) - j*np.sin(angle)
            Roty[i,j] = i*np.cos(angle) + j*np.sin(angle)
    Rotated = np.zeros((I.width, I.height, 3))
    for i in range(0, I.width):
        for j in range(0, I.height):
            print str(Rotx[i,j]) + str(Roty[i,j]) + str(i) + str(j)
            Rotated[Rotx[i,j], Roty[i,j]] = I[i,j]
    return Rotated
I = SimpleCV.Image("1.jpg")
I.show()
a = raw_input("enter: ")

R = SimpleCV.Image(myrotate(I, 90))
R.show()
b = raw_input("adsf")
