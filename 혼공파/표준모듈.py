# module 모듈 : 파이썬은 모듈을 활용해 코드를 분리하고 공유
# 모듈은 여러 변수와 함수를 까지고 있는 집합체로 표준 모듈과 외부 모듈로 구분.
# 표준 모듈: 파이썬에 기본적으로 내장되어 있는 모듈
# 외부 모듈: 다른 사람들이 만들어서 꽁개한 모듈
# import 모듈 이름

# 모듈 사용의 기본: math 모듈
import math
print(math.sin(1))
print(math.cos(1))
print(math.tan(1))
print(math.floor(2.5)) # 내림
print(math.ceil(2.5)) # 올림

# from 구문
# from 모듈 이름 import 가져오고 싶은 변수 또는 함수
from math import sin, cos, tan, floor, ceil
print(sin(1))
print(cos(1))
print(tan(1))
print(floor(2.5))
print(ceil(2.5))

# as 구문 - 이름 충돌 방지 or 모듈의 이름을 짧게 줄여서 사용
# import 모듈 as 사용하고 싶은 식별자
import math as m
print(m.sin(1))
print(m.cos(1))
print(m.tan(1))
print(m.floor(2.5))
print(m.ceil(2.5))

# random 모듈 : 랜덤한 값을 생성할 때 사용하는 모듈
import random
print("# random 모듈")
# random() : 0.0 <= x < 1.0 사이의 float를 리턴
print(" - random():", random.random())
# uniform(10,20): 지정한 범위 사이의 float를 리턴
print(" - uniform(10,20):", random.uniform(10, 20))
# randrange(): 지정한 범위의 int를 리턴
# - randrange(max): 0부터 max 사이의 값을 리턴
# - randrange(min, max): min 부터 max 사이의 값을 리턴
print(" - randrange(10):", random.randrange(10))
# choice(list): 리스트 내부에 있는 요소를 랜덤하게 선택
print(" - choice([1,2,3,4,5]):", random.choice([1,2,3,4,5]))
# shuffle(list): 리스트의 요소들을 랜덤하게 섞는다
print(" - shuffle([1,2,3,4,5]):", random.shuffle([1,2,3,4,5]))
# sample(list, k=<숫자>): 리스트의 요소 중에 k개 뽑습니다.
print(" - sample([1,2,3,4,5], k=2)", random.sample([1,2,3,4,5], k=2))
