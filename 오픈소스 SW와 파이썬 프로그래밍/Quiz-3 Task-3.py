# Quiz-3 Task-3 다음과 같이 사용자로부터 정수로 나이를 입력받아 20살 이상이면 “Adult", 
# 10살 이상 20살 미 만이면 "Youth", 10살 미만이면 "Kid"를 출력하는 Python 프로그램을 if - elif - else 를 사용하여 작성하시오
age= int(input("나이를 입력하시오:"))
if age>=20:
    print("Adult")
elif 10<=age<20:
    print("Youth")
else:
    print("Kid")