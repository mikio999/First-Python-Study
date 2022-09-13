black_chess = [1,1,2,2,2,8]
white_chess = list(map(int,input().split()))
for i in range(6):
  print(black_chess[i]-white_chess[i], end=' ')