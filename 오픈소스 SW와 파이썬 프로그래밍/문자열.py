# 문자열 비교
a = input("문자열을 입력하시오: ")
b = input("문자열을 입력하시오: ")
if (a < b):
    print(a, "가 앞에 있음")
else:
    print(b, "가 앞에 있음")

# 문자열 출력하기
x = 25
y = 98
prod = x*y
print(f"{x}과 {y}의 곱은 {prod}")

# 머리 글자어 만들기
# 머리 글자어(acronym)은 NATO(North Atlantic Treaty Organization)처럼 각 단어의 첫글자를 모아서 만든 문자열이다.
# 사용자가 문장을 입력하면 해당되는 머리 글자어를 출력하는 프로그램을 작성하여 보자.

# 내 답
string = input("문자열을 입력하시오:")
slist = string.split()
acro_list = []
for s in slist:
    acro_list.append(s[0])
acronym="".join(acro_list)
print(acronym)

# 해설
phrase = input("문자열을 입력하시오:")
acronym=""
for word in phrase.upper().split():
    acronym += word[0]
print(acronym)

# 이메일 주소 분석
# 이메일 주소에서 아이디와 도메인을 구분하는 프로그램을 작성하여 보자.
email = input("이메일 주소를 입력하시오:")
id, domain = email.split('@')
print(email)
print("아이디:",id)
print("도메인:", domain)

# 문자열 분석
# 문자열 안에 있는 문자의 개수, 숫자의 개수, 공백의 개수를 계산하는 프로그램을 작성하여 보자.
string = input("문자열을 입력하시오:")
table = {"alphas":0, "digits":0, "spaces":0}
for i in string:
    if i.isdigit():
        table["digits"] += 1
    if i.isalpha():
        table["alphas"] += 1
    if i.isspace():
        table["spaces"] += 1
print(table)
# Lab: 트위터 메시지 처리
# 일반적으로 부정적인 감정은 긍정적인 것보다 적은 양의 단어를 포함한다고 한다.
# 트윗에서 단어의 개수를 추출하여서 발신자의 감정을 판단해보자
t = "Python is very easy and powerful!"
length = len(t.split(" "))
print(length)

# Lab: OTP 발생 프로그램
# 일회용 암호(OTP) 프로그램을 작성해보자
import random
s = "0123456789"
pass_len = 4
p = "".join(random.sample(s,pass_len))
print(p)
