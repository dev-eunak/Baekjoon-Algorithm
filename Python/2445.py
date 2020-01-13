N = int(input())

for i in range(N):
    print("*"*(i+1) + " "*(N*2-2*(i+1)) + "*"*(i+1))

for i in range(N-1, 0, -1):
    print("*"*i + " "*(N*2-2*i) + "*"*i)
