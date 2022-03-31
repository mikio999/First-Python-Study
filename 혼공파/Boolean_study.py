# 불은 오직 True, False
print(10 == 100) #같다
print(10 != 100) #다르다
print(10 < 100)
print(10 > 100)
print(10 <= 100)
print(10 >= 100)

#문자열도 적용 가능
print("가방" == "가방")
print("가방" != "연필")
print("가방" < "하마") #사전 순서 기준
print("가방" > "하마")

# 범위 구하기
x = 25
print(10<x<30)
print(40<x<60)

# not 연산자
print(not True)
print(not False)

# not 연산자 조합하기
x = 10
under_20 = x < 20
print("under_20 :" , under_20)
print("not under_20 :", not under_20)

# and 연산자와 or 연산자
print(True and True)
print(True and False)
print(False and True)
print(False and False)
print(True or True)
print(True or False)
print(False or True)
print(False or False)

if True:
    print("True입니다...!")
    print("정말 True입니다...!")

if False:
    print("False입니다...!")

# 조건문의 기본 사용
# 입력을 받습니다.
number = input("정수 입력>")
number = int(number)

# 양수 조건
if number > 0 :
    print("양수입니다")

# 음수 조건
if number < 0 :
    print("음수입니다")

# 0 조건
if number == 0:
    print("0입니다")

print()
# 날짜/시간과 관련된 기능을 가져옵니다.
import datetime

# 현재 날짜/시간을 구합니다.
now = datetime.datetime.now()

# 출력합니다.
print(now.year, "년")
print(now.month, "월")
print(now.day, "일")
print(now.hour, "시")
print(now.minute, "분")
print(now.second, "초")

# 날짜/ 시간을 한 줄로 출력하기
import datetime
now = datetime.datetime.now()
print("{}년 {}월 {}일 {}시 {}분 {}초".format(
    now.year,
    now.month,
    now.day,
    now.hour,
    now.minute,
    now.second
))

# 오전과 오후를 구분하는 프로그램
import datetime
now = datetime.datetime.now()

# 오전 구분
if now.hour < 12 :
    print("현재 시각은 {}시로 오전입니다!" .format(now.hour))

# 오후 구분
if now.hour > 12 :
    print("현재 시각은 {}시로 오후입니다!" .format(now.hour))

# 계절을 구분하는 프로그램
import datetime
now = datetime.datetime.now()

# 봄 구분
if 3 <= now.month <= 5:
    print("이번 달은 {}월로 봄입니다!" .format(now.month))

# 여름 구분
if 6 <= now.month <= 8:
    print("이번 달은 {}월로 여름입니다!" .format(now.month))

# 가을 구분
if 9 <= now.month <= 11:
    print("이번 달은 {}월로 가을입니다!" .format(now.month))

# 겨울 구분
if now.month == 12 or 1 <= now.month <= 2:
    print("이번 달은 {}월로 겨울입니다!" .format(now.month))
