# 윤년
year = int(input())
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 :
    print("1")
else:
    print("0")

# 사분면
x = int(input())
y = int(input())

if 0 < x and 0 < y:
    print("1")
if 0 > x and 0 < y:
    print("2")
if 0 > x and 0 > y:
    print ("3")
if 0 < x and 0 > y:
    print ("4")
