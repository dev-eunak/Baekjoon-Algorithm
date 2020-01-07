N = int(input())
score = list(map(int, input().split()))

change_score = []
M, avg = 0, 0

for i in range(N):
    if (score[i] > M): M = score[i]

for i in range(N):
    change_score.append(score[i]/M*100)

avg = sum(change_score)/N

print(round(avg, 2))
