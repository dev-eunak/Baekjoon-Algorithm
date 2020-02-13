T = int(input())

for i in range(T):
    N, M = map(int, input().split())
    print(M*2-N, M-(M*2-N))
