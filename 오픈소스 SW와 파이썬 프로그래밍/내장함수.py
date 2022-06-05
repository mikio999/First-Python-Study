# all() 함수
mylist = [1,3,4,6]
all(mylist)
print(all(mylist))

mylist = [1,3,4,0]
print(all(mylist))

mylist = [True, 0, False, 0]
print(all(mylist))

#any() 함수
mylist = [0,1,2,3]
print(any(mylist))

mylist = [0,False]
print(any(mylist))

# dir() 함수
print(dir([1,2,3]))

# divmod() 함수
print(divmod(10,3))
x = 27.3
y = 3.5
print(x//y,x%y)
print(divmod(x,y))

# eval() 함수
print(eval("1+2"))

x=1
y=1
print(eval('x+y'))

eval("print('Hi!')")

# exec() 함수
exec("y=2+3")
print(y)

statements = """
import math
def area_of_circle(radius):
    return math.pi*radius*radius
"""
exec(statements)
print(area_of_circle(5))

# float() 함수
#str = input("실수를 입력하시오:")
#print(str)
#value = float(str)
#print(value)

x = 17
print(hex(x)) #16진수
print(oct(x)) #8진수

# max() 함수
values = [1,2,3,4,5]
print(max(values))
print(min(values))

values ={"d":1, "c":2, "b":3, "a":4}
print(max(values))
print(min(values))

# map() 함수
def square(n):
    return n*n

mylist = [1,2,3,4,5]
result = list(map(square, mylist))
print(result)

# filter() 함수
def myfilter(x):
    return x>3
result = filter( myfilter, (1,2,3,4,5,6))
print(list(result))

# 정렬
myList0 = [4,2,3,5,1]
myList1 = sorted(myList0)
print(myList0)
print(myList1)
myList2 = [4,2,3,5,1]
myList2.sort()
print(myList2)