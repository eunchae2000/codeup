m, d = map(int, input().split())
day = 0
n = m+1

if(m != 10):
    if(m%2 == 0):
        day = 30 - d + 1
    else:
        day = 31 - d + 1
    for i in range(m+1, 10, 1):
        if (i%2 == 0):
            day += 30
        else:
            day += 31
    day += 29

else:
    day = 30 - d
print(day)