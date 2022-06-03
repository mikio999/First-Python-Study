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