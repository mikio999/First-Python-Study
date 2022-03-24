import random;
player = input("(가위,바위,보) 중에서 하나를 선택하세요:")
number = random.randint(0,2)
if (number == 0):
    computer = "가위"
elif (number == 1):
    computer = "바위"
else:
    computer = "보"
print("사용자:", player, "컴퓨터:",computer)