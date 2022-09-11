X = int(input())
N = int(input())

sum = 0

for n in range(N):
  a,b = input().split()
  a = int(a)
  b = int(b)
  sum += a*b

if sum == X :
    print("Yes")
else:
    print("No")