N = int(input())
score = map(int,input().split())
score = list(score)
max_score = max(score)
fake_score = []
for i in score:
    fake_score.append(i/max_score*100)
final_score=(sum(fake_score)/N)
print(final_score)