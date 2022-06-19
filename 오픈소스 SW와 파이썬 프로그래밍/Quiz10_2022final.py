data = {'Frogs':30, 'Hogs':40, 'Dogs':10, 'Logs':20}
print("data = ", data)
data = sorted(data.items(), key=lambda x:x[1])
print("sorted data =", data)

print(iter(range(7)))