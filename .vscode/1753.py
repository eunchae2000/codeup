n = int(input())
s = [input() for _ in range(n)]
result = 0

for i in range(0, n):
    for j in range(len(s[i])-1, -1, -1):
        print(s[i][j], end = "")
    print()