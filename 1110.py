n = int(input())
num = ncnt = 0

while True:
    a = num//10
    b = num%10
    c = (a+b) % 10
    num = (b*10) + c

    cnt = cnt + 1
    if(num == n):
        break