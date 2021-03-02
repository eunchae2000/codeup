n = int(input())
m = list(map(int, input().split()))
m.sort(reverse=True)

for i in range(0, n):
    print(m[i], end = " ")