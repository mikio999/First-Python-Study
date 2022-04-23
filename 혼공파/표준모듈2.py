## os 모듈
import os
from urllib import request
# 기본 정보를 몇 개 출력해 봅시다.
print("현재 운영체제:", os.name)
print("현재 폴더:", os.getcwd())
print("현재 폴더 내부의 요소:", os.listdir())

# 폴더를 만들고 제거합니다[폴더가 비어있을 때만 제거 가능].
os.mkdir("hello")
os.rmdir("hello")

# 파일을 생성하고 + 파일 이름을 변경합니다.
with open("original.txt", "w") as file:
    file.write("hello")
os.rename("original.txt", "new.txt")

# 파일을 제거합니다.
os.remove("new.txt")
# os.unlink("new txt")
# 시스템 명령어 실행
os.system("dir")

# datetime 모듈
import datetime
print("# 현재 시각 출력하기")
now = datetime.datetime.now()
print(now.year, "년")
print(now.month, "월")
print(now.day, "일")
print(now.hour, "시")
print(now.minute, "분")
print(now.second, "초")
print()
# 시간 출력 방법
print("시간을 포맷에 맞춰 출력하기")
output_a = now.strftime("%Y.%m.%d %H:%M:%S")
output_b = "{}년 {}월 {}일 {}시 {}분 {}초".format(now.year,\
    now.month,\
    now.day,\
    now.hour,\
    now.minute,\
    now.second)
output_c = now.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}").format(*"년월일시분초") # 문자열, 리스트 등 앞에 *을 붙이면 요소 하나하나가 매개변수로 지정
print(output_a)
print(output_b)
print(output_c)
print()

# 시간 처리하기
import datetime
now = datetime.datetime.now()
# 특정 시간 이후의 시간 구하기
print("#datetime.timedelta로 시간 더하기")
after = now + datetime.timedelta(\
    weeks =1,\
    days = 1,\
    hours = 1,\
    minutes = 1,\
    seconds = 1)
print(after.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}").format(*"년월일시분초"))
print()
# 특정 시간 요소 교체하기
print("# now.replace()로 1년 더하기")
output = now.replace(year=(now.year+1))
print(output.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}").format(*"년월일시분초"))

# time 모듈
import time
print("지금부터 5초 동안 정지합니다!")
time.sleep(5)
print("프로그램을 종료합니다.")

# urllib 모듈
# URL Uniform Resource Locator
from urllib.request import urlopen
response = urlopen("http://www.google.co.kr")
print(response)

from urllib import request
target = request.urlopen("https://google.com")
output = target.read()
print(output)