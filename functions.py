import sys
import OpenGL

from OpenGL.GL import *     
from OpenGL.GLU import *    
from OpenGL.GLUT import *
from PIL import Image

import numpy as np
import copy

from numpy import linalg as LA
from numpy.linalg import inv
from numpy.linalg import qr
from numpy.linalg import det
#from numpy.linalg import transpose
from numpy.linalg import norm
from numpy.linalg import matrix_rank

def vect_int(arr):
    rtrn = []
    for k in arr:
        rtrn.append(int(k))
    return rtrn

def vect_float(arr):
    rtrn = []
    for k in arr:
        rtrn.append(float(k))
    return rtrn

def art(mProj):

    A=[0,0,0]
    R=[0,0,0]
    t=[0,0,0]
#    M = np.matrix(self.matrixProjection)
    M = np.matrix(mProj)
    fsign = 1
    s=np.matrix(M[0:3,3])
#   s=np.matrix([[m[0][3]],[m[1][3]],[m[2][3]]])
    Q=inv(M[0:3,0:3])
#   Q=inv(np.matrix([[m[0][0],m[0][1],m[0][2]],\
#                    [m[1][0],m[1][1],m[1][2]],\
#                    [m[2][0],m[2][1],m[2][2]]]))

    (U,B) = qr(Q)

    U = np.matrix(U)
    B = np.matrix(B)



#   print(' P = ', '\n', str(m), '\n')
#   print(' Q = ', '\n', str(Q), '\n')
#   print(' U = ', '\n', str(U), '\n')
#   print(' B = ', '\n', str(B), '\n')

#   for i in range(3):
#       for j in range(3):
#           print(' Q[',str(i),'][',str(j),'] = np.matrix(U[',str(i),'])*np.matrix((B.T)[',str(j),']).T = ',np.matrix(U[i])*np.matrix((B.T)[j]).T)

#   print(' ')
#   print(' U*B = ','\n', str(U*B),'\n')
#   print(' ')
#   print(' np.matrix(U)*np.matrix(B) = ','\n', np.matrix(U)*np.matrix(B),'\n\n')


    sig = (1 if B.item((2,2)) > 0 else (-1 if B((2,2)) < 0 else 0))
    B = B*sig
    s = s*sig

    if(fsign*B.item((0,0)) < 0):
        E = np.matrix([[-1,0,0],[0,1,0],[0, 0, 1]])
        B = E*B
        U = U*E
            
    if(fsign*B.item((1,1)) < 0):
        E = np.matrix([[1,0,0],[0,-1,0],[0, 0, 1]])
        B = E*B
        U = U*E

    if det(U) < 0:
        U = -U
        s = -s


    fSmall = 1e-10                


#   print(' B = ', '\n', str(B), '\n', end='\n')
#   print(' np.matrix(Q)-np.matrix(U)*np.matrix(B) = ', '\n', str(np.matrix(Q)-np.matrix(U)*np.matrix(B)), '\n')
#   print(' np.matrix(Q)+np.matrix(U)*np.matrix(B) = ', '\n', str(np.matrix(Q)+np.matrix(U)*np.matrix(B)), '\n')

    try:
        if(norm(np.matrix(Q)-np.matrix(U)*np.matrix(B)) > fSmall and norm(np.matrix(Q)+np.matrix(U)*np.matrix(B)) > fSmall):
            raise exception
    except:
        print('Something went wrong')

    R = np.transpose(U)
#   R = (np.matrix(U)).transpose()
    t = np.matrix(B)*np.matrix(s)
#   print(' R = ', '\n', str(R), '\n', end='\n')
#   print(' t = ', '\n', str(t), '\n', end='\n')
            
    A = inv(B)
    A = A/A.item((2,2))

#   print(' A = ', '\n', str(A), '\n', end='\n')

    try:
        if(det(R) < 0):
            raise exception
    except:
        print('R is not a rotation matrix')
            

    try:
        if(A.item((2,2)) < 0):
            raise exception
    except:
        print('Wrong sign of A.item((2,2))')

                
#   W = np.matrix(A)*np.matrix([[R[0][0],R[0][1],R[0][2],t[0][0]],\
#                               [R[1][0],R[1][1],R[1][2],t[1][0]],\
#                               [R[2][0],R[2][1],R[2][2],t[2][0]]])
    W = np.matrix(A)*np.concatenate((R, t), axis=1)

    M_col = M.reshape((M.size,1))
    W_col = W.reshape((W.size,1))


#   print(' M_col = ','\n',str(M_col),'\n\n')
#   print(' W_col = ','\n',str(W_col),'\n\n')

#   print(' np.concatenate((M_col,W_col),axis=1) = ', '\n', np.concatenate((M_col,W_col),axis=1), '\n\n')
#   print(' matrix_rank(np.concatenate((M_col,W_col),axis=1)) = ', '\n', matrix_rank(np.concatenate((M_col,W_col),axis=1)), '\n\n')

    try:
        if(matrix_rank(np.concatenate((M_col,W_col),axis=1)) != 1):
            raise exception
    except:
        print('Something wrong with the ART factorization')

                
#   print(' W = ', '\n', str(W), '\n', end='\n')
#   self.matrixA = A
#   self.matrixR = R
#   self.matrixT = t
            
    return (A,R,t)
