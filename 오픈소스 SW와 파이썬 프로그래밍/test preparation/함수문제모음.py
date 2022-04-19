def get_sum(start, end):
    sum = 0
    for i in range(start, end+1):
        sum += i
    return sum
print(get_sum(1,10))
print(get_sum(1,20))

# 생일 축하 메세지 출력하는 함수 happyBirthday()
def happyBirthday():
    print("생일축하 합니다!")
    print("생일축하 합니다!")
    print("사랑하는 친구의", end=" ")
    print("생일축하 합니다!")

happyBirthday()

# Lab: 소수 찾기
def is_prime(n):
    for i in range(2,n):
        if (n%i > 0):
            return True
        else:
            return False
n = int(input("정수를 입력하시오:"))
print(is_prime(n))

# Lab: 구의 부피 계산
import math
def sphereVolume(r):
    return math.pi*r*r*r*(4/3)
r = float(input("구의 반지름을 입력하시오:"))
print(sphereVolume(r))

# Lab: 패스워드 생성기
import random
def genPass():
    alphabet = "abcedfghijklmnopqrstuvwxyz0123456789"
    password = ""

    for i in range(6):
        index = random.randrange(len(alphabet))
        password += alphabet[index]
    return password
print(genPass())