A, B = input().split()

a = int(''.join(list(reversed(A))))
b = int(''.join(list(reversed(B))))

print(a) if a > b else print(b)
