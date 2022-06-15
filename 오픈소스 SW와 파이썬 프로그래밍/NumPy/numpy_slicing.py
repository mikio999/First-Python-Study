# 배열의 인덱싱 슬라이싱
a = np.array([1,2,3])
print(a[0],a[1],a[2])
print(a[-1],a[-2],a[-3])

a = np.array([1,2,3,4,5])
print(a[np.array([0,1])])
print(a[np.array([0,1,2])])
print(a[np.array([0,1,3])])
print(a[np.array([1,1,1,1])])

# 넘파이 슬라이싱
a = np.array([10,20,30,40,50,60,70,80])
print(a[1:5])
print(a[1:])
print(a[:])
print(a[::2])
print(a[::-1])