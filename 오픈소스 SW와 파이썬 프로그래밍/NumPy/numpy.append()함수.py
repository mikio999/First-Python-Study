import numpy as np
a = np.array([1,2,3])
b = np.array([[4,5,6],[7,8,9]])
np.append(a,b)
print("array([1, 2, 3, 4, 5, 6, 7, 8, 9])")
np.append([a],b,axis=0)
print("array([[1, 2, 3],[4, 5, 6],[7, 8, 9]]")
