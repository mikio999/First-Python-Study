# while 반복문
# 무한 반복
# while True:
    # print(".", end ="")
    # "."이 무한하게 반복

# while 반복문 : for 반복문처럼 사용하기
# 반복 변수를 기반으로 반복하기
i = 0
while i < 10:
    print("{}번째 반복입니다.".format(i))
    i += 1

# while 반복문: 상태를 기반으로 반복하기 
list_test = [1,2,1,2]
value = 2

# list_test 내부에 value가 있다면 반복
while value in list_test:
    list_test.remove(value)

print(list_test)

# while 반복문 : 시간을 기반으로 반복하기 
import time
print(time.time())

# 5초 동안 반복하기 
import time
number = 0
target_tick = time.time() + 5
while time.time() < target_tick:
    number += 1

# 출력합니다.
print("5초 동안 {}번 반복했습니다.".format(number))

# while 반복문: break 키워드 / continue 키워드
# 변수를 선언합니다.
i = 0
# 무한 반복합니다.
while True:
    # 몇 번째 반복인지 출력합니다.
    print("{}번째 반복문입니다.".format(i))
    i = i+1
    # 반복을 종료합니다.
    input_text = input("> 종료하시겠습니까? (y/n):")
    if input_text in ["y","Y"]:
        print("반복을 종료합니다.")
        break

# 변수를 선언합니다.
numbers = [5, 15, 6, 20, 7, 25]
for number in numbers:
    # number가 10보다 작으면 다음 반복으로 넘어갑니다.
    if number < 10:
        continue
    print(number)

# 예제 2
key_list = ["name", "hp", "mp", "level"]
value_list = ["기사", 200, 30, 5]
character = {}

for i in range(len(key_list)):
    character[key_list[i]] = value_list[i]
    print(character)

# 예제 3
limit = 10000
i = 1
sum_value = 0
while sum_value < limit:
    sum_value += i
    i += 1
print("{}를 더할 때 {}을 넘으며 그때의 값은 {}입니다.".format(i-1,limit,sum_value))

# 예제 4
max_value = 0
a = 0
b = 0
for i in range(1,101):
    j = 100 - i
    # 최댓값 구하기
    current = i*j
    if max_value<current:
        a = i
        b = j
        max_value = current
print("최대가 되는 경우 : {} * {} = {}".format(a,b,max_value))
