# OX퀴즈 문제
case_number = int(input())
for i in range(case_number):
    a = input()
    b = list(a)
    score = 0
    sum = 0
    for k in b:
        if k == 'O':
            score += 1
            sum += score
        else:
            score = 0
    print(sum)