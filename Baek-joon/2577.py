A = int(input())
B = int(input())
C = int(input())

output = list(str(A*B*C))
print(list(str(A*B*C)))
for i in range(10):
    print(output.count(str(i)))