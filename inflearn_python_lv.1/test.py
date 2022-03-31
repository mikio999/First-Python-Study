print('hello python! 헬로 파이썬!')

# %10s
print ('%10s' % ('window'))
print ('{:>10}' .format ('window'))
print ('%10s' % ('entrepreneursentp'))
print ('{:>10}' .format ('entrepreneursentp'))

print ('%-10s' % ('nice'))
print ('{:10}' .format ('nice'))

print ('{:_>10s}' .format ('nice'))
print ('{:#>10s}' .format ('mikio'))
print ('{:^>30s}' .format ('boys be ambitious'))
print ('{:^30}' .format ('boys be ambitious'))

print ('%.10s' % ('entrepreneurship'))

print ('%10s' % ('window'))
print ('{:>10}' .format ('window'))

print ('%-10s' % ('window'))
print ('{:10}' .format ('window'))

print ('%.5s' % ('widowmaker'))
print ('{:10.5}' .format ('widowmaker'))

# %d
print ('%d %d' % (1,2))
print ('%d %d' % (2,1))
print ('{} {}' .format (1,2))
print ('{} {}' .format (2,1))

str1 = "Python"
bool = True
str2 = "Anaconda"
float = 10.0
int = 7
list = [str1, str2]
dict = {
    "name" : "Machine Learning",
    "version" : 2.0
    }

print(type(str1))
print(type(bool))
print(type(str2))
print(type(float))
print(type(int))
print(type(list))
print(type(dict))

tuple = (7,8,9)
set = {7,8,9}

print(type(tuple))
print(type(set))

i = 77
i2 = -14
big_int = 7777777777777999999999999

print(i)
print(i2)
print(big_int)
print()

f=0.9999
f2=3.141592
f3=-3.9
f4=3/9
print(f)
print(f2)
print(f3)
print(f4)
print()

i=39
i2=939
big_int1=777777777298347298748
big_int2=129874309127409237140
f1=1.234
f2=3.939

print(">>>>+")
print (f1+f2)
print ("i1 + i2 :", i + i2)
print ("f1 + f2 :" , f1 + f2)
print ("big_int1 + big_int2 : ", big_int1 + big_int2)
print (f1-f2)
