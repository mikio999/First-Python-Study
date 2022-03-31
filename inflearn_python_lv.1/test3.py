i = 77
i2 = -14
big_int = 7777777799999999999

print(i)
print(i2)
print(big_int)

f=0.9999
f2=3.141592
f3=-3.9
f4=3/9

i1=39
i2=939
big_int1=7777777276187638176381
big_int2=1111111111111111111111

print((">>>>+"))
print("i1 + i2 : ", i1+i2)
print("i2 - i1 : ", i1-i2)
print("i1 * i2 : ", i1*i2)
print("i2/i1 : ", i2/i1)

a = 3.
b = 6
c = .7
d = 12.7

print(type(a), type(b), type(c), type(d))

print(float(b))
print(int(c))
print(int(a))
print(int(d))

print(int(True))
print(float(False))
print(int(False))

print(abs(-7))
x, y = divmod(100,8)
print(x, y)
print(pow(5,3), 5**3)

import math
print(math.ceil(5.1))
print(math.pi)

str1 = "I am Python"
str2 = "Python"
str3 = """ How are you?"""
str4 = '''Thank you!'''

print(type(str1), type(str2), type(str3), type(str4))
print(len(str1), len(str2), len(str3), len(str4))

str1_t1 = ''
str2_t2 =str()

print(type(str1_t1), len(str1_t1))
print(type(str2_t2), len(str2_t2))

t_s1 = "Click \t start!"
t_s2 = "New Line \n Check!"
print(t_s1)
print(t_s2)

print("I\'m a boy")
print('a \t b')
print('a \"\" b')

escape_str1 = "Do you have a \"retro games\" ?"
print(escape_str1)

escape_str2 = 'What\'s on TV?'
print(escape_str2)

str_o1 = "Python"
str_o2 = "Apple"
str_o3 = "How are you doing"
str_o4 = "Seoul Daejeon Busan Jinju"

print(str_o1 *3)
print(str_o1 + str_o2)
print('y' in str_o1)
print('z' in str_o1)
print('P' not in str_o1)

print(str(66))
print(str(66), type(str(66)))
print(str(10.1))
print(str(True), type(str(True)))

print("Capitalize :", str_o1.capitalize())
print("ends with? :", str_o2.endswith("s"))
print(str_o2.endswith("e"))
print()
print(str_o1.replace("thon", 'Good'))
print("sorted :", sorted(str_o1))
print("split :", str_o4.split(' '))

str_sl = "Nice Python"
print(str_sl[1:-2])

a=[]
print(type(a))
b=list()
print(type(b))
c=[70,75,80,85]
print(len(c))
d=[1000,10000,'Ace', 'Base', 'Captain']
e=[1000, 10000, ['Ace', 'Base', 'Captain']]
f=[21.42, 'footbar', 3,4, False, 3,14159]

print('>>>>>')
print('d-', d[1])
print('d-', type(d), d)
print('d-', d[0] + d[1]+ d[1])
print('d-', d[-1])

print('e-', e[-1][1])
print('e-', list(e[-1][1]))

print('>>>>>')
print('d-', d[0:3])
print('d-', d[2:])
print('e-', e[-1][1:3])

print('c+d', c+d)
print('c*3', c*3)
print("'Test' + c[0]", 'Test' + str(c[0]))

print('>>>>>')
print('d-', type(d), d)
print('d-', d[1])
print('d-', d[0] + d[1]+ d[1])
print('d-', d[-1])

print(c==c[:3] + c[3:])
print(c)
print(c[:3] + c[3:])

temp = c
print(temp, c)
print(id(temp))
print(id(c))

print('>>>>>')
c[0] = 4
print('c-', c)
c[1:2] = ['a', 'b', 'c']
print(c)
c[1]=['a','b','c']
c[1:3] = []
print('c-', c)
del c[2]
print('c-', c)

a = [5,2,3,1,4]
print('a-', a)
a.append(10)
print('a-', a)
a.sort()
print('a-', a)
a.reverse()
print('a-', a)
print('a-', a.index(3), a[3])
a.insert(2,7)
print('a-',a)
a.reverse()

a.remove(10)
print('a-',a)
print('a-',a.pop())
print('a-',a)
print('a-',a.pop())
print('a-',a)
print('a-',a.count(4))

ex=[8,9]
a.extend(ex)
print('a-',a)

a = ()
b = (1,2)
print (type(a), type(b))
c = (11, 12, 13, 14)
d = (100, 1000, 'Ace', 'Base', 'Captain')
e = (100, 1000, ('Ace','Base', 'Captain'))

print(d[1])
print(d[1]+d[0])
print(d[-1])
print(e[-1])
print(e[-1][-1])
print(list(e[-1][1]))
print(list(e[2][1]))

print('d-', d[0:3])
print(d[2:])
print(e[2][1:3])

print(c+d)
print()

print('c*3', c*3)

a = (5,2,3,1,4)
print('a-',a)
print('a-',a.index(3))
print(a.count(2))

t = ('foo', 'bar', 'baz', 'qux')
print(t)
print(t[0])
print(t[-1])

(x1, x2, x3, x4) = t
print(type(x1), type(x2), type(x3), type(x4))
print(x1, x2, x3, x4)

t2 = (1,2,3)
t3 = 4
x1, x2, x3 = t2
x4, x5, x6 = 4,5,6
print(t2)
print(t3)
print(x1, x2, x3)
print(x4, x5, x6)

t = ('foo', 'bar', 'baz', 'qux')
print(t)
print(t[0])
print(t[-1])

(x1,x2,x3,x4) = t
print(type(x1), type(x2), type(x3), type(x4))
print(x1, x2, x3, x4)

a = {'name' : 'Kim', 'phone' : '01033337777', 'birth' : '870514'}
b = {0 : 'Hello Python'}
c = {
    'Name' : 'Niceman',
    'City' : 'Seoul',
    'Age' : 33,
    'Grade' : 'A',
    'Status' : True
    }

e = dict([
    ('Name', 'Niceman')
    ('City', 'Seoul')
    ('Age', 33)
    ('Grade', 'A')
    ('Status', True)
])

f = dict(
    Name = 'Niceman',
    City = 'Seoul',
    Age = 33,
    Grade = 'A',
    Status = True
)
print('a - ', type(a), a)
print('b - ', type(b), b)
print('c - ', type(c), c)
print('d - ', type(d), d)
print('e - ', type(e), e)
