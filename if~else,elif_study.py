# if 조건문에 else 구문을 추가해서 짝수와 홀수 구분
number = input("정수 입력>")
number = int(number)
if number % 2 == 0 :
    print("짝수입니다.")
else :
    print("홀수입니다.")

# 계절 구하기
import datetime
now = datetime.datetime.now()
month = now.month
# 조건문으로 계절 확인
if 3 <= month <= 5 :
    print("현재는 봄입니다.")
elif 6 <= month <= 8 :
    print("현재는 여름입니다.")
elif 9 <= month <= 11 :
    print("현재는 가을입니다.")
else:
    print("현재는 겨울입니다.")