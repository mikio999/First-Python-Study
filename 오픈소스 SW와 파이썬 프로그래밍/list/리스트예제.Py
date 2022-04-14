# zip 함수
questions = ['name','quest', 'color']
answers=['Kim', 'Python','blue']
for q,a in zip(questions, answers):
    print(f"What is your {q}? It is a {a}")

# append method
heroes = []
heroes.append("ironman")
print(heroes)
heroes.append("hulk")
print(heroes)
heroes.append("captain_america")
print(heroes)

# scores = []
# for i in range(5):
    # scores.append(int(input("성적을 입력하시오:")))
# print(scores)

# .insert()
heroes.insert(1,"spiderman")
print(heroes)
heroes.insert(0,"widow")
print(heroes)

# .index()
n = heroes.index("hulk")
print(n)
n = heroes.index("hulk", 1)
print(n)

# pop(i), remove(value)

scores = []
for i in range(5):
    score = int(input("성적을 입력하시오:"))
    scores.append(score)
avg = sum(scores)//len(scores)
print("성적 평균은 {}점 입니다." .format(avg))
total = 0
for x in scores:
    if x >= 80:
        total += 1
    else:
        total += 0
print("80점 이상 성적을 받은 학생은 {}명입니다." .format(total))

# 강아지들 이름 저장하기
dogs = []
while True:
    dog_name = input("강아지의 이름을 입력하시오(종료시에는 엔터키):")
    if dog_name == '':
        break
    dogs.append(dog_name)
print('강아지들의 이름')
print(dogs)
for dog in dogs:
    print(dog_name, end=",")

# 두번째로 큰 수 출력하기
# 정수들이 저장된 리스트에서 두 번째로 큰 수를 찾아보자.
list1 = [1,2,3,56,5,61,7]
list1.sort()
print(list1)
print("두 번째로 큰 수=", list1[-2])

list3 = [5,2,8,4,7,10,3]
list3.sort()
list3.remove((max(list3)))
print(max(list3))

# Lab: 콘테스트 평가
# 심판들의 점수가 리스트에 저장되어 있다고 가정하고 최소값과 최대값을
# 리스트에서 제거하는 프로그램을 작성
alist = [10.0, 9.0, 8.3, 7.1, 3.0, 9.0]
alist.sort()
alist.remove(alist[0])
alist.remove(alist[-1])
print(alist)

blist = [10.0, 9.0, 8.3, 7.1, 3.0, 9.0]
blist.remove(max(blist))
blist.remove(min(blist))
print(blist)

# Lab: 리스트로 스택 흉내내기
# 스택은 데이터 구조 중의 하나로 데이터를 추가한 순서와 삭제하는 순서가 완전히 반대인 데이터 구조.
# 파이썬에는 내장 스택 유형이 없지만, 스택을 리스트로 구현 가능
stack = []
for i in range(3):
    fruit = input("과일을 입력하시오:")
    stack.append(fruit)
for i in range(3):
    print(stack.pop())

    # 얕은 복사, 깊은 복사
temps = [28,31,33,35,27,26,25]
values = list(temps)
print(values[1])

import copy
org1d = [10,20,30]
result1d_A = org1d
result1d_B = org1d[:]
result1d_C = list(org1d)
result1d_D = copy.copy(org1d)
result1d_E = copy.deepcopy(org1d)

result1d_A[1] = 40
print(result1d_A)
print(result1d_B)
print(result1d_C)

import copy
org2d = [[10,20,30],[40,50,60]]
result2d_A = org2d
result2d_B = org2d[:]
result2d_C = list(org2d)
result2d_D = copy.copy(org2d)
result2d_E = copy.deepcopy(org2d)
result2d_A[0][0] = -1
print(result2d_A)
print(result2d_B)
print(result2d_C)
print(result2d_D)
print(result2d_E)
