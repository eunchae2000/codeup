n = int(input())
s = [input() for _ in range(n)]
result = sorted(s, reverse=False)

for i in range(0, n):
    print(result[i])