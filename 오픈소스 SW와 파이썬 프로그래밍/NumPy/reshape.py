import numpy as np
# reshape()을 이용한 배열의 재구성
print("np.arange(0,12).reshape(3,4)")
print(np.arange(0,12).reshape(3,4))
print("np.arange(0,12).reshape(4,3)")
print(np.arange(0,12).reshape(4,3))
print("np.arange(0,12).reshape(2,6)")
print(np.arange(0,12).reshape(2,6))
print("np.arange(0,12).reshape(6,2)")
print(np.arange(0,12).reshape(6,2))

# 다른 차원으로의 reshape() 실습
print("np.arange(0,24).reshape(4,3,2)")
a = np.arange(6).reshape(3,2)
print(a)
print("np.transpose(a)")
print(np.transpose(a))

# sum() 함수와 axis에 따른 원소의 합
a = np.arange(0,6).reshape(3,2)
print("np.arange(0,6).reshape(3,2)")
print(a)
print("a.sum()")
print(a.sum())
print("a.sum(axis=0)")
print(a.sum(axis=0))