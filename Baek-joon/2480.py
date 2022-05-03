A, B, C = input().split()
A = int(A)
B = int(B)
C = int(C)
if A == B == C:
    print(10000 + A*1000)
elif A == B or B == C:
    print(1000 + B*100)
elif A == C:
    print(1000 + A*100)
else:
    print(100*max(A,B,C))

# 2트
A, B, C = map(int,input().split())
if A == B == C:
    print(10000+1000*A)
elif A == B or B == C:
    print(1000 + B*100)
elif A == C:
    print(1000+A*100)
else:
    print(max(A,B,C)*100)

# 리스트
temp = input().split(" ")
list_dice = []
for i in temp:
	list_dice.append(int(i))
	list_dice.sort()
	dice_set = set(list_dice)
	
if len(dice_set)==1 :
	print(10000 + 1000*list_dice[0])
elif len(dice_set)==3:
	print(100*list_dice[-1])
else:
	print(1000*list_dice[1])