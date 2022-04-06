C = int(input())
for i in range (C):
    scores = list(map(int,input().split()))
    average = sum(scores[1:])/scores[0]
    output = 0
    for score in scores[1:]:
        if score > average:
            output += 1
    rate =(output/scores[0])*100
    print(f'{rate:.3f}%')