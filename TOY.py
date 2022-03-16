def first_func(w):
    print("Nice to meet you,", w)

word = "mikio"
first_func(word)

def return_func(w1):
    value = "Hello," + str(w1)
    return value

def return_func(w2):
   return "Hello," + str(w2)

x = return_func('Goodboy2')
print(x)

def mul_func(z):
    y1 = z**2
    y2 = z**3
    y3 = z**4
    return y1, y2, y3
a,b,c = mul_func(2)
print(a,b,c)

def mul_func2(z):
    y1 = z**2
    y2 = z**3
    y3 = z**4
    return (y1, y2, y3)
a= mul_func2(2)
print(type(a),a, list(a))

def mul_func3(z):
    y1 = z**2
    y2 = z**3
    y3 = z**4
    return [y1, y2, y3]
b= mul_func3(3)
print(type(b),b,set(b))

def mul_func4(z):
    y1 = z**2
    y2 = z**3
    y3 = z**4
    return {'y1':y1,'y2':y2,'y3':y3}
c = mul_func4(4)
print(type(c),c)