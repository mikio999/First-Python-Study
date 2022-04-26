empty_set = set()
for i in range(4):
    number = int((input("Enter an integer:")))
    empty_set.add(number)
print("The max number is", max(empty_set))
empty_set.discard(max(empty_set))
list_set = list(empty_set)
list_set.sort(reverse=True)
print(list_set)