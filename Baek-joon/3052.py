list_number = []
for i in range(10):
    n = int(input())
    list_number.append(n%42)

set_number = set(list_number)
print(len(set_number))