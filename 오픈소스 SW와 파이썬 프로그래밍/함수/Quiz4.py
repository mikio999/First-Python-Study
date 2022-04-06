# Quiz4 - Question-1

def avg4(a,b,c,d):
    print("Average of four numbers:",(a+b+c+d)/4)
a = float(input("Please enter a number:"))
b = float(input("Please enter a number:"))
c = float(input("Please enter a number:"))
d = float(input("Please enter a number:"))
avg4(a,b,c,d)

# Quiz4 - Question-2
def maxmin(a,b,c,d):
    print("Max value =",max(a,b,c,d),",","Min value=",min(a,b,c,d))
a= float(input("Please enter a number:"))
b= float(input("Please enter a number:"))
c= float(input("Please enter a number:"))
d= float(input("Please enter a number:"))
maxmin(a,b,c,d)

# Quiz4 - Question-3
def multiply(*values):
    output = 1
    for value in values:
        output *= value
    return output
print("answer =", multiply(7, 3, 5))
print("answer =", multiply(99, 2, 6, 9, 4, 3))
print("answer =", multiply(1, 11, 5, 8, 15, 17, 13, 32, 120, 8, 91))