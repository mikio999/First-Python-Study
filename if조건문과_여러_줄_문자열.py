# if 조건문과 여러 줄 문자열(1)
number = int(input("정수입력>"))

# if 조건문으로 홀수 짝수를 구분합니다.
if number % 2 == 0:
    print("""\
        입력한 문자열은 {}입니다.
        {}는(은) 짝수입니다.""".format(number, number))
else:
    print("""\
        입력한 문자열은 {}입니다.
        {}는(은) 홀수입니다.""".format(number,number))

# if 조건문과 여러 줄 문자열(2)
number = int(input("정수 입력>"))
# if 조건문으로 홀수 짝수를 구분합니다.
if number % 2 == 0:
    print("""입력한 문자열은 {}입니다.
{}는(은) 짝수입니다.""".format(number, number))
else:
    print("""입력한 문자열은 {}입니다.
{}는(은) 홀수입니다.""".format(number,number))

# if 조건문과 긴 문자열
# 변수 선언
number = int(input("정수 입력>"))
# if 조건문으로 홀수 짝수를 구분합니다.
if number % 2 == 0:
    print("입력한 문자열은 {}입니다.\n{}는(은) 짝수입니다.".format(number,number))
else:
    print("입력한 문자열은 {}입니다.\n{}는(은) 홀수입니다.".format(number,number))

# 괄호로 문자열 연결하기
    # 변수 선언
test = (
    "이렇게 입력해도"
    "하나의 문자열로 연결되어"
    "생성됩니다."
)

print("test:", test)
print("type(test):", type(test))

# 튜플 자료형의 구분
test_1 = (
    "쉼표로 연결하면",
    "문자열이 아니라",
    "튜플이 생성된답니다."
)
print(test_1)

# 여러 줄 문자열과 if 구문을 조합했을 때의 문제 해결(1)
number = int(input("정수 입력>"))
if number % 2 == 0:
    print((
        "입력한 문자열은 {}입니다.\n"
        "{}는(은) 짝수입니다."
    ).format(number,number))
else:
    print((
        "입력한 문자열은 {}입니다.\n"
        "{}는(은) 홀수입니다."
    ).format(number,number))

# 문자열의 join() 함수
print("::".join(["1","2","3","4","5"]))

# 여러 줄 문자열과 if 구문을 조합했을 때의 문제 해결(2)
number = int(input("정수 입력>"))
if number % 2 == 0:
    print("\n".join([
        "입력한 문자열은 {}입니다.",
        "{}는(은) 짝수입니다."
    ]))
else:
    print("\n".join([
    "입력한 문자열은 {}입니다.",
    "{}는(은) 홀수입니다."
    ]).format(number, number))