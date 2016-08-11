import pprint
import scipy
import scipy.linalg   # SciPy Linear Algebra Library

A = scipy.array([[12, -51, 4], [6, 167, -68], [-4, 24, -41]])  # From the Wikipedia Article on QR Decomposition
Q, R = scipy.linalg.qr(A)

print("A:")
print(A)

print("Q:")
print(Q)

print("R:")
print(R)



for i in range(3):
    for j in range(3):
        print(' A[',str(i),'][',str(j),'] = scipy.matrix(Q[',str(i),'])*scipy.matrix((R.T)[',str(j),']).T = ',scipy.matrix(Q[i])*scipy.matrix((R.T)[j]).T)

print(' ')
print(' Q*R = ','\n', str(Q*R),'\n')
print(' ')
print(' scipy.matrix(Q)*scipy.matrix(R) = ','\n', scipy.matrix(Q)*scipy.matrix(R),'\n')
