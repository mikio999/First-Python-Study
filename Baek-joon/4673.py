numbers = set(range(1,10001))
number_set = set()

for i in range(1, 10001):
    for a in str(i):
        i += int(a)
    number_set.add(i)

final_numbers = numbers - number_set
for final_num in sorted(final_numbers):
    print(final_num)