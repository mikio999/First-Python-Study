# 1
import copy
a = [[1,2,3], [4,5,6]]
b = a
c = [copy.copy(a[0]), copy.copy(a[1])]
b[1][1] = -1
print(a)
print(b)
print(c)
print(a[1])
print(c[1])

#2
import copy
a = ["hello", "world"]
b = list(a)
c = copy.deepcopy(a)
b[1] = "Hong"
print(a)
print(b)
print(c)
# a[1] = "world"
# c[1] = "world"