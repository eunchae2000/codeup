x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())
a = 0
b = 0
c = 0
d = 0
result = 0

if (x1>x2):
    a = x2
    b = x1
else:
    a = x1
    b = x2

if (y1>y2):
    c = y2
    d = y1
else:
    c = y1
    d = y2

for i in range(a, b+1):
    if(x3 == i):
        for j in range(c, d+1):
            if(y3 == j):
                result = 1
                break

if(result == 1):
    print("충돌")
else:
    print("비충돌")