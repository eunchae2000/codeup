a, b, n = map(int, input().split())
c = b-a

for i in range(a, n+1, c):
    print(i, end = " ")