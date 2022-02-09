print("Hello Python Programming")
print( "# 여러개를 출력합니다.")
print("안녕하세요","저의","이름은","미키오입니다!")
print() #줄바꿈
#표현식
#키워드
#식별자
#주석

#자료형(data) : 문자열(string), 숫자(number), 불(boolean)
print("hello")
print('hello')
print()
print('"안녕하세요" 라고 말했습니다')
print("\"안녕하세요\" 라고 말했습니다")
print()

#줄바꿈
print("안녕하세요\n안녕하세요")
#탭
print("안녕하세요\t안녕하세요")
print()

#개인정보 작성하기
print("이름\t나이\t학교\t")
print("미키오\t24\t중앙대")
print()
#역슬래시 출력
print(" \\ \\ \\ \\")
print()
# 여러 줄 문자열 만들기
print("동해물과 백두산이 마르고 닳도록 \n 하느님이 보우하사 우리나라 만세 \n 무궁화 삼천리 화려강산 \n 대한사랑 대한으로 길이 보전하세")
print()
print("""동해물과 백두산이 마르고 닳도록 
하느님이 보우하사 우리나라 만세 
무궁화 삼천리 화려강산 
대한사랑 대한으로 길이 보전하세""")
print()
print("""\
동해물과 백두산이 마르고 닳도록 
하느님이 보우하사 우리나라 만세 
무궁화 삼천리 화려강산 
대한사랑 대한으로 길이 보전하세\
    """)
print("안녕" + "하세요")
print("안녕하세요" + "!")
print("안녕하세요" * 3)
print(3* "안녕하세요")
print("안녕하세요"[0])
print("안녕하세요"[1])
print("안녕하세요"[3])
print("안녕하세요"[-2])
print("안녕하세요"[0:2])
print("안녕하세요"[3:5])
print("안녕하세요"[1:])
print("안녕하세요"[:3])

hello = "안녕하세요"
print(hello)
print(hello[0:2])
hello

print(len("안녕하세요"))
students = ["mikio", "kwawkwak", "yuza", "namo"]
grades = [1, 6, 2, 1]
import statistics
print(statistics.mean(grades))

import random
print(random.choice(students))
print(len("mikio"))

print("0", type(0))
print("0.0", type(0.0))

0.52273e2
print(0.52273e2)
print(0.52273e-2)

print(3//2)
print(5%2)
print(17%13)

#변수형
pi = 3.14159265
pi
print(pi)

# 변수 = 값 -> 값을 변수에 할당한다.
# pi = 3.14159265 -> 3.14159265를 변수 pi에 저장한다.

print(pi + 2)
print(pi - 2)
print(pi * 2)
print(pi / 2)
print(pi % 2)
print(pi * pi)
