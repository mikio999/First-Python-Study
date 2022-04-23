def han_number(N):
    hansu = 0
    for i in range(1,N+1):
        num_list = list(map(int,str(i)))
        if i<100:
            hansu += 1
        elif num_list[2] - num_list[1] == num_list[1] - num_list[0]:
            hansu += 1
    return hansu

N = int(input())
print(han_number(N))