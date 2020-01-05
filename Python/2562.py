M = 0
count = 1

for i in range(1, 10):
    
    N = int(input())
    
    if (N > M):
        M = N
        count = i

print('{0}\n{1}'.format(M, count))
