# 인수들의 위치에 의해서가 아니고, 키워드, 즉 "매개변수의 이름"을 명시적으로 지정하여, 값을 함수로 전달하는 방식
def sub(x,y,z):
    print("x=",x,"y=",y,"z=",z)
sub(1,2,3)
sub(z=4,y=3,x=1)
sub(1,y=9,z=2)
sub(1,2,z=4)

# 키워드 인수 Lab: 사칙 연산기
# 사칙 연산을 수행하는 4개의 함수(add(), sub(), mul(), div())를 작성한다.
# 이들 함수를 이용하여 10+20*30을 계산하여 보자.
# 함수를 호출할 때, 키워드 인수를 사용하여 호출해보자

def f(x,y,z):
    k = y*z
    print(k+x)

f(10,20,30)

# Solution
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
r1 = mul(a=20, b=30)
r2 = add(a=10, b=r1)
print(r2)