n = int(input())
m = list(map(int, input().split()))
nn = 0
result = 1

for i in range(0, n):
    result = 1
    for j in range(0, n):
        if(m[i] < m[j]):
            result += 1
    print(m[i], result)
