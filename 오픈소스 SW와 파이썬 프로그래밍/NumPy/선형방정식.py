import numpy as np
a = np.array([[2,3],[1,-2]])
b = np.array([1,4])
x = np.linalg.solve(a,b)
print(x)

# 행렬 곱
a = np.array([1,2,3])
b = np.array([4,5,6])
c =a+b
print(c)

a = ([[1,2],[3,4]])
b = ([[10,20], [30,40]])
print(np.matmul(a,b))
# a[0,0]*b[0,0]+a[0,1]*b[1,0] = 70
# a[0,0]*b[0,1]+a[0,1]*b[1,1] = 100
# a[1,0]*b[0,0]+a[1,1]*b[1,0] = 150
# a[1,0]*b[0,1]+a[1,1]*b[1,1] = 220

a = [[1,2],[3,4]]
b = [[1,0],[0,1]]
print(np.matmul(a,b))