N = int(input())
num_list = list(map(int, input().split()))

M = num_list[0]
m = num_list[0]

for num in num_list:

    if (num > M): M = num
    if (num < m): m = num

print(m, M)
