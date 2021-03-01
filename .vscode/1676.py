n = int(input())
m = [int(input()) for _ in range(n)]
result = 0

for i in range(0, n):
    result = 1
    for j in range(0, n):
        if m[i]<m[j]:
            result += 1
    print(result)