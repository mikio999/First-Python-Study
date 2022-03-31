i1=39
i2=939
big_int1=123382749871249827
big_int2=384729874928749827
f1=1.234
f2=3.939

print("+")
print("i1+i2 : ", i1+i2)
print()

print("i2 - i1 : ", i2 - i1)
print("i2/i1 :" , i2/i1)

i3=12.9
print(i3)
f4=7
print(f4)

a=3.
b=6
c=.7
d=12.7
print(type(a), type(b), type(c), type(d))

print(float(a))
print(int(a))
print(int(d))
print(int(True))
print(int(False))
print(float(True))
print(float(False))
print(complex(3))
print(complex('3'))
print(complex('7.4'))
print(complex(False))

#수치연산 함수
print(abs(-7))
x,y=divmod(100,8)
print(x,y)
print(pow(5,3), 5**3)

import math
print(math.ceil(5.1))
print(math.pi)

str1 = "I am Python"
str2 = 'Python'
str3 = """How are you?"""
str4 = '''Thank you'''

print(type(str1), type(str2), type(str3), type(str4))
print(len(str1), len(str2), len(str3), len(str4))

str_t1 =''
str_t2 =  str()

print(type(str_t1), len(str_t1))
print(type(str_t2), len(str_t2))

# 탭, 줄바꿈
t_s1 = "Click \t start!"
t_s2 = "New Line \n Check!"

print(t_s1)
print(t_s2)

print('I\'m a Boy')
print("I'm a Boy")

print('a \t b')
print('a \n b')
print('a\"\"b')

escape_str1 = "Do you have a \"retro games\"?"
print(escape_str1)

escape_str2 = 'What\'s on TV?'
print(escape_str2)

# 멀티라인 입력
multi_str = '''
mikio
namo
yuza
'''

print(multi_str)

multi_str1 = \
"""
mikio
namo
yuza
"""

print(multi_str1)

str_o1 = "python"
str_o2 = "Apple"
str_o3 = "How are you doing"
str_o4 = "Seoul Daejeon Busan Jinju"
str_o5 = "PineApple"

print(str_o1*3)
print("y" in str_o1)
print(str_o1+str_o2)
print("z" in str_o1)

# 문자열 형 변환
print(str(66))
print(str(66), type(str(66)))
print(str(10.1))
print(str(True), type(str(True)))
print(type(True))
print(True)
print(float(True))
print(int(True))

# 문자열 함수
print("Capitalize :", str_o1.capitalize()) 
print("ends with? :", str_o2.endswith("s"))
print("ends with? :", str_o2 .endswith ("e"))

print("replace", str_o1 .replace("thon", "Good"))
print("sorted",sorted(str_o1))
print("split", str_o4 .split(" "))
print("split", str_o4 .split('!'))

im_str = "Good Boy!"
print(dir(im_str))

for i in im_str :
    print(i)

# 슬라이싱
str_s1 = "Nice Python"
print(len(str_s1))
print(str_s1[0:3])
print(str_s1[0:9:2])
print(str_s1[5:11])
print(str_s1[5:])
print(str_s1[:len(str_s1)])
print(str_s1[:len(str_s1)-1])
print(str_s1[1:-2])
print(str_s1[::2])
print(str_s1[::-1])

n = 700
print(n)
print(n*700)
print(type(n))

x=y=z=700
print(x,y,z)
var = 75
var = "Change Class"
print(var)
print(type(var))

print(300)
print(int(300))
print(str("300"))
print(str(300))

n = 777
print(n, type(n))
m=n
print(type(m), type(n))

m = 400
print(m,n)
print(type(m), type(n))

m=800
n=655
print(id(m))
print(id(n))
print(id(m) == id(n))

m=800
n=800
print(id(m))
print(id(n))
print(id(m) == id(n))

i = 77
i2 = -14
big_int = 7777777779999999999
print(i)
print(i2)
print(big_int)
print()
