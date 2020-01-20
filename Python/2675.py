N = int(input())
result = ''

for i in range(N):
    num, words = input().split()
    words = str(words)
    for word in range(len(words)):
        result += (int(num)*words[word])
    if((i+1) < N): result += '\n'

print(result)
