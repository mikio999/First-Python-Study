# 끝자리로 짝수와 홀수 구분
number = input("정수 입력>")

# 마지막 자리 숫자를 추출
last_character = number[-1]

# 숫자로 변환하기
last_number = int(last_character)

# 짝수 확인
if last_number == 0 \
    or last_number == 2 \
    or last_number == 4 \
    or last_number == 6 \
    or last_number == 8 :
    print("짝수입니다")

# 홀수 확인
if last_number == 1 \
    or last_number == 3 \
    or last_number == 5 \
    or last_number == 7 \
    or last_number == 9:
    print("홀수입니다")

# if문 두 수 비교하기
A, B = input() .split()
A = int(A)
B = int(B)
if A > B :
    print('>')
elif A < B :
    print('<')
else :
    print('==')

# 나머지 연산자를 활용해서 짝수와 홀수 구분
# 입력을 받습니다.
number = input("정수 입력> ")
number = int(number)

# 짝수 조건
if number % 2 == 0:
    print("짝수입니다.")

# 홀수 조건
if number % 2 == 1:
    print("홀수입니다.")
