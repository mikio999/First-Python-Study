# 구의 부피를 계산하는 함수 sphereVolume()을 작성하여 보자. 반지름이 r인 구의 부피는 다음과 같다.
import math
def sphereVolume(r):
    output=(4/3)*math.pi*r*r*r
    return output
r = float(input("구의 반지름을 입력하시오:"))
print(sphereVolume(r))