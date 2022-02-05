if True:
    print('Good')
if False:
    print('Bad')

if True:
    print('Bad!')
else:
    print('Good!')
x = 15
y = 10
print(x==y)
print(x>y)
print(x>=y)
print(x<y)
print(x<=y)

city = ""
if city:
    print("You are in :", city)
else:
    print("Plz enter your city")
    city = ""
city2 = "Seoul"
if city2:
    print(" You are in:", city2)
else:
    print("Plz enter your city")

a = 75
b = 40
c = 10

print('and :', a>b and b>c)
print('or : ', a>b or b>c)
print('not', not a>b)
print('not', not b>a)
print(not True)
print(not False)