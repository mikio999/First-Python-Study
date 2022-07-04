T = int(input())
for i in range(T):
        P, S = input().split()
        for s in S:
            print(s*int(P),end='')
        print()