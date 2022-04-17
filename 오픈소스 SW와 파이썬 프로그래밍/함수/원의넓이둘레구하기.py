# 원의 넓이와 둘레를 동시에 반환하는 함수를 작성, 테스트해보자.
import math
def circle(r):
    area = math.pi * r ** 2
    circum = math.pi * r * 2
    return area, circum

radius = float(input("원의 반지름을 입력하시오:"))
a, c = circle(radius)
print("원의 넓이는{}이고 원의 둘레는 {}이다.".format(a,c))