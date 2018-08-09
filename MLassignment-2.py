#Q1.
import numpy as np
A=np.random.rand(10,1)
print("Mean = ",np.mean(A))

#Q2.
B=np.random.rand(20,1)
print("Variance = ",np.var(B))
print("Standard Deviation = ",np.std(B))

#Q3.
A=np.random.rand(10,20)
B=np.random.rand(20,25)
C=np.dot(A,B)
print("Matrix multiplication,C = ",C)
print("Shape of matrix C = ",C.shape)
print("Sum of all elements of matrix C =",np.sum(C))

#Q4.
import numpy as np
def f(i):
    return( 1 / (1 +( np.exp(-i))))
A=np.random.rand(10,1)
print("Original array =",A)
B=f(A)
print("New array =",B)