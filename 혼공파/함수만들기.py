def print_3_times():
    print("안녕하세요")
    print("안녕하세요")
    print("안녕하세요")

print_3_times()

def introduce():
    print("오랜만입니다.")
    print("오랜만입니다.")
    print("오랜만입니다.")
introduce()

def print_n_times(value, n):
    for i in range(n):
        print(value)

print_n_times("안녕하세요",5)

def print_n_times(n, value):
    for i in range(n):
        print(value)
print_n_times(3, '어서와')

def introduction(x, n):
    for i in range(n):
        print(x)
introduction("나는 미키오 입니다.", 6)

# 가변 매개변수
# def 함수 이름(매개변수, 매개변수, ..., *가변 매개변수):

def print_n_times(n,*values):
    # n번 반복합니다.
    for i in range(n):
        # values는 리스트처럼 활용합니다.
        for value in values:
            print(value)
        # 단순한 줄바꿈
        print()

# 함수를 호출합니다.
print_n_times(3, "안녕하세요", "즐거운", "파이썬 프로그래밍","냥냥이")

def play_game(n,*statements): #가변 매개변수
    for i in range(n):
        for statement in statements:
            print(statement)
        print()
play_game(2, "스위치 신작", "스타워즈", "하고싶다", "나울어")

# 기본 매개변수
def print_n_times(value, n=2):
    # n번 반복합니다.
    for i in range(n):
        print(value)
# 함수를 호출합니다.
print_n_times("안녕하세요")

def newgame(x, n=3):
    for i in range(n):
        print(x)
newgame("짱구는못말려")

print()

# 기본 매개변수가 가변 매개변수보다 앞에 올 때
#def print_n_times(n=2, *values):
    #for i in range(n):
       # for value in values:
           # print(value)
       # print()
#print_n_times("안녕하세요", "즐거운", "파이썬 프로그래밍") #type error

# 가변 매개변수가 기본 매개변수보다 앞에 올 때
def print_n_times(*values, n=2):
    for i in range(n):
        for value in values:
            print(value)
        print()
print_n_times("나는","세계최고","익명이",3) #가변 매개변수가 우선시
print()

# 키워드 매개변수 : 매개변수 이름을 지정해서 입력하는 매개변수
def print_n_times(*values, n=2):
    for i in range(n):
        for value in values:
            print(value)
        print()
print_n_times("안녕하세요", "즐거운", "파이썬 프로그래밍", n=3)

# 여러 함수 호출 형태
def test(a, b=10, c=100):
    print(a+b+c)
test(10,20,30)
test(a=10,b=100, c=200)
test(c=10, a=100, b=200)
test(10, c=200)

# input() 함수의 리턴값을 변수에 저장합니다.
value = input(">")
# 출력합니다.
print(value)

# 자료 없이 리턴하기
# 함수를 정의합니다.
def return_test():
    print("A 위치입니다.")
    return
    print("B 위치입니다.")
return_test()

# 자료와 함께 리턴
# 함수 정의
def return_test():
    return 200
# 함수 호출
value = return_test()
print(value)
print(return_test())

# 아무것도 리턴하지 않았을 때의 리턴값
# 함수를 정의
def return_test():
    return
value = return_test()
print(value)

# 기본적인 함수의 활용
# 범위 내부의 정수를 모두 더하는 함수
# 함수 선언
def sum_all(start, end):
# 변수 선언
    output = 0
    # 반복문을 돌려 숫자를 더함
    for i in range(start, end+1):
        output+=i
    return output
# 함수를 호출합니다
print("0 to 100:",sum_all(0,100))
print("0 to 1000:", sum_all(0,1000))
print("50 to 100:", sum_all(50,100))
print("500 to 1000:", sum_all(500,1000))

# 기본 매개변수와 키워드 매개변수를 활용해 범위의 정수를 더하는 함수
def sum_all(start=0, end=100, step=1):
    output = 0
    for i in range(start, end+1, step):
        output += i
    return output
print('A', sum_all(0,100,10))
print('B', sum_all(end=100))
print('C', sum_all(end=100, step=2))

