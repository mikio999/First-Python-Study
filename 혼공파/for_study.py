# 반복문과 while 반복문

# 범위, 매개변수에 숫자 넣기
a = range(5)
print(a)
list(range(10))
print(list(range(10)))
print(list(range(0,10)))
print(list(range(10)) == list(range(0,10)))

print(list(range(0,5)))
print(list(range(5,10)))

print(list(range(0,10,2)))
print(list(range(0,10,3)))

# 10 포함 강조
a = range(0,10+1)
print(list(a))

# 나누기 연산자 사용 수식
n = 10
# a = range(0, n/2) -> TypeError

a = range(0, n//2)
print(list(a))

# for 반복문: 범위와 함께 사용하기
for i in range(5):
    print(str(i)+"= 반복 변수")
print()

for i in range(5, 10):
    print(str(i)+"= 반복 변수")
print()

for i in range(0, 10, 3):
    print(str(i)+"= 반복 변수")
print()

# for 반복문: 리스트와 범위 조합하기
array = [273, 32, 103, 57, 52]
for element in array:
    print(element)

array = [273, 32, 103, 57, 52]
for i in range(len(array)):
    print("{}번째 반복: {}" .format(i, array[i]))

# for 반복문: 반대로 반복하기
# 역반복문
for i in range(4, 0-1, -1):
    print("현재 반복 변수: {}".format(i))
print()
# reversed 함수 활용 역반복문
for i in reversed(range(5)):
    # 출력합니다.
    print("현재 반복 변수: {}".format(i))
    print(i)

