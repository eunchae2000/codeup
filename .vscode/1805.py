n = int(input())
m = [list(map(int, input().split())) for _ in range(n)]
m.sort(reverse=False)

for i in m:
    for j in i:
        print(j, end= " ")
    print()