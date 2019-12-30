A, B, C = map(int, input().split())

if (A > B):
    if (A > C): print(max(B, C))
    else: print(A)
else:
    if (B > C): print(max(A, C))
    else: print(B)
