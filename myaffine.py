import SimpleCV
import numpy as np
from PIL import Image

def myaffine(In, po0,po1,po2):
    dim = I.size()
#    po1, po2, p03, p04 =  O[0,0][0], O[dim[0]-1, 0][0], O[dim[0]-1,dim[1]-1][0], O[0, dim[1]-1][0]
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
    e = np.linalg.det(eMat)/delta
    fMat = np.matrix([[x0, v1, 1], [x1,v2,1], [x2,v3,1]])
    f = np.linalg.det(fMat)/delta
    gMat = np.matrix([[x0,y0,v1],[x1,y1,v2], [x2,y2,v3]])
    g = np.linalg.det(gMat)/delta
    
    print a,b,c,e,f,g


I = SimpleCV.Image("1.jpg")
myaffine(I, [0,0], [I.width*2, 0], [I.width*2,I.height*2])
