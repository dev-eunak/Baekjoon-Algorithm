A = int(input())
B = int(input())
C = int(input())

N = A * B * C
N = str(N)

for i in range(9):
    print(N.count(str(i)))
